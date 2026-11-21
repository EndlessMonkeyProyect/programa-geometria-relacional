#!/usr/bin/env python3
"""Control racional exacto de Q_S = 1 + (2^|S| rho_S)/12.

H_S(u) = sum_{d|M} mu(d) {u/d}; para u en (j,j+1) todos los
pisos floor(u/d) son constantes; H es lineal por tramos.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod


def moment(primes):
    M=prod(primes)
    dd=[]
    for k in range(len(primes)+1):
        for c in combinations(primes,k):
            dd.append((prod(c),(-1)**k))
    slope=sum((F(mu,d) for d,mu in dd),F(0))
    total=F(0)
    for j in range(M):
        a=sum((mu*(F(j,d)-j//d) for d,mu in dd),F(0))
        # integral_0^1 (1+a+s*slope)^2 ds
        total += (1+a)**2+(1+a)*slope+slope*slope/3
    actual=total/M
    rho=prod((1-F(1,p) for p in primes),start=F(1))
    expected=1+F(2**len(primes),12)*rho
    assert slope==rho,(primes,slope,rho)
    assert actual==expected,(primes,actual,expected)
    return M,expected

for ps in [(2,), (2,3), (2,3,5), (2,3,5,7)]:
    M,result=moment(ps)
    print(f'PASS periodo S={ps}, M={M}: Q={result} = {float(result):.9f}')
print('ESTADO: 4 comprobaciones racionales exactas de promedios aprobadas')
