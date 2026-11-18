#!/usr/bin/env python3
"""R-03: finite spectral inheritance, normalization, stability, and control model.

Dependencies: mpmath (no network access needed).
Tests are numerical illustrations of proved identities, NOT a RH proof.
"""
from mpmath import mp
import math

mp.dps = 65
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def partial_factor(S, s):
    return mp.fprod([1 - mp.power(p, -s) for p in S])


def check_close(a, b, tol=mp.mpf('1e-53')):
    assert abs(a - b) < tol, f'mismatch: {a} vs {b}'


print('§1 · Filter factor and normalized recovery')
for s in (mp.mpc('0.37', '2.5'), mp.mpc('0.7', '4.1'), mp.mpf('0.8')):
    for k in (0, 1, 3, 8):
        P = partial_factor(PRIMES[:k], s)
        assert abs(P) > 0
        F = mp.zeta(s) * P / s  # Right-hand side of the published Mellin formula.
        check_close(F / P, mp.zeta(s) / s)
print('  PASS: all 12 algebraic normalization checks')

print('§1a · Independent Mellin quadrature from sieve counts')

def direct_mellin_quadrature(S, s, N=240000):
    """Independent unit-interval integration of A_S(x)-delta_S*x.

    No use of zeta or of a precomputed Mellin transform on this path.
    For k>=1, the periodic E_S has mean zero. With N a multiple of
    M=prod(S) and |E_S|<2^(k-1), integration by parts bounds the tail by
      |s+1| * M * 2**(k-1) / (Re(s)+1) * N**(-Re(s)-1).
    Unit-interval integrals are evaluated analytically in double precision.
    """
    M = math.prod(S)
    assert S and N % M == 0
    delta = math.prod((p-1)/p for p in S)
    ss = complex(s)
    val = -delta/(1-ss)  # on (0,1), E_S(x) = -delta*x
    counter = 0
    correction = 0j
    for n in range(1, N):
        if math.gcd(n, M) == 1:
            counter += 1
        term = (counter * (n**(-ss) - (n+1)**(-ss))/ss
                - delta * ((n+1)**(1-ss) - n**(1-ss))/(1-ss))
        inc = term - correction    # compensated summation
        new_val = val + inc
        correction = (new_val - val) - inc
        val = new_val
    sigma = ss.real
    tail_bound = (abs(ss+1) * M * 2**(len(S)-1) /
                  (sigma+1) * N**(-sigma-1))
    return val, tail_bound

for S in ([2], [2,3], [2,3,5]):
    for s in (mp.mpf('0.7'), mp.mpc('0.7','2.4')):
        integral, tail_bound = direct_mellin_quadrature(S, s)
        reference = complex(mp.zeta(s) * partial_factor(S, s) / s)
        err = abs(integral - reference)
        assert err < tail_bound + 2e-8, (S, s, err, tail_bound)
        print(f'  S={S}, s={s}: |integral - Mellin formula|={err:.3g}, '
              f'rigorous tail bound <= {tail_bound:.3g} (+2e-8 rounding allowance)')
print('  PASS: 6 independent sieve-integral comparisons')

print('§2 · Known zeta zeros retain a nonzero finite multiplier')
for j in (1, 2, 3):
    rho = mp.zetazero(j)
    P = partial_factor(PRIMES[:8], rho)
    assert abs(P) > mp.mpf('1e-12')
    assert abs(mp.zeta(rho)) < mp.mpf('1e-50')
    print(f'  zero {j}: Im(rho)={mp.nstr(rho.imag, 12)}, |P_8(rho)|={mp.nstr(abs(P), 12)}')
print('  PASS: three illustrative known zeros (not exhaustive)')

print('§3 · Control counterexample: symmetry plus off-line zeros')
a = mp.mpf('0.2') + 1j

def H(s):
    z = s - mp.mpf('0.5')
    return (z*z - a*a) * (z*z - mp.conj(a)**2)

roots = [mp.mpf('0.3') + 1j, mp.mpf('0.3') - 1j,
         mp.mpf('0.7') + 1j, mp.mpf('0.7') - 1j]
for rho in roots:
    check_close(H(rho), mp.mpc(0), mp.mpf('1e-55'))
    for k in (0, 3, 8):
        check_close(H(rho) * partial_factor(PRIMES[:k], rho), 0, mp.mpf('1e-53'))
for s in (mp.mpc('0.2', '0.13'), mp.mpc('0.73', '-2.01')):
    check_close(H(1-s), H(s))
    check_close(H(mp.conj(s)), mp.conj(H(s)))
# The unsymmetrized family generally fails functional reflection.
s = mp.mpc('0.34', '0.91')
ps = partial_factor(PRIMES[:3], s)
psr = partial_factor(PRIMES[:3], 1-s)
assert abs(H(s) * ps - H(1-s) * psr) > mp.mpf('1e-6')

def H_symmetric(S, s):
    return H(s) * partial_factor(S, s) * partial_factor(S, 1-s)

for S in ([], PRIMES[:3], PRIMES[:8]):
    for rho in roots:
        check_close(H_symmetric(S, rho), 0, mp.mpf('1e-50'))
        assert abs(partial_factor(S,rho) * partial_factor(S,1-rho)) > 0
    for s in (mp.mpc('0.2', '0.13'), mp.mpc('0.73','-2.01')):
        check_close(H_symmetric(S, 1-s), H_symmetric(S, s), mp.mpf('1e-50'))
        check_close(H_symmetric(S, mp.conj(s)), mp.conj(H_symmetric(S, s)), mp.mpf('1e-50'))
print('  PASS: H and symmetrized H_S preserve both symmetries; unsymmetrized H_S fails reflection')

print('§4 · Finite-reference stability, growing inverse factor')
sigma0 = mp.mpf('0.7')
previous = mp.mpf(1)
for k in (1, 3, 6, 10, 15):
    P = partial_factor(PRIMES[:k], sigma0)
    inverse = 1 / abs(P)
    assert inverse > previous
    previous = inverse
    print(f'  k={k:2d}: inverse |P_k(0.7)| = {mp.nstr(inverse, 12)}')
print('  PASS: inverse factor increases on positive real sigma=0.7')

print('§5 · Radius versus full transfer amplitude')
rho = mp.mpc('0.7', '14.1')
p = mp.mpf(7)
radius = mp.power(p, -rho.real)
multiplier = 1 - mp.power(p, -rho)
formula = 1 + radius**2 - 2*radius*mp.cos(rho.imag * mp.log(p))
check_close(abs(multiplier)**2, formula)
check_close(abs(mp.power(p, -rho)), radius)
print(f'  r_7(rho)={mp.nstr(radius, 12)}, |lambda_7(rho)|={mp.nstr(abs(multiplier), 12)}')
print('  PASS: radius and full multiplier are distinct quantities')
print('R-03 numerical checks: ALL PASS')
