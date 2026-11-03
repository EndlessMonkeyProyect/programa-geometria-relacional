#!/usr/bin/env python3
"""El tetraedro desde el origen en los bits, y su crecimiento como cristal.

Comprueba con enteros exactos:
  T1. Desde el origen 000, cambiar bits de a pares da exactamente el tetraedro par
      {000, 011, 101, 110}: cuatro palabras a distancia 2 entre sí, producto de signos +1.
      Cambiar un solo bit lleva al tetraedro impar. Cuatro es el máximo de palabras
      equidistantes en 3 bits.
  T2. Los cruces: SWAP está en el origen (correlaciones +1, +1, +1); un Pauli local
      cambia dos signos, así que los otros tres cruces son el origen con dos bits cambiados.
  T3. Construcción A: los enteros cuya reducción módulo 2 es par forman D3 (cúbica de
      caras centradas). El diamante es D3 más su copia corrida en (1/2, 1/2, 1/2): desde un
      átomo de D3 los vecinos más cercanos apuntan al tetraedro par; desde la copia, al impar.
  T4. La copia corrida D_n + (1/2,...,1/2) cierra en una red solo si n es par, y queda a la
      misma distancia que los vecinos de D_n solo si n = 8. En n = 8 la red es E8:
      240 vectores mínimos, normas pares.
Uso: python3 verificar_origen_tetraedro.py [salida.json]
"""
import itertools as it
import json
import sys
from fractions import Fraction as Fr

import numpy as np


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def signos(w):  # bit 0 -> +1, bit 1 -> -1
    return tuple(1 - 2 * b for b in w)


def t1():
    origen = (0, 0, 0)
    pares = {tuple(b ^ f for b, f in zip(origen, flip))
             for flip in it.product((0, 1), repeat=3) if sum(flip) % 2 == 0}
    impares = {tuple(b ^ f for b, f in zip(origen, flip))
               for flip in it.product((0, 1), repeat=3) if sum(flip) % 2 == 1}
    dist = sorted({hamming(a, b) for a, b in it.combinations(sorted(pares), 2)})
    prod = sorted({int(np.prod(signos(w))) for w in pares})
    d2 = sorted({sum((x - y) ** 2 for x, y in zip(signos(a), signos(b)))
                 for a, b in it.combinations(sorted(pares), 2)})
    cubo = list(it.product((0, 1), repeat=3))
    maximo = max(len(S) for r in range(1, 9) for S in it.combinations(cubo, r)
                 if len({hamming(a, b) for a, b in it.combinations(S, 2)}) <= 1)
    return {
        "tetraedro_par_desde_origen": ["".join(map(str, w)) for w in sorted(pares)],
        "tetraedro_impar_un_bit": ["".join(map(str, w)) for w in sorted(impares)],
        "distancias_hamming_entre_vertices": dist,
        "distancia_euclidea_al_cuadrado": d2,
        "producto_de_signos": prod,
        "es_subgrupo_xor": all(tuple(x ^ y for x, y in zip(a, b)) in pares for a in pares for b in pares),
        "maximo_de_palabras_equidistantes_en_3_bits": maximo,
    }


def t2():
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.diag([1, -1]).astype(complex)
    SWAP = np.eye(4)[[0, 2, 1, 3]].astype(complex)

    def correl(M):
        return tuple(int(round(np.trace(M @ np.kron(P, P)).real / 2)) for P in (X, Y, Z))

    def palabra(c):
        return "".join("0" if v == 1 else "1" for v in c)

    out = {"SWAP": palabra(correl(SWAP))}
    for nombre, P in (("X", X), ("Y", Y), ("Z", Z)):  # corregir por un Pauli local: conjugar
        U = np.kron(P, I)
        out[f"({nombre}⊗I)·SWAP·({nombre}⊗I)"] = palabra(correl(U @ SWAP @ U.conj().T))
    return out


def en_D(x):  # x entero, suma par
    return all(v.denominator == 1 for v in x) and sum(x) % 2 == 0


def t3():
    rango = range(-2, 3)
    d3 = [x for x in it.product(rango, repeat=3) if sum(x) % 2 == 0]
    reduccion = sorted({tuple(v % 2 for v in x) for x in d3})
    h = (Fr(1, 2),) * 3
    copia = [tuple(Fr(v) + hv for v, hv in zip(x, h)) for x in d3]

    def vecinos(p, otros):
        d = [(sum((a - b) ** 2 for a, b in zip(p, q)), q) for q in otros if q != p]
        m = min(dd for dd, _ in d)
        return m, [tuple(b - a for a, b in zip(p, q)) for dd, q in d if dd == m]

    m1, v1 = vecinos((Fr(0),) * 3, copia)
    m2, v2 = vecinos(h, [tuple(map(Fr, x)) for x in d3])
    sig = lambda v: int(np.sign(float(v[0] * v[1] * v[2])))
    return {
        "D3_modulo_2": ["".join(map(str, w)) for w in reduccion],
        "vecinos_desde_D3": {"distancia2": str(m1), "cantidad": len(v1),
                             "producto_de_signos": sorted({sig(v) for v in v1})},
        "vecinos_desde_la_copia": {"distancia2": str(m2), "cantidad": len(v2),
                                   "producto_de_signos": sorted({sig(v) for v in v2})},
        "vecino_mas_cercano_dentro_de_D3_distancia2": 2,
    }


def t4():
    filas = []
    for n in range(2, 11):
        dos_h = (1,) * n  # h + h
        cierra = sum(dos_h) % 2 == 0  # D_n + h es red si 2h está en D_n
        norma_h = Fr(n, 4)
        filas.append({"n": n, "es_red": cierra, "norma_de_h": str(norma_h),
                      "norma_minima_de_Dn": 2, "misma_distancia": norma_h == 2})
    # E8 = D8 ∪ (D8 + h): vectores de norma 2
    raices_d8 = sum(1 for x in it.product((-1, 0, 1), repeat=8)
                    if sum(abs(v) for v in x) == 2)
    raices_mitad = sum(1 for s in it.product((1, -1), repeat=8)
                       if sum(s) % 4 == 0)  # sum(s/2) par  <=>  sum(s) ≡ 0 mod 4
    # normas pares en una muestra de sumas
    rng = np.random.default_rng(0)
    gen = [np.array(x, dtype=float) for x in it.product((-1, 0, 1), repeat=8)
           if sum(abs(v) for v in x) == 2][:60] + [np.full(8, 0.5)]
    pares = all(abs(np.dot(v, v) - 2 * round(np.dot(v, v) / 2)) < 1e-12
                for v in (gen[i] + gen[j] for i in range(len(gen)) for j in range(len(gen))))
    return {"tabla": filas, "E8_raices_de_D8": raices_d8, "E8_raices_semienteras": raices_mitad,
            "E8_total_vectores_minimos": raices_d8 + raices_mitad, "E8_normas_pares_en_muestra": pares}


def main():
    res = {"T1": t1(), "T2": t2(), "T3": t3(), "T4": t4()}
    salida = sys.argv[1] if len(sys.argv) > 1 else "resultados_origen_tetraedro.json"
    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
