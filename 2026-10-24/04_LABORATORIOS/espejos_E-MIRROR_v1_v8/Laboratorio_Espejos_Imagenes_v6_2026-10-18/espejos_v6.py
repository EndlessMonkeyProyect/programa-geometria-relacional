"""E-MIRROR v6. Cavidades acopladas: rayos finitos y respuesta coherente/incoherente.

El sensor espacial es una cámara de barrido temporal (eje y, tiempo), NO foto común.
Para la onda se utiliza una aproximación de modo transversal único, con dos
entradas coherentes y lectura por combinador óptico externo.
Este archivo es ejecutable y reproduce los gráficos y datos.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

C=299_792_458.0
ROOT=Path(__file__).resolve().parent
@dataclass(frozen=True)
class Setup:
    A: float=2.0
    B: float=1.0
    R: float=0.35
    M: float=0.95
    tap: float=0.02  # puerto de medida débil de ambas cavidades
    aperture: float=0.30  # semianchura de espejos y vidrio
    y0: float=0.012
    depth: int=8
    sigma_ns: float=0.12
    wavelength_m: float=633e-9


def histories(s:Setup, launch='both'):
    """Bifurca el campo 1D ideal, contabiliza retorno previo al divisor.
    Cada visita al espejo M agrega fase pi y recorrido 2L.
    Pane: reflexión r=sqrt(R), transmisión it=i sqrt(1-R).
    En cada llegada al vidrio, el sensor extrae una amplitud sqrt(tap)
    y las ramas sobrevivientes llevan sqrt(1-tap).
    """
    if not (0<=s.R<=1 and 0<=s.M<=1 and 0<=s.tap<1): raise ValueError()
    if s.A<=0 or s.B<=0: raise ValueError()
    seeds={'A':1+0j} if launch=='A' else {'A':2**-.5+0j,'B':2**-.5+0j}
    active=[(k,0.0,amp,0,0,0,0.0,k) for k,amp in seeds.items()]
    out=[]
    for cycle in range(1,s.depth+1):
        nxt=[]
        for side,L,amp,N,K,P,last,path in active:
            length=s.A if side=='A' else s.B
            L2=L+2*length
            amp2=amp*(-np.sqrt(s.M))
            record=dict(side=side,length_m=L2,time_ns=L2/C*1e9,
                        amplitude=amp2*np.sqrt(s.tap),visits=N+1,
                        transmissions=K,pane_reflections=P,
                        reflection_count=N+1+P,
                        reflection_parity=(N+1+P)%2,path=path+side)
            out.append(record)
            if cycle<s.depth:
                q=amp2*np.sqrt(1-s.tap)
                if abs(q*np.sqrt(s.R))>1e-15:
                    nxt.append((side,L2,q*np.sqrt(s.R),N+1,K,P+1,last,path+side))
                if abs(q*np.sqrt(1-s.R))>1e-15:
                    nxt.append(('B' if side=='A' else 'A',L2,q*1j*np.sqrt(1-s.R),N+1,K+1,P,last,path+side))
        active=nxt
    return out


def gated_fields(s:Setup, t_ns:float, phi:float=0, source='both'):
    """Campo en dos canales, posible recombinación coherente.
    La fase relativa de un combinador sobre el canal B es phi.
    """
    h=histories(s,source)
    Ea=0j; Eb=0j; incoh=0.0
    for x in h:
        gate=np.exp(-.5*((t_ns-x['time_ns'])/s.sigma_ns)**2)
        field=x['amplitude']*gate*np.exp(2j*np.pi*((x['length_m']%s.wavelength_m)/s.wavelength_m))
        if x['side']=='A': Ea+=field
        else: Eb+=field
        incoh+=abs(x['amplitude']*gate)**2
    # Factor 1/2 del combinador de dos entradas; sensor incoherente se escala igual
    return {'E_A':Ea,'E_B':Eb,'coherente':abs((Ea+np.exp(1j*phi)*Eb)/np.sqrt(2))**2,
            'incoherente':incoh/2,'min_posible':(abs(Ea)-abs(Eb))**2/2,
            'max_posible':(abs(Ea)+abs(Eb))**2/2}


def geometric_return_paths(s:Setup, angles_rad:np.ndarray, source='both'):
    """Óptica de rayos 2D con superficies planas FINITAS.
    Emisor en vidrio (y0); rayos desde el separador a los dos espejos.
    El campo transversal deriva monotónicamente en cada ida y vuelta.
    Devuelve las intersecciones con el plano detector de vidrio (tap).
    """
    d={}
    starts=('A','B') if source=='both' else ('A',)
    for theta in angles_rad:
        slope=np.tan(theta)
        gauss=np.exp(-.5*(theta/np.deg2rad(3))**2)
        for initial in starts:
            branches=[(initial,s.y0,0.0,1.0/len(starts),0,0,0)]
            for cyc in range(s.depth):
                new=[]
                for side,y,t,w,ref,trans,vis in branches:
                    L=s.A if side=='A' else s.B
                    ym=y+L*slope
                    yr=ym+L*slope
                    if abs(ym)>s.aperture or abs(yr)>s.aperture: continue
                    t2=t+2*L/C*1e9
                    w2=w*s.M
                    key=(side,t2,round(float(yr),7),ref+1,trans,vis+1)
                    d[key]=d.get(key,0.0)+w2*gauss*s.tap
                    if cyc<s.depth-1:
                        remaining=w2*(1-s.tap)
                        if remaining*s.R>1e-15:
                            new.append((side,yr,t2,remaining*s.R,ref+2,trans,vis+1))
                        if remaining*(1-s.R)>1e-15:
                            new.append(('B' if side=='A' else 'A',yr,t2,remaining*(1-s.R),ref+1,trans+1,vis+1))
                branches=new
    return [{'side':k[0],'time_ns':k[1],'y_m':k[2],
             'reflection_parity':k[3]%2,'transmissions':k[4],
             'visits':k[5],'weight':v} for k,v in d.items()]


def streak_image(s:Setup, angles=101, time_max=48, t_bins=520, y_bins=140):
    """Cámara de barrido temporal idealizada: brillo vs llegada y lateral.
    Captura el flujo por un detector en cada lado, sin interferencia ni difracción.
    """
    ang=np.linspace(-np.deg2rad(8),np.deg2rad(8),angles)
    rows=geometric_return_paths(s,ang)
    imgs={}
    for side in ('A','B'):
        item=[r for r in rows if r['side']==side and r['time_ns']<=time_max]
        H,_,_=np.histogram2d([r['y_m'] for r in item],
                            [r['time_ns'] for r in item],
                            bins=[np.linspace(-s.aperture,s.aperture,y_bins+1),np.linspace(0,time_max,t_bins+1)],
                            weights=[r['weight'] for r in item])
        imgs[side]=gaussian_filter(H,sigma=(1.15,1.15))
    return imgs,rows


def make_figures(out=ROOT):
    out.mkdir(exist_ok=True,parents=True)
    s=Setup()
    samples=[.667,1.0,np.sqrt(2),1.5]
    fig,axs=plt.subplots(2,4,figsize=(15.5,6.8),sharex=True,sharey=True)
    ray_summary=[]
    for j,b in enumerate(samples):
        sn=Setup(B=b)
        cam,rows=streak_image(sn)
        ray_summary.append({'B':float(b),'trayectorias_pesadas':len(rows),
                            'total_registro':float(sum(cam[k].sum() for k in cam)),
                            'vistas':{k:float(v.sum()) for k,v in cam.items()}})
        for i,side in enumerate(['A','B']):
            x=cam[side]
            axs[i,j].imshow(np.log10(x+1e-8),origin='lower',aspect='auto',
                            extent=[0,48,-sn.aperture,sn.aperture],vmin=-8,vmax=-2.5)
            axs[i,j].set_title(f'B={b:.3f}m · retorno {side}')
            axs[i,j].set_xlabel('Tiempo (ns)')
            axs[i,j].set_ylabel('y vidrio (m)')
    fig.suptitle('Cámara temporal 2D: rayos válidos con vidrio y espejos finitos',y=1.01)
    fig.tight_layout();fig.savefig(out/'01_camara_temporal_2D.png',dpi=155,bbox_inches='tight');plt.close(fig)

    # Barrido de la región B=A/2, respuesta registrada con mezcla de dos canales.
    t0=2*s.A/C*1e9
    Bs=np.arange(.90,1.101,.001)
    incoh=[]; maxc=[]; minc=[]; fixed=[]
    for B in Bs:
        e=gated_fields(Setup(B=float(B)),t0,phi=0)
        incoh.append(e['incoherente']);maxc.append(e['max_posible'])
        minc.append(e['min_posible']);fixed.append(e['coherente'])
    fig,ax=plt.subplots(figsize=(10.5,5.0))
    ax.plot(Bs,incoh,label='Suma incoherente de historias')
    ax.plot(Bs,maxc,'--',label='Máximo coherente con fase ajustada')
    ax.plot(Bs,minc,':',label='Mínimo coherente con fase ajustada')
    ax.axvline(1.0,ls='--',lw=.9)
    ax.set(xlabel='Profundidad B (m)',ylabel='Señal de retorno (unidades relativas)',
           title='Un encuentro de recorridos no obliga al máximo de brillo')
    ax.legend(fontsize=9);ax.grid(alpha=.22)
    fig.tight_layout();fig.savefig(out/'02_interferencia_en_mitad.png',dpi=155);plt.close(fig)

    # A B=1m, barrido de fase del combinador: el mismo retraso, distintas señales.
    phis=np.linspace(0,2*np.pi,251)
    cs=[gated_fields(s,t0,phi=p)['coherente'] for p in phis]
    incoh0=gated_fields(s,t0)['incoherente']
    fig,ax=plt.subplots(figsize=(10,4.6))
    ax.plot(phis/np.pi,cs,label='Dos canales recombinados coherentemente')
    ax.axhline(incoh0,ls='--',label='Suma incoherente de historias')
    ax.set(xlabel='Fase adicional en canal B (múltiplos de π)',ylabel='Señal detectada (u.r.)',
           title='Misma geometría B = 1m, distinto brillo por interferencia')
    ax.grid(alpha=.22);ax.legend();fig.tight_layout()
    fig.savefig(out/'03_fase_y_observabilidad.png',dpi=155);plt.close(fig)

    # Comparación de paridad: fracción de retornos que tienen reflectividades totales impares/par.
    par_summary=[]
    for B in samples:
        ss=Setup(B=float(B))
        hr=histories(ss,'A')
        for side in ['A','B']:
            r=[x for x in hr if x['side']==side]
            counts={str(k):len([x for x in r if x['reflection_parity']==k]) for k in [0,1]}
            par_summary.append({'B':float(B),'side':side,'paridades_0par_1impar':counts})
    results={'setup':s.__dict__,'tiempo_referencia_ns':t0,'camera':ray_summary,
             'sweep':{'B_m':Bs.tolist(),'intensidad_incoherente':incoh,
                      'min_coherente':minc,'max_coherente':maxc},
             'punto_mitad':{'min':float(min(cs)),'max':float(max(cs)),
                            'sin_fase':float(incoh0),'señal_fase_cero':float(cs[0])},
             'paridades':par_summary,
             'regla': 'Con fuente en A, lado de llegada A <=> transmisiones pares; B <=> impares',
             'limites':['Sensor espacial: rayos especulares bidimensionales con vidrio ideal sin refraccion y espejo finito',
                        'Sensor de interferencia: modo escalar unico, fases de interfaz ideal y mezcla calibrada externa',
                        'No se combinan el resultado de rayos con el de fase en un único detector electromagnetico',
                        'El barrido de 1mm no resuelve franjas opticas de ~158 nanometros para el retorno B doble',
                        'Se incluyen todos los caminos truncados en profundidad, no la solución de onda continua completa']}
    (out/'resultados_v6.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print('MITAD',results['punto_mitad'])
    print('CAMARA',ray_summary)
    return results

if __name__=='__main__': make_figures()
