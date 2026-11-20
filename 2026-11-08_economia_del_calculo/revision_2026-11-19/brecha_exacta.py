#!/usr/bin/env python3
"""Exact split of the orbit gap o_w - d_w (equation 9) for the 3-colour strip, widths 1..10.

For each width w it builds the orbit quotient A (S3 x C2 acting on proper columns),
and computes over Q, with exact integer arithmetic:
  d_w  = dimension of the Krylov space of the all-ones vector (exact rank),
  the characteristic polynomial of A and its factorization into irreducibles over Q,
  which irreducible factors are active (have nonzero projection of the all-ones vector).
A is similar to a symmetric matrix, hence diagonalizable; this is checked exactly
(the squarefree part of the characteristic polynomial annihilates A).
The printed table is compared with the table of the appendix (EXPECTED).
Dependency: sympy.
"""
from collections import defaultdict
from itertools import permutations
import sympy as sp
from sympy.polys.matrices import DomainMatrix

def colour_states(w):
    out = []
    def rec(seq):
        if len(seq) == w:
            out.append(tuple(seq)); return
        for c in range(3):
            if not seq or c != seq[-1]:
                rec(seq + [c])
    rec([])
    return out

PERMS = list(permutations(range(3)))

def orbit_key(s):
    return min(tuple(p[x] for x in v) for p in PERMS for v in (s, s[::-1]))

def quotient(w):
    states = colour_states(w)
    group = defaultdict(list)
    for y in states:
        group[orbit_key(y)].append(y)
    keys = sorted(group)
    idx = {k: i for i, k in enumerate(keys)}
    A = [[0] * len(keys) for _ in keys]
    for i, x in enumerate(keys):
        for y in states:
            if all(a != b for a, b in zip(x, y)):
                A[i][idx[orbit_key(y)]] += 1
    return A

def apply_poly(coeffs_high_to_low, M, v):
    r = DomainMatrix.zeros(v.shape, sp.ZZ)
    for c in coeffs_high_to_low:
        r = M * r + v * sp.ZZ(int(c))
    return r

# w: (orbits, d_w, distinct r_w, kernel dimension, degrees of inactive nonzero factors)
EXPECTED = {1: (1, 1, 1, 0, []), 2: (1, 1, 1, 0, []), 3: (2, 2, 2, 0, []), 4: (3, 3, 3, 0, []),
            5: (6, 5, 6, 0, [1]), 6: (10, 7, 8, 3, []), 7: (20, 13, 20, 0, [7]),
            8: (36, 19, 28, 9, [8]), 9: (72, 35, 72, 0, [37]), 10: (136, 51, 92, 45, [40])}

t = sp.symbols('t')
print(' w  orbits  d_w  distinct  zero-eig  inactive-nonzero(deg)   o-d = sum(m-1) + #inactive')
for w in range(1, 11):
    Al = quotient(w)
    o = len(Al)
    A = DomainMatrix([[sp.ZZ(x) for x in row] for row in Al], (o, o), sp.ZZ)
    one = DomainMatrix([[sp.ZZ(1)] for _ in range(o)], (o, 1), sp.ZZ)
    cols, v = [one], one
    for _ in range(o):
        v = A * v
        cols.append(v)
    d = DomainMatrix.hstack(*cols).convert_to(sp.QQ).rank()
    chi = sp.Poly(A.charpoly(), t)
    _, facs = chi.factor_list()
    rad = sp.prod([f for f, _ in facs])
    # diagonalizability: rad(A) = 0 exactly
    I = DomainMatrix.eye(o, sp.ZZ)
    assert apply_poly(rad.all_coeffs(), A, I).is_zero_matrix
    active_deg, n_active, zero_mult, inactive_nonzero = 0, 0, 0, []
    for f, m in facs:
        g = sp.quo(rad, f)
        active = not apply_poly(g.all_coeffs(), A, one).is_zero_matrix
        if active:
            assert m == 1
            active_deg += f.degree()
            n_active += 1
        elif f.as_expr() == t:
            zero_mult = m
        else:
            assert m == 1
            inactive_nonzero.append(f.degree())
    assert active_deg == d and n_active == 1
    r = rad.degree()
    excess, inactive = o - r, r - d
    assert excess + inactive == o - d
    assert (o, d, r, zero_mult, sorted(inactive_nonzero)) == EXPECTED[w], w
    print(f'{w:2} {o:7} {d:4} {r:9} {zero_mult:9}  {str(inactive_nonzero):22} {o-d:3} = {excess:3} + {inactive:3}')
print('In every width the active part is a single irreducible factor of degree d_w.')
print('Table matches the appendix.')
