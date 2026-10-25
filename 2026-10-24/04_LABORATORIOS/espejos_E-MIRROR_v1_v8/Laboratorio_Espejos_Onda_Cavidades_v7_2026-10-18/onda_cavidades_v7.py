#!/usr/bin/env python3
"""E-MIRROR v7: cavidades 1D con espejos ideales y hoja reactiva sin pérdidas.
Coordenadas normalizadas por lambda0 (a=1), q=k/k0, k0=2*pi.
Campo transversal escalar a incidencia normal, E''+k^2 E=-F delta(x-xs).
E=0 en extremos, E continua en divisor, E'_+ - E'_- = g*E.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
A=1.0
K0=2*np.pi
XS=0.23

def sheet_g(R:float,k_ref:float=K0)->float:
    if not (0 <= R < 1): raise ValueError('Reflectividad en [0,1)')
    return float(2*k_ref*np.sqrt(R/(1-R)))

def rt(k:float,g:float):
    r=g/(2j*k-g)
    t=2j*k/(2j*k-g)
    return r,t

def determinant(k:complex,b:float,g:float,a:float=A):
    return k*np.sin(k*(a+b))+g*np.sin(k*a)*np.sin(k*b)

def green_cross(k:complex,b:float,g:float,x_src:float=XS,x_bfrac:float=0.5):
    # Fuente en A; medida en B a x=a + x_bfrac*b. E normalizada F=1
    assert 0<x_src<A and 0<x_bfrac<1
    return np.sin(k*x_src)*np.sin(k*(1-x_bfrac)*b) / determinant(k,b,g)

def green_interface(k:complex,b:float,g:float,x_src:float=XS):
    return np.sin(k*x_src)*np.sin(k*b)/determinant(k,b,g)

def eigen_roots(b:float,g:float,q_lo:float=0.62,q_hi:float=1.66,n_samples:int=3500):
    grid=np.linspace(q_lo,q_hi,n_samples)
    vals=np.real(determinant(K0*grid,b,g))
    roots=[]
    for i in range(grid.size-1):
        if vals[i]==0:
            root=grid[i]
        elif vals[i]*vals[i+1] < 0:
            root=brentq(lambda q: float(np.real(determinant(K0*q,b,g))),grid[i],grid[i+1],xtol=1e-13)
        else:
            continue
        if root>1e-8 and (not roots or abs(root-roots[-1])>1e-7): roots.append(root)
    return roots

def mode_shape(q:float,b:float,g:float,n_pts:int=501):
    """E_1=A sin(kx), E_2=B sin(k(T-x)); use derivative at divider to find B if node."""
    k=K0*q
    sA=np.sin(k*A);sB=np.sin(k*b)
    if abs(sB)>1e-8:
        ratio=sA/sB
    elif abs(np.cos(k*b))>1e-8:
        ratio=-(np.cos(k*A)+g*sA/k)/np.cos(k*b)
    else:
        raise ValueError('ill-conditioned mode shape')
    x=np.linspace(0,A+b,n_pts)
    e=np.where(x<=A,np.sin(k*x),ratio*np.sin(k*(A+b-x)))
    dx=x[1]-x[0]
    norm=np.sqrt(np.trapezoid(e*e,x))
    return x,e/norm,ratio

def data_and_charts():
    g_nom=sheet_g(.5)
    # Mode spectrum for changing B, five modes nearby
    bs=np.linspace(.27,.99,145)
    spec=[]
    for b in bs:
        for j,q in enumerate(eigen_roots(float(b),g_nom,q_lo=.10)):
            if q >= .62: spec.append((b,q,j))
    # Fixed light frequency response; weak homogeneous absorption via complex k
    eta=0.003
    kcomplex=K0*(1+1j*eta)
    sweep=np.linspace(.25,.97,1441)
    curves={}
    for r in [0.0,.25,.5,.9]:
        g=sheet_g(r)
        curves[r]=np.array([abs(green_cross(kcomplex,b,g))**2 for b in sweep])
    # Search resonances including protected common node in 1:2 ratio
    pivot={}
    for r in [0,.25,.5,.9]:
        g=sheet_g(r)
        roots=eigen_roots(.5,g,.8,1.33)
        nearest=min(roots,key=lambda q: abs(q-1))
        pivot[str(r)]={'g_lambda_inv':g,'eigen_q_near_1':nearest,
                       'determinant_at_q1_bhalf':float(np.real(determinant(K0,.5,g))),
                       'green_B_abs2_at_half_lossy':float(abs(green_cross(kcomplex,.5,g))**2)}
    # Critical comparison other rational returns, spectral condition for protected node
    rationals=[(.5,2,1), (2/3,3,2),(.75,4,3),(.4,5,2),(.6,5,3)]
    commensurate=[]
    for b,p,m in rationals:
        q=p/2 # A=1 ; k= p*pi, q=p/2
        node=abs(np.sin(K0*q*A))<1e-12 and abs(np.sin(K0*q*b))<1e-12
        commensurate.append({'b_over_a':b,'longitudinal_index_A':p,'longitudinal_index_B':m,
                            'lowest_common_q':q,'matches_q0_1':abs(q-1)<1e-10,
                            'node_at_sheet':bool(node),
                            'relative_sign_B_over_A_at_common_node':int((-1)**(p+m+1))})
    # Plot 1. band structure vs change in second cavity
    fig,ax=plt.subplots(figsize=(10,6))
    sb=np.array(spec)
    for j in sorted(set(sb[:,2].astype(int))):
        group=sb[sb[:,2]==j]
        ax.plot(group[:,0],group[:,1],lw=1.6,label=f'Modo longitudinal {j+1}' if j<4 else None)
    ax.axvline(.5,color='black',ls='--',lw=1.25,label='B/A=1/2')
    ax.axhline(1,color='gray',ls=':',lw=1.5,label='Luz fijada: q=1')
    ax.scatter([.5],[1],c='black',s=65,zorder=10)
    ax.set(xlabel='Profundidad B / longitud de onda de referencia',
           ylabel='Frecuencia del modo / frecuencia de referencia',
           title='Modos de dos cavidades acopladas al mover la pared (R=50 % a q=1)',ylim=(.62,1.66))
    ax.legend(fontsize=8,ncol=2,loc='upper right')
    fig.tight_layout();fig.savefig(HERE/'01_modos_pared_movil.png',dpi=165);plt.close(fig)
    # Plot 2. detected signal
    fig,ax=plt.subplots(figsize=(10,5.4))
    for r,v in curves.items():
        ax.plot(sweep,v,label=f'Reflectividad hoja {r:.0%} a q=1')
    ax.axvline(.5,color='black',ls='--',label='Mitad (B=λ/2)')
    ax.set(xlabel='Profundidad B / λ',ylabel='Intensidad en B (unidades arbitrarias)',
           title='Señal estacionaria en B para una onda monocromática a q=1 (amortiguación fija)',yscale='log')
    ax.legend(fontsize=9);fig.tight_layout();fig.savefig(HERE/'02_senal_frecuencia_fija.png',dpi=165);plt.close(fig)
    # Plot 3. protected eigenfunction and sheet; at k0, node exactly for any g
    fig,ax=plt.subplots(figsize=(10,4.7))
    x,y,ratio=mode_shape(1.0,.5,g_nom)
    ax.plot(x,y,label='Modo exacto q=1; R=50 %',lw=2.2)
    ax.axvline(1,color='black',lw=1.7,ls='--',label='Divisor parcialmente reflectante')
    ax.axhline(0,color='gray',lw=.8)
    ax.fill_between(x,0,y,where=(x<=1),alpha=.1)
    ax.fill_between(x,0,y,where=(x>=1),alpha=.1)
    ax.scatter([1],[0],color='red',s=55,zorder=4,label='Nodo protegido: E(divisor)=0')
    ax.set(xlabel='Coordenada x / λ',ylabel='Campo E normalizado (signo = fase)',
           title='Una onda atraviesa dos cuartos de distinta escala manteniendo un nodo común')
    ax.legend(fontsize=9);fig.tight_layout();fig.savefig(HERE/'03_modo_nodo_comun.png',dpi=165);plt.close(fig)
    # Plot 4. fixed k geometry detuning and alignment of node
    fig,axs=plt.subplots(2,1,figsize=(10,7),sharex=True)
    b_local=np.linspace(.42,.58,801)
    for r in [.0,.25,.5,.9]:
        g=sheet_g(r)
        D=np.array([abs(determinant(K0,b,g)) for b in b_local])
        axs[0].plot(b_local,D,label=f'R={r:.0%}')
    axs[0].set(ylabel='|D(k₀)|',title='Condición de modo a frecuencia fija: cero exacto en la mitad')
    axs[0].legend(ncol=4,fontsize=9)
    for r in [.25,.5,.9]:
        g=sheet_g(r)
        e=np.array([abs(green_interface(K0*(1+1j*eta),b,g)) for b in b_local])
        axs[1].plot(b_local,e,label=f'R={r:.0%}')
    axs[1].set(xlabel='Profundidad B / λ',ylabel='Amplitud E sobre el vidrio (excitado, con pérdidas)')
    for ax in axs: ax.axvline(.5,color='black',ls='--',lw=1)
    fig.tight_layout();fig.savefig(HERE/'04_nodo_y_respuesta_vidrio.png',dpi=165);plt.close(fig)
    # plot 5 reflectivity frequency dependent
    qs=np.linspace(.6,1.5,300)
    fig,ax=plt.subplots(figsize=(9,4.4))
    for r in [.25,.5,.9]:
        g=sheet_g(r)
        rr=np.array([abs(rt(float(q*K0),g)[0])**2 for q in qs])
        ax.plot(qs,rr,label=f'R(q=1)={r:.0%}')
    ax.axvline(1,color='gray',ls=':');ax.set(xlabel='Frecuencia / referencia',ylabel='Reflectividad energética',
         title='La hoja ideal tiene reflectividad dependiente de frecuencia',ylim=(0,1))
    ax.legend();fig.tight_layout();fig.savefig(HERE/'05_vidrio_y_frecuencia.png',dpi=165);plt.close(fig)
    # Plot 6. parity controls spatial sign across the interface for common-node modes.
    fig,axes=plt.subplots(3,1,figsize=(10,8.4),sharex=False)
    for ax,(b,p,m) in zip(axes,[(.5,2,1),(2/3,3,2),(.6,5,3)]):
        q=p/2
        x,e,ratio=mode_shape(q,b,g_nom,n_pts=1501)
        ax.plot(x,e,lw=1.7,color='#3667A4')
        ax.axvline(1,color='black',ls='--',lw=1)
        ax.axhline(0,color='gray',lw=.7)
        ax.set(xlim=(0,1+b),ylabel='E normalizado',title=f'B/A={b:.4g} | (nA,nB)=({p},{m}) | q={q:g} | signo relativo={ratio:+.0f}')
    axes[-1].set_xlabel('Posición x / longitud de onda inicial')
    fig.suptitle('Paridad de los modos con nodo compartido: no todos conservan el mismo signo',fontsize=14)
    fig.tight_layout();fig.savefig(HERE/'06_paridad_de_modos_comunes.png',dpi=165);plt.close(fig)
    # write data
    with (HERE/'barrido_campo_v7.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.writer(f);w.writerow(['B_sobre_lambda','I_R0','I_R25','I_R50','I_R90'])
        for i,b in enumerate(sweep): w.writerow([f'{b:.7f}',*[f'{curves[r][i]:.12g}' for r in [0,.25,.5,.9]]])
    with (HERE/'modos_v7.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.writer(f);w.writerow(['B_sobre_lambda','frecuencia_q','orden_en_ventana'])
        for row in spec:w.writerow([f'{row[0]:.7f}',f'{row[1]:.12g}',int(row[2])])
    outcome={'units':'longitud normalizada λ0=1, frecuencia q=k/k0',
             'model':'1D Maxwell transverse-E idealized as Helmholtz + conservative reactive sheet, PEC ends',
             'g_nominal_R50':g_nom,'source_x':XS,'loss_k_imag_fraction':eta,
             'mode_protected_at_B_half':pivot,
             'commensurate_nodal_modes':commensurate,
             'mode_half_shape_right_over_left':ratio,
             'mode_half_node_E':0.0,
             'mode_half_energy_fraction_A':2/3,'mode_half_energy_fraction_B':1/3,
             'max_detected_signal_by_R':{str(r):{'B':float(sweep[np.argmax(v)]),'I':float(np.max(v))} for r,v in curves.items()},
             'sweep_n':int(len(sweep)),'eigen_sample_count':int(len(spec))}
    (HERE/'resultados_v7.json').write_text(json.dumps(outcome,indent=2,ensure_ascii=False),encoding='utf8')
    return outcome

if __name__=='__main__':
    summary=data_and_charts()
    print(json.dumps(summary,indent=2,ensure_ascii=False))
