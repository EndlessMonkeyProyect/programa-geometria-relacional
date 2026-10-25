#!/usr/bin/env python3
"""Laboratorio E-MIRROR v8: razones trigonométricas, nodos y prueba de transferencia.

Modelo 1D idealizado, coordenadas en longitudes de onda iniciales:
 E'' + k^2 E = -F_A delta(x-xs) en [0,A+B], E(0)=E(A+B)=0.
 Interfaz x=A: E continua y E'(A+) - E'(A-) = g E(A).
 g real >= 0 modela una hoja reactiva sin pérdidas, no un vidrio real completo.
 Representación por razones válida sólo cuando E(A) != 0:
            cot(k A) + cot(k B) = -g/k.
 La matriz homogénea de frontera conserva los nodos excluidos por la división.
 Transferencia: F_A -> E_B (fuente controlada sólo en A), comparada con
 cavidades independientes de igual frecuencia (transferencia cero).
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

HERE=Path(__file__).resolve().parent
A=1.0
K0=2*np.pi
XS=.23
XA=.37
ETA=.003

def g_from_R(R:float,kref:float=K0)->float:
    if not 0 <= R < 1: raise ValueError('R debe estar en [0,1)')
    return float(2*kref*np.sqrt(R/(1-R)))

def sheet_rt(k:complex,g:float):
    return g/(2j*k-g), 2j*k/(2j*k-g)

def determinant(k:complex,b:float,g:float,a:float=A):
    return k*np.sin(k*(a+b)) + g*np.sin(k*a)*np.sin(k*b)

def interface_matrix(k:float,b:float,g:float,a:float=A):
    """M dot (left_amplitude,right_amplitude) == 0 para modo normal."""
    return np.array([[np.sin(k*a),-np.sin(k*b)],
                     [k*np.cos(k*a)+g*np.sin(k*a), k*np.cos(k*b)]],dtype=float)

def ratio_residual(k:float,b:float,g:float):
    """Solo usar cuando sin(kA), sin(kB) != 0."""
    sA=np.sin(k*A);sB=np.sin(k*b)
    if abs(sA)<1e-10 or abs(sB)<1e-10:
        raise ZeroDivisionError('Nodo en la interfaz: usar matriz homogénea')
    return float(np.cos(k*A)/sA + np.cos(k*b)/sB + g/k)

def tangent_residual(k:float,b:float,g:float):
    """Carta por tangentes; cubre nodos comunes, falla en cos(kA)*cos(kB)=0."""
    cA=np.cos(k*A);cB=np.cos(k*b)
    if abs(cA)<1e-10 or abs(cB)<1e-10:
        raise ZeroDivisionError('Polo de tangente: usar matriz homogénea')
    ta=np.tan(k*A);tb=np.tan(k*b)
    return float(ta+tb+(g/k)*ta*tb)

def sheet_state_at_node(k:float,b:float):
    """B0/A0 derivado de continuidad de E' en un nodo común."""
    if abs(np.sin(k*A))>1e-8 or abs(np.sin(k*b))>1e-8:
        raise ValueError('No es nodo compartido')
    return float(-np.cos(k*A)/np.cos(k*b))

def green_b_from_a(k:complex,b:float,g:float,xs:float=XS,fracB:float=.5):
    """Respuesta al forzamiento en A medida en B."""
    if not 0<xs<A or not 0<fracB<1: raise ValueError('coordenadas fuera')
    return np.sin(k*xs)*np.sin(k*b*(1-fracB))/determinant(k,b,g)

def _vleft(k:complex,b:float,g:float,x:float):
    h=A-x
    return np.sin(k*b)*np.cos(k*h)+(np.cos(k*b)+g*np.sin(k*b)/k)*np.sin(k*h)

def green_a_from_a(k:complex,b:float,g:float,xs:float=XS,x:float=XA):
    """Medición en A, x>=xs."""
    if not xs <= x < A: raise ValueError('requiere xs<=x<A')
    return np.sin(k*xs)*_vleft(k,b,g,x)/determinant(k,b,g)

def find_modes(b:float,g:float,qmin=.75,qmax=1.25):
    qs=np.linspace(qmin,qmax,2401); d=np.array([determinant(K0*q,b,g) for q in qs])
    roots=[]
    for i in range(len(qs)-1):
        if d[i]*d[i+1]<0:
            root=brentq(lambda z: float(np.real(determinant(K0*z,b,g))),qs[i],qs[i+1],xtol=1e-13)
            if not roots or abs(root-roots[-1])>1e-9: roots.append(float(root))
    if b==.5 and qmin<1<qmax and all(abs(r-1)>1e-7 for r in roots):
        roots.append(1.0)
    return sorted(roots)

def finite_difference_cross(k:complex,b:float,g:float,independent:bool=False,nsteps:int=600):
    """Segundo método numérico, independiente del Green analítico.

    Resuelve la ecuación de Helmholtz por diferencias finitas en el conjunto.
    Si independent=True, impone E(A)=0 y corta los elementos de acoplamiento.
    Solo está implementado para una malla que alinee A y la fuente.
    """
    length=A+b
    h=length/nsteps
    ia=round(A/h)
    if abs(ia*h-A)>1e-10:raise ValueError('malla debe alinear la interfaz')
    isrc=round(XS/h)
    iprobe=round((A+.5*b)/h)
    if not 0<isrc<ia<iprobe<nsteps:raise ValueError('malla insuficiente')
    num=nsteps-1
    main=np.full(num,-2/h**2+k*k,complex)
    off=np.full(num-1,1/h**2,complex)
    if not independent: main[ia-1] -= g/h
    M=diags([off,main,off],[-1,0,1],format='lil',dtype=complex)
    rhs=np.zeros(num,dtype=complex);rhs[isrc-1]=-1/h
    if independent:
        j=ia-1
        M[j,j]=1
        M[j,j-1]=M[j,j+1]=0
        M[j-1,j]=M[j+1,j]=0
    response=spsolve(M.tocsr(),rhs)
    return complex(response[iprobe-1])

def data():
    """Produce datos y gráficas de manera completamente determinista."""
    Rlist=[0,.5,.9,.99]
    b=.5
    # 1. The ratio formulation makes nodal solutions disappear if naively divided.
    q1=np.linspace(.75,1.25,1501)
    g=g_from_R(.5)
    values=[]
    for q in q1:
        k=K0*q
        values.append(float('nan') if abs(np.sin(k*A))<.015 or abs(np.sin(k*b))<.015
                      else np.cos(k*A)/np.sin(k*A)+np.cos(k*b)/np.sin(k*b))
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    ax.plot(q1,values,label=r'$\cot(kA)+\cot(kB)$')
    ax.plot(q1,-g/(K0*q1),label=r'$-g/k$')
    ax.axvline(1,linestyle='--',linewidth=1.2,label='Nodo común q=1: las razones no existen')
    ax.set(xlabel='Frecuencia normalizada q',ylabel='Razones de pendiente/campo',ylim=(-16,16),
           title='Una relación económica, pero incompleta en los nodos')
    ax.legend(fontsize=8);fig.tight_layout()
    fig.savefig(HERE/'01_razones_y_nodo.png',dpi=170);plt.close(fig)
    # Alternative tangent chart covers the common node, but not cosine zeros.
    tan_values=[]
    for q in q1:
        k=K0*q
        tan_values.append(float('nan') if abs(np.cos(k*A))<.02 or abs(np.cos(k*b))<.02
                          else tangent_residual(k,b,g))
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    ax.plot(q1,tan_values,label=r'$\tan(kA)+\tan(kB)+(g/k)\tan(kA)\tan(kB)$')
    ax.axhline(0,linewidth=1,label='Modo: residuo = 0')
    ax.axvline(1,linestyle='--',label='Nodo común incluido')
    ax.set(xlabel='Frecuencia normalizada q',ylabel='Residuo en coordenadas de tangente',
           title='La tangente rescata el nodo perdido por la cotangente',ylim=(-12,12))
    ax.legend(fontsize=8);fig.tight_layout()
    fig.savefig(HERE/'07_tangente_y_nodo.png',dpi=170);plt.close(fig)
    # 2. Matrix formulation spans the node, indicating a genuine eigenmode.
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    for R in Rlist[:-1]:
        gg=g_from_R(R)
        ratios=[]
        for q in q1:
            sv=np.linalg.svd(interface_matrix(K0*q,b,gg),compute_uv=False)
            ratios.append(sv[-1]/sv[0])
        ax.plot(q1,ratios,label=f'R={R:.0%} a q=1')
    ax.axvline(1,linestyle='--',linewidth=1,label='Nodo común q=1')
    ax.set(xlabel='Frecuencia normalizada q',ylabel='Razón singular menor / mayor',
           title='La condición de frontera sigue siendo regular donde falla la cotangente',yscale='log',ylim=(1e-17,1))
    ax.legend(fontsize=9);fig.tight_layout()
    fig.savefig(HERE/'02_matriz_y_nodo.png',dpi=170);plt.close(fig)
    # 3. Causal drive-response transfer differs from independent same-frequency fields.
    q2=np.linspace(.84,1.16,1201)
    response={}
    for R in Rlist:
        gg=g_from_R(R)
        response[R]=np.array([abs(green_b_from_a(K0*q*(1+1j*ETA),b,gg)) for q in q2])
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    for R in Rlist:
        ax.plot(q2,response[R],label=f'Acopladas R={R:.0%}')
    ax.axhline(1e-4,linestyle=':',label='Dos cavidades aisladas: transferencia exacta cero (no visible en escala log)')
    ax.axvline(1,linestyle='--',linewidth=1)
    ax.set(xlabel='q = frecuencia / referencia',ylabel='|Respuesta en B / excitación en A| (u. arbitrarias)',
           title='La prueba de unidad dinámica requiere transmisión entre cuartos',yscale='log',ylim=(1e-3,1e2))
    ax.legend(fontsize=8);fig.tight_layout()
    fig.savefig(HERE/'03_transferencia_controlada.png',dpi=170);plt.close(fig)
    # 4. wall motion controls resonance condition and changes cross transfer.
    bs=np.linspace(.40,.60,601)
    shifts={}
    for q in [.96,1.0,1.04]:
        kk=K0*q*(1+1j*ETA)
        shifts[q]=np.array([abs(green_b_from_a(kk,float(bb),g_from_R(.9))) for bb in bs])
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    for q,v in shifts.items(): ax.plot(bs,v,label=f'q={q:.2f}')
    ax.axvline(.5,linestyle='--',label='B/A=1/2')
    ax.set(xlabel='Profundidad B / A',ylabel='Transferencia A → B (amplitud arbitraria)',
           title='Mover la pared reorganiza la respuesta; la mitad no siempre maximiza la señal',yscale='log')
    ax.legend();fig.tight_layout()
    fig.savefig(HERE/'04_pared_movil.png',dpi=170);plt.close(fig)
    # 5 and 6. At the node, the normalized electric field is zero but its slope is not.
    x=np.linspace(0,1+b,901)
    shape=np.where(x<=1,np.sin(K0*x),np.sin(K0*(1+b-x)))
    dshape=np.where(x<=1,np.cos(K0*x),-np.cos(K0*(1+b-x)))
    for fname,y,ylab,title in [
        ('05_campo_E.png',shape,'Campo E (normalizado)','El campo E se anula en la interfaz, pero no desaparece'),
        ('06_gradiente_H.png',dshape,"E'/k (proxy magnético)",'La pendiente se conserva en el nodo compartido')]:
        fig,ax=plt.subplots(figsize=(9.5,4.5))
        ax.plot(x,y)
        ax.axvline(1,linestyle='--',label='Vidrio en x=A')
        ax.axhline(0,linewidth=.8)
        ax.set(xlabel='Posición x / λ de referencia',ylabel=ylab,title=title)
        ax.legend();fig.tight_layout();fig.savefig(HERE/fname,dpi=170);plt.close(fig)
    with (HERE/'transferencia_v8.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.writer(f)
        w.writerow(['q',*[f'G_BA_abs_R{int(R*100)}' for R in Rlist]])
        for i,q in enumerate(q2): w.writerow([f'{q:.9f}',*[f'{response[R][i]:.12g}' for R in Rlist]])
    with (HERE/'pared_movil_v8.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.writer(f); w.writerow(['B_sobre_A','transfer_q096','transfer_q100','transfer_q104'])
        for i,bb in enumerate(bs): w.writerow([f'{bb:.8f}',*[f'{shifts[q][i]:.12g}' for q in [.96,1.,1.04]]])
    # robust reference point with field+derivative maintained.
    gglist=[g_from_R(R) for R in Rlist]
    nodal_eigenvalues=[float(determinant(K0,b,gg)) for gg in gglist]
    areas=[float(np.trapezoid(shape[x<=1]**2,x[x<=1])),float(np.trapezoid(shape[x>=1]**2,x[x>=1]))]
    testsweep=[]
    for q in [.96,1,1.04]:
        vals=shifts[q]
        testsweep.append({'q':q,'B_of_max_in_0_4_to_0_6':float(bs[np.argmax(vals)]),'max_amplitude':float(np.max(vals)),
                          'amplitude_at_half':float(abs(green_b_from_a(K0*q*(1+1j*ETA),b,g_from_R(.9))))})
    summary={'v':'8.0','regime':'1D scalar normal-incidence wave in ideal cavities; finite loss via Im(k)',
        'key_ratio':'cot(k A)+cot(k B)=-g/k provided sin(k A)*sin(k B)!=0',
        'alternative_tangent_ratio':'tan(k A)+tan(k B)+(g/k)*tan(k A)*tan(k B)=0 provided cos(k A)*cos(k B)!=0',
        'homogeneous_matrix':'[[sin(k A),-sin(k B)],[k cos(k A)+g sin(k A),k cos(k B)]]',
        'node_k0':'k0=2 pi, A=1, B=1/2',
        'node_amplitude_B_over_A':sheet_state_at_node(K0,b),
        'node_eigenvalues_det_by_R':dict(zip(map(str,Rlist),nodal_eigenvalues)),
        'node_energy_fraction_A':areas[0]/sum(areas),'node_energy_fraction_B':areas[1]/sum(areas),
        'node_slope_from_left':float(np.cos(K0*A)),'node_slope_from_right':float(-np.cos(K0*b)),
        'reference_cross_transfer_at_q1_eta0003':{str(R):float(abs(green_b_from_a(K0*(1+1j*ETA),b,g_from_R(R)))) for R in Rlist},
        'independent_cross_transfer':0,'source_x':XS,'measurement_in_A_x':XA,'observation_in_B_fraction':.5,
        'wall_scan_R90':testsweep,
        'sheet_transmission_energy_q1':{str(R):float(abs(sheet_rt(K0,g_from_R(R))[1])**2) for R in Rlist},
        'loss_ratio_eta':ETA,'frequency_samples':len(q2),'wall_samples':len(bs)}
    (HERE/'resultados_v8.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf8')
    return summary

if __name__=='__main__':
    print(json.dumps(data(),indent=2,ensure_ascii=False))
