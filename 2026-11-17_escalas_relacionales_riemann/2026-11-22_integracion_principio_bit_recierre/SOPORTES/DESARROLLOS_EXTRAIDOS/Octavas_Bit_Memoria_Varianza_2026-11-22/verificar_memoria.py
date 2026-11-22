#!/usr/bin/env python3
"""Verificaciones exactas de fases y covarianzas; evaluacion numerica de la trayectoria diagonal."""
from fractions import Fraction
from math import lcm, log, lgamma, sqrt
from pathlib import Path


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n-p*p)//p)+1)
    return [p for p in range(2, n+1) if sieve[p]]


def powers(n, plist):
    out=[]
    for p in plist:
        if p>n: break
        q=p
        a=1
        while q<=n:
            out.append((p,a,q))
            q*=p
            a+=1
    return out


def c(q,t):
    return int(2*(t%q)>=q)


def mean(q):
    return Fraction(q//2,q)


def analytical_cov(p,a,q, r,b,Q):
    if q==Q:
        v=mean(q)
        return v*(1-v)
    if p!=r or p==2:
        return Fraction(0)
    if q>Q:
        q,Q=Q,q
    return Fraction(q*q-1,4*q*Q)


def exact_cov(q,Q):
    n=lcm(q,Q)
    jointly=sum(c(q,t)*c(Q,t) for t in range(n))
    return Fraction(jointly,n)-mean(q)*mean(Q)


checks=0
plist=primes_upto(131072)
for X in (3,6,12,20,30,48,64,90):
    pp=powers(X,plist)
    for i,(p,a,q) in enumerate(pp):
        for r,b,Q in pp[i:]:
            assert analytical_cov(p,a,q,r,b,Q)==exact_cov(q,Q), (p,a,q,r,b,Q)
            checks+=1

for m in range(1,5001):
    for a in range(1,17):
        assert c(2**(a+1),2*m)==c(2**a,m)
        checks+=1
    assert sum(c(2**a,2*m) for a in range(1,18))==sum(c(2**a,m) for a in range(1,18))
    checks+=1

# Correctitud de los indicadores y la cota de varianza por bloques fijos.
def stats(X):
    pp=powers(X,plist)
    mu=sum(log(p)*float(mean(q)) for p,a,q in pp)
    psi=sum(log(p) for p,a,q in pp)
    v=sum((log(p)**2)*float(analytical_cov(p,a,q,p,a,q)) for p,a,q in pp)
    for i,(p,a,q) in enumerate(pp):
        for r,b,Q in pp[i+1:]:
            if p==r and p!=2:
                v+=2*log(p)**2*float(analytical_cov(p,a,q,r,b,Q))
    return mu,v,psi

rows=[]
for X in (16,32,64,128,512,2048,8192,32768,65536):
    mu,v,psi=stats(X)
    assert v<=0.5*psi*log(X)+1e-7
    q2=powers(2*X,plist)
    psi2=sum(log(p) for p,a,q in q2)
    H=lgamma(2*X+1)-2*lgamma(X+1)-(psi2-psi)
    diff=mu-H
    z=abs(diff)/sqrt(v)
    rows.append((X,H/X,mu/X,diff/X,sqrt(v)/X,z))
    checks+=1

# Comparacion con la suma directa sobre un periodo completo para X pequeno.
for X in (4,8,10,12):
    pp=powers(X,plist)
    P=1
    for k in range(1,X+1): P=lcm(P,k)
    assert P<=30000
    data=[sum(log(p)*c(q,t) for p,a,q in pp) for t in range(P)]
    mean_data=sum(data)/P
    var_data=sum((t-mean_data)**2 for t in data)/P
    mu,v,psi=stats(X)
    assert abs(mean_data-mu)<1e-9
    assert abs(var_data-v)<1e-8
    checks+=2

with Path(__file__).with_name('RESULTADOS.txt').open('w',encoding='utf-8') as out:
    out.write('Verificador: memoria binaria, covarianzas exactas y varianza de ciclo fijo\n')
    out.write(f'Controles superados: {checks}\n')
    out.write('X | H_X(X)/X | media_X/X | (media-H)/X | sigma_X/X | distancia_en_sigmas\n')
    for x,*nums in rows:
        out.write(str(x)+' | '+' | '.join(f'{v:.8f}' for v in nums)+'\n')
print('OK',checks)
for x,*nums in rows: print(x,*[round(v,6) for v in nums])
