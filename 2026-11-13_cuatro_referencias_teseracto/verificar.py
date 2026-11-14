#!/usr/bin/env python3
"""Verificacion de «Cuatro referencias, paridad y reconstruccion de un teseracto», v1.1.

Solo biblioteca estandar y aritmetica exacta. Uso: python3 verificar.py

Comprueba por enumeracion finita: Q4, las dos 16-celdas y sus 16 celdas, las firmas
por pares (n = 2..7), los 15 patrones de regiones, la coincidencia de S_i S_j y S_j S_i
solo sobre la arista comun, y el lema 1 con la etiqueta F del teorema 6 en todas las
palabras reducidas hasta longitud PROFUNDIDAD. Las afirmaciones sobre orbitas completas
(proposicion 4, teoremas 5 y 6) se demuestran en el articulo.
"""
from fractions import Fraction as Fr
from itertools import combinations, product

PROFUNDIDAD = 10
V = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
# N_i = 3I - 2 v_i v_i^T ;  S_i(z) = (N_i z - 2 v_i) / 3
N = tuple(tuple(tuple((3 if a == b else 0) - 2 * v[a] * v[b] for b in range(3))
                for a in range(3)) for v in V)
E = tuple(tuple(int(k == i) for k in range(4)) for i in range(4))


def signature(bits):
    return tuple(bits[i] ^ bits[j] for i, j in combinations(range(len(bits)), 2))


def parity(bits):
    return sum(bits) % 2


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


# ---------------------------------------------------------------- secciones 2-4
def check_binary():
    X = list(product((0, 1), repeat=4))
    edges = {frozenset((x, y)) for x, y in combinations(X, 2) if hamming(x, y) == 1}
    assert len(X) == 16 and len(edges) == 32
    assert all(parity(x) != parity(y) for x, y in map(tuple, edges))
    fibers = {}
    for x in X:
        fibers.setdefault(signature(x), []).append(x)
    assert len(fibers) == 8 and all(len(v) == 2 for v in fibers.values())
    for q, (x, y) in fibers.items():
        assert xor(x, y) == (1, 1, 1, 1)
        assert parity(x) == parity(y) == q[0] ^ q[5] == q[1] ^ q[4] == q[2] ^ q[3]
        assert q[3] == q[0] ^ q[1]  # q23 = q12 xor q13
        assert q[4] == q[0] ^ q[2]  # q24 = q12 xor q14
        assert q[5] == q[1] ^ q[2]  # q34 = q13 xor q14
        assert signature((0, q[0], q[1], q[2])) == q
    assert sum(parity(v[0]) == 0 for v in fibers.values()) == 4
    image = [q for q in product((0, 1), repeat=6)
             if q[3] == q[0] ^ q[1] and q[4] == q[0] ^ q[2] and q[5] == q[1] ^ q[2]]
    assert sorted(image) == sorted(fibers)
    print('Q4: 16 vertices y 32 aristas, todas entre par e impar.')
    print('Firma K4: 8 fibras de dos; imagen = ecuaciones triangulares; reconstruccion correcta.')


def check_16_cells():
    X = list(product((0, 1), repeat=4))
    for eps in (0, 1):
        fam = [x for x in X if parity(x) == eps]
        pts = {x: tuple((-1) ** b for b in x) for x in fam}
        assert len(fam) == 8
        # cuatro pares antipodales de vectores ortogonales de igual norma
        reps = [p for p in pts.values() if p[0] == 1]
        assert len(reps) == 4 and all(tuple(-c for c in p) in pts.values() for p in reps)
        assert all(dot(a, b) == 0 for a, b in combinations(reps, 2))
        assert all(dot(a, a) == 4 for a in reps)
        edges = [(x, y) for x, y in combinations(fam, 2) if hamming(x, y) == 2]
        assert len(edges) == 24
        assert sum(hamming(x, y) == 4 for x, y in combinations(fam, 2)) == 4
        cells = [c for c in combinations(fam, 4)
                 if all(hamming(x, y) == 2 for x, y in combinations(c, 2))]
        assert len(cells) == 16
        for c in cells:
            P = [pts[x] for x in c]
            normal = tuple(sum(p[k] for p in P) for k in range(4))
            values = sorted(dot(normal, q) for q in pts.values())
            assert values == [-4] * 4 + [4] * 4          # plano soporte n.y = 4
            assert all(dot(normal, p) == 4 for p in P)    # contiene exactamente la celda
            dists = {sum((a - b) ** 2 for a, b in zip(p, q)) for p, q in combinations(P, 2)}
            assert dists == {8}                           # tetraedro regular
    print('16-celdas: 8 vertices, 24 aristas y 16 celdas tetraedricas regulares en cada familia.')


def check_general_n():
    for n in range(2, 8):
        fibers = {}
        for x in product((0, 1), repeat=n):
            fibers.setdefault(signature(x), []).append(x)
        assert len(fibers) == 2 ** (n - 1)
        assert all(len(v) == 2 for v in fibers.values())
        same = all(parity(a) == parity(b) for a, b in fibers.values())
        opposite = all(parity(a) != parity(b) for a, b in fibers.values())
        assert same if n % 2 == 0 else opposite
    print('Generalizacion n=2..7: paridad recuperable si y solo si n par.')


# ---------------------------------------------------------------- secciones 5-6
def S(i, z):
    return tuple(z[j] - Fr(2, 3) * (dot(V[i], z) + 1) * V[i][j] for j in range(3))


def check_planes():
    assert tuple(sum(v[j] for v in V) for j in range(3)) == (0, 0, 0)
    # certificado del patron ausente: sum_i v_i.z = 0 para todo z, luego no es < -4
    patterns = set()
    for mark in product((0, 1), repeat=4):
        k = sum(mark)
        if k == 4:
            continue
        if k == 0:
            z = (Fr(0), Fr(0), Fr(0))
        else:
            values = [Fr(-2) if mark[i] else Fr(2 * k, 4 - k) for i in range(4)]
            assert sum(values) == 0
            z = tuple(sum(values[i] * V[i][j] for i in range(4)) / 4 for j in range(3))
            assert all(dot(V[i], z) == values[i] for i in range(4))
        patterns.add(tuple(int(dot(v, z) < -1) for v in V))
    assert len(patterns) == 15
    print('Planos tetraedricos: 15 patrones realizables; el exterior a las cuatro caras no.')


def affine(i):
    return ([[Fr(N[i][a][b], 3) for b in range(3)] for a in range(3)],
            [Fr(-2 * V[i][a], 3) for a in range(3)])


def compose(f, g):  # f o g
    (A, b), (C, d) = f, g
    AC = [[sum(A[a][k] * C[k][c] for k in range(3)) for c in range(3)] for a in range(3)]
    return AC, [sum(A[a][k] * d[k] for k in range(3)) + b[a] for a in range(3)]


def apply(f, z):
    A, b = f
    return tuple(sum(A[a][k] * z[k] for k in range(3)) + b[a] for a in range(3))


def rank3(M):
    M = [row[:] for row in M]
    r = 0
    for c in range(3):
        piv = next((i for i in range(r, 3) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(3):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [M[i][k] - f * M[r][k] for k in range(3)]
        r += 1
    return r


def check_commutation():
    for i, j in combinations(range(4), 2):
        R = compose(affine(i), affine(j))           # S_i S_j
        R2 = compose(R, R)                           # (S_i S_j)^2
        A = R2[0]
        assert rank3([[A[a][b] - (a == b) for b in range(3)] for a in range(3)]) == 2
        k, l = [m for m in range(4) if m not in (i, j)]
        for vert in (V[k], V[l]):                    # la arista comun pasa por v_k y v_l
            z = tuple(map(Fr, vert))
            assert S(i, z) == z and S(j, z) == z and apply(R2, z) == z
        z = tuple(map(Fr, (2, 3, 5)))
        assert S(i, S(j, z)) != S(j, S(i, z))
    print('Reflexiones: S_iS_j = S_jS_i exactamente sobre la recta de la arista comun (6 pares).')


# ---------------------------------------------------------------- seccion 7.1
def canon(m, y):
    """Punto y / 3^m en forma reducida."""
    while m > 0 and all(c % 3 == 0 for c in y):
        y, m = tuple(c // 3 for c in y), m - 1
    return m, y


def S_int(j, key):
    m, y = key
    y2 = tuple(sum(N[j][a][k] * y[k] for k in range(3)) - 2 * 3 ** m * V[j][a]
               for a in range(3))
    return canon(m + 1, y2)


def matmul(A, B):
    return tuple(tuple(sum(A[a][k] * B[k][b] for k in range(3)) for b in range(3))
                 for a in range(3))


def check_quotient(depth=PROFUNDIDAD):
    ident = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    c = (0, (0, 0, 0))                       # centroide
    label = {c: (0, 0, 0, 0)}
    frontier = [(None, None, ident, c)]      # (primera letra, ultima letra, N-producto, punto)
    for n in range(1, depth + 1):
        new = []
        sign = 1 if n % 2 == 1 else -1       # (-1)^(n-1)
        for first, last, M, key in frontier:
            for j in range(4):
                if j == first:
                    continue
                M2 = matmul(N[j], M)
                lastj = j if last is None else last
                assert all((M2[a][b] - sign * V[j][a] * V[lastj][b]) % 3 == 0
                           for a in range(3) for b in range(3))          # lema 1, parte lineal
                key2 = S_int(j, key)
                m2, tau = key2
                assert m2 == n                                            # 3^n pi(w)(c) no es 0 mod 3
                r = tuple(t % 3 for t in tau)
                assert r in (tuple(v % 3 for v in V[j]), tuple(-v % 3 for v in V[j]))  # lema 1, traslacion
                assert key2 not in label                                  # estabilizador trivial
                label[key2] = xor(label[key], E[j])
                new.append((j, lastj, M2, key2))
        assert len(new) == 4 * 3 ** (n - 1)
        frontier = new
    assert len(label) == 1 + 2 * (3 ** depth - 1)
    # ecuacion F(S_i z) = F(z) xor e_i en toda la bola de radio depth-1
    for key, lab in label.items():
        if key[0] < depth:
            for i in range(4):
                assert label[S_int(i, key)] == xor(lab, E[i])
    classes = {}
    for key, lab in label.items():
        classes.setdefault(lab, []).append(key[0])
    assert len(classes) == 16
    assert all(min(ls) == sum(lab) for lab, ls in classes.items())
    sizes = [len(v) for v in classes.values()]
    print(f'Lema 1: verificado en las {len(label) - 1} palabras reducidas de longitud 1..{depth}.')
    print(f'Orbita del centroide: {len(label)} puntos distintos; 16 clases '
          f'({min(sizes)} a {max(sizes)} puntos cada una); F(S_i z) = F(z) + e_i.')


def check_integer_starts(depth=7):
    good = [z for z in product(range(3), repeat=3)
            if all((dot(v, z) + 1) % 3 for v in V)]
    for z0 in good:
        frontier = [(None, (0, z0))]
        for n in range(1, depth + 1):
            new = []
            for first, (m, y) in frontier:
                for j in range(4):
                    if j == first:
                        continue
                    y2 = tuple(sum(N[j][a][k] * y[k] for k in range(3)) - 2 * 3 ** m * V[j][a]
                               for a in range(3))
                    assert any(t % 3 for t in y2)            # 3^n pi(w)(z0) no es 0 mod 3
                    new.append((j, (m + 1, y2)))
            frontier = new
    z = (Fr(-1), Fr(0), Fr(0))                               # punto del plano H_1
    assert dot(V[0], z) == -1 and S(0, z) == z
    print(f'Inicios enteros con v_i.z0 != -1 (mod 3): {len(good)} residuos, estabilizador trivial '
          f'hasta longitud {depth}. Sobre H_1, S_1 fija el punto: sin etiqueta.')


if __name__ == '__main__':
    check_binary()
    check_16_cells()
    check_general_n()
    check_planes()
    check_commutation()
    check_quotient()
    check_integer_starts()
    print('TODAS LAS COMPROBACIONES FINITAS PASARON.')
