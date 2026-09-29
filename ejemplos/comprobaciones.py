#!/usr/bin/env python3
"""Ejemplos editoriales exactos; no son los scripts históricos del programa."""
from fractions import Fraction as F
from itertools import product
import json
import sys


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mv(a, x):
    return [dot(row, x) for row in a]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def main():
    checks = []
    s, x, y = [0,0,1,1], [0,1,0,1], [0,0,0,1]
    signatures = lambda *cols: set(zip(*cols))
    assert len(signatures(s)) == 2
    assert len(signatures(s,x)) == 4
    assert len(signatures(s,y)) == 3
    assert len(signatures(s,x,y)) == 4
    assert all(c == a*b for a,b,c in zip(s,x,y))
    checks.append("Novedad plena 2→4, parcial 2→3 y redundancia 4→4")
    a = {(v,w) for v,w in product((0,1), repeat=2) if v == w}
    b = a.copy()
    joined = {(v,w,z) for v,w,z in product((0,1), repeat=3) if (v,w) in a and (w,z) in b}
    frontier = {(v,z) for v,w,z in joined}
    assert frontier == {(0,0),(1,1)}
    assert {v for v,z in frontier} == {0,1}
    assert {z for v,z in frontier} == {0,1}
    checks.append("Composición por frontera compartida y dependencia conjunta")
    j = [[0,-1],[1,0]]
    assert mm(j,j) == [[-1,0],[0,-1]]
    v = [1,0]
    orbit = []
    for _ in range(4):
        orbit.append(tuple(v))
        v = mv(j,v)
    assert len(set(orbit)) == 4 and v == [1,0]
    assert dot([1,2], mv(j,[1,2])) == 0
    checks.append("Cierre orbital de cuatro y perpendicularidad con métrica compatible")
    p = [[1,0,0],[0,1,0],[0,0,0]]
    d = [2,-3,0]
    assert [u-v for u,v in zip(d,mv(p,d))] == [0,0,0]
    checks.append("La resta interna al subespacio no produce residuo exterior")
    q = [0,0,1]
    assert cross(q,q) == [0,0,0]
    checks.append("La semilla paralela al eje es anulada por el producto")
    pure = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
    mixed = [[F(1,2),F(0)],[F(0),F(1,2)]]
    tr = lambda a: sum(a[i][i] for i in range(len(a)))
    assert tr(mm(pure,pure)) == 1
    assert tr(mm(mixed,pure)) == F(1,2)
    checks.append("Estado mixto y vector uniforme difieren ante un proyector no diagonal")
    b1 = [[-1,0,1],[1,-1,0],[0,1,-1]]
    h = [1,1,1]
    lap_open = mm(transpose(b1), b1)
    lap_filled = [[lap_open[i][k] + h[i]*h[k] for k in range(3)] for i in range(3)]
    assert mv(lap_open,h) == [0,0,0]
    assert mv(lap_filled,h) == [3,3,3]
    checks.append("Ciclo armónico sin cara y disipación habilitada al rellenarla")
    phases = [F(1,3),F(7,5),F(-2,7)]
    delta = [phases[0]-phases[1],phases[1]-phases[2],phases[2]-phases[0]]
    assert sum(delta) == 0
    checks.append("Diferencias exactas cancelan sobre un ciclo")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"estado":"PASS","grupos_de_comprobaciones":len(checks),"resultados":checks,
                      "alcance":"Ejemplos editoriales finitos; no validación física ni reproducción histórica."},
                     ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
