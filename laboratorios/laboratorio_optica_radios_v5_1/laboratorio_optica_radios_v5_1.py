#!/usr/bin/env python3
# Endless Monkey Project — Relational Geometry Program
# Le Matt Ansatz Di Ego
# Laboratorio óptico v5.1 / Optical lab v5.1 — solo biblioteca estándar, Python >= 3.9.
"""Radios, pared móvil y aparición de nuevas referencias (secciones A–E).

Cada valor que se escribe en el CSV se calcula en esta ejecución.
"""
from __future__ import annotations

import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / 'resultados_optica_v5_1.csv'
ROWS: list[dict] = []

C_LUZ = 299_792_458.0          # [m/s]
R0 = 0.25                      # radio de apertura del receptor [m]
LAMBDA_REF = 550e-9            # banda central: referencia de la extensión angular [m]
R = 5e8                        # radio de la estructura [m]
SEP = 1e7                      # separación de los pares cercanos [m]
ESCENA_A = [-R, -R + SEP, 0.0, R - SEP, R]
ESCENA_B = [-R, -R, 0.0, R, R]  # fuentes coincidentes: tres posiciones distintas
BANDAS = [450e-9, 450e-9, 550e-9, 650e-9, 650e-9]
PESOS = [1.0, 1.2, 2.0, 1.3, 1.0]
D0 = 1e15                      # distancia inicial [m]
V = -2e6                       # velocidad relativa, negativa = acercamiento [m/s]
INSTANTES = [0, 2e8, 3.3e8, 4e8, 4.9e8, 4.96e8, 4.99e8]   # [s]
CONTEOS_ESPERADOS = [1, 1, 2, 3, 3, 4, 5]


def reg(seccion, caso, medida, valor, unidad='', notas=''):
    ROWS.append(dict(seccion=seccion, caso=caso, medida=medida,
                     valor=str(valor), unidad=unidad, notas=notas))


def g6(x):
    return f'{x:.6g}'


# ---------------------------------------------------------------- A — espejos
def firma_orbita(x, L):
    """Representante en [0, L] de la órbita {±x + 2kL} bajo x→−x, x→2L−x."""
    return L - abs((x % (2 * L)) - L)


def prueba_A():
    p, q = 0.25, 1.75
    for L in (1.0, 2.0, 7.0):
        s0 = lambda x: -x
        sL = lambda x, L=L: 2 * L - x
        for x in (p, q, 3.3):
            assert math.isclose(s0(s0(x)), x)
            assert math.isclose(sL(sL(x)), x)
            assert math.isclose(sL(s0(x)), x + 2 * L)
    for L in (1.0, 2.0):
        for k in range(-3, 4):
            for x in (p, q):
                for y in (x + 2 * k * L, -x + 2 * k * L):
                    assert math.isclose(firma_orbita(y, L), firma_orbita(x, L), abs_tol=1e-12)
    misma_L1 = math.isclose(firma_orbita(p, 1), firma_orbita(q, 1))
    misma_L2 = math.isclose(firma_orbita(p, 2), firma_orbita(q, 2))
    assert misma_L1 and not misma_L2
    for L, misma in ((1, misma_L1), (2, misma_L2)):
        reg('A_espejos', f'L={L}', 'firma(0.25)', firma_orbita(p, L), 'u')
        reg('A_espejos', f'L={L}', 'firma(1.75)', firma_orbita(q, L), 'u')
        reg('A_espejos', f'L={L}', 'misma_orbita', int(misma), 'bool')


# ------------------------------------------------------- B — radios y óptica
def doppler(v):
    """Doppler relativista longitudinal de un trayecto emisor→observador."""
    b = v / C_LUZ
    return math.sqrt((1 + b) / (1 - b))


def umbral(lam, f):
    """Rayleigh, apertura circular de radio R0, longitud de onda observada lam·f."""
    return 1.22 * lam * f / (2 * R0)


def pares_vecinos(pos):
    orden = sorted(range(len(pos)), key=lambda i: pos[i])
    return list(zip(orden[:-1], orden[1:]))


def componentes(pos, D, f):
    """Un par de vecinos se separa si su hueco angular alcanza el umbral de la
    mayor longitud de onda del par (la mancha más ancha)."""
    ang = [math.atan(x / D) for x in pos]
    n = 1
    for i, j in pares_vecinos(pos):
        if ang[j] - ang[i] >= umbral(max(BANDAS[i], BANDAS[j]), f):
            n += 1
    return n


def extension_relativa(pos, D, f):
    """Tamaño angular total dividido entre el umbral de la banda central."""
    ang = [math.atan(x / D) for x in pos]
    return (max(ang) - min(ang)) / umbral(LAMBDA_REF, f)


def transiciones(pos, f):
    """Distancia D_i = g_i / θ_i a la que cada hueco alcanza su umbral."""
    out = []
    for i, j in pares_vecinos(pos):
        g = pos[j] - pos[i]
        if g > 0:
            out.append(g / umbral(max(BANDAS[i], BANDAS[j]), f))
    return sorted(out)


def prueba_B():
    f_ac, f_al = doppler(V), doppler(-V)
    assert abs(V) / C_LUZ < 0.01
    reg('B_radios', 'acercamiento', 'factor_doppler', f'{f_ac:.9g}', 'adimensional')
    reg('B_radios', 'alejamiento', 'factor_doppler', f'{f_al:.9g}', 'adimensional')
    for lam in sorted(set(BANDAS)):
        reg('B_radios', f'banda {lam * 1e9:.0f} nm', 'umbral_rayleigh_acercamiento',
            f'{umbral(lam, f_ac):.6g}', 'rad')

    distancias = [D0 + V * t for t in INSTANTES]
    conteos = []
    for t, D in zip(INSTANTES, distancias):
        assert D > 0
        n = componentes(ESCENA_A, D, f_ac)
        ext = extension_relativa(ESCENA_A, D, f_ac)
        conteos.append(n)
        caso = f't={t:.4g} s'
        reg('B_radios', caso, 'distancia_D', g6(D), 'm')
        reg('B_radios', caso, 'componentes_espaciales', n, 'grupos')
        reg('B_radios', caso, 'extension_angular/umbral_550nm', f'{ext:.4g}', 'adimensional')
        reg('B_radios', caso, 'imagen', 'puntual' if ext < 1 else 'extendida', '')
        reg('B_radios', caso, 'flujo_relativo', g6((D0 / D) ** 2), 'proporción', 'Ley 1/D²')
    assert conteos == CONTEOS_ESPERADOS
    # Una sola componente no implica imagen puntual.
    assert conteos[0] == 1 and extension_relativa(ESCENA_A, distancias[0], f_ac) < 1
    assert conteos[1] == 1 and extension_relativa(ESCENA_A, distancias[1], f_ac) > 1

    # Transiciones exactas y escalera completa.
    tr = transiciones(ESCENA_A, f_ac)
    assert len(tr) == 4
    for k, Dk in enumerate(tr, 1):
        antes = componentes(ESCENA_A, Dk * (1 - 1e-6), f_ac)
        despues = componentes(ESCENA_A, Dk * (1 + 1e-6), f_ac)
        assert antes == despues + 1
        reg('B_transiciones', f'D_{k}', 'distancia', g6(Dk), 'm',
            f'{antes} componentes por debajo, {despues} por encima')
    puntos = [tr[0] / 2] + [math.sqrt(a * b) for a, b in zip(tr[:-1], tr[1:])] + [tr[-1] * 2]
    escalera = [componentes(ESCENA_A, D, f_ac) for D in puntos]
    assert escalera == [5, 4, 3, 2, 1]
    reg('B_transiciones', 'escalera', 'componentes_por_tramo', '-'.join(map(str, escalera)),
        'grupos', 'De cerca a lejos')

    # Movimiento invertido: alejamiento real (v > 0), distancias recorridas al revés.
    conteos_alejamiento = [componentes(ESCENA_A, D, f_al) for D in reversed(distancias)]
    assert conteos_alejamiento == conteos[::-1]
    reg('B_radios', 'alejamiento', 'componentes_en_orden_recorrido',
        '-'.join(map(str, conteos_alejamiento)), 'grupos')
    reg('B_radios', 'alejamiento', 'desplazamiento_relativo_transiciones',
        f'{f_ac / f_al:.6g}', 'adimensional', 'D_i(alejamiento)/D_i(acercamiento)')

    espectro = defaultdict(float)
    for lam, w in zip(BANDAS, PESOS):
        espectro[round(lam * 1e9)] += w
    assert len(espectro) == 3
    for banda in sorted(espectro):
        reg('B_espectro', 'receptor_ideal', f'peso_banda_{banda}_nm', g6(espectro[banda]), 'relativo')


# ----------------------------------------------------------- C — fases
CASOS_C = [([3], 5), ([3, 5], 9), ([3, 5, 9], 7), ([3, 5, 7], 9), ([3, 5, 7, 9], 9), ([3, 5], 5)]


def firma_de_fase(d, periodos):
    """Fase ideal 2π·d/p para cada período p, con d en unidades u."""
    return tuple(d % p for p in periodos)


def prueba_C():
    for P, m in CASOS_C:
        H = math.lcm(*P)
        Hn = math.lcm(H, m)
        factor = Hn // H
        assert factor == m // math.gcd(H, m)
        assert (factor > 1) == (H % m != 0)
        assert all(firma_de_fase(d, P) == firma_de_fase(d + H, P) for d in range(2 * H))
        assert len({firma_de_fase(d, P) for d in range(H)}) == H
        assert len({firma_de_fase(d, P + [m]) for d in range(Hn)}) == Hn
        for d in range(min(Hn, 200)):
            separa = firma_de_fase(d, P + [m]) != firma_de_fase(d + H, P + [m])
            assert separa == (H % m != 0)
        costo, aporte = math.log2(m), math.log2(factor)
        caso = f'P={P}, nuevo={m}'
        reg('C_fases', caso, 'periodo_heredado_H', H, 'u')
        reg('C_fases', caso, 'periodo_combinado_H2', Hn, 'u')
        reg('C_fases', caso, 'clases_por_clase_heredada', factor, 'clases')
        reg('C_fases', caso, 'bits_que_cuesta', f'{costo:.4f}', 'bits', 'log2(m)')
        reg('C_fases', caso, 'bits_que_aporta', f'{aporte:.4f}', 'bits', 'log2(m/mcd(H,m))')
        reg('C_fases', caso, 'eficiencia', f'{aporte / costo:.4f}', 'proporción')
    u = 100e-9
    for p in (3, 5, 7, 9):
        lam = 2 * p * u
        desplazamiento = lam / 2
        assert math.isclose(desplazamiento, p * u)
        assert math.isclose(math.cos(4 * math.pi * desplazamiento / lam), 1, abs_tol=1e-12)
        reg('C_fases', f'periodo={p}', 'lambda', f'{lam * 1e9:.0f}', 'nm')
        reg('C_fases', f'periodo={p}', 'periodo_en_distancia', f'{desplazamiento * 1e9:.0f}', 'nm')


# -------------------------------------------------------- D — economía
def potencias_maximas(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            out.append(q)
        p += 1
    if n > 1:
        out.append(n)
    return sorted(out)


def prueba_D():
    B = 630
    reg('D_economia', f'ventana=[0,{B})u', 'bits_para_ubicar_una_posicion', f'{math.log2(B):.4f}', 'bits')
    for P in ([3, 5], [3, 5, 9], [5, 7, 9], [3, 5, 7, 9]):
        H = math.lcm(*P)
        clases = defaultdict(list)
        for d in range(B):
            clases[firma_de_fase(d, P)].append(d)
        assert len(clases) == H
        assert {len(v) for v in clases.values()} == {B // H}
        guardados = sum(math.log2(p) for p in P)
        redundantes = guardados - math.log2(H)
        redundantes = 0.0 if abs(redundantes) < 1e-12 else redundantes
        caso = f'P={P}'
        reg('D_economia', caso, 'firmas_distintas', H, 'clases')
        reg('D_economia', caso, 'posiciones_por_firma', B // H, 'posiciones')
        reg('D_economia', caso, 'bits_que_distingue', f'{math.log2(H):.4f}', 'bits')
        reg('D_economia', caso, 'bits_guardados', f'{guardados:.4f}', 'bits', 'suma de log2(p)')
        reg('D_economia', caso, 'bits_redundantes', f'{redundantes:.4f}', 'bits')

    P = [3, 5, 7, 9]
    H = math.lcm(*P)
    base = potencias_maximas(H)
    assert base == [5, 7, 9] and math.prod(base) == H
    for d in range(B):
        for e in range(d + 1, min(B, d + H + 1)):
            assert (firma_de_fase(d, P) == firma_de_fase(e, P)) == (firma_de_fase(d, base) == firma_de_fase(e, base))
    reg('D_economia', f'P={P}', 'base_minima', '{' + ','.join(map(str, base)) + '}', 'periodos',
        'Potencias máximas de primos de H')

    P = [3, 5, 9]
    H = math.lcm(*P)
    for m in (3, 9, 15, 45, 2, 7):
        tabla, determinada = {}, True
        for d in range(B):
            if tabla.setdefault(firma_de_fase(d, P), d % m) != d % m:
                determinada = False
                break
        assert determinada == (H % m == 0)
        reg('D_economia', f'P={P}, consulta x mod {m}', 'respondida_con_lo_heredado',
            int(determinada), 'bool')


# ------------------------------------------------------ E — reapertura
def centroide(pos, D):
    return sum(w * math.atan(x / D) for x, w in zip(pos, PESOS)) / sum(PESOS)


def prueba_E():
    f = doppler(V)
    lejos, cerca = 1e15, 2e12
    nA_l, nB_l = componentes(ESCENA_A, lejos, f), componentes(ESCENA_B, lejos, f)
    nA_c, nB_c = componentes(ESCENA_A, cerca, f), componentes(ESCENA_B, cerca, f)
    assert (nA_l, nB_l, nA_c, nB_c) == (1, 1, 5, 3)
    eA, eB = extension_relativa(ESCENA_A, lejos, f), extension_relativa(ESCENA_B, lejos, f)
    assert math.isclose(eA, eB) and eA < 1
    reg('E_reapertura', 'A', 'posiciones_distintas', len(set(ESCENA_A)), 'posiciones')
    reg('E_reapertura', 'B', 'posiciones_distintas', len(set(ESCENA_B)), 'posiciones')
    for caso, n in (('A_lejos', nA_l), ('B_lejos', nB_l), ('A_cerca', nA_c), ('B_cerca', nB_c)):
        reg('E_reapertura', caso, 'componentes_espaciales', n, 'grupos')
    reg('E_reapertura', 'A_lejos', 'extension_angular/umbral_550nm', f'{eA:.4g}', 'adimensional')
    reg('E_reapertura', 'B_lejos', 'extension_angular/umbral_550nm', f'{eB:.4g}', 'adimensional')
    dc = abs(centroide(ESCENA_A, lejos) - centroide(ESCENA_B, lejos))
    reg('E_reapertura', 'A_vs_B_lejos', 'diferencia_de_centroides', f'{dc:.4g}', 'rad')
    reg('E_reapertura', 'A_vs_B_lejos', 'diferencia_de_centroides/umbral_550nm',
        f'{dc / umbral(LAMBDA_REF, f):.4g}', 'adimensional')


def main():
    if not __debug__:
        sys.exit('Este laboratorio verifica con assert; ejecútelo sin -O. / '
                 'This lab checks with assert; run it without -O.')
    prueba_A()
    prueba_B()
    prueba_C()
    prueba_D()
    prueba_E()
    with RESULTS.open('w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['seccion', 'caso', 'medida', 'valor', 'unidad', 'notas'])
        w.writeheader()
        w.writerows(ROWS)
    print('PRUEBAS A-E SUPERADAS; registros =', len(ROWS))
    claves = ('componentes_espaciales', 'imagen', 'componentes_por_tramo',
              'clases_por_clase_heredada', 'base_minima')
    for row in ROWS:
        if row['medida'] in claves or row['seccion'] == 'B_transiciones':
            print(row['seccion'], row['caso'], row['medida'], '=', row['valor'])
    print('CSV:', RESULTS.name)


if __name__ == '__main__':
    main()
