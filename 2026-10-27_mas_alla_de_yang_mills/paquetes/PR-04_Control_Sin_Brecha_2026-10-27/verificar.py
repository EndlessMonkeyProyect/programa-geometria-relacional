#!/usr/bin/env python3
"""PR-04 — El control que puede fallar: interacción sin brecha (Ising 2D crítico y de baja temperatura).

Todo se calcula con matrices dispersas explícitas en L²(π); ningún resultado se fija a mano.
Ejecutar:  python verificar.py            (completo, hasta 20 espines en 2D; ~10 min; escribe resultados.json)
           python verificar.py --rapido   (hasta 16 espines; ~1 min; no escribe resultados)
Dependencias: numpy, scipy.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

RAPIDO = "--rapido" in sys.argv
N2D = 16 if RAPIDO else 20
N1D = 16
BETA_C = 0.5 * np.log(1 + np.sqrt(2))                     # punto crítico de Ising 2D (Onsager)
BETAS_2D = {"alta_T": 0.25, "critico": float(BETA_C), "baja_T": 0.6}
BETAS_1D = {"1D_beta_0.5": 0.5, "1D_beta_1.5": 1.5}
TOL = 1e-8


# --------------------------------------------------------------------- geometría y modelo
def orden_cuadrado(n):
    """Cada prefijo de longitud k² es un cuadrado k×k y cada prefijo k(k+1) un rectángulo k×(k+1)."""
    o, k = [(0, 0)], 1
    while len(o) < n:
        o += [(r, k) for r in range(k)]
        o += [(k, c) for c in range(k + 1)]
        k += 1
    return o[:n]


def orden_cadena(n):
    return [(0, c) for c in range(n)]


def aristas(orden, N):
    pos = {q: i for i, q in enumerate(orden[:N])}
    return [(i, pos[q]) for i, (r, c) in enumerate(orden[:N]) for q in ((r + 1, c), (r, c + 1)) if q in pos]


def operador(N, E, beta):
    """S = D^½(−L)D^-½ del baño térmico; el espín k es el bit k (el más nuevo es el bit más alto)."""
    M = 2 ** N
    x = np.arange(M, dtype=np.int64)
    s = 1 - 2 * ((x[:, None] >> np.arange(N)) & 1)
    e = np.zeros(M)
    for i, j in E:
        e += s[:, i] * s[:, j]
    w = np.exp(beta * (e - e.max()))
    p = w / w.sum()
    filas, cols, vals, diag = [], [], [], np.zeros(M)
    for k in range(N):
        y = x ^ (1 << k)
        c = 1.0 / (1.0 + np.exp(beta * (e - e[y])))        # tasa x→y; la recíproca es 1−c
        diag += c
        filas.append(x); cols.append(y); vals.append(-np.sqrt(c * (1 - c)))
    filas.append(x); cols.append(x); vals.append(diag)
    S = sp.csr_matrix((np.concatenate(vals), (np.concatenate(filas), np.concatenate(cols))), shape=(M, M))
    return S, p


def duplicacion(p_sig, N):
    """J levanta funciones de los primeros N espines; es isometría desde L²(μ), μ = marginal de π_(N+1)."""
    M = 2 ** N
    p0, p1 = p_sig[:M], p_sig[M:]
    mu = p0 + p1
    a, b = p0 / mu, p1 / mu
    i = np.arange(M)
    r, c = np.concatenate([i, i + M]), np.concatenate([i, i])
    J = sp.csr_matrix((np.concatenate([np.sqrt(a), np.sqrt(b)]), (r, c)), shape=(2 * M, M))
    K = sp.csr_matrix((np.concatenate([np.sqrt(b), -np.sqrt(a)]), (r, c)), shape=(2 * M, M))
    return J, K, mu


def bajos(A, k):
    if A.shape[0] <= 2048:
        v, w = np.linalg.eigh(A.toarray())
        return v[:k], w[:, :k]
    v0 = np.random.default_rng(20261027).standard_normal(A.shape[0])   # arranque fijo: resultados reproducibles
    v, w = eigsh(A, k=k, which="SA", tol=1e-12, ncv=max(4 * k, 40), v0=v0)
    o = np.argsort(v)
    return v[o], w[:, o]


def norma2(X):
    if X.shape[0] <= 2048:
        return float(np.linalg.norm(X.toarray(), 2))
    # norma espectral = raíz del mayor autovalor de XᵀX; tolerancia alcanzable en doble precisión
    G = (X.T @ X).tocsr()
    v0 = np.random.default_rng(20261027).standard_normal(G.shape[0])
    lam = eigsh(G, k=1, which="LA", tol=1e-12, ncv=20, v0=v0, return_eigenvectors=False)[0]
    return float(np.sqrt(max(lam, 0.0)))


def cota_2x2(a, b, k):
    return 0.5 * (a + b) - np.sqrt(0.25 * (b - a) ** 2 + k ** 2)


# --------------------------------------------------------------------- medición de una serie
def serie(orden, beta, Nmax):
    filas = [dict(espines=1, brecha=1.0)]                 # un espín aislado: brecha 1 a todo β
    p_prev = np.array([0.5, 0.5])
    for N in range(1, Nmax):
        S, p = operador(N + 1, aristas(orden, N + 1), beta)
        J, K, mu = duplicacion(p, N)
        v, w = bajos(S, 3)
        g = float(v[1])
        Ew = w[:, np.abs(v - g) < 1e-7]
        H = (J.T @ S @ J).tocsr()
        vh, wh = bajos(H, 2)
        X = (J.T @ S @ K).tocsr()
        f = dict(
            espines=N + 1,
            brecha=g,
            brecha_heredados=float(vh[1]),
            brecha_nuevos=float(bajos((K.T @ S @ K).tocsr(), 1)[0][0]),
            acoplamiento=norma2(X),
            acoplamiento_efectivo=float(np.linalg.norm(X.T @ wh[:, 1])),   # sobre el mejor modo heredado
            peso_heredado_modo_bajo=float(np.sum(np.asarray(J.T @ Ew) ** 2) / Ew.shape[1]),
            cambio_de_lo_heredado_TV=float(0.5 * np.abs(mu - p_prev).sum()),  # 0 si la marginal es exacta
            perdida_log=float(np.log(filas[-1]["brecha"] / g)),
        )
        # lema (a), (b), (f) en cada nivel
        a, b, k = f["brecha_heredados"], f["brecha_nuevos"], f["acoplamiento"]
        assert np.allclose(J @ np.sqrt(mu), np.sqrt(p)) and abs(S @ np.sqrt(p)).max() < 1e-10
        assert g <= min(a, b) + TOL and g >= min(a, b) - k - TOL and g >= cota_2x2(a, b, k) - TOL
        filas.append(f)
        p_prev = p
    return filas


def exponente_efectivo(filas, puntos, d):
    """z_ef entre puntos de control consecutivos: pérdida log por log del lado L = N^(1/d)."""
    g = {f["espines"]: f["brecha"] for f in filas}
    out = []
    for n1, n2 in zip(puntos[:-1], puntos[1:]):
        out.append(dict(de=n1, a=n2, z_ef=float(np.log(g[n1] / g[n2]) / (np.log(n2 / n1) / d))))
    return out


# --------------------------------------------------------------------- cálculo
salida = {"rapido": RAPIDO, "beta_critico": float(BETA_C), "series_2D": {}, "series_1D": {}, "ciclo": []}
# Se compara forma con forma: cuadrados (1, 4, 9, 16) y rectángulos k×(k+1) (2, 6, 12, 20) por separado,
# porque pasar de cuadrado a rectángulo y de rectángulo a cuadrado no son pasos equivalentes.
CUADRADOS = [n for n in (1, 4, 9, 16) if n <= N2D]
RECTANGULOS = [n for n in (2, 6, 12, 20) if n <= N2D]
for nombre, beta in BETAS_2D.items():
    F = serie(orden_cuadrado(N2D), beta, N2D)
    salida["series_2D"][nombre] = dict(beta=beta, filas=F,
                                       z_ef_cuadrados=exponente_efectivo(F, CUADRADOS, 2),
                                       z_ef_rectangulos=exponente_efectivo(F, RECTANGULOS, 2))
    print(f"2D {nombre} listo", flush=True)
for nombre, beta in BETAS_1D.items():
    F = serie(orden_cadena(N1D), beta, N1D)
    salida["series_1D"][nombre] = dict(beta=beta, limite_exacto=float(1 - np.tanh(2 * beta)),
                                       filas=F, z_ef=exponente_efectivo(F, list(range(1, N1D + 1)), 1))
for n in range(2, 12):                                     # ciclo libre (PR-02): brecha 4 sin²(π/N)
    N = 2 ** n
    salida["ciclo"].append(dict(puntos=N, z_ef=float(np.log(np.sin(np.pi / (N // 2)) ** 2 / np.sin(np.pi / N) ** 2) / np.log(2))))


# --------------------------------------------------------------------- comprobaciones
def zs(serie_, clave="z_ef"):
    return [z["z_ef"] for z in serie_[clave]]


def ultimo_z(serie_, clave="z_ef"):
    return zs(serie_, clave)[-1]


S2 = salida["series_2D"]
for nombre, d in list(S2.items()) + list(salida["series_1D"].items()):
    F = d["filas"][1:]
    # Las medidas estructurales se parecen con y sin brecha:
    assert all(f["peso_heredado_modo_bajo"] > 0.9 for f in F if f["espines"] >= 5), nombre
    assert all(0.99 < f["brecha_nuevos"] < 1.5 for f in F[2:]), nombre
    assert all(0.15 < f["acoplamiento"] < 0.55 for f in F if f["acoplamiento"] > 0), nombre
    assert F[-1]["acoplamiento_efectivo"] < 0.5 * F[2]["acoplamiento_efectivo"], nombre
for d in salida["series_1D"].values():                     # en 1D la marginal es exacta
    assert all(f["cambio_de_lo_heredado_TV"] < 1e-12 for f in d["filas"][1:])
    assert all(f["brecha"] > d["limite_exacto"] for f in d["filas"])
assert all(f["cambio_de_lo_heredado_TV"] > 1e-3 for f in S2["critico"]["filas"][1:] if f["espines"] in (4, 9, 16))
# El exponente efectivo, comparando forma con forma, ordena los tres regímenes...
def creciente(v):
    return all(a < b for a, b in zip(v[:-1], v[1:]))


for clave in ("z_ef_cuadrados", "z_ef_rectangulos"):
    a_, c_, b_ = zs(S2["alta_T"], clave), zs(S2["critico"], clave), zs(S2["baja_T"], clave)
    assert all(x < y < z for x, y, z in zip(a_, c_, b_)), clave
    assert creciente(c_) and 1.7 < c_[-1] < 2.3, clave       # crítico: sube hacia z conocido, no hacia 0
    assert creciente(b_), clave                              # baja T: crece con el tamaño
    assert creciente(a_[::-1]) and a_[-1] > 0.5, clave       # alta T: baja, pero lejos de 0
assert ultimo_z(salida["series_1D"]["1D_beta_0.5"]) < 0.1
assert 0.3 < ultimo_z(salida["series_1D"]["1D_beta_1.5"]) < 1.0
assert creciente(zs(salida["series_1D"]["1D_beta_1.5"])[-6:][::-1])
assert abs(salida["ciclo"][-1]["z_ef"] - 2) < 1e-3

if not RAPIDO:
    root = Path(__file__).resolve().parent
    (root / "resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --------------------------------------------------------------------- informe
for nombre, d in list(S2.items()) + list(salida["series_1D"].items()):
    print(f"\n{nombre} (β={d['beta']:.4f})")
    print(f"{'esp':>3} {'brecha':>9} {'her':>9} {'nue':>6} {'κ':>6} {'κ_ef':>8} {'peso':>6} {'TV':>7} {'ℓ':>7}")
    for f in d["filas"][1:]:
        print(f"{f['espines']:>3} {f['brecha']:>9.6f} {f['brecha_heredados']:>9.6f} {f['brecha_nuevos']:>6.3f} "
              f"{f['acoplamiento']:>6.3f} {f['acoplamiento_efectivo']:>8.2e} {f['peso_heredado_modo_bajo']:>6.3f} "
              f"{f['cambio_de_lo_heredado_TV']:>7.4f} {f['perdida_log']:>7.4f}")
    claves = ("z_ef",) if "1D" in nombre else ("z_ef_cuadrados", "z_ef_rectangulos")
    for clave in claves:
        lista = d[clave][-6:]
        print(f"  {clave}: " + "  ".join(f"{z['de']}→{z['a']}: {z['z_ef']:.2f}" for z in lista))
print("\nciclo libre: z_ef → " + f"{salida['ciclo'][-1]['z_ef']:.4f}")
print("\nOK: todas las aserciones pasaron. No es una prueba de brecha de Yang-Mills.")
