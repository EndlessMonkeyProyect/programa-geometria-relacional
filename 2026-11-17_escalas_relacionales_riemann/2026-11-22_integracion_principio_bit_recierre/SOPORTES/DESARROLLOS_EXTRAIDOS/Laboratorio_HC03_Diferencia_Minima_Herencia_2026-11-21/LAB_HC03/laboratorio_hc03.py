#!/usr/bin/env python3
"""LAB-HC-03. Diferencia minima, herencia afirmativa y contraste de cotas.

Reproduce identidades de diferencias con aritmetica racional por etiquetas de primos,
compara acumulados hasta 2 millones, y evalua un criterio de bloques equivalente
(al nivel de orden) a RH. Nunca infiere teoremas asintoticos de datos finitos.
Solo biblioteca estandar. Python 3.10+.
"""
from __future__ import annotations
from array import array
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt, log, sqrt, fsum
from pathlib import Path
import csv, json

ROOT=Path(__file__).resolve().parent
LIMIT=2_000_000


def sieve(N):
    b=bytearray(b'\x01')*(N+1)
    b[0:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if b[p]: b[p*p:N+1:p]=b'\x00'*((N-p*p)//p+1)
    return [p for p in range(2,N+1) if b[p]]


def label_coeff_T(N,p):
    """Coeficiente racional de log(p) en T(N), para todas las potencias p^k."""
    ans=Fraction(0)
    q=p
    while q<=N:
        ans+=Fraction(N,q)-1
        if q>N//p: break
        q*=p
    return ans


def exact_symbolic_tests(primes):
    tests=0
    small=[p for p in primes if p<=128]
    for n in range(2,129):
        for p in small:
            if p>n+1: break
            second=(label_coeff_T(n+1,p)-2*label_coeff_T(n,p)
                    +label_coeff_T(n-1,p))
            q=p
            isp=False
            while q<=n:
                if q==n: isp=True; break
                if q>n//p: break
                q*=p
            assert second==(Fraction(1,n) if isp else Fraction(0)), (n,p,second)
            tests+=1
    for N in range(2,151):
        for p in small:
            if p>N:break
            rebuilt=Fraction(0)
            q=p
            while q<N:
                rebuilt+=Fraction(N-q,q)
                if q>(N-1)//p: break
                q*=p
            assert rebuilt==label_coeff_T(N,p),(N,p,rebuilt,label_coeff_T(N,p))
            tests+=1
    return tests


CHARS={
    'mod3':(3,{0:0,1:1,2:-1}),
    'mod4':(4,{0:0,1:1,2:0,3:-1}),
    'mod5quad':(5,{0:0,1:1,2:-1,3:-1,4:1}),
}


def A_twisted(x,S,mod,table):
    M=1
    for p in S:M*=p
    return sum(table[n%mod] for n in range(1,x+1) if gcd(n,M)==1)


def char_tests():
    tests=0
    for mod,table in CHARS.values():
        for S,p in [((),2),((2,),3),((2,3),5),((3,5),2),((2,5),7)]:
            for x in range(1,201):
                lhs=A_twisted(x,(*S,p),mod,table)
                rhs=A_twisted(x,S,mod,table)-table[p%mod]*A_twisted(x//p,S,mod,table)
                assert lhs==rhs,(mod,S,p,x,lhs,rhs)
                tests+=1
        # Twist of impulse: coefficient of log(p) in delta^2 T_chi(n).
        for n in range(2,101):
            for p in (2,3,5,7,11,13):
                def C(N):
                    return sum((Fraction(N,p**k)-1)*table[p**k%mod]
                              for k in range(1,12) if p**k<=N)
                lhs=C(n+1)-2*C(n)+C(n-1)
                q=p;k=0;expected=Fraction(0)
                while q<=n:
                    k+=1
                    if q==n:
                        expected=Fraction(table[q%mod],n);break
                    if q>n//p:break
                    q*=p
                assert lhs==expected,(mod,n,p,lhs,expected)
                tests+=1
    return tests


def n_rho(n):
    """n*(Delta^2[n log n] - 1/n), serie absolutamente convergente.
    Integral triangular: sum_{m>=1} 2 / [(2m+1)(2m+2)n^(2m)].
    """
    total=0.0
    q=1.0/(n*n)
    for m in range(1,31):
        term=2.0*q/((2*m+1)*(2*m+2))
        total+=term
        if term<2e-18: break
        q/=n*n
    return total


def prime_powers_event(primes,N):
    lam=array('d',[0.0])*(N+1)
    pcnt=0
    for p in primes:
        w=log(p)
        q=p
        while q<=N:
            lam[q]=w
            if q>N//p:break
            q*=p;pcnt+=1
    return lam,pcnt


def num_diff_tests(lam,N):
    # Avoid cancellation of huge linear terms by testing on moderate n.
    psi=0.0
    over_n=0.0
    T=array('d',[0.0])*(10002)
    for n in range(1,10002):
        psi+=lam[n]
        over_n+=lam[n]/n
        T[n]=n*over_n-psi
    err=0.0
    for n in range(2,10001):
        e=abs(T[n+1]-2*T[n]+T[n-1]-lam[n]/n)
        err=max(err,e)
    assert err<1e-9,err
    return err


def sieve_survivor_tests(primes):
    """Sieve at sqrt(x): survivors {1} U {p>sqrt(x)}. Exactly, by divisibility."""
    count=0
    checks=[]
    for x in (100,1000,10000,100000):
        z=isqrt(x)
        small=[p for p in primes if p<=z]
        survivors={n for n in range(2,x+1)
                   if all(n%p for p in small)}
        expected={p for p in primes if z<p<=x}
        assert survivors==expected,(x,len(survivors),len(expected),len(survivors^expected))
        sum_generation=fsum(log(n) for n in survivors)
        theta_total=fsum(log(p) for p in primes if p<=x)
        theta_old=fsum(log(p) for p in small)
        err=abs(sum_generation+theta_old-theta_total)
        assert err<1e-8,(x,err)
        checks.append(dict(x=x,limite_heredado=z,nuevos=len(survivors),
                           error_logaritmico=err))
        count+=x-1
    return count,checks


def main():
    primes=sieve(LIMIT)
    lam,power_extra=prime_powers_event(primes,LIMIT)
    exact=exact_symbolic_tests(primes)
    twisted=char_tests()
    survivor_count,survivor_checks=sieve_survivor_tests(primes)
    diff_error=num_diff_tests(lam,LIMIT)
    psi=0.0
    theta=0.0
    cnt=0
    checkpoints={100,1000,10000,100000,1000000,LIMIT}
    rows=[]
    blockrows=[]
    j=1
    block_start=2**j
    B=0.0
    block_max=0.0
    block_where=0
    S=0.0
    peak_global=0.0
    R=0.0
    J=0.0
    max_curv_err=0.0
    for n in range(2,LIMIT+1):
        delta=lam[n]
        psi+=delta
        S+=delta-1.0
        q=n_rho(n)
        R+=q
        J+=delta-1.0-q
        max_curv_err=max(max_curv_err,abs((J-1.0+R)-(psi-n)))
        assert 0.0<R<0.125
        while n >= 2**(j+1):
            # Complete previous block. Terminal block n-1 is correct.
            b_n=2**j
            norm=block_max/(sqrt(b_n)*(j+1)**2)
            blockrows.append(dict(j=j,inicio=b_n,fin=n-1,
                     sup_parcial=block_max,donde=block_where,
                     razon_certificado=norm))
            j+=1;B=0.0;block_max=0.0;block_where=0
        B+=delta-1.0
        if abs(B)>block_max: block_max=abs(B);block_where=n
        peak_global=max(peak_global,abs(S)/sqrt(n))
        if n in checkpoints:
            rows.append(dict(N=n,psi=psi,referencia_N=n,discrepancia_psi_menos_N=psi-n,
                 nuevo_contra_referencia=S,normalizado_sqrt=(psi-n)/sqrt(n),
                 normalizado_RH=(psi-n)/(sqrt(n)*(log(n)**2)),
                 suma_local=psi/n,
                 J_curvatura=J,R_referencia=R,
                 reconstruccion_diferencia_minima=J-1.0+R))
    blockrows.append(dict(j=j,inicio=2**j,fin=LIMIT,
              sup_parcial=block_max,donde=block_where,
              razon_certificado=block_max/(sqrt(2**j)*(j+1)**2)))
    # Separate auxiliary arrays for chart and a larger set of block metrics.
    with (ROOT/'escalas.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    with (ROOT/'bloques_diadicos.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(blockrows[0]));w.writeheader();w.writerows(blockrows)
    # Effect of modifying prime-power weights without changing positions of primes or descendants.
    # w(p^k)=log(p)+1, so psi_modified(x)=psi(x)+number_of_prime_powers_up_to_x.
    selected={1000,10000,100000,1000000,LIMIT}
    n_powers=0;psi=0.0
    modrows=[]
    for n in range(2,LIMIT+1):
        psi+=lam[n]
        if lam[n]>0:n_powers+=1
        if n in selected:
            modrows.append(dict(N=n,cantidad_potencias_primas=n_powers,
                discrepancy_original=psi-n,
                discrepancia_pesos_ajustados=psi+n_powers-n,
                cambio=n_powers,
                cambio_sobre_sqrt=n_powers/sqrt(n)))
    with (ROOT/'control_pesos.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(modrows[0]));w.writeheader();w.writerows(modrows)

    metadata=dict(limite=LIMIT,primos=len(primes),
             potencias_con_exponente_mayor_igual_2=power_extra,
             pruebas_fracciones_exactas=exact,
             pruebas_caracteres_exactas=twisted,
             pruebas_criba_identificacion=survivor_count,
             casos_identificacion=survivor_checks,
             mayor_error_segunda_diferencia_numerica=diff_error,
             max_cociente_global_observado=peak_global,
             correccion_curvatura_acumulada_N_2M=R,
             max_error_reconstruccion_curvatura=max_curv_err,
             cota_analitica_correccion_curvatura=0.125,
             max_razon_bloques_observada=max(r['razon_certificado'] for r in blockrows),
             ultimo_bloque=blockrows[-1],observaciones=rows,control_pesos=modrows)
    (ROOT/'resumen.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(metadata,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
