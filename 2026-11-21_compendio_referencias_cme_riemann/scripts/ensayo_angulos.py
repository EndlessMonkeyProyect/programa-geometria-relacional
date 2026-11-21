#!/usr/bin/env python3
"""Ensayo de contraste CME-002 frente a las referencias f_n entre 1024 y 2048.

Prueba una asignación explícita y tentativa: cada referencia f_n como normal de
Householder, comparada con la regla angular pi/k de CME-002 con k = n.
Productos internos por la fórmula de Gram de prueba_reglas_de_peso.py.
Los errores óptimos y la fracción recuperada del paso 1024 -> 2048 se recalculan
en recalcular_gram.py. Requiere numpy.
"""
import math

from prueba_reglas_de_peso import gram, mu_of

M, N = 1024, 2048
n_ant = sum(mu_of(n) != 0 for n in range(1, M + 1))
n_nuevas = sum(mu_of(n) != 0 for n in range(M + 1, N + 1))
n_tot = sum(mu_of(n) != 0 for n in range(1, N + 1))
assert (n_ant, n_nuevas, n_tot) == (624, 621, 1245)

# Asignación experimental: normales f_1027 y f_1030 en la métrica de Gram.
a, b = 1027, 1030
assert mu_of(a) != 0 and mu_of(b) != 0
cos_a = gram(a, b) / math.sqrt(gram(a, a) * gram(b, b))
angulo_a = math.degrees(math.acos(min(1, max(-1, abs(cos_a)))))
angulo_cme_k = 180 / a
assert abs(angulo_a - 6.512951133432455) < 1e-6
assert abs(angulo_a - angulo_cme_k) > 6

# CME (2,3,k): régimen abierto cuando 1/2 + 1/3 + 1/k < 1.
assert 1/2 + 1/3 + 1/M < 1
assert 1/2 + 1/3 + 1/N < 1

print(f'Referencias libres de cuadrados: hasta {M}: {n_ant}; nuevas hasta {N}: {n_nuevas}; total: {n_tot}')
print(f'Normales candidatas f_{a}, f_{b}: cos = {cos_a:.12f}; ángulo = {angulo_a:.9f} grados')
print(f'Regla angular CME-002 con k = {a}: pi/k = {angulo_cme_k:.9f} grados')
print('CME (2,3,1024) y (2,3,2048): régimen abierto bajo la identificación k = N')
print('RESULTADO: la asignación f_n = normal da ángulos distintos de los de CME-002;')
print('queda descartada esa asignación concreta. Otros entrelazadores siguen sin definir.')
