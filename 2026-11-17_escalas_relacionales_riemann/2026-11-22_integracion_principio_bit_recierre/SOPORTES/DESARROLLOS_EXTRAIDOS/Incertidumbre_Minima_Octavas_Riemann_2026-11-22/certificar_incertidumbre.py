#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ensayo reproducible de incertidumbre minima por octavas.

Fuente de datos: Mecanismos del programa frente a la regla de eliminacion
entre escalas (20-XI-2026). Los valores fuente se imprimieron redondeados.
No se reejecuta el calculo original de las matrices de Gram: se certifican
las identidades y comparaciones construidas a partir de las tablas publicadas.

Uso: python3 certificar_incertidumbre.py [directorio_salida]
"""
from decimal import Decimal, localcontext
from pathlib import Path
import csv, json, math, sys

E_2_STR = '0.289965'
DELTA_STR = [
 '0.19613', '0.067953', '0.0064500', '0.0042219', '0.0033660',
 '0.0018686', '0.0015117', '0.00088547', '0.00090770', '0.00044319'
]
SEED_STR = [
 '0.19613', '0.057310', '0.0047878', '0.0035845', '0.0029370',
 '0.0013847', '0.0010898', '0.00054585', '0.00062970', '0.00029450'
]


def half_digit(literal: str) -> Decimal:
    x = Decimal(literal)
    return Decimal('0.5') * Decimal(10) ** x.as_tuple().exponent


def calcular():
    with localcontext() as ctx:
        ctx.prec = 40
        rests = [Decimal(E_2_STR)]
        uncertainty = [half_digit(E_2_STR)]
        gains = list(map(Decimal, DELTA_STR))
        seeds = list(map(Decimal, SEED_STR))
        for ds, d in zip(DELTA_STR, gains):
            rests.append(rests[-1] - d)
            uncertainty.append(uncertainty[-1] + half_digit(ds))
        assert len(rests) == 11
        assert all(rests[i] > rests[i+1] > 0 for i in range(10))
        assert all(seeds[i] <= gains[i] for i in range(10))
        rows = []
        for j in range(1, 12):
            E = rests[j-1]
            A = (j+1)*E
            lnN = j*math.log(2)
            row = dict(j=j,m=2**j,error=float(E),error_print_uncertainty=float(uncertainty[j-1]),
                       a_normalizado=float(A),error_por_logaritmo=float(E)*lnN)
            if j <= 10:
                d = gains[j-1]
                seed = seeds[j-1]
                theta = d/E
                c=(j+2)*theta
                c_seed = (j+2)*seed/E
                z = c-1
                nxtA=(j+2)*rests[j]
                assert abs(nxtA-A+E*z) < Decimal("1e-30"), (j, nxtA, A, z)
                # controles robustos a las cifras redondeadas
                Emin = E-uncertainty[j-1]
                Emax = E+uncertainty[j-1]
                dmin=d-half_digit(DELTA_STR[j-1]); dmax=d+half_digit(DELTA_STR[j-1])
                smin=seed-half_digit(SEED_STR[j-1])
                theta_lo=dmin/Emax
                theta_hi=dmax/Emin
                c_lo=(j+2)*theta_lo
                c_seed_lo=(j+2)*smin/Emax
                row.update(gain=float(d),semilla=float(seed),theta=float(theta),
                           c_critico=float(c),c_semilla=float(c_seed),
                           desfase=float(z),theta_min_redondeo=float(theta_lo),
                           theta_max_redondeo=float(theta_hi),
                           c_min_redondeo=float(c_lo),
                           semilla_c_min_redondeo=float(c_seed_lo),
                           cambio_a=float(nxtA-A))
            rows.append(row)
        assert all(row['c_min_redondeo'] > 0.75 for row in rows[:-1])
        assert all(row['semilla_c_min_redondeo'] > 0.5 for row in rows[:-1])
        assert rows[9]['c_critico'] < 1
        assert rows[9]['c_min_redondeo'] > .75
        assert rows[9]['cambio_a'] > 0
        # C_B es una referencia que se identifica con una constante
        # asintotica bajo hipotesis adicionales, no una cota puntual.
        gamma = 0.57721566490153286060651209
        C_B=2+gamma-math.log(4*math.pi)
        return rows,dict(
          fuente='Datos redondeados de informe del 20-XI-2026; no se ejecuta matriz de Gram',
          c_ref_bettin_conrey_farmer=C_B,
          residual_2048=rows[-1]['error'],
          error_por_log_2048=rows[-1]['error_por_logaritmo'],
          residual_2048_hipotetico_incertidumbre=rows[-1]['error_print_uncertainty'],
          ultima_theta=rows[9]['theta'],
          ultima_c_critico=rows[9]['c_critico'],
          ultima_c_semilla=rows[9]['c_semilla'],
          ultima_cambio_a=rows[9]['cambio_a'],
          c_rigida_1_pasa=False,
          c_flexible_075_pasa_10=True,
          c_semilla_05_pasa_10=True,
          solo_ensayo_finito=True,
        )


def salida(dest):
    rows,s=calcular()
    dest.mkdir(parents=True,exist_ok=True)
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys:keys.append(k)
    with (dest/'tabla_octavas.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys)
        w.writeheader(); w.writerows(rows)
    (dest/'resultado.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('j     m     e_m^2      (j+1)e_m^2   (j+2)theta  desfase  c_semilla')
    for row in rows:
        c=row.get('c_critico',float('nan'))
        z=row.get('desfase',float('nan'))
        b=row.get('c_semilla',float('nan'))
        print(f"{row['j']:2d} {row['m']:5d}  {row['error']:.8f}   {row['a_normalizado']:.7f}    {c:8.4f}   {z:+7.4f}   {b:7.4f}")
    print('\nCOMPROBACIONES: PASS')
    print('C_critico>=0.75 para los diez j, incluso con redondeo: SI')
    print('C_semilla>=0.50 para los diez j, incluso con redondeo: SI')
    print('La ley rigida C>=1 falla en j=10: SI')
    print('Error final y datos: ',s['residual_2048'],s['error_por_log_2048'])
    print('SALIDAS:',dest/'tabla_octavas.csv',dest/'resultado.json')


if __name__ == '__main__':
    d=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
    salida(d)
