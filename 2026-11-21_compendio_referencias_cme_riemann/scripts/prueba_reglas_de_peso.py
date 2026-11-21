#!/usr/bin/env python3
"""Prueba de reglas de peso para la herencia de la criba (Endless Monkey Project).

Referencias f_d(x) = {1/(d x)}; objetivo: la unidad en (0,1]. Aproximante con regla w:
g = sum_d (-mu(d)) w_d f_d. Se mide ||1 - g||^2 (sin ajuste) y con una escala libre a*.
Gram exacto por fórmula de cotangentes. Requiere numpy.
"""
import math, time
import numpy as np

EG = 0.57721566490153286060651209
L2PI = math.log(2 * math.pi)


def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for p in range(2, int(n ** .5) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0].tolist()


def divisors(ps):
    d = [(1, 1)]
    for p in ps:
        d += [(p * x, -m) for x, m in d]
    d.sort()
    return [x for x, _ in d], np.array([m for _, m in d], float)


_Vc = {}
def V(h, k):
    if k == 1:
        return 0.0
    key = (h, k)
    if key not in _Vc:
        m = np.arange(1, k, dtype=np.int64)
        _Vc[key] = float(np.sum(((m * h) % k) / k / np.tan(np.pi * m / k)))
    return _Vc[key]


def gram(n, m):
    g = math.gcd(n, m); h, k = n // g, m // g
    val = ((L2PI - EG) / 2 * (1 / h + 1 / k) + (k - h) / (2 * h * k) * math.log(h / k)
           - math.pi / (2 * h * k) * (V(h, k) + V(k, h)))
    return val / g


def build(idx):
    n = len(idx); G = np.empty((n, n))
    for i in range(n):
        for j in range(i + 1):
            G[i, j] = G[j, i] = gram(idx[i], idx[j])
    b = np.array([(math.log(d) + 1 - EG) / d for d in idx])
    return G, b


def err(G, b, c, alpha=None):
    bc, cGc = b @ c, c @ G @ c
    if alpha is None:
        return 1 - bc * bc / cGc, bc / cGc
    return 1 - 2 * alpha * bc + alpha ** 2 * cGc, alpha


def mu_of(n):
    m, p, k = 1, 2, n
    while p * p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            m = -m
        p += 1
    return -m if k > 1 else m


def tramo(N):
    mu = np.ones(N + 1, np.int8); mu[0] = 0
    lam = np.zeros(N + 1)
    isp = np.ones(N + 1, bool); isp[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if isp[p]: isp[p*p::p] = False
    for p in np.nonzero(isp)[0]:
        p = int(p)
        mu[p::p] *= -1
        if p * p <= N: mu[p*p::p*p] = 0
        q = p
        while q <= N:
            lam[q] = math.log(p); q *= p
    d = np.arange(1, N + 1, dtype=float)
    beta = float(np.sum(mu[1:] * np.log(N / d) / d))
    psi = np.cumsum(lam); k = np.arange(1, N, dtype=float); ps = psi[1:N]
    S = float(np.sum(ps**2 * (1/k - 1/(k+1)) - 2*ps*beta*np.log((k+1)/k) + beta**2))
    L = math.log(N)
    return beta, S, S / L**2, (beta / L)**2

if __name__ == '__main__':
    print('== A. Herencia con sus propios pesos (mu): cota inferior exacta del resto ==')
    print('   en [1, p_siguiente) solo sobrevive la unidad -> resto >= p_sig * rho^2, rho = prod(1-1/p)')
    ps = primes_upto(200000)
    rho = 1.0
    for i, p in enumerate(ps[:-1]):
        rho *= 1 - 1 / p
        if p in {11, 29, 97, 997, 9973, 99991}:
            print(f'   P={p:6d}  p_sig={ps[i+1]:6d}  rho={rho:.5f}  resto >= {ps[i+1]*rho*rho:.4f}')

    print('\n== B. Totalidad = bloque de primos (d | M_P) ==')
    for P in (5, 7, 11, 13, 17):
        pp = primes_upto(P); idx, mu = divisors(pp); M = math.prod(pp)
        G, b = build(idx); d = np.array(idx, float)
        print(f' P={P} dim={len(idx)} óptimo libre={1 - b @ np.linalg.solve(G, b):.5f}')
        for name, w in [('herencia   w=1', np.ones_like(d)), ('celda      w=1/d', 1 / d),
                        ('por resolver w=1-log d/log M', 1 - np.log(d) / math.log(M))]:
            c = -mu * w
            e1, _ = err(G, b, c, 1.0); es, a = err(G, b, c)
            print(f'    {name:30s} sin ajuste: {e1:.5f}   con escala a*={a:.3f}: {es:.5f}')

    print('\n== C. Totalidad = tamaño N contra la unidad (d libre de cuadrados, d <= N) ==')
    for N in (30, 100, 300, 1000, 3000):
        idx = [x for x in range(1, N + 1) if mu_of(x) != 0]
        mu = np.array([mu_of(x) for x in idx], float); d = np.array(idx, float)
        G, b = build(idx)
        row = []
        for name, w in [('herencia', np.ones_like(d)), ('por resolver', 1 - np.log(d) / math.log(N))]:
            c = -mu * w
            e1, _ = err(G, b, c, 1.0)
            row.append(f'{name}: {e1:.4f}')
        print(f' N={N:5d} dim={len(idx):4d}  sin ajuste -> ' + '   '.join(row), flush=True)

    print('\n== D. Regla "por resolver" en la escala N: resto exacto en [1,N] ==')
    print('   resto[1,N] = S / log^2 N,  S = int_1^N (psi(u) - beta_N u)^2 / u^2 du  (fluctuación acumulada)')
    for N in (10**3, 10**4, 10**5, 10**6, 10**7):
        beta, S, piece, p0 = tramo(N)
        print(f'   N=10^{round(math.log10(N))}  S={S:.3f}  resto[1,N]={piece:.4f}  [0,1)={p0:.4f}  suma={piece+p0:.4f}', flush=True)
