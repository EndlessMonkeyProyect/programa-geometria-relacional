#!/usr/bin/env python3
"""Controles exactos de resultados R1/R2/R3/R6 para la versión 2026-11-21.
Solo usa la biblioteca estándar. No sustituye las demostraciones universales.
"""
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from collections import Counter


def mobius_sieve(limit):
    mu = [1] * (limit + 1)
    mu[0] = 0
    primes = []
    composite = [False] * (limit + 1)
    for i in range(2, limit + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            x = i * p
            if x > limit:
                break
            composite[x] = True
            if i % p == 0:
                mu[x] = 0
                break
            mu[x] = -mu[i]
    return mu


def jump(n, N, mu):
    return sum(mu[d] for d in range(1, min(n, N)+1) if n % d == 0)


def test_inheritance():
    for N, h, q in [(7, 3, 11), (36, -7, 5), (1024, 81, 2)]:
        assert F(h, N) == F(q*h, q*N)


def test_O58():
    for a, b, N in [(2, 2, 3), (4, 8, 9), (12, 12, 17)]:
        assert a*a + b*b + 1 == N*N
        assert F(a*a+b*b, N*N) + F(1, N*N) == 1


def test_universal_jump(limit=4096):
    mu = mobius_sieve(2*limit)
    for N in range(1, limit+1):
        # Demostración general en R3; aquí se muestrean N<=4096 con
        # puntos seleccionados y pruebas exhaustivas en escalas relevantes.
        positions = {N+1, min(2*N, N+2), 2*N}
        if N in (1, 2, 8, 16, 32, 64, 128, 256, 1024):
            positions = range(N+1, 2*N+1)
        for n in positions:
            assert jump(n,N,mu) == -mu[n], (N,n,'antes')
            assert jump(n,2*N,mu) == 0, (N,n,'despues')
    active = sum(mu[n]!=0 for n in range(1025,2049))
    null = 1024-active
    assert (active,null)==(621,403), (active,null)
    assert jump(1030,1024,mu)==1
    assert jump(1030,2048,mu)==0
    return active,null


def periodic_energy_formula(coeffs):
    mean = F(1) - sum(coeffs.values(),F())/2
    variance = sum((ca*cb*F(gcd(n,m)**2,12*n*m)
                    for n,ca in coeffs.items()
                    for m,cb in coeffs.items()), F())
    return mean*mean + variance


def periodic_energy_integral(coeffs):
    M=1
    for n in coeffs: M=lcm(M,n)
    integral=F()
    for k in range(M):
        alpha=F(1)-sum((c*F(k%n,n) for n,c in coeffs.items()), F())
        beta=-sum((c/F(n) for n,c in coeffs.items()),F())
        integral += alpha*alpha + alpha*beta + beta*beta/3
    return integral/M


def test_periodic():
    cases = [{1:F(1)}, {1:F(-1),2:F(2)}, {2:F(1,3),3:F(-5,7)},
             {1:F(-2),2:F(1,2),3:F(3,4),6:F(-1,5)}]
    for c in cases:
        q=periodic_energy_formula(c)
        qi=periodic_energy_integral(c)
        assert q==qi, (c,q,qi)
    return len(cases)


def test_projection_identity():
    # chi=(1,2,3), W_m=span(e1), W_n=span(e1,e2)
    chi=(F(1),F(2),F(3))
    error_m=chi[1]**2+chi[2]**2
    error_n=chi[2]**2
    gain=chi[1]**2
    assert error_m-error_n==gain==F(4)


if __name__=='__main__':
    test_inheritance();test_O58();a,b=test_universal_jump();c=test_periodic();test_projection_identity()
    print('R1: transporte racional exacto — OK')
    print('R2: identidades O58 — OK')
    print(f'R3: saltos por escala — OK; N=1024: {a} focos activos, {b} ya nulos')
    print('R4: balance finito de proyecciones — OK')
    print(f'R6: energía periódica racional exacta — OK ({c} familias)')
    print('Resultado: TODOS LOS CONTROLES FINITOS COMPLETADOS')
