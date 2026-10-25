#!/usr/bin/env python3
"""Ensayo abierto, Navier-Stokes 3D periodico sin forzamiento.
Valida propagacion temporal de anillos vorticiales; no afirma retorno poloidal material.
Solo NumPy. Estancias espectrales 2/3, RK4. 20 Oct 2026.
"""
import argparse, json, time
import numpy as np


def make_case(N=40, sign=1, viscosity=0.03):
    grid = np.arange(N)*2*np.pi/N-np.pi
    x,y,z=np.meshgrid(grid,grid,grid,indexing='ij')
    rho=np.sqrt(x*x+y*y+1.e-4)
    R,a=1.65,.39
    ph=np.arctan2(y,x)
    # Same first two phases and same modal magnitudes, different third phase.
    amp=1. +.20*np.cos(ph)+.12*np.cos(2*ph) + sign*.10*np.cos(3*ph)
    f=np.exp(-((rho-R)**2+z*z)/(2*a*a))*amp
    wraw=np.array((-y/rho*f,x/rho*f,np.zeros_like(f)))
    k=np.fft.fftfreq(N, 1/N)
    K=np.array(np.broadcast_arrays(k[:,None,None],k[None,:,None],k[None,None,:]))
    k2=np.sum(K*K,axis=0)
    invk2=np.where(k2==0,0.,1/np.maximum(k2,1.))
    lim=N/3
    dealias=np.logical_and.reduce([np.abs(K[j])<lim for j in range(3)])
    wh=np.fft.fftn(wraw,axes=(-3,-2,-1))*dealias
    # Helmholtz-projected vorticity, Biot-Savart inversion.
    wh=wh-K*np.sum(K*wh,axis=0)[None,...]*invk2
    uh=1j*np.cross(K,wh,axisa=0,axisb=0,axisc=0)*invk2
    uh[:,0,0,0]=0
    nu=viscosity

    def rhs(h):
        wh=1j*np.cross(K,h,axisa=0,axisb=0,axisc=0)
        u=np.fft.ifftn(h,axes=(-3,-2,-1)).real
        w=np.fft.ifftn(wh,axes=(-3,-2,-1)).real
        lc=np.cross(u,w,axisa=0,axisb=0,axisc=0)
        lc_h=np.fft.fftn(lc,axes=(-3,-2,-1))*dealias
        lc_h=lc_h - K*np.sum(K*lc_h,axis=0)[None,...]*invk2
        return lc_h-nu*k2[None,...]*h

    def diagnostic(h, t):
        wh=1j*np.cross(K,h,axisa=0,axisb=0,axisc=0)
        u=np.fft.ifftn(h,axes=(-3,-2,-1)).real
        w=np.fft.ifftn(wh,axes=(-3,-2,-1)).real
        ow2=np.sum(w*w,axis=0)
        D=nu*float(np.sum(k2[None,...]*np.abs(wh)**2)/N**6)
        E=.5*float(np.mean(ow2))
        Kenergy=.5*float(np.mean(np.sum(u*u,axis=0)))
        G=np.array([np.fft.ifftn(1j*K[j][None,...]*h,axes=(-3,-2,-1)).real for j in range(3)])
        # G[j,i,x] = d_j u_i
        stretch=np.array([sum(w[j]*G[j,i] for j in range(3)) for i in range(3)])
        pfield=np.sum(w*stretch,axis=0)
        P=float(np.mean(pfield))
        wm=np.sum(w*np.array([-y/rho,x/rho,np.zeros_like(z)]),axis=0)
        weights=np.abs(wm)
        W=float(np.sum(weights))
        RR=float(np.sum(weights*rho)/W)
        aa=float(np.sqrt(np.sum(weights*((rho-RR)**2+z*z))/W))
        # Fit angular modes on a declared annulus. Raw Cartesian moments mix
        # harmonics due to unequal angular sampling; least squares prevents it.
        F=np.exp(-((rho-R)**2+z*z)/(2*a*a))
        region=(np.abs(rho-R)<.35)&(np.abs(z)<.40)
        angles=ph[region]
        design=np.stack([np.ones_like(angles)]+[v(m*angles) for m in range(1,5)
                     for v in (np.cos,np.sin)],axis=1)
        fit=np.linalg.lstsq(design,wm[region]/F[region],rcond=None)[0]
        coefs=[fit[2*m-1]-1j*fit[2*m] for m in (1,2,3)]
        c1,c2,c3=coefs
        z21=c2*np.conj(c1)**2/(abs(c2)*abs(c1)**2)
        z31=c3*np.conj(c1)**3/(abs(c3)*abs(c1)**3)
        divH=1j*np.sum(K*h,axis=0)
        divL2=float(np.sqrt(np.mean(np.abs(np.fft.ifftn(divH))**2)))
        # Derivative diagnostics: compare energy and enstrophy budget in next timestep.
        return dict(t=float(t),E=E,K=Kenergy,stretch=P,viscD=D,dEdt=P-D,
            R_eff=RR,a_eff=aa,delta21=float(np.angle(z21)),delta31=float(np.angle(z31)),
            amp1=float(abs(c1)),amp2=float(abs(c2)),amp3=float(abs(c3)),
            P_front=float(np.mean(pfield*(x>0))),P_back=float(np.mean(pfield*(x<0))),
            divergence_L2=divL2)
    return uh,rhs,diagnostic,K,k2


def integrate(N=40,sign=1,viscosity=.03,dt=.005,T=.10):
    h,rhs,diagnose,K,k2=make_case(N,sign,viscosity)
    steps=int(round(T/dt)); dt=T/steps
    log=[diagnose(h,0)]
    for i in range(steps):
        k1=rhs(h); k2_=rhs(h+.5*dt*k1);k3=rhs(h+.5*dt*k2_);k4=rhs(h+dt*k3)
        h=h+dt*(k1+2*k2_+2*k3+k4)/6
        if (i+1)%(max(1,steps//5))==0 or i+1==steps:
            log.append(diagnose(h,(i+1)*dt))
    # robust curl and divergence constraint guaranteed by spectral construction
    return log

if __name__=='__main__':
    arg=argparse.ArgumentParser();arg.add_argument('--N',type=int,default=40);arg.add_argument('--T',type=float,default=.10);arg.add_argument('--dt',type=float,default=.005);arg.add_argument('--out');args=arg.parse_args()
    start=time.time();res={}
    for s in (+1,-1):
        tag='phase3_positive' if s==1 else 'phase3_negative'
        res[tag]=integrate(args.N,s,dt=args.dt,T=args.T)
        print(tag,'elapsed',round(time.time()-start,2),'s')
        for x in (res[tag][0],res[tag][-1]):
            print('  ',{k:round(v,9) for k,v in x.items() if k in ('t','E','stretch','viscD','R_eff','a_eff','delta21','delta31','P_front')})
    res['configuration']={'N':args.N,'T':args.T,'dt':args.dt,'nu':.03,'R':1.65,'a':.39}
    if args.out:
        with open(args.out,'w') as f:json.dump(res,f,indent=2)
