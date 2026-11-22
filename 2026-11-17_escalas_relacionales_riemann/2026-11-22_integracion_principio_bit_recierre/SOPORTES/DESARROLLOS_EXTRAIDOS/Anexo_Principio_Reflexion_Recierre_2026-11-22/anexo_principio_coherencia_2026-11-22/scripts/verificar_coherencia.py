#!/usr/bin/env python3
"""Verificación reproducible del anexo de recierre y coherencia de Möbius.

Usa solo enteros y la biblioteca estándar. Las identidades y la caracterización
asintótica se demuestran en la nota; este script es un control finito.
"""
from __future__ import annotations
import argparse
import csv
from fractions import Fraction
from math import sqrt
from pathlib import Path


def sieve_mobius(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    lp = [0] * (limit + 1)
    primes = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if not lp[n]:
            lp[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            v = p * n
            if v > limit or p > lp[n]:
                break
            lp[v] = p
            if n % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[n]
    return mu


def truncated_divisor_sum(mu: list[int], n: int, upper: int) -> int:
    result = 0
    k = 1
    while k * k <= n:
        if n % k == 0:
            if k <= upper:
                result += mu[k]
            d = n // k
            if d != k and d <= upper:
                result += mu[d]
        k += 1
    return result


def verify_local_recierre(mu: list[int], max_octave: int) -> int:
    checks = 0
    for N in range(1, max_octave + 1):
        for m in range(N + 1, 2 * N + 1):
            assert truncated_divisor_sum(mu, m, N) == -mu[m], (N, m)
            assert truncated_divisor_sum(mu, m, 2 * N) == 0, (N, m)
            checks += 2
    return checks


def verify_uniqueness(mu: list[int], nmax: int) -> int:
    # La recurrencia determina la única función con a(1)=1 y
    # sum_{d|n} a(d)=0 para todo n>1.
    a = [0] * (nmax + 1)
    a[1] = 1
    for n in range(2, nmax + 1):
        # Todos los divisores propios son menores que n.
        a[n] = -truncated_divisor_sum(a, n, n - 1)
        assert a[n] == mu[n], n
    return nmax - 1



def verify_prime_reflection_and_boundary(mu: list[int], Xmax: int) -> int:
    # Emparejamiento exacto de las copias con y sin p: mu(pr)=-mu(r)
    # cuando p no divide a r. La suma queda en la frontera (X/p, X].
    primes = [2, 3, 5, 7, 11]
    total = 0
    prefix = [0] * (Xmax + 1)
    for x in range(1, Xmax + 1):
        prefix[x] = prefix[x - 1] + mu[x]
    for p in primes:
        for x in range(1, Xmax + 1):
            boundary = sum(mu[n] for n in range(x // p + 1, x + 1) if n % p != 0)
            assert prefix[x] == boundary, (p, x, prefix[x], boundary)
            total += 1
    # Involución que conmuta soporte primo; cada par cruza toda octava.
    for N in [4, 16, 64, 256]:
        for n in range(N + 1, 2 * N + 1):
            if mu[n] == 0:
                continue
            for p in primes:
                reflected = n // p if n % p == 0 else n * p
                assert not (N < reflected <= 2 * N)
                assert mu[reflected] == -mu[n]
                total += 1
    return total

def octave_rows(mu: list[int], min_j: int, max_j: int):
    rows = []
    for j in range(min_j, max_j + 1):
        N = 2**j
        A = 0
        S = 0
        B = 0
        t_of_B = N
        for n in range(N + 1, 2 * N + 1):
            m = mu[n]
            A += m * m
            S += m
            if abs(S) > B:
                B = abs(S)
                t_of_B = n
        assert A > 0
        C2 = Fraction(B * B, N * A)
        # Para cualquier prefijo, C(t)^2 = S(t)^2/(N*A), exacto.
        assert C2 <= 1
        rows.append({
            'j': j,
            'N': N,
            'novedad_A': A,
            'suma_final_S': S,
            'maximo_prefijos_B': B,
            't_del_maximo': t_of_B,
            'coherencia_max_cuadrada_fraccion': f'{C2.numerator}/{C2.denominator}',
            'coherencia_max': f'{sqrt(float(C2)):.12f}',
            'sqrtN_por_coherencia': f'{sqrt(N) * sqrt(float(C2)):.12f}',
        })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-j', type=int, default=17)
    parser.add_argument('--max-local-N', type=int, default=64)
    parser.add_argument('--salida', default=str(Path(__file__).resolve().parents[1] / 'datos_octavas.csv'))
    args = parser.parse_args()
    assert args.max_j >= 4
    limit = max(2 ** (args.max_j + 1), 2 * args.max_local_N, 512, 11 * 512)
    mu = sieve_mobius(limit)
    checks = verify_local_recierre(mu, args.max_local_N)
    uniqueness = verify_uniqueness(mu, 512)
    reflection = verify_prime_reflection_and_boundary(mu, 256)
    rows = octave_rows(mu, 4, args.max_j)
    # Contraste de los datos ya registrados en el Compendio (21-XI)
    expected = {1024: (621, 11, 17), 2048: (1246, -26, 32)}
    for row in rows:
        N = row['N']
        if N in expected:
            assert (row['novedad_A'], row['suma_final_S'], row['maximo_prefijos_B']) == expected[N], row
    path = Path(args.salida)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'Recierre local: {checks} verificaciones enteras exactas')
    print(f'Unicidad de coeficientes: {uniqueness} comprobaciones enteras exactas')
    print(f'Reflexión y frontera de escala: {reflection} controles enteros exactos')
    print('Filas diádicas:', len(rows))
    print('    N        A       S       B       coherencia_max')
    for row in rows:
        print(f"{row['N']:7} {row['novedad_A']:8} {row['suma_final_S']:7} {row['maximo_prefijos_B']:7} {row['coherencia_max']}")
    print('Datos guardados:', path)
    print('Resultado: identidades finitas comprobadas; sin conclusión asintótica de RH.')


if __name__ == '__main__':
    main()
