#!/usr/bin/env python3
"""Controles exactos del puente entre reflexiones y recuperabilidad funcional.

Solo biblioteca estandar. Resultados:
(1) grupo de reflexiones de tipo B3 (simetria del cubo) de orden 48,
    con una direccion invisible en dimension cuatro;
(2) grupo de dos reflexiones de orden infinito que reconstruyen R^2;
(3) identidad exacta de ganancia de una reflexion en un ejemplo racional.
"""
from fractions import Fraction as F
from collections import deque


def matmul(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def eye(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))


def order(a, limit=200):
    c = eye(len(a))
    for k in range(1, limit+1):
        c = matmul(c, a)
        if c == eye(len(a)):
            return k
    return None


def closure(generators):
    base = eye(len(generators[0]))
    seen = {base}
    q = deque([base])
    while q:
        a = q.popleft()
        for g in generators:
            b = matmul(a, g)
            if b not in seen:
                seen.add(b)
                q.append(b)
    return seen


def apply(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(v)))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def householder(n):
    k=len(n)
    z=dot(n,n)
    return tuple(tuple(F(i==j)-2*n[i]*n[j]/z for j in range(k)) for i in range(k))


# Simetria completa del cubo: reflejos s1=(12), s2=(23), s3: x3 -> -x3.
# Extension trivial de R3 a R4: el cuarto eje no es observable por los espejos.
s1=((0,1,0,0),(1,0,0,0),(0,0,1,0),(0,0,0,1))
s2=((1,0,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1))
s3=((1,0,0,0),(0,1,0,0),(0,0,-1,0),(0,0,0,1))
G=closure([s1,s2,s3]); target=(0,0,0,1)
assert len(G)==48
assert (order(matmul(s1,s2)),order(matmul(s2,s3)),order(matmul(s1,s3)))==(3,4,2)
assert all(apply(g,target)==target for g in G)
print('CONTROL A: B3 de orden',len(G),'; relaciones (3,4,2); eje 4 fijo; resto cuadratico = 1')

# Reflejos de orden infinito pero las dos normales generan todo R2.
a=(F(1),F(0)); b=(F(3,5),F(4,5))
R1,R2=householder(a),householder(b)
prod=matmul(R1,R2)
tr=prod[0][0]+prod[1][1]
assert tr==F(-14,25)
assert dot(a,b)==F(3,5)
assert a[0]*b[1]-a[1]*b[0]==F(4,5)
# Si el producto tuviera orden finito, la traza racional de la matriz
# (suma de raices de la unidad) seria un entero algebraico racional,
# por tanto un entero. -14/25 no es entero => orden infinito.
assert tr.denominator!=1
print('CONTROL B: reflejos en R2 generan grupo infinito (traza =',tr,'); sus normales abarcan R2; resto = 0')

# Identidad de recuperacion con un espejo h: la fraccion recuperada
# es |<r,h>|^2/||h||^2 y = ||r-R_h r||^2/4.
r=(F(1),F(2)); h=(F(3),F(4)); R=householder(h)
rr=apply(R,r); diff=tuple(x-y for x,y in zip(r,rr))
gain=dot(r,h)**2/dot(h,h)
mirror=dot(diff,diff)/4
assert gain==mirror==F(121,25)
print('CONTROL C: ganancia = desplazamiento por reflexion / 4 =',gain,'(aritmetica racional exacta)')
print('ESTADO: 3 controles racionales exactos aprobados')
