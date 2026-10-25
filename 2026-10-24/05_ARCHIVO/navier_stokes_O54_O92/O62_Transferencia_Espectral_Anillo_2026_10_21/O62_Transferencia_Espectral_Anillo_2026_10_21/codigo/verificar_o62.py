#!/usr/bin/env python3
"""Control focal independiente sobre salidas previamente calculadas O62."""
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'resultados/transferencias_y_predicciones.csv').open()))
r=json.loads((ROOT/'resultados/resumen.json').read_text())
assert len(rows)==108
assert all(r['checks'].values())
for n in (32,40,48):
 for t in (.02,.08):
  for case in ((0.,0),(.14,0),(.14,1)):
   sub=[z for z in rows if int(z['N'])==n and abs(float(z['t'])-t)<1e-9 and abs(float(z['epsilon'])-case[0])<1e-9 and int(z['match_energy'])==case[1]]
   assert len(sub)==6
   assert abs(sum(float(z['initial_nonlinear_curvature']) for z in sub))<1e-11
   # Pronóstico de signos en los 6 sectores para los intervalos estudiados
   for z in sub:
    q=float(z['predicted_nonlinear_change']);obs=float(z['observed_nonlinear_change'])
    assert abs(q)>1e-10, (n,t,case,z['band'])
    assert q*obs>0, (n,t,case,z['band'],q,obs)
   core=next(z for z in sub if z['band']=='[2,4)')
   assert (float(core['initial_nonlinear_curvature'])>0)==(case[0]>.0)
# Reproducción de energías originales O53 en N=40 y N=48.
expected={(40,0.,0):.07788157,(40,.14,0):.08749412,(48,0.,0):.07788169,(48,.14,0):.08749141}
for t in r['totals']:
 key=(t['N'],t['epsilon'],int(t['match_energy']))
 if key in expected: assert abs(t['E']-expected[key])<1e-7,(key,t['E'])
assert max(abs(t['T']) for t in r['totals'])<1e-12
print('O62: 9 pares escenario-malla, 108 predicciones de signo, presupuesto y reproducción O53: PASS')
