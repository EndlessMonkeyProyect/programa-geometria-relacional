#!/usr/bin/env python3
"""Verificaciones ejecutables del laboratorio O44: alcance finito, no un certificado PDE."""
from pathlib import Path
import json, math
import numpy as np
import laboratorio_O44 as lab
import O43E_BASE_NO_MODIFICADA as orig

root=Path(__file__).parent
main=json.loads((root/'resultados_O44_N48.json').read_text())
high=json.loads((root/'control_O44_N64_fases_opuestas.json').read_text())
low=json.loads((root/'control_N32.json').read_text())
half=json.loads((root/'control_O44_N32_dtmitad.json').read_text())
matched=json.loads((root/'control_O44_N48_misma_enstrofia.json').read_text())
tests=0

def check(cond,name):
    global tests
    tests+=1
    if not cond: raise AssertionError(name)

# Interpolation of a spatially constant field including periodic boundaries.
N=16
const=np.ones((3,N,N,N),float)*np.array([1.4,-.7,.1])[:,None,None,None]
pts=np.array([[1,2,3],[-3.3,9.1,-8.5],[0,0,0],[3.12,-3.13,2.8]])
out=lab.grid_sample(const,pts)
check(np.max(np.abs(out-np.array([1.4,-.7,.1])))<1e-13,'interpolacion campo constante')
check(lab.tests_kine()==[(2,5,True),(1,4,True),(3,7,True)],'prueba cinemática')

# Phase 0/pi reproduce precisely initial data O43E. No physical time scaling inserted.
for N in (32,48):
    for theta,sign in ((0.,1),(math.pi,-1)):
        h0,_,_,K,k2=orig.make_case(N,sign)
        h1=lab.projected_initial_velocity(N,theta,K,k2)
        check(float(np.max(np.abs(h0-h1)))<1e-10, f'fase O43E N={N} theta={theta}')

assert len(main['cases'])==8
for j,r in enumerate(main['cases']):
    st,en=r['start'],r['end']
    tr=r['tracers']
    check(tr['count']==32,f'traza numero {j}')
    check(tr['num_complete_toroidal_turns']==0,f'sin retorno toroidal {j}')
    check(not tr['rho_material_defined'],f'resto indefinido {j}')
    check(tr['num_complete_poloidal_turns']==0,f'sin retorno poloidal {j}')
    check(tr['max_abs_toroidal_advance_radians']<.001,f'deriva toroidal acotada {j}')
    check(tr['min_distance_to_poloidal_axis']>.20,f'coordenada poloidal no singular {j}')
    check(en['divergence_L2']<1e-12,f'divergencia {j}')
    check(abs(en['dEdt']-en['stretch']+en['viscD'])<1e-13,f'identidad E {j}')
    check(en['E']<st['E'],f'E decrece {j}')
    check(abs(lab.angular_distance(en['delta31'],r['phase_requested']))<8e-3,f'fase detectada {j}')
    check(abs(en['delta21'])<1e-2,f'fase 2:1 proxima pero NO identica {j}')
check(main['phase_regression']['phase_LOOCV_RMSE']<.1*main['phase_regression']['blind_LOOCV_RMSE'],'mejora fase descriptiva')
check(main['phase_regression']['other_phase_blind_scalar_LOOCV_RMSE']['E']<main['phase_regression']['phase_LOOCV_RMSE'],'control adversarial de E0: fase NO independiente')
check(abs(matched['cases'][0]['start']['E']-matched['cases'][1]['start']['E'])<1e-14,'enstrofia inicial igualada')
check(matched['cases'][0]['end']['P_front']-matched['cases'][1]['end']['P_front']>2e-6,'diferencia local bajo E0 igualada')
check(max(r['end']['P_front'] for r in main['cases'])-min(r['end']['P_front'] for r in main['cases'])>2e-6,'Pfront distingue fases')
check(max(r['end']['stretch'] for r in main['cases'])-min(r['end']['stretch'] for r in main['cases'])<1e-7,'P global mucho menor que diferencia local')

for container in (low,half,high):
    for r in container['cases']:
        check(not r['tracers']['rho_material_defined'],'sin retorno todos los controles')

# Confirm N64 matches the archived O43-E published quantities (6-10 decimal digits).
for j,expected in enumerate((.009737247,.009739914)):
    check(abs(high['cases'][j]['end']['E']-expected)<5e-9,'N64 concordancia E O43E')
for j in (0,1):
    a=low['cases'][2*j]['end']
    b=half['cases'][j]['end']
    check(abs(a['P_front']-b['P_front'])<5e-11,'mitad paso Pfront N32')
    check(abs(a['E']-b['E'])<5e-11,'mitad paso E N32')
print(json.dumps({'checks':tests,'status':'PASS',
'scope':'O44 NS 3D Galerkin finito N32/48/64, T=.12; ausencia de vueltas y discriminación de fases en esta familia',
'no_claim':'no retorno físico universal, no prueba global de Navier-Stokes, no topología ni memoria material demostradas'},ensure_ascii=False,indent=2))
