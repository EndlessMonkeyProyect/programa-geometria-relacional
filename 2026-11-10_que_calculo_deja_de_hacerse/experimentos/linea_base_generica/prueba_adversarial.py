#!/usr/bin/env python3
"""Prueba del contrato del reconocedor de paridades distribuidas.

Toma fórmulas válidas de la familia y les aplica una mutación al azar: cambiar un signo,
quitar o añadir una cláusula, reconectar un literal, fijar una variable, intercambiar
variables o identificar dos variables en toda la fórmula. Añade casos construidos a mano
fuera de la familia (ciclos de paridad, entradas negadas, compuertas sueltas, bloques de
paridad escritos sin compuertas).
Cada fórmula termina en uno de dos resultados: el reconocedor la rechaza, o la acepta y su
conteo se compara con la eliminación genérica, que no reconoce nada.

Uso:
    python3 -I experimentos/linea_base_generica/prueba_adversarial.py --salida RESULTADOS.json
"""
import argparse
import collections
import json
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, '..', 'reconocimiento_de_paridades_distribuidas'))
import laboratorio_relaciones_distribuidas as L   # noqa: E402
from eliminacion_generica import conteo_exacto    # noqa: E402

MUTACIONES = ('signo', 'quitar', 'anadir', 'reconectar', 'identificar', 'fijar', 'intercambiar')


def evaluar(nvars, cnf):
    """'rechazada', 'aceptada_correcta' o 'aceptada_incorrecta'."""
    try:
        cuenta = L.count_extracted(L.extract(cnf, nvars))['count']
    except (ValueError, AssertionError):
        return 'rechazada'
    return 'aceptada_correcta' if cuenta == conteo_exacto(nvars, list(set(cnf))) else 'aceptada_incorrecta'


def mutar(rng, cnf, nv, m):
    cnf = list(cnf)
    s = lambda l: 1 if l > 0 else -1          # noqa: E731
    if m == 'signo':
        i = rng.randrange(len(cnf)); c = list(cnf[i]); j = rng.randrange(len(c)); c[j] = -c[j]; cnf[i] = tuple(c)
    elif m == 'quitar':
        cnf.pop(rng.randrange(len(cnf)))
    elif m == 'anadir':
        vs = rng.sample(range(1, nv + 1), rng.choice((2, 3))); cnf.append(tuple(v * rng.choice((1, -1)) for v in vs))
    elif m == 'reconectar':
        i = rng.randrange(len(cnf)); c = list(cnf[i]); j = rng.randrange(len(c))
        c[j] = rng.randrange(1, nv + 1) * s(c[j]); cnf[i] = tuple(c)
    elif m == 'fijar':
        cnf.append((rng.randrange(1, nv + 1) * rng.choice((1, -1)),))
    elif m == 'intercambiar':
        a, b = rng.sample(range(1, nv + 1), 2); i = rng.randrange(len(cnf))
        cnf[i] = tuple((b if abs(l) == a else abs(l)) * s(l) for l in cnf[i])
    elif m == 'identificar':
        a, b = rng.sample(range(1, nv + 1), 2)
        cnf = [tuple((a if abs(l) == b else abs(l)) * s(l) for l in c) for c in cnf]
    return [L.norm(c) for c in cnf]


def casos_a_mano():
    def xor_en(b, z, x, y):                    # z := x XOR y sobre una variable ya existente
        t = b.gate('OR', x, y); u = b.gate('AND', x, y); b.cl += L.emit_gate(z, 'AND', t, -u)
    out = []
    b = L.Builder(4); xor_en(b, 3, 4, 1); xor_en(b, 4, 3, 2); out.append(('ciclo_de_paridad', b.top, b.cl))
    b = L.Builder(3); t = b.gate('OR', -1, 2); u = b.gate('AND', -1, 2); z = b.gate('AND', t, -u); b.cl.append((z,))
    out.append(('entrada_negada', b.top, b.cl))
    b = L.Builder(3); z = b.gate('AND', 1, 2); b.cl.append((z, 3, -1)); out.append(('compuerta_suelta', b.top, b.cl))
    b = L.Builder(4); z = b.xor2(1, 2); b.cl.append((z, 3, 4)); out.append(('paridad_dentro_de_OR', b.top, b.cl))
    b = L.Builder(3); t = b.gate('OR', 1, 2); u = b.gate('AND', 1, 2); b.gate('AND', t, -u); b.cl.append((t,))
    out.append(('auxiliar_fijada', b.top, b.cl))
    out.append(('tres_de_cuatro_sin_compuertas', 3, [(1, 2, 3), (1, -2, -3), (-1, 2, -3)]))
    out.append(('bloque_de_paridad_sin_compuertas', 3, [(1, 2, 3), (1, -2, -3), (-1, 2, -3), (-1, -2, 3)]))
    out.append(('igualdad_binaria', 2, [(1, -2), (-1, 2)]))
    return [(n, v, [L.norm(c) for c in cl]) for n, v, cl in out]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida')
    ap.add_argument('--casos', type=int, default=6000)
    a = ap.parse_args()
    rng = random.Random(20261110)
    tabla = collections.defaultdict(collections.Counter)
    tautologias = 0
    for _ in range(a.casos):
        n = rng.choice((6, 8, 10))
        u = rng.randrange(min(3, n // 4)) if n >= 8 else 0
        g = L.gen(n, rng.randrange(3), rng.randrange(10 ** 9), partial=u, long_edges=rng.randrange(3))
        m = rng.choice(MUTACIONES)
        cnf = mutar(rng, g['cnf'], g['variables'], m)
        if None in cnf:
            tautologias += 1
            continue
        tabla[m][evaluar(g['variables'], cnf)] += 1
    a_mano = {nombre: evaluar(nv, cnf) for nombre, nv, cnf in casos_a_mano()}
    total = collections.Counter()
    for c in tabla.values():
        total.update(c)
    total.update(a_mano.values())
    out = {'semilla': 20261110, 'mutaciones_generadas': a.casos, 'descartadas_por_tautologia': tautologias,
           'por_mutacion': {m: dict(tabla[m]) for m in MUTACIONES}, 'casos_a_mano': a_mano,
           'total': dict(total)}
    for m in MUTACIONES:
        print(f'{m:13s}', dict(tabla[m]))
    print('a mano      ', a_mano)
    print('total       ', dict(total))
    assert total['aceptada_incorrecta'] == 0
    if a.salida:
        with open(a.salida, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
