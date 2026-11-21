#!/usr/bin/env python3
"""Controles exactos del anexo 2026-11-20. Solo Python estándar.

Controles finitos de las identidades enumeradas en main().
"""
from fractions import Fraction as F
from math import gcd, isqrt


def mu(n):
    c = 0
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            c += 1
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        c += 1
    return -1 if c % 2 else 1


def frac(x):
    return x - x.numerator // x.denominator


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def check_crt():
    for a in range(6):
        residues = {x % 5 for x in range(30) if x % 6 == a}
        assert residues == set(range(5)), (a, residues)
    return "CRT: cada clase mod 6 admite exactamente cinco extensiones mod 30"


def check_o58():
    children = [(4,8,9),(12,12,17),(8,4,9)]
    assert all(a*a+b*b+1 == N*N for a,b,N in children)
    assert len(set(children)) == 3
    N, a = 3, 2
    seq=[]
    for k in range(5):
        assert 2*a*a+1 == N*N
        seq.append((N, a, F(1, N*N)))
        N,a = 3*N+4*a,2*N+3*a
    assert [z[0] for z in seq] == [3,17,99,577,3363]
    assert all(seq[i][2] > seq[i+1][2] for i in range(len(seq)-1))
    return "O58/G01: ramas distintas; Pell simétrica N=3,17,99,577,3363; resto estrictamente menor"


def check_sufficiency():
    # q(x)=x², interfaz Phi(x)=x; mejor proyección en span{1,Phi}.
    xs = range(3)
    q = lambda x: F(x*x)
    fit = lambda x: 2*x-F(1,3)
    sq_err = sum((q(x)-fit(x))**2 for x in xs)/3
    assert sq_err == F(2,9), sq_err
    # Residuo ortogonal a 1 y x.
    assert sum((q(x)-fit(x)) for x in xs) == 0
    assert sum(x*(q(x)-fit(x)) for x in xs) == 0
    return "Consulta exacta q=Phi²; mejor reconstrucción lineal deja error 2/9"


def check_sieve():
    S=(2,3); M=6; delta=F(1,3); next_prime=5
    for x in [F(1,2),F(1),F(3,2),F(2),F(3),F(9,2),F(6),F(13,2)]:
        A=sum(1 for n in range(1,x.numerator//x.denominator+1) if gcd(n,M)==1)
        E=F(A)-delta*x
        G=-E
        g=sum(mu(d)*frac(x/F(d)) for d in divisors(M))
        assert G==g, (x,G,g)
        if x < next_prime:
            chi=1 if x>=1 else 0
            assert F(chi)+G == delta*x, (x,G)
    return "Criba: G_S=-E_S(1/t)=sum mu(d){1/(dt)} y ventana x<q, exactos"


def check_prime_jumps():
    # Para q primo > max(F), solo 1 divide q entre los indices F.
    Fset=(1,2,3,5,6,10)
    for q in (11,13,17,19,23):
        assert [n for n in Fset if q % n == 0] == [1]
    return "Saltos: un primo nuevo no puede ser absorbido por los indices divisores previos"


def check_prime_indexed_control():
    # Serie de pesos de un vector: 1/2 sobre un modo invisible e_0,
    # y 2^{-(j+1)} sobre cada nuevo modo primo j>=1.
    for m in (0,1,2,3,5,10,50):
        e2=F(1,2)+F(1,2**(m+1))
        next_e2=F(1,2)+F(1,2**(m+2))
        assert e2-next_e2==F(1,2**(m+2))>0
        assert e2>=F(1,2)
    return "Control primo-indexado: cada mejora es positiva, y el resto >= 1/2"


def check_telescope():
    # Modelo formal que SATISFACE (L) por definicion; no es la familia de RH.
    for j in range(30):
        e=F(1,j+1)
        new=F(1,j+2)
        assert e-new==e/F(j+2)
    return "Recurrencia (L) comprobada en un modelo formal que la satisface por construcción"


def main():
    tests=[check_crt,check_o58,check_sufficiency,check_sieve,
           check_prime_jumps,check_prime_indexed_control,check_telescope]
    for t in tests:
        print("PASS:",t())
    print(f"TOTAL: {len(tests)} controles exactos aprobados")

if __name__=="__main__":
    main()
