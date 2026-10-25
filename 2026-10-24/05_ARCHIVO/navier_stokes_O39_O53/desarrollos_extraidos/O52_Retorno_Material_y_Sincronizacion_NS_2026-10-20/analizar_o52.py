#!/usr/bin/env python3
"""O52: postprocesamiento de retornos de fase, controles y gráficos reproducibles.
No identifica retorno de fase con retorno espacial material ni garantiza convergencia del PDE.
"""
import json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE = Path(__file__).parent

def event_time(times, signal, level=-1.0):
    """Primera intersección de fase desenrollada (en vueltas) con el nivel."""
    hit=np.flatnonzero(signal <= level)
    if hit.size == 0:return None
    i=int(hit[0]); assert i>0 and signal[i-1]>level
    w=(level-signal[i-1])/(signal[i]-signal[i-1])
    return float(times[i-1]+w*(times[i]-times[i-1]))

def summarize(j):
    s=j['samples']; t=np.array([z['t'] for z in s]);
    phi=np.array([z['particle_phase_turns'] for z in s]);
    dz=np.array([z['Zcore_unwrapped'] for z in s]);
    dd=np.array([z['phase_difference_outer_layers_turns'] for z in s]);
    en=np.array([z['energy'] for z in s]); enn=np.array([z['enstrophy'] for z in s]);
    events=[]
    for i,label in enumerate(j['tracer_labels']):
        tt=event_time(t,phi[:,i]);
        zz=None if tt is None else float(np.interp(tt,t,dz)-dz[0]);
        events.append({'tracer':label,'primer_retorno_fase_t':tt,'avance_centro_hasta_retorno':zz,'vueltas_finales':float(phi[-1,i])})
    balance=float(((en[-1]-en[0])+2*j['params']['nu']*np.trapezoid(enn,t))/en[0])
    out={'N':j['params']['N'],'T':float(t[-1]),'n_muestras':len(t),'retornos_2pi':sum(z['primer_retorno_fase_t'] is not None for z in events),
         'eventos':events,'avance_centro':float(dz[-1]-dz[0]),'desfase_exterior_final_vueltas':float(dd[-1]),
         'desfase_exterior_max_vueltas':float(dd.max()),'tiempo_maximo_desfase':float(t[dd.argmax()]),
         'balance_energia_relativo_E0':balance,
         'energia_relativa_final':float(en[-1]/en[0]),'enstrofia_relativa_final':float(enn[-1]/enn[0]),
         'divergencia_maxima':j['max_divergence']}
    return out,t,phi,dd,dz

def main():
    runs={N:json.loads((BASE/f'NS{N}_T2p4.json').read_text()) for N in [40,48]}
    processed={};
    fig,ax=plt.subplots(figsize=(8.5,4.7))
    for N,j in runs.items():
        out,t,phi,dd,z=summarize(j)
        processed[N]=out
        ax.plot(t,dd,label=f'N={N} — desfase exterior 0,12 vs 0,26')
    ax.set(xlabel='Tiempo de simulación',ylabel='Desfase de fase relativa (vueltas)',title='O52 · El desfase no permanece nulo al completar las primeras vueltas')
    ax.legend(fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(BASE/'o52_desfase_largo.png',dpi=175);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8.5,4.7))
    j=runs[48];out,t,phi,dd,z=summarize(j)
    for k,label in enumerate(j['tracer_labels']): ax.plot(t,phi[:,k],label=label)
    ax.axhline(-1,color='gray',ls='--',lw=1,label='Primer cruce de −1 vuelta')
    ax.set(xlabel='Tiempo de simulación',ylabel='Fase desenrollada acumulada (vueltas)',title='O52 · Primeros cruces de fase meridiana relativa (N=48)')
    ax.legend(fontsize=7,ncol=2);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(BASE/'o52_primeras_vueltas.png',dpi=175);plt.close(fig)
    # Controles diferenciados, son chequeos de condiciones, no demostraciones generales.
    checks={}
    for N,a in processed.items():
        checks[f'{N}_5_retornos']=a['retornos_2pi']==5
        checks[f'{N}_desfase_no_nulo']=abs(a['desfase_exterior_final_vueltas'])>.1
        checks[f'{N}_desfase_no_monotono']=a['desfase_exterior_max_vueltas']>a['desfase_exterior_final_vueltas']+.05
        checks[f'{N}_energia_disipa']=a['energia_relativa_final']<1
        checks[f'{N}_enstrofia_disipa']=a['enstrofia_relativa_final']<1
        checks[f'{N}_balance_energia']=abs(a['balance_energia_relativo_E0'])<2e-5
        checks[f'{N}_divergencia']=a['divergencia_maxima']<1e-11
    checks['desplazamiento_espacial_40_48']=abs(processed[48]['avance_centro']-processed[40]['avance_centro'])<.001
    checks['desfase_espacial_40_48']=abs(processed[48]['desfase_exterior_final_vueltas']-processed[40]['desfase_exterior_final_vueltas'])<.01
    for q,r in zip(processed[40]['eventos'], processed[48]['eventos']):
        if q['primer_retorno_fase_t'] is not None and r['primer_retorno_fase_t'] is not None:
            checks[f"retorno_40_48_{q['tracer']}"]=abs(q['primer_retorno_fase_t']-r['primer_retorno_fase_t'])<.04
        else: checks[f"no_retorno_40_48_{q['tracer']}"]=(q['primer_retorno_fase_t'] is None and r['primer_retorno_fase_t'] is None)
    comparison={'resoluciones':{'40':processed[40], '48':processed[48]},'checks':checks,
                'n_checks':len(checks),'n_pass':sum(checks.values()),
                'nota':'Cruce de -2π de fase respecto al centro de enstrofía: NO equivale a retorno al mismo punto físico o período exacto de Poincaré.'}
    (BASE/'O52_RESULTADOS.json').write_text(json.dumps(comparison,indent=2,ensure_ascii=False))
    print('O52 checks',comparison['n_pass'],'/',comparison['n_checks']);
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    for N,out in processed.items():
        print(N, 'retornos',out['retornos_2pi'],'dz',out['avance_centro'],'desfase',out['desfase_exterior_final_vueltas'],'max',out['desfase_exterior_max_vueltas'])
        for ev in out['eventos']:print(' ',ev)
if __name__=='__main__':main()
