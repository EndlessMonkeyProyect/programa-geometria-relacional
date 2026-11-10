#!/usr/bin/env python3
"""Recierre exacto de dos plaquetas Z2; contraste economía ↔ gauge.
Verifica todas las 64 configuraciones de seis enlaces de frontera,
para cuatro valores del acoplamiento. No es un cálculo de Yang–Mills 4D.
"""
from itertools import product
from math import cosh, exp, log, sqrt


def comprobar(beta):
    k_eff = 0.5 * log(cosh(2 * beta))
    prefactor = 2 * sqrt(cosh(2 * beta))
    max_error = 0.0
    histogram = {-1: 0, 1: 0}
    for e in product((-1, 1), repeat=6):
        a = e[0] * e[1] * e[2]
        b = e[3] * e[4] * e[5]
        p = a * b
        histogram[p] += 1
        directo = sum(exp(beta * t * (a + b)) for t in (-1, 1))
        recerrado = prefactor * exp(k_eff * p)
        max_error = max(max_error, abs(directo - recerrado))
        assert abs(directo - recerrado) < 1e-12
    assert histogram == {-1: 32, 1: 32}
    print(f"beta={beta:.2f}  K_eff={k_eff:.12f}  "
          f"clases={histogram}  error_max={max_error:.3e}")


if __name__ == "__main__":
    for value in (0.00, 0.25, 0.50, 1.00):
        comprobar(value)
