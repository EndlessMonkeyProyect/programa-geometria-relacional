#!/usr/bin/env python3
"""Controles finitos EXACTOS para la cadena O58--Pell--Möbius.
No verifica RH ni convergencia de proyecciones en dimensión infinita.
Sólo usa biblioteca estándar de Python.
"""
from fractions import Fraction
from math import gcd, lcm
from itertools import combinations


def pell(k):
    n, a = 1, 0
    for _ in range(k):
        n, a = 3*n + 4*a, 2*n + 3*a
    return n, a


def mobius(n):
    k, sign, x = 2, 1, n
    while k*k <= x:
        if x % k == 0:
            x //= k
            sign = -sign
            if x % k == 0:
                return 0
            while x % k == 0:
                x //= k
        k += 1
    if x > 1:
        sign *= -1
    return sign


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def f(d, x):
    z = Fraction(1, d) / x
    return z - (z.numerator // z.denominator)


def G(primes, x):
    prod = 1
    for p in primes:
        prod *= p
    return sum((mobius(d)*f(d, x) for d in divisors(prod)), Fraction(0))


def subsets(xs):
    for k in range(len(xs)+1):
        yield from combinations(xs, k)


def primes_upto(n):
    return [p for p in range(2, n+1) if all(p%d for d in range(2, int(p**.5)+1))]


def main():
    counts = dict(pell=0, divisibility=0, orbit=0, chain=0, mobius=0, local=0)
    for k in range(1, 13):
        n, a = pell(k)
        assert n*n - 2*a*a == 1
        counts['pell'] += 1
    for k in range(1, 15):
        _, a = pell(k)
        for ell in range(1, 8):
            assert pell(k*ell)[1] % a == 0
            counts['divisibility'] += 1
    for p in primes_upto(97):
        n, a = 1, 0
        found = False
        for t in range(1, p*p+1):
            n, a = (3*n+4*a)%p, (2*n+3*a)%p
            if (n, a) == (1, 0):
                found = True
                assert a % p == 0
                break
        assert found, p
        counts['orbit'] += 1
    for j in range(1, 9):
        kappa = lcm(*range(1, j+1))
        _, a = pell(kappa)
        if j > 1:
            assert a % previous_a == 0
        previous_a = a
        counts['chain'] += 1
    samples = [Fraction(1, 7), Fraction(2, 5), Fraction(3, 2), Fraction(11, 13)]
    for primes in [[], [2], [2,3], [2,3,5], [2,3,5,7]]:
        M = 1
        for p in primes:
            M *= p
        for x in samples:
            rhs = sum(((-1)**len(sub)*G(sub, x) for sub in subsets(primes)), Fraction(0))
            assert f(M, x) == rhs
            counts['mobius'] += 1
    for N in range(1, 55):
        for n in range(N+1, 2*N+1):
            value = sum(mobius(d) for d in divisors(n) if d <= N)
            assert value == -mobius(n)
            counts['local'] += 1
    print('Comprobación finita exacta: CORRECTA')
    for k,v in counts.items():
        print(f'{k}: {v}')
    print('Total:', sum(counts.values()))
    print('No es una prueba de RH ni de convergencia global en L2.')


if __name__ == '__main__':
    main()
