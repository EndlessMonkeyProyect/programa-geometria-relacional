"""Controles exactos del marco D1-D7. No constituye prueba de RH."""
from math import gcd, lcm, comb
from fractions import Fraction
from collections import Counter
import json
from pathlib import Path

LIMIT=1024
TOP=2*LIMIT+2
spf=list(range(TOP+1))
for p in range(2,int(TOP**0.5)+1):
    if spf[p]==p:
        for k in range(p*p,TOP+1,p):
            if spf[k]==k:spf[k]=p

def power_base(n):
    if n<2:return 1
    p=spf[n]
    while n%p==0:n//=p
    return p if n==1 else 1

L=[1]*(TOP+1)
r=[1]*(TOP+1)
for n in range(1,TOP+1):
    L[n]=lcm(L[n-1],n)
    r[n]=L[n]//L[n-1]
    assert r[n]==power_base(n)
    assert r[n]==n//gcd(n,L[n-1])

checks=0
for n in range(2,TOP+1):
    t=1
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            t*=r[d]
            if d*d!=n:t*=r[n//d]
    assert t==n
    checks+=1

prime_powers=[]
for n in range(2,TOP+1):
    if r[n]!=1:prime_powers.append((n,r[n]))

AA=[0]*(LIMIT+2)
BB=[0]*(LIMIT+2)
for m in range(1,LIMIT+2):
    a=L[2*m]//L[m]
    c=comb(2*m,m)
    assert c%a==0
    b=c//a
    b_alt=1
    for q,p in prime_powers:
        if q>m:break
        if 2*(m%q)>=q:b_alt*=p
    assert b==b_alt
    # A has at most one occurrence of each prime.
    factors=set()
    for q,p in prime_powers:
        if m<q<=2*m:
            assert p not in factors
            factors.add(p)
    assert a==__import__('math').prod(factors)
    AA[m],BB[m]=a,b
    checks+=1

for m in range(1,LIMIT+1):
    assert AA[m+1]*r[m+1]==AA[m]*r[2*m+1]*r[2*m+2]
    r_odd=lambda n:(r[n] if r[n]%2==1 else 1)
    assert BB[m+1]*(m+1)*r[2*m+1]==BB[m]*2*(2*m+1)*r_odd(m+1)
    v2=lambda n:(n & -n).bit_length()-1
    assert v2(BB[m])==m.bit_count()-1
    checks+=3

# D3: cada rampa racional tiene segunda diferencia centrada 1/k en n=k, cero fuera.
for k in range(2,90):
    def w(t):return max(Fraction(t,k)-1, Fraction(0))
    for n in range(2,98):
        d=w(n+1)-2*w(n)+w(n-1)
        assert d==(Fraction(1,k) if n==k else 0)
        checks+=1

# D6: cota óptima para potencias primas q<=49, ventanas variadas, con cálculo racional exacto.
for q,p in prime_powers:
    if q>49:break
    h=q//2
    def c(x):return int((x%q)>=((q+1)//2))
    sharp=Fraction(h*(q-h),q)
    observed=Fraction(0)
    for a in range(q):
        for N in range(1,2*q+1):
            count=sum(c(m) for m in range(a,a+N))
            d=abs(Fraction(count,1)-Fraction(N*h,q))
            assert d<=sharp
            if d>observed:observed=d
            checks+=1
    assert observed==sharp,(q,observed,sharp)

# D7: ley binomial binaria para J<=9, usando la expresión exacta de A,B.
for J in range(1,10):
    cnt=Counter(m.bit_count()-1 for m in range(2**J,2**(J+1)))
    for k in range(J+1):assert cnt[k]==comb(J,k)
    checks+=J+1

# D4 CRT ejemplo.
assert sum(1 for n in range(72) if n%8>=4 and n%9>=5)==16
print(json.dumps({'controles_exactos':checks,'escalas':LIMIT,'ventanas_hasta_q':49,'crt_8_9':16,'estado':'APROBADO'},ensure_ascii=False,indent=2))
