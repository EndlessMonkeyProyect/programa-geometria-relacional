#!/usr/bin/env python3
"""Recálculo de los errores óptimos restringidos e_m^2 hasta m=2048.

Familia: f_n(x) = {1/(n x)}, n libre de cuadrados, n <= m; objetivo chi = 1_(0,1].
Gram <f_n,f_m> por la fórmula de cotangentes de prueba_reglas_de_peso.py;
<chi,f_n> = (log n + 1 - gamma)/n.

El script:
  1. contrasta la fórmula de Gram con integración directa por tramos en seis pares;
  2. calcula e_m^2 para m = 1, 2, 4, ..., 2048 (float64, con un paso de refinamiento
     iterativo) y el número de condición de cada matriz de Gram;
  3. calcula gamma_{2^j} = (e_m^2 - e_{2m}^2)/e_m^2 y lo compara con 1/(j+2);
  4. calcula, para N = 2048, el error de los coeficientes fijos -mu(n) (corte abrupto)
     y -mu(n)(1 - log n/log N) (pesos logarítmicos).

Tiempo típico: 20-40 s. Requiere numpy.
"""
import math
import time

import numpy as np

from prueba_reglas_de_peso import gram, mu_of

EG = 0.57721566490153286060651209
C0 = 2 + EG - math.log(4 * math.pi)  # constante de Burnol / Bettin-Conrey-Farmer


def gram_directo(h, k):
    """<f_h,f_k> = int_0^inf {y/h}{y/k} y^-2 dy, integrado exactamente en cada [j, j+1]
    hasta Y = 20000 * mcm(h,k); la cola se aproxima por su media sobre el período."""
    per = h * k // math.gcd(h, k)
    Y = 20000 * per
    j = np.arange(1, Y, dtype=np.float64)
    ji = np.arange(1, Y, dtype=np.int64)
    a1, b1 = -(ji // h).astype(np.float64), 1.0 / h
    a2, b2 = -(ji // k).astype(np.float64), 1.0 / k
    tramos = a1 * a2 * (1 / j - 1 / (j + 1)) + (a1 * b2 + a2 * b1) * np.log1p(1 / j) + b1 * b2
    media = 0.25 + math.gcd(h, k) ** 2 / (12 * h * k)
    return 1.0 / (h * k) + float(np.sum(tramos)) + media / Y


print('1. Fórmula de Gram contra integración directa')
for h, k in [(1, 1), (1, 2), (2, 3), (3, 5), (4, 6), (7, 10)]:
    f, d = gram(h, k), gram_directo(h, k)
    assert abs(f - d) < 1e-8, (h, k, f, d)
    print(f'   <f_{h},f_{k}>: fórmula {f:.10f}   directa {d:.10f}')

t0 = time.time()
idx = [n for n in range(1, 2049) if mu_of(n) != 0]
G = np.empty((len(idx), len(idx)))
for i, a in enumerate(idx):
    for j in range(i + 1):
        G[i, j] = G[j, i] = gram(a, idx[j])
b = np.array([(math.log(n) + 1 - EG) / n for n in idx])
print(f'\n2. Matriz de Gram de dimensión {len(idx)} construida en {time.time() - t0:.1f} s')


def error_optimo(m):
    k = sum(1 for n in idx if n <= m)
    Gk, bk = G[:k, :k], b[:k]
    x = np.linalg.solve(Gk, bk)
    x = x + np.linalg.solve(Gk, bk - Gk @ x)  # refinamiento iterativo
    w = np.linalg.eigvalsh(Gk)
    return k, float(1 - bk @ x), float(w[-1] / w[0])


print('    m    dim      e_m^2       e_m^2 log m   condición')
E = {}
for j in range(12):
    m = 2 ** j
    k, e2, cond = error_optimo(m)
    E[m] = e2
    print(f'{m:5d}  {k:5d}   {e2:.6f}   {e2 * math.log(m) if m > 1 else float("nan"):10.4f}   {cond:.2e}')
print(f'   C0 = 2 + gamma - log(4 pi) = {C0:.6f}')

print('\n3. Fracción recuperada por octava')
print('   j     m    gamma_m     1/(j+2)   gamma >= 1/(j+2)')
fallos = []
for j in range(11):
    m = 2 ** j
    g = (E[m] - E[2 * m]) / E[m]
    ok = g >= 1 / (j + 2)
    if not ok:
        fallos.append(j)
    print(f'{j:4d} {m:5d}   {g:.4f}      {1 / (j + 2):.4f}     {"sí" if ok else "NO"}')
g1024 = (E[1024] - E[2048]) / E[1024]
assert abs(E[1024] - 0.006672) < 5e-7 and abs(E[2048] - 0.006229) < 5e-7
assert abs(g1024 - 0.0664) < 5e-4 and g1024 < 1 / 12
print(f'   Pasos donde falla gamma >= 1/(j+2): j = {fallos}')
print(f'   Paso 1024 -> 2048: gamma = {g1024:.5f}; ángulo arccos(sqrt(gamma)) = '
      f'{math.degrees(math.acos(math.sqrt(g1024))):.3f} grados')

print('\n4. Coeficientes fijos en N = 2048 (sin ajuste de escala)')
N = 2048
c_log = np.array([-mu_of(n) * (1 - math.log(n) / math.log(N)) for n in idx])
c_cut = np.array([-mu_of(n) for n in idx], dtype=float)
e_log = float(1 - 2 * c_log @ b + c_log @ G @ c_log)
e_cut = float(1 - 2 * c_cut @ b + c_cut @ G @ c_cut)
assert abs(e_log - 0.067054) < 5e-6 and abs(e_cut - 0.084783) < 5e-6
print(f'   pesos 1 - log n/log N: {e_log:.6f}')
print(f'   corte abrupto -mu(n):  {e_cut:.6f}')
print(f'   óptimo restringido:     {E[2048]:.6f}')
print('RESULTADO: cifras de la tabla de §6 recalculadas en float64.')
