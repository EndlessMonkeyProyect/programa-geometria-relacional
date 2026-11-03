#!/usr/bin/env python3
"""
Verificador: particiones, autorreferencia y la concavidad del Apéndice B.

Comprueba las afirmaciones de la pestaña «Conversación 3-nov» del documento
«El cruce como reflejo central» (Programa de Geometría Relacional, 3-11-2026).

  V1  p(E), número de maneras de llenar la totalidad E con partes enteras, y su
      crecimiento (Hardy–Ramanujan): log p(E) ≈ π·sqrt(2E/3) − log(4E·sqrt 3).
  V2  Log-concavidad: p(E)^2 > p(E−1)·p(E+1) para todo E > 25 (DeSalvo–Pak, 2015);
      se listan las excepciones con E ≤ 25.
  V3  Autorreferencia: el número de particiones iguales a su propio reflejo
      (autoconjugadas, diagrama de Young simétrico en la diagonal) es igual al número
      de particiones en partes impares distintas.
  V4  Operadores del Apéndice B sobre V = Q[t1, t2, ...] con peso de t_k igual a k:
      subir  ∇_{−l} f = t_l · f        (agrega una parte l),
      bajar  ∇_k f    = k · ∂f/∂t_k     (quita una parte k).
      Se verifica dim V_E = p(E) y la relación [∇_k, ∇_{−l}] = k·[k = l]·Id.
  V5  Familias de partes admisibles: conteo c(E), exponente α de log c(E) ~ E^α y
      el ρ = 2^(α−1) que daría el cálculo del Apéndice B si existiera una estructura
      de operadores con las propiedades de sus Lemas 9 y 10 (eso NO se verifica aquí).

Uso: python3 verificar_particiones.py [salida.json]
"""

import json
import sys
from math import log, log2, pi, sqrt

EMAX = 2000


# ---------------------------------------------------------------- conteos

def conteo(partes, emax=EMAX, distintas=False):
    """Número de particiones de E en partes del conjunto dado (con o sin repetición)."""
    c = [0] * (emax + 1)
    c[0] = 1
    for k in partes:
        if k > emax:
            break
        if distintas:
            for e in range(emax, k - 1, -1):
                c[e] += c[e - k]
        else:
            for e in range(k, emax + 1):
                c[e] += c[e - k]
    return c


def primos(n):
    criba = [True] * (n + 1)
    criba[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if criba[i]:
            criba[i * i::i] = [False] * len(criba[i * i::i])
    return [i for i, b in enumerate(criba) if b]


# ---------------------------------------------------------------- V3: autoconjugadas

def particiones(n, maximo=None):
    if maximo is None:
        maximo = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maximo), 0, -1):
        for resto in particiones(n - k, k):
            yield (k,) + resto


def conjugada(mu):
    return tuple(sum(1 for m in mu if m > i) for i in range(mu[0])) if mu else ()


# ---------------------------------------------------------------- V4: operadores

def subir(f, l):
    out = {}
    for mono, c in f.items():
        m = list(mono)
        m[l - 1] += 1
        out[tuple(m)] = out.get(tuple(m), 0) + c
    return out


def bajar(f, k):
    out = {}
    for mono, c in f.items():
        if mono[k - 1] > 0:
            m = list(mono)
            coef = k * m[k - 1]
            m[k - 1] -= 1
            out[tuple(m)] = out.get(tuple(m), 0) + c * coef
    return out


def resta(f, g):
    out = dict(f)
    for m, c in g.items():
        out[m] = out.get(m, 0) - c
    return {m: c for m, c in out.items() if c}


def monomios(W):
    """Monomios t^mu con peso ≤ W, como vectores de exponentes de longitud W."""
    res = []
    for E in range(W + 1):
        for mu in particiones(E):
            v = [0] * W
            for parte in mu:
                v[parte - 1] += 1
            res.append((E, tuple(v)))
    return res


# ---------------------------------------------------------------- main

def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "resultados_particiones.json"
    res = {"referencia": "Conversación del 3-11-2026; Claude (Anthropic) 2026, Apéndice B"}

    # V1, V2
    p = conteo(range(1, EMAX + 1))
    hr = {E: round(log(p[E]) / (pi * sqrt(2 * E / 3) - log(4 * E * sqrt(3))), 6) for E in (100, 1000, 2000)}
    fallas = [E for E in range(1, EMAX) if p[E] ** 2 <= p[E - 1] * p[E + 1]]
    res["V1_p"] = {str(E): p[E] for E in (1, 2, 3, 4, 5, 10, 20, 50, 100)}
    res["V1_cociente_Hardy_Ramanujan"] = {str(k): v for k, v in hr.items()}
    res["V2_log_concava_para_todo_E_mayor_que_25_hasta"] = EMAX - 1 if all(E <= 25 for E in fallas) else None
    res["V2_excepciones"] = fallas

    # V3
    NMAX = 40
    impares = conteo(range(1, NMAX + 1, 2), NMAX, distintas=True)
    autoconj = [sum(1 for mu in particiones(n) if conjugada(mu) == mu) for n in range(NMAX + 1)]
    res["V3_autoconjugadas_igual_impares_distintas_hasta"] = NMAX if autoconj == impares else None
    res["V3_valores_n_1_a_20"] = autoconj[1:21]

    # V4
    W = 8
    mons = monomios(W)
    dims = [sum(1 for E, _ in mons if E == e) for e in range(W + 1)]
    ok_dim = dims == [p[e] for e in range(W + 1)]
    ok_rel = True
    for _, m in mons:
        f = {m: 1}
        for k in range(1, W + 1):
            for l in range(1, W + 1):
                if sum((i + 1) * x for i, x in enumerate(m)) + l > W:
                    continue
                conm = resta(bajar(subir(f, l), k), subir(bajar(f, k), l))
                esperado = {m: k} if k == l else {}
                ok_rel &= conm == esperado
    res["V4_dim_V_E_igual_p_E_hasta"] = W if ok_dim else None
    res["V4_relacion_Heisenberg_hasta_peso"] = W if ok_rel else None

    # V5
    pr = primos(EMAX)
    familias = [
        ("todas las partes", range(1, EMAX + 1), False, 0.5, "superpolinómico"),
        ("partes distintas", range(1, EMAX + 1), True, 0.5, "superpolinómico"),
        ("impares distintas (= autoconjugadas)", range(1, EMAX + 1, 2), True, 0.5, "superpolinómico"),
        ("primos", pr, False, 0.5, "superpolinómico (α = 1/2 con factor 1/sqrt(log E))"),
        ("cuadrados 1, 4, 9, 16, ...", [k * k for k in range(1, 50)], False, 1 / 3, "superpolinómico"),
        ("cubos 1, 8, 27, ...", [k ** 3 for k in range(1, 13)], False, 1 / 4, "superpolinómico"),
        ("potencias de 2 (duplicación)", [2 ** k for k in range(11)], False, 0.0, "cuasipolinómico: log c ~ (log E)^2; no alcanza"),
        ("múltiplos que cierran 1 a 5", range(1, 6), False, 0.0, "polinómico (grado 4); no alcanza"),
    ]
    tabla = []
    for nombre, partes, dist, alfa, crec in familias:
        c = conteo(partes, EMAX, distintas=dist)
        f1, f2 = log2(c[EMAX // 2]), log2(c[EMAX])
        tabla.append({
            "familia": nombre,
            "log2_c_E1000": round(f1, 3),
            "log2_c_E2000": round(f2, 3),
            "alfa_estimado_E2000": round(log2(f2 / f1), 3),
            "rho_estimado_E2000": round(f2 / (2 * f1), 3),
            "alfa_asintotico": round(alfa, 4),
            "rho_si_existieran_operadores": round(2 ** (alfa - 1), 4) if 0 < alfa < 1 else None,
            "crecimiento": crec,
        })
    res["V5_familias"] = tabla
    res["V5_nota"] = ("rho = 2^(alfa−1) es el cálculo del Apéndice B (\"if it grew like E^alfa\"). "
                      "Que exista una estructura de operadores con los Lemas 9 y 10 para una familia "
                      "restringida no se verifica aquí: es la pregunta abierta.")

    with open(salida, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # consolas Windows con cp1252
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
