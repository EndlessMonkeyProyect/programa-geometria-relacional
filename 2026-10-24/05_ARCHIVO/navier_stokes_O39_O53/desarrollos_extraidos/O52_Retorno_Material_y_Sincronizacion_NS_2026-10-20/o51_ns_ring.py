#!/usr/bin/env python3
"""O51: resolved periodic Fourier-Galerkin NS from smooth toroidal vorticity.
This is a forced-free 3D incompressible Galerkin approximation, not an exact PDE solution.
Never claims that enstrophy contours are material, nor that this proves global regularity.
"""
import argparse, json, time, os
import numpy as np
from scipy import fft as spfft
from scipy.ndimage import map_coordinates

L=2*np.pi

def run(N=48, T=.60, dt=.005, nu=.025, Gamma=6., R=1., a=.35, sampler_every=10):
    xx=np.linspace(-np.pi,np.pi,N,endpoint=False)
    h=L/N
    x,y,z=np.meshgrid(xx,xx,xx,indexing='ij')
    rr=np.sqrt(x*x+y*y)
    f=Gamma/(np.pi*a*a*R)*np.exp(-((rr*rr-R*R)/(2*R*a))**2 -(z/a)**2)
    w0=np.array([-y*f,x*f,np.zeros_like(f)])
    ks=spfft.fftfreq(N,d=1./N)
    kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
    k=(kx,ky,kz)
    k2=kx*kx+ky*ky+kz*kz
    k2s=np.where(k2==0,1,k2)
    mask=(np.abs(kx)<=N//3)&(np.abs(ky)<=N//3)&(np.abs(kz)<=N//3)
    # Transform initial vorticity and invert curl to divergence-free velocity.
    wh=np.array([spfft.fftn(q) for q in w0])
    uh=np.array([1j*(ky*wh[2]-kz*wh[1])/k2s,1j*(kz*wh[0]-kx*wh[2])/k2s,1j*(kx*wh[1]-ky*wh[0])/k2s]);uh[:,0,0,0]=0
    uh*=mask
    def phys(fh):return np.array([spfft.ifftn(fi).real for fi in fh])
    def omhat(fh):return np.array([1j*(ky*fh[2]-kz*fh[1]),1j*(kz*fh[0]-kx*fh[2]),1j*(kx*fh[1]-ky*fh[0])])
    def fields(fh):
        return phys(fh),phys(omhat(fh))
    def rhs(fh, return_fields=False):
        u,omega=fields(fh)
        cross=np.cross(u,omega,axis=0)
        crosshat=np.array([spfft.fftn(q) for q in cross])
        kd=(kx*crosshat[0]+ky*crosshat[1]+kz*crosshat[2])/k2s
        proj=crosshat-np.array([kx*kd,ky*kd,kz*kd]);proj[:,0,0,0]=0
        ret=mask*(proj-nu*k2*fh)
        if return_fields:return ret,u,omega
        return ret,u
    def interp_velocity(u,pts):
        cc=np.asarray(pts)
        coords=[((cc[:,i]+np.pi)%L)/h for i in range(3)]
        return np.array([map_coordinates(ui,coords,order=1,mode='grid-wrap',prefilter=False) for ui in u]).T
    def cores(u,omega):
        weight=np.sum(omega*omega,axis=0)
        sumw=weight.sum()
        Rc=float((weight*rr).sum()/sumw)
        # Periodic circular center in z
        Zc=float(np.angle((weight*np.exp(1j*z)).sum()))
        E=float((u*u).sum()/(2*N**3))
        Ens=float(weight.sum()/(2*N**3))
        return Rc,Zc,E,Ens
    # 8 trace particles: two streamline depths, outer & inner, both at y=0, and axial shifted markers for stability
    depths=[.12,.26,.34]
    particles=[];labels=[]
    for d in depths:
        for side in [1,-1]:
            particles.append([R+side*d,0.,0.]);labels.append(f'd{d:.2f}_'+('outer' if side==1 else 'inner'))
    pts=np.array(particles,dtype=float)
    nstep=int(round(T/dt));dt=T/nstep
    samples=[]
    t_start=time.time()
    for j in range(nstep+1):
        if j%sampler_every==0 or j==nstep:
            uu,ww=fields(uh)
            Rc,Zc,energy,ens=cores(uu,ww)
            rtr=np.linalg.norm(pts[:,:2],axis=1)
            phi=np.arctan2(pts[:,2]-Zc,rtr-Rc)
            flux=interp_velocity(uu,pts)
            samples.append({'t':round(j*dt,12),'Rcore':Rc,'Zcore':Zc,'energy':energy,'enstrophy':ens,
                            'particle_phase_raw':phi.tolist(),'particles':pts.tolist(),
                            'u_z_center':float(interp_velocity(uu,np.array([[R,0,0]]))[0,2]),
                            'particle_u_z':flux[:,2].tolist()})
        if j==nstep:break
        k1,u1=rhs(uh)
        v1=interp_velocity(u1,pts)
        k2r,u2=rhs(uh+dt*k1/2)
        v2=interp_velocity(u2,pts+dt*v1/2)
        k3,u3=rhs(uh+dt*k2r/2)
        v3=interp_velocity(u3,pts+dt*v2/2)
        k4,u4=rhs(uh+dt*k3)
        v4=interp_velocity(u4,pts+dt*v3)
        uh=uh+(dt/6)*(k1+2*k2r+2*k3+k4)
        uh*=mask
        pts+=dt/6*(v1+2*v2+2*v3+v4)
        pts=(pts+np.pi)%L-np.pi
        if not np.isfinite(uh).all():raise ValueError(f'NS failed step {j}')
    # unroll phase
    phi=np.unwrap(np.array([s['particle_phase_raw'] for s in samples]),axis=0)
    zz=np.unwrap(np.array([s['Zcore'] for s in samples]))
    for i,s in enumerate(samples):
        s['particle_phase_unwrapped']=phi[i].tolist()
        s['Zcore_unwrapped']=float(zz[i])
        s['particle_phase_turns']=((phi[i]-phi[0])/(2*np.pi)).tolist()
        s['phase_difference_outer_layers_turns']=float((phi[i,2]-phi[i,0]-(phi[0,2]-phi[0,0]))/(2*np.pi))
        s['phase_difference_inner_layers_turns']=float((phi[i,3]-phi[i,1]-(phi[0,3]-phi[0,1]))/(2*np.pi))
    u,omega=fields(uh)
    divhat=1j*(kx*uh[0]+ky*uh[1]+kz*uh[2])
    diverr=float(np.max(np.abs(spfft.ifftn(divhat))))
    core_displacement=float(zz[-1]-zz[0]); duration=samples[-1]['t']
    result={'params':{'N':N,'T':T,'dt':dt,'nu':nu,'Gamma_init_param':Gamma,'R_init':R,'a_init':a,'initial_profile':'omega_theta=r*Gamma/(pi*a² R)exp(-[((r²-R²)/(2Ra))²+(z/a)²])','boundary':'3D periodic box length 2pi; vortex localized'},
            'method':'3D Fourier Galerkin 2/3 dealias, RK4, trilinear Lagrangian interpolation; no forcing',
            'tracer_labels':labels,
            'max_divergence':diverr,
            'ring_center_displacement':core_displacement,
            'mean_axial_velocity':core_displacement/duration,
            'energy_rel_change':(samples[-1]['energy']-samples[0]['energy'])/samples[0]['energy'],
            'enstrophy_rel_change':(samples[-1]['enstrophy']-samples[0]['enstrophy'])/samples[0]['enstrophy'],
            'max_abs_phase_turns':float(np.max(np.abs((phi[-1]-phi[0])/(2*np.pi)))),
            'elapsed_seconds':time.time()-t_start, 'samples':samples}
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--N',type=int,default=48);p.add_argument('--T',type=float,default=.6);p.add_argument('--dt',type=float,default=.005);p.add_argument('--nu',type=float,default=.025);p.add_argument('--Gamma',type=float,default=6);p.add_argument('--a',type=float,default=.35);p.add_argument('--out',type=str,default='results.json')
    args=p.parse_args();r=run(N=args.N,T=args.T,dt=args.dt,nu=args.nu,Gamma=args.Gamma,a=args.a)
    with open(args.out,'w') as f:json.dump(r,f,indent=2)
    for key in ['max_divergence','ring_center_displacement','mean_axial_velocity','energy_rel_change','enstrophy_rel_change','max_abs_phase_turns','elapsed_seconds']:
        print(key,r[key])
    print('phase turns (final)',r['samples'][-1]['particle_phase_turns'])
    print('phase outer layer differential turns',r['samples'][-1]['phase_difference_outer_layers_turns'])
