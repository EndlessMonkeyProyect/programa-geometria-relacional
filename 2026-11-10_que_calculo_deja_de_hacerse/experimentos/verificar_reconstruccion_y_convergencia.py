#!/usr/bin/env python3
"""Verificador ligero y sin dependencias externas para los teoremas 1-4.
No reconstruye la extracción distribuida de compuertas ni reproduce las tablas C1-C8.
Uso: python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
"""
from itertools import combinations, product
from random import Random


def rank_count(n, equations):
    """Cantidad de soluciones de un sistema de ecuaciones XOR; cero si imposible."""
    basis = {}
    for mask, rhs in equations:
        mask, rhs = int(mask), int(rhs)
        while mask:
            p = mask.bit_length() - 1
            if p not in basis:
                basis[p] = (mask, rhs)
                break
            m, b = basis[p]
            mask ^= m
            rhs ^= b
        else:
            if rhs:
                return 0
    return 1 << (n - len(basis))


def count_ie(n, equations, ors):
    """Conteo XOR+OR por inclusión-exclusión; OR = tuplas (variable, negada)."""
    result = 0
    for include in product((0, 1), repeat=len(ors)):
        eqs = list(equations)
        for present, clause in zip(include, ors):
            if present:
                # Al negar una cláusula, todos sus literales deben resultar falsos.
                eqs.extend((1 << v, int(neg)) for v, neg in clause)
        result += (-1) ** sum(include) * rank_count(n, eqs)
    return result


def count_brute(n, equations, ors):
    total = 0
    for x in range(1 << n):
        if not all(((x & mask).bit_count() & 1) == rhs for mask, rhs in equations):
            continue
        if all(any(((x >> v) & 1) != neg for v, neg in clause) for clause in ors):
            total += 1
    return total


def all_affine_planes_f2_3():
    # Todo plano de dimensión 2 en F2^3 es un hiperplano m·x = c.
    return [frozenset(x for x in range(8) if ((x & m).bit_count() & 1) == c)
            for m in range(1, 8) for c in (0, 1)]


def test_gr3():
    patterns = set()
    for s in range(16):
        b = {(i, j): ((s >> i) & 1) ^ ((s >> j) & 1)
             for i in range(4) for j in range(i + 1, 4)}
        patterns.add(tuple(b.items()))
        for f in range(4):
            star = {i: ((s >> f) & 1) ^ ((s >> i) & 1) for i in range(4)}
            assert all(b[(i, j)] == (star[i] ^ star[j]) for i, j in b)
    assert len(patterns) == 8
    print('GR3: 16 estados de vertices -> 8 patrones de aristas; 3 bits minimos. OK')


def test_rosi():
    planes = all_affine_planes_f2_3()
    assert len(set(planes)) == 14
    closings = retractions = 0
    for forbidden in combinations(range(8), 3):
        allowed = set(range(8)) - set(forbidden)
        roots = [P for P in planes if P <= allowed]
        assert len(roots) == 1
        # La cuarta cláusula excluiría un estado que aún estaba permitido.
        for last in allowed:
            after = allowed - {last}
            if any(P <= after for P in planes):
                closings += 1
            else:
                retractions += 1
    assert (closings, retractions) == (56, 224)
    # Cada triple no ordenado corresponde a 3! órdenes de exclusión.
    print('ROSI: 56 cinco-conjuntos; 336 trayectorias ordenadas; '
          '336 cierres y 1344 retracciones. OK')


def test_local_3cnf():
    planes = all_affine_planes_f2_3()
    for a, b, c in combinations(range(8), 3):
        missing = {a, b, c}
        residue = a ^ b ^ c
        assert residue not in missing
        L = missing | {residue}
        assert L in planes
        P = frozenset(set(range(8)) - L)
        assert P in planes
        allowed = set(range(8)) - missing
        assert allowed == set(P) | {residue}
    print('3-CNF local: 56 ternas de exclusiones -> plano unico + residuo. OK')


def test_xor_or():
    rng = Random(20261110)
    for n in range(3, 10):
        for _ in range(25):
            eqs = []
            for _ in range(rng.randint(0, n)):
                vs = rng.sample(range(n), rng.randint(1, min(n, 3)))
                eqs.append((sum(1 << v for v in vs), rng.randint(0, 1)))
            ors = []
            for _ in range(rng.randint(0, 5)):
                vs = rng.sample(range(n), rng.randint(1, min(3, n)))
                ors.append(tuple((v, rng.randint(0, 1)) for v in vs))
            assert count_ie(n, eqs, ors) == count_brute(n, eqs, ors)
    print('XOR + OR: 175 instancias aleatorias contrastadas con fuerza bruta. OK')


if __name__ == '__main__':
    test_gr3()
    test_rosi()
    test_local_3cnf()
    test_xor_or()
    print('Todos los controles independientes completados.')
