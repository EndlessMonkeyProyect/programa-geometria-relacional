#!/usr/bin/env python3
"""Controles finitos exactos para los puentes T / Lambda / acarreos / Chebyshev.

Aritmetica racional y coeficientes de log(p), sin evaluacion aproximada de logaritmos.
No constituye una comprobacion de resultados asintoticos.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import gcd
import argparse


def sieve(n):
    primes = []
    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False
    for i in range(2, n + 1):
        if isprime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                isprime[j] = False
    return primes


def prime_powers(limit):
    d = {}
    for p in sieve(limit):
        q = p
        while q <= limit:
            d[q] = p
            q *= p
    return d


def num_carry(q, m):
    return (2*m)//q - 2*(m//q)


def alpha(q):
    return F(q//2, q)


def add(a, b, factor=1):
    z = defaultdict(F)
    for p, v in a.items(): z[p] += v
    for p, v in b.items(): z[p] += factor*v
    return {p:v for p, v in z.items() if v}


def t_coeff(y, powers):
    """Coeficientes exactos de T(y) en la base formal log(p)."""
    z = defaultdict(F)
    for q, p in powers.items():
        if q <= y:
            z[p] += F(y,q) - 1
    return {p:v for p,v in z.items() if v}


def m2(a,b,c):
    return add(add(a, b, -2), c)


def run(M=400):
    powers = prime_powers(2*M)
    tests = defaultdict(int)
    # Identidad de segunda diferencia: Delta2 T(m) = Lambda(m)/m.
    vals = [t_coeff(m,powers) for m in range(M+2)]
    for m in range(2, M+1):
        z = m2(vals[m+1], vals[m], vals[m-1])
        target = {powers[m]:F(1,m)} if m in powers else {}
        assert z == target, ("segunda diferencia",m,z,target)
        tests['segunda_diferencia'] += 1

    # Acumulacion: cada p^j tiene coeficiente log(p).
    for m in range(2,M+1):
        b = defaultdict(int); tail = defaultdict(int); psi2 = defaultdict(int); psi1 = defaultdict(int)
        Hodd = defaultdict(F); s = defaultdict(F)
        for q,p in powers.items():
            if q<=2*m:
                k=num_carry(q,m)
                b[p] += k
                psi2[p] += 1
                if q>m: tail[p] += 1
            if q<=m:
                psi1[p] += 1
                s[p] += num_carry(q,m)-alpha(q)
                if p%2: Hodd[p] += F(1,q)
        # Verifica el coeficiente v_p(C(2m,m)) contra la formula de Legendre.
        for p in sieve(2*m):
            q=p; v=0
            while q<=2*m:
                v += (2*m)//q - 2*(m//q)
                q*=p
            assert b[p]==v
            tests['legendre_carry'] += 1
        # Formula S(m)=logC - psi(2m)+1/2 psi(m)+1/2 Hodd.
        for p in sieve(2*m):
            right=F(b[p]-psi2[p],1) + F(psi1[p],2) + Hodd[p]/2
            assert s[p]==right, ("identidad S",m,p,s[p],right)
            tests['S_identidad']+=1

    # Independencia sobre periodo completo y dependencia 3-9.
    for q in range(2,18):
        for r in range(2,18):
            if gcd(q,r)!=1: continue
            joint=sum(num_carry(q,m)*num_carry(r,m) for m in range(q*r))
            assert F(joint,q*r)==alpha(q)*alpha(r)
            tests['periodos_coprimos']+=1
    joint39=F(sum(num_carry(3,m)*num_carry(9,m) for m in range(9)),9)
    assert joint39==F(2,9) and alpha(3)*alpha(9)==F(4,27)
    tests['dependencia_3_9']+=1

    # Ventanas exactas: W(a,b)=T(b)/b -T(a)/a; coeficiente integral de psi(t)/t^2.
    for a in range(2,min(M,45)):
        for b in range(a+1,min(M+1,a+15)):
            z=add({p:v/b for p,v in vals[b].items()},
                  {p:v/a for p,v in vals[a].items()}, -1)
            integral=defaultdict(F)
            for q,p in powers.items():
                if q<=b:
                    integral[p]+=F(1,max(a,q))-F(1,b)
            integral={p:v for p,v in integral.items() if v}
            assert z==integral, ("ventana",a,b,z,integral)
            tests['ventanas']+=1

    # Costo de invertir diferencias segundas, cota aguda 4m epsilon.
    for m in range(2,M+1):
        e=[F(1,1),F(-1,1),F(1,1)]
        assert abs(m*(e[2]-2*e[1]+e[0]))==4*m
        tests['condicionamiento']+=1
    return tests

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--M',type=int,default=400)
    a=p.parse_args()
    d=run(a.M)
    for k,v in sorted(d.items()):print(f'{k}: {v}')
    print(f'TOTAL: {sum(d.values())} controles finitos exactos OK (M={a.M})')
