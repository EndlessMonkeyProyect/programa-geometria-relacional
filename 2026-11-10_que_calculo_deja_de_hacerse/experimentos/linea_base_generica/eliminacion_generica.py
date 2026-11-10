#!/usr/bin/env python3
"""Contador exacto por eliminación de variables sobre la fórmula de cláusulas tal como llega.

No reconoce compuertas ni paridades: cada cláusula es una tabla de 0/1 y las variables
se eliminan en orden de grado mínimo. Es la línea base genérica del §9.
La tabla mayor que se forma es 2^w, con w el ancho de esa ordenación.
El conteo es exacto: se calcula módulo dos primos y se reconstruye por el teorema chino del resto,
lo que basta mientras el número de soluciones sea menor que el producto de los primos (~4,6·10^18).

Uso directo (autocomprobación contra fuerza bruta):
    python3 -I experimentos/linea_base_generica/eliminacion_generica.py
Requiere NumPy.
"""
import itertools
import random

import numpy as np

P1, P2 = 2147483629, 2147483587
ANCHO_MAXIMO = 24          # tablas de hasta 2^24 entradas


class AnchoExcedido(Exception):
    pass


def ancho_grado_minimo(nvars, cnf):
    """Ancho de la ordenación de grado mínimo (tamaño del mayor ámbito formado)."""
    adj = {v: set() for v in range(1, nvars + 1)}
    for cl in cnf:
        vs = [abs(l) for l in cl]
        for a in vs:
            adj[a].update(x for x in vs if x != a)
    w = 0
    while adj:
        v = min(adj, key=lambda x: (len(adj[x]), x))
        nb = list(adj[v])
        w = max(w, len(nb) + 1)
        for a in nb:
            adj[a].discard(v)
            adj[a].update(x for x in nb if x != a)
        del adj[v]
    return w


def _conteo_modular(nvars, cnf, p, ancho_maximo=ANCHO_MAXIMO):
    factores = []
    for cl in cnf:
        vs = tuple(sorted(abs(l) for l in cl))
        T = np.ones((2,) * len(vs), dtype=np.int64)
        T[tuple(0 if l > 0 else 1 for l in sorted(cl, key=abs))] = 0   # la asignación que la falsea
        factores.append((vs, T))
    adj = {v: set() for v in range(1, nvars + 1)}
    for vs, _ in factores:
        for a in vs:
            adj[a].update(x for x in vs if x != a)
    por_var = {v: [] for v in range(1, nvars + 1)}
    for i, (vs, _) in enumerate(factores):
        for v in vs:
            por_var[v].append(i)
    vivo = [True] * len(factores)
    escalar = 1
    pendientes = set(adj)
    while pendientes:
        v = min(pendientes, key=lambda x: (len(adj[x]), x))
        pendientes.discard(v)
        idx = [i for i in por_var[v] if vivo[i]]
        vecinos = sorted(adj[v])
        if len(vecinos) + 1 > ancho_maximo:
            raise AnchoExcedido(len(vecinos) + 1)
        if not idx:
            escalar = (escalar * 2) % p
        else:
            ambito = tuple(sorted(set().union(*[set(factores[i][0]) for i in idx])))
            pos = {u: k for k, u in enumerate(ambito)}
            acc = None
            for i in idx:
                vs, T = factores[i]
                vivo[i] = False
                forma = [1] * len(ambito)
                for u in vs:
                    forma[pos[u]] = 2
                Tb = T.reshape(forma)
                acc = Tb if acc is None else (acc * Tb) % p
            acc = np.broadcast_to(acc, (2,) * len(ambito))
            red = acc.sum(axis=pos[v]) % p
            salida = tuple(u for u in ambito if u != v)
            if salida:
                factores.append((salida, red))
                vivo.append(True)
                for u in salida:
                    por_var[u].append(len(factores) - 1)
            else:
                escalar = (escalar * int(red)) % p
        for a in vecinos:
            adj[a].discard(v)
            adj[a].update(x for x in vecinos if x != a)
        del adj[v]
    return escalar


def conteo_exacto(nvars, cnf, ancho_maximo=ANCHO_MAXIMO):
    """Número de asignaciones de las variables 1..nvars que satisfacen todas las cláusulas."""
    cnf = list(cnf)
    if any(len(c) == 0 for c in cnf):
        return 0
    a1 = _conteo_modular(nvars, cnf, P1, ancho_maximo)
    a2 = _conteo_modular(nvars, cnf, P2, ancho_maximo)
    return a1 + P1 * (((a2 - a1) * pow(P1, -1, P2)) % P2)


def autocomprobacion(casos=300, semilla=1):
    r = random.Random(semilla)
    for _ in range(casos):
        n = r.randint(1, 9)
        cnf = list({tuple(sorted({v * r.choice((1, -1)) for v in r.sample(range(1, n + 1), r.randint(1, min(3, n)))},
                                 key=abs)) for _ in range(r.randint(0, 12))})
        cnf = [c for c in cnf if len({abs(l) for l in c}) == len(c)]
        bruto = sum(all(any((bits[abs(l) - 1] == 1) == (l > 0) for l in c) for c in cnf)
                    for bits in itertools.product((0, 1), repeat=n))
        assert conteo_exacto(n, cnf) == bruto, (n, cnf)
    return casos


if __name__ == '__main__':
    print('eliminación genérica:', autocomprobacion(), 'fórmulas aleatorias contrastadas con fuerza bruta. OK')
