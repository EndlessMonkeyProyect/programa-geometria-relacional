#!/usr/bin/env python3
"""Puentes finitos: referencias, firmas y economía de información.

Contrato: controles exactos de ejemplos definidos en los documentos.
Sin red ni bibliotecas externas; no se infieren cotas generales de complejidad.
"""

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import product


def wall_signature(x, L):
    """Distancia a 2L Z para L>0; igualdad exacta si x,L son fracciones."""
    if L <= 0:
        raise ValueError("L debe ser positiva")
    two_L = 2 * L
    r = x % two_L
    return min(r, two_L - r)


def factorizes(states, phi, q):
    """(sí, testigo) de q=g o phi para un conjunto de estados finito."""
    seen = {}
    for x in states:
        a, b = phi(x), q(x)
        if a in seen and seen[a][1] != b:
            return False, (seen[a][0], x)
        if a not in seen:
            seen[a] = (x, b)
    return True, None


def supplementary_bits(states, phi, q):
    """Mínimo de bits adicionales por fibra de phi (etiqueta de longitud fija)."""
    states = tuple(states)
    if not states:
        raise ValueError("Se requiere un conjunto de estados no vacío")
    answers = defaultdict(set)
    for x in states:
        answers[phi(x)].add(q(x))
    k = max(map(len, answers.values()))
    return (k - 1).bit_length(), k, {str(s): len(vals) for s, vals in answers.items()}


def classes_count(states, questions):
    states = tuple(states)
    if not states:
        raise ValueError("Se requiere X no vacío")
    return len({tuple(q(x) for q in questions) for x in states})


def update_compatible(states, phi, update):
    """Existe f con phi∘update=f∘phi si y solo si las fibras son estables."""
    seen = {}
    for x in states:
        key, successor = phi(x), phi(update(x))
        if key in seen and seen[key][1] != successor:
            return False, (seen[key][0], x)
        if key not in seen:
            seen[key] = (x, successor)
    return True, None


def pair_xor(a):
    n = len(a)
    return tuple(a[i] ^ a[j] for i in range(n) for j in range(i + 1, n))


def squared_distance(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def pairwise_squared_distances(points):
    return tuple(squared_distance(points[i], points[j])
                 for i in range(len(points)) for j in range(i + 1, len(points)))


def determinant3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def signed_volume6(points):
    p0, p1, p2, p3 = points
    def diff(p):
        return tuple(p[i] - p0[i] for i in range(3))
    return determinant3(diff(p1), diff(p2), diff(p3))


def satisfies_cnf(assignment, formula):
    return all(any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)
               for clause in formula)


def entails_clause(formula, clause, n):
    """F |= C; fuerza bruta finita para control, no algoritmo eficiente de SAT."""
    if any(not 1 <= abs(lit) <= n for row in list(formula) + [clause] for lit in row):
        raise ValueError("Un literal está fuera del universo declarado")
    return all(not satisfies_cnf(a, formula)
               or any(a[abs(lit) - 1] == (lit > 0) for lit in clause)
               for a in product((False, True), repeat=n))


def economy_break_even(fixed, direct, reused, max_queries=1000):
    """Primer número entero de consultas con fixed + m*reused < m*direct."""
    if fixed < 0 or reused < 0 or direct <= reused:
        raise ValueError("Se requiere fixed>=0 y 0<=reused<direct")
    for m in range(1, max_queries + 1):
        if fixed + m * reused < m * direct:
            return m
    return None


def run():
    x, y = Fraction(1, 4), Fraction(9, 4)
    q1 = lambda z: wall_signature(z, Fraction(1))
    q2 = lambda z: wall_signature(z, Fraction(2))
    factors, witness = factorizes((x, y), q1, q2)
    assert not factors and witness == (x, y)
    assert (q1(x), q1(y)) == (Fraction(1, 4), Fraction(1, 4))
    assert (q2(x), q2(y)) == (Fraction(1, 4), Fraction(7, 4))
    mirror_bits, mirror_k, _ = supplementary_bits((x, y), q1, q2)
    assert (mirror_bits, mirror_k) == (1, 2)

    xs = tuple(range(30))
    modular_bits, modular_k, fiber_counts = supplementary_bits(
        xs, lambda z: z % 6, lambda z: z % 10)
    assert (modular_bits, modular_k) == (3, 5)
    assert set(fiber_counts.values()) == {5}
    assert classes_count(xs, (lambda z: z % 6,)) == 6
    assert classes_count(xs, (lambda z: z % 6, lambda z: z % 10)) == 30
    assert classes_count(xs, (lambda z: z % 6, lambda z: z % 10)) >= 6

    mod4 = tuple(range(4))
    mod5 = tuple(range(5))
    good4, witness4 = update_compatible(mod4, lambda z: z % 2,
                                        lambda z: (z + 1) % 4)
    good5, witness5 = update_compatible(mod5, lambda z: z % 2,
                                        lambda z: (z + 1) % 5)
    assert good4 and witness4 is None
    assert not good5 and witness5 is not None

    four_bit_states = tuple(product((0, 1), repeat=4))
    xors = {pair_xor(a) for a in four_bit_states}
    assert len(four_bit_states) == 16 and len(xors) == 8
    assert all(pair_xor(a) == pair_xor(tuple(1 ^ v for v in a))
               for a in four_bit_states)
    assert all(pair_xor(a) == tuple((a[0] ^ a[i]) ^ (a[0] ^ a[j])
                                for i in range(4) for j in range(i + 1, 4))
               for a in four_bit_states)

    geom_plus = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    geom_minus = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1))
    metric_plus = pairwise_squared_distances(geom_plus)
    metric_minus = pairwise_squared_distances(geom_minus)
    assert metric_plus == metric_minus
    assert (signed_volume6(geom_plus), signed_volume6(geom_minus)) == (1, -1)

    F = ((1,),)
    assert entails_clause(F, (1,), 2)
    assert not entails_clause(F, (2,), 2)
    assert entails_clause(((1,), (-1,)), (2,), 2)
    assert economy_break_even(120, 20, 6) == 9

    return {
        "version": "2026-11-11-v0.1",
        "contract": "finite_exact",
        "mirror": {
            "old_signatures": [str(q1(x)), str(q1(y))],
            "new_signatures": [str(q2(x)), str(q2(y))],
            "factorizes": factors,
            "witness": [str(v) for v in witness],
            "supplementary_bits": mirror_bits,
        },
        "modular": {
            "old_classes": 6,
            "joint_classes": 30,
            "max_new_answers_per_old_fiber": modular_k,
            "supplementary_bits": modular_bits,
        },
        "updates": {
            "parity_z4_compatible": good4,
            "parity_z5_compatible": good5,
            "z5_witness": list(witness5),
        },
        "tetrahedron_binary": {"assignments": 16, "xor_edge_patterns": len(xors), "relative_bits": 3},
        "tetrahedron_geometry": {"squared_distances": list(metric_plus),
                                 "signed_volume6": [1, -1]},
        "cnf": {"inherited_x1": True, "new_x2": True, "unsat_entails_any": True},
        "economic_example": {"fixed": 120, "direct_per_query": 20,
                             "reuse_per_query": 6, "first_profitable_queries": 9},
        "test_groups": 7,
        "status": "PASS",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", metavar="PATH", help="Guardar JSON reproducible")
    args = parser.parse_args()
    result = run()
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, ensure_ascii=False, sort_keys=True)
            handle.write("\n")
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
