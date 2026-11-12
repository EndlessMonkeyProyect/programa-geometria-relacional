#!/usr/bin/env python3
"""Controles finitos editoriales para la reflexión sobre referencia y P frente a NP.

No proporciona un algoritmo para 3-SAT general ni una cota general de complejidad.
"""

import json
import random
from itertools import combinations, permutations, product


def affine_planes():
    """Subconjuntos afines de cuatro puntos en F_2^3."""
    return [frozenset(points) for points in combinations(range(8), 4)
            if all(a ^ b ^ c in points for a, b, c in product(points, repeat=3))]


def check_five_states():
    planes = affine_planes()
    assert len(planes) == 14
    closures = retractions = initial_paths = 0
    universe = set(range(8))
    for exclusions in permutations(range(8), 3):
        allowed = universe.difference(exclusions)
        candidates = [plane for plane in planes if plane <= allowed]
        assert len(candidates) == 1
        plane = candidates[0]
        residual = next(iter(allowed.difference(plane)))
        initial_paths += 1
        for fourth in allowed:
            remaining = allowed.difference((fourth,))
            if fourth == residual:
                assert remaining == plane
                closures += 1
            else:
                assert fourth in plane and remaining != plane
                retractions += 1
    assert (initial_paths, closures, retractions) == (336, 336, 1344)
    return {"affine_planes": len(planes), "initial_paths": initial_paths,
            "closures": closures, "retractions": retractions}


def check_tetrahedron():
    patterns = set()
    for bits in product((0, 1), repeat=4):
        edges = tuple(bits[i] ^ bits[j] for i in range(4) for j in range(i + 1, 4))
        focus = tuple(bits[0] ^ bits[i] for i in range(1, 4))
        rebuilt = tuple((0, *focus)[i] ^ (0, *focus)[j]
                        for i in range(4) for j in range(i + 1, 4))
        assert edges == rebuilt
        patterns.add(edges)
    assert len(patterns) == 8
    return {"vertex_assignments": 16, "edge_patterns": len(patterns),
            "relative_bits": 3}


def affine_count(n, equations):
    """Número de soluciones de un sistema XOR por eliminación sobre F_2."""
    pivots = {}
    for mask, rhs in equations:
        row, value = mask, rhs
        while row:
            leading = row.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = (row, value)
                break
            other_row, other_value = pivots[leading]
            row ^= other_row
            value ^= other_value
        if row == 0 and value:
            return 0
    return 1 << (n - len(pivots))


def count_by_inclusion_exclusion(n, equations, clauses):
    total = 0
    for selected in product((0, 1), repeat=len(clauses)):
        forced = [(1 << (abs(lit) - 1), int(lit < 0))
                  for use, clause in zip(selected, clauses) if use for lit in clause]
        sign = -1 if sum(selected) % 2 else 1
        total += sign * affine_count(n, [*equations, *forced])
    return total


def count_by_brute_force(n, equations, clauses):
    count = 0
    for bits in product((0, 1), repeat=n):
        parity_ok = all((sum(bits[i] for i in range(n) if mask & (1 << i)) % 2) == rhs
                        for mask, rhs in equations)
        clauses_ok = all(any(bits[abs(lit) - 1] == int(lit > 0) for lit in clause)
                         for clause in clauses)
        count += parity_ok and clauses_ok
    return count


def check_xor_or():
    rng = random.Random(20261110)
    for _ in range(50):
        n = rng.randrange(2, 7)
        equations = [(rng.randrange(1, 1 << n), rng.randrange(2))
                     for _ in range(rng.randrange(5))]
        clauses = []
        for _ in range(rng.randrange(5)):
            variables = rng.sample(range(1, n + 1), rng.randrange(1, min(n, 3) + 1))
            clauses.append(tuple(var if rng.randrange(2) else -var for var in variables))
        exact = count_by_inclusion_exclusion(n, equations, clauses)
        brute = count_by_brute_force(n, equations, clauses)
        assert exact == brute, (n, equations, clauses, exact, brute)
    return {"cases": 50, "result": "PASS"}


def main():
    result = {"five_states": check_five_states(),
              "tetrahedron": check_tetrahedron(),
              "xor_or": check_xor_or(), "status": "PASS"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
