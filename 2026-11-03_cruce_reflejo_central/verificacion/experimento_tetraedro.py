#!/usr/bin/env python3
"""
Experimento: el tetraedro como base para descomponer el cruce [x=v][y=u].

Referencia del mecanismo: Claude (Anthropic), "A 2^{o(n)} Time Algorithm for 3-SAT",
26-10-2026, §4 (ecs. 27-31, Definición 5) y Apéndice H.
Referencia del tetraedro: clase par del cubo de espejos, x⊕y⊕z = 0,
{000, 011, 101, 110}, torsor de F2^2 (Imagen Total 3.4.1 del programa).

Costo de una pieza = log2(rango por filas) + log2(rango por columnas), con
    filas    = corte (x,y)|(u,v)
    columnas = corte (x,u)|(y,v).
El cruce de t bloques de N valores cuesta 4·t·log2(N) bits. rho = costo de la peor pieza / ese valor.

A. Tetraedro como alfabeto de bloque.
   Los signos sigma de la identidad de ocho cuadrados (tabla de los octoniones sobre F2^3)
   restringidos a un subgrupo de orden 4 dan una identidad de cuatro cuadrados (cuaterniones).
   Se prueban los 7 subgrupos de orden 4 del cubo: 3 caras, 3 rectángulos diagonales y el tetraedro.

B. Tetraedro como geometría de los dos cortes (estados de Bell, dos bits).
   En el cubo de correlaciones (<XX>, <YY>, <ZZ>) los cuatro estados de Bell ocupan un tetraedro
   regular (producto -1), el centro es la identidad, y los cuatro cruces I - 2·Pi_v ocupan el
   tetraedro opuesto. Se miden rangos por corte y las piezas D1 para cada elección de vértice.

Uso: python3 experimento_tetraedro.py [salida.json]
"""

import itertools as it
import json
import sys
from math import comb, log2

import numpy as np


# ---------------------------------------------------------------- utilidades comunes

def matrices(f, N):
    filas = np.zeros((N * N, N * N))
    cols = np.zeros((N * N, N * N))
    for x, y, u, v in it.product(range(N), repeat=4):
        val = f(x, y, u, v)
        filas[x * N + y, u * N + v] = val
        cols[x * N + u, y * N + v] = val
    return filas, cols


def de_operador(O):
    """Matriz por filas (operador de dos qubits) -> matriz por columnas (reacomodo parcial)."""
    cols = np.zeros((4, 4))
    for x, y, u, v in it.product(range(2), repeat=4):
        cols[x * 2 + u, y * 2 + v] = O[x * 2 + y, u * 2 + v]
    return cols


def kron_lista(ms):
    out = np.ones((1, 1))
    for m in ms:
        out = np.kron(out, m)
    return out


def pieza(R, C, t, i):
    acc = None
    for Q in it.combinations(range(t), i):
        term = kron_lista([C if s in Q else R for s in range(t)])
        acc = term if acc is None else acc + term
    return acc


def rango(m):
    return int(np.linalg.matrix_rank(m))


def bits(r):
    return log2(r) if r > 0 else 0.0


def peor_pieza(Rf, Rc, Cf, Cc, t, b):
    rf = [rango(pieza(Rf, Cf, t, i)) for i in range(t + 1)]
    rc = [rango(pieza(Rc, Cc, t, i)) for i in range(t + 1)]
    costo = [bits(a) + bits(c) for a, c in zip(rf, rc)]
    i = max(range(t + 1), key=lambda k: costo[k])
    return rf, rc, round(costo[i] / (4 * t * b), 4)


def rho_hurwitz(N, t):
    """Fórmula del Apéndice H (N = 4, 8): filas(i) = sum_{z<=i} C(t,z)(N^2-N)^z N^(t-z), columnas(i) = filas(t-i)."""
    pref, acc = [], 0
    for z in range(t + 1):
        acc += comb(t, z) * (N * N - N) ** z * N ** (t - z)
        pref.append(acc)
    lb = [bits(p) for p in pref]
    c = max(lb[i] + lb[t - i] for i in range(t + 1))
    return round(c / (4 * t * log2(N)), 4)


# ---------------------------------------------------------------- A. alfabeto de bloque

def sigma(p, q):
    a = [(p >> 2) & 1, (p >> 1) & 1, p & 1]
    b = [(q >> 2) & 1, (q >> 1) & 1, q & 1]
    phi = sum(a[i] * b[j] for i in range(3) for j in range(i, 3))
    phi += b[0] * a[1] * a[2] + a[0] * b[1] * a[2] + a[0] * a[1] * b[2]
    return -1 if phi % 2 else 1


def palabra(p):
    return format(p, "03b")


def subgrupos_orden_4():
    out = []
    for f in range(1, 8):  # núcleo del funcional lineal p -> <f,p> mod 2
        H = [p for p in range(8) if bin(p & f).count("1") % 2 == 0]
        peso = bin(f).count("1")
        tipo = {1: "cara", 2: "rectángulo diagonal", 3: "tetraedro (clase par)"}[peso]
        out.append((tipo, H))
    return out


def experimento_A(t_max=2):
    resultados = []
    for tipo, H in subgrupos_orden_4():
        idx = {p: k for k, p in enumerate(H)}

        def psi(k, p, q):
            return sigma(p, q) if (p ^ q) == k else 0

        def R(x, y, u, v):
            X, Y, U, V = H[x], H[y], H[u], H[v]
            return sum(psi(k, X, Y) * psi(k, V, U) for k in H)

        def C(x, y, u, v):
            X, Y, U, V = H[x], H[y], H[u], H[v]
            return sum(psi(k, X, U) * psi(k, V, Y) for k in H)

        identidad = all(R(*w) + C(*w) == 2 * float(w[0] == w[3] and w[1] == w[2])
                        for w in it.product(range(4), repeat=4))
        no_nulos = [p for p in H if p != 0]
        cuaterniones = (all(sigma(p, p) == -1 for p in no_nulos)
                        and all(sigma(p, q) == -sigma(q, p) for p in no_nulos for q in no_nulos if p != q))
        Rf, Rc = matrices(R, 4)
        Cf, Cc = matrices(C, 4)
        por_t = []
        for t in range(1, t_max + 1):
            rf, rc, rho = peor_pieza(Rf, Rc, Cf, Cc, t, 2)
            formula = ([sum(comb(t, z) * 12 ** z * 4 ** (t - z) for z in range(i + 1)) for i in range(t + 1)])
            por_t.append({"t": t, "rangos_filas": rf, "rangos_columnas": rc, "rho": rho,
                          "formula_apendice_H_coincide": rf == formula and rc == formula[::-1]})
        resultados.append({
            "tipo": tipo,
            "vertices": [palabra(p) for p in H],
            "R_mas_C_igual_2_cruce": identidad,
            "signos_de_cuaterniones_Q8": cuaterniones,
            "por_t": por_t,
        })
    return resultados


# ---------------------------------------------------------------- B. geometría de los dos cortes

def experimento_B(t_max=4):
    s2 = 1 / np.sqrt(2)
    bell = {
        "Phi+": np.array([1, 0, 0, 1]) * s2,
        "Phi-": np.array([1, 0, 0, -1]) * s2,
        "Psi+": np.array([0, 1, 1, 0]) * s2,
        "Psi- (singlete)": np.array([0, 1, -1, 0]) * s2,
    }
    I2 = np.eye(2)
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.diag([1, -1])
    paulis = [np.kron(P, P) for P in (X, Y, Z)]
    SWAP, _ = matrices(lambda x, y, u, v: float(x == v and y == u), 2)
    I4 = np.eye(4)
    locales = {"I": I2, "X": X, "Z": Z, "XZ": X @ Z}

    def corr(O):
        tr = np.trace(O).real
        return [int(round(np.trace(O @ P).real / tr)) for P in paulis]

    def a_palabra(c):
        return "".join("0" if ci == 1 else "1" for ci in c)

    vertices = {}
    for nombre, b in bell.items():
        Pi = np.outer(b, b)
        M = I4 - 2 * Pi
        local = [k for k, U in locales.items()
                 if np.allclose(M, np.kron(I2, U) @ SWAP @ np.kron(I2, U).T)]
        Rf, Rc = -2 * Pi, de_operador(-2 * Pi)
        Cf, Cc = I4, de_operador(I4)
        rhos = [peor_pieza(Rf, Rc, Cf, Cc, t, 1)[2] for t in range(1, t_max + 1)]
        c_pi, c_m = corr(Pi), corr(M)
        vertices[nombre] = {
            "correlacion_estado": c_pi,
            "producto_estado": int(np.prod(c_pi)),
            "rangos_estado_filas_columnas": [rango(Pi), rango(de_operador(Pi))],
            "cruce_I_menos_2Pi": {
                "correlacion": c_m,
                "es_reflejo_central_del_estado": c_m == [-c for c in c_pi],
                "palabra_en_el_cubo": a_palabra(c_m),
                "rangos_filas_columnas": [rango(M), rango(de_operador(M))],
                "igual_a_SWAP_con_local": local,
            },
            "rho_D1_por_t": rhos,
        }
    centro = {"rangos_identidad_filas_columnas": [rango(I4), rango(de_operador(I4))],
              "suma_de_los_cuatro_estados_es_I": bool(np.allclose(
                  sum(np.outer(b, b) for b in bell.values()), I4))}
    pal = sorted(v["cruce_I_menos_2Pi"]["palabra_en_el_cubo"] for v in vertices.values())
    pts = [np.array(v["correlacion_estado"]) for v in vertices.values()]
    dist = sorted({round(float(np.linalg.norm(a - b)), 6) for a, b in it.combinations(pts, 2)})
    return {
        "vertices": vertices,
        "centro": centro,
        "estados_forman_tetraedro_regular_distancias": dist,
        "cruces_ocupan_la_clase_par": pal == ["000", "011", "101", "110"],
        "palabras_de_los_cruces": pal,
    }


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "resultados_tetraedro.json"
    res = {
        "referencia": "Claude (Anthropic), A 2^{o(n)} Time Algorithm for 3-SAT, 26-10-2026, §4 y Apéndice H",
        "A_tetraedro_como_alfabeto": experimento_A(),
        "A_rho_asintotico_por_formula": {
            "N4_cuaterniones_t10000": rho_hurwitz(4, 10000),
            "N8_octoniones_t10000": rho_hurwitz(8, 10000),
            "conteo_simple_Lema_2": {"N4": "2+4+1+1 = 8 de 8 bits (sin ganancia)",
                                     "N8": "3+6+1+1 = 11 de 12 bits (rho = 11/12)"},
        },
        "B_tetraedro_de_los_dos_cortes": experimento_B(),
        "B_rho_asintotico_D1": round(log2(12) / 4, 4),
    }
    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # consolas Windows con cp1252
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
