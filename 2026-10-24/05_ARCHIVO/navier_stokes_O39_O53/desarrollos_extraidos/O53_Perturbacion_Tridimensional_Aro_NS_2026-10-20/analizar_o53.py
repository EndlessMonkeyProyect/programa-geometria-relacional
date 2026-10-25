#!/usr/bin/env python3
"""O53 analysis. Computes diagnostics, events, baseline regression and creates figures.
Explicitly distinguishes numerical observation from proof of PDE regularity.
"""
from pathlib import Path
import numpy as np,json,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
FILES={'40_control':'NS_N40_eps00.json','40_7pct':'NS_N40_eps07.json','40_14pct':'NS_N40_eps14.json',
       '48_control':'NS_N48_eps00.json','48_14pct':'NS_N48_eps14.json','40_14pct_equal_energy':'NS_N40_eps14_equienergia.json','48_14pct_equal_energy':'NS_N48_eps14_equienergia.json'}

def crossing(t,phi,level=-1.0):
    hit=np.flatnonzero(phi<=level)
    if len(hit)==0:return None
    i=int(hit[0])
    if i==0:return float(t[0])
    p=(level-phi[i-1])/(phi[i]-phi[i-1])
    return float(t[i-1]+p*(t[i]-t[i-1]))

def summarise(j):
    a=j['records'];s=j['stats'];N=j['params']['N'];
    tt=np.array([v['t'] for v in a]);
    ph=np.array([v['phase_turns'] for v in a]);
    z=np.array([v['Zc_unwrapped'] for v in a]);
    phase=np.array([v['outer_diff_turns'] for v in a]);
    K=np.gradient(phase*2*np.pi,tt)/np.gradient(z,tt)*np.array([v['Rc'] for v in a]);
    events={name:crossing(tt,ph[:,i]) for i,name in enumerate(j['tracer_labels'])}
    return dict(N=N,perturbation=j['params']['epsilon'],match_energy=j['params'].get('match_energy',False),
                Ekin_initial=a[0]['energy'],Ekin_final=a[-1]['energy'],
                Eomega_initial=a[0]['enstrophy'],Eomega_final=a[-1]['enstrophy'],
                ell_initial=a[0]['ell_omega'],ell_final=a[-1]['ell_omega'],
                axial_displacement=s['axial_displacement'],outer_phase_diff_final=s['outer_phase_diff_final'],
                phase_peak=float(phase.max()),phase_trough=float(phase.min()),
                P_peak=float(max(q['stretching_P'] for q in a)),
                P_final=a[-1]['stretching_P'],D_final=a[-1]['dissipation_D'],
                K_middle_median=float(np.median(K[5:-5])),K_middle_range=[float(np.min(K[5:-5])),float(np.max(K[5:-5]))],
                swirl_rms_initial=s['initial_swirl_rms'],
                energy_balance_rel=s['energy_balance_rel'],enstrophy_balance_rel=s['enstrophy_balance_rel'],
                max_abs_divergence=s['max_abs_divergence'],events=events)

def build():
    raw={q:json.loads((D/fn).read_text()) for q,fn in FILES.items()}
    st={q:summarise(v) for q,v in raw.items()}
    reference=D.parent/'O52_Retorno_Material_y_Sincronizacion_NS_2026-10-20'/'O52_RESULTADOS.json'
    prior=json.loads(reference.read_text())
    tests={}
    for q,s in st.items():
        tests[f'{q}:divergence<1e-11']=s['max_abs_divergence']<1e-11
        tests[f'{q}:kinetic_dissipated']=s['Ekin_final']<s['Ekin_initial']
        tests[f'{q}:enstrophy_balance<1e-3']=abs(s['enstrophy_balance_rel'])<1e-3
        tests[f'{q}:energy_balance<1e-3']=abs(s['energy_balance_rel'])<1e-3
        tests[f'{q}:finite_trajectory']=np.isfinite(s['outer_phase_diff_final'])
    for N in (40,48):
        q=f'{N}_control'
        tests[f'{q}:O52_axial_regression']=abs(st[q]['axial_displacement']-prior['resoluciones'][str(N)]['avance_centro'])<1e-5
        tests[f'{q}:O52_phase_regression']=abs(st[q]['outer_phase_diff_final']-prior['resoluciones'][str(N)]['desfase_exterior_final_vueltas'])<1e-5
    for label in ('control','14pct','14pct_equal_energy'):
        q40=st[f'40_{label}'];q48=st[f'48_{label}']
        tests[f'{label}:N40_N48_axial_agreement']=abs(q40['axial_displacement']-q48['axial_displacement'])<.015
        tests[f'{label}:N40_N48_phase_agreement']=abs(q40['outer_phase_diff_final']-q48['outer_phase_diff_final'])<.025
    tests['perturbation_breaks_axisymmetry']=st['40_14pct']['swirl_rms_initial']>3*st['40_control']['swirl_rms_initial']
    tests['perturbation_changes_phase_both_N']=all(st[f'{N}_14pct']['outer_phase_diff_final']>st[f'{N}_control']['outer_phase_diff_final']+.01 for N in (40,48))
    for N in (40,48):
        tests[f'energy_is_matched_N{N}']=abs(st[f'{N}_control']['Ekin_initial']-st[f'{N}_14pct_equal_energy']['Ekin_initial'])<1e-12
        tests[f'matched_energy_phase_decreases_N{N}']=st[f'{N}_14pct_equal_energy']['outer_phase_diff_final']<st[f'{N}_control']['outer_phase_diff_final']-.01
    tests['P_nonzero_evolution']=st['40_14pct']['P_peak']>.02
    out={'results':st,'tests':{k:bool(v) for k,v in tests.items()},'passed':sum(bool(v) for v in tests.values()),'total':len(tests),
         'limits':{'not_proven':'No finite-time experiment proves NS global regularity, a universal locking law, or material closed orbits.',
                   'symmetry':'Perturbed run constructed from solenoidal velocity vector potential; finite periodic Fourier-Galerkin approximation.',
                   'phase':'A tracer crossing an unwrapped 2pi around the moving enstrophy center is NOT a Poincare return.',
                   'common_energy':'For epsilon changes without match_energy, the initial energy ALSO changes; compare equal-energy control.',
                   'uniform_background':'Mean Fourier zero mode set to zero: axial displacement is measured relative to zero background mean velocity.'}}
    (D/'O53_RESUMEN.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
    times=np.array([q['t'] for q in raw['48_control']['records']]);
    fig,ax=plt.subplots(figsize=(9,5.2))
    for q,lab in [('48_control','48³ control'),('48_14pct','48³ perturbación 14 %'),('40_7pct','40³ perturbación 7 %'),('48_14pct_equal_energy','48³ perturbación 14 % (energía igualada)')]:
        r=raw[q]['records'];ax.plot([v['t'] for v in r],[v['outer_diff_turns'] for v in r],label=lab)
    ax.set(xlabel='Tiempo de simulación',ylabel='Desfase exterior (vueltas)',title='O53 · Respuesta material al romper la simetría axial')
    ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(D/'o53_desfase_perturbacion.png',dpi=170);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5.2))
    for q,lab in [('48_control','48³ control'),('48_14pct','48³ perturbación 14 %'),('48_14pct_equal_energy','48³ perturbación 14 % (energía igualada)')]:
        r=raw[q]['records'];ax.plot([v['t'] for v in r],[v['Zc_unwrapped']-r[0]['Zc_unwrapped'] for v in r],label=lab)
    ax.set(xlabel='Tiempo de simulación',ylabel='Desplazamiento axial relativo',title='O53 · Desplazamiento del centro del aro')
    ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(D/'o53_avance.png',dpi=170);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5.2))
    for q,lab in [('48_control','48³ control'),('48_14pct','48³ perturbación 14 %')]:
        r=raw[q]['records'];ax.plot([v['t'] for v in r],[v['stretching_P'] for v in r],label=lab)
    ax.set(xlabel='Tiempo de simulación',ylabel='Producción global de enstrofía P',title='O53 · Estiramiento de vorticidad en flujos 3D')
    ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(D/'o53_estiramiento.png',dpi=170);plt.close(fig)
    print('O53',out['passed'],'/',out['total'],'CHECKS')
    for q,s in st.items():print(q,'E0',round(s['Ekin_initial'],7),'axial',round(s['axial_displacement'],6),'phase',round(s['outer_phase_diff_final'],6),'P_peak',round(s['P_peak'],5),'Krange',s['K_middle_range'])
    bad=[k for k,v in tests.items() if not v]
    if bad: print('FAILURES',bad);raise RuntimeError(bad)
    return out
if __name__=='__main__':build()
