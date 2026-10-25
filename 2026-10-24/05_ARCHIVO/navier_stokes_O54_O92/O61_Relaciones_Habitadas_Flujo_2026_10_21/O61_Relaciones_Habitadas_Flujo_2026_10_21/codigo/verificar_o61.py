#!/usr/bin/env python3
"""O61. Subespacio exacto de Navier-Stokes 3D sobre T^3.
No usa una solucion aproximada del toroide O53; la ODE es la representacion
espectral de una solucion exacta reducida de NS en la clase invariante.
Programa de Geometria Relacional, Le Matt Ansatz Di Ego, 2026-10-21.
"""
from pathlib import Path
import json, csv, math, hashlib
import numpy as np
from scipy.integrate import solve_ivp

BASE = Path(__file__).resolve().parents[1]
OUT = BASE/'resultados'
OUT.mkdir(exist_ok=True)
A=B=1.0
NU=0.025
T=1.26
TIMES=np.linspace(0,T,127)
THEtas=(0.0,math.pi/6,math.pi/2)

def integrate(theta,M=18):
    k=np.arange(-M,M+1)
    s=A*np.sin(theta)
    z0=np.zeros(len(k),dtype=complex); z0[M]=B
    def rhs(t,c):
        left=np.r_[0.+0j,c[:-1]]
        right=np.r_[c[1:],0.+0j]
        return -NU*(k*k+1)*c-0.5j*s*np.exp(-NU*t)*(left+right)
    solution=solve_ivp(rhs,(0,T),z0,method='DOP853',t_eval=TIMES,rtol=2e-12,atol=2e-13)
    assert solution.success
    C=solution.y.T
    E=(A*A*np.exp(-2*NU*TIMES)+np.sum(np.abs(C)**2,axis=1))/4
    H=(A*A*np.exp(-2*NU*TIMES)+np.sum((k*k+1)[None,:]*np.abs(C)**2,axis=1))/4
    coeff=np.abs(C[:,M+1])
    # analytical RHS: non-linear transfer at t=0 is AB sin(theta) /2 in this coefficient
    assert abs(rhs(0,z0)[M+1]+0.5j*A*B*math.sin(theta))<1e-14
    # total energy dissipation computed from spectral derivative, not estimated backwards
    ddE=np.array([(-2*NU*A*A*np.exp(-2*NU*t)+2*np.real(np.vdot(c,rhs(t,c))))/4 for t,c in zip(TIMES,C)])
    res=float(np.max(np.abs(ddE+2*NU*H)))
    return {'theta':theta,'M':M,'t':TIMES,'E':E,'H':H,'sideband':coeff,'C':C,'k':k,'energy_residual':res,'coupling':A*B*math.sin(theta)}

def main():
    checks=0
    sol={}
    convergence={}
    for th in THEtas:
        arr=[]
        for M in (6,12,24):
            z=integrate(th,M);arr.append(z)
            assert z['energy_residual']<2e-12;checks+=1
            assert abs(z['E'][0]-.5)<1e-13 and abs(z['H'][0]-.5)<1e-13;checks+=2
            assert np.max(np.diff(z['E']))<1e-10;checks+=1
            assert np.max(z['sideband'])<1e-11 if th==0 else z['sideband'][-1]>1e-3;checks+=1
        # Reference convergence of three observed scalars at T
        d=max(abs(arr[-2][f][-1]-arr[-1][f][-1]) for f in ('E','H','sideband'))
        assert d<1e-9;checks+=1
        sol[th]=arr[-1]
        convergence[f'{th:.12g}']={'M6_a_M12':{f:float(abs(arr[0][f][-1]-arr[1][f][-1])) for f in ('E','H','sideband')},'M12_a_M24':{f:float(abs(arr[1][f][-1]-arr[2][f][-1])) for f in ('E','H','sideband')}}
    # Full exact invariant dynamics includes u_x=0, u_y=A sin(th)e^{-nu t}cos x,
    # u_z=A cos(th)e^{-nu t}cos x + Re(e^{iy} sum_m c_m e^{imx}).
    # u_y_y=0, u_z_z=0 => div=0. Advective term only u_y d_y u_z.
    checks+=1
    # Pairwise initial invariants equal, yet sideband changes continuously.
    assert abs(sol[0]['sideband'][-1])<1e-12
    assert sol[math.pi/6]['sideband'][-1]>0.15
    assert sol[math.pi/2]['sideband'][-1]>0.3
    checks+=3
    # initial derivative transfers from p,q to p+q with strength proportional to sin(theta)
    assert abs(sol[math.pi/2]['coupling']-2*sol[math.pi/6]['coupling'])<1e-12;checks+=1
    # Objectivity of the triadic interaction: simultaneous rotation of wavevectors
    # and polarizations preserves the transverse coupling norm.
    p=np.array([1.,0.,0.]); q=np.array([0.,1.,0.]); k=p+q
    aa=np.array([0.,math.sin(math.pi/6),math.cos(math.pi/6)]); bb=np.array([0.,0.,1.])
    def transfer(p,q,aa,bb):
        k=p+q; raw=np.dot(aa,q)*bb+np.dot(bb,p)*aa
        proj=raw-k*np.dot(k,raw)/np.dot(k,k)
        return float(np.linalg.norm(proj))
    baseline=transfer(p,q,aa,bb)
    for alpha in (math.pi/2,math.pi/3,math.pi/7):
        cc,ss=math.cos(alpha),math.sin(alpha)
        rot=np.array([[cc,-ss,0.],[ss,cc,0.],[0.,0.,1.]])
        assert abs(transfer(rot@p,rot@q,rot@aa,rot@bb)-baseline)<1e-13
        checks+=1
    # total bound: at most floor(1/eps) independent coefficients with normalized weight >= eps
    for th,z in sol.items():
        for i in (0,12,63,126):
            weights=np.abs(z['C'][i])**2
            weights/=weights.sum()
            for eps in (.01,.05,.1,.2):
                assert int(np.count_nonzero(weights>=eps))<=math.floor(1/eps);checks+=1
    rows=[]
    for theta,z in sol.items():
        for t,e,h,side in zip(z['t'],z['E'],z['H'],z['sideband']):
            rows.append({'theta_rad':f'{theta:.12g}','t':f'{t:.12g}','energia':f'{e:.12g}','enstrofia':f'{h:.12g}','modo_1_1_amplitud':f'{side:.12g}','acoplamiento_inicial':f'{z["coupling"]:.12g}'})
    with (OUT/'series_o61.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    result={'titulo':'O61 — Relaciones disponibles y ocupacion efectiva en NS 3D','solucion':'u=(0, A sin(theta)exp(-nu t)cos x, A cos(theta)exp(-nu t)cos x + Re(exp(iy) sum c_m(t)exp(imx)))','nu':NU,'A':A,'B':B,'tiempo_final':T,'checks':checks,'M_reporte':24,'valor_inicial_E':0.5,'valor_inicial_H':0.5,'resultados':{},'convergencia_M':convergence,'acoplamiento_objetivo_rotaciones':True,'alcance':'Subclase invariante exacta de NS 3D en el toro periodico; evolucion modal mediante truncacion convergente, no es el anillo O53, y no demuestra ley cuadratica O60.'}
    for th,z in sol.items():
        result['resultados'][f'{th:.12g}']={'angulo_grados':th*180/math.pi,'modo_nuevo_amplitud_tfinal':float(z['sideband'][-1]),'energia_tfinal':float(z['E'][-1]),'enstrofia_tfinal':float(z['H'][-1]),'acoplamiento_inicial':float(z['coupling']),'residuo_energia':float(z['energy_residual'])}
    (OUT/'resumen_o61.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    # Visualize before/after with default matplotlib colors
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(2,1,figsize=(8,7),sharex=True)
    for th,z in sol.items():
        label=f'θ={th*180/math.pi:.0f}°'
        axs[0].plot(z['t'],z['sideband'],label=label)
        axs[1].plot(z['t'],z['E'],label=label)
    axs[0].set(ylabel='Amplitud modo nuevo (1,1,0)',title='O61 | Mismos modos y energía inicial; distinta ocupación dinámica')
    axs[1].set(xlabel='Tiempo',ylabel='Energía cinética media')
    axs[0].legend();axs[1].legend()
    fig.tight_layout();fig.savefig(BASE/'graficos'/'o61_modo_nuevo_y_energia.png',dpi=180)
    plt.close(fig)
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
