"""Análisis de la escalera O17-F: diferencias contra N=256, bootstrap espacial pareado y
clasificación según PRERREGISTRO_O17F.json.

Uso: python escalera_ns_o17f.py analizar --runs DIR --out DIR
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

NIVELES = (64, 128, 192, 256)
REF = 256
VECTORES = ("om", "tau", "b", "r_nu", "P", "Vc", "Y")
BLOQUES_POR_LADO = 8          # 8^3 = 512 bloques espaciales
B_REPLICAS = 400
SEMILLA_BOOT = 20261019
TOL_REL_MEDIANA = 0.02
TOL_ABS_FRACCION = 0.01
TOL_PUNTUAL = 0.05
BORDES_Q = (0, 1, 2, 3, 4, 5)


# ---------------------------------------------------------------------------
# utilidades
# ---------------------------------------------------------------------------

def norma(x):
    return np.sqrt(np.sum(x * x, axis=0))


def bloque_de(flat, N, m=BLOQUES_POR_LADO):
    i, j, k = np.unravel_index(flat, (N,) * 3)
    return (i * m // N) * m * m + (j * m // N) * m + (k * m // N)


def mediana_ponderada_ordenada(xs, ws):
    """Mediana ponderada con la convención de IB.wquantile, para datos ya ordenados."""
    c = np.cumsum(ws)
    if c[-1] <= 0:
        return np.nan
    c = (c - 0.5 * ws) / c[-1]
    keep = ws > 0
    return float(np.interp(0.5, c[keep], xs[keep]))


class Mediana:
    """Mediana ponderada de una variable en una clase; admite réplicas por bloques en O(n)."""

    def __init__(self, x, w, bloques):
        ok = np.isfinite(x)
        o = np.argsort(x[ok], kind="stable")
        self.x = x[ok][o]
        self.w = w[ok][o]
        self.b = bloques[ok][o]
        self.n = int(self.x.size)

    def valor(self, conteos=None):
        if self.n == 0:
            return np.nan
        w = self.w if conteos is None else self.w * conteos[self.b]
        return mediana_ponderada_ordenada(self.x, w)


class Fraccion:
    """Fracción ponderada sum(w·cond)/sum(w); réplicas por sumas por bloque."""

    def __init__(self, cond, w, bloques, nb=BLOQUES_POR_LADO ** 3):
        self.s1 = np.bincount(bloques, weights=w * cond, minlength=nb)
        self.s0 = np.bincount(bloques, weights=w, minlength=nb)
        self.n = int(np.count_nonzero(w))

    def valor(self, conteos=None):
        c = np.ones_like(self.s0) if conteos is None else conteos
        den = np.dot(c, self.s0)
        return float(np.dot(c, self.s1) / den) if den > 0 else np.nan


# ---------------------------------------------------------------------------
# estadísticas prerregistradas
# ---------------------------------------------------------------------------

def estadisticas(alto, N):
    """Construye los objetos de cada estadística para un nivel (convención del autor: z = q/q_rms del nivel)."""
    z = alto["q"] / float(alto["qrms"])
    w = alto["w"]
    bl = bloque_de(alto["flat"].astype(np.int64), N)
    pos = (alto["a"] > 0) & np.isfinite(alto["rho"])
    clases = {"all_a>0": pos, "q>2qrms": pos & (z > 2), "q>3qrms": pos & (z > 3), "q>4qrms": pos & (z > 4)}
    out = {}
    for c in ("all_a>0", "q>2qrms", "q>3qrms", "q>4qrms"):
        m = clases[c]
        out[f"mediana rho | {c}"] = Mediana(alto["rho"][m], w[m], bl[m])
    m3 = clases["q>3qrms"]
    for var in ("Lam", "Dperp", "cosphi", "sP", "sV", "dlogb_dG"):
        out[f"mediana {var} | q>3qrms"] = Mediana(alto[var][m3], w[m3], bl[m3])
    with np.errstate(invalid="ignore", divide="ignore"):
        trunc = alto["Me"] / alto["bn"]
    out["mediana |e_perp|/|b| | q>3qrms"] = Mediana(trunc[m3], w[m3], bl[m3])
    for nombre, var, signo in (("frac sP>0 | q>3qrms", "sP", 1), ("frac sV<0 | q>3qrms", "sV", -1),
                               ("frac dlogb_dG>0 | q>3qrms", "dlogb_dG", 1)):
        ok = m3 & np.isfinite(alto[var])
        out[nombre] = Fraccion((signo * alto[var][ok] > 0).astype(float), w[ok], bl[ok])
    for lo, hi in zip(BORDES_Q[:-1], BORDES_Q[1:]):
        m = pos & (z >= lo) & (z < hi)
        out[f"P(rho<0.05) | q/qrms en [{lo},{hi})"] = Fraccion((alto["rho"][m] < 0.05).astype(float), w[m], bl[m])
    return out


def tipo(nombre):
    return "fraccion" if nombre.startswith(("frac", "P(")) else "mediana"


def acreditado(delta, ic, ref, clase):
    tol = TOL_ABS_FRACCION if clase == "fraccion" else TOL_REL_MEDIANA * abs(ref)
    contiene_cero = ic[0] <= 0 <= ic[1]
    return bool(contiene_cero or abs(delta) <= tol), bool(contiene_cero), tol


# ---------------------------------------------------------------------------
# análisis
# ---------------------------------------------------------------------------

def cargar(runs):
    runs = Path(runs)
    datos = {}
    for N in NIVELES:
        datos[N] = {
            "comun": dict(np.load(runs / f"comun_N{N}.npz")),
            "alto": dict(np.load(runs / f"alto_N{N}.npz")),
            "diag": json.loads((runs / f"diag_N{N}.json").read_text()),
        }
    return datos


def puntual(datos):
    ref = datos[REF]["comun"]
    z = ref["q"] / float(ref["qrms"])
    filas, clasif = [], {}
    for N in NIVELES[:-1]:
        c = datos[N]["comun"]
        m = (z > 3) & (ref["a"] > 0) & (c["a"] > 0) & np.isfinite(ref["rho"]) & np.isfinite(c["rho"])
        for k in VECTORES:
            with np.errstate(invalid="ignore", divide="ignore"):
                e = norma(c[k] - ref[k]) / norma(ref[k])
            e = e[m & np.isfinite(e)]
            filas.append(dict(N=N, cantidad=k, n=int(e.size), mediana=float(np.median(e)),
                              p90=float(np.percentile(e, 90)), acreditado=bool(np.median(e) <= TOL_PUNTUAL)))
        Lr, Ln = ref["rho"][m] < 0.05, c["rho"][m] < 0.05
        union = int(np.sum(Lr | Ln))
        clasif[N] = dict(n=int(m.sum()), bajo_giro_ref=int(Lr.sum()), bajo_giro_N=int(Ln.sum()),
                         ambos=int(np.sum(Lr & Ln)), jaccard=(float(np.sum(Lr & Ln) / union) if union else np.nan))
    return filas, clasif


def estadistico(datos, B=B_REPLICAS, semilla=SEMILLA_BOOT):
    objs = {N: estadisticas(datos[N]["alto"], N) for N in NIVELES}
    rng = np.random.default_rng(semilla)
    nb = BLOQUES_POR_LADO ** 3
    conteos = rng.multinomial(nb, np.full(nb, 1.0 / nb), size=B).astype(float)
    nombres = list(objs[REF])
    filas = []
    for nombre in nombres:
        v = {N: objs[N][nombre].valor() for N in NIVELES}
        reps = {N: np.array([objs[N][nombre].valor(c) for c in conteos]) for N in NIVELES}
        ref = v[REF]
        lo_r, hi_r = np.nanpercentile(reps[REF], [2.5, 97.5])
        fila = dict(estadistica=nombre, tipo=tipo(nombre), ref_N256=ref, ic95_ref=[float(lo_r), float(hi_r)],
                    n_ref=objs[REF][nombre].n, niveles={})
        deltas = {}
        for N in NIVELES[:-1]:
            d = v[N] - ref
            dr = reps[N] - reps[REF]
            ic = [float(x) for x in np.nanpercentile(dr, [2.5, 97.5])]
            ok, cero, tol = acreditado(d, ic, ref, tipo(nombre))
            deltas[N] = abs(d)
            ic_n = [float(x) for x in np.nanpercentile(reps[N], [2.5, 97.5])]
            fila["niveles"][N] = dict(valor=v[N], ic95=ic_n, delta=d, ic95_delta=ic, acreditado=ok, ic_contiene_0=cero,
                                      tolerancia=tol)
        fila["convergente"] = bool(deltas[64] >= deltas[128] >= deltas[192])
        fila["contenido_del_plano"] = bool(fila["niveles"][192]["acreditado"] and fila["convergente"])
        fila["robusto"] = bool(fila["contenido_del_plano"] and fila["niveles"][128]["acreditado"])
        # Lectura descriptiva posterior al prerregistro (no cambia la clasificación anterior):
        # menor N desde el cual la estadística queda acreditada en todos los niveles más finos.
        desde = None
        for N in (192, 128, 64):
            if all(fila["niveles"][M]["acreditado"] for M in NIVELES[:-1] if M >= N):
                desde = N
        fila["posterior_acreditada_desde_N"] = desde
        filas.append(fila)
    return filas


def comparar_autor(estad, rama):
    """Comparación estadística con las tablas publicadas de la corrida A (N=128, cinco instantes) y A_192."""
    datos = Path(rama) / "data"
    leer = lambda p: list(csv.DictReader(open(p)))  # noqa: E731
    cond = {t: leer(datos / f"budget_{t}_conditional.csv") for t in ("n128", "n192")}
    tail = {t: leer(datos / f"budget_{t}_tail_vs_q.csv") for t in ("n128", "n192")}
    mapa = {"mediana rho | q>3qrms": ("q>3qrms", "rho"), "mediana Lam | q>3qrms": ("q>3qrms", "Lam"),
            "mediana Dperp | q>3qrms": ("q>3qrms", "Dperp"), "mediana cosphi | q>3qrms": ("q>3qrms", "cosphi"),
            "mediana sP | q>3qrms": ("q>3qrms", "sP"), "mediana sV | q>3qrms": ("q>3qrms", "sV"),
            "mediana dlogb_dG | q>3qrms": ("q>3qrms", "dlogb_dG"), "mediana rho | all_a>0": ("all_a>0", "rho")}
    por_nombre = {f["estadistica"]: f for f in estad}
    out = []
    for nombre, (cls, var) in mapa.items():
        fila = dict(estadistica=nombre)
        for t, N in (("n128", 128), ("n192", 192)):
            r = next((x for x in cond[t] if x["cls"] == cls and x["var"] == var), None)
            fila[f"autor_{t}"] = float(r["median"]) if r else None
            fila[f"O17F_N{N}"] = por_nombre[nombre]["niveles"][N]["valor"]
            fila[f"O17F_N{N}_ic95"] = por_nombre[nombre]["niveles"][N]["ic95"]
        out.append(fila)
    for lo, hi in zip(BORDES_Q[:-1], BORDES_Q[1:]):
        nombre = f"P(rho<0.05) | q/qrms en [{lo},{hi})"
        fila = dict(estadistica=nombre)
        for t, N in (("n128", 128), ("n192", 192)):
            r = next((x for x in tail[t] if float(x["q_over_qrms_lo"]) == lo), None)
            fila[f"autor_{t}"] = float(r["P_rho_lt_0p05"]) if r else None
            fila[f"O17F_N{N}"] = por_nombre[nombre]["niveles"][N]["valor"]
            fila[f"O17F_N{N}_ic95"] = por_nombre[nombre]["niveles"][N]["ic95"]
        out.append(fila)
    for fila in out:
        for t, N in (("n128", 128), ("n192", 192)):
            a, ic = fila[f"autor_{t}"], fila[f"O17F_N{N}_ic95"]
            fila[f"autor_{t}_dentro_ic95"] = (None if a is None else bool(ic[0] <= a <= ic[1]))
    return out


def texto(res):
    L = ["O17-F · escalera de resolución, corrida A (ν=0.008), estado común t=15, evolución 0.6, float64", ""]
    L.append("Niveles:")
    for N in NIVELES:
        d = res["diagnosticos"][str(N)]
        L.append(f"  N={N:<4} kmax·η={d['kmax_eta']:.2f}  Re_λ={d['Re_lambda']:.1f}  ε={d['eps']:.4f}  CFL={d['cfl']:.2f}  "
                 f"puntos modo alto={d['n_alto']}")
    L.append("")
    L.append("Puntual en malla común (q>3 q_rms, a>0): mediana |x_N − x_256|/|x_256|  [acreditado si ≤ 0.05]")
    cab = "  cantidad " + "".join(f"   N={N:<6}" for N in NIVELES[:-1])
    L.append(cab)
    for k in VECTORES:
        fila = [f for f in res["puntual"] if f["cantidad"] == k]
        L.append(f"  {k:<8} " + "".join(f"   {f['mediana']:.3f}{'*' if f['acreditado'] else ' '}  " for f in fila))
    L.append("  (* acreditado)")
    L.append("Clasificación individual de bajo giro (ρ<0.05, q>3 q_rms) frente a N=256 — Jaccard:")
    for N, c in res["clasificacion"].items():
        L.append(f"  N={N}: {c['ambos']} en ambos, {c['bajo_giro_N']} en N, {c['bajo_giro_ref']} en N=256 → Jaccard {c['jaccard']:.2f}")
    L.append("")
    L.append("Estadísticas (valor N=256 [IC95]; Δ por nivel; A = acreditado; C = convergente; P = contenido del plano; R = robusto):")
    for f in res["estadistico"]:
        niv = "  ".join(f"N{N}: Δ={f['niveles'][str(N)]['delta']:+.4f}{'A' if f['niveles'][str(N)]['acreditado'] else '·'}"
                        for N in (64, 128, 192))
        marcas = ("C" if f["convergente"] else "·") + ("P" if f["contenido_del_plano"] else "·") + ("R" if f["robusto"] else "·")
        desde = f["posterior_acreditada_desde_N"]
        L.append(f"  {f['estadistica']:<38} {f['ref_N256']:+.4f} [{f['ic95_ref'][0]:+.4f},{f['ic95_ref'][1]:+.4f}]  {niv}  {marcas}"
                 f"  desde N={desde if desde else '—'}")
    L.append("")
    L.append("Reproducción estadística frente a las tablas del autor (corrida A):")
    for f in res["comparacion_autor"]:
        si = lambda b: "dentro" if b else "fuera"  # noqa: E731
        L.append(f"  {f['estadistica']:<38} N128: autor {f['autor_n128']:.4f} / O17F {f['O17F_N128']:.4f} "
                 f"[{f['O17F_N128_ic95'][0]:.4f},{f['O17F_N128_ic95'][1]:.4f}] {si(f['autor_n128_dentro_ic95'])}   "
                 f"N192: autor {f['autor_n192']:.4f} / O17F {f['O17F_N192']:.4f} "
                 f"[{f['O17F_N192_ic95'][0]:.4f},{f['O17F_N192_ic95'][1]:.4f}] {si(f['autor_n192_dentro_ic95'])}")
    return "\n".join(L)


def analizar(runs, out, rama=None):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    rama = rama or Path(__file__).absolute().parents[2] / "03_navier_stokes"
    datos = cargar(runs)
    pf, cl = puntual(datos)
    est = estadistico(datos)
    res = {"diagnosticos": {str(N): datos[N]["diag"] for N in NIVELES}, "puntual": pf,
           "clasificacion": {str(k): v for k, v in cl.items()}, "estadistico": est,
           "comparacion_autor": comparar_autor(est, rama),
           "parametros": dict(B=B_REPLICAS, bloques=BLOQUES_POR_LADO ** 3, semilla=SEMILLA_BOOT,
                              tol_rel_mediana=TOL_REL_MEDIANA, tol_abs_fraccion=TOL_ABS_FRACCION, tol_puntual=TOL_PUNTUAL)}
    res_json = json.loads(json.dumps(res, default=float))
    (out / "RESULTADOS_O17F.json").write_text(json.dumps(res_json, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    t = texto(res_json)
    (out / "RESULTADOS_O17F.txt").write_text(t + "\n", encoding="utf-8")
    print(t)
    return res_json
