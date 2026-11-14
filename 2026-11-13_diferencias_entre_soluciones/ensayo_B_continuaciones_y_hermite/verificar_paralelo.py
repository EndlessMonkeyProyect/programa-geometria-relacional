#!/usr/bin/env python3
"""Pruebas paralelas: continuaciones y recuperacion por Hermite (13-XI-2026).

Solo biblioteca estandar y aritmetica entera exacta. Uso: python3 verificar_paralelo.py

Ruta 1: agrupacion de prefijos por su funcion de continuacion en F=(x|z)&(y|z).
Ruta 2: H_F(T,u) = sum_{x|=F} (1+u)^{w(x)} prod_{i<=min(3,n)} (1+T x_i)  (mod u^3),
        valores y primeras derivadas en T=1,2 por eliminacion de variables con pares
        (H, dH/dT); recuperacion de H(0,u)=J_F(u) por la identidad de Hermite cubica.
La enumeracion de asignaciones solo audita los resultados.
Genera resultados_paralelos.json junto al script.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

ZERO = (0, 0, 0)
ONE = (1, 0, 0)


class Ops:
    """Cuenta sumas y productos enteros: suma de ternas = 3 sumas;
    producto truncado mod u^3 = 6 productos + 3 sumas."""

    def __init__(self):
        self.adds = 0
        self.mults = 0

    def add(self, a, b):
        self.adds += 3
        return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    def mul(self, a, b):
        self.mults += 6
        self.adds += 3
        return (a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[0] * b[2] + a[1] * b[1] + a[2] * b[0])

    @property
    def total(self):
        return self.adds + self.mults


def jet_pow(w):  # (1+u)^w mod u^3
    return (1, w, w * (w - 1) // 2)


def moments(j):  # (N, S, Q) desde N + S u + B u^2, con Q = S + 2B
    return (j[0], j[1], j[1] + 2 * j[2])


def clause_ok(clause, env):
    return any(env[abs(l) - 1] == (1 if l > 0 else 0) for l in clause)


def eliminate(n, clauses, var_table, zero, unit, add, mul, final_product):
    """Eliminacion de variables en orden 0..n-1 sobre factores (alcance, tabla)."""
    factors = [((i,), {(b,): var_table(i, b) for b in (0, 1)}) for i in range(n)]
    for clause in clauses:
        scope = tuple(sorted({abs(l) - 1 for l in clause}))
        tab = {}
        for bits in product((0, 1), repeat=len(scope)):
            env = dict(zip(scope, bits))
            tab[bits] = unit if clause_ok(clause, env) else zero
        factors.append((scope, tab))
    for v in range(n):
        chosen = [f for f in factors if v in f[0]]
        factors = [f for f in factors if v not in f[0]]
        rem = tuple(sorted(set().union(*(set(f[0]) for f in chosen)) - {v}))
        tab = {}
        for assignment in product((0, 1), repeat=len(rem)):
            env = dict(zip(rem, assignment))
            acc = zero
            for bit in (0, 1):
                env[v] = bit
                cur = chosen[0][1][tuple(env[i] for i in chosen[0][0])]
                for scope, t in chosen[1:]:
                    cur = mul(cur, t[tuple(env[i] for i in scope)])
                acc = add(acc, cur)
            tab[assignment] = acc
        factors.append((rem, tab))
    assert all(scope == () for scope, _ in factors) and len(factors) == 1
    value = factors[0][1][()]
    if final_product:
        value = mul(unit, value)
    return value


def joint_contraction(n, clauses):
    ops = Ops()
    j = eliminate(n, clauses, lambda i, b: (1, b, 0), ZERO, ONE, ops.add, ops.mul, False)
    return j, ops


def hermite_pair(n, clauses, t, ops):
    """(H(t,u), dH/dT(t,u)) con pares y regla del producto."""
    zero2, unit2 = (ZERO, ZERO), (ONE, ZERO)

    def add2(a, b):
        return (ops.add(a[0], b[0]), ops.add(a[1], b[1]))

    def mul2(a, b):
        return (ops.mul(a[0], b[0]), ops.add(ops.mul(a[0], b[1]), ops.mul(a[1], b[0])))

    def var_table(i, b):
        if b == 0:
            return unit2
        u1 = jet_pow(1)
        if i < min(3, n):                   # factor (1+u)(1+T): valor y derivada en T=t
            return (tuple((1 + t) * c for c in u1), u1)
        return (u1, ZERO)

    return eliminate(n, clauses, var_table, zero2, unit2, add2, mul2, True)


def hermite_weights():
    """Pesos w con H(0) = w . (H(1), H'(1), H(2), H'(2)) para grado <= 3."""
    rows = []
    for t in (1, 2):
        rows.append([Fraction(t) ** k for k in range(4)])                       # valor
        rows.append([Fraction(k) * Fraction(t) ** (k - 1) if k else Fraction(0)  # derivada
                     for k in range(4)])
    # resolver rows^T w = e0
    A = [[rows[i][k] for i in range(4)] + [Fraction(int(k == 0))] for k in range(4)]
    for c in range(4):
        p = next(r for r in range(c, 4) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for r in range(4):
            if r != c and A[r][c] != 0:
                A[r] = [a - A[r][c] * b for a, b in zip(A[r], A[c])]
    return [A[k][4] for k in range(4)]


def brute(n, clauses, deform=False, t=0):
    acc = ZERO
    for x in product((0, 1), repeat=n):
        if all(clause_ok(c, x) for c in clauses):
            f = 1
            if deform:
                for i in range(min(3, n)):
                    f *= 1 + t * x[i]
            acc = tuple(a + f * b for a, b in zip(acc, jet_pow(sum(x))))
    return acc


# ------------------------------------------------------------ Ruta 1
def ruta_continuaciones():
    clauses = [(1, 3), (2, 3)]                       # (x | z) & (y | z)
    prefixes = list(product((0, 1), repeat=2))
    firma = {p: tuple(int(all(clause_ok(c, p + (z,)) for c in clauses)) for z in (0, 1))
             for p in prefixes}
    assert firma == {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (1, 1)}
    clases = {}
    for p in prefixes:
        clases.setdefault(firma[p], []).append(p)
    assert len(clases) == 2
    # directo: cada prefijo con cada continuacion
    direct, checks_direct = ZERO, 0
    for p in prefixes:
        for z in (0, 1):
            checks_direct += 1
            if firma[p][z]:
                direct = tuple(a + b for a, b in zip(direct, jet_pow(sum(p) + z)))
    # agrupado: suma de pesos de prefijo en R por clase, cada continuacion una vez por clase
    grouped, checks_grouped = ZERO, 0
    ops = Ops()
    for f, miembros in clases.items():
        peso = ZERO
        for p in miembros:
            peso = ops.add(peso, jet_pow(sum(p)))
        for z in (0, 1):
            checks_grouped += 1
            if f[z]:
                grouped = ops.add(grouped, ops.mul(peso, jet_pow(z)))
    assert direct == grouped == brute(3, clauses) == (5, 10, 6)
    assert moments(grouped) == (5, 10, 22)
    assert (checks_direct, checks_grouped) == (8, 4)
    print('Ruta 1: 4 prefijos, 2 clases; J = 5 + 10u + 6u^2, (N,S,Q) = (5,10,22); '
          'verificaciones 8 -> 4.')
    return {'firmas': {''.join(map(str, p)): list(f) for p, f in firma.items()},
            'clases': len(clases), 'J': list(grouped), 'NSQ': list(moments(grouped)),
            'verificaciones_prefijo_sufijo': checks_direct,
            'verificaciones_clase_sufijo': checks_grouped}


# ------------------------------------------------------------ Ruta 2
SISTEMAS = [
    ('3 variables, (x|z)(y|z)', 3, [(1, 3), (2, 3)], (5, 10, 22), 138, 900),
    ('Cadena, 4 variables', 4, [(1, 2), (2, 3), (3, 4)], (8, 22, 64), 240, 1548),
    ('Ciclo, 6 variables', 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
     (18, 78, 348), 780, 4956),
    ('Formula incompatible, 4 variables', 4, [(1, 2), (2, 3), (3, 4), (1,), (-1,)],
     (0, 0, 0), 312, 2028),
]


def ruta_hermite():
    w = hermite_weights()
    assert w == [-4, -4, 5, -2]
    # la identidad vale para la base 1, T, T^2, T^3
    for k in range(4):
        data = [1 ** k, k * 1 ** (k - 1) if k else 0, 2 ** k, k * 2 ** (k - 1) if k else 0]
        assert sum(a * b for a, b in zip(w, data)) == int(k == 0)
    filas = []
    for nombre, n, clauses, nsq, joint_ref, herm_ref in SISTEMAS:
        j, jops = joint_contraction(n, clauses)
        hops = Ops()
        data = []
        for t in (1, 2):
            h, dh = hermite_pair(n, clauses, t, hops)
            assert h == brute(n, clauses, True, t)
            data += [h, dh]
        rec = tuple(sum(int(w[i]) * data[i][k] for i in range(4)) for k in range(3))
        assert rec == j == brute(n, clauses)
        assert moments(j) == nsq
        assert (jops.total, hops.total) == (joint_ref, herm_ref), (nombre, jops.total, hops.total)
        filas.append({'sistema': nombre, 'variables': n, 'clausulas': clauses,
                      'N': nsq[0], 'S': nsq[1], 'Q': nsq[2],
                      'operaciones_contraccion_conjunta': jops.total,
                      'operaciones_hermite_2_valores_2_derivadas': hops.total,
                      'razon': round(hops.total / jops.total, 2)})
        print(f'{nombre:36s} N={nsq[0]:3d} S={nsq[1]:3d} Q={nsq[2]:4d}  '
              f'conjunta={jops.total:5d}  hermite={hops.total:5d}  razon={hops.total / jops.total:.2f}')
    razones = [f['razon'] for f in filas]
    assert min(razones) == 6.35 and max(razones) == 6.52
    print('Hermite cubico: H(0) = -4H(1) - 4H\'(1) + 5H(2) - 2H\'(2); razon entre 6,35 y 6,52.')
    return {'pesos_hermite': [int(x) for x in w], 'sistemas': filas,
            'conteo': 'suma de ternas = 3 sumas; producto truncado = 6 productos + 3 sumas; '
                      'par (H, dH): producto = 3 productos truncados + 1 suma de ternas. '
                      'Se excluye la combinacion lineal final de los cuatro datos.'}


if __name__ == '__main__':
    out = {'fecha': '2026-11-13', 'ruta_continuaciones': ruta_continuaciones(),
           'ruta_hermite': ruta_hermite()}
    fn = Path(__file__).resolve().parent / 'resultados_paralelos.json'
    fn.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print('TODAS LAS COMPROBACIONES PASARON. Guardado:', fn.name)
