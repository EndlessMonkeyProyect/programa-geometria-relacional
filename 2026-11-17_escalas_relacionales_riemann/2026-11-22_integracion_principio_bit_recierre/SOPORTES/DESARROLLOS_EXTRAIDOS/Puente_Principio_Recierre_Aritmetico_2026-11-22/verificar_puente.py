#!/usr/bin/env python3
"""Control exacto (enteros): defecto local de Mobius y desbalance de octavas.
No demuestra RH: las cotas que RH requiere siguen abiertas.
"""
import csv
from math import isqrt
from pathlib import Path

OUT=Path(__file__).resolve().parent
MAX_J=17
LIMIT=2**(MAX_J+1)


def mobius_sieve(limit):
    mu=[1]*(limit+1)
    is_prime=bytearray(b'\x01')*(limit+1)
    is_prime[0]=is_prime[1]=0
    for p in range(2,isqrt(limit)+1):
        if is_prime[p]:
            for k in range(p*p,limit+1,p):
                is_prime[k]=0
    for p in range(2,limit+1):
        if is_prime[p]:
            for k in range(p,limit+1,p):
                mu[k]*=-1
            sq=p*p
            if sq<=limit:
                for k in range(sq,limit+1,sq):
                    mu[k]=0
    return mu

mu=mobius_sieve(LIMIT)
assert mu[1]==1
# Check the divisor exact-recierre identity on every octave through 4096.
checks=0
for j in range(1,12):
    N=2**j
    for m in range(N+1,2*N+1):
        defect=sum(mu[d] for d in range(1,N+1) if m%d==0)
        closure=sum(mu[d] for d in range(1,2*N+1) if m%d==0)
        assert defect==-mu[m], (N,m,defect,mu[m])
        assert closure==0, (N,m,closure)
        checks+=2

rows=[]
for j in range(4,MAX_J+1):
    N=2**j
    A=S=max_abs=0
    max_at=N
    for n in range(N+1,2*N+1):
        a=mu[n]
        A+=a*a
        S+=a
        if abs(S)>max_abs:
            max_abs=abs(S)
            max_at=n
    # Signed populations: number of squarefree n with odd/even prime factor count
    plus=(A+S)//2
    minus=(A-S)//2
    assert plus-minus==S and plus+minus==A
    assert abs(S)<=A
    # exact pair-correlation identity: S^2 = A + 2*sum_{n<m} mu(n)mu(m)
    pair=(S*S-A)//2
    assert 2*pair+A==S*S
    rows.append((j,N,2*N,A,plus,minus,S,max_abs,max_at,round(max_abs/(N**.5),6),pair))

with (OUT/'datos_bloques.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['j','N','2N','cantidad_libres_cuadrados','mu_positivos','mu_negativos','suma_mu_bloque','maximo_prefijo_abs','posicion_maximo','maximo_prefijo_sobre_raiz_N','correlacion_pares'])
    w.writerows(rows)
print('CONTRASTES ENTEROS EXACTOS')
print('identidades recierre/local: ',checks,'verificadas')
print('j | N | libres_cuadrados | sum_mu | max_prefijo | ratio_max/sqrt(N)')
for row in rows:
    j,N,_,A,plus,minus,S,B,m,r,pair=row
    print(f'{j:2d} {N:7d} {A:7d} {S:6d} {B:6d} {r:10.4f}')
print('TODOS LOS CONTROLES SUPERADOS; esto no es una cota universal.')
