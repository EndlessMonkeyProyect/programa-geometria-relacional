"""Controles de reflectividad, ancho de pulso, paridad y fuente inicial."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from espejos_v6 import Setup,C,histories,gated_fields

ROOT=Path(__file__).resolve().parent

def main():
    dataset=[]
    for R in [.02,.08,.20,.35,.5,.8]:
        for sig in [.06,.12,.25]:
            s=Setup(R=R,sigma_ns=sig)
            t=2*s.A/C*1e9
            x=gated_fields(s,t)
            dataset.append(dict(R=R,sigma_ns=sig,I_min=float(x['min_posible']),
                                I_max=float(x['max_posible']),I_incoh=float(x['incoherente']),
                                contraste=float((x['max_posible']-x['min_posible'])/(x['max_posible']+x['min_posible']))))
    tests=[]
    for source in ['A','both']:
        h=histories(Setup(depth=6),source)
        sides={s: {str(p):len([x for x in h if x['side']==s and x['reflection_parity']==p and abs(x['amplitude'])>1e-15]) for p in [0,1]} for s in ['A','B']}
        tests.append({'fuentes':source,'paridades_cantidad':sides})
    fig,axs=plt.subplots(1,2,figsize=(12,4.3))
    for sig in [.06,.12,.25]:
        arr=[q for q in dataset if q['sigma_ns']==sig]
        axs[0].plot([q['R'] for q in arr],[q['contraste'] for q in arr],marker='o',label=f'sigma={sig} ns')
    axs[0].set(xlabel='Reflectividad del divisor',ylabel='Visibilidad coherente (contraste)',title='Control: cambiar el vidrio')
    axs[0].legend();axs[0].grid(alpha=.2)
    s=Setup()
    t=2*s.A/C*1e9
    h=[x for x in histories(s) if abs(x['time_ns']-t)<1e-7]
    labs=['Retorno A: 1 visita','Retorno B: 2 visitas']
    counts=[x['reflection_count'] for x in h]
    axs[1].bar(labs,counts)
    axs[1].set(ylabel='Reflexiones totales',title='A igual tiempo no implica igual historia')
    axs[1].set_yticks([0,1,2,3,4]);axs[1].grid(axis='y',alpha=.2)
    fig.tight_layout();fig.savefig(ROOT/'04_paridad_y_robustez.png',dpi=155);plt.close(fig)
    # Subescala de fase: microfranjas alrededor de B=1 m (camino B de 2 retornos).
    central=gated_fields(Setup(), 2*Setup().A/C*1e9)
    ds=np.linspace(-3*Setup().wavelength_m/4,3*Setup().wavelength_m/4,901)
    E_a=central['E_A']; E_b=central['E_B']
    fringe=np.abs((E_a+E_b*np.exp(2j*np.pi*4*ds/Setup().wavelength_m))/np.sqrt(2))**2
    fig,ax=plt.subplots(figsize=(10,4.5))
    ax.plot(ds*1e9,fringe)
    ax.set(xlabel='Desplazamiento respecto a B=1 m (nanómetros)',ylabel='Intensidad relativa',
           title='Escala de fase: período de 158,25 nm para un retorno doble en B')
    ax.grid(alpha=.2);fig.tight_layout();fig.savefig(ROOT/'05_franjas_subescala.png',dpi=155);plt.close(fig)
    summary={'R_sigma':dataset,'periodo_subescala_fase_m':Setup().wavelength_m/4,'paridades':tests,'coincidencias_t0':[
        {'lado':x['side'],'visitas':x['visits'],'reflexiones':x['reflection_count'],
         'paridad':'impar' if x['reflection_parity'] else 'par',
         'cruces_vidrio':x['transmissions']} for x in h]}
    (ROOT/'controles_v6.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print('18 controles; paridad a t0:',summary['coincidencias_t0'])
    for x in dataset:
        if x['sigma_ns']==.12: print(x)

if __name__=='__main__':main()
