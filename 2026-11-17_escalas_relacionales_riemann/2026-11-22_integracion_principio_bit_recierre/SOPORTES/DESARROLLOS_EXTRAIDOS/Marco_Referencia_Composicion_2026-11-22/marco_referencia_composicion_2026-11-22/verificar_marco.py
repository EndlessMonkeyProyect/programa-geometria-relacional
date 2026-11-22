#!/usr/bin/env python3
"""Controles finitos de referencia, cociclo, ventanas, CRT y aritmética prima.

Solo biblioteca estándar; pruebas deterministas. No demuestra cotas asintóticas.
"""
from fractions import Fraction
from math import gcd

nchecks = 0


def check(condition, message):
    global nchecks
    nchecks += 1
    if not condition:
        raise AssertionError(message)


def remainder(n, q):
    return n % q


def carry(a, b, q):
    return ((a % q) + (b % q)) // q


def activation(m, q):
    return (2 * m) // q - 2 * (m // q)


# P2: actualización por acarreo.
for q in range(2, 39):
    for a in range(0, 51):
        for b in range(0, 37):
            check((a+b)//q == a//q + b//q + carry(a,b,q), 'actualizacion')
            check((a+b)%q == ((a%q)+(b%q))%q, 'resto')

# P3: identidad de cociclo.
for q in range(2, 23):
    for a in range(q):
        for b in range(q):
            for c in range(q):
                check(carry(a,b,q)+carry(a+b,c,q) ==
                      carry(b,c,q)+carry(a,b+c,q), 'cociclo')

# P4: periodicidad, activación y cota racional exacta.
for q in range(2, 48):
    k = q // 2
    alpha = Fraction(k,q)
    active_start = (q+1)//2
    check(sum(activation(m,q) for m in range(q)) == k, 'frecuencia')
    check(all(activation(m+q,q) == activation(m,q) for m in range(q)), 'periodicidad')
    for a in range(q):
        for n in list(range(1,q+1)) + [q+3,2*q+1]:
            d = Fraction(sum(activation(m,q) for m in range(a,a+n))) - n*alpha
            check(abs(d) <= Fraction(k*(q-k),q), 'cota optima')
    witness = Fraction(sum(activation(m,q) for m in range(active_start,active_start+k))) - k*alpha
    check(witness == Fraction(k*(q-k),q), 'testigo optimalidad')

# P5: distribución por CRT para dos módulos coprimos.
for q in range(2, 23):
    for r in range(q+1, 25):
        if gcd(q,r)==1:
            both = sum(activation(m,q) and activation(m,r) for m in range(q*r))
            check(Fraction(both,q*r)==Fraction(q//2,q)*Fraction(r//2,r), 'CRT')
check(Fraction(sum(activation(m,3) and activation(m,9) for m in range(9)),9)==Fraction(2,9), 'dependencia 3/9')

# P7: descomposición exacta de los exponentes binomiales.
def primes(n):
    sieve = [True]*(n+1)
    sieve[0:2]=[False,False]
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            for z in range(p*p,n+1,p):
                sieve[z]=False
    return [p for p in range(2,n+1) if sieve[p]]

for m in range(1,251):
    for p in primes(2*m):
        qs=[]
        q=p
        while q<=2*m:
            qs.append(q)
            q*=p
        legendre=sum((2*m)//q - 2*(m//q) for q in qs)
        new=sum(1 for q in qs if m<q<=2*m)
        inherited=sum(activation(m,q) for q in qs if q<=m)
        check(legendre==new+inherited,'Legendre y herencia')

# P6: testigo exacto SU(2), U=i*sigma_x y V=i*sigma_y.
U=((0+0j, 1j), (1j, 0+0j))
V=((0+0j, 1+0j), (-1+0j, 0+0j))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def adj(A):
    return tuple(tuple(A[j][i].conjugate() for j in range(2)) for i in range(2))

UV,VU=mm(U,V),mm(V,U)
comm=mm(mm(U,V),mm(adj(U),adj(V)))
nu=1-(comm[0][0]+comm[1][1]).real/2
frobenius=sum(abs(UV[i][j]-VU[i][j])**2 for i in range(2) for j in range(2))
check(comm==((-1+0j,0j),(0j,-1+0j)),'conmutador testigo')
check(nu==frobenius/4==2,'norma conmutador')

print(f'OK: {nchecks} controles finitos; Python estandar; aritmetica exacta en la parte discreta.')
print('Probadas por escrito: 7 proposiciones. RH, P vs NP y brecha espectral YM: cuestiones abiertas.')
