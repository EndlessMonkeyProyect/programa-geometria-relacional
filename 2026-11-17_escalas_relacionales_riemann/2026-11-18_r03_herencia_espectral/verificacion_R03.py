#!/usr/bin/env python3
"""R-03 v0.3: finite spectral inheritance, normalization, stability,
inversion cost at the pivot, and control models.

Endless Monkey Project · Relational Geometry Program · Le Matt Ansatz Di Ego

Dependencies: mpmath (no network access needed).
Usage:  python verificacion_R03.py            (about 10 s; pivot lab up to 1e8, ~150 MB RAM)
        python verificacion_R03.py --hasta 7  (lighter run, pivot lab up to 1e7)

Tests are numerical illustrations of proved identities, NOT a RH proof.
"""
from fractions import Fraction
from itertools import compress
import math
import sys

from mpmath import mp

mp.dps = 65
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
HASTA = int(sys.argv[sys.argv.index('--hasta') + 1]) if '--hasta' in sys.argv else 8


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


def period_profile(S):
    """Exact mean and sup of G(y) = int_0^y E_S over one period [0, M).

    E_S(x) = A_S(x) - delta*x is linear on each [n, n+1), so G is a quadratic
    there; mean and extremes are computed in rational arithmetic.
    """
    M = math.prod(S)
    d = Fraction(math.prod(p - 1 for p in S), M)
    A, G, total, sup = 0, Fraction(0), Fraction(0), Fraction(0)
    for n in range(M):
        if n >= 1 and math.gcd(n, M) == 1:
            A += 1
        # on [n, n+1): G(x) = G + A (x-n) - d (x^2 - n^2)/2
        total += G + Fraction(A, 2) - d * (3 * n * n + 3 * n + 1) / 6 + d * n * n / 2
        cands = [n, n + 1]
        if d and n < Fraction(A) / d < n + 1:
            cands.append(Fraction(A) / d)
        for x in cands:
            sup = max(sup, abs(G + A * (x - n) - d * (x * x - n * n) / 2))
        G += A - d * (2 * n + 1) / 2
    assert G == 0
    return total / M, sup


def direct_mellin_quadrature(S, s, N=240000):
    """Independent unit-interval integration of A_S(x)-delta_S*x.

    No use of zeta or of a precomputed Mellin transform on this path.
    For k>=1, the periodic E_S has mean zero. With N a multiple of
    M=prod(S) and |E_S|<2^(k-1), integration by parts bounds the tail by
      |s+1| * M * 2**(k-1) / (Re(s)+1) * N**(-Re(s)-1).
    A second integration by parts gives the tail as <G> N^(-s-1) plus a
    remainder of order N^(-Re(s)-2), where <G> is the period mean of
    G(y) = int_0^y E_S. Unit-interval integrals use double precision.
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
    meanG, supG = period_profile(S)
    lead = float(meanG) * N**(-ss-1)
    remainder_bound = (abs(ss+1) * abs(ss+2) * M * 2 * float(supG) /
                       (sigma+2) * N**(-sigma-2))
    return val, tail_bound, lead, remainder_bound


for S in ([2], [2, 3], [2, 3, 5]):
    for s in (mp.mpf('0.7'), mp.mpc('0.7', '2.4')):
        integral, tail_bound, lead, rem = direct_mellin_quadrature(S, s)
        reference = complex(mp.zeta(s) * partial_factor(S, s) / s)
        err = abs(integral - reference)
        err_lead = abs(integral + lead - reference)
        assert err < tail_bound + 2e-8, (S, s, err, tail_bound)
        assert abs(err - abs(lead)) < rem + 1e-13, (S, s, err, lead)
        assert err_lead < rem + 1e-13, (S, s, err_lead, rem)
        print(f'  S={S}, s={s}: |integral - Mellin|={err:.3g} '
              f'(tail bound {tail_bound:.3g}); leading tail term {abs(lead):.3g}; '
              f'after subtracting it {err_lead:.1g} (remainder bound {rem:.1g})')
print('  PASS: 6 independent sieve-integral comparisons; the residual is the leading tail term')

print('§2 · Known zeta zeros retain a nonzero finite multiplier')
for j in (1, 2, 3):
    rho = mp.zetazero(j)
    P = partial_factor(PRIMES[:8], rho)
    assert abs(P) > mp.mpf('1e-12')
    assert abs(mp.zeta(rho)) < mp.mpf('1e-50')
    print(f'  zero {j}: Im(rho)={mp.nstr(rho.imag, 12)}, |P_8(rho)|={mp.nstr(abs(P), 12)}')
print('  PASS: three illustrative known zeros (not exhaustive)')

print('§3 · Minimal control: symmetric polynomial with off-line zeros')
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
        assert abs(partial_factor(S, rho) * partial_factor(S, 1-rho)) > 0
    for s in (mp.mpc('0.2', '0.13'), mp.mpc('0.73', '-2.01')):
        check_close(H_symmetric(S, 1-s), H_symmetric(S, s), mp.mpf('1e-50'))
        check_close(H_symmetric(S, mp.conj(s)), mp.conj(H_symmetric(S, s)), mp.mpf('1e-50'))
print('  PASS: H and symmetrized H_S preserve both symmetries; unsymmetrized H_S fails reflection')

print('§3b · Standard control: Davenport-Heilbronn function')
mp.dps = 30
tau = (mp.sqrt(10 - 2*mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
coef = [1, tau, -tau, -1, 0]          # a(n) for n = 1..5, period 5


def f_dh(s):
    return mp.power(5, -s) * mp.fsum(coef[j] * mp.zeta(s, mp.mpf(j + 1) / 5) for j in range(4))


def Lambda_dh(s):
    return mp.power(5/mp.pi, (s+1)/2) * mp.gamma((s+1)/2) * f_dh(s)


for s in (mp.mpc('0.3', '7.1'), mp.mpc('0.12', '-3.3'), mp.mpc('0.81', '40.2')):
    assert abs(Lambda_dh(s) - Lambda_dh(1-s)) < mp.mpf('1e-25') * (1 + abs(Lambda_dh(s)))
for t in (5, 30):
    assert abs(mp.im(Lambda_dh(mp.mpc(0.5, t)))) < mp.mpf('1e-25') * abs(Lambda_dh(mp.mpc(0.5, t)))
on_line = mp.findroot(f_dh, mp.mpc('0.5', '5.094'))
assert abs(on_line.real - mp.mpf('0.5')) < mp.mpf('1e-20')
off_line = mp.findroot(f_dh, mp.mpc('0.808517', '85.699348'))
mirror = mp.findroot(f_dh, mp.mpc('0.191483', '85.699348'))
assert abs(off_line.real - mp.mpf('0.5')) > mp.mpf('0.3')
assert abs(mirror - (1 - off_line.real + 1j * off_line.imag)) < mp.mpf('1e-20')
assert abs(coef[1] * coef[2] - coef[0]) > mp.mpf('0.5')   # a(2)a(3) != a(6) = a(1)
print(f'  functional equation Lambda(s) = Lambda(1-s) and real Lambda on the line: checked')
print(f'  zero on the line:  {mp.nstr(on_line, 12)}')
print(f'  zero off the line: {mp.nstr(off_line, 12)}   mirror: {mp.nstr(mirror, 12)}')
print(f'  a(2)a(3) = {mp.nstr(coef[1]*coef[2], 6)} while a(6) = a(1) = 1: no Euler product')
print('  PASS: symmetric Dirichlet series with zeros on and off the line')
mp.dps = 65

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

print(f'§4b · Inversion cost at the pivot s = 1/2, all primes up to X = 1e{HASTA}')
mp.dps = 30
N = 10 ** HASTA
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
for i in range(2, math.isqrt(N) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytes(len(range(i*i, N + 1, i)))
checkpoints = [10 ** k for k in range(2, HASTA + 1)]
logs, thetas, blk_l, blk_t, c = [], [], [], [], 0
for p in compress(range(N + 1), sieve):
    while p > checkpoints[c]:
        logs.append(math.fsum(blk_l) + (logs[-1] if logs else 0.0))
        thetas.append(math.fsum(blk_t) + (thetas[-1] if thetas else 0.0))
        blk_l, blk_t, c = [], [], c + 1
    blk_l.append(-math.log1p(-p ** -0.5))
    blk_t.append(math.log(p))
logs.append(math.fsum(blk_l) + (logs[-1] if logs else 0.0))
thetas.append(math.fsum(blk_t) + (thetas[-1] if thetas else 0.0))
limit_E1 = -mp.sqrt(2) * mp.zeta(0.5)
E1s = []
for X, lg, th in zip(checkpoints, logs, thetas):
    E1 = mp.exp(lg - mp.li(mp.sqrt(th)))
    E1s.append(E1)
    normF = 2 * mp.zeta(0.5) / E1        # F_{S_X}(1/2) * exp(li(sqrt(theta(X))))
    print(f'  X=1e{int(math.log10(X))}: 1/P_S(1/2) = e^{lg:8.2f}   '
          f'E1(X) = {mp.nstr(E1, 6)}   F_S(1/2)*e^li = {mp.nstr(normF, 6)}')
assert all(2.0 < e < 3.5 for e in E1s)
assert all(E1s[i] > E1s[i + 1] for i in range(len(E1s) - 1))
print(f'  limit under RH: E1 -> -sqrt(2) zeta(1/2) = {mp.nstr(limit_E1, 8)};  '
      f'F_S(1/2)*e^li -> -sqrt(2) = {mp.nstr(-mp.sqrt(2), 8)}')
print('  PASS: inverse factor grows as e^li(sqrt(theta)); E1 stays in (2, 3.5) and decreases (observation, not proof)')
mp.dps = 65

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
