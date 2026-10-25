#!/usr/bin/env python3
"""O62: análisis a priori de bandas en O53, sin modificar la fuente O53.
Reproduce la inicialización de o53_perturbed_ring.py y la evolución Galerkin
sin trazadores, para aislar la predicción de transferencia por bandas.
"""
import argparse, csv, hashlib, json, sys
from pathlib import Path
import numpy as np
from scipy import fft

CUTS=[0,2,4,6,8,11,float('inf')]
LABELS=['[0,2)','[2,4)','[4,6)','[6,8)','[8,11)','[11,infinito)']

def make_state(N=32,eps=0.0,nu=.025,match_energy=False):
    c=np.linspace(-np.pi,np.pi,N,endpoint=False)
    x,y,z=np.meshgrid(c,c,c,indexing='ij')
    R=1.;a=.35;gamma=6.
    rr=np.sqrt(x*x+y*y)
    g=np.exp(-((rr*rr-R*R)/(2*R*a))**2-(z/a)**2)
    f=gamma/(np.pi*a*a*R)*g
    omega_init=np.stack((-y*f,x*f,np.zeros_like(f)))
    k1=fft.fftfreq(N,d=1/N);kx,ky,kz=np.meshgrid(k1,k1,k1,indexing='ij')
    ks=np.stack((kx,ky,kz)); k2=kx*kx+ky*ky+kz*kz; k2safe=np.where(k2==0,1,k2)
    mask=(np.abs(kx)<=N//3)&(np.abs(ky)<=N//3)&(np.abs(kz)<=N//3)
    def hats(x):return fft.fftn(x,axes=(-3,-2,-1))
    def cross_hat(x):return np.stack((1j*(ky*x[2]-kz*x[1]),1j*(kz*x[0]-kx*x[2]),1j*(kx*x[1]-ky*x[0])))
    uh_base=cross_hat(hats(omega_init))/k2safe
    uh_base[:,0,0,0]=0;uh_base*=mask
    avec=np.stack((np.zeros_like(g),g*x/R,g*y/R))
    uh_pert=cross_hat(hats(avec))*mask
    uh_pert[:,0,0,0]=0
    unorm=float(np.linalg.norm(uh_base));pnorm=float(np.linalg.norm(uh_pert))
    assert unorm>0 and pnorm>0
    uh=uh_base+eps*(unorm/pnorm)*uh_pert
    if match_energy:uh*=unorm/np.linalg.norm(uh)
    uh*=mask
    return uh,ks,k2,k2safe,mask,cross_hat

def evaluate(uh,ks,k2,k2safe,mask,cross_hat,nu=.025):
    u=fft.ifftn(uh,axes=(-3,-2,-1)).real
    om=fft.ifftn(cross_hat(uh),axes=(-3,-2,-1)).real
    ch=fft.fftn(np.cross(u,om,axis=0),axes=(-3,-2,-1))
    dot=np.sum(ks*ch,axis=0)/k2safe
    nl=(ch-ks*dot)*mask;nl[:,0,0,0]=0
    rhs=(nl-nu*k2*uh)*mask
    return rhs,nl

def diagnose(uh,nl,ks,k2,mask,nu=.025):
    n=uh.shape[-1]
    kinetic=.5*np.sum(np.abs(uh)**2,axis=0)/n**6
    nonlinear=np.real(np.sum(np.conj(uh)*nl,axis=0))/n**6
    diss=2*nu*k2*kinetic
    mag=np.sqrt(k2)
    output=[]
    for i,label in enumerate(LABELS):
        mm=(mag>=CUTS[i])&(mag<CUTS[i+1])&mask
        e=float(kinetic[mm].sum());t=float(nonlinear[mm].sum());d=float(diss[mm].sum())
        output.append(dict(banda=label,E=e,T=t,D=d,prediccion=t-d))
    return output,dict(E=float(kinetic.sum()),T=float(nonlinear.sum()),D=float(diss.sum()))

def second_order(uh, sys, nu=.025):
    """Segunda derivada exacta del sistema Galerkin en el estado inicial.
    F'(u)F=P[F x curl(u) + u x curl(F)]-nu*k2*F.
    """
    ks,k2,k2safe,mask,cross_hat=sys
    n=uh.shape[-1]
    F,nl=evaluate(uh,*sys,nu)
    u=fft.ifftn(uh,axes=(-3,-2,-1)).real
    om=fft.ifftn(cross_hat(uh),axes=(-3,-2,-1)).real
    v=fft.ifftn(F,axes=(-3,-2,-1)).real
    dom=fft.ifftn(cross_hat(F),axes=(-3,-2,-1)).real
    h=fft.fftn(np.cross(v,om,axis=0)+np.cross(u,dom,axis=0),axes=(-3,-2,-1))
    dot=np.sum(ks*h,axis=0)/k2safe
    nprime=(h-ks*dot)*mask;nprime[:,0,0,0]=0
    fprime=(nprime-nu*k2*F)*mask
    density=(np.sum(np.abs(F)**2,axis=0)+np.real(np.sum(np.conj(uh)*fprime,axis=0)))/n**6
    ek=.5*np.sum(np.abs(uh)**2,axis=0)/n**6
    heatsecond=4*nu**2*k2**2*ek
    out={}
    mag=np.sqrt(k2)
    for i,label in enumerate(LABELS):
        mm=(mag>=CUTS[i])&(mag<CUTS[i+1])&mask
        out[label]=dict(second=float(density[mm].sum()),heat_second=float(heatsecond[mm].sum()),
                        nonlinear_second=float((density-heatsecond)[mm].sum()))
    return out

def heat_energy(uh0,k2,mask,t,nu=.025):
    n=uh0.shape[-1]
    ek0=.5*np.sum(np.abs(uh0)**2,axis=0)/n**6
    eheat=ek0*np.exp(-2*nu*k2*t)
    mag=np.sqrt(k2)
    return {label:float(eheat[((mag>=CUTS[i])&(mag<CUTS[i+1])&mask)].sum()) for i,label in enumerate(LABELS)}

def rk4_step(u,dt,sys,nu):
    ks,k2,k2safe,mask,cross_hat=sys
    def rhs(q):return evaluate(q,ks,k2,k2safe,mask,cross_hat,nu)[0]
    k1=rhs(u);k2r=rhs(u+dt*k1/2);k3r=rhs(u+dt*k2r/2);k4=rhs(u+dt*k3r)
    return (u+dt/6*(k1+2*k2r+2*k3r+k4))*mask

def execute(N,epsilon,match_energy,T=.08,dt=.004):
    nu=.025
    u,ks,k2,k2safe,mask,cross_hat=make_state(N,epsilon,nu,match_energy)
    sys=(ks,k2,k2safe,mask,cross_hat)
    _,nl=evaluate(u,*sys,nu)
    initial,total0=diagnose(u,nl,ks,k2,mask,nu)
    second=second_order(u,sys,nu)
    u0=u.copy()
    times=[.02,.08]
    if T!=.08:times=[T/4,T]
    rows=[]
    nsteps=int(round(T/dt));dt=T/nsteps
    for step in range(1,nsteps+1):
        u=rk4_step(u,dt,sys,nu)
        t=step*dt
        if any(abs(t-st)<dt/3 for st in times):
            _,nonlinear=evaluate(u,*sys,nu)
            current,whole=diagnose(u,nonlinear,ks,k2,mask,nu)
            heat=heat_energy(u0,k2,mask,t,nu)
            for before,after in zip(initial,current):
                rows.append(dict(N=N,epsilon=epsilon,match_energy=int(match_energy),t=t,band=before['banda'],
                                E0=before['E'],transfer0=before['T'],diss0=before['D'],
                                predicted_derivative=before['prediccion'],
                                predicted_change=t*before['prediccion'],observed_change=after['E']-before['E'],
                                E_now=after['E'],T_now=after['T'],D_now=after['D'],
                                initial_nonlinear_curvature=second[before['banda']]['nonlinear_second'],
                                predicted_nonlinear_change=.5*t*t*second[before['banda']]['nonlinear_second'],
                                observed_nonlinear_change=after['E']-heat[before['banda']],
                                heat_reference=heat[before['banda']]))
    return rows,total0

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default=None);ap.add_argument('--quick',action='store_true');args=ap.parse_args()
    root=Path(args.out or Path(__file__).resolve().parents[1]);(root/'resultados').mkdir(parents=True,exist_ok=True)
    allrows=[];totals=[]
    ns=(32,) if args.quick else (32,40,48)
    for n in ns:
        for eps,match in [(0.,False),(.14,False),(.14,True)]:
            rows,total=execute(n,eps,match)
            allrows.extend(rows);totals.append(dict(N=n,epsilon=eps,match_energy=match,**total))
            print('Listo',n,eps,match,'E',total['E'],'transfer total',total['T'],flush=True)
    with (root/'resultados/transferencias_y_predicciones.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(allrows[0].keys()));w.writeheader();w.writerows(allrows)
    # Falsación de la predicción: no se reajusta tras observar la evolución
    tests={}
    tests['sum_transfer_zero']=all(abs(t['T'])<1e-10 for t in totals)
    tests['equal_base_energy_across_matched']=all(abs(next(t['E'] for t in totals if t['N']==n and t['epsilon']==0)-next(t['E'] for t in totals if t['N']==n and t['epsilon']==.14 and t['match_energy']))<2e-13 for n in ns)
    tests['all_finite']=all(np.isfinite(r['E_now']) and np.isfinite(r['predicted_derivative']) for r in allrows)
    tests['total_nonzero_dissipation']=all(t['D']>0 for t in totals)
    tests['initial_band_nonlinear_transfer_vanishes']=all(abs(r['transfer0'])<1e-12 for r in allrows)
    tests['energy_derivative_sum_is_dissipation']=all(abs(sum(r['predicted_derivative'] for r in allrows if r['N']==t['N'] and r['epsilon']==t['epsilon'] and r['match_energy']==int(t['match_energy']) and abs(r['t']-.02)<1e-5) + t['D'])<1e-10 for t in totals)
    # Predicciones con signo correctamente discriminante para la banda [2,4)
    tests['signo_40_banda_2_4']=all(
        np.sign(r['predicted_nonlinear_change'])==np.sign(r['observed_nonlinear_change'])
        for r in allrows if r['N']==40 and r['band']=='[2,4)'
    )
    for r in allrows:
        if abs(r['t']-.02)<1e-5 and abs(r['predicted_change'])>1e-10:
            r['same_sign_early']=bool(np.sign(r['predicted_change'])==np.sign(r['observed_change']))
    stats={"checks":tests,"totals":totals,"number_records":len(allrows)}
    (root/'resultados/resumen.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False))
    print(json.dumps(stats,indent=2));assert all(tests.values()),tests
    return allrows
if __name__=='__main__':main()
