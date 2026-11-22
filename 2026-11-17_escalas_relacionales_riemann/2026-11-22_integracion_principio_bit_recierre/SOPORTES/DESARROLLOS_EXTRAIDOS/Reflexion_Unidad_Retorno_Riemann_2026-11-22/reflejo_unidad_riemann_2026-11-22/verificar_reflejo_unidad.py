#!/usr/bin/env python3
"""Control finito exacto para la nota Reflexion, unidad y retorno.
Aserciones finitas adicionales a las demostraciones del manuscrito.
"""
from math import comb, gcd, lcm

checks = 0

def check(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

for q in range(2, 257):
    for r in range(q):
        refl = q - 1 - r
        carry = lambda t, q=q: (2 * t) // q
        fixed = int(q % 2 == 1 and 2 * r == q-1)
        check(q-1-refl == r, f'involution q={q},r={r}')
        check(carry(r) + carry(refl) == 1 - fixed, f'paired bit q={q},r={r}')
        check((q - 1 - ((2*r)%q) - (2*(q-1-r))%q) % q == 1 % q,
              f'commutation defect q={q},r={r}')

N = 512
L = [1] * (2*N+1)
for n in range(2, 2*N+1):
    L[n] = lcm(L[n-1], n)

def prime_powers(n):
    ps = []
    for x in range(2, n+1):
        if all(x % z for z in range(2, int(x**0.5)+1)):
            p = x
            q = p
            while q <= n:
                ps.append((p, q))
                q *= p
    return ps

powers = prime_powers(2*N)

def bit(q, m):
    return (2*m)//q - 2*(m//q)

def B(m):
    numer = comb(2*m, m) * L[m]
    assert numer % L[2*m] == 0
    return numer//L[2*m]

for m in range(1, N+1):
    b = 1
    for p,q in powers:
        if q <= m:
            b *= p**bit(q,m)
    check(B(m) == b, f'factorization B at m={m}')
    if m <= N//2:
        old = 1
        new = 1
        for p,q in powers:
            if p % 2 == 0:
                continue
            if q <= m:
                d = bit(q,2*m)-bit(q,m)
                if d >= 0: new *= p**d
                else: old *= p**(-d)
            elif m < q <= 2*m and bit(q,2*m):
                new *= p
        check(B(2*m)*old == B(m)*new, f'odd inheritance m={m}')

for t in range(2, 3001):
    vals = []
    k = 1
    while (1 << k) <= t:
        q = 1 << k
        h = int(t % q == 0) - int(t % q == 1)
        vals.append((q//2)*h)  # Twice the toy weight 2^(k-2).
        k += 1
    # Check |D*(t)/t| < 1/2, scaling by 2 for integer arithmetic.
    check(abs(sum(vals)) < t, f'unit bound at t={t}')

for K in range(1, 26):
    t = 1 << K
    d4 = sum((1 << k) for k in range(1,K+1))
    # D* = sum 2^(k-2) = (t-1)/2
    check(d4 == 2*(t-1), f'toy weighting K={K}')
    # One full period always has exactly one + and one -, except k=1:
    # at modulus 2 they are distinct as well.
    for k in range(1, min(K,12)+1):
        mod = 1<<k
        check((sum(int(r==0)-int(r==1) for r in range(mod)) == 0), f'period k={k}')
print(f'OK: {checks:,} finite exact checks; unit-normalized toy grows linearly.')
