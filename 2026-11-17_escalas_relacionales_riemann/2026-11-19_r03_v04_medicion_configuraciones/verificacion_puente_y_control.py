#!/usr/bin/env python3
"""Controls for R03 v0.4: exact squarefree bridge and shifted completed zeta.
Dependencies: mpmath. Contrasting numerical values is not a proof of RH.
"""
from fractions import Fraction
from itertools import combinations
import math
from mpmath import mp
mp.dps=45

# Exact rational verification of h_S(t)=sum mu(d) f_d(t)
def fracpart(x):return x-(x.numerator//x.denominator)
def check(S, t):
    M=math.prod(S); delta=Fraction(math.prod(p-1 for p in S),M)
    y=1/t
    A=sum(math.gcd(n,M)==1 for n in range(1,y.numerator//y.denominator+1))
    h=-(Fraction(A)-y*delta)
    rhs=Fraction(0)
    for k in range(len(S)+1):
        for I in combinations(S,k):
            d=math.prod(I)
            rhs+=(-1)**k*fracpart(1/(t*d))
    assert h==rhs,(S,t,h,rhs)
    return h
for S in ([],[2],[2,3],[2,3,5],[2,3,5,7]):
    for t in [Fraction(1,n) for n in range(2,50)]+[Fraction(n,d) for n,d in ((2,7),(3,11),(5,29),(7,33))]:check(S,t)
print('PASS: rational Möbius/inverse-reference bridge; 5 prime sets x 52 points')

# Completed function with reflection and a genuine (shifted) Euler product.
a=mp.mpf('0.2');rho=mp.zetazero(1)
def xi(s):return (s*(s-1)/2)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
def H(s):return xi(s+a)*xi(s-a)
for s in [mp.mpc('.28','1.4'), mp.mpc('.72','4.1'),mp.mpc('.45','-2.8')]:
    assert abs(H(s)-H(1-s))<mp.mpf('1e-35')
    assert abs(H(mp.conj(s))-mp.conj(H(s)))<mp.mpf('1e-35')
for s in [rho-a,rho+a]:
    assert abs(s.real-mp.mpf('0.5'))>mp.mpf('0.19')
    assert abs(H(s))<mp.mpf('1e-35')
    print('off-line zero of shifted completed product:',mp.nstr(s,22))
for s in [mp.mpf('2.4'),mp.mpc('2.2','0.5')]:
    lhs=mp.zeta(s+a)*mp.zeta(s-a)
    # Check truncated product, not as equality without tail: use 1000 primes
    sieve=[True]*8000;sieve[0]=sieve[1]=False
    for i in range(2,math.isqrt(7999)+1):
        if sieve[i]:
            for j in range(i*i,8000,i):sieve[j]=False
    ps=[i for i,v in enumerate(sieve) if v]
    approx=mp.fprod((1-mp.power(p,-s-a))**(-1)*(1-mp.power(p,-s+a))**(-1) for p in ps)
    assert abs(lhs-approx)/abs(lhs)<mp.mpf('.005')
print('PASS: completed shifted-zeta control with Euler product and off-line zeros')
print('Interpretation: no standard primitive-L-function assumptions are claimed.')
