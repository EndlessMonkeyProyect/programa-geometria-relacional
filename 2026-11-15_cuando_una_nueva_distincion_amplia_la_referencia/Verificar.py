"""Comprobaciones finitas de las identidades de la nota editorial.
La ejecución no prueba ninguna afirmación asintótica sobre Goldbach.
Biblioteca estándar de Python.
"""
from math import gcd, lcm, log, sqrt
from random import Random

rnd = Random(20261115)
checks = 0


def close(x, y, eps=1e-10):
    global checks
    checks += 1
    assert abs(x-y) <= eps*(1+abs(x)+abs(y)), (x,y)


def modular_grid(n, m):
    L = lcm(n,m)
    a = {k*(L//n)%L for k in range(n)}
    b = {k*(L//m)%L for k in range(m)}
    sums = {(u+v)%L for u in a for v in b}
    assert sums == set(range(L))
    assert (n % m != 0) == (L != n)
    return L


def reflect(a):
    L=len(a)
    return [a[(-k)%L] for k in range(L)]


def coarse_projection(a,n):
    L=len(a); q=L//n
    means=[sum(a[r+j*n] for j in range(q))/q for r in range(n)]
    return [means[k%n] for k in range(L)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


for n in range(2,23):
    for m in range(2,23):
        L=modular_grid(n,m)
        q=L//n
        for _ in range(2):
            a=[rnd.uniform(-1,1) for _ in range(L)]
            p=coarse_projection(a,n)
            d=[u-v for u,v in zip(a,p)]
            close(dot(a,reflect(a)),dot(p,reflect(p))+dot(d,reflect(d)))
            close(dot(coarse_projection(reflect(a),n), [1]*L), dot(reflect(p),[1]*L))
            jr=reflect(p)
            close(sum((x-y)**2 for x,y in zip(coarse_projection(reflect(a),n),jr)),0.0)
            assert abs(dot(d,reflect(d))) <= dot(d,d)+1e-9
            checks += 1

# Nuevo denominador: 0 y N pertenecen a la misma fibra mod N
# pero no tienen el mismo resto mod m cuando m no divide N.
N,m=6,4
assert lcm(N,m)==12 and 0%N == N%N and 0%m != N%m
checks+=1


def von_mangoldt(k):
    if k<2: return 0.0
    n=k
    for p in range(2,int(sqrt(n))+1):
        if n%p==0:
            while n%p==0: n//=p
            return log(p) if n==1 else 0.0
    return log(k)


def goldbach_vector(N):
    units=[r for r in range(1,N) if gcd(r,N)==1]
    a={r:(von_mangoldt(r)/sqrt(N) if 3*r>=N and 3*r<=2*N else 0.0) for r in units}
    return units,a

for N in range(4,602,2):
    units,a=goldbach_vector(N)
    G=sum(a[r]*a[N-r] for r in units)
    norm2=sum(v*v for v in a.values())
    even2=sum(((a[r]+a[N-r])/2)**2 for r in units)
    odd2=sum(((a[r]-a[N-r])/2)**2 for r in units)
    close(G,even2-odd2)
    close(norm2,even2+odd2)
    assert G>=-1e-9
    checks += 1

N=30
units,a=goldbach_vector(N)
G=sum(a[r]*a[N-r] for r in units)
target=2/30*(log(11)*log(19)+log(13)*log(17))
close(G,target)

print(f"APROBADO: {checks} controles finitos; G(30) = {G:.12f}.")
print("Contrato: identidades de grillas, proyecciones, reflexión y conteo finito.")
print("ABIERTO: estimaciones uniformes, semilla generada sin conocer la respuesta y Goldbach.")
