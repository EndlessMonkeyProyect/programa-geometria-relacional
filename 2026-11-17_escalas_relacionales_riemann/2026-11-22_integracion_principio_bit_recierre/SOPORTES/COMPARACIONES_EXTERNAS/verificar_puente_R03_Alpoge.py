#!/usr/bin/env python3
"""Verificador exacto de coeficientes racionales del puente de sumas ponderadas.
No verifica RH ni la prueba Lean; usa aritmética exacta de Fraction.
"""
from fractions import Fraction
from math import isqrt


def primo(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def potencias_primas(y):
    for p in range(2, y + 1):
        if not primo(p):
            continue
        n = p
        while n <= y:
            yield p, n
            n *= p


def coeficientes(y):
    d = {}
    for p, n in potencias_primas(y):
        d[p] = d.get(p, Fraction(0)) + Fraction(y, n) - 1
    return {p: c for p, c in d.items() if c}


def cerrada_un_primo(y, p):
    if y < p:
        return Fraction(0)
    n, k = p, 0
    while n <= y:
        k += 1
        n *= p
    return Fraction(y, p - 1) * (1 - Fraction(1, p**k)) - k


def verificar(y, S):
    todos = coeficientes(y)
    dentro = {p: c for p, c in todos.items() if p in S}
    fuera = {p: c for p, c in todos.items() if p not in S}
    reconstruidos = {p: dentro.get(p, 0) + fuera.get(p, 0) for p in todos}
    assert todos == reconstruidos
    for p, c in dentro.items():
        assert c == cerrada_un_primo(y, p), (y, p, c)
    return todos, dentro, fuera


if __name__ == "__main__":
    for y in (10, 30, 100, 1000):
        todos, dentro, fuera = verificar(y, {2, 3})
        print(f"PASS y={y}: {len(todos)} primos; {len(dentro)} dentro, {len(fuera)} fuera")
        if y == 30:
            assert dentro == {2: Fraction(193, 8), 3: Fraction(103, 9)}
            assert fuera == {5: Fraction(26, 5), 7: Fraction(23, 7),
                             11: Fraction(19, 11), 13: Fraction(17, 13),
                             17: Fraction(13, 17), 19: Fraction(11, 19),
                             23: Fraction(7, 23), 29: Fraction(1, 29)}
            print("Coeficientes de log(p), y=30:", todos)
    print("ALL PASS — identidad finita exacta; sin afirmaciones asintoticas")
