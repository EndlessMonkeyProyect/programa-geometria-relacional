#!/usr/bin/env python3
"""O44 -- laboratorio 3D de fase espacial vs retorno material.

Extiende O43-E sin cambiar sus ecuaciones NS, integrador RK4 o diagnósticos.
Los trazadores satisfacen dX/dt = u(X,t) con interpolación trilineal periódica.
El dominio T^3 no contiene una interfaz material toroidal rígida.

Dependencias: NumPy. Ejemplos:
python laboratorio_O44.py --N 48 --T .12 --dt .005 --phases 8 --out resultados_O44_N48.json
python laboratorio_O44.py --N 32 --T .12 --dt .005 --phases 4 --out resultados_O44_N32.json
"""
import argparse, json, math
from pathlib import Path
import numpy as np
import O43E_BASE_NO_MODIFICADA as base

R, A = 1.65, .39
TAU = 2*np.pi

def angular_distance(a,b):
    return (a-b+np.pi) % TAU-np.pi

def velocities_from_fourier(h):
    return np.fft.ifftn(h,axes=(-3,-2,-1)).real

def grid_sample(u,X):
    """Periodic trilinear interpolation at 3-D positions X (n,3); no invented vortex dynamics."""
    N=u.shape[1]
    g=((X+np.pi)*N/TAU) % N
    lower=np.floor(g).astype(int)
    frac=g-lower
    out=np.zeros((len(X),3))
    for ax in (0,1):
        for ay in (0,1):
            for az in (0,1):
                weight=np.prod(np.where(np.array([ax,ay,az])==1,frac,1-frac),axis=1)
                ids=(lower+np.array([ax,ay,az]))%N
                out += weight[:,None]*u[:,ids[:,0],ids[:,1],ids[:,2]].T
    return out

def projected_initial_velocity(N,phase,K,k2):
    grid=np.arange(N)*TAU/N-np.pi
    x,y,z=np.meshgrid(grid,grid,grid,indexing='ij')
    rho=np.sqrt(x*x+y*y+1.e-4)
    ph=np.arctan2(y,x)
    f=np.exp(-((rho-R)**2+z*z)/(2*A*A)) * (1+.20*np.cos(ph)+.12*np.cos(2*ph)+.10*np.cos(3*ph+phase))
    wraw=np.array((-y/rho*f,x/rho*f,np.zeros_like(f)))
    invk2=np.where(k2==0,0.,1/np.maximum(k2,1.))
    mask=np.logical_and.reduce([np.abs(K[j]) < N/3 for j in range(3)])
    wh=np.fft.fftn(wraw,axes=(-3,-2,-1))*mask
    wh=wh-K*np.sum(K*wh,axis=0)[None,...]*invk2
    uh=1j*np.cross(K,wh,axisa=0,axisb=0,axisc=0)*invk2
    uh[:,0,0,0]=0
    return uh

def initial_tracers():
    # 8 positions around the major circle x 4 around an offset of .23 in the tube.
    # All positions are strictly away from the polar/poloidal coordinate singularities.
    phi=np.arange(8)*TAU/8 + .12
    th=np.arange(4)*TAU/4 + .23
    pp,tt=np.meshgrid(phi,th,indexing='ij')
    rr=R+.23*np.cos(tt)
    return np.stack([rr*np.cos(pp),rr*np.sin(pp),.23*np.sin(tt)],axis=-1).reshape(-1,3)

def angles(X):
    rad=np.hypot(X[:,0],X[:,1]); phi=np.arctan2(X[:,1],X[:,0]); theta=np.arctan2(X[:,2],rad-R)
    return phi,theta,np.hypot(rad-R,X[:,2]),rad

def simulate_one(N=48,T=.12,dt=.005,phase=0.,nu=.03,track=True,target_E0=None):
    _,rhs,diagnostic,K,k2=base.make_case(N=N,sign=1,viscosity=nu)
    h=projected_initial_velocity(N,phase,K,k2)
    original_E0=diagnostic(h,0)['E']
    scaling=math.sqrt(target_E0/original_E0) if target_E0 is not None else 1.
    h=h*scaling
    steps=int(round(T/dt)); assert steps>0
    dt=T/steps
    X=initial_tracers() if track else None
    if track:
        pprev,thprev,tube_rad,rho=angles(X)
        cum_phi=np.zeros(len(X)); cum_th=np.zeros(len(X))
        min_tube_rad=float(tube_rad.min())
        max_phi_displacement=0.0
        max_th_displacement=0.0
        max_ph_velocity=0.0
    start=diagnostic(h,0)
    for step in range(steps):
        k1=rhs(h)
        h2=h + (dt/2)*k1
        k2_=rhs(h2)
        h3=h + (dt/2)*k2_
        k3=rhs(h3)
        h4=h + dt*k3
        k4=rhs(h4)
        if track:
            u1=velocities_from_fourier(h)
            u2=velocities_from_fourier(h2)
            u3=velocities_from_fourier(h3)
            u4=velocities_from_fourier(h4)
            v1=grid_sample(u1,X)
            v2=grid_sample(u2,X+dt/2*v1)
            v3=grid_sample(u3,X+dt/2*v2)
            v4=grid_sample(u4,X+dt*v3)
            Xn=X+dt*(v1+2*v2+2*v3+v4)/6
            pn,tn,tuber,rn=angles(Xn)
            cum_phi+=angular_distance(pn,pprev)
            cum_th+=angular_distance(tn,thprev)
            min_tube_rad=min(min_tube_rad,float(tuber.min()))
            max_phi_displacement=max(max_phi_displacement,float(np.max(np.abs(cum_phi))))
            max_th_displacement=max(max_th_displacement,float(np.max(np.abs(cum_th))))
            velphi=(X[:,0]*v1[:,1]-X[:,1]*v1[:,0])/np.maximum(X[:,0]**2+X[:,1]**2,1e-10)
            max_ph_velocity=max(max_ph_velocity,float(np.max(np.abs(velphi))))
            X=Xn;pprev=pn;thprev=tn
        h=h + dt*(k1+2*k2_+2*k3+k4)/6
    final=diagnostic(h,T)
    ans={'phase_requested':float(phase),'initial_scale_factor':float(scaling),'start':start,'end':final}
    if track:
        full_phi=int(np.sum(np.abs(cum_phi)>=TAU))
        full_theta=int(np.sum(np.abs(cum_th)>=TAU))
        ans['tracers']={'count':int(len(X)),'num_complete_toroidal_turns':full_phi,
                        'num_complete_poloidal_turns':full_theta,
                        'rho_material_defined':bool(full_phi>0),
                        'max_abs_toroidal_advance_radians':float(max_phi_displacement),
                        'max_abs_poloidal_advance_radians':float(max_th_displacement),
                        'max_abs_omega_toroidal_sampled':float(max_ph_velocity),
                        'min_distance_to_poloidal_axis':min_tube_rad,
                        'mean_signed_toroidal_advance':float(np.mean(cum_phi)),
                        'positions_initial':initial_tracers().round(10).tolist(),
                        'positions_final':X.round(10).tolist()}
    return ans

def scalar_baseline_LOOCV(results,feature):
    y=np.array([r['end']['P_front'] for r in results])
    x=np.array([r['start'][feature] for r in results])
    z=(x-x.mean())/max(float(x.std()),1e-14)
    design=np.stack([np.ones_like(z),z],axis=1)
    errors=[]
    for i in range(len(y)):
        mask=np.arange(len(y))!=i
        fit=np.linalg.lstsq(design[mask],y[mask],rcond=None)[0]
        errors.append(y[i]-design[i]@fit)
    return float(np.sqrt(np.mean(np.square(errors))))

def phase_regression(results):
    """Descriptive LOOCV: phase-blind mean vs cosine/sine response, no universal prediction claim."""
    x=np.array([r['phase_requested'] for r in results])
    y=np.array([r['end']['P_front'] for r in results])
    A=np.stack([np.ones_like(x),np.cos(x),np.sin(x)],axis=1)
    blind=[];aware=[]
    for leave in range(len(x)):
        mask=np.arange(len(x))!=leave
        blind.append(float(np.mean(y[mask])))
        coeff=np.linalg.lstsq(A[mask],y[mask],rcond=None)[0]
        aware.append(float(A[leave]@coeff))
    rmse0=float(np.sqrt(np.mean((y-np.array(blind))**2)))
    rmse1=float(np.sqrt(np.mean((y-np.array(aware))**2)))
    return {'target':'P_front at T (domain x>0, frame-dependent)',
            'model_baseline':'training mean (radii prescribed; phase ignored)',
            'model_phase':'intercept+cos(phase)+sin(phase)',
            'method':'leave-one-out cross-validation on deterministic phase sweep',
            'blind_LOOCV_RMSE':rmse0,'phase_LOOCV_RMSE':rmse1,
            'improvement_fraction':(1-rmse1/rmse0) if rmse0 else None,
            'other_phase_blind_scalar_LOOCV_RMSE':{v:scalar_baseline_LOOCV(results,v) for v in ('E','K','R_eff','a_eff','amp1','amp3','delta21')},
            'caveat':'very small restricted family, can reflect geometry, not a PDE closure'}

def tests_kine():
    # Pure map test; no attribution to NS.
    ans=[]
    for p,q in ((2,5),(1,4),(3,7)):
        x=0.
        for n in range(q): x=(x+p/q)%1
        ans.append((p,q,abs(x-0)<1e-12))
    return ans

def run(N,T,dt,phases,nu,track,match_enstrophy=False):
    angles_list=np.arange(phases)*TAU/phases
    cases=[]
    E_target=None
    if match_enstrophy:
        _,_,diagnostic,K,k2=base.make_case(N=N,sign=1,viscosity=nu)
        E_target=diagnostic(projected_initial_velocity(N,0,K,k2),0)['E']
    for i,theta in enumerate(angles_list):
        result=simulate_one(N,T,dt,theta,nu,track,target_E0=E_target)
        cases.append(result)
        print(f'case {i+1}/{phases}: phase={theta:.5f}; E={result["end"]["E"]:.8f}; '
              f'Pfront={result["end"]["P_front"]:.10f}; material_return={result.get("tracers",{}).get("rho_material_defined")}', flush=True)
    return {'contract':{'N':N,'nu':nu,'T':T,'dt':dt,'phases':phases,'R_prescribed':R,'a_prescribed':A,'tracer_method':'RK4 parallel to NS RK4 with periodic trilinear velocity interpolation','tracer_count':32 if track else 0,'initial_enstrophy_target':E_target,'physical_statement':'finite Galerkin NS 3D with passive tracers; no full-time/continuum theorem'},
            'cases':cases,'phase_regression':phase_regression(cases) if phases>=5 else None,
            'kinematic_map_unit_tests':tests_kine()}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,default=40);p.add_argument('--T',type=float,default=.12);p.add_argument('--dt',type=float,default=.005);p.add_argument('--phases',type=int,default=8);p.add_argument('--nu',type=float,default=.03);p.add_argument('--no-tracers',action='store_true');p.add_argument('--match-enstrophy',action='store_true');p.add_argument('--out',required=True)
    a=p.parse_args()
    res=run(a.N,a.T,a.dt,a.phases,a.nu,not a.no_tracers,a.match_enstrophy)
    Path(a.out).write_text(json.dumps(res,indent=2,ensure_ascii=False),encoding='utf-8')
    print('saved',a.out,'phase_regression:',res['phase_regression'])
