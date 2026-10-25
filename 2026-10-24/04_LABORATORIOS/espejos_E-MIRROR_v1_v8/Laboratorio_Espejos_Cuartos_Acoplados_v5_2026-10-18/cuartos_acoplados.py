"""E-MIRROR v5: dos cavidades con separador semirreflectante y pared móvil.

Modelo de rayos 1D a incidencia normal (reducido, no trazado 3D).
No hay umbral de reorganización impuesto: se barre toda la longitud B.

Ejecutar: python cuartos_acoplados.py
"""
from __future__ import annotations
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

C = 299_792_458.0
ROOT = Path(__file__).resolve().parent

@dataclass(frozen=True)
class Config:
    length_A_m: float=2.0
    length_B_min_m: float=0.35
    length_B_max_m: float=2.0
    step_B_m: float=0.001
    R: float=0.08       # vidrio de dos caras aprox.; modelo efectivo, sin interferencia de la lámina
    M: float=0.95       # intensidad preservada en espejo del fondo
    pulse_sigma_ns: float=0.12
    max_returns: int=8


def round_trip_ns(length_m: float) -> float:
    return 2.0 * length_m / C * 1e9


def echo_intensity(n: int, R: float, M: float=0.95) -> float:
    """Intensidad de la familia que NO cambia de cavidad hasta salir por vidrio.
    Excitación inicial unitaria en la cavidad, n espejos del fondo, n-1 rebotes en vidrio,
    salida por vidrio con T=1-R. No suma familias con cambios de cavidad.
    """
    if n < 1 or not (0 <= R <= 1) or not (0 <= M <= 1):
        raise ValueError('parámetros inválidos')
    return (1-R) * M**n * R**(n-1)


def simple_pair_weights(cfg: Config):
    return [(p,q,float(np.sqrt(echo_intensity(p,cfg.R,cfg.M)*echo_intensity(q,cfg.R,cfg.M))))
            for p in range(1,cfg.max_returns+1) for q in range(1,cfg.max_returns+1)]


def coincidence_profile(length_B: np.ndarray, cfg: Config):
    """Score de superposición temporal de familias de eco; unidades relativas.
    Sin fases ópticas ni refuerzos constructivos asumidos.
    """
    L_B = np.asarray(length_B,dtype=float)
    prof = np.zeros_like(L_B)
    for p,q,weight in simple_pair_weights(cfg):
        delta_ns = p*round_trip_ns(cfg.length_A_m) - q*(2*L_B/C*1e9)
        prof += weight * np.exp(-0.5*(delta_ns/cfg.pulse_sigma_ns)**2)
    return prof


def low_order_resonances(cfg: Config):
    vals=[]
    for q in range(1,cfg.max_returns+1):
        for p in range(1,cfg.max_returns+1):
            f=Fraction(p,q)
            if f.numerator!=p or f.denominator!=q: continue
            L=cfg.length_A_m*p/q
            if not (cfg.length_B_min_m<=L<=cfg.length_B_max_m): continue
            ia=echo_intensity(p,cfg.R,cfg.M)
            ib=echo_intensity(q,cfg.R,cfg.M)
            vals.append(dict(p=p,q=q,ratio=p/q,length_B_m=L,
                             period_A_ns=p*round_trip_ns(cfg.length_A_m),
                             period_B_ns=q*round_trip_ns(L),
                             intensity_A=ia,intensity_B=ib,
                             pair_weight=np.sqrt(ia*ib),
                             end_mirror_parity_A='par' if p%2==0 else 'impar',
                             end_mirror_parity_B='par' if q%2==0 else 'impar',
                             all_reflections_A=2*p-1,all_reflections_B=2*q-1,
                             complete_reflection_parity_A='impar',complete_reflection_parity_B='impar'))
    return sorted(vals,key=lambda x: (-x['pair_weight'],x['q']))


def paths_for_coupled_rooms(LA=2.0, LB=1.0, R=0.5, M=0.95, depth=6):
    """Enumera trayectorias de amplitud en vidrio semirreflectante compartido.
    Salimos desde cavidad A (amplitud 1). Cada ida-vuelta hasta divisor añade una
    reflexión en espejo del fondo; en cada encuentro intermedio con vidrio podemos
    reflejar (misma cavidad, +1 inversión) o transmitir (cambiar cavidad, +0).
    Resultado: historial de retornos sin sensor, no intensidad detectada.
    """
    if not (0 <= R <= 1 and 0 <= M <= 1): raise ValueError()
    histories=[]
    # lado, tiempo, amplitud, espejos, refl_vidrio, transmisiones, cadena
    branches=[('A',0.,complex(1.,0.),0,0,0,'')]
    for cycle in range(1,depth+1):
        new=[]
        for side,time,amplitude,mirs,glrefl,trans,path in branches:
            length=LA if side=='A' else LB
            t2=time+round_trip_ns(length)
            a2=amplitude*(-np.sqrt(M))  # fase pi espejo ideal y absorción M
            item=dict(cycle=cycle,side=side,time_ns=t2,
                      amplitude_real=float(a2.real),amplitude_imag=float(a2.imag),
                      intensity_path=float(abs(a2)**2),end_mirror_reflections=mirs+1,
                      pane_reflections=glrefl,transmissions=trans,
                      total_reflections=mirs+1+glrefl,
                      reflection_parity='impar' if (mirs+1+glrefl)%2 else 'par',
                      path=path+side)
            histories.append(item)
            if cycle<depth:
                # Reflejo en vidrio: retorno a la misma cavidad.
                new.append((side,t2,a2*np.sqrt(R),mirs+1,glrefl+1,trans,path+side))
                # Transmisión por vidrio: entra en la otra cavidad; desfase 90°.
                new.append(('B' if side=='A' else 'A',t2,a2*1j*np.sqrt(1-R),
                            mirs+1,glrefl,trans+1,path+side))
        branches=new
    return histories


def plot_results(cfg, scan, signal, peaks, ratios, output=ROOT):
    plt.rcParams.update({'font.size':10})
    fig,ax=plt.subplots(figsize=(12,4.8))
    ax.plot(scan,signal,linewidth=1.6)
    ax.set_xlabel('Profundidad B (m), A = 2 m')
    ax.set_ylabel('Solapamiento temporal relativo')
    ax.set_title('Barrido sin imponer la mitad: retornos coincidentes')
    ax.grid(alpha=.2)
    for d in ratios[:11]:
        L=d['length_B_m']
        if .35<=L<=2.0:
            idx=np.argmin(abs(scan-L))
            if signal[idx]>0.002:
                ax.annotate(f"{d['p']}:{d['q']}",(L,float(signal[idx])),
                            textcoords='offset points',xytext=(1,5),fontsize=8,rotation=30)
    fig.tight_layout(); fig.savefig(output/'01_barrido_completo.png',dpi=155); plt.close(fig)

    fig,ax=plt.subplots(figsize=(10,4.6))
    sub=(scan>=.88)&(scan<=1.12)
    ax.plot(scan[sub],signal[sub])
    ax.axvline(1.0,linestyle='--',linewidth=1.5,label='B = A/2 (1:2)')
    ax.grid(alpha=.22);ax.legend()
    ax.set_xlabel('Profundidad B (m)');ax.set_ylabel('Solapamiento temporal relativo')
    ax.set_title('Cercanía de la mitad: pico finito, no discontinuidad')
    fig.tight_layout();fig.savefig(output/'02_entorno_mitad.png',dpi=155);plt.close(fig)

    fig,axs=plt.subplots(2,1,figsize=(9,6.8),sharex=True)
    x=np.arange(1,cfg.max_returns+1)
    for name,r in [('Vidrio claro (R=0,08)',.08),('Vidrio semiespejado (R=0,50)',.5)]:
        axs[0].plot(x,[echo_intensity(n,r,cfg.M) for n in x],marker='o',label=name)
    axs[0].set_yscale('log');axs[0].set_ylabel('Intensidad de la familia de eco')
    axs[0].set_title('Qué rebotes quedan accesibles según el vidrio')
    axs[0].legend();axs[0].grid(alpha=.2)
    axs[1].bar(x,[1 if n%2 else 0 for n in x],alpha=.65,label='Paridad solo del espejo del fondo')
    axs[1].plot(x, [1]*len(x),'o-',label='Paridad de todas las reflexiones (impar)')
    axs[1].set_yticks([0,1],labels=['par','impar'])
    axs[1].set_xlabel('Índice del retorno n')
    axs[1].set_title('La paridad cambia según QUÉ reflexiones se cuentan')
    axs[1].legend(fontsize=8);axs[1].grid(alpha=.2)
    fig.tight_layout();fig.savefig(output/'03_eco_y_paridad.png',dpi=155);plt.close(fig)

    fig,ax=plt.subplots(figsize=(10,4.8))
    for R in [.08,.5,.75]:
        cc=Config(R=R)
        zz=coincidence_profile(scan,cc)
        ax.plot(scan,zz,label=f'R={R:.2f}',linewidth=1.4)
    ax.set_xlabel('Profundidad B (m)'); ax.set_ylabel('Solapamiento temporal relativo')
    ax.set_title('El vidrio regula visibilidad; la geometría fija las proporciones')
    ax.legend();ax.grid(alpha=.2);fig.tight_layout()
    fig.savefig(output/'04_efecto_vidrio.png',dpi=155);plt.close(fig)


def main():
    cfg=Config()
    scan=np.round(np.arange(cfg.length_B_min_m,cfg.length_B_max_m+cfg.step_B_m/2,cfg.step_B_m),6)
    signal=coincidence_profile(scan,cfg)
    peaks_idx, props=find_peaks(signal,prominence=.0002,distance=8)
    peaks=sorted([{'length_B_m':float(scan[i]),'score':float(signal[i]),
                  'prominence':float(props['prominences'][j])}
                 for j,i in enumerate(peaks_idx)],key=lambda x:-x['prominence'])
    ratios=low_order_resonances(cfg)
    plot_results(cfg,scan,signal,peaks,ratios)
    path_half=paths_for_coupled_rooms(LB=1.0,R=0.5,depth=7)
    path_irr=paths_for_coupled_rooms(LB=np.sqrt(2),R=0.5,depth=7)
    summary={
       'modelo':'dos brazos unidimensionales con vidrio semirreflectante, ecos sin cambio de brazo',
       'supuestos':{'A_m':cfg.length_A_m,'B_min_m':cfg.length_B_min_m,
                    'B_max_m':cfg.length_B_max_m,'paso_m':cfg.step_B_m,
                    'R_vidrio_intensidad':cfg.R,'M_espejos_intensidad':cfg.M,
                    'sigma_temporal_ns':cfg.pulse_sigma_ns,'max_retorno':cfg.max_returns},
       'resonancias_de_orden_bajo':ratios,
       'picos_barrido_por_prominencia':peaks[:30],
       'punto_mitad':{'B_m':1.0,'A_recorridos':1,'B_recorridos':2,
                      'retorno_A_ns':round_trip_ns(2),
                      'retorno_B_dos_ns':2*round_trip_ns(1),
                      'eco_A':echo_intensity(1,cfg.R,cfg.M),
                      'eco_B':echo_intensity(2,cfg.R,cfg.M),
                      'score_total':float(signal[np.argmin(abs(scan-1))])},
       'ancho_cercano_mitad_1sigma_m':(C*cfg.pulse_sigma_ns*1e-9)/(2*2),
       'control_vidrio_opaco':{'R':1.0,'T':0.0,'intensidad_transmitida':echo_intensity(1,1.0,cfg.M)},
       'rutas_acopladas_1m_7pasos':path_half,
       'rutas_acopladas_sqrt2m_7pasos':path_irr,
    }
    (ROOT/'resultados_v5.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print('V5 perfil:',len(scan),'posiciones;','picos:',len(peaks),'racionales:',len(ratios))
    print('Picos de mayor prominencia:',peaks[:10])
    print('Resonancias de mayor peso:',[(x['p'],x['q'],round(x['length_B_m'],5),round(x['pair_weight'],6)) for x in ratios[:10]])
    print('Punto mitad',summary['punto_mitad'])
    print('Rutas de red acoplada:',len(path_half))

if __name__=='__main__': main()
