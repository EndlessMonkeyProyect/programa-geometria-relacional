"""O17-F — Escalera de resolución del presupuesto de vorticidad material (Navier–Stokes).

Reutiliza sin modificar el solucionador y el presupuesto de la rama:
03_navier_stokes/scripts/dns_forced_isotropic.py e instantaneous_budget.py.

Subcomandos (los estados pesados quedan fuera del paquete):

  spinup  --runs DIR                      N=64 hasta t=10, luego N=128 hasta t=15 (float64)
  nivel   --runs DIR --N 64|128|192|256   evoluciona 0.6 desde el estado común y evalúa el presupuesto
  analizar --runs DIR --out DIR           diferencias contra N=256, bootstrap espacial, clasificación

Criterios fijados en PRERREGISTRO_O17F.json antes de correr.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

AQUI = Path(__file__).absolute()
RAMA = AQUI.parents[2] / "03_navier_stokes" / "scripts"
sys.path.insert(0, str(RAMA))
from dns_forced_isotropic import (Spectral, diagnostics, initial_field, load_state,  # noqa: E402
                                  refine, run, save_state, step)
import instantaneous_budget as IB  # noqa: E402

NU, EPS_IN, KF, SEMILLA = 0.008, 0.1, 2.0, 20261004
T_EVOL, DT = 0.6, 4e-3
NIVELES = (64, 128, 192, 256)
VECTORES = ("om", "tau", "b", "r_nu", "P", "Vc", "Y")


def log(runs, msg):
    linea = f"{time.strftime('%H:%M:%S')} {msg}"
    print(linea, flush=True)
    with open(Path(runs) / "progreso.log", "a") as fh:
        fh.write(linea + "\n")


def coarsen(U, N_from, N_to):
    """Truncamiento espectral a una malla más gruesa (modos dentro de la máscara 2/3 del destino)."""
    sp_to = Spectral(N_to)
    h, nz = N_to // 2, N_to // 2 + 1
    V = np.zeros((3, N_to, N_to, nz), dtype=complex)
    V[:, :h, :h, :] = U[:, :h, :h, :nz]
    V[:, -h:, :h, :] = U[:, -h:, :h, :nz]
    V[:, :h, -h:, :] = U[:, :h, -h:, :nz]
    V[:, -h:, -h:, :] = U[:, -h:, -h:, :nz]
    return V * (N_to / N_from) ** 3 * sp_to.mask


def cmd_spinup(runs):
    runs = Path(runs)
    meta = dict(nu=NU, eps_in=EPS_IN, kf=KF, seed=SEMILLA)
    sp = Spectral(64)
    U = initial_field(sp, seed=SEMILLA)
    log(runs, "spinup N=64 hasta t=10")
    U, t = run(sp, U, 0.0, 10.0, NU, EPS_IN, KF, 0.4, [], str(runs / "n64"), dict(meta, N=64))
    log(runs, f"N=64 listo t={t:.3f}; refinando a 128")
    sp = Spectral(128)
    U = refine(U, 64, 128)
    U, t = run(sp, U, t, 15.0, NU, EPS_IN, KF, 0.4, [15.0], str(runs / "n128"), dict(meta, N=128))
    log(runs, f"N=128 listo t={t:.3f}")


def puntos_comunes(N):
    m = np.arange(64)
    I, J, K = np.meshgrid(m, m, m, indexing="ij")
    s = N // 64
    return (s * I.ravel(), s * J.ravel(), s * K.ravel())


def cmd_nivel(runs, N):
    runs = Path(runs)
    U0, t0, meta0 = load_state(str(runs / "n128" / "state_t015.000.npz"))
    U0 = U0.astype(np.complex128)
    sp = Spectral(N)
    U = coarsen(U0, 128, N) if N < 128 else (U0 if N == 128 else refine(U0, 128, N))
    del U0
    pasos = int(round(T_EVOL / DT))
    log(runs, f"N={N}: evolución de {pasos} pasos")
    tw = time.time()
    umax = 0.0
    for i in range(pasos):
        U, umax = step(sp, U, DT, NU, EPS_IN, KF)
        if (i + 1) % 25 == 0:
            log(runs, f"N={N}: paso {i + 1}/{pasos}")
    seg_evol = time.time() - tw
    diag = diagnostics(sp, U, NU)
    diag.update(N=N, t=t0 + T_EVOL, evolve_seconds=seg_evol, umax=float(umax),
                cfl=float(umax * DT / (2 * np.pi / N)))
    qrms = float(np.sqrt(sp.enstrophy(U)))
    diag["qrms"] = qrms
    log(runs, f"N={N}: evolución lista ({seg_evol:.0f} s), kmax_eta={diag['kmax_eta']:.3f}, CFL={diag['cfl']:.3f}")

    # 1) malla común 64^3
    tw = time.time()
    g = IB.budget(sp, U, NU, EPS_IN, KF, sel=puntos_comunes(N))
    o = IB.observables(g)
    comun = {k: g[k].astype(np.float64) for k in VECTORES}
    comun.update({k: o[k].astype(np.float64) for k in ("q", "a", "rho", "bn", "Me")})
    np.savez_compressed(runs / f"comun_N{N}.npz", qrms=qrms, **comun)
    del g, o, comun
    log(runs, f"N={N}: presupuesto en malla común ({time.time() - tw:.0f} s)")

    # 2) modo alto del autor (q>2 qrms completo + 2 % uniforme)
    tw = time.time()
    sel_hi, w = IB.select_high(sp, U, qrms)
    flat = np.ravel_multi_index(sel_hi, (N,) * 3)
    acc = {}
    for c0 in range(0, flat.size, IB.CHUNK):
        sl = slice(c0, c0 + IB.CHUNK)
        sel = np.unravel_index(flat[sl], (N,) * 3)
        o = IB.observables(IB.budget(sp, U, NU, EPS_IN, KF, sel=sel))
        for k in IB.KEEP:
            acc.setdefault(k, []).append(o[k].astype(np.float64))
        log(runs, f"N={N}: bloque alto {c0 // IB.CHUNK + 1}/{(flat.size + IB.CHUNK - 1) // IB.CHUNK}")
    alto = {k: np.concatenate(v) for k, v in acc.items()}
    np.savez_compressed(runs / f"alto_N{N}.npz", qrms=qrms, w=w, flat=flat, N=N, **alto)
    diag["n_alto"] = int(flat.size)
    diag["budget_seconds"] = time.time() - tw
    with open(runs / f"diag_N{N}.json", "w") as fh:
        json.dump({k: (float(v) if isinstance(v, (np.floating, float)) else v) for k, v in diag.items()}, fh, indent=1)
    log(runs, f"N={N}: listo ({diag['budget_seconds']:.0f} s de presupuesto en modo alto)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("spinup")
    a.add_argument("--runs", required=True)
    b = sub.add_parser("nivel")
    b.add_argument("--runs", required=True)
    b.add_argument("--N", type=int, choices=NIVELES, required=True)
    c = sub.add_parser("analizar")
    c.add_argument("--runs", required=True)
    c.add_argument("--out", required=True)
    args = ap.parse_args()
    os.makedirs(args.runs, exist_ok=True)
    if args.cmd == "spinup":
        cmd_spinup(args.runs)
    elif args.cmd == "nivel":
        cmd_nivel(args.runs, args.N)
    else:
        from analisis_o17f import analizar
        analizar(args.runs, args.out, rama=RAMA.parent)


if __name__ == "__main__":
    main()
