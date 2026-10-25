#!/usr/bin/env python3
"""O47 — Par de datos NS 3D con (N,E,J,ell,bispectro) iguales pero J' distintos.
Solver pseudospectral Galerkin 2/3, RK4; trazadores RK4 con interpolacion trilineal.
No demuestra NS global ni origen fisico del reloj de singularidad.
"""
import json, math, argparse, time
from pathlib import Path
import numpy as np
TAU=2*np.pi
nu=0.03
A,D,B=1.,.7,.4
CA={2:.6,3:.4,4:.4}
CB={2:math.sqrt(.402),3:math.sqrt(.088),4:math.sqrt(.19)}
ks=sorted(CA)
O=Path(__file__).parent
S0=np.array([[.3,.3,.3],[1.0,1.25,.75],[2.25,.55,1.35],[.55,2.2,2.4]],float)

def assert_close(name,x,y,tol=1e-10):
    if not abs(x-y)<tol:raise AssertionError(f'{name}: {x} != {y}, tol {tol}')

def setup(N):
    k=np.fft.fftfreq(N,d=1/N)
    K=np.array(np.broadcast_arrays(k[:,None,None],k[None,:,None],k[None,None,:]))
    k2=np.sum(K*K,axis=0)
    invk2=np.where(k2==0,0,1/np.maximum(1,k2))
    mask=np.logical_and.reduce([np.abs(K[j])<N/3 for j in range(3)])
    return K,k2,invk2,mask

def make_initial(N,amps):
    g=np.arange(N)*TAU/N
    x,y,z=np.meshgrid(g,g,g,indexing='ij')
    psi=A*np.cos(x)+D*np.cos(y)+B*np.cos(x-y)
    h=sum(v/k*np.cos(k*z) for k,v in amps.items())
    U=np.array([B*np.sin(x-y)-D*np.sin(y),A*np.sin(x)+B*np.sin(x-y)+h,np.zeros_like(x)])
    return np.fft.fftn(U,axes=(-3,-2,-1))

def sample_velocity(U,X):
    n=U.shape[1]
    coord=np.mod(X,TAU)*n/TAU
    ix=np.floor(coord).astype(int);frac=coord-ix
    out=np.zeros((len(X),3))
    for dx in (0,1):
      for dy in (0,1):
       for dz in (0,1):
        offsets=np.array([dx,dy,dz]); ids=(ix+offsets)%n
        weight=np.prod(np.where(offsets==1,frac,1-frac),axis=1)
        out+=weight[:,None]*U[:,ids[:,0],ids[:,1],ids[:,2]].T
    return out

def make_rhs(N,K,k2,invk2,mask):
    def rhs(h):
        w_hat=1j*np.cross(K,h,axisa=0,axisb=0,axisc=0)
        u=np.fft.ifftn(h,axes=(-3,-2,-1)).real
        w=np.fft.ifftn(w_hat,axes=(-3,-2,-1)).real
        nonlinear=np.cross(u,w,axisa=0,axisb=0,axisc=0)
        nh=np.fft.fftn(nonlinear,axes=(-3,-2,-1))*mask
        nh=nh-K*np.sum(K*nh,axis=0)[None,...]*invk2
        return nh-nu*k2*h
    return rhs

def diagnostic(h,rhs,N,K,k2,with_slopes=False):
    w_hat=1j*np.cross(K,h,axisa=0,axisb=0,axisc=0)
    w=np.fft.ifftn(w_hat,axes=(-3,-2,-1)).real
    vel=np.fft.ifftn(h,axes=(-3,-2,-1)).real
    E=float(np.sum(abs(w_hat)**2)/(2*N**6))
    J=float(np.sum(k2[None,...]*abs(w_hat)**2)/N**6)
    wgrad=np.array([np.fft.ifftn(1j*K[j][None,...]*h,axes=(-3,-2,-1)).real for j in range(3)])
    stretch=np.einsum('jxyz,jixyz->ixyz',w,wgrad,optimize=True)
    P=float(np.mean(np.sum(stretch*w,axis=0)))
    bis_psi=[]
    for idx,kval in enumerate([(1,0,0),(0,1,0),(1,-1,0)]):
        ix=tuple(q%N for q in kval)
        zhat=w_hat[2][ix]/(kval[0]**2+kval[1]**2)
        bis_psi.append(zhat/N**3)
    beta=np.conj(bis_psi[0])*bis_psi[1]*bis_psi[2]
    ans=dict(E=E,J=J,P=P,ell=float(math.sqrt(2*E/J)),dE_balance=float(P-nu*J),beta_real=float(beta.real),beta_imag=float(beta.imag),triad_phase=float(np.angle(beta)),moment4=float(np.sum((k2[None,...]**2)*abs(w_hat)**2)/N**6),stretch2=float(np.mean(np.sum(stretch**2,axis=0))),kinetic=float(np.sum(abs(h)**2)/(2*N**6)))
    if with_slopes:
        dh=rhs(h)
        dw=1j*np.cross(K,dh,axisa=0,axisb=0,axisc=0)
        dE=float(np.real(np.sum(np.conj(w_hat)*dw))/N**6)
        dJ=float(2*np.real(np.sum(k2[None,...]*np.conj(w_hat)*dw))/N**6)
        ans.update(dE_from_PDE=dE,dJ_from_PDE=dJ,dell_over_ell=.5*(dE/E-dJ/J))
    return ans

def simulate(N,amps,dt,T):
    K,k2,invk2,mask=setup(N)
    rhs=make_rhs(N,K,k2,invk2,mask)
    h=make_initial(N,amps)*mask
    X=S0.copy();init=S0.copy()
    times=[0.,T/2,T]
    readings=[]
    steps=round(T/dt); assert abs(steps*dt-T)<1e-12 and steps%2==0
    initial=diagnostic(h,rhs,N,K,k2,with_slopes=True)
    readings.append(dict(t=0.,**initial,clock=0.,material_relative_xy_angle=0.,relative_separation=float(np.linalg.norm((X[1]-X[0])/initial['ell']))))
    clock=0.
    zeta_initial=(X[1]-X[0])/initial['ell']
    start_phi=math.atan2(zeta_initial[1],zeta_initial[0]); last_phi=start_phi
    rel_angular_advance=0.;ref_angular_advance=0.
    for step in range(1,steps+1):
        dh1=rhs(h);h2=h+.5*dt*dh1
        dh2=rhs(h2);h3=h+.5*dt*dh2
        dh3=rhs(h3);h4=h+dt*dh3
        dh4=rhs(h4)
        u1=np.fft.ifftn(h,axes=(-3,-2,-1)).real
        u2=np.fft.ifftn(h2,axes=(-3,-2,-1)).real
        u3=np.fft.ifftn(h3,axes=(-3,-2,-1)).real
        u4=np.fft.ifftn(h4,axes=(-3,-2,-1)).real
        v1=sample_velocity(u1,X)
        v2=sample_velocity(u2,X+.5*dt*v1)
        v3=sample_velocity(u3,X+.5*dt*v2)
        v4=sample_velocity(u4,X+dt*v3)
        X+=dt*(v1+2*v2+2*v3+v4)/6
        h+=dt*(dh1+2*dh2+2*dh3+dh4)/6
        dn=diagnostic(h,rhs,N,K,k2,with_slopes=False)
        clock+=dt*(1/readings[-1]['ell']+1/dn['ell'])/2 if step==1 else dt*(1/prev_ell+1/dn['ell'])/2
        prev_ell=dn['ell']
        zeta=(X[1]-X[0])/dn['ell']
        p=math.atan2(zeta[1],zeta[0]); rel_angular_advance+=math.atan2(math.sin(p-last_phi),math.cos(p-last_phi));last_phi=p
        if step==steps//2 or step==steps:
            readings.append(dict(t=round(step*dt,10),**dn,clock=clock,material_relative_xy_angle=rel_angular_advance,relative_separation=float(np.linalg.norm(zeta))))
    particle_distances=np.linalg.norm(X-init,axis=1)
    return dict(readings=readings,tracers_initial=init.tolist(),tracers_final=X.tolist(),max_material_displacement=float(np.max(particle_distances)),material_angular_advance=float(rel_angular_advance),material_return_defined=bool(abs(rel_angular_advance)>=TAU),clock_cycles=float(clock/TAU), max_divergence=float(np.sqrt(np.mean(abs(np.fft.ifftn(1j*np.sum(K*h,axis=0)))**2))))

def run():
    p=argparse.ArgumentParser()
    p.add_argument('--N',type=int,nargs='+',default=[24,32])
    p.add_argument('--dt',type=float,default=.004)
    p.add_argument('--T',type=float,default=.12)
    opt=p.parse_args()
    expected_Amom2=sum(x*x for x in CA.values());expected_Bmom2=sum(x*x for x in CB.values())
    expected_Aw2=sum(k*k*v*v for k,v in CA.items());expected_Bw2=sum(k*k*v*v for k,v in CB.items())
    expected_Aw4=sum(k**4*v*v for k,v in CA.items());expected_Bw4=sum(k**4*v*v for k,v in CB.items())
    assert_close('sum amps equal',expected_Amom2,expected_Bmom2)
    assert_close('second moments equal',expected_Aw2,expected_Bw2)
    assert_close('fourth moment gap',expected_Bw4-expected_Aw4,2.52)
    results={}
    for n in opt.N:
        started=time.monotonic()
        a=simulate(n,CA,opt.dt,opt.T);b=simulate(n,CB,opt.dt,opt.T)
        a0=a['readings'][0];b0=b['readings'][0]
        for name in ('E','J','ell','beta_real','beta_imag','P','triad_phase','dE_from_PDE'):
            assert_close('initial equal '+name,a0[name],b0[name],1e-8)
        assert a0['stretch2']>.01 and b0['stretch2']>.01
        assert_close('dJ exact difference',b0['dJ_from_PDE']-a0['dJ_from_PDE'],-nu*2.52,1e-8)
        assert_close('mirror rate difference',b0['dell_over_ell']-a0['dell_over_ell'],nu*2.52/(2*a0['J']),1e-8)
        assert_close('E balance A',a0['dE_from_PDE'],a0['dE_balance'],1e-8)
        assert_close('E balance B',b0['dE_from_PDE'],b0['dE_balance'],1e-8)
        assert not a['material_return_defined'] and not b['material_return_defined']
        assert abs(a['readings'][-1]['ell']-b['readings'][-1]['ell'])>1e-6
        assert abs(a['readings'][-1]['clock']-b['readings'][-1]['clock'])>1e-7
        results[str(n)]={'I':a,'II':b,'differences':{k:float(b['readings'][-1][k]-a['readings'][-1][k]) for k in ('E','J','ell','P','clock','material_relative_xy_angle','relative_separation')},'elapsed_seconds':round(time.monotonic()-started,2)}
        print('N',n,'PDE Jprime diff',b0['dJ_from_PDE']-a0['dJ_from_PDE'],'end ell diff',results[str(n)]['differences']['ell'],'end E diff',results[str(n)]['differences']['E'],'end clock diff',results[str(n)]['differences']['clock'],'elapsed',results[str(n)]['elapsed_seconds'],flush=True)
    out={'module':'O47','source':'initial fields O46 enlarged by k=4, matched E and J, phase and N; NS spectral RK4 tracer', 'nu':nu,'dt':opt.dt,'T':opt.T,'N':opt.N,'input_amplitudes':{'I':CA,'II':CB},'proof':{'moment2_I':expected_Amom2,'moment2_II':expected_Bmom2,'weighted2_I':expected_Aw2,'weighted2_II':expected_Bw2,'weighted4_I':expected_Aw4,'weighted4_II':expected_Bw4,'dJprime_II_minus_I':-nu*2.52},'results':results,'checks':'all assertions passed','limits':'finite Galerkin/time horizon; no physical clocks or NS global regularity'}
    (O/'O47_RESULTADOS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('Wrote',O/'O47_RESULTADOS.json')
if __name__=='__main__':run()
