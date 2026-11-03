#!/usr/bin/env python3
"""
Verificador: la cadena de duplicación por reflexión y el cruce [x=v][y=u].

Comprueba, con enteros exactos, las proposiciones de la §7 del paper
«El cruce como reflejo central» (Programa de Geometría Relacional, 3-11-2026).

Regla de duplicación (Cayley–Dickson, nota v2.2 del programa, 13-10-2026):
    (a, b)(c, d) = (ac − d̄ b,  d a + b c̄),      conj(a, b) = (ā, −b)
Desde los reales da los niveles N = 1, 2, 4, 8, 16.

Para cada nivel N se definen, con e_p e_q = σ(p,q) e_(p⊕q):
    ψ_k(p, q) = [p ⊕ q = k] σ(p, q)
    R(x,y,u,v) = Σ_k ψ_k(x,y) ψ_k(v,u)      (barata por filas)
    C(x,y,u,v) = Σ_k ψ_k(x,u) ψ_k(v,y)      (barata por columnas)
    L_x[k, y]  = ψ_k(x, y)                  (multiplicación a la izquierda por e_x)

Se verifica:
  P0  e_p e_q = ±e_(p⊕q) en cada nivel.
  P1  identidad (28) y R + C = 2·cruce en N = 2, 4, 8; falla en N = 16.
  P2  R = (L_vᵀ L_x)[u,y], C = (L_xᵀ L_v)[u,y] y L_vᵀ L_x + L_xᵀ L_v = 2[x=v]·Id.
  P3  rangos de R por filas y por columnas; costo por bloque con el conteo del Lema 2
      (log2 rango por filas + log2 rango por columnas + 2) frente a 4·log2 N.
  C4  asociatividad de cada nivel; ganancia solo en el nivel no asociativo.

Uso: python3 verificar_cadena_duplicacion.py [salida.json]
"""

import itertools as it
import json
import sys
from math import log2

import numpy as np


# ---------------------------------------------------------------- álgebra exacta

def conj(x):
    if len(x) == 1:
        return list(x)
    h = len(x) // 2
    return conj(x[:h]) + [-v for v in x[h:]]


def suma(x, y):
    return [a + b for a, b in zip(x, y)]


def resta(x, y):
    return [a - b for a, b in zip(x, y)]


def mul(x, y):
    if len(x) == 1:
        return [x[0] * y[0]]
    h = len(x) // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return resta(mul(a, c), mul(conj(d), b)) + suma(mul(d, a), mul(b, conj(c)))


def unidad(i, N):
    v = [0] * N
    v[i] = 1
    return v


# ---------------------------------------------------------------- nivel N

def nivel(N):
    tabla = {}
    destino_xor = True
    for p in range(N):
        for q in range(N):
            r = mul(unidad(p, N), unidad(q, N))
            nz = [k for k, v in enumerate(r) if v]
            destino_xor &= nz == [p ^ q]
            tabla[(p, q)] = r[p ^ q]

    def psi(k, p, q):
        return tabla[(p, q)] if (p ^ q) == k else 0

    violaciones_28 = sum(
        1 for p, q, pp, qq in it.product(range(N), repeat=4)
        if (p ^ q) == (pp ^ qq) and q != qq
        and tabla[(p, q)] * tabla[(pp, qq)] + tabla[(p, qq)] * tabla[(pp, q)] != 0)

    asociativa = all(
        mul(mul(unidad(a, N), unidad(b, N)), unidad(c, N))
        == mul(unidad(a, N), mul(unidad(b, N), unidad(c, N)))
        for a, b, c in it.product(range(N), repeat=3))

    out = {
        "N": N,
        "P0_destino_por_xor": destino_xor,
        "P1_violaciones_identidad_28": violaciones_28,
        "C4_asociativa": asociativa,
    }
    if N > 8:
        return out

    def R(x, y, u, v):
        return sum(psi(k, x, y) * psi(k, v, u) for k in range(N))

    def C(x, y, u, v):
        return sum(psi(k, x, u) * psi(k, v, y) for k in range(N))

    cruce = all(R(*w) + C(*w) == 2 * int(w[0] == w[3] and w[1] == w[2])
                for w in it.product(range(N), repeat=4))

    L = {x: np.array([[psi(k, x, y) for y in range(N)] for k in range(N)]) for x in range(N)}
    hurwitz_radon = all(
        np.array_equal(L[v].T @ L[x] + L[x].T @ L[v], 2 * int(x == v) * np.eye(N, dtype=int))
        for x in range(N) for v in range(N))
    dos_ordenes = all(
        R(x, y, u, v) == (L[v].T @ L[x])[u, y] and C(x, y, u, v) == (L[x].T @ L[v])[u, y]
        for x, y, u, v in it.product(range(N), repeat=4))

    filas = np.zeros((N * N, N * N))
    cols = np.zeros((N * N, N * N))
    for x, y, u, v in it.product(range(N), repeat=4):
        filas[x * N + y, u * N + v] = R(x, y, u, v)
        cols[x * N + u, y * N + v] = R(x, y, u, v)
    rf, rc = int(np.linalg.matrix_rank(filas)), int(np.linalg.matrix_rank(cols))
    costo = log2(rf) + log2(rc) + 2
    out.update({
        "P1_R_mas_C_igual_2_cruce": cruce,
        "P2_dos_ordenes": dos_ordenes,
        "P2_relaciones_Hurwitz_Radon": hurwitz_radon,
        "P3_rango_R_filas": rf,
        "P3_rango_R_columnas": rc,
        "P3_costo_bloque_conteo_Lema_2": round(costo, 4),
        "P3_costo_cruce": 4 * log2(N),
        "P3_gana": costo < 4 * log2(N),
    })
    return out


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "resultados_cadena_duplicacion.json"
    niveles = [nivel(N) for N in (2, 4, 8, 16)]
    con_ganancia = [n["N"] for n in niveles if n.get("P3_gana")]
    no_asociativos = [n["N"] for n in niveles if not n["C4_asociativa"]]
    res = {
        "referencia": "Paper «El cruce como reflejo central», §7; Claude (Anthropic) 2026, §4 y Apéndice H",
        "regla": "(a,b)(c,d) = (ac − conj(d) b, d a + b conj(c)); conj(a,b) = (conj(a), −b)",
        "niveles": niveles,
        "niveles_con_ganancia": con_ganancia,
        "niveles_no_asociativos_hasta_8": [N for N in no_asociativos if N <= 8],
        "C4_ganancia_solo_en_el_nivel_no_asociativo": con_ganancia == [N for N in no_asociativos if N <= 8],
    }
    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # consolas Windows con cp1252
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
