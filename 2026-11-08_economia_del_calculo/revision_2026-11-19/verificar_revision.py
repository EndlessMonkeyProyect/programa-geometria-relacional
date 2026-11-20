#!/usr/bin/env python3
"""Finite checks of partition defects and 3-colour-grid orbit counts.

The modular Krylov ranks are LOWER bounds on the rational ranks.
Exact ranks over Q: brecha_exacta.py (sympy) and the original E5/E5x/E5c certificates.
No external dependencies.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
import argparse

ORDERS = [1, 1, 2, 3, 5, 7, 13, 19, 35, 51]
ORBITS = [1, 1, 2, 3, 6, 10, 20, 36, 72, 136]


def partitions(n):
    """All set partitions of range(n), in canonical restricted growth order."""
    def rec(i, blocks):
        if i == n:
            yield tuple(frozenset(b) for b in blocks)
        else:
            for j in range(len(blocks)):
                blocks[j].append(i)
                yield from rec(i+1, blocks)
                blocks[j].pop()
            blocks.append([i])
            yield from rec(i+1, blocks)
            blocks.pop()
    yield from rec(0, [])


def partition_stats(P, Q):
    assert P and Q
    assert set.union(*(set(b) for b in P)) == set.union(*(set(b) for b in Q))
    edges = [(i, j) for i, B in enumerate(P) for j, C in enumerate(Q) if B & C]
    nr = len(P) + len(Q)
    parent = list(range(nr))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        parent[root(a)] = root(b)
    for i, j in edges:
        union(i, len(P) + j)
    comps = defaultdict(lambda: [0, 0, 0])
    for i in range(len(P)):
        comps[root(i)][0] += 1
    for j in range(len(Q)):
        comps[root(len(P)+j)][1] += 1
    for i, j in edges:
        comps[root(i)][2] += 1
    sizes = list(comps.values())
    k = len(sizes)
    E = len(edges)
    delta = sum(p*q-e for p, q, e in sizes)
    beta = E - len(P) - len(Q) + k
    covariance = Fraction(sum(p*q for p, q, _ in sizes), k) - Fraction(len(P)*len(Q), k*k)
    assert all(p + q - 1 <= e <= p*q for p,q,e in sizes)
    assert beta == sum((p-1)*(q-1) for p,q,_ in sizes) - delta
    assert k*E == len(P)*len(Q) + k*k*covariance - k*delta
    return dict(k=k, edges=E, p=len(P), q=len(Q), beta=beta, defect=delta, covariance=covariance, components=sizes)


def check_partitions():
    for n in range(1, 6):
        family = list(partitions(n))
        for P in family:
            for Q in family:
                partition_stats(P, Q)
        print(f'Partitions n={n}: {len(family)**2} pairs checked')
    P = [frozenset(x) for x in [{0,1},{2,3},{4}]]
    Q = [frozenset(x) for x in [{0,2},{1,3},{4}]]
    a = partition_stats(P, Q)
    assert (a['edges'],a['k'],a['beta'],a['defect'],a['covariance']) == (5,2,1,0,Fraction(1,4))
    print('Example A (E=5, k=2, beta=1, delta=0, cov=1/4): OK')
    P = [frozenset(x) for x in [{0},{1,2,3},{4,5}]]
    Q = [frozenset(x) for x in [{0},{1,4},{2,5},{3}]]
    b = partition_stats(P,Q)
    assert (b['edges'],b['k'],b['p'],b['q'],b['defect'],b['covariance']) == (6,2,3,4,1,Fraction(1,2))
    assert b['edges']*b['k'] == b['p']*b['q'] and b['defect'] > 0
    print('Example B, product law without permuting (E=6, k=2, |P|=3, |Q|=4, delta=1): OK')
    # Example B has minimum size: no such pair on <= 5 elements; 720 ordered pairs on 6.
    for n in range(1, 7):
        family = list(partitions(n))
        count = 0
        for P in family:
            for Q in family:
                s = partition_stats(P, Q)
                if s['edges']*s['k'] == s['p']*s['q'] and s['defect'] > 0:
                    count += 1
        assert count == (720 if n == 6 else 0), (n, count)
    print('Product law without permuting: none on n<=5 elements, 720 ordered pairs on n=6: OK')


def colour_states(w):
    results = []
    def rec(seq):
        if len(seq)==w:
            results.append(tuple(seq))
            return
        for color in range(3):
            if not seq or color != seq[-1]:
                rec(seq+[color])
    rec([])
    return results


def orbit_key(state, perms):
    return min(tuple(p[x] for x in s) for p in perms for s in (state, state[::-1]))


def burnside(w):
    if w == 1:
        return 1
    n = w-1
    total = 2**n + 2**((n+1)//2) + (2**(n//2) if n % 2==0 else 0)
    assert total % 4 == 0
    return total // 4


def orbit_quotient(w):
    states = colour_states(w)
    perms = list(permutations(range(3)))
    group = defaultdict(list)
    for y in states:
        group[orbit_key(y,perms)].append(y)
    keys = sorted(group)
    index = {key:i for i,key in enumerate(keys)}
    O = len(keys)
    sizes = [len(group[key]) for key in keys]
    A = [[0]*O for _ in range(O)]
    for i,x in enumerate(keys):
        for y in states:
            if all(a != b for a,b in zip(x,y)):
                A[i][index[orbit_key(y,perms)]] += 1
    for i in range(O):
        for j in range(O):
            assert sizes[i]*A[i][j] == sizes[j]*A[j][i]
    return states, A


def matvec_mod(A, v, mod):
    return [sum(a*x for a,x in zip(row,v))%mod for row in A]


def krylov_mod_rank(A, mod):
    n = len(A)
    basis = {}
    vector = [1]*n
    for k in range(n+1):
        r = vector[:]
        for pivot in sorted(basis):
            coeff = r[pivot]
            if coeff:
                q=basis[pivot]
                r = [(a-coeff*b)%mod for a,b in zip(r,q)]
        pivot = next((i for i,x in enumerate(r) if x),None)
        if pivot is None:
            return len(basis)
        inv = pow(r[pivot],-1,mod)
        basis[pivot] = [(x*inv)%mod for x in r]
        vector = matvec_mod(A,vector,mod)
    raise AssertionError('Krylov dimension exceeded n')


def check_grid(max_width=10):
    for w in range(1,max_width+1):
        states, A = orbit_quotient(w)
        assert len(states)==3*2**(w-1)
        assert len(A)==burnside(w)==ORBITS[w-1]
        d = krylov_mod_rank(A,1000000007)
        assert d==ORDERS[w-1], (w,d,ORDERS[w-1])
        print(f'Grid w={w}: states={len(states):4}, orbits={len(A):3}, modular Krylov rank={d:2} (lower bound)')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grid-max',type=int,default=10)
    args=parser.parse_args()
    assert 1 <= args.grid_max <= 10
    check_partitions()
    check_grid(args.grid_max)
    print('All stated finite checks passed.')
