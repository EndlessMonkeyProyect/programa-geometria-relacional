#!/usr/bin/env python3
"""Controles exactos del marco de aparición, herencia y acarreos.

Solo biblioteca estándar. Las aserciones numéricas NO prueban RH.
Uso: python3 verificar_marco.py [--max-m 1024]
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd, isqrt, lcm
from pathlib import Path


def primos_hasta(n: int) -> list[int]:
    criba = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        criba[0] = 0
    if n >= 1:
        criba[1] = 0
    for p in range(2, isqrt(n) + 1):
        if criba[p]:
            criba[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if criba[p]]


def potencias_primas_hasta(n: int, primos: list[int]):
    return [(p, p**j) for p in primos if p <= n for j in range(1, 1 + n.bit_length()) if p**j <= n]


def s2(n: int) -> int:
    return n.bit_count()


def c(q: int, m: int) -> int:
    return int(2 * (m % q) >= q)


def ejecutar(max_m: int, salida: Path) -> dict:
    assert max_m >= 8
    techo = 2 * (max_m + 1)
    pp = potencias_primas_hasta(techo, primos_hasta(techo))
    r = [1] * (techo + 1)
    for p, q in pp:
        r[q] = p
    L = [1] * (techo + 1)
    cantidad = 0
    for n in range(2, techo + 1):
        assert r[n] == n // gcd(n, L[n - 1]); cantidad += 1
        L[n] = lcm(L[n - 1], n)
        assert L[n] == L[n - 1] * r[n]; cantidad += 1
        # Reconstrucción exacta por divisores: válida hasta techo.
        reconstruido = 1
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                reconstruido *= r[d]
                if d * d != n:
                    reconstruido *= r[n // d]
        assert reconstruido == n; cantidad += 1

    for n in range(1, min(techo, 100) + 1):
        producto = 1
        for d in range(1, n + 1):
            producto *= r[d] ** (n // d)
        assert producto == factorial(n); cantidad += 1

    ejemplos = []
    for m in range(1, max_m + 2):
        A = L[2 * m] // L[m]
        C = comb(2 * m, m)
        assert C % A == 0; cantidad += 1
        B = C // A
        assert L[2 * m] == A * L[m]; cantidad += 1
        # Cuadrado libre: cada primo aparece una vez como máximo.
        assert all(A % (p * p) for p in primos_hasta(2 * m) if p * p <= A); cantidad += 1
        via_pp = 1
        for p, q in pp:
            if m < q <= 2 * m:
                via_pp *= p
        assert A == via_pp; cantidad += 1
        via_acarreos = 1
        for p, q in pp:
            if q <= m and c(q, m):
                via_acarreos *= p
        assert B == via_acarreos; cantidad += 1
        assert (B & -B).bit_length() - 1 == s2(m) - 1; cantidad += 1
        if m <= max_m:
            A_prox = L[2 * m + 2] // L[m + 1]
            assert A_prox * r[m + 1] == A * r[2 * m + 1] * r[2 * m + 2]; cantidad += 1
            B_prox = comb(2 * m + 2, m + 1) // A_prox
            rimpar = r[m + 1] if r[m + 1] != 2 else 1
            assert B_prox * (m + 1) * r[2 * m + 1] == B * 2 * (2 * m + 1) * rimpar; cantidad += 1
        if m in (5, 6, 7, 8, 31, 32, 100, max_m):
            ejemplos.append({"m": m, "A": str(A), "B": str(B), "C": str(C), "v2B": s2(m) - 1})

    for J in range(1, 9):
        frecuencias = [0] * (J + 1)
        for m in range(2**J, 2**(J + 1)):
            frecuencias[s2(m) - 1] += 1
        assert frecuencias == [comb(J, k) for k in range(J + 1)]; cantidad += J + 1

    # Independencia sobre ciclos COMPLETOS de potencias de primos distintos.
    pares = [(4, 9), (8, 9), (9, 25), (16, 27), (8, 49), (25, 27)]
    for q, t in pares:
        assert gcd(q, t) == 1
        juntos = sum(c(q, m) * c(t, m) for m in range(q * t))
        assert juntos == (q // 2) * (t // 2); cantidad += 1

    # Cota óptima para TODAS las ventanas de los períodos enumerados.
    # Cálculo independiente por suma directa, con Fraction exacta.
    pruebas_ventanas = 0
    for q in (2, 3, 4, 5, 7, 8, 9, 11, 16, 25, 27):
        a, b = q // 2, q - q // 2
        media = Fraction(a, q)
        max_desv = Fraction(a * b, q)
        assert sum(c(q, m) for m in range(q)) == a; cantidad += 1
        for u in range(q):
            total = 0
            for N in range(0, 2 * q + 1):
                if N:
                    total += c(q, u + N - 1)
                desv = abs(Fraction(total) - N * media)
                assert desv <= max_desv, (q, u, N, desv, max_desv)
                pruebas_ventanas += 1
        assert abs(Fraction(sum(c(q, m) for m in range(b))) - b * media) == max_desv
        cantidad += 1

    salida.parent.mkdir(parents=True, exist_ok=True)
    resultado = {
        "estado": "OK",
        "max_m": max_m,
        "controles_exactos_basicos": cantidad,
        "ventanas_exactas": pruebas_ventanas,
        "controles_exactos_totales": cantidad + pruebas_ventanas,
        "pares_crt": len(pares),
        "ejemplos": ejemplos,
        "aclaracion": "Verificación finita de identidades. No constituye prueba de la estimación equivalente a RH.",
    }
    salida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OK | controles exactos: {cantidad + pruebas_ventanas} | escalas 1..{max_m + 1}")
    return resultado


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=1024)
    ap.add_argument("--salida", type=Path, default=Path(__file__).with_name("resultado_verificacion.json"))
    args = ap.parse_args()
    ejecutar(args.max_m, args.salida)
