#!/usr/bin/env python3
"""D4 equivariant projection for Galerkin NS on [-pi,pi)^3.
Tests the mirror quotient / unresolved Reynolds stress. No global PDE claims.
"""
from pathlib import Path
import sys,json, csv
import numpy as np
from scipy import fft
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'codigo'
sys.path.insert(0,str(SRC))
import o63_operadores as op

def group_mats():
    rot=np.array([[0,-1,0],[1,0,0],[0,0,1]],dtype=int)
    ref=np.array([[-1,0,0],[0,1,0],[0,0,1]],dtype=int)
    i=np.eye(3,dtype=int)
    return [np.linalg.matrix_power(rot,k)@mat for mat in (i,ref) for k in range(4)]

G=group_mats()

def g_apply(u,Q):
    # physical vector transformation Q u(Q.T x), exact lattice permutation
    N=u.shape[-1]
    inds=np.indices((N,N,N)).reshape(3,-1)-N//2
    old=Q.T@inds+N//2
    old%=N
    sampled=u[:,old[0],old[1],old[2]].reshape(3,N,N,N)
    return np.einsum('ab,bijk->aijk',Q,sampled,optimize=True)

def proj(u):
    return sum((g_apply(u,Q) for Q in G),start=np.zeros_like(u))/len(G)

def norm(u):
    return np.sqrt(np.mean(np.sum(u*u,axis=0)))

def state(n,eps=0):
    uh,sys=op.original_state(n,eps,False)
    return fft.ifftn(uh,axes=(-3,-2,-1)).real,sys

def from_real(u, sys):
    return fft.fftn(u,axes=(-3,-2,-1))*sys[3]

def vel_rhs(u,sys):
    rh,_=op.evaluate(from_real(u,sys),*sys,nu=op.NU)
    return fft.ifftn(rh,axes=(-3,-2,-1)).real

def projected_rhs(u,sys):
    return proj(vel_rhs(u,sys))

def trace(n=32,steps=8,dt=.004):
    u0,sys=state(n,0);up,_=state(n,.14)
    sym0=proj(u0);v=up-proj(up)
    assert norm(u0-sym0)<1e-11
    assert norm(proj(v))<1e-11
    orig_norm=norm(v)
    samples=[];aves={}
    # states u0 + c v all have EXACTLY same projected initial field
    for c in (0.,1.,2.):
        u=u0+c*v
        ah=from_real(u,sys)
        for st in range(steps+1):
            t=st*dt
            uc=fft.ifftn(ah,axes=(-3,-2,-1)).real
            ave=proj(uc)
            loss=uc-ave
            aves[(c,st)]=ave
            rhs_p=projected_rhs(uc,sys)
            rhs_cl=vel_rhs(ave,sys)
            defect=rhs_p-rhs_cl
            samples.append(dict(N=n,c=c,step=st,t=t,norm_total=norm(uc),norm_collective=norm(ave),norm_unresolved=norm(loss),norm_defect=norm(defect),err_ref=norm(ave-u0)))
            if st==steps:break
            def f(x):return op.evaluate(x,*sys,nu=op.NU)[0]
            k1=f(ah);k2=f(ah+dt*k1/2);k3=f(ah+dt*k2/2);k4=f(ah+dt*k3)
            ah=(ah+dt/6*(k1+2*k2+2*k3+k4))*sys[3]
    for row in samples:
        row["difference_from_base_trajectory"]=norm(aves[(row["c"],row["step"])]-aves[(0.,row["step"])])
    return samples,orig_norm,sys,v,u0

def test():
    import time
    allrows=[];results=[];checks={}
    for n in (32,40):
        rows,vnorm,sys,v,u0=trace(n)
        allrows+=rows
        states={c:[r for r in rows if r['c']==c] for c in (0.,1.,2.)}
        defects=[states[c][0]['norm_defect'] for c in (0.,1.,2.)]
        diffs={c: states[c][-1]['err_ref'] for c in (0.,1.,2.)}
        project_identity=norm(proj(proj(v))-proj(v))
        equiv_err=max(norm(g_apply(vel_rhs(u0+v,sys),Q)-vel_rhs(g_apply(u0+v,Q),sys)) for Q in G)
        checks[f'd4_projector_{n}']=project_identity<5e-13
        checks[f'equivariance_{n}']=equiv_err<1e-9
        checks[f'zero_defect_base_{n}']=defects[0]<1e-9
        checks[f'positive_defect_perturb_{n}']=defects[1]>1e-7
        checks[f'quadratic_defect_{n}']=abs(defects[2]/defects[1]-4)<1e-7
        checks[f'same_P_initial_{n}']=max(states[c][0]['err_ref'] for c in (0.,1.,2.))<1e-11
        # final distance to initial base is not the right difference: all evolve.
        deltas=[states[c][-1]['difference_from_base_trajectory'] for c in (0.,1.,2.)]
        checks[f'different_P_future_{n}']=deltas[2]>deltas[1]>1e-7 and deltas[0]<1e-14
        checks[f'near_quadratic_future_{n}']=3.5<deltas[2]/deltas[1]<4.5
        results.append(dict(N=n,vnorm=vnorm,defects=defects,errors_future=diffs,projected_future_differences=deltas,equivariance_error=equiv_err))
        print('N',n,'vnorm',vnorm,'defects',defects,'errs',diffs,'equiv',equiv_err,flush=True)
    with (ROOT/'resultados'/'series.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(allrows[0].keys()));w.writeheader();w.writerows(allrows)
    obj={'checks':checks,'passed':sum(checks.values()),'total':len(checks),'results':results}
    (ROOT/'resultados'/'resumen.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=lambda x: bool(x) if isinstance(x,np.bool) else float(x)))
    print(json.dumps(checks,indent=2,default=lambda x: bool(x) if isinstance(x,np.bool) else float(x)))
    assert all(checks.values()),checks
if __name__=='__main__':test()
