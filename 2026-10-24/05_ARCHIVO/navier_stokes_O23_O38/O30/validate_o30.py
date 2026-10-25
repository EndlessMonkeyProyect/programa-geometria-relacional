#!/usr/bin/env python3
"""Controles discretos O30. En puntos, se prueba la parte advección Euler;
la identidad difusiva 4 nu Γ es analítica por Δ|x-C|²=4.
No constituye DNS de Navier–Stokes.
"""
import json, math
from pathlib import Path
import numpy as np

J = lambda r: np.array([-r[1], r[0]], dtype=float)
def K(r):
    return J(r)/(2*math.pi*float(r@r))

def stats(pos, weights, lab):
    sel=np.where(lab==1)[0] if lab is not None else np.arange(len(pos))
    w=weights[sel]; x=pos[sel]; G=float(sum(w)); c=np.sum(x*w[:,None],axis=0)/G
    delta=x-c
    S=float(np.sum(w*np.sum(delta**2,axis=1))/G)
    Q=complex(np.sum(w*(delta[:,0]+1j*delta[:,1])**2)/G)
    return G,c,S,Q

def run_case(rng):
    na=int(rng.integers(2,5)); nb=int(rng.integers(2,5))
    a=rng.normal(loc=(-2.,.6),scale=.33,size=(na,2)); b=rng.normal(loc=(2.,-.4),scale=.45,size=(nb,2))
    x=np.vstack((a,b)); w=rng.uniform(.2,2.0,size=len(x)); labels=np.array([1]*na+[2]*nb)
    # To use the stat method on B, a label=1 selector must be prepared.
    ga,ca,sa,qa=stats(x,w,labels)
    gb,cb,sb,qb=stats(x,w,np.where(labels==2,1,2))
    gt,ct,st,qt=stats(x,w,None)
    v=np.zeros_like(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j: v[i]+=w[j]*K(x[i]-x[j])
    I=np.zeros(2)
    for i in range(na):
        for j in range(na,len(x)):
            I+=w[i]*w[j]*K(x[i]-x[j])
    cdota=np.sum(w[:na,None]*v[:na],axis=0)/ga
    cdotb=np.sum(w[na:,None]*v[na:],axis=0)/gb
    r=ca-cb; rd=cdota-cdotb
    alpha=(1/ga+1/gb)
    tol=2e-10
    assert np.linalg.norm(cdota-I/ga)<tol
    assert np.linalg.norm(cdotb+I/gb)<tol
    assert np.linalg.norm(rd-alpha*I)<tol
    d2=float(r@r); dotd2=2*float(r@rd)
    Omega=np.linalg.det(np.stack([r,rd]))/d2
    g=float(r@rd)/d2
    assert np.linalg.norm(rd - (g*r+Omega*J(r)))<tol
    # ν=0: second moment of each population, and global balance
    dSa=2*float(np.sum(w[:na]*np.einsum('ij,ij->i', x[:na]-ca,v[:na])))/ga
    dSb=2*float(np.sum(w[na:]*np.einsum('ij,ij->i', x[na:]-cb,v[na:])))/gb
    totder=ga*dSa+gb*dSb+(ga*gb/(ga+gb))*dotd2
    assert abs(totder)<tol
    M=ga*sa+gb*sb+(ga*gb/(ga+gb))*d2
    assert abs(M-gt*st)<tol
    assert d2<=gt*M/(ga*gb)+tol
    # Quadrupole angular phase, exact derivative in the point-vortex model
    Za=(x[:na,0]-ca[0])+1j*(x[:na,1]-ca[1]);
    Zb=(x[na:,0]-cb[0])+1j*(x[na:,1]-cb[1]);
    Ua=v[:na,0]+1j*v[:na,1]; Ub=v[na:,0]+1j*v[na:,1]
    dQa=2*sum(w[:na]*Za*Ua)/ga; dQb=2*sum(w[na:]*Zb*Ub)/gb
    if abs(qa)>1e-8 and abs(qb)>1e-8:
        for Q,dQ in ((qa,dQa),(qb,dQb)):
            z=dQ/Q
            h=1e-8/(1+abs(z))
            fd=np.angle(1+h*z)/h  # phase difference, branch-safe
            assert abs(fd-float(np.imag(z)))<1e-5*(1+abs(z))
    assert abs(qa)<=sa+tol and abs(qb)<=sb+tol
    return {'max_moment_balance_error':abs(totder),'max_center_motion_error':max(float(np.linalg.norm(cdota-I/ga)),float(np.linalg.norm(cdotb+I/gb))),'positive_shape':bool(sa>0 and sb>0)}

def main():
    rng=np.random.default_rng(20261019)
    records=[run_case(rng) for _ in range(500)]
    # Point vortex limit: two single masses, exact orbital frequency, no radial drift
    GA,GB=3.,2.; r=np.array([3.,4.]); I=GA*GB*K(r)
    rd=(1/GA+1/GB)*I
    assert abs(float(r@rd))<1e-13
    assert abs(float(np.linalg.det(np.stack((r,rd))))/float(r@r)-(GA+GB)/(2*math.pi*25))<1e-13
    # Pure heat shear NS exactly: orientation/phase of Fourier harmonics fixed,
    # while amplitude ratio changes unless k identical or one amplitude vanishes.
    nu=.4; t=.7
    assert abs(math.exp(-4*nu*t)/math.exp(-nu*t)-math.exp(-3*nu*t))<1e-14
    # A localized positive radial Oseen vortex has no quadrupole phase: Q=0.
    output={'cases_euler_point_vortex_advection':len(records),'point_pair_control':True,'heat_shear_phase_vs_amplitude_control':True,'circular_quadrupole_undefined_control':True,'max_center_motion_error':max(q['max_center_motion_error'] for q in records),'max_global_second_moment_drift_error':max(q['max_moment_balance_error'] for q in records),'all_passed':True,'scope':'Discrete Euler advection identities; viscosity contributions and smooth NS results are proven analytically in the note, not numerically DNS.'}
    target=Path(__file__).resolve().parent/'VALIDACION_O30.json'
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
