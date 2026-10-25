#!/usr/bin/env python3
"""O63: derivada de desfase material, prueba adversarial de información omitida.
Reutiliza los operadores originales de O62 y prepara los estados originales O53.
Unidades adimensionales; resultados Fourier-Galerkin periódicos, no el PDE continuo.
"""
import os,sys, csv,json, math
from pathlib import Path
import numpy as np
from scipy import fft
from scipy.ndimage import map_coordinates
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'fuentes'))
from ejecutar_o62_ORIGINAL import make_state,evaluate,second_order,diagnose,CUTS,LABELS
NU=.025

def original_state(n,eps,matched):
    uh,ks,k2,k2safe,mask,cross_hat=make_state(n,eps,NU,matched)
    return uh,(ks,k2,k2safe,mask,cross_hat)

def frame_center(uh,sys,need_derivative=False):
    ks,k2,k2safe,mask,ch=sys
    n=uh.shape[-1]
    c=np.linspace(-np.pi,np.pi,n,endpoint=False)
    x,y,z=np.meshgrid(c,c,c,indexing='ij'); rr=np.hypot(x,y)
    om=fft.ifftn(ch(uh),axes=(-3,-2,-1)).real
    ww=np.sum(om*om,axis=0)
    wtotal=float(ww.sum())
    Rc=float(np.sum(rr*ww)/wtotal)
    Q=np.sum(ww*np.exp(1j*z));Zc=float(np.angle(Q))
    if not need_derivative:return Rc,Zc
    dudt,_=evaluate(uh,*sys,nu=NU)
    domdt=fft.ifftn(ch(dudt),axes=(-3,-2,-1)).real
    dw=2*np.sum(om*domdt,axis=0)
    dRc=float(np.sum((rr-Rc)*dw)/wtotal)
    dZc=float(np.imag(np.sum(dw*np.exp(1j*z))/Q))
    return Rc,Zc,dRc,dZc

def initial_particles(phi):
    d=np.array([.12,.26,.34])
    rho=np.array([1+s*di for di in d for s in (1,-1)])
    return np.stack((rho*np.cos(phi),rho*np.sin(phi),np.zeros_like(rho)),axis=1)

def interpolate(field,pts):
    n=field.shape[-1];pos=[np.mod(pts[:,j]+np.pi,2*np.pi)*n/(2*np.pi) for j in range(3)]
    return np.stack([map_coordinates(a,pos,order=1,mode='grid-wrap',prefilter=False) for a in field],axis=1)

def phase(pts,Rc,Zc):
    rad=np.hypot(pts[:,0],pts[:,1]); return np.arctan2(pts[:,2]-Zc,rad-Rc)

def initial_slope(uh,sys,phi):
    Rc,Zc,dRc,dZc=frame_center(uh,sys,True)
    u=fft.ifftn(uh,axes=(-3,-2,-1)).real
    pts=initial_particles(phi)
    vel=interpolate(u,pts)
    rho=np.hypot(pts[:,0],pts[:,1]);dotrho=(pts[:,0]*vel[:,0]+pts[:,1]*vel[:,1])/rho
    xx=rho-Rc; zz=pts[:,2]-Zc
    dotphase=(xx*(vel[:,2]-dZc)-zz*(dotrho-dRc))/(xx*xx+zz*zz)
    return float((dotphase[2]-dotphase[0])/(2*np.pi)),dict(Rc=Rc,Zc=Zc,Rcdot=dRc,Zcdot=dZc, u_out12=vel[0].tolist(),u_out26=vel[2].tolist())

def azimuthal_distribution(uh,sys,count=24):
    """Firma de ritmos de marcas materiales relativas al centro, sin fijar azimut preferente."""
    Rc,Zc,dRc,dZc=frame_center(uh,sys,True)
    u=fft.ifftn(uh,axes=(-3,-2,-1)).real
    phis=np.arange(count)*2*np.pi/count
    pts=np.concatenate([initial_particles(phi) for phi in phis])
    vel=interpolate(u,pts)
    rho=np.hypot(pts[:,0],pts[:,1]);drho=(pts[:,0]*vel[:,0]+pts[:,1]*vel[:,1])/rho
    x=rho-Rc;z=pts[:,2]-Zc
    wdot=(x*(vel[:,2]-dZc)-z*(drho-dRc))/(x*x+z*z)
    rates=((wdot.reshape(count,6)[:,2]-wdot.reshape(count,6)[:,0])/(2*np.pi))
    modes=np.fft.rfft(rates)/count
    return rates,dict(mean=float(np.mean(rates)),std=float(np.std(rates)),range=float(np.max(rates)-np.min(rates)),
                      abs_harmonic_1=float(abs(modes[1])),abs_harmonic_2=float(abs(modes[2])),
                      count=count)

def rotate_90_z(uh):
    """Q u(Q^-1 x) para Q=rotación 90° CCW alrededor de z en retícula par."""
    n=uh.shape[-1]
    arr=fft.ifftn(uh,axes=(-3,-2,-1)).real
    yind=np.arange(n)[None,:]; negx=(-np.arange(n))[:,None]%n
    original=arr[:,yind,negx,:]
    new=np.stack((-original[1],original[0],original[2]))
    return fft.fftn(new,axes=(-3,-2,-1))

def band_summary(uh,sys):
    ks,k2,k2safe,mask,ch=sys
    rhs,nl=evaluate(uh,*sys,nu=NU)
    initial,whole=diagnose(uh,nl,ks,k2,mask,nu=NU)
    second=second_order(uh,sys,nu=NU)
    return np.array([r['E'] for r in initial]),np.array([second[r['banda']]['nonlinear_second'] for r in initial]),whole

def rk4_step_uh_pts(uh,pts,dt,sys):
    ks,k2,k2safe,mask,ch=sys
    def step(x,p):
        f,_=evaluate(x,*sys,nu=NU)
        vel=fft.ifftn(x,axes=(-3,-2,-1)).real
        return f,interpolate(vel,p)
    a,b=step(uh,pts)
    c,d=step(uh+dt*a/2,pts+dt*b/2)
    e,f=step(uh+dt*c/2,pts+dt*d/2)
    g,h=step(uh+dt*e,pts+dt*f)
    return (uh+dt*(a+2*c+2*e+g)/6)*mask,(pts+dt*(b+2*d+2*f+h)/6+np.pi)%(2*np.pi)-np.pi

def trajectories(uh0,sys,dt=.004,T=.08):
    uh=uh0.copy(); pts=np.concatenate([initial_particles(0.),initial_particles(np.pi/2),initial_particles(-np.pi/2)],axis=0)
    old={}; rr=[]; nsteps=int(round(T/dt));dt=T/nsteps
    for j in range(nsteps+1):
        if j in (0,1,2,5,10,20) or j==nsteps:
            Rc,Zc=frame_center(uh,sys)
            p0=phase(pts[:6],Rc,Zc);p1=phase(pts[6:12],Rc,Zc);pm=phase(pts[12:],Rc,Zc)
            # En la ventana corta, la diferencia de fase se obtiene sobre el círculo.
            for tag,ph in [('0',p0),('90',p1),('-90',pm)]:
                if tag not in old:old[tag]=ph.copy()
                delta=np.angle(np.exp(1j*(ph-old[tag])))
                rr.append(dict(t=j*dt,azimuth=tag,S=float((delta[2]-delta[0])/(2*np.pi)),Rc=Rc,Zc=Zc))
        if j==nsteps:break
        uh,pts=rk4_step_uh_pts(uh,pts,dt,sys)
    return rr

def load_original(n,eps,matched):
    source=BASE/'fuentes'/'datos_O53_originales'
    nm=f'NS_N{n}_eps{int(round(eps*100)):02d}'+('_equienergia' if matched else '')+'.json'
    data=json.loads((source/nm).read_text()); return data

def run(out=BASE,quick=False):
    configs=[(0.,False),(.14,False),(.14,True)];ns=(32,) if quick else (40,48)
    values=[];truth=[];checks={};symmetry=[];angular=[];angular_summaries=[];rotated_trace=[]
    for n in ns:
        for eps,match in configs:
            uh,sys=original_state(n,eps,match)
            s0,info=initial_slope(uh,sys,0.)
            s90,_=initial_slope(uh,sys,np.pi/2)
            en,Q,whole=band_summary(uh,sys)
            rates,aggr=azimuthal_distribution(uh,sys)
            for i,rate in enumerate(rates):angular.append(dict(N=n,eps=eps,match=int(match),azimuth_degrees=i*360/len(rates),slope=float(rate)))
            angular_summaries.append(dict(N=n,eps=eps,match=int(match),**aggr))
            trace=trajectories(uh,sys)
            for az,ss in [('0',s0),('90',s90)]:
                for r in trace:
                    if r['azimuth']!=az:continue
                    t=r['t'];prediction=ss*t
                    values.append(dict(N=n,eps=eps,match=int(match),azimuth=az,t=t,measured_S=r['S'],predicted_S=prediction,initial_slope=ss,error=r['S']-prediction,center_R=r['Rc'],center_Z=r['Zc']))
            if not quick:
                original=load_original(n,eps,match)
                origin={round(r['t'],6):r for r in original['records']}
                for r in trace:
                    if r['azimuth']!='0':continue
                    sr=origin.get(round(r['t'],6))
                    if sr is not None:
                        truth.append(dict(N=n,eps=eps,match=int(match),t=r['t'],reproduced_S=r['S'],original_O53_S=sr['outer_diff_turns'],difference=r['S']-sr['outer_diff_turns']))
            if eps==.14 and not match:
                rotated=rotate_90_z(uh)
                er,qr,whole_r=band_summary(rotated,sys)
                srot,_=initial_slope(rotated,sys,0.)
                # rotar Q +90 sobre un campo produce resultado en phi0 como original phi-90.
                sminus,_=initial_slope(uh,sys,-np.pi/2)
                rrot,arot=azimuthal_distribution(rotated,sys)
                symmetry_err=float(np.max(np.abs(np.sort(rates)-np.sort(rrot))))
                if n==40:
                    rotated_trajectory=trajectories(rotated,sys)
                    # mismo giro de marco y marcas: -90 en original = 0 en campo rotado.
                    refminus={round(r['t'],6):r['S'] for r in trace if r['azimuth']=='-90'}
                    rot0={round(r['t'],6):r['S'] for r in rotated_trajectory if r['azimuth']=='0'}
                    rotated_trace.append(dict(N=n,max_difference=max(abs(rot0[t]-refminus[t]) for t in refminus)))
                symmetry.append(dict(N=n,relative_E_err=float(np.max(np.abs(er-en))/max(np.max(en),1e-15)),
                                     max_Q_err=float(np.max(np.abs(qr-Q))),
                                     s_original_0=s0,s_original_90=s90,s_rotated_0=srot,s_original_minus90=sminus,
                                     delta_slopes=s0-s90,azimuthal_sorted_max_err=symmetry_err,rotated_std=arot["std"]))
            print('listo',n,eps,match,'Sdot 0',s0,'90',s90,'initial E',whole['E'],flush=True)
    valid_truth=max(abs(v['difference']) for v in truth) if truth else None
    tests={
      'datos_finitos':all(np.isfinite([v['measured_S'],v['predicted_S']]).all() for v in values),
      'derivada_initial_positiva_todos':all(v['initial_slope']>0 for v in values),
      'reproduccion_O53_tolerancia_1e-8':valid_truth is None or valid_truth<1e-8,
      'rotacion_cambio_global_band_minimo':all(s['relative_E_err']<2e-12 and s['max_Q_err']<2e-12 for s in symmetry),
      'rotacion_covariancia_slope':all(abs(s['s_rotated_0']-s['s_original_minus90'])<1e-9 for s in symmetry),
      'rotacion_distingue_anclaje_local':all(abs(s['delta_slopes'])>.3 for s in symmetry),
      'trayectoria_equivariante_90grados':all(s['max_difference']<1e-10 for s in rotated_trace),
      'distribucion_angular_invariante_por_rotacion':all(s['azimuthal_sorted_max_err']<1e-9 for s in symmetry),
      'caso_perturbado_tiene_varianza_angular':all(r['std']>.1 for r in angular_summaries if r['eps']>.1),
      'caso_base_armonico2_nulo':all(r['abs_harmonic_2']<1e-11 for r in angular_summaries if r['eps']==0.),
      'perturbacion_armonico2_presente':all(r['abs_harmonic_2']>.1 for r in angular_summaries if r['eps']>.1),
      'sym_sin_perturbacion_azimutes':all(abs(next(v['initial_slope'] for v in values if v['N']==n and v['eps']==0. and v['azimuth']=='0') - next(v['initial_slope'] for v in values if v['N']==n and v['eps']==0. and v['azimuth']=='90'))<1e-10 for n in ns),
    }
    out=Path(out);(out/'resultados').mkdir(parents=True,exist_ok=True)
    def writecsv(name,rows):
        if not rows:return
        with (out/'resultados'/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
    writecsv('desfases_predichos_y_calculados.csv',values)
    writecsv('reproduccion_o53.csv',truth)
    writecsv('controles_rotacion.csv',symmetry)
    writecsv('distribucion_azimutal.csv',angular)
    writecsv('resumen_distribucion.csv',angular_summaries)
    sums={'checks':tests,'num_pronosticos':len(values),'num_reproducciones':len(truth),'max_error_reproduccion_O53':valid_truth,
          'simetria':symmetry,'control_temporal_rotacion':rotated_trace,'distribuciones':angular_summaries,'comentario':'Taylor de primer orden inicial no sirve como pronóstico largo; rotación preserva espectro pero cambia respuesta en marca fija.'}
    (out/'resultados'/'resumen.json').write_text(json.dumps(sums,indent=2,ensure_ascii=False))
    print(json.dumps(sums,indent=2,ensure_ascii=False),flush=True)
    assert all(tests.values()), tests
    return values,sums

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--quick',action='store_true');a=p.parse_args()
    run(quick=a.quick)
