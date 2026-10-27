#!/usr/bin/env python3
"""PR-03 — La duplicación con interacción: cadena de Ising que crece por volumen.

Todo se calcula con matrices explícitas en L²(π); ningún resultado se fija a mano.
Ejecutar: python verificar.py   (dependencia: numpy; ~30 s)
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

BETAS = (0.0, 0.5, 1.0, 1.5)
ESPINES = range(1, 11)        # nivel n -> n+1 espines; el último nivel tiene 11 espines = 2048 estados
TOL = 1e-9


# ------------------------------------------------------------------ modelo declarado
def gibbs(m, beta):
    """Cadena abierta de m espines, J=1, sin campo. Sitio k = bit (m-1-k) del índice."""
    x = np.arange(2 ** m)
    s = np.array([[1 - 2 * ((i >> (m - 1 - k)) & 1) for k in range(m)] for i in x])
    e = (s[:, :-1] * s[:, 1:]).sum(1) if m > 1 else np.zeros(len(x))
    w = np.exp(beta * e)
    return w / w.sum()


def operador(m, beta):
    """Baño térmico (heat-bath) en cada sitio, tasa c = π(x^k)/(π(x)+π(x^k)).
    Devuelve S = D^½(−L)D^-½, simétrica y semidefinida positiva, y π."""
    p = gibbs(m, beta)
    M = 2 ** m
    Lg = np.zeros((M, M))
    for x in range(M):
        for k in range(m):
            y = x ^ (1 << (m - 1 - k))
            c = p[y] / (p[x] + p[y])
            Lg[x, y] += c
            Lg[x, x] -= c
    d = np.sqrt(p)
    S = -(d[:, None] * Lg / d[None, :])
    assert np.abs(S - S.T).max() < 1e-12            # reversibilidad respecto de π
    return (S + S.T) / 2, p


def duplicacion(n, beta):
    """J: levantar f(x) a la cadena con un espín más al final; K: base de los modos nuevos.
    En coordenadas simétricas J[(2i+b), i] = sqrt(π(b | i))."""
    pn, pm = gibbs(n, beta), gibbs(n + 1, beta)
    assert np.allclose(pm.reshape(-1, 2).sum(1), pn)   # marginal exacta: el contrato isométrico es exacto
    N = 2 ** n
    J = np.zeros((2 * N, N)); K = np.zeros((2 * N, N))
    for i in range(N):
        a, b = pm[2 * i] / pn[i], pm[2 * i + 1] / pn[i]
        J[2 * i, i], J[2 * i + 1, i] = np.sqrt(a), np.sqrt(b)
        K[2 * i, i], K[2 * i + 1, i] = np.sqrt(b), -np.sqrt(a)
    return J, K, pn, pm


def lap_ciclo(N):
    L = np.zeros((N, N))
    pares = [(i, (i + 1) % N) for i in range(N)] if N > 2 else [(0, 1), (1, 0)]
    for x, y in pares:
        L[x, x] += 1; L[y, y] += 1; L[x, y] -= 1; L[y, x] -= 1
    return L


def ciclo_volumen(N):
    J = np.zeros((2 * N, N)); K = np.zeros((2 * N, N))
    for i in range(N):
        J[i, i] = J[i + N, i] = 1 / np.sqrt(2)
        K[i, i], K[i + N, i] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return J, K


def cota_2x2(a, b, k):
    """(f): mínimo de [[a,-k],[-k,b]]; cota inferior de la brecha con bloques a, b y acoplamiento k."""
    return 0.5 * (a + b) - np.sqrt(0.25 * (b - a) ** 2 + k ** 2)


def medir(Sv, Sn, J, K, vac_v):
    """Todas las medidas del lema para un paso de duplicación."""
    Nv = Sv.shape[0]
    Q, _ = np.linalg.qr(np.column_stack([vac_v, np.eye(Nv)[:, : Nv - 1]]))
    B = J @ Q[:, 1:]                                           # heredados ⊥ vacío
    val, vec = np.linalg.eigh(Sn)
    g = float(val[1])
    E = vec[:, np.abs(val - g) < 1e-8]
    vv, wv = np.linalg.eigh(Sv)
    R = J.T @ Sn @ J - Sv                                      # defecto de herencia de la forma (c = 1)
    out = dict(
        brecha=g,
        brecha_previa=float(vv[1]),
        brecha_heredados=float(np.linalg.eigvalsh(B.T @ Sn @ B)[0]),
        brecha_nuevos=float(np.linalg.eigvalsh(K.T @ Sn @ K)[0]),
        acoplamiento=float(np.linalg.norm(J.T @ Sn @ K, 2)),
        defecto=float(np.linalg.norm(R, 2)),
        multiplicidad_modo_bajo=int(E.shape[1]),
        peso_heredado_modo_bajo=float(np.trace(E.T @ J @ J.T @ E) / E.shape[1]),
    )
    if np.sum(np.abs(vv - vv[1]) < 1e-8) == 1:                # modo bajo previo bien definido
        phi = wv[:, 1]
        out["defecto_efectivo"] = float(phi @ R @ phi)
        out["acoplamiento_efectivo"] = float(np.linalg.norm(K.T @ Sn @ J @ phi))
    out["perdida"] = out["brecha_previa"] - g
    return out


# ------------------------------------------------------------------ medición
salida = {"modelo": "cadena de Ising abierta, J=1, h=0, baño térmico por sitio; duplicación = agregar un espín al final",
          "ising": {}, "control_ciclo_volumen": []}

for beta in BETAS:
    filas, cota_iter = [], None
    for n in ESPINES:
        Sv, pv = operador(n, beta)
        Sn, pn = operador(n + 1, beta)
        J, K, _, _ = duplicacion(n, beta)
        assert np.allclose(J.T @ J, np.eye(2 ** n)) and np.allclose(K.T @ K, np.eye(2 ** n))
        assert np.allclose(J.T @ K, 0) and np.allclose(J @ np.sqrt(pv), np.sqrt(pn))
        assert np.allclose(Sn @ np.sqrt(pn), 0)
        f = medir(Sv, Sn, J, K, np.sqrt(pv))
        a, b, k, e = f["brecha_heredados"], f["brecha_nuevos"], f["acoplamiento"], f["defecto"]
        # lema (a), (b), (e) con c = 1, (f)
        assert f["brecha"] <= min(a, b) + TOL
        assert f["brecha"] >= min(a, b) - k - TOL
        assert a >= f["brecha_previa"] - e - TOL
        assert f["brecha"] >= cota_2x2(a, b, k) - TOL
        assert f["brecha"] >= cota_2x2(f["brecha_previa"] - e, b, k) - TOL
        # cota iterada: sólo usa la brecha del nivel inicial y las normas de operador
        cota_iter = f["brecha_previa"] if cota_iter is None else cota_iter
        cota_iter = float(cota_2x2(cota_iter - e, b, k))
        f["cota_iterada_por_normas"] = cota_iter
        f["espines"] = n + 1
        filas.append(f)
    lim = 1 - np.tanh(2 * beta)
    m = float(-np.log(np.tanh(beta))) if beta > 0 else None
    Ns = np.array([r["espines"] for r in filas[-4:]], float)
    G = np.array([r["brecha"] for r in filas[-4:]])
    A = np.column_stack([np.ones(4), (Ns + 1) ** -2.0, (Ns + 1) ** -3.0])
    extrap = float(np.linalg.lstsq(A, G, rcond=None)[0][0])
    perd = np.array([r["perdida"] for r in filas[-3:]])
    expo = float(-np.polyfit(np.log(Ns[-3:]), np.log(perd), 1)[0]) if beta > 0 else None
    salida["ising"][str(beta)] = dict(
        limite_volumen_infinito_exacto_Glauber_1963=float(lim),
        masa_matriz_de_transferencia=m,
        longitud_de_correlacion=(1 / m if m else 0.0),
        extrapolacion_desde_11_espines=extrap,
        exponente_de_la_perdida_por_nivel=expo,
        filas=filas,
    )

# control sin brecha: ciclo por volumen (PR-02), mismas medidas
for n in ESPINES:
    N = 2 ** n
    J, K = ciclo_volumen(N)
    f = medir(lap_ciclo(N), lap_ciclo(2 * N), J, K, np.ones(N) / np.sqrt(N))
    f["puntos"] = 2 * N
    salida["control_ciclo_volumen"].append(f)

# ------------------------------------------------------------------ comprobaciones de alcance
I0 = salida["ising"]["0.0"]["filas"]
assert all(abs(r["brecha"] - 1) < TOL and r["acoplamiento"] < TOL and r["defecto"] < TOL for r in I0)   # = hipercubo
for beta in BETAS[1:]:
    d = salida["ising"][str(beta)]
    F = d["filas"]
    lim = d["limite_volumen_infinito_exacto_Glauber_1963"]
    assert all(r["brecha"] > lim for r in F)                                          # por encima del límite
    assert all(F[i]["brecha"] > F[i + 1]["brecha"] for i in range(len(F) - 1))        # decrece con el volumen
    assert max(r["defecto"] for r in F[1:]) - min(r["defecto"] for r in F[1:]) < 1e-12        # normas constantes
    assert max(r["acoplamiento"] for r in F[1:]) - min(r["acoplamiento"] for r in F[1:]) < 1e-12
    assert all(abs(r["brecha_nuevos"] - 1 - r["defecto"]) < 1e-10 for r in F)          # observado: γ_nue = 1 + ε
    assert all(r["peso_heredado_modo_bajo"] > 0.85 for r in F[1:]) and F[-1]["peso_heredado_modo_bajo"] > 0.99
    ef = [abs(r["defecto_efectivo"]) for r in F[1:]]; ka = [r["acoplamiento_efectivo"] for r in F[1:]]
    assert all(ef[i] > ef[i + 1] for i in range(len(ef) - 1)) and all(ka[i] > ka[i + 1] for i in range(len(ka) - 1))
    assert F[-1]["acoplamiento_efectivo"] < 0.1 * F[-1]["acoplamiento"]
    assert F[-1]["cota_iterada_por_normas"] < 0 < F[-1]["brecha"]                   # las normas no alcanzan
C = salida["control_ciclo_volumen"]
assert all(r["acoplamiento"] < TOL and r["defecto"] < TOL for r in C)
assert C[-1]["brecha"] < 1e-5 and all(r["peso_heredado_modo_bajo"] < 1e-9 for r in C)

root = Path(__file__).resolve().parent
(root / "resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# ------------------------------------------------------------------ informe
for beta in BETAS:
    d = salida["ising"][str(beta)]
    print(f"\nβ={beta}: límite exacto {d['limite_volumen_infinito_exacto_Glauber_1963']:.6f}"
          + (f" · masa {d['masa_matriz_de_transferencia']:.4f} · ξ {d['longitud_de_correlacion']:.1f} sitios"
             f" · extrapolado {d['extrapolacion_desde_11_espines']:.6f}" if beta else ""))
    print(f"{'esp':>3} {'brecha':>9} {'her':>9} {'nue':>7} {'κ':>6} {'ε':>6} {'κ_ef':>8} {'ε_ef':>9} {'pérdida':>9} {'peso':>6} {'cota_it':>8}")
    for r in d["filas"]:
        print(f"{r['espines']:>3} {r['brecha']:>9.6f} {r['brecha_heredados']:>9.6f} {r['brecha_nuevos']:>7.4f} "
              f"{r['acoplamiento']:>6.3f} {r['defecto']:>6.3f} {r.get('acoplamiento_efectivo', float('nan')):>8.2e} "
              f"{r.get('defecto_efectivo', float('nan')):>9.2e} {r['perdida']:>9.2e} {r['peso_heredado_modo_bajo']:>6.3f} "
              f"{r['cota_iterada_por_normas']:>8.4f}")
print("\ncontrol ciclo por volumen:")
for r in C:
    print(f"{r['puntos']:>5} brecha {r['brecha']:.6f}  nuevos {r['brecha_nuevos']:.6f}  peso heredado {r['peso_heredado_modo_bajo']:.3f}")
print("\nOK: todas las aserciones pasaron. No es una prueba de brecha de Yang-Mills.")
