#!/usr/bin/env python3
import json, csv, hashlib, zipfile, pathlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=pathlib.Path(__file__).resolve().parent
names=['NS32','NS40','NS40_halfdt','NS48']
data={name:json.loads((ROOT/(name+'.json')).read_text()) for name in names}
checks={}
def check(name, pred):
    checks[name]=bool(pred)
    if not pred:raise AssertionError(name)
for name,r in data.items():
    xs=r['samples']; t=np.array([z['t'] for z in xs]);Es=np.array([z['energy'] for z in xs]);J=np.array([z['enstrophy'] for z in xs]);nu=r['params']['nu']
    err=(Es[-1]-Es[0])+2*nu*np.trapezoid(J,t)
    r['energy_balance_rel_abs_error']=abs(err)/Es[0]
    check(name+' divergence free',r['max_divergence']<1e-10)
    check(name+' energy nonincreasing sampled',np.max(np.diff(Es))<1e-10)
    check(name+' energy balance trapezoidal',r['energy_balance_rel_abs_error']<5e-4)
    check(name+' moving ring',r['ring_center_displacement']>1.)
    check(name+' nontrivial material phase shear',abs(xs[-1]['phase_difference_outer_layers_turns'])>.07)
    check(name+' no full material turn',r['max_abs_phase_turns']<1.)
check('temporal displacement close',abs(data['NS40']['ring_center_displacement']-data['NS40_halfdt']['ring_center_displacement'])<1e-6)
check('temporal phase close',abs(data['NS40']['samples'][-1]['phase_difference_outer_layers_turns']-data['NS40_halfdt']['samples'][-1]['phase_difference_outer_layers_turns'])<1e-4)
check('spatial ring center difference N40/48',abs(data['NS40']['ring_center_displacement']-data['NS48']['ring_center_displacement'])<1e-3)
check('spatial phase difference N40/48',abs(data['NS40']['samples'][-1]['phase_difference_outer_layers_turns']-data['NS48']['samples'][-1]['phase_difference_outer_layers_turns'])<.015)
for i in range(3):
    n=['NS32','NS40','NS48'][i]; r=data[n];s=r['samples'];
    plt.plot([z['t'] for z in s],[z['phase_difference_outer_layers_turns'] for z in s],label=n)
plt.axhline(0,linewidth=.8,color='gray',alpha=.7)
plt.xlabel('Tiempo adimensional')
plt.ylabel('Desfase acumulado entre capas exteriores (vueltas)')
plt.title('O51 · Evolución NS 3D de un anillo vorticial')
plt.legend()
plt.grid(alpha=.25)
plt.tight_layout()
plt.savefig(ROOT/'o51_desfase_capas.png',dpi=180)
plt.close()
for n in ['NS40','NS48']:
    s=data[n]['samples']
    plt.plot([z['t'] for z in s],[z['Zcore_unwrapped']-s[0]['Zcore_unwrapped'] for z in s],label=n)
plt.xlabel('Tiempo adimensional')
plt.ylabel('Desplazamiento axial del centro de vorticidad')
plt.title('O51 · Propagación axial autogenerada')
plt.legend();plt.grid(alpha=.25);plt.tight_layout()
plt.savefig(ROOT/'o51_desplazamiento.png',dpi=180)
plt.close()
with (ROOT/'resumen_comparativo.csv').open('w',newline='') as f:
    wr=csv.writer(f);wr.writerow(['corrida','N','T','dt','desplazamiento_axial','U_media','energia_rel','enstrofia_rel','max_vueltas','desfase_exterior_vueltas','desfase_interior_vueltas','balance_energia_err_rel','divergencia_max'])
    for n in names:
        r=data[n];s=r['samples'];wr.writerow([n,r['params']['N'],r['params']['T'],r['params']['dt'],r['ring_center_displacement'],r['mean_axial_velocity'],r['energy_rel_change'],r['enstrophy_rel_change'],r['max_abs_phase_turns'],s[-1]['phase_difference_outer_layers_turns'],s[-1]['phase_difference_inner_layers_turns'],r['energy_balance_rel_abs_error'],r['max_divergence']])
(ROOT/'verificaciones_o51.json').write_text(json.dumps({'num_checks':len(checks),'passed':sum(checks.values()),'results':checks},indent=2))
print('PASS',sum(checks.values()),'/',len(checks))
for n in names:
    r=data[n];print(n, 'U=',r['mean_axial_velocity'],'desfase=',r['samples'][-1]['phase_difference_outer_layers_turns'],'relative energy residual=',r['energy_balance_rel_abs_error'])
