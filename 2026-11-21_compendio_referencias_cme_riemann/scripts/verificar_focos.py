#!/usr/bin/env python3
"""Prueba exacta de focos aritméticos y control en L2.

Para f_d(x)={1/(dx)}, el salto al aumentar x a través de 1/n es
  +1 si d | n y 0 en otro caso.
El salto de G_N=sum_{d<=N} mu(d) f_d es J_N(n)=sum_{d|n,d<=N} mu(d).
La prueba del salto usa aritmética entera (sin coma flotante).
El control adicional en L2 usa la fórmula de Gram de prueba_reglas_de_peso.py.
"""
import math
from collections import Counter
from prueba_reglas_de_peso import gram, mu_of
import numpy as np


def divisors(n):
    return [d for d in range(1, math.isqrt(n)+1) if n%d==0 for d in ([d] if d*d==n else [d,n//d])]

def focal_jump(N, n):
    return sum(mu_of(d) for d in divisors(n) if d<=N)

def omega_sqfree(n):
    if mu_of(n)==0: return None
    r=0; p=2; t=n
    while p*p<=t:
        if t%p==0:
            r+=1; t//=p
        p+=1
    if t>1: r+=1
    return r

def raw_mobius_error(N):
    idx=[n for n in range(1,N+1) if mu_of(n)!=0]
    c=np.array([-mu_of(n) for n in idx], dtype=float)
    b=np.array([(math.log(n)+1-0.5772156649015329)/n for n in idx])
    G=np.array([[gram(n,m) for m in idx] for n in idx])
    return float(1-2*c@b+c@G@c)

for N in [8,16,64,1024]:
    squarefree=[n for n in range(N+1,2*N+1) if mu_of(n)!=0]
    for n in range(N+1,2*N+1):
        assert focal_jump(N,n)==-mu_of(n), (N,n)
        assert focal_jump(2*N,n)==0, (N,n)
    print(f'N={N}: focos que cambian por novedad={len(squarefree)}; coincidencias no cuadrado-libres={N-len(squarefree)}; cierre de saltos {len(squarefree)}/{len(squarefree)}')
    if N==1024:
        print('Distribución por primos distintos:', dict(sorted(Counter(omega_sqfree(n) for n in squarefree).items())))
        print('Referencias nuevas=',len(squarefree))

n=1030; old=1024; new=2048
prev=sorted(d for d in divisors(n) if d<=old and mu_of(d)!=0)
after=sorted(d for d in divisors(n) if d<=new and mu_of(d)!=0)
print('Foco n=1030: divisores en 1024=', prev)
print('Valores mu=', [(d,mu_of(d)) for d in after])
print('Salto anterior=',focal_jump(old,n),'salto posterior=',focal_jump(new,n))
assert len(prev)==7 and len(after)==8
assert focal_jump(old,n)==1 and focal_jump(new,n)==0

# Acciones de alternar presencia de un primo en la firma de divisores:
# en un cubo booleano son involuciones conmutativas, no el par de orden 3 de CME-002.
P=[2,5,103]
def toggle(bits,i): return bits ^ (1<<i)
assert toggle(toggle(0,0),0)==0
assert toggle(toggle(0,0),1)==toggle(toggle(0,1),0)
def pair(bits): return toggle(toggle(bits,0),1)
assert pair(pair(0))==0 and pair(pair(pair(0)))==pair(0)!=0 # orden exactamente 2

for N in [16,32]:
    print(f'Error cuadrático global para c=-mu y N={N}: {raw_mobius_error(N):.6f}')
assert raw_mobius_error(32)>raw_mobius_error(16)
print('RESULTADO: saltos cerrados exactamente en todos los focos; el error de la combinación fija -mu crece de N=16 a N=32.')
