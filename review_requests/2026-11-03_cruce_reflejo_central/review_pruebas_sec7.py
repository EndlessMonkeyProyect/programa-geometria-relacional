#!/usr/bin/env python3
"""Verificación independiente de las pruebas de la §7 del paper.

Reimplementa Cayley–Dickson y comprueba, paso a paso y con enteros exactos,
las afirmaciones de las Proposiciones 1–3 y el Corolario 4, más el conteo
«168 de 210» del nodo abierto. No depende de los verificadores del paquete.
"""
import itertools as it

import numpy as np


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


def check(N):
    tabla = {}
    for p in range(N):
        for q in range(N):
            r = mul(unidad(p, N), unidad(q, N))
            nz = [k for k, v in enumerate(r) if v]
            assert nz == [p ^ q], (N, p, q, nz, r)
            tabla[(p, q)] = r[p ^ q]

    def psi(k, p, q):
        return tabla[(p, q)] if (p ^ q) == k else 0

    def R(x, y, u, v):
        return sum(psi(k, x, y) * psi(k, v, u) for k in range(N))

    def C(x, y, u, v):
        return sum(psi(k, x, u) * psi(k, v, y) for k in range(N))

    # --- Proposición 1: R + C = 2·[x=v][y=u] ---
    prop1 = all(R(x, y, u, v) + C(x, y, u, v) == 2 * int(x == v and y == u)
                for x, y, u, v in it.product(range(N), repeat=4))

    # identidad (28): sigma(p,q)sigma(p',q') + sigma(p,q')sigma(p',q) = 0
    viol28 = sum(1 for p, q, pp, qq in it.product(range(N), repeat=4)
                 if (p ^ q) == (pp ^ qq) and q != qq
                 and tabla[(p, q)] * tabla[(pp, qq)] + tabla[(p, qq)] * tabla[(pp, q)] != 0)

    # --- Matrices en los dos cortes ---
    # Rf: corte por filas   (filas (x,y), columnas (u,v))
    # Rc: corte por columnas (filas (x,u), columnas (y,v))
    # Rt: matricización del paper en Prop. 3 (filas (x,y), columnas (v,u))
    Rf = np.zeros((N * N, N * N))
    Rc = np.zeros((N * N, N * N))
    Rt = np.zeros((N * N, N * N))
    Ct = np.zeros((N * N, N * N))
    Cf = np.zeros((N * N, N * N))
    for x, y, u, v in it.product(range(N), repeat=4):
        Rf[x * N + y, u * N + v] = R(x, y, u, v)
        Rc[x * N + u, y * N + v] = R(x, y, u, v)
        Rt[x * N + y, v * N + u] = R(x, y, u, v)
        Ct[x * N + y, v * N + u] = C(x, y, u, v)
        Cf[x * N + y, u * N + v] = C(x, y, u, v)

    rRf = int(np.linalg.matrix_rank(Rf))
    rRc = int(np.linalg.matrix_rank(Rc))
    rCf = int(np.linalg.matrix_rank(Cf))

    # --- Paso delicado: ¿R por columnas == C por filas, entrada a entrada? ---
    Rc_eq_Cf = np.array_equal(Rc, Cf)

    # --- Proposición 3, en la matricización del paper (columnas (v,u)): ---
    #   R = ΦᵀΦ  con  ΦΦᵀ = N·Id  ⇒  R² = N·R ;  cruce = Id ⇒ C = 2·Id − R
    R2_NR = np.array_equal(Rt @ Rt, N * Rt)
    C_2I_R = np.array_equal(Ct, 2 * np.eye(N * N) - Rt)
    cruce_es_Id = np.array_equal(Rt + Ct, 2 * np.eye(N * N))

    # --- Proposición 2: L_v^T L_x + L_x^T L_v = 2[x=v]·Id ---
    L = {x: np.array([[psi(k, x, y) for y in range(N)] for k in range(N)])
         for x in range(N)}
    hurwitz_radon = all(
        np.array_equal(L[v].T @ L[x] + L[x].T @ L[v], 2 * int(x == v) * np.eye(N, dtype=int))
        for x in range(N) for v in range(N))

    # --- Corolario 4: asociatividad ---
    asociativa = all(
        mul(mul(unidad(a, N), unidad(b, N)), unidad(c, N))
        == mul(unidad(a, N), mul(unidad(b, N), unidad(c, N)))
        for a, b, c in it.product(range(N), repeat=3))

    print(f"N={N}:")
    print(f"  P1 (R+C=2·cruce)            = {prop1}")
    print(f"  identidad (28), violaciones  = {viol28}")
    print(f"  P2 (Hurwitz–Radon)          = {hurwitz_radon}")
    print(f"  P3: R_cols == C_filas       = {Rc_eq_Cf}  (paso delicado)")
    print(f"  P3: R^2 == N·R [matriz (v,u)] = {R2_NR}")
    print(f"  P3: C == 2·Id − R           = {C_2I_R}")
    print(f"  P3: cruce == Id [matriz (v,u)] = {cruce_es_Id}")
    print(f"  rangos: filas={rRf}, columnas={rRc}, C_filas={rCf}"
          f"  (esperado R_filas={N}, R_cols={N * N if N != 2 else 2})")
    print(f"  C4 asociativa               = {asociativa}")
    return {
        "prop1": prop1, "viol28": viol28, "hurwitz_radon": hurwitz_radon,
        "Rc_eq_Cf": Rc_eq_Cf, "R2_NR": R2_NR, "C_2I_R": C_2I_R,
        "cruce_es_Id": cruce_es_Id,
        "rRf": rRf, "rRc": rRc, "rCf": rCf, "asociativa": asociativa,
    }


def contar_no_asociativos(N):
    """Cuenta tríos (a,b,c) de unidades NO nulas y distintas, no asociativos."""
    base = list(range(1, N))  # excluye la identidad (0)
    tabla = {}
    for p in range(N):
        for q in range(N):
            r = mul(unidad(p, N), unidad(q, N))
            tabla[(p, q)] = r[p ^ q]
    no_asoc = 0
    total = 0
    for a, b, c in it.permutations(base, 3):
        total += 1
        # (e_a e_b) e_c  vs  e_a (e_b e_c): comparamos el destino y el signo
        ab = mul(unidad(a, N), unidad(b, N))
        bc = mul(unidad(b, N), unidad(c, N))
        izq = mul(ab, unidad(c, N))
        der = mul(unidad(a, N), bc)
        if izq != der:
            no_asoc += 1
    return total, no_asoc


if __name__ == "__main__":
    ok = True
    for N in (2, 4, 8):
        r = check(N)
        esperado_cols = N * N if N != 2 else 2
        ok &= (r["prop1"] and r["Rc_eq_Cf"] and r["R2_NR"] and r["C_2I_R"]
               and r["cruce_es_Id"]
               and r["rRf"] == N and r["rRc"] == esperado_cols
               and r["rCf"] == esperado_cols
               and r["hurwitz_radon"])
    # N = 16: identidad (28) debe fallar (672) y ser no asociativo
    r16 = check(16)
    print(f"N=16: violaciones (28) = {r16['viol28']}  (esperado 672), "
          f"asociativa = {r16['asociativa']} (esperado False)")
    ok &= (r16["viol28"] == 672 and not r16["asociativa"])

    total, no_asoc = contar_no_asociativos(8)
    print(f"Octoniones (N=8): {no_asoc} de {total} tríos de unidades distintas "
          f"no asociativos  (la nota reporta 168 de 210)")
    ok &= (no_asoc == 168 and total == 210)

    print("\nRESULTADO GLOBAL:", "TODAS LAS AFIRMACIONES VERIFICADAS" if ok else "HAY DISCREPANCIAS")
