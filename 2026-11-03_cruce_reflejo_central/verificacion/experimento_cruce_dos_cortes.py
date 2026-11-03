#!/usr/bin/env python3
"""
Experimento: costo por corte de las piezas que descomponen el cruce [x=v][y=u].

Referencia: Claude (Anthropic), "A 2^{o(n)} Time Algorithm for 3-SAT", 26-10-2026,
§4 (Definición 5, Lema 2) y Apéndice H.

El cruce, como función de cadenas x, y, u, v de t bits, tiene rango completo 4^t en los dos
cortes:
    corte por filas     (x,y) | (u,v)
    corte por columnas  (x,u) | (y,v)
Cuesta, por tanto, 2t + 2t = 4t bits. El algoritmo escribe el cruce como suma de piezas
A_0, ..., A_t (coeficientes de T^i en  prod_s (R_s + T*C_s), Definición 5) y gana si la
peor pieza cuesta rho * 4t bits con rho < 1.

Aquí el costo de una pieza se mide por rangos: log2(rango por filas) + log2(rango por columnas).
El rango es una cota inferior de los bits de cualquier factorización; convertirlo en algoritmo
exige factorizaciones explícitas y eficientes (el Lema 2 usa un conteo más simple).

Se comparan dos descomposiciones del cruce de un bit:

  D1, dos cortes:      cruce = C + R
                       C = [x=u][y=v]                       (rango 1 por columnas)
                       R = -[x!=y](-1)^x [u!=v](-1)^u       (rango 1 por filas)
                       Es SWAP = I - 2P_-  (Apéndice H del paper).

  D2, signo propio:    cruce = P_+ - P_-  (partes simétrica y antisimétrica de SWAP).

Control: bloque de 3 bits con la identidad de ocho cuadrados (ecs. 27-31 del paper):
R + C = 2*cruce, y R tiene rangos 8 (filas) y 64 (columnas).

Uso: python3 experimento_cruce_dos_cortes.py [salida.json]
"""

import itertools as it
import json
import sys
from math import comb, log2

import numpy as np


# ---------------------------------------------------------------- utilidades

def matrices(f, N):
    """Matrices de f(x,y,u,v) en los dos cortes, para un bloque de N valores."""
    filas = np.zeros((N * N, N * N))
    cols = np.zeros((N * N, N * N))
    for x, y, u, v in it.product(range(N), repeat=4):
        val = f(x, y, u, v)
        filas[x * N + y, u * N + v] = val
        cols[x * N + u, y * N + v] = val
    return filas, cols


def kron_lista(ms):
    out = np.ones((1, 1))
    for m in ms:
        out = np.kron(out, m)
    return out


def pieza(R, C, t, i):
    """A_i = suma sobre Q de tamaño i del producto que toma C en Q y R fuera de Q.

    El producto de Kronecker por bloques da filas y columnas intercaladas, que son una
    permutación del corte (x,y)|(u,v) o (x,u)|(y,v); el rango no cambia.
    """
    acc = None
    for Q in it.combinations(range(t), i):
        term = kron_lista([C if s in Q else R for s in range(t)])
        acc = term if acc is None else acc + term
    return acc


def rango(m):
    return int(np.linalg.matrix_rank(m))


def bits(r):
    return log2(r) if r > 0 else 0.0


# ---------------------------------------------------------------- funciones de un bit

def cruce(x, y, u, v):
    return float((x == v) and (y == u))


def C1(x, y, u, v):
    return float((x == u) and (y == v))


def R1(x, y, u, v):
    return -float((x != y) * (-1) ** x * (u != v) * (-1) ** u)


def P_menos(x, y, u, v):
    return (C1(x, y, u, v) - cruce(x, y, u, v)) / 2


def P_mas(x, y, u, v):
    return (C1(x, y, u, v) + cruce(x, y, u, v)) / 2


DESCOMPOSICIONES = {
    "D1_dos_cortes": {
        "descripcion": "cruce = C + R con C=[x=u][y=v], R=-[x!=y](-1)^x[u!=v](-1)^u  (SWAP = I - 2P_-)",
        "R": R1,
        "C": C1,
    },
    "D2_signo_propio": {
        "descripcion": "cruce = P_+ - P_-  (partes simétrica y antisimétrica de SWAP)",
        "R": P_mas,
        "C": lambda *a: -P_menos(*a),
    },
}


# Fórmulas cerradas para D1 (autovalores comunes de SWAP y P_-: dimensiones 3 y 1).
def d1_filas(t, i):
    return sum(comb(t, z) * 3 ** (t - z) for z in range(t - i, t + 1))


def d1_cols(t, i):
    return sum(comb(t, z) * 3 ** (t - z) for z in range(i, t + 1))


def d2_filas(t, i):
    return comb(t, i) * 3 ** (t - i)


# ---------------------------------------------------------------- control de ocho cuadrados

def control_ocho_cuadrados():
    def bitsde(p, orden):
        b = [(p >> 2) & 1, (p >> 1) & 1, p & 1]
        return b if orden == 0 else b[::-1]

    for orden in (0, 1):
        def sigma(p, q):
            a, b = bitsde(p, orden), bitsde(q, orden)
            phi = sum(a[i] * b[j] for i in range(3) for j in range(i, 3))
            phi += b[0] * a[1] * a[2] + a[0] * b[1] * a[2] + a[0] * a[1] * b[2]
            return -1 if phi % 2 else 1

        def psi(k, p, q):
            return sigma(p, q) if (p ^ q) == k else 0

        def R8(x, y, u, v):
            return sum(psi(k, x, y) * psi(k, v, u) for k in range(8))

        def C8(x, y, u, v):
            return sum(psi(k, x, u) * psi(k, v, y) for k in range(8))

        ok = all(R8(x, y, u, v) + C8(x, y, u, v) == 2 * cruce(x, y, u, v)
                 for x, y, u, v in it.product(range(8), repeat=4))
        if ok:
            Rf, Rc = matrices(R8, 8)
            Cf, Cc = matrices(C8, 8)
            return {
                "identidad_R_mas_C_igual_2_cruce": True,
                "orden_de_bits": "p1 = bit más significativo" if orden == 0 else "p1 = bit menos significativo",
                "R_rangos_filas_columnas": [rango(Rf), rango(Rc)],
                "C_rangos_filas_columnas": [rango(Cf), rango(Cc)],
                "esperado_por_el_paper": "R: 8 por filas y 64 por columnas (Apéndice H)",
            }
    return {"identidad_R_mas_C_igual_2_cruce": False}


# ---------------------------------------------------------------- experimento

def medir(nombre, d, t_max, t_extra):
    Rf, Rc = matrices(d["R"], 2)
    Cf, Cc = matrices(d["C"], 2)
    cruce_f, cruce_c = matrices(cruce, 2)
    filas_out = []
    for t in range(1, t_max + 1):
        piezas_f = [pieza(Rf, Cf, t, i) for i in range(t + 1)]
        piezas_c = [pieza(Rc, Cc, t, i) for i in range(t + 1)]
        exacta = (np.allclose(sum(piezas_f), kron_lista([cruce_f] * t))
                  and np.allclose(sum(piezas_c), kron_lista([cruce_c] * t)))
        rf = [rango(m) for m in piezas_f]
        rc = [rango(m) for m in piezas_c]
        costo = [bits(a) + bits(b) for a, b in zip(rf, rc)]
        peor = max(range(t + 1), key=lambda i: costo[i])
        fila = {
            "t": t,
            "suma_de_piezas_igual_al_cruce": bool(exacta),
            "rangos_filas": rf,
            "rangos_columnas": rc,
            "peor_pieza_i": peor,
            "bits_por_bloque_peor_pieza": round(costo[peor] / t, 4),
            "rho": round(costo[peor] / (4 * t), 4),
        }
        if nombre == "D1_dos_cortes":
            fila["formula_cerrada_coincide"] = (rf == [d1_filas(t, i) for i in range(t + 1)]
                                                and rc == [d1_cols(t, i) for i in range(t + 1)])
        else:
            fila["formula_filas_coincide"] = rf == [d2_filas(t, i) for i in range(t + 1)]
        filas_out.append(fila)
    extra = []
    for t, idx in t_extra:
        for i in idx:
            a = rango(pieza(Rf, Cf, t, i))
            b = rango(pieza(Rc, Cc, t, i))
            extra.append({"t": t, "i": i, "rango_filas": a, "rango_columnas": b,
                          "bits_por_bloque": round((bits(a) + bits(b)) / t, 4)})
    return {"descripcion": d["descripcion"], "por_t": filas_out, "t_adicional": extra}


def asintotico_d1(ts):
    out = []
    for t in ts:
        # cola[z] = sum_{w >= z} C(t,w) 3^(t-w); filas(i) = cola[t-i], columnas(i) = cola[i]
        cola = [0] * (t + 2)
        for z in range(t, -1, -1):
            cola[z] = cola[z + 1] + comb(t, z) * 3 ** (t - z)
        lb = [bits(c) for c in cola[: t + 1]]
        mejor = max(range(t + 1), key=lambda i: lb[t - i] + lb[i])
        c = lb[t - mejor] + lb[mejor]
        out.append({"t": t, "peor_pieza_i": mejor, "bits_por_bloque": round(c / t, 4),
                    "rho": round(c / (4 * t), 4)})
    return out


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "resultados_cruce_dos_cortes.json"
    res = {
        "referencia": "Claude (Anthropic), A 2^{o(n)} Time Algorithm for 3-SAT, 26-10-2026, §4 y Apéndice H",
        "costo_del_cruce_bits_por_bloque": 4,
        "medida": "log2(rango por filas) + log2(rango por columnas) de la peor pieza, por bloque",
        "control_ocho_cuadrados": control_ocho_cuadrados(),
        "D1_dos_cortes": medir("D1_dos_cortes", DESCOMPOSICIONES["D1_dos_cortes"], 5, []),
        "D2_signo_propio": medir("D2_signo_propio", DESCOMPOSICIONES["D2_signo_propio"], 5, []),
        "D1_asintotico_por_formula": asintotico_d1([10, 100, 1000, 10000]),
        "limite_D1": {"bits_por_bloque": round(log2(12), 4), "rho": round(log2(12) / 4, 4),
                      "nota": "log2(12) = 2 + log2(3); el paper reporta ~3.58 de 4 bits (Apéndice H)"},
    }
    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # consolas Windows con cp1252
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
