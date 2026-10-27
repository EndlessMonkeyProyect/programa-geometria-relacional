#!/usr/bin/env python3
"""PR-05 — Brecha uniforme de Ising 2D a alta temperatura, por resolución local contra influencia.

Teorema (§3 del README): si α_b(β) < 1, todo rectángulo Λ con frontera libre cumple
    γ_Λ ≥ (1 − α_b(β)) · m_b(β).
Este script calcula α_b y m_b por enumeración exhaustiva, los umbrales β*_b, y contrasta la cota
con brechas exactas de rectángulos. Ejecutar:
    python verificar.py            (completo, ~6 min; escribe resultados.json)
    python verificar.py --rapido   (sin b = 4 ni m_3; ~20 s; no escribe resultados)
Dependencias: numpy, scipy.
"""

from __future__ import annotations
import itertools
import numpy as np


def forma(r, s):
    """Rectángulo r×s. Devuelve: estados de espín (2^n × n), energía interna por estado,
    y la lista de 'ranuras' externas: (lado, índice de sitio interno que toca)."""
    n = r * s
    idx = lambda i, j: i * s + j
    x = np.arange(2 ** n, dtype=np.int64)
    S = 1 - 2 * ((x[:, None] >> np.arange(n)) & 1)
    e = np.zeros(2 ** n)
    for i in range(r):
        for j in range(s):
            if j + 1 < s:
                e += S[:, idx(i, j)] * S[:, idx(i, j + 1)]
            if i + 1 < r:
                e += S[:, idx(i, j)] * S[:, idx(i + 1, j)]
    lados = {
        "arriba": [idx(0, j) for j in range(s)],
        "abajo": [idx(r - 1, j) for j in range(s)],
        "izquierda": [idx(i, 0) for i in range(r)],
        "derecha": [idx(i, s - 1) for i in range(r)],
    }
    return S, e, lados


def entornos(lados):
    """Cada lado está ausente (borde del volumen: campo 0) o presente con valores ±1.
    Devuelve matriz de campos por ranura (n_entornos × n_ranuras), sitio de cada ranura,
    y para cada ranura presente, el índice del entorno con esa ranura invertida."""
    nombres = list(lados)
    opciones = []
    for nm in nombres:
        L = len(lados[nm])
        opts = [None] + list(itertools.product((-1, 1), repeat=L))
        opciones.append(opts)
    ranura_sitio = [x for nm in nombres for x in lados[nm]]
    combos = list(itertools.product(*[range(len(o)) for o in opciones]))
    pos = {c: k for k, c in enumerate(combos)}
    campos = np.zeros((len(combos), len(ranura_sitio)))
    pares = []                                    # (entorno con y=-1, entorno con y=+1)
    for k, c in enumerate(combos):
        col = 0
        for li, nm in enumerate(nombres):
            L = len(lados[nm]); o = opciones[li][c[li]]
            if o is not None:
                campos[k, col:col + L] = o
                for t in range(L):
                    if o[t] == -1:                # pareja: misma configuración con la ranura t en +1
                        o2 = list(o); o2[t] = 1
                        c2 = list(c); c2[li] = opciones[li].index(tuple(o2))
                        pares.append((k, pos[tuple(c2)], col + t))
            col += L
    return campos, np.array(ranura_sitio), np.array(pares, dtype=np.int64)


def influencias(r, s, beta):
    """Para cada ranura externa (lado, posición): máx sobre entornos de Σ_x (m_x(y=+) − m_x(y=−))/2.
    Por Holley (ferromagnético) las dos condicionales están ordenadas, y el acoplamiento
    monótono da exactamente ese número esperado de espines distintos: cota de W1-Hamming."""
    S, e, lados = forma(r, s)
    campos, sitio, pares = entornos(lados)
    F = campos @ S[:, sitio].T                    # campo de frontera por (entorno, estado)
    A = beta * (e[None, :] + F)
    A -= A.max(axis=1, keepdims=True)
    W = np.exp(A)
    W /= W.sum(axis=1, keepdims=True)
    m = W @ S                                     # magnetizaciones por sitio
    d = 0.5 * (m[pares[:, 1]] - m[pares[:, 0]]).sum(axis=1)
    assert d.min() > -1e-12                       # comprobación de Holley: el orden se respeta
    por_ranura = np.zeros(campos.shape[1])
    np.maximum.at(por_ranura, pares[:, 2], d)
    out, col = {}, 0
    for nm, L in lados.items():
        out[nm] = por_ranura[col:col + len(L)].copy()
        col += len(L)
    return out


def influencia_maxima(r, s, beta):
    return float(max(v.max() for v in influencias(r, s, beta).values()))


def influencia_total(b, beta):
    """Cota de A_y = Σ sobre las 4b ventanas vecinas de y de su influencia, contando los recortes:
    para la ventana a la derecha de y con desplazamiento k, el recorte es (u+v+1)×w con u ≤ k,
    v ≤ b−1−k, w ≤ b, e y toca el lado izquierdo en la fila u. Igual en las otras 3 direcciones."""
    tabla = {(r, s): influencias(r, s, beta) for r, s in formas(b)}
    lado_de = {"derecha_de_y": "izquierda", "izquierda_de_y": "derecha", "debajo_de_y": "arriba", "encima_de_y": "abajo"}
    total = 0.0
    for dirn, lado in lado_de.items():
        for k in range(b):
            mejor = 0.0
            for u in range(k + 1):
                for v in range(b - k):
                    for w in range(1, b + 1):
                        alto = u + v + 1
                        rs = (alto, w) if lado in ("izquierda", "derecha") else (w, alto)
                        mejor = max(mejor, tabla[rs][lado][u])
            total += mejor
    return total


def brecha_interna(S, e, F_row, beta):
    """Brecha del baño térmico dentro de la ventana con un entorno fijo."""
    n = S.shape[1]; M = 2 ** n
    E = e + F_row
    x = np.arange(M)
    H = np.zeros((M, M))
    for k in range(n):
        y = x ^ (1 << k)
        c = 1.0 / (1.0 + np.exp(beta * (E - E[y])))
        H[x, x] += c
        H[x, y] -= np.sqrt(c * (1 - c))
    v = np.linalg.eigvalsh(H)
    return float(v[1])


def resolucion_minima(r, s, beta):
    """m(r,s,β) = mínimo sobre entornos de la brecha interna. Usa la simetría global de espín
    (entorno → −entorno da la misma brecha) para evaluar la mitad de los entornos."""
    S, e, lados = forma(r, s)
    campos, sitio, _ = entornos(lados)
    F = campos @ S[:, sitio].T
    vistos, mejor = set(), np.inf
    for k in range(len(campos)):
        clave = tuple(campos[k]); neg = tuple(-campos[k])
        if neg in vistos:
            continue
        vistos.add(clave)
        mejor = min(mejor, brecha_interna(S, e, F[k], beta))
    return float(mejor)


def formas(b):
    return [(r, s) for r in range(1, b + 1) for s in range(1, b + 1)]


def alfa(b, beta):
    """Influencia recibida por sitio, repartida entre las b² ventanas que lo contienen."""
    return influencia_total(b, beta) / b ** 2


def umbral(b, lo=0.0, hi=0.6, it=45):
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if alfa(b, mid) < 1:
            lo = mid
        else:
            hi = mid
    return lo

# ---- matriz de transferencia (b = 4) ----



def _opciones(L):
    return [None] + list(itertools.product((-1, 1), repeat=L))


def influencias_tm(r, s, beta, trozo=60000):
    R = 2 ** r
    st = np.arange(R)
    spin = 1 - 2 * ((st[:, None] >> np.arange(r)) & 1)            # (R, r): fila i del estado de columna
    vert = (spin[:, :-1] * spin[:, 1:]).sum(1) if r > 1 else np.zeros(R)
    T = np.exp(beta * (spin @ spin.T))                              # acople horizontal entre columnas
    o_top, o_bot, o_izq, o_der = _opciones(s), _opciones(s), _opciones(r), _opciones(r)
    tam = (len(o_top), len(o_bot), len(o_izq), len(o_der))
    n_env = int(np.prod(tam))

    def campos(lista, L):
        a = np.zeros((len(lista), L))
        for k, o in enumerate(lista):
            if o is not None:
                a[k] = o
        return a
    Ct, Cb, Cl, Cr = campos(o_top, s), campos(o_bot, s), campos(o_izq, r), campos(o_der, r)

    def magnetizaciones(idx):
        it, ib, il, ir_ = np.unravel_index(idx, tam)
        n = len(idx)
        # peso local por columna j y estado: vertical + campo arriba (fila 0) + abajo (fila r-1) + lados
        logw = np.empty((n, s, R))
        for j in range(s):
            e = vert[None, :] + Ct[it, j][:, None] * spin[None, :, 0] + Cb[ib, j][:, None] * spin[None, :, r - 1]
            if j == 0:
                e = e + Cl[il] @ spin.T
            if j == s - 1:
                e = e + Cr[ir_] @ spin.T
            logw[:, j, :] = beta * e
        w = np.exp(logw - logw.max(axis=2, keepdims=True))
        f = np.empty_like(w); g = np.empty_like(w)
        f[:, 0] = w[:, 0]; f[:, 0] /= f[:, 0].sum(1, keepdims=True)
        for j in range(1, s):
            f[:, j] = (f[:, j - 1] @ T) * w[:, j]
            f[:, j] /= f[:, j].sum(1, keepdims=True)
        g[:, s - 1] = 1.0
        for j in range(s - 2, -1, -1):
            g[:, j] = (g[:, j + 1] * w[:, j + 1]) @ T.T
            g[:, j] /= g[:, j].sum(1, keepdims=True)
        p = f * g
        p /= p.sum(2, keepdims=True)
        return np.einsum("njk,ki->nji", p, spin)                    # (n, s, r): magnetización en (col j, fila i)

    # ranuras: ('arriba', j) campo sobre (0, j); ('abajo', j) sobre (r-1, j); ('izquierda', i); ('derecha', i)
    mejor = {"arriba": np.zeros(s), "abajo": np.zeros(s), "izquierda": np.zeros(r), "derecha": np.zeros(r)}
    lados = [("arriba", 0, o_top), ("abajo", 1, o_bot), ("izquierda", 2, o_izq), ("derecha", 3, o_der)]
    minimo = np.inf
    for ini in range(0, n_env, trozo):
        idx = np.arange(ini, min(ini + trozo, n_env))
        m = magnetizaciones(idx)
        cod = np.array(np.unravel_index(idx, tam)).T                  # (n, 4) índices por lado
        for nombre, li, opts in lados:
            L = len(opts[1]) if len(opts) > 1 else 0
            for t in range(L):
                # entornos donde el lado li está presente con la posición t en −1
                presentes = cod[:, li] > 0
                if not presentes.any():
                    continue
                vals = np.array([opts[c][t] if c > 0 else 0 for c in range(len(opts))])
                sel = presentes & (vals[cod[:, li]] == -1)
                if not sel.any():
                    continue
                # índice de la opción con la posición t en +1
                mapa = np.zeros(len(opts), dtype=np.int64)
                for c in range(1, len(opts)):
                    if opts[c][t] == -1:
                        o2 = list(opts[c]); o2[t] = 1
                        mapa[c] = opts.index(tuple(o2))
                cod2 = cod[sel].copy(); cod2[:, li] = mapa[cod2[:, li]]
                idx2 = np.ravel_multi_index(cod2.T, tam)
                m2 = magnetizaciones(idx2)
                d = 0.5 * (m2 - m[sel]).sum(axis=(1, 2))
                minimo = min(minimo, d.min())
                mejor[nombre][t] = max(mejor[nombre][t], d.max())
    assert minimo > -1e-10                                          # Holley
    return mejor


def influencia_total_tm(b, beta):
    tabla = {(r, s): influencias_tm(r, s, beta) for r in range(1, b + 1) for s in range(1, b + 1)}
    lado_de = {"derecha_de_y": "izquierda", "izquierda_de_y": "derecha", "debajo_de_y": "arriba", "encima_de_y": "abajo"}
    total = 0.0
    for dirn, lado in lado_de.items():
        for k in range(b):
            mejor = 0.0
            for u in range(k + 1):
                for v in range(b - k):
                    for w in range(1, b + 1):
                        alto = u + v + 1
                        rs = (alto, w) if lado in ("izquierda", "derecha") else (w, alto)
                        mejor = max(mejor, tabla[rs][lado][u])
            total += mejor
    return total


def alfa_tm(b, beta):
    return influencia_total_tm(b, beta) / b ** 2


def umbral_tm(b, lo=0.25, hi=0.45, it=30):
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if alfa_tm(b, mid) < 1:
            lo = mid
        else:
            hi = mid
    return lo


# =====================================================================================
#  Parte principal
# =====================================================================================
import json, sys, time
from pathlib import Path
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

RAPIDO = "--rapido" in sys.argv
BETA_C = 0.5 * np.log(1 + np.sqrt(2))
BETAS = (0.20, 0.25, 0.30)
BS = (1, 2) if RAPIDO else (1, 2, 3)
RECTANGULOS = [(2, 2), (2, 4), (3, 3), (3, 4), (4, 4), (2, 8)] + ([] if RAPIDO else [(3, 6)])


def brecha_exacta_rectangulo(r, s, beta):
    """Brecha exacta del baño térmico en el rectángulo r×s con frontera libre (como en PR-04)."""
    N = r * s
    M = 2 ** N
    x = np.arange(M, dtype=np.int64)
    S = 1 - 2 * ((x[:, None] >> np.arange(N)) & 1)
    e = np.zeros(M)
    for i in range(r):
        for j in range(s):
            if j + 1 < s:
                e += S[:, i * s + j] * S[:, i * s + j + 1]
            if i + 1 < r:
                e += S[:, i * s + j] * S[:, (i + 1) * s + j]
    filas, cols, vals, diag = [], [], [], np.zeros(M)
    for k in range(N):
        y = x ^ (1 << k)
        c = 1.0 / (1.0 + np.exp(beta * (e - e[y])))
        diag += c
        filas.append(x); cols.append(y); vals.append(-np.sqrt(c * (1 - c)))
    filas.append(x); cols.append(x); vals.append(diag)
    H = sp.csr_matrix((np.concatenate(vals), (np.concatenate(filas), np.concatenate(cols))), shape=(M, M))
    if M <= 2048:
        return float(np.linalg.eigvalsh(H.toarray())[1])
    v0 = np.random.default_rng(20261027).standard_normal(M)
    v = eigsh(H, k=2, which="SA", tol=1e-12, ncv=40, v0=v0, return_eigenvectors=False)
    return float(np.sort(v)[1])


salida = {"rapido": RAPIDO, "beta_critico": float(BETA_C)}
t0 = time.time()

# 1. Comprobaciones de consistencia del cálculo
assert all(abs(alfa(1, be) - 4 * np.tanh(be)) < 1e-12 for be in (0.1, 0.2, 0.3))   # b = 1: Dobrushin clásico
err = max(np.abs(influencias(r, s, be)[k] - influencias_tm(r, s, be)[k]).max()
          for be in (0.2, 0.3) for r in (1, 2, 3) for s in (1, 2, 3) for k in ("arriba", "abajo", "izquierda", "derecha"))
assert err < 1e-12                                                                    # transferencia = directo
salida["error_transferencia_vs_directo"] = float(err)

# 2. Umbrales β*_b donde α_b = 1
umbrales = {1: umbral(1), 2: umbral(2)}
if not RAPIDO:
    umbrales[3] = umbral(3)
    umbrales[4] = umbral_tm(4)
assert abs(umbrales[1] - np.arctanh(0.25)) < 1e-6
assert all(umbrales[b] < umbrales[b + 1] for b in umbrales if b + 1 in umbrales)
salida["umbrales"] = {str(b): float(v) for b, v in umbrales.items()}
print("umbrales β*_b:", {b: round(v, 4) for b, v in umbrales.items()}, f"(β_c = {BETA_C:.4f})", flush=True)

# 3. Influencia, resolución y cota explícita para cada β
cotas = {}
for be in BETAS:
    fila = {}
    for b in BS:
        a = alfa(b, be)
        m = min(resolucion_minima(r, s, be) for r, s in formas(b))
        fila[str(b)] = dict(alfa=a, resolucion_minima=m, cota=((1 - a) * m if a < 1 else None))
    cotas[str(be)] = fila
    print(f"β={be}: " + "  ".join(f"b={b}: α={v['alfa']:.4f} m={v['resolucion_minima']:.4f} cota={v['cota'] if v['cota'] is None else round(v['cota'], 4)}"
                                for b, v in fila.items()), flush=True)
salida["cotas"] = cotas

# 4. Contraste con brechas exactas de rectángulos (consistencia, no prueba)
exactas = {}
for be in BETAS:
    mejor = max([v["cota"] for v in cotas[str(be)].values() if v["cota"] is not None], default=None)
    for r, s in RECTANGULOS:
        g = brecha_exacta_rectangulo(r, s, be)
        exactas[f"{be}|{r}x{s}"] = g
        if mejor is not None:
            assert g >= mejor - 1e-10, (be, r, s, g, mejor)
salida["brechas_exactas"] = exactas
# la resolución mínima coincide con la brecha libre del bloque mayor (el entorno ausente es el más lento)
for be in BETAS:
    for b in BS:
        if b >= 2:
            libre = brecha_exacta_rectangulo(b, b, be)
            assert abs(cotas[str(be)][str(b)]["resolucion_minima"] - libre) < 1e-9

salida["segundos"] = round(time.time() - t0, 1)
if not RAPIDO:
    (Path(__file__).resolve().parent / "resultados.json").write_text(
        json.dumps({k: v for k, v in salida.items() if k != "segundos"}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("brechas exactas:", {k: round(v, 4) for k, v in exactas.items()})
print("\nOK: todas las aserciones pasaron. Brecha uniforme demostrada para β < β*_b con la cota indicada;"
      " no es Yang–Mills.")
