#!/usr/bin/env python3
"""PR-06 — Masa positiva de Ising 2D por cierre de ventanas: el flujo de correlación por el borde.

Teorema (§3 del README): si φ_β(S_n) < 1 para la caja n×n centrada, entonces para todo z
    ⟨σ_0 σ_z⟩ ≤ φ_β(S_n)^⌊‖z‖∞ / ((n+1)/2)⌋,   es decir, masa ≥ −ln φ / ((n+1)/2) > 0.
Este script calcula φ exactamente (matriz de transferencia factorizada), los umbrales β_n,
comprueba la desigualdad de Simon–Lieb en volúmenes pequeños y compara la masa certificada
con la masa exacta de Onsager.
Ejecutar:  python verificar.py            (completo, cajas hasta 21×21; ~4 min; escribe resultados.json)
           python verificar.py --rapido   (cajas hasta 13×13; ~10 s; no escribe resultados)
Dependencia: numpy.
"""

from __future__ import annotations
import itertools
import numpy as np


def _aplicar_T(X, t):
    """Acople horizontal entre columnas: T = ⊗_i t, aplicado eje por eje (coste n·2^n)."""
    for i in range(X.ndim):
        X = np.moveaxis(np.tensordot(t, X, axes=([1], [i])), 0, i)
    return X


def _signo(n, i):
    s = np.array([1.0, -1.0]).reshape([2 if k == i else 1 for k in range(n)])
    return s


def correlaciones_borde(n, beta):
    """⟨σ_0 σ_x⟩ en la caja n×n libre, 0 en el centro (n impar), para x en las columnas j ≥ c.
    Devuelve dict (fila, columna) -> correlación para todos los sitios del borde de esas columnas."""
    assert n % 2 == 1
    c = (n - 1) // 2
    t = np.array([[np.exp(beta), np.exp(-beta)], [np.exp(-beta), np.exp(beta)]])
    # peso de columna: enlaces verticales dentro de la columna
    logw = np.zeros([2] * n)
    for i in range(n - 1):
        logw = logw + beta * (_signo(n, i) * _signo(n, i + 1))
    w = np.exp(logw - logw.max())
    # hacia atrás: B[j] = suma sobre columnas j+1..n-1 dado el estado de la columna j
    B = [None] * n
    B[n - 1] = np.ones([2] * n)
    for j in range(n - 2, -1, -1):
        X = _aplicar_T(w * B[j + 1], t)
        B[j] = X / X.sum()
    # hacia adelante hasta c, luego con σ_0 insertado
    F = w.copy(); F /= F.sum()
    for j in range(1, c + 1):
        F = _aplicar_T(F, t) * w
        F /= F.sum()
    s0 = _signo(n, c)
    Fp = F * s0
    out = {}
    for j in range(c, n):
        if j > c:
            F_new = _aplicar_T(F, t) * w
            Fp = _aplicar_T(Fp, t) * w
            k = F_new.sum(); F = F_new / k; Fp = Fp / k
        Z = (F * B[j]).sum()
        filas = range(n) if j == n - 1 else (0, n - 1)
        for i in filas:
            out[(i, j)] = float((Fp * _signo(n, i) * B[j]).sum() / Z)
    return out


def flujo(n, beta):
    """φ_β(S_n) = tanh β · Σ_{x ∈ ∂S} (aristas que salen de S en x) · ⟨σ_0 σ_x⟩_S."""
    if n == 1:
        return 4 * np.tanh(beta)
    c = (n - 1) // 2
    corr = correlaciones_borde(n, beta)
    total = 0.0
    for i in range(n):
        for j in range(n):
            salen = (i == 0) + (i == n - 1) + (j == 0) + (j == n - 1)
            if salen:
                jj = j if j >= c else 2 * c - j          # simetría izquierda-derecha
                total += salen * corr[(i, jj)]
    return np.tanh(beta) * total


def umbral(n, lo=0.0, hi=0.4407, it=40):
    """φ crece con β (segunda desigualdad de Griffiths), así que la bisección es válida."""
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if flujo(n, mid) < 1:
            lo = mid
        else:
            hi = mid
    return lo


def correlaciones_directas(r, s, beta, pares):
    """Enumeración exhaustiva en un rectángulo r×s libre (para validar)."""
    N = r * s
    x = np.arange(2 ** N, dtype=np.int64)
    S = 1 - 2 * ((x[:, None] >> np.arange(N)) & 1)
    e = np.zeros(2 ** N)
    for i in range(r):
        for j in range(s):
            if j + 1 < s:
                e += S[:, i * s + j] * S[:, i * s + j + 1]
            if i + 1 < r:
                e += S[:, i * s + j] * S[:, (i + 1) * s + j]
    w = np.exp(beta * (e - e.max())); w /= w.sum()
    return {p: float((w * S[:, p[0][0] * s + p[0][1]] * S[:, p[1][0] * s + p[1][1]]).sum()) for p in pares}


# =====================================================================================
#  Parte principal
# =====================================================================================
import json, sys, time
from pathlib import Path

RAPIDO = "--rapido" in sys.argv
BETA_C = 0.5 * np.log(1 + np.sqrt(2))
NS = list(range(1, 14 if RAPIDO else 22, 2))
UMBRAL_PR05 = 0.33215555883944026          # mejor umbral de PR-05 (ventana 4×4, peor entorno)
salida = {"rapido": RAPIDO, "beta_critico": float(BETA_C)}


def masa_onsager(beta):
    """Masa exacta a lo largo del eje para β < β_c: 2(β* − β), con β* = −½ ln tanh β."""
    return float(2 * (-0.5 * np.log(np.tanh(beta)) - beta))


# 1. Validación del cálculo de correlaciones
err3 = 0.0
for be in (0.2, 0.4):
    corr = correlaciones_borde(3, be)
    d = correlaciones_directas(3, 3, be, [((1, 1), k) for k in corr])
    err3 = max(err3, max(abs(corr[k] - d[((1, 1), k)]) for k in corr))


def transferencia_densa(n, beta):
    st = np.array(list(itertools.product((1, -1), repeat=n)))
    w = np.exp(beta * (st[:, :-1] * st[:, 1:]).sum(1)); T = np.exp(beta * st @ st.T)
    c = (n - 1) // 2; M = len(st)

    def cadena(ops):
        v = w * ops[0]
        for j in range(1, n):
            v = (v @ T) * w * ops[j]
        return v.sum()
    Z = cadena([np.ones(M)] * n); out = {}
    for j in range(c, n):
        for i in (range(n) if j == n - 1 else (0, n - 1)):
            ops = [np.ones(M) for _ in range(n)]
            ops[c] = ops[c] * st[:, c]; ops[j] = ops[j] * st[:, i]
            out[(i, j)] = cadena(ops) / Z
    return out


err5 = max(abs(correlaciones_borde(5, be)[k] - v) for be in (0.3, 0.44) for k, v in transferencia_densa(5, be).items())
assert err3 < 1e-12 and err5 < 1e-12
assert all(abs(flujo(1, be) - 4 * np.tanh(be)) < 1e-15 for be in (0.1, 0.25))     # n = 1: Dobrushin
salida["validacion"] = {"error_n3_vs_enumeracion": err3, "error_n5_vs_transferencia_densa": err5}


# 2. Desigualdad de Simon–Lieb (Lieb 1980) comprobada en volúmenes pequeños, con S = caja 3×3
def simon_lieb(r, s, beta):
    S = [(i, j) for i in range(3) for j in range(3)]; o = (1, 1)
    fuera = [(i, j) for i in range(r) for j in range(s) if (i, j) not in S]
    CL = correlaciones_directas(r, s, beta, [(o, z) for z in fuera] + [(y, z) for y in fuera for z in fuera])
    CS = correlaciones_directas(3, 3, beta, [(o, x) for x in S])
    th, peor = np.tanh(beta), -np.inf
    for z in fuera:
        rhs = sum(th * CS[(o, x)] * (1.0 if y == z else CL[(y, z)])
                  for x in S for y in ((x[0] + 1, x[1]), (x[0] - 1, x[1]), (x[0], x[1] + 1), (x[0], x[1] - 1)) if y in fuera)
        peor = max(peor, CL[(o, z)] - rhs)
    return float(peor)


sl = {f"{be}|{r}x{s}": simon_lieb(r, s, be) for be in (0.2, 0.3, 0.44, 0.6) for r, s in ((3, 6), (4, 5))}
assert all(v <= 1e-12 for v in sl.values())
salida["simon_lieb_max_lhs_menos_rhs"] = sl
print("validación y Simon–Lieb: OK", flush=True)

# 3. Umbrales β_n donde φ_β(S_n) = 1 (φ crece con β por la segunda desigualdad de Griffiths)
umbrales, previo = {}, 0.0
for n in NS:
    t = time.time()
    if flujo(n, previo) >= 1:                       # sólo se arranca desde el umbral previo si es válido
        previo = 0.0
    assert flujo(n, float(BETA_C)) >= 1             # en β_c ninguna caja cierra (Duminil-Copin–Tassion)
    umbrales[n] = umbral(n, lo=previo, hi=float(BETA_C), it=(40 if n <= 13 else 18))
    assert flujo(n, umbrales[n]) < 1                # el valor informado es un β certificado
    previo = umbrales[n]
    print(f"n={n:2d}: β_n = {umbrales[n]:.5f}  ({umbrales[n] / BETA_C:.1%} de β_c)  [{time.time() - t:.1f} s]", flush=True)
vals = [umbrales[n] for n in NS]
assert all(a < b for a, b in zip(vals[:-1], vals[1:])) and vals[-1] < BETA_C
assert umbrales[5] > UMBRAL_PR05                                                # pasa la pared de PR-05
salida["umbrales"] = {str(n): float(v) for n, v in umbrales.items()}

# 4. Masa certificada frente a masa exacta
masas = {}
for be in (0.25, 0.30, 0.35, 0.38, 0.40):
    mejor, n_mejor = 0.0, None
    for n in NS:
        f = flujo(n, be)
        if f < 1 and -np.log(f) / ((n + 1) / 2) > mejor:
            mejor, n_mejor = float(-np.log(f) / ((n + 1) / 2)), n
    ex = masa_onsager(be)
    assert mejor <= ex                                                           # cota por debajo de lo exacto
    masas[str(be)] = {"masa_certificada": mejor, "caja": n_mejor, "masa_exacta_eje": ex}
    print(f"β={be}: masa certificada {mejor:.4f} (caja {n_mejor}) · exacta {ex:.4f}", flush=True)
if not RAPIDO:
    assert masas["0.4"]["masa_certificada"] > 0
salida["masas"] = masas

if not RAPIDO:
    (Path(__file__).resolve().parent / "resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("\nOK: todas las aserciones pasaron. Masa positiva certificada para β < β_n; no es Yang–Mills.")
