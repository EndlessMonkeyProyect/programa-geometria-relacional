#!/usr/bin/env python3
"""O53 Fourier–Galerkin, unforced periodic incompressible Navier–Stokes.
Reuses O51/O52 base ring with a quantified non-axisymmetric solenoidal
perturbation constructed as the curl of a smooth vector potential.
This is numerical finite-mode NS; it is NOT exact PDE regularity evidence.
"""
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy import fft as fft
from scipy.ndimage import map_coordinates

L=2*np.pi

def run(N=32, T=1.2, dt=0.008, epsilon=0.12, nu=0.025,
        gamma=6., R=1., a=.35, sample_every=5, match_energy=False):
    c=np.linspace(-np.pi,np.pi,N,endpoint=False)
    x,y,z=np.meshgrid(c,c,c,indexing='ij'); h=L/N
    rr=np.sqrt(x*x+y*y); rr_safe=np.maximum(rr,1e-12)
    g=np.exp(-((rr*rr-R*R)/(2*R*a))**2-(z/a)**2)
    f=gamma/(np.pi*a*a*R)*g
    omega_init=np.stack((-y*f,x*f,np.zeros_like(f)))
    k1=fft.fftfreq(N,d=1/N)
    kx,ky,kz=np.meshgrid(k1,k1,k1,indexing='ij')
    ks=np.stack((kx,ky,kz)); k2=kx*kx+ky*ky+kz*kz
    k2safe=np.where(k2==0,1,k2)
    mask=(np.abs(kx)<=N//3)&(np.abs(ky)<=N//3)&(np.abs(kz)<=N//3)
    ik=1j*ks
    def hats(a):return fft.fftn(a,axes=(-3,-2,-1))
    def vals(a):return fft.ifftn(a,axes=(-3,-2,-1)).real
    def cross_hat(a):
        return np.stack((1j*(ky*a[2]-kz*a[1]),1j*(kz*a[0]-kx*a[2]),1j*(kx*a[1]-ky*a[0])))
    wh=hats(omega_init)
    uh_base=cross_hat(wh)/k2safe
    uh_base[:,0,0,0]=0
    uh_base*=mask
    # Explicitly nonaxisymmetric, smooth perturbation, prescribed *relative velocity L2*.
    # A=(0,g x/R,g y/R) is a vector potential; curl(A) is divergence-free.
    Avec=np.stack((np.zeros_like(g),g*x/R,g*y/R))
    uh_pert=cross_hat(hats(Avec))*mask
    uh_pert[:,0,0,0]=0
    unorm=float(np.linalg.norm(uh_base))
    pnorm=float(np.linalg.norm(uh_pert))
    assert unorm>0 and pnorm>0
    uh=uh_base+epsilon*(unorm/pnorm)*uh_pert
    if match_energy:
        uh*=unorm/float(np.linalg.norm(uh))
    uh*=mask
    h=2*np.pi/N
    def fields(fh):return vals(fh), vals(cross_hat(fh))
    def rhs(fh):
        u,om=fields(fh)
        ct=np.cross(u,om,axis=0)
        ch=hats(ct)
        dot=(ks*ch).sum(axis=0)/k2safe
        pp=ch-ks*dot
        pp[:,0,0,0]=0
        return mask*(pp-nu*k2*fh),u
    def interp(u,pts):
        coords=[((pts[:,i]+np.pi)%L)/h for i in range(3)]
        return np.stack([map_coordinates(q,coords,order=1,mode='grid-wrap',prefilter=False) for q in u],axis=1)
    def diagnostics(fh,full=False):
        u,om=fields(fh)
        ww=(om*om).sum(axis=0)
        wsum=ww.sum()
        Zc=float(np.angle((ww*np.exp(1j*z)).sum()))
        Rc=float((ww*rr).sum()/wsum)
        energy=float((u*u).sum()/(2*N**3))
        ens=float(wsum/(2*N**3))
        omh=cross_hat(fh)
        palin=float((k2*np.abs(omh)**2).sum()/N**6)
        ell=float(np.sqrt(2*ens/palin))
        # Global axial swirl: nonzero denotes 3D symmetry-breaking component.
        uphi=(x*u[1]-y*u[0])/rr_safe
        swirl=float(np.sqrt(np.mean(uphi**2)))
        if not full:return (Rc,Zc,energy,ens,palin,ell,swirl),u
        # Stretching P = <om_i om_j d_j u_i>; exact Galerkin quadrature for retained modes.
        dvel=vals(ik[:,None]*fh[None,:])  # (derivative j, velocity i, spatial)
        grad_stretch=np.einsum('i...,j...,ji...->...',om,om,dvel,optimize=True)
        P=float(np.mean(grad_stretch))
        D=float(nu*palin)
        divhat=(ks*fh).sum(axis=0)*1j
        div=float(np.max(np.abs(vals(divhat))))
        return (Rc,Zc,energy,ens,palin,ell,swirl,P,D,div),u
    pts=[];labels=[]
    for d in [.12,.26,.34]:
        for side in [1,-1]:
            pts.append((R+side*d,0.,0.));labels.append(f'd{d:.2f}_'+('out' if side==1 else 'in'))
    pts=np.array(pts,dtype=float)
    nsteps=int(round(T/dt));dt=T/nsteps
    records=[]
    t0=time.time()
    for j in range(nsteps+1):
        if j%sample_every==0 or j==nsteps:
            diag,u=diagnostics(uh,full=True)
            Rc,Zc,energy,ens,palin,ell,swirl,P,D,div=diag
            pr=np.linalg.norm(pts[:,:2],axis=1)
            ph=np.arctan2(pts[:,2]-Zc,pr-Rc)
            records.append(dict(t=j*dt,Rc=Rc,Zc=Zc,energy=energy,enstrophy=ens,palinstrophy=palin,
                                ell_omega=ell,swirl_rms=swirl,stretching_P=P,dissipation_D=D,
                                divergence_max=div,phase_raw=ph.tolist(),particles=pts.tolist()))
        if j==nsteps:break
        k1r,u1=rhs(uh);v1=interp(u1,pts)
        k2r,u2=rhs(uh+dt*k1r/2);v2=interp(u2,pts+dt*v1/2)
        k3r,u3=rhs(uh+dt*k2r/2);v3=interp(u3,pts+dt*v2/2)
        k4r,u4=rhs(uh+dt*k3r);v4=interp(u4,pts+dt*v3)
        uh+=dt/6*(k1r+2*k2r+2*k3r+k4r)
        uh*=mask
        pts+=dt/6*(v1+2*v2+2*v3+v4)
        pts=(pts+np.pi)%L-np.pi
        if not np.isfinite(uh).all():raise RuntimeError('nonfinite NS coefficients')
    raw=np.array([i['phase_raw'] for i in records]);p=np.unwrap(raw,axis=0)
    zz=np.unwrap(np.array([i['Zc'] for i in records]));
    for i,s in enumerate(records):
        turns=(p[i]-p[0])/(2*np.pi)
        s['phase_turns']=turns.tolist()
        s['outer_diff_turns']=float(turns[2]-turns[0])
        s['inner_diff_turns']=float(turns[3]-turns[1])
        s['Zc_unwrapped']=float(zz[i])
    es=np.array([r['energy'] for r in records]); ee=np.array([r['enstrophy'] for r in records]);
    pp=np.array([r['stretching_P'] for r in records]);dd=np.array([r['dissipation_D'] for r in records]);
    tt=np.array([r['t'] for r in records]);
    energy_balance=float((es[-1]-es[0]+2*nu*np.trapezoid(ee,tt))/es[0]);
    enstrophy_balance=float((ee[-1]-ee[0]-np.trapezoid(pp-dd,tt))/ee[0]);
    return dict(params=dict(N=N,T=T,dt=dt,nu=nu,epsilon=epsilon,gamma=gamma,R=R,a=a,match_energy=bool(match_energy),
                            perturbation='curl A, A=(0,g*x/R,g*y/R), g=exp[-((r²-R²)/(2Ra))²-(z/a)²]; L2 velocity epsilon ratio',
                            boundaries='periodic [-pi,pi)^3',method='Fourier Galerkin 2/3 mask RK4, trilinear tracers'),
                tracer_labels=labels,
                stats=dict(axial_displacement=float(zz[-1]-zz[0]),outer_phase_diff_final=float(records[-1]['outer_diff_turns']),
                           ell_change=float(records[-1]['ell_omega']-records[0]['ell_omega']),
                           kinetic_change_fraction=float(es[-1]/es[0]-1),
                           enstrophy_change_fraction=float(ee[-1]/ee[0]-1),
                           initial_swirl_rms=float(records[0]['swirl_rms']),
                           initial_P=float(pp[0]),initial_D=float(dd[0]),
                           max_abs_divergence=float(max(r['divergence_max'] for r in records)),
                           energy_balance_rel=energy_balance,enstrophy_balance_rel=enstrophy_balance,
                           elapsed=float(time.time()-t0)),
                records=records)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--N',type=int,default=32);ap.add_argument('--T',type=float,default=1.2)
    ap.add_argument('--dt',type=float,default=.008);ap.add_argument('--epsilon',type=float,default=.12)
    ap.add_argument('--out',type=str,default='run.json')
    a=ap.parse_args();res=run(N=a.N,T=a.T,dt=a.dt,epsilon=a.epsilon)
    Path(a.out).write_text(json.dumps(res,indent=2,ensure_ascii=False))
    print(json.dumps({'params':res['params'],'stats':res['stats']},indent=2))
