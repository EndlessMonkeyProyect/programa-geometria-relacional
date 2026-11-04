#!/usr/bin/env python3
"""Checks for "The pair swap in both 2026 ETH refutations" (3 Nov 2026).

1. The swap S on R^r (x) R^r satisfies S = I - 2P_-, rank P_- = r(r-1)/2,
   and the antisymmetric fraction is p = (r-1)/(2r)  (OpenAI, Sec. 2.7, Step 2).
2. At r = 2, OpenAI's pair swap equals Claude's crossing [x=v][y=u] and the
   one-bit identity of Claude's Appendix H holds on all 16 entries.
3. V0 = prod Pi_s equals (-1)^W0 with W0 = sum P_-^(s); M0 = V0 f(W0) fixes
   the interpolation window; rank(I - M0) equals the number of eigenvectors
   whose antisymmetry count j lies outside the window.
4. In the one-bit split S = I - 2P_- over t blocks, the piece A_i with i
   factors I and t-i factors -2P_- has row rank  sum_{j>=t-i} C(t,j) 3^(t-j)
   and column rank  sum_{j>=i} C(t,j) 3^(t-j): tail sums of the same spectrum.
   Checked here for t = 3, 4, 5; proved for every t in NOTA_PRUEBA_3_3.md.

These checks are numerical, not formal proofs.

Requires numpy. Exits with status 1 if any check fails.
"""
import itertools
import sys
from functools import reduce
from math import comb

import numpy as np

failures = []


def check(name, ok):
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
    if not ok:
        failures.append(name)


def pair_swap(r):
    """Matrix of (a, b) -> (b, a) on [r] x [r], index a*r + b."""
    D = r * r
    S = np.zeros((D, D))
    for a in range(r):
        for b in range(r):
            S[b * r + a, a * r + b] = 1
    return S


# 1. S = I - 2P_- and the antisymmetric fraction
for r in (2, 3, 4, 5):
    S = pair_swap(r)
    I = np.eye(r * r)
    Pm = (I - S) / 2
    neg = int(round(np.trace(Pm)))
    check(
        f"r={r}: S = I - 2P_-, P_- projector, rank {neg} = r(r-1)/2, p = {neg / r**2:.4f}",
        np.allclose(S, I - 2 * Pm)
        and np.allclose(Pm @ Pm, Pm)
        and neg == r * (r - 1) // 2
        and abs(neg / r**2 - (r - 1) / (2 * r)) < 1e-12,
    )

# 2. r = 2: pair swap == crossing, and Claude's Appendix H identity
S2 = pair_swap(2)  # rows: output (u, v) index 2u+v ; columns: input (x, y) index 2x+y
ok = True
for x, y, u, v in itertools.product((0, 1), repeat=4):
    crossing = float(x == v and y == u)
    rhs = float(x == u and y == v) - float(x != y) * (-1) ** x * float(u != v) * (-1) ** u
    ok &= crossing == rhs and S2[2 * u + v, 2 * x + y] == crossing
check("r=2: pair swap = [x=v][y=u] = [x=u][y=v] - [x!=y](-1)^x [u!=v](-1)^u (16 entries)", ok)

# 3. V0 = (-1)^W0, M0 fixes the window, rank(I - M0) = directions outside it
for r, Q in ((2, 3), (2, 4), (3, 3)):
    pairs = [(a, b) for a in range(r) for b in range(r)]
    idx = {u: i for i, u in enumerate(itertools.product(pairs, repeat=Q))}
    D = len(idx)
    I = np.eye(D)
    Pis = []
    for s in range(Q):
        M = np.zeros((D, D))
        for u, i in idx.items():
            w = list(u)
            a, b = w[s]
            w[s] = (b, a)
            M[idx[tuple(w)], i] = 1
        Pis.append(M)
    V0 = reduce(np.matmul, Pis)
    W0 = sum((I - P) / 2 for P in Pis)
    ev, U = np.linalg.eigh(W0)
    js = np.round(ev).astype(int)
    sign_W0 = U @ np.diag((-1.0) ** js) @ U.T
    R = 2
    p = (r - 1) / (2 * r)
    A0 = max(0, round(Q * p - (R - 1) / 2))
    window = list(range(A0, A0 + R))
    coeffs = np.polyfit(window, [(-1) ** j for j in window], R - 1)
    fW = sum(c * np.linalg.matrix_power(W0, R - 1 - k) for k, c in enumerate(coeffs))
    M0 = V0 @ fW
    fixes = all(np.allclose(M0 @ U[:, i], U[:, i]) for i in range(D) if js[i] in window)
    a_dim, s_dim = r * (r - 1) // 2, r * (r + 1) // 2
    outside = sum(comb(Q, j) * a_dim**j * s_dim ** (Q - j) for j in range(Q + 1) if j not in window)
    rk = np.linalg.matrix_rank(I - M0)
    check(
        f"r={r}, Q={Q}: V0 = (-1)^W0, M0 fixes window {window}, rank(I-M0) = {rk} = {outside}",
        np.allclose(V0, sign_W0) and fixes and rk == outside,
    )

# 4. One-bit split: ranks are tail sums of the antisymmetry spectrum
#    (the general proof is in NOTA_PRUEBA_3_3.md / PROOF_NOTE_3_3_EN.md)
I4 = np.eye(4)
Rb = -2 * (I4 - S2) / 2  # cheap by rows (rank 1)
Cb = I4                  # cheap by columns


def to_column_cut(M):
    """(x,y | u,v) -> (x,u | y,v) for a one-bit block."""
    return M.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)


def piece(t, i, column_cut):
    total = 0
    for chosen in itertools.combinations(range(t), i):
        mats = [Cb if s in chosen else Rb for s in range(t)]
        if column_cut:
            mats = [to_column_cut(m) for m in mats]
        total = total + reduce(np.kron, mats)
    return total


# Facts used by the column-cut proof: the realignment R maps I to Phi Phi^T and S to S,
# and the two images commute.
Phi = np.array([1.0, 0, 0, 1.0])
check(
    "realignment: R(I) = Phi Phi^T, R(S) = S, and they commute",
    np.allclose(to_column_cut(I4), np.outer(Phi, Phi))
    and np.allclose(to_column_cut(S2), S2)
    and np.allclose(S2 @ np.outer(Phi, Phi), np.outer(Phi, Phi) @ S2),
)

for t in (3, 4, 5):
    mult = {j: comb(t, j) * 3 ** (t - j) for j in range(t + 1)}
    ok = True
    for i in range(t + 1):
        rows = np.linalg.matrix_rank(piece(t, i, False))
        cols = np.linalg.matrix_rank(piece(t, i, True))
        ok &= rows == sum(mult[j] for j in range(t - i, t + 1))
        ok &= cols == sum(mult[j] for j in range(i, t + 1))
    check(f"t={t}: row and column ranks of every A_i are tail sums of C(t,j) 3^(t-j)", ok)

print()
print("All checks passed." if not failures else f"{len(failures)} check(s) failed.")
sys.exit(1 if failures else 0)
