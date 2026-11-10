#!/usr/bin/env python3
"""Comparación del §9 con una sola medición para todos los métodos.

Fórmulas: las mismas semillas del laboratorio de paridades distribuidas (ciclo de ternas y
conexiones largas) y la familia de conexiones largas extendida hasta 256 variables primarias.
Para cada fórmula, ya generada (la generación no se cronometra):
  - reconocimiento + conteo: mediana de 7 ejecuciones de extract + count_extracted;
  - eliminación genérica sobre la fórmula tal como llega: mediana de 3, si la tabla mayor es ≤ 2^24;
  - DPLL del laboratorio (sin límite de reloj, 250.000 nodos): mediana de 3, solo en tamaños pequeños.
Se comprueba que todos los conteos completados coinciden.

Uso:
    python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --salida RESULTADOS.json
    python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --dimacs carpeta/
--dimacs escribe cada fórmula en formato DIMACS con su conteo esperado, para cualquier contador dedicado.
Requiere NumPy; NetworkX es opcional (ancho de relleno mínimo como segunda ordenación).
"""
import argparse
import json
import os
import platform
import statistics
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, '..', 'reconocimiento_de_paridades_distribuidas'))
import numpy as np                                    # noqa: E402
import laboratorio_relaciones_distribuidas as L       # noqa: E402
from eliminacion_generica import (ANCHO_MAXIMO, ancho_grado_minimo,  # noqa: E402
                                  conteo_exacto)


def ancho_relleno_minimo(nvars, cnf):
    try:
        import networkx as nx
        from networkx.algorithms.approximation import treewidth_min_fill_in
    except ImportError:
        return None
    G = nx.Graph()
    G.add_nodes_from(range(1, nvars + 1))
    for cl in cnf:
        vs = [abs(l) for l in cl]
        G.add_edges_from((a, b) for i, a in enumerate(vs) for b in vs[i + 1:])
    return treewidth_min_fill_in(G)[0] + 1


def mediana_ms(fn, veces):
    t, val = [], None
    for _ in range(veces):
        t0 = time.perf_counter()
        val = fn()
        t.append(1000 * (time.perf_counter() - t0))
    return round(statistics.median(t), 3), val


CASOS = (
    [('ciclo', dict(n=n, extra=k, seed=981 + n * 7 + k, partial=u))
     for n, k, u in [(8, 0, 0), (10, 1, 1), (12, 2, 1), (14, 2, 2), (16, 3, 2), (20, 2, 2),
                     (24, 2, 2), (32, 2, 3), (48, 2, 3), (64, 2, 3), (96, 2, 3)]]
    + [('largas', dict(n=n, extra=2, seed=8282 + n, partial=min(3, n // 8), long_edges=n // 3))
       for n in (12, 16, 20, 24, 32, 48, 64, 96, 128, 160, 200, 256)]
)


def medir(familia, kw):
    g = L.gen(kw['n'], kw['extra'], kw['seed'], partial=kw['partial'], long_edges=kw.get('long_edges', 0))
    cnf, nv = g['cnf'], g['variables']
    esperado = L.direct_primary(kw['n'], g['eq'], g['near'], g['ors'])
    t_rec, res = mediana_ms(lambda: L.count_extracted(L.extract(cnf, nv)), 7)
    assert res['count'] == esperado
    w = ancho_grado_minimo(nv, cnf)
    fila = {'familia': familia, 'n_primarias': kw['n'], 'variables': nv, 'clausulas': len(cnf),
            'raices_parciales': kw['partial'], 'clausulas_OR': kw['extra'],
            'conexiones_largas': kw.get('long_edges', 0), 'conteo': esperado,
            'reconocimiento_y_conteo_ms': t_rec,
            'ancho_grado_minimo': w, 'ancho_relleno_minimo': ancho_relleno_minimo(nv, cnf)}
    if w <= ANCHO_MAXIMO:
        t_el, c = mediana_ms(lambda: conteo_exacto(nv, cnf), 3)
        assert c == esperado
        fila['eliminacion_generica_ms'] = t_el
    else:
        fila['eliminacion_generica_ms'] = None
    if (familia == 'ciclo' and kw['n'] <= 32) or (familia == 'largas' and kw['n'] <= 24):
        t_d, d = mediana_ms(lambda: L.dpll_cnf(nv, cnf, maxnodes=250000, seconds=float('inf')), 3)
        assert d['complete'] and d['count'] == esperado
        fila['dpll_ms'], fila['dpll_nodos'] = t_d, d['nodes']
    else:
        fila['dpll_ms'], fila['dpll_nodos'] = None, None
    return fila, g


def escribir_dimacs(carpeta, familia, kw, g, conteo):
    os.makedirs(carpeta, exist_ok=True)
    nombre = os.path.join(carpeta, f"{familia}_n{kw['n']:03d}.cnf")
    with open(nombre, 'w') as f:
        f.write(f"c familia {familia}, primarias {kw['n']}, semilla {kw['seed']}\n")
        f.write(f"c conteo esperado {conteo}\n")
        f.write(f"p cnf {g['variables']} {len(g['cnf'])}\n")
        for cl in g['cnf']:
            f.write(' '.join(map(str, cl)) + ' 0\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida')
    ap.add_argument('--dimacs')
    a = ap.parse_args()
    filas = []
    for familia, kw in CASOS:
        fila, g = medir(familia, kw)
        filas.append(fila)
        if a.dimacs:
            escribir_dimacs(a.dimacs, familia, kw, g, fila['conteo'])
        el = fila['eliminacion_generica_ms']
        print(f"{familia:6s} n={kw['n']:3d} cl={fila['clausulas']:4d} conteo={fila['conteo']} | "
              f"reconocer+contar {fila['reconocimiento_y_conteo_ms']} ms | eliminación "
              f"{'%s ms' % el if el is not None else '—'} (tabla 2^{fila['ancho_grado_minimo']}) | "
              f"DPLL {fila['dpll_ms']}", flush=True)
    out = {'fecha_programa': '2026-11-10', 'protocolo': __doc__.strip().split('\n\n')[1],
           'entorno': {'python': platform.python_version(), 'numpy': np.__version__,
                       'procesador': platform.processor() or platform.machine()},
           'filas': filas}
    if a.salida:
        with open(a.salida, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
