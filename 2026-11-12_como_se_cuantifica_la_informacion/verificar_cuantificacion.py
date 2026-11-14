#!/usr/bin/env python3
"""Verificacion de «¿Como se cuantifica la informacion de un sistema?» (12-XI-2026).

Solo biblioteca estandar y aritmetica exacta. Uso: python3 verificar_cuantificacion.py

  1. C4 y K4 bajo paridad: 16 asignaciones, 8 patrones, derivaciones de la seccion 5.
  2. Teorema 1: 2^(n-c) patrones de paridad en los 1.099 grafos etiquetados de 1 a 5 vertices.
  3. Teorema 2: dimension real de {s_u + s_v = 0} igual al numero de componentes bipartitas.
  4. Cinco de ocho estados: 14 planos afines, 56 conjuntos de cinco, 336 / 1.344 continuaciones.
  5. Economia del tetraedro: respuestas iguales y costos de los modelos A y B (seccion 8).
  6. Paridad mas clausulas OR: inclusion-exclusion frente a enumeracion (anexo A.5).
"""
from fractions import Fraction
from itertools import combinations, product
import random

V4 = 'ABCD'


def components(n, edges):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for u, v in edges:
        parent[find(u)] = find(v)
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), []).append(v)
    return list(groups.values())


def is_bipartite(comp, edges):
    color = {comp[0]: 0}
    stack = [comp[0]]
    adj = {v: [] for v in comp}
    for u, v in edges:
        if u in adj:
            adj[u].append(v)
            adj[v].append(u)
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in color:
                color[w] = 1 - color[u]
                stack.append(w)
            elif color[w] == color[u]:
                return False
    return True


def rank(rows, ncols):
    M = [[Fraction(x) for x in r] for r in rows]
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


# ------------------------------------------------------------------ 1
def check_c4_k4():
    idx = {v: i for i, v in enumerate(V4)}
    C4 = ['AB', 'BC', 'CD', 'DA']
    K4 = C4 + ['AC', 'BD']
    for edges in (C4, K4):
        pats = {tuple(s[idx[e[0]]] ^ s[idx[e[1]]] for e in edges) for s in product((0, 1), repeat=4)}
        assert len(pats) == 8
    for s in product((0, 1), repeat=4):
        b = {e: s[idx[e[0]]] ^ s[idx[e[1]]] for e in K4}
        assert b['AC'] == b['AB'] ^ b['BC']
        assert b['BD'] == b['BC'] ^ b['CD']
        assert b['DA'] == b['AB'] ^ b['BC'] ^ b['CD']
    print('C4 y K4: 16 asignaciones, 8 patrones (3 bits); AC, BD y DA se derivan de AB, BC, CD.')


# ------------------------------------------------------------------ 2 y 3
def check_graphs():
    total = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = [pairs[k] for k in range(len(pairs)) if mask >> k & 1]
            comps = components(n, E)
            c = len(comps)
            pats = {tuple(s[u] ^ s[v] for u, v in E) for s in product((0, 1), repeat=n)}
            assert len(pats) == 2 ** (n - c)
            beta = sum(is_bipartite(cp, E) for cp in comps)
            rows = [[int(k in (u, v)) for k in range(n)] for u, v in E]
            assert n - rank(rows, n) == beta
            total += 1
    assert total == 1 + 2 + 8 + 64 + 1024 == 1099
    print('Teorema 1: 2^(n-c) patrones en los 1.099 grafos de 1 a 5 vertices.')
    print('Teorema 2: dim {s_u+s_v=0} = componentes bipartitas en los mismos 1.099 grafos.')


# ------------------------------------------------------------------ 4
def check_five_of_eight():
    pts = list(product((0, 1), repeat=3))
    forms = [f for f in pts if any(f)]
    planes = {frozenset(p for p in pts if sum(a * b for a, b in zip(f, p)) % 2 == c)
              for f in forms for c in (0, 1)}
    assert len(planes) == 14 and all(len(P) == 4 for P in planes)
    fives = [frozenset(S) for S in combinations(pts, 5)]
    assert len(fives) == 56
    assert all(sum(P <= S for P in planes) == 1 for S in fives)
    confirm = revise = 0
    for excl in [(a, b, c) for a in pts for b in pts for c in pts if len({a, b, c}) == 3]:
        rest = frozenset(pts) - set(excl)
        for d in rest:
            if rest - {d} in planes:
                confirm += 1
            else:
                revise += 1
    assert (confirm, revise) == (336, 1344)
    print('Cinco de ocho: 14 planos afines; cada conjunto de cinco contiene uno; 336 confirman, 1.344 revisan.')


# ------------------------------------------------------------------ 5
class Store:
    def __init__(self, model, bits):
        self.model = model
        self.b = dict(bits)
        self.cost = 0

    def read(self, k):
        self.cost += 1
        return self.b[k]

    def xor(self, a, b):
        self.cost += 1
        return a ^ b

    def flip(self, k):
        if self.model == 'A':            # inversion atomica de un bit registrado
            self.cost += 1
            self.b[k] ^= 1
        else:                            # lectura + XOR con 1 + escritura
            v = self.read(k)
            v = self.xor(v, 1)
            self.cost += 1
            self.b[k] = v


def check_k4_costs():
    idx = {v: i for i, v in enumerate(V4)}
    full_keys = ['AB', 'BC', 'CD', 'DA', 'AC', 'BD']
    rng = random.Random(20261112)
    for model, fT, fR in (('A', (3, 1), (1, 3)), ('B', (9, 1), (3, 3))):
        for s0 in product((0, 1), repeat=4):
            for _ in range(20):
                s = list(s0)
                bits = {e: s[idx[e[0]]] ^ s[idx[e[1]]] for e in full_keys}
                T = Store(model, bits)
                R = Store(model, {k: bits[k] for k in ('AB', 'BC', 'CD')})
                U = Q = 0
                for op in [rng.choice('UQ') for _ in range(rng.randint(0, 12))]:
                    if op == 'U':
                        U += 1
                        s[0] ^= 1
                        for k in ('AB', 'DA', 'AC'):
                            T.flip(k)
                        R.flip('AB')
                    else:
                        Q += 1
                        ans_T = T.read('AC')
                        ans_R = R.xor(R.read('AB'), R.read('BC'))
                        assert ans_T == ans_R == s[0] ^ s[2]
                assert T.cost == fT[0] * U + fT[1] * Q
                assert R.cost == fR[0] * U + fR[1] * Q
    for U, Q in ((10, 3), (2, 10)):
        assert (3 * U + Q, U + 3 * Q) == {(10, 3): (33, 19), (2, 10): (16, 32)}[(U, Q)]
    print('Economia K4: respuestas AC identicas; modelo A 3U+Q frente a U+3Q, modelo B 9U+Q frente a 3U+3Q.')


# ------------------------------------------------------------------ 6
def solve_count(rows, n):
    """Numero de soluciones de un sistema afin sobre F2 (filas: (mascara, b))."""
    piv = []
    for mask, b in rows:
        for pm, pb, bit in piv:
            if mask >> bit & 1:
                mask ^= pm
                b ^= pb
        if mask == 0:
            if b:
                return 0
            continue
        piv.append((mask, b, mask.bit_length() - 1))
    return 2 ** (n - len(piv))


def check_inclusion_exclusion(trials=300):
    rng = random.Random(5)
    for _ in range(trials):
        n = rng.randint(3, 8)
        A = [(rng.randrange(1, 1 << n), rng.randint(0, 1)) for _ in range(rng.randint(0, n - 1))]
        k = rng.randint(0, 4)
        ors = [rng.sample([v * rng.choice((1, -1)) for v in range(1, n + 1)], rng.randint(1, 3))
               for _ in range(k)]
        brute = 0
        for x in product((0, 1), repeat=n):
            if all(sum(x[i] for i in range(n) if m >> i & 1) % 2 == b for m, b in A) and \
               all(any(x[abs(l) - 1] == (l > 0) for l in c) for c in ors):
                brute += 1
        ie, systems = 0, 0
        for S in range(1 << k):
            rows = list(A)
            for j in range(k):
                if S >> j & 1:                           # clausula j falsa: literales en falso
                    for l in ors[j]:
                        rows.append((1 << (abs(l) - 1), 0 if l > 0 else 1))
            systems += 1
            ie += (-1) ** bin(S).count('1') * solve_count(rows, n)
        assert ie == brute and systems <= 2 ** k
    print(f'Paridad + OR: inclusion-exclusion igual a la enumeracion en {trials} instancias aleatorias.')


if __name__ == '__main__':
    check_c4_k4()
    check_graphs()
    check_five_of_eight()
    check_k4_costs()
    check_inclusion_exclusion()
    print('TODAS LAS COMPROBACIONES PASARON.')
