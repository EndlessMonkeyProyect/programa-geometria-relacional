#!/usr/bin/env python3
"""Laboratorio S–RA–01 · semilla de Möbius por octavas.

Calcula, para los índices libres de cuadrados n <= 2^J, el error óptimo
e_j^2 = dist(chi, W_j)^2 en L^2((0,inf), dx), la ganancia óptima de cada
octava y la ganancia d_j de la semilla g_j = sum_{2^j<n<=2^{j+1}} mu(n) f_n.

Requiere numpy. Doble precisión; los valores son mediciones reproducibles,
no intervalos certificados.
"""
import sys, time
from math import gcd, log, pi
import numpy as np

EULER = 0.5772156649015329
J = int(sys.argv[1]) if len(sys.argv) > 1 else 11
NMAX = 2 ** J

# --- aritmética -----------------------------------------------------------
def mobius_hasta(n):
    mu = np.ones(n + 1, dtype=np.int64); mu[0] = 0
    primo = np.ones(n + 1, dtype=bool); primo[:2] = False
    for p in range(2, n + 1):
        if primo[p]:
            primo[2 * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    return mu

mu = mobius_hasta(NMAX)
S = np.array([n for n in range(1, NMAX + 1) if mu[n] != 0])

# --- producto interno <f_h, f_k> -----------------------------------------
# Para h, k coprimos:
#   <f_h,f_k> = (log 2pi - g)/2 (1/h+1/k) + (k-h)/(2hk) log(h/k)
#               - pi/(2hk) (V(h,k)+V(k,h)),
#   V(h,k) = sum_{m=1}^{k-1} {m h/k} cot(pi m/k);
# y <f_{dh}, f_{dk}> = <f_h, f_k>/d.
TABLA = {}
def tabla(k):
    if k not in TABLA:
        if k == 1:
            TABLA[k] = np.zeros(1)
        else:
            m = np.arange(1, k)
            cot = 1.0 / np.tan(np.pi * m / k)
            r = np.arange(k)
            TABLA[k] = ((np.outer(r, m) % k) / k) @ cot
    return TABLA[k]

def producto(h, k):
    d = gcd(h, k); h //= d; k //= d
    v = tabla(k)[h % k] + tabla(h)[k % h]
    return ((log(2 * pi) - EULER) / 2 * (1 / h + 1 / k)
            + (k - h) / (2 * h * k) * log(h / k)
            - pi / (2 * h * k) * v) / d

def producto_por_tramos(h, k, periodos):
    """Integral directa: int_0^inf {t/h}{t/k} dt/t^2, exacta por tramos
    hasta T = periodos*mcm, más la media del período en la cola."""
    d = gcd(h, k); h2, k2 = h // d, k // d
    T = periodos * h2 * k2
    pts = np.union1d(np.arange(0, T + 1, h2), np.arange(0, T + 1, k2)).astype(float)
    s, e = pts[1:-1], pts[2:]
    a, b = np.floor(s / h2), np.floor(s / k2)
    total = pts[1] / (h2 * k2)
    total += np.sum((e - s) / (h2 * k2) - (b / h2 + a / k2) * np.log(e / s)
                    + a * b * (1 / s - 1 / e))
    total += (0.25 + 1 / (12 * h2 * k2)) / T
    return total / d

def main():
    t0 = time.time()
    print(f'LABORATORIO S–RA–01 · SEMILLA DE MÖBIUS POR OCTAVAS · N <= {NMAX}')
    print('\n1. Validación del producto interno (fórmula exacta vs. integración por tramos)')
    for h, k, per in [(1, 1, 20000), (1, 2, 20000), (2, 3, 20000), (3, 5, 20000),
                      (37, 101, 400), (30, 77, 300), (105, 143, 60), (210, 221, 40)]:
        a, b = producto(h, k), producto_por_tramos(h, k, per)
        print(f'   <f_{h},f_{k}> = {a:.12f}   tramos: {b:.12f}   dif: {abs(a-b):.1e}')
        assert abs(a - b) < 1e-8

    n = len(S)
    G = np.empty((n, n))
    for i in range(n):
        for j in range(i, n):
            G[i, j] = G[j, i] = producto(int(S[i]), int(S[j]))
    bvec = np.array([(1 - EULER + log(m)) / m for m in S])     # <chi, f_n>
    dg = np.sqrt(np.diag(G))
    Gs = G / np.outer(dg, dg)                                  # escalado diagonal
    bs = bvec / dg

    def error2(idx):
        g = Gs[np.ix_(idx, idx)]
        w = np.linalg.eigvalsh(g)
        return 1 - bs[idx] @ np.linalg.solve(g, bs[idx]), w[-1] / w[0]

    print(f'\n2. Error óptimo e_j^2 = dist(chi, W_j)^2, W_j = span{{f_n : n <= 2^j, n libre de cuadrados}}')
    print('    j      N   dim        e_j^2   condicion   e_j^2*log N')
    E = {}
    for j in range(J + 1):
        idx = np.where(S <= 2 ** j)[0]
        E[j], c = error2(idx)
        ln = log(2 ** j) if j else float('nan')
        print(f'   {j:2d} {2**j:6d} {len(idx):5d}  {E[j]:.8f}   {c:9.2e}   {E[j]*ln:.5f}' if j else
              f'   {j:2d} {2**j:6d} {len(idx):5d}  {E[j]:.8f}   {c:9.2e}         -')

    print('\n3. Octavas: ganancia optima Delta_j (Schur) y ganancia d_j de la semilla de Mobius')
    print('    j   Delta_j=e_j^2-e_{j+1}^2   gamma_j=Delta_j/e_j^2    d_j          d_j/Delta_j   (j+1)*d_j/e_j^2   sola/Delta_j')
    filas = []
    for j in range(J):
        A = np.where(S <= 2 ** j)[0]
        B = np.where((S > 2 ** j) & (S <= 2 ** (j + 1)))[0]
        GAA, GAB, GBB = Gs[np.ix_(A, A)], Gs[np.ix_(A, B)], Gs[np.ix_(B, B)]
        xA = np.linalg.solve(GAA, bs[A]); Y = np.linalg.solve(GAA, GAB)
        h = bs[B] - GAB.T @ xA                     # <chi, parte nueva>
        Sc = GBB - GAB.T @ Y                       # complemento de Schur
        delta = h @ np.linalg.solve(Sc, h)
        assert abs(delta - (E[j] - E[j + 1])) <= 1e-9 + 1e-6 * delta
        c = mu[S[B]] * dg[B]                       # semilla en la base escalada
        d = (c @ h) ** 2 / (c @ Sc @ c)
        assert -1e-15 <= d <= delta * (1 + 1e-9)   # cota (1) de RA–01
        sola = np.max(h ** 2 / np.diag(Sc))        # mejor referencia nueva tomada sola
        filas.append((j, delta, delta / E[j], d, d / delta, (j + 1) * d / E[j], sola / delta))
        print(f'   {j:2d}   {delta:.6e}        {delta/E[j]:.5f}      {d:.6e}   {d/delta:.4f}    {(j+1)*d/E[j]:.3f}          {sola/delta:.4f}')

    if J >= 11:
        assert (len(np.where(S <= 1024)[0]), len(np.where(S <= 2048)[0])) == (624, 1245)
        assert abs(E[10] - 0.006672) < 5e-6 and abs(E[11] - 0.006229) < 5e-6
        assert abs(filas[10][2] - 0.0664) < 5e-4
        print('\n4. Registro 1024->2048: 624 + 621 = 1245 referencias; '
              f'e2_1024 = {E[10]:.7f}, e2_2048 = {E[11]:.7f}, gamma = {100*filas[10][2]:.2f} % - coincide con el registro archivado')
    print(f'\nConstante de referencia 2+gamma-log(4*pi) = {2 + EULER - log(4*pi):.6f}')
    print(f'Tiempo: {time.time()-t0:.1f} s')
    print('RESULTADO: LABORATORIO S–RA–01 REPRODUCIDO')

if __name__ == '__main__':
    main()
