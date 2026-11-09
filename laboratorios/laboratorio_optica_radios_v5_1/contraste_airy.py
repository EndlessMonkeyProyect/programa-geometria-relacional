#!/usr/bin/env python3
# Endless Monkey Project — Relational Geometry Program
# Le Matt Ansatz Di Ego
# Contraste opcional de la sección B / Optional check of section B. Requiere numpy y scipy.
"""Compara el criterio discreto del laboratorio con una imagen física idealizada.

Imagen: suma incoherente de patrones de Airy (apertura circular de radio R0),
un patrón por fuente con su propia longitud de onda, receptor pancromático,
sin ruido. Se cuentan los máximos locales sobre la línea de las fuentes
(se descartan los anillos de Airy, menores al 5 % del pico).
"""
import importlib.util
import math
from pathlib import Path

import numpy as np
from scipy.special import j1

_ruta = Path(__file__).resolve().with_name('laboratorio_optica_radios_v5_1.py')
_spec = importlib.util.spec_from_file_location('lab', _ruta)
lab = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lab)

POS_A = np.array(lab.ESCENA_A)
POS_B = np.array(lab.ESCENA_B)
BANDAS = np.array(lab.BANDAS)
PESOS = np.array(lab.PESOS)
F = lab.doppler(lab.V)


def airy(theta, lam):
    x = 2 * math.pi * lab.R0 * np.sin(theta) / lam
    out = np.ones_like(x)
    nz = np.abs(x) > 1e-12
    out[nz] = (2 * j1(x[nz]) / x[nz]) ** 2
    return out


def imagen(pos, D, n=40001):
    ang = np.arctan(pos / D)
    margen = 3 * lab.umbral(max(lab.BANDAS), F)
    t = np.linspace(ang.min() - margen, ang.max() + margen, n)
    I = np.zeros_like(t)
    for a, lam, w in zip(ang, BANDAS * F, PESOS):
        I += (w / lam ** 2) * airy(t - a, lam)   # potencia w → pico ∝ w/λ²
    return t, I


def indices_maximos(I):
    idx = np.where((I[1:-1] > I[:-2]) & (I[1:-1] >= I[2:]))[0] + 1
    return [k for k in idx if I[k] > 0.05 * I.max()]


def profundidad_valle(I):
    k = indices_maximos(I)
    if len(k) < 2:
        return 0.0
    return 1 - I[k[0]:k[-1]].min() / min(I[k[0]], I[k[-1]])


def fwhm(t, I):
    arriba = np.where(I >= I.max() / 2)[0]
    return t[arriba[-1]] - t[arriba[0]]


def tramos(Ds, fun):
    out, prev, inicio = [], None, None
    for D in Ds:
        k = fun(D)
        if k != prev:
            if prev is not None:
                out.append((inicio, D, prev))
            prev, inicio = k, D
    out.append((inicio, Ds[-1], prev))
    return out


def main():
    t1, I1 = imagen(np.array([0.0]), 1e15)
    ancho_puntual = fwhm(t1, I1)
    print('== Instantes del laboratorio (escena A; B solo en la última columna) ==')
    print(f"{'D [m]':>9} {'ext/θ':>7} {'por banda':>9} {'Airy':>5} {'valle Airy':>10} "
          f"{'FWHM/puntual':>12} {'Airy B':>6}")
    for t in lab.INSTANTES:
        D = lab.D0 + lab.V * t
        tt, I = imagen(POS_A, D)
        _, IB = imagen(POS_B, D)
        print(f"{D:9.2e} {lab.extension_relativa(lab.ESCENA_A, D, F):7.2f} "
              f"{lab.componentes(lab.ESCENA_A, D, F):9d} {len(indices_maximos(I)):5d} "
              f"{profundidad_valle(I) * 100:9.2f}% {fwhm(tt, I) / ancho_puntual:12.2f} "
              f"{len(indices_maximos(IB)):6d}")

    print('\n== Recorrido continuo de D (escena A) ==')
    Ds = np.logspace(12, 15, 3000)
    for nombre, fun in (
        ('criterio por banda (laboratorio)', lambda D: lab.componentes(lab.ESCENA_A, D, F)),
        ('imagen Airy, máximos', lambda D: len(indices_maximos(imagen(POS_A, D, n=8001)[1]))),
    ):
        print(f'-- {nombre}')
        for a, b, k in tramos(Ds, fun):
            print(f'   D ∈ [{a:.2e}, {b:.2e}) → {k}')


if __name__ == '__main__':
    main()
