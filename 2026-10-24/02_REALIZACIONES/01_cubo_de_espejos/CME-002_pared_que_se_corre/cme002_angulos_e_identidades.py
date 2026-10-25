#!/usr/bin/env python3
"""CME-002 · Laboratorio del Cubo de Espejos — la pared que se corre: ángulos e identidades.

Regla de Diego (24-oct-2026): desde adentro la celda mide siempre uno; desde afuera, al
correrse la pared, la celda queda normalizada a la totalidad como 1/k. Cuando aparece un
múltiplo nuevo, ese entero k fija el ángulo pi/k entre dos espejos.

Dos lecturas de lo mismo:
  ÁNGULOS     dos espejos que se cortan en pi/k (matrices de reflexión, representación de Tits).
  IDENTIDADES aplicar los dos espejos k veces seguidas es no hacer nada: (s_i s_j)^k = 1.
              Se trabaja solo con esas igualdades, sin geometría (enumeración de Todd–Coxeter
              y serie de crecimiento de Steinberg).

Recinto: tres espejos con enteros (p, q, k). Familia principal (2, 3, k); control (2, 2, k).
Observable: orientaciones distintas alcanzadas con a lo sumo L reflexiones.
Criterio conocido (suma de ángulos del triángulo): 1/p + 1/q + 1/k > 1 cierra,
= 1 se repite (tesela el plano), < 1 se abre.

Ejecutar: python3 cme002_angulos_e_identidades.py   (NumPy y SymPy)
Escribe cme002_resultados.json y falla si las dos lecturas no coinciden.
"""
import json, math
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as sp
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.coset_table import coset_enumeration_r

LMAX = 16          # longitud máxima de palabra (H3 necesita 15 para cerrar)
TOPE_COCLASES = 6000

def matriz_coxeter(p, q, k):
    # m(s1,s2)=q, m(s2,s3)=k, m(s1,s3)=p  ->  triángulo de ángulos pi/p, pi/q, pi/k
    return [[1, q, p], [q, 1, k], [p, k, 1]]

# ---------- lectura por ÁNGULOS: matrices de reflexión ----------
def reflexiones(M):
    B = np.array([[-math.cos(math.pi / M[i][j]) for j in range(3)] for i in range(3)])
    gens = []
    for i in range(3):
        S = np.eye(3)
        S[i, :] -= 2 * B[i, :]          # s_i(v) = v - 2 B(e_i, v) e_i
        gens.append(S)
    return gens

def contar_por_angulos(M, lmax=LMAX):
    gens = reflexiones(M)
    clave = lambda A: tuple(np.round(A, 6).ravel() + 0.0)
    vistos = {clave(np.eye(3))}; frente = [np.eye(3)]; por_longitud = [1]
    for _ in range(lmax):
        nuevo = []
        for A in frente:
            for g in gens:
                P = g @ A; c = clave(P)
                if c not in vistos: vistos.add(c); nuevo.append(P)
        if not nuevo: break
        por_longitud.append(len(nuevo)); frente = nuevo
    return por_longitud

# ---------- lectura por IDENTIDADES ----------
F, a, b, c = free_group("a b c")
def cierre_por_identidades(M):
    g = [a, b, c]
    rel = [a**2, b**2, c**2] + [(g[i] * g[j]) ** M[i][j] for i in range(3) for j in range(i + 1, 3)]
    try:
        T = coset_enumeration_r(FpGroup(F, rel), [], max_cosets=TOPE_COCLASES)
        T.compress()
        return len(T.table)
    except ValueError:
        return None   # no cerró dentro del tope

t, u = sp.symbols('t u')
def serie_steinberg(M, lmax=LMAX):
    """Conteo por longitud deducido solo de los enteros (grupo infinito):
    1/W(1/t) = suma sobre subconjuntos propios T de (-1)^|T| / W_T(t)."""
    dihedral = lambda m: (1 + t) * sum(t**i for i in range(m))
    suma = 1 - 3 / (1 + t) + sum(1 / dihedral(M[i][j]) for i in range(3) for j in range(i + 1, 3))
    W = sp.cancel(1 / suma.subs(t, 1 / u))
    serie = sp.series(W, u, 0, lmax + 1).removeO()
    coef = [int(serie.coeff(u, n)) for n in range(lmax + 1)]
    num, den = sp.fraction(sp.together(W))
    raices = [r for r in sp.Poly(den, u).nroots(n=30) if abs(sp.im(r)) < 1e-20 and sp.re(r) > 0]
    tasa = 1 / min(float(sp.re(r)) for r in raices) if raices else None
    return coef, tasa

def regimen(p, q, k):
    s = Fraction(1, p) + Fraction(1, q) + Fraction(1, k)
    return s, ('cierra' if s > 1 else 'se repite' if s == 1 else 'se abre')

def factores(k):
    return sorted(sp.factorint(k).items())

def main():
    out = {'LMAX': LMAX, 'familias': {}}
    lehmer = max(float(r) for r in sp.Poly(u**10 + u**9 - u**7 - u**6 - u**5 - u**4 - u**3 + u + 1, u).nroots(n=30)
                 if abs(sp.im(r)) < 1e-20)
    for nombre, (p, q) in (('2_3_k', (2, 3)), ('2_2_k_control', (2, 2))):
        filas = []
        print(f"\nFamilia ({p},{q},k)")
        print(" k  factores      suma    régimen    ángulos (orientaciones nuevas por L)  identidades")
        for k in range(2, 13):
            M = matriz_coxeter(p, q, k)
            s, reg = regimen(p, q, k)
            geo = contar_por_angulos(M)
            orden = cierre_por_identidades(M)
            fila = {'k': k, 'factores': factores(k), 'suma': str(s), 'regimen': reg,
                    'conteo_por_longitud_angulos': geo, 'orden_identidades': orden}
            if reg == 'cierra':
                assert orden is not None and sum(geo) == orden, (p, q, k, orden, sum(geo))
                ident = f"cierra en {orden}"
            else:
                assert orden is None, (p, q, k, orden)
                coef, tasa = serie_steinberg(M)
                assert coef == geo, (p, q, k, coef, geo)       # ángulos == identidades, longitud por longitud
                fila['conteo_por_longitud_identidades'] = coef
                fila['tasa_de_crecimiento'] = tasa
                ident = (f"misma serie; crece linealmente (sin tasa exponencial)" if reg == 'se repite'
                         else f"misma serie; tasa {tasa:.6f} por paso")
                if reg == 'se repite':
                    # crecimiento lineal: los incrementos se repiten con periodo fijo
                    dif = [geo[n + 1] - geo[n] for n in range(1, len(geo) - 1)]
                    per = next(P for P in range(1, len(dif)) if all(dif[i] == dif[i + P] for i in range(len(dif) - P)))
                    assert per <= len(dif) // 2, dif
                    assert tasa is None or abs(tasa - 1) < 1e-9, tasa
                    fila['incrementos'] = dif; fila['periodo'] = per
                    fila['incremento_medio_por_paso'] = str(Fraction(sum(dif[:per]), per))
            filas.append(fila)
            print(f"{k:2d}  {'·'.join(f'{b}^{e}' if e > 1 else str(b) for b, e in factores(k)):12s} {str(s):>6s}  {reg:10s} {str(geo[:8]):37s} {ident}")
        out['familias'][nombre] = filas
    k7 = next(f for f in out['familias']['2_3_k'] if f['k'] == 7)
    out['tasa_2_3_7'] = k7['tasa_de_crecimiento']; out['numero_de_Lehmer'] = lehmer
    assert abs(k7['tasa_de_crecimiento'] - lehmer) < 1e-12
    print(f"\n(2,3,7): tasa de apertura {k7['tasa_de_crecimiento']:.12f} = número de Lehmer {lehmer:.12f}")
    for f in out['familias']['2_3_k']:
        assert f['regimen'] == ('cierra' if f['k'] <= 5 else 'se repite' if f['k'] == 6 else 'se abre')
    for f in out['familias']['2_2_k_control']:
        assert f['regimen'] == 'cierra' and f['orden_identidades'] == 4 * f['k']
    out['resumen'] = ('(2,3,k): cierra para k=2..5 (12, 24, 48, 120), se repite en k=6, se abre desde k=7. '
                      '(2,2,k): cierra para todo k en 4k. Ángulos e identidades coinciden en todos los casos.')
    print(out['resumen'])
    Path(__file__).with_name('cme002_resultados.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
