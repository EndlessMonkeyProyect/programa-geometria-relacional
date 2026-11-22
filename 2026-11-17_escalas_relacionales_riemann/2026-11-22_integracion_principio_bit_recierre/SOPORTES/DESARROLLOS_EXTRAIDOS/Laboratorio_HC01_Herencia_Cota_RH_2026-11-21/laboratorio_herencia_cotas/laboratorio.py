#!/usr/bin/env python3
"""Laboratorio de puente: herencia de primos a cota ponderada unilateral.
Solo biblioteca estandar. Python >= 3.9. Ninguna afirmacion de RH.
"""
import csv
import bisect
import math
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
N=1_000_000

def sieve(n):
    prime = bytearray(b'\x01') * (n+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,math.isqrt(n)+1):
        if prime[p]:
            prime[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    primes = [i for i in range(2,n+1) if prime[i]]
    return prime,primes

def psi_ritz(x,primes,cutoff=0):
    # T(x) from exact enumeration of prime powers and the Riesz weight (x/n - 1)
    a=[]
    for p in primes:
        if p>x: break
        if p<=cutoff: continue
        q=p
        lp=math.log(p)
        while q<=x:
            a.append(lp*(x/q-1.0))
            if q>x//p: break
            q*=p
    return math.fsum(a)

def inherited_exact_terms(x,p):
    # Determines K=floor(log_p(x)) without floating point.
    k=0; q=1
    while q <= x//p:
        q*=p; k+=1
    return k, q

def h_term(x,p):
    k,q=inherited_exact_terms(x,p)
    return math.log(p)*(k + (x/q)/(p-1))

def b_term(x,p):
    k,q=inherited_exact_terms(x,p)
    total=0.0
    power=p
    for _ in range(k):
        total+=math.log(p)*(x/power-1.0)
        power*=p
    return total

def exact_rational_coeff_check():
    # Coefficients for ln(p), testing B_p = a_p*x - H_p as exact rational equation.
    checks=0
    for x in range(2,160):
        for p in (2,3,5,7,11,13,17,19,23):
            if p>x: continue
            k,q=inherited_exact_terms(x,p)
            left=sum((Fraction(x, p**j)-1 for j in range(1,k+1)),Fraction(0))
            right=Fraction(x,p-1)-k-Fraction(x,q*(p-1))
            assert left==right, (x,p,left,right)
            checks+=1
    return checks

def delta_of(primes):
    v=1.0
    for p in primes:v*=1-1/p
    return v

def periodic_energy(primes):
    M=math.prod(primes)
    delta=Fraction(math.prod(p-1 for p in primes),M)
    a=0; integ=Fraction(0)
    for j in range(M):
        # For interval (j,j+1), A_S(x) = count survivors n <= j.
        if j and all(j%p for p in primes): a+=1
        c=Fraction(a)-delta*j
        integ+=c*c - c*delta + delta*delta/3
    lhs=integ/M
    rhs=2**len(primes)*delta/12
    assert lhs==rhs,(primes,lhs,rhs)
    return M, lhs

def main():
    _,ps=sieve(N)
    check=exact_rational_coeff_check()
    energies=[(list(ps[:k]),periodic_energy(ps[:k])) for k in range(1,5)]
    print('Identidad racional B_p=a_p*x-H_p:',check,'pruebas exactas')
    for primes,(m,e) in energies:
        print('Energia',primes,'periodo',m,'promedio exacto',str(e))
    print('pi(10^6) =', len(ps))
    rows=[]
    resumen=[]
    for x in (1_000,10_000,100_000,1_000_000):
        psmall=[p for p in ps if p<=math.isqrt(x)]
        pi_x=sum(p<=x for p in ps)
        z=math.isqrt(x)
        # Independently sieve survivors, not by assuming the Legendre identity.
        mark=bytearray(b'\x01')*(x+1)
        mark[0]=0
        for p in psmall:
            mark[p:x+1:p]=b'\x00'*((x-p)//p+1)
        a_x=sum(mark)
        assert a_x==1+pi_x-len(psmall), (x,a_x,pi_x,len(psmall))
        d=delta_of(psmall)
        E=a_x-d*x
        assert abs((d*x+E+len(psmall)-1)-pi_x)<1e-9
        theta=math.fsum(math.log(p) for p in psmall)
        full=psi_ritz(x,ps)
        G=full-x*(math.log(x)-1-math.euler_gamma) if hasattr(math,'euler_gamma') else full-x*(math.log(x)-1-0.5772156649015328606)
        for cutoff in (2,5,11,z):
            S=[p for p in ps if p<=cutoff]
            aa=math.fsum(math.log(p)/(p-1) for p in S)
            hh=math.fsum(h_term(x,p) for p in S)
            BB=psi_ritz(x,ps,0)-psi_ritz(x,ps,cutoff)
            # the equality is checked independently via exact per-p identity
            assert abs(BB-(x*aa-hh)) < 2e-7, (x,cutoff,BB,x*aa-hh)
            R=psi_ritz(x,ps,cutoff)
            D=R-x*(math.log(x)-1-0.5772156649015328606-aa)
            # G=D-H ; upper unilateral transfer G <= D since H >= 0.
            assert abs((D-hh)-G)<3e-7, (x,cutoff,D-hh,G)
            assert G<=D+3e-7
            rows.append(dict(x=x,z=round(cutoff),k=len(S),delta=d if cutoff==z else '',error_cierre=E if cutoff==z else '',error_sobre_raiz=E/math.sqrt(x) if cutoff==z else '',G=G,G_sobre_raiz=G/math.sqrt(x),D=D,H=hh,H_sobre_raiz=hh/math.sqrt(x),D_sobre_raiz=D/math.sqrt(x),margen_2k=(2**len(S)) if len(S)<100 else 'enorme',pi=pi_x))
            if cutoff==z:
                assert hh >= 2*theta - 1e-7
                resumen.append(dict(x=x,pi=pi_x,primos_heredados=len(S),H=round(hh,6),H_sobre_raiz=round(hh/math.sqrt(x),6),theta_raiz=round(theta,6),H_menos_2theta=round(hh-2*theta,6),H_correccion_sobre_cuberoot=round((hh-2*theta)/(x**(1/3)),6),G=round(G,6),D=round(D,6),D_sobre_raiz=round(D/math.sqrt(x),6),discrepancia_cierre=round(E,6)))
        print('x:',x,'pi:',pi_x,'k:',len(psmall),'E cierre:',round(E,3), 'E/sqrt:',round(E/math.sqrt(x),3),'G:',round(G,3),'G/sqrt:',round(G/math.sqrt(x),3))
    with (HERE/'resultados.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    with (HERE/'resumen.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=resumen[0].keys());w.writeheader();w.writerows(resumen)
    print('Correcto: herencia, identidades, energia, signo, particion y Legendre.')
    print('Guardado:',HERE/'resultados.csv')

if __name__=='__main__':main()
