#!/usr/bin/env python3
"""Verificacion de «Certificacion de optimalidad local y composicion de cotas en conteo exacto».

Solo biblioteca estandar y aritmetica racional exacta. Uso: python3 verificar_certificacion.py

  1. Lema 1 y Proposicion 2: rangos q^2 y 1 del tensor de cruce para q = 2, 4, 8,
     y descomposicion por columnas con exactamente q^2 terminos.
  2. SWAP = I - 2 P_- para dos indices binarios; P_- proyector de rango 1.
  3. Proposicion 3: con s <= d datos de Hermite en nodos no nulos, P(T) = prod (T - a_i)^{m_i}
     anula todos los datos y P(0) != 0; con s = d + 1 la recuperacion de H(0) es exacta.
  4. Proposicion 4: criterio de nucleo; en span{1, T(T-1)} basta H(1).
  5. Ejemplo: F* (paridad par y clausula positiva) tiene soluciones 011, 101, 110;
     H(T) = 3(1+T)^2 y H(0) = H(1) - H'(1) + H''(1)/2 = 3.
"""
from fractions import Fraction
from itertools import product
from math import comb, prod
import random


def rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    r = 0
    for c in range(len(A[0]) if A else 0):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def solve(M, rhs):
    n = len(M)
    A = [[Fraction(x) for x in row] + [Fraction(rhs[i])] for i, row in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                A[i] = [a - A[i][c] * b for a, b in zip(A[i], A[c])]
    return [A[i][n] for i in range(n)]


# ------------------------------------------------------------------ 1
def check_crossing():
    for q in (2, 4, 8):
        idx = list(product(range(q), repeat=2))
        X = lambda i, j, u, v: int(i == v and j == u)
        A = [[X(i, j, u, v) for (j, v) in idx] for (i, u) in idx]       # corte (i,u)|(j,v)
        B = [[X(i, j, u, v) for (j, u) in idx] for (i, v) in idx]       # corte (i,v)|(j,u)
        assert all(sum(row) == 1 for row in A) and all(sum(col) == 1 for col in zip(*A))
        assert rank(A) == q * q and rank(B) == 1
        # descomposicion por columnas: q^2 terminos separables a_h(i,u) b_h(j,v)
        terms = [([A[r][h] for r in range(q * q)], [int(c == h) for c in range(q * q)])
                 for h in range(q * q)]
        S = [[sum(a[r] * b[c] for a, b in terms) for c in range(q * q)] for r in range(q * q)]
        assert S == A and len(terms) == q * q
    print('Cruce: rangos (q^2, 1) = (4,1), (16,1), (64,1); descomposicion de q^2 terminos exacta.')


# ------------------------------------------------------------------ 2
def check_swap():
    basis = list(product((0, 1), repeat=2))
    SW = [[int(r == (c[1], c[0])) for c in basis] for r in basis]
    h = Fraction(1, 2)
    Pm = [[Fraction(0)] * 4 for _ in range(4)]
    Pm[1][1], Pm[1][2], Pm[2][1], Pm[2][2] = h, -h, -h, h        # |01>-|10> normalizado
    I = [[int(i == j) for j in range(4)] for i in range(4)]
    assert SW == [[I[i][j] - 2 * Pm[i][j] for j in range(4)] for i in range(4)]
    Pm2 = [[sum(Pm[i][k] * Pm[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    assert Pm2 == Pm and rank(Pm) == 1
    print('SWAP = I - 2 P_-, con P_- proyector de rango 1.')


# ------------------------------------------------------------------ 3
def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def deriv_at(coeffs, j, t):
    """H^{(j)}(t) para H = sum c_k T^k."""
    return sum(c * prod(range(k - j + 1, k + 1)) * Fraction(t) ** (k - j)
               for k, c in enumerate(coeffs) if k >= j)


def hermite_rows(nodes, mults, d):
    return [[deriv_at([int(k == m) for m in range(d + 1)], j, a) for k in range(d + 1)]
            for a, m in zip(nodes, mults) for j in range(m)]


def check_hermite(trials=200):
    rng = random.Random(12)
    for _ in range(trials):
        d = rng.randint(0, 6)
        # s = d: el polinomio de los datos se anula y P(0) != 0
        if d >= 1:
            k = rng.randint(1, d)
            nodes = rng.sample([x for x in range(-6, 7) if x != 0], k)
            cuts = sorted(rng.sample(range(1, d), k - 1)) if k > 1 else []
            mults = [b - a for a, b in zip([0] + cuts, cuts + [d])]
            P = [Fraction(1)]
            for a, m in zip(nodes, mults):
                for _ in range(m):
                    P = poly_mul(P, [Fraction(-a), Fraction(1)])
            P += [Fraction(0)] * (d + 1 - len(P))
            assert all(deriv_at(P, j, a) == 0 for a, m in zip(nodes, mults) for j in range(m))
            assert P[0] != 0
        # s = d + 1: la matriz confluente es invertible y recupera H(0)
        k = rng.randint(1, d + 1)
        nodes = rng.sample([x for x in range(-6, 7) if x != 0], k)
        cuts = sorted(rng.sample(range(1, d + 1), k - 1)) if k > 1 else []
        mults = [b - a for a, b in zip([0] + cuts, cuts + [d + 1])]
        V = hermite_rows(nodes, mults, d)
        assert rank(V) == d + 1
        w = solve([list(col) for col in zip(*V)], [int(i == 0) for i in range(d + 1)])
        H = [Fraction(rng.randint(-9, 9)) for _ in range(d + 1)]
        data = [deriv_at(H, j, a) for a, m in zip(nodes, mults) for j in range(m)]
        assert sum(x * y for x, y in zip(w, data)) == H[0]
    # Corolario 1: Q nodos con J derivadas recuperan grado d si y solo si QJ >= d + 1
    for d in range(0, 7):
        for Q in range(1, 5):
            for J in range(1, 5):
                nodes, mults = list(range(1, Q + 1)), [J] * Q
                V = hermite_rows(nodes, mults, d)
                e0 = [int(k == 0) for k in range(d + 1)]
                recoverable = rank(V + [e0]) == rank(V)
                assert recoverable == (Q * J >= d + 1)
    print(f'Hermite: {trials} casos aleatorios; s <= d no determina H(0), s = d + 1 lo recupera; '
          'Corolario 1 para d <= 6, Q, J <= 4.')


# ------------------------------------------------------------------ 4
def check_structured():
    # V = span{1, T(T-1)}: coeficientes en la base de monomios
    basis = [[Fraction(1), Fraction(0), Fraction(0)], [Fraction(0), Fraction(-1), Fraction(1)]]
    E = [[deriv_at(b, 0, 1)] for b in basis]          # observacion H(1)
    l0 = [b[0] for b in basis]                         # H(0)
    assert [row[0] for row in E] == l0                 # l0 en la imagen de E*: H(0) = H(1)
    rng = random.Random(4)
    for _ in range(50):
        a, b = rng.randint(-9, 9), rng.randint(-9, 9)
        H = [a * x + b * y for x, y in zip(*basis)]
        assert deriv_at(H, 0, 0) == deriv_at(H, 0, 1)
    print('Proposicion 4: en span{1, T(T-1)} una observacion H(1) recupera H(0).')


# ------------------------------------------------------------------ 5
def check_example():
    clauses = [(1, 2, -3), (1, -2, 3), (-1, 2, 3), (-1, -2, -3), (1, 2, 3)]
    sols = [x for x in product((0, 1), repeat=3)
            if all(any(x[abs(l) - 1] == (l > 0) for l in c) for c in clauses)]
    assert sols == [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    H = [Fraction(0)] * 4
    for x in sols:
        p = [Fraction(1)]
        for _ in range(sum(x)):
            p = poly_mul(p, [Fraction(1), Fraction(1)])
        for k, c in enumerate(p):
            H[k] += c
    assert H[:3] == [3, 6, 3] and H[3] == 0
    h1, d1, dd1 = deriv_at(H, 0, 1), deriv_at(H, 1, 1), deriv_at(H, 2, 1)
    assert (h1, d1, dd1) == (12, 12, 6)
    assert h1 - d1 + dd1 / 2 == 3 == len(sols)
    print('Ejemplo F*: soluciones 011, 101, 110; H(1)=12, H\'(1)=12, H\'\'(1)=6; H(0)=3.')


if __name__ == '__main__':
    check_crossing()
    check_swap()
    check_hermite()
    check_structured()
    check_example()
    print('TODAS LAS COMPROBACIONES PASARON.')
