#!/usr/bin/env python3
"""Auditoría exacta + intervalos racionales del puente aritmético a Goldbach.

Alcance: función escalón ilustrativa w_N(n)=1 para N/3<=n<=2N/3.
Identidades combinatorias exactas para cada par N<=1000, junto con intervalos
rigorosos para logaritmos. NO verifica hipótesis de operadores de Hardy, GRH,
Goldbach general, ni la fórmula del operador T_N para pesos no suaves.
Sólo biblioteca estándar Python.
"""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from math import gcd, isqrt
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING

LIMIT=1000
M=24  # términos de la serie de atanh; cota rigurosa explícita.


def spf_table(K):
    spf=list(range(K+1))
    for p in range(2,isqrt(K)+1):
        if spf[p]==p:
            for n in range(p*p,K+1,p):
                if spf[n]==n: spf[n]=p
    return spf

SPF=spf_table(30000)


def base_prime_power(n):
    """p si n=p^k (k>=1), None en otros casos."""
    if n<2: return None
    p=SPF[n]
    while n%p==0: n//=p
    return p if n==1 else None


def isprime(n):
    return n>=2 and SPF[n]==n


def units(N):
    return [x for x in range(1,N) if gcd(x,N)==1]


def active_vector(N):
    return {n:base_prime_power(n) for n in units(N)
            if N<=3*n<=2*N and base_prime_power(n) is not None}


def sym_coeffs(N):
    """Polinomios exactos en los símbolos log(p), con coeficientes racionales.
    D=||a||^2, G=<a,Ja>, Q=2||P_-a||^2.
    """
    v=active_vector(N)
    D=defaultdict(F); G=defaultdict(F); Q=defaultdict(F)
    key=lambda x,y:tuple(sorted((x,y)))
    for n,p in v.items():
        D[(p,p)]+=F(1,N)
        q=v.get(N-n)
        if q is not None: G[key(p,q)]+=F(1,N)
    for n in units(N):
        p=v.get(n); q=v.get(N-n)
        if p is not None: Q[(p,p)]+=F(1,2*N)
        if q is not None: Q[(q,q)]+=F(1,2*N)
        if p is not None and q is not None: Q[key(p,q)]-=F(1,N)
    clean=lambda d:{k:v for k,v in d.items() if v}
    E=defaultdict(F)
    for k,vv in D.items(): E[k]+=vv
    for k,vv in G.items(): E[k]-=vv
    assert clean(E)==clean(Q),(N,clean(E),clean(Q))
    haspair=any((N-n in v) for n in v)
    assert bool(G)==haspair
    # Separar parejas de primos y de potencias propias en el polinomio G.
    PP=defaultdict(F); R=defaultdict(F)
    for n,p in v.items():
        q=v.get(N-n)
        if q is None: continue
        dst=PP if isprime(n) and isprime(N-n) else R
        dst[key(p,q)]+=F(1,N)
    assert clean({k:PP[k]+R[k]-G[k] for k in set(PP)|set(R)|set(G)})=={}
    return clean(D),clean(G),clean(Q),clean(PP),clean(R),v


@lru_cache(maxsize=None)
def log_interval(n):
    """[L,U] racional exacto: 2*atanh((t-1)/(t+1)) + k log 2.
    Restante <= 2 y^(2M+1)/((2M+1)(1-y^2)).
    """
    assert n>=1
    if n==1: return F(0),F(0)
    k=n.bit_length()-1
    t=F(n,2**k)
    def estimate(y):
        ys=y*y; power=y; series=F(0)
        for j in range(M):
            series+=2*power/F(2*j+1)
            power*=ys
        remaining=2*power/(F(2*M+1)*(1-ys)) if ys<1 else None
        return series,series+remaining
    l,u=estimate((t-1)/(t+1))
    l2,u2=estimate(F(1,3))
    return l+k*l2,u+k*u2


def poly_interval(poly):
    """Intervalo racional de un polinomio en log(p) (coef. con signo)."""
    lo=F(0); hi=F(0)
    for (p,q),c in poly.items():
        lp,up=log_interval(p); lq,uq=log_interval(q)
        productlo=lp*lq; producthi=up*uq
        if c>=0:
            lo+=c*productlo; hi+=c*producthi
        else:
            lo+=c*producthi; hi+=c*productlo
    return lo,hi


def fmt_fraction_interval(interval, digits=13):
    low,up=interval
    with localcontext() as cx:
        cx.prec=80;cx.rounding=ROUND_FLOOR
        val_lo=Decimal(low.numerator)/Decimal(low.denominator)
    with localcontext() as cx:
        cx.prec=80;cx.rounding=ROUND_CEILING
        val_hi=Decimal(up.numerator)/Decimal(up.denominator)
    fmt=f'.{digits}f'
    with localcontext() as cx:
        cx.prec=80;cx.rounding=ROUND_FLOOR
        a=format(val_lo,fmt)
    with localcontext() as cx:
        cx.prec=80;cx.rounding=ROUND_CEILING
        b=format(val_hi,fmt)
    return f'[{a}, {b}]'


def test_Q_N():
    for N in (4,6,10,30,42):
        for K in (1,N-1,N,N+1,2*N-1,2*N,3*N+5):
            nonzero=[len([n for n in range(1,K+1) if n%N==r]) for r in units(N)]
            assert max(nonzero, default=0)==(K+N-1)//N


def test_CRT_N30():
    _,_,_,_,_,v=sym_coeffs(30)
    # Orden: columnas 1,2,3,4 mod 5; filas 1,2 mod 3.
    mat=[[v.get(next(r for r in units(30) if r%3==i and r%5==j)) for j in (1,2,3,4)]
         for i in (1,2)]
    assert mat==[[None,None,13,19],[11,17,None,None]],mat
    # Los pesos son log(p)/sqrt(30); menor cols (1,3) = -log(11)log(13)/30.
    return mat


def test_defect(N=30,p=7,B=3000):
    assert gcd(N,p)==1 and isprime(p)
    for n in range(1,B+1):
        k=base_prime_power(n)
        kp=base_prime_power(n*p)
        if gcd(n,N)>1:
            continue # chi(n)=0
        if n==1: assert kp==p
        elif k==p: assert kp==p
        elif k is not None: assert kp is None
        else: assert kp is None



def C2_certified(B=200000):
    """Cota inferior/superior decimal dirigida del producto gemelo C_2.

    C2=prod_{p>2}(1-1/(p-1)^2), cola >=1-sum_{k>=B}1/k^2
       >= 1-1/(B-1), and <=1. Los contextos dirigen redondeos.
    """
    prime=bytearray(b'\x01')*(B+1)
    prime[0:2]=b'\x00\x00'
    for p in range(2,isqrt(B)+1):
        if prime[p]: prime[p*p:B+1:p]=b'\x00'*(((B-p*p)//p)+1)
    lo=Decimal(1);hi=Decimal(1)
    for p in range(3,B+1,2):
        if not prime[p]: continue
        a=(p-1)**2-1; d=(p-1)**2
        with localcontext() as ctx:
            ctx.prec=55;ctx.rounding=ROUND_FLOOR
            f=Decimal(a)/Decimal(d)
            lo=lo*f
        with localcontext() as ctx:
            ctx.prec=55;ctx.rounding=ROUND_CEILING
            f=Decimal(a)/Decimal(d)
            hi=hi*f
    with localcontext() as ctx:
        ctx.prec=55;ctx.rounding=ROUND_FLOOR
        lo=lo*(Decimal(B-2)/Decimal(B-1))
    return lo,hi


def c2_gap30_interval():
    """Intervalo de c_{step}S(30)-G_step(30), c_step=1/3.
       El resultado NO se identifica con una forma del operador de Hardy.
    """
    c2lo,c2hi=C2_certified()
    _,G,_,_,_,_=sym_coeffs(30)
    glo,ghi=poly_interval(G)
    with localcontext() as ctx:
        ctx.prec=55;ctx.rounding=ROUND_CEILING
        gd_hi=Decimal(ghi.numerator)/Decimal(ghi.denominator)
    with localcontext() as ctx:
        ctx.prec=55;ctx.rounding=ROUND_FLOOR
        gd_lo=Decimal(glo.numerator)/Decimal(glo.denominator)
        slow=Decimal(16)*c2lo/Decimal(9)
        gaplo=slow-gd_hi
    with localcontext() as ctx:
        ctx.prec=55;ctx.rounding=ROUND_CEILING
        shi=Decimal(16)*c2hi/Decimal(9)
        gaphi=shi-gd_lo
    return (c2lo,c2hi), (gaplo,gaphi)


def main():
    test_Q_N()
    mat=test_CRT_N30()
    test_defect()
    for N in range(4,LIMIT+1,2):
        sym_coeffs(N)  # 499 casos, polinomios exactos (sin floats)
    print('CERTIFICACIÓN SIMBÓLICA: 499 pares N=4,6,...,1000: OK')
    print('Q_N: norma exacta a partir de multiplicidades de clases: OK')
    print('Defecto primo: soporte en índices n<=3000: OK')
    print('CRT N=30, filas mod 3 y columnas mod 5:',mat)
    print('Intervalos avalados por atanh racional; M=',M)
    for N in (30,42,60,210):
        D,G,Q,PP,R,v=sym_coeffs(N)
        print('N=',N,'soporte=',len(v),'G=',fmt_fraction_interval(poly_interval(G)),
              'D=',fmt_fraction_interval(poly_interval(D)),
              '2||P_-a||²=',fmt_fraction_interval(poly_interval(Q)),
              'G_pp=',fmt_fraction_interval(poly_interval(PP)))
    D,G,Q,_,_,_=sym_coeffs(30)
    assert poly_interval(G)[0]>0
    print('N=30: certificados todos los intervalos por aritmética racional, no por float.')
    c2,gap=c2_gap30_interval()
    print('C2 (Euler finito, cola acotada):',tuple(str(x) for x in c2))
    print('Diagnóstico escalón cstep*S(30)-Gstep(30):',tuple(str(x) for x in gap))
    print('El peso escalón es discontinuo; no verifica la identidad de Hardy de Li-Liu.')


if __name__=='__main__': main()
