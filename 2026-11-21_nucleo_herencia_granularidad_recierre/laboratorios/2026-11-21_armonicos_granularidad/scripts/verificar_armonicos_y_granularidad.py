#!/usr/bin/env python3
"""Ensayo A–G–01: aritmética exacta; biblioteca estándar solamente."""
from fractions import Fraction
from math import isqrt

TRIPLES = [(2, 2, 3), (4, 8, 9), (12, 12, 17), (70, 70, 99)]

def qcell(n: int, K: int) -> int:
    assert n >= 1 and K >= 1
    return K*K // n

def ratio(n: int, K: int) -> Fraction:
    return Fraction(K*K, n*(n+1))

def radius(n: int) -> Fraction:
    return Fraction(1, n)

def grano(K: int) -> Fraction:
    return Fraction(1, K*K)

def umbral(K: int, theta: Fraction) -> int:
    """Primer entero n≥1 con n(n+1)≥K²/theta, por búsqueda entera."""
    assert 0 < theta <= 1
    # n(n+1) >= K*K * theta.denominator/theta.numerator
    goal = K*K*theta.denominator
    p = theta.numerator
    n = max(1, isqrt(goal // p))
    while n > 1 and (n-1)*n*p >= goal:
        n -= 1
    while n*(n+1)*p < goal:
        n += 1
    return n

def main():
    tested = 0
    print('LABORATORIO A-G-01 / ARMONICOS Y GRANULARIDAD / 2026-11-21')
    print('K | n | delta/g | Q(n), Q(n+1) | misma celda')
    for a,b,K in TRIPLES:
        assert a*a+b*b+1 == K*K
        assert Fraction(a*a+b*b,K*K)+Fraction(1,K*K)==1
        for n in (K, K*K, K*K+1):
            delta = radius(n)-radius(n+1)
            assert delta == Fraction(1,n*(n+1))
            assert delta/grano(K) == ratio(n,K)
            Qn, Qnext = qcell(n,K), qcell(n+1,K)
            assert Qn == int(radius(n)/grano(K))
            same = Qn == Qnext
            assert same == (n==K*K+1)
            print(f'{K:2} | {n:5} | {str(ratio(n,K)):>11} | {Qn:2}, {Qnext:2} | {"SI" if same else "NO"}')
            tested += 1
        assert ratio(K,K) == Fraction(K,K+1)
        assert ratio(K*K,K) == Fraction(1,K*K+1)
        assert qcell(K*K,K)==1 and qcell(K*K+1,K)==0
        assert qcell(K*K+1,K)==qcell(K*K+2,K)==0
        for n in range(K*K+1, K*K+1+200):
            assert qcell(n,K)==0
        theta = Fraction(1,2)
        nmin = umbral(K,theta)
        assert ratio(nmin,K) <= theta
        assert nmin==1 or ratio(nmin-1,K)>theta
        print('  Umbral theta=1/2:',nmin, 'ratio:',ratio(nmin,K))
    print(f'PASS: {tested} filas aritmeticas, 4 continuaciones O58, 800 controles de cola y 4 umbrales.')

if __name__=='__main__':
    main()
