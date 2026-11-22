#!/usr/bin/env python3
"""Certificados exactos: transiciones de herencia, activaciones y ciclos CRT.
Python 3, biblioteca estándar. No depende de RH ni de estadística aleatoria.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
import csv
import json
import sys

BASE = Path(__file__).resolve().parent
M = int(sys.argv[1]) if len(sys.argv)>1 else 2048
if M < 8:
    raise SystemExit('M debe ser al menos 8')
N = 2*M+2

# Eratóstenes y potencias primas: r(n)=p exactamente cuando n=p^j.
comp = bytearray(N+1)
primes=[]
for x in range(2,N+1):
    if not comp[x]:
        primes.append(x)
        if x*x<=N:
            for y in range(x*x,N+1,x): comp[y]=1
power_to_prime={}
prime_powers=[]
for p in primes:
    q=p
    while q<=N:
        power_to_prime[q]=p
        prime_powers.append((q,p))
        q*=p
prime_powers.sort()

r=[1]*(N+1)
L=[1]*(N+1)
for n in range(2,N+1):
    r[n]=power_to_prime.get(n,1)
    L[n]=L[n-1]*r[n]
    assert r[n] == n//gcd(n,L[n-1]), n

exact_checks=0
B_values=[None]*(M+1)
A_values=[None]*(M+1)
rows=[]
for m in range(1,M+1):
    A,rem=divmod(L[2*m],L[m]); assert rem == 0
    C=comb(2*m,m)
    B,rem=divmod(C,A); assert rem==0
    Ccarry=1
    for q,p in prime_powers:
        if q>m:break
        if 2*(m%q)>=q:Ccarry *=p
    assert B==Ccarry, (m,B,Ccarry)
    exact_checks+=1
    assert A==L[2*m]//L[m]
    exact_checks+=1
    for p in primes:
        if p>2*m:break
        if A%p==0: assert (A//p)%p != 0, ('not squarefree',m,p)
    exact_checks+=1
    assert (B & -B) == 2**(m.bit_count()-1), ('binary',m)
    exact_checks+=1
    A_values[m]=A;B_values[m]=B
    if m in (1,2,3,4,5,6,7,8,16,31,32,64,100,128,256,512,1024,2048):
        rows.append({'m':m,'A':str(A),'B':str(B),'v2_B':m.bit_count()-1,
                     'num_primos_incorporados':sum(1 for p in primes if p<=2*m and A%p==0),
                     'binom_digitos':len(str(C))})

for m in range(1,M):
    assert A_values[m+1]*r[m+1] == A_values[m]*r[2*m+1]*r[2*m+2],m
    exact_checks +=1
    assert B_values[m+1]*(m+1)*r[2*m+1]*r[2*m+2] == B_values[m]*2*(2*m+1)*r[m+1],m
    exact_checks +=1
    # La referencia 2 se transmite en ambos lados de la duplicación.
    rodd = r[m+1] if r[m+1]!=2 else 1
    assert B_values[m+1]*(m+1)*r[2*m+1] == B_values[m]*2*(2*m+1)*rodd,m
    exact_checks +=1

# Independencia exacta CRT para potencias primas de bases distintas, sobre un ciclo completo.
small_powers=[(q,p) for q,p in prime_powers if q<=36]
crt_rows=[]
for i,(q,p) in enumerate(small_powers):
    for t,ell in small_powers[i+1:]:
        if p==ell: continue
        count=sum(1 for m in range(q*t) if 2*(m%q)>=q and 2*(m%t)>=t)
        target=(q//2)*(t//2)
        assert count==target,(q,t,count,target)
        exact_checks+=1
        crt_rows.append({'q':q,'p':p,'r':t,'ell':ell,'periodo':q*t,
                         'coactivaciones':count,'producto_frecuencias':target})

# Dentro de una misma familia prima la independencia puede fallar: 3 y 9.
q,t=3,9
both=sum(2*(m%q)>=q and 2*(m%t)>=t for m in range(t))
assert both==2
cov=Fraction(both,t)-Fraction(q//2,q)*Fraction(t//2,t)
assert cov==Fraction(2,27)
exact_checks+=1

# Independencia exacta de los bloques de potencias de distintos primos en un ciclo L(Q).
# Q=12, L(12)=27720: verificacion entera de todos los productos cruzados.
from math import lcm
Q=12
period=1
for j in range(1,Q+1): period=lcm(period,j)
assert period==27720
blocks={}
for p in primes:
    if p>Q: break
    powers=[q for q,b in prime_powers if q<=Q and b==p]
    blocks[p]=[sum(2*(m%q)>=q for q in powers) for m in range(period)]
block_checks=0
for p in blocks:
    for q in blocks:
        if p>=q:continue
        cross=sum(a*b for a,b in zip(blocks[p],blocks[q]))
        assert period*cross==sum(blocks[p])*sum(blocks[q]),(p,q)
        exact_checks+=1
        block_checks+=1

# Binario: para m en [2^J,2^(J+1)), v_2 B sigue exactamente la ley binomial J.
bin_rows=[]
for J in range(1,11):
    if (1<<(J+1))-1>M:break
    hist=Counter(m.bit_count()-1 for m in range(1<<J, 1<<(J+1)))
    for k in range(J+1):
        assert hist[k]==comb(J,k),(J,k,hist[k],comb(J,k))
        exact_checks+=1
        bin_rows.append({'J':J,'k':k,'conteo':hist[k],'esperado_binomial':comb(J,k)})

with (BASE/'muestras.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
with (BASE/'crt_pares.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(crt_rows[0]));w.writeheader();w.writerows(crt_rows)
with (BASE/'binario_hist.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(bin_rows[0]));w.writeheader();w.writerows(bin_rows)
result={'m_max':M,'cota_superior_L':N,'verificaciones_exactas':exact_checks,
        'pares_CRT_verificados':len(crt_rows),'pares_bloques_CRT':block_checks,'periodo_bloques_CRT':period,'casos_histograma_binario':len(bin_rows),
        'ejemplo_independencia':{'q':8,'r':9,'periodo':72,'coactivaciones':4*4},
        'ejemplo_dependencia':{'q':3,'r':9,'coactivaciones_en_9':both,
             'covarianza':'2/27'},
        'alcance':'Identidades y promedios de ciclos finitos. No prueba RH ni cancelacion global.'}
(BASE/'resultado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
