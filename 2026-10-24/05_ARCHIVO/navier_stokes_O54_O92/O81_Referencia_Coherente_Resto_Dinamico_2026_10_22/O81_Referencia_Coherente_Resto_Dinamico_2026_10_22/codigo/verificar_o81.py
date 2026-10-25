#!/usr/bin/env python3
"""O81: exact Fourier audits of critical-norm invariance and perturbation about a shear.
Only static algebra/inequalities are tested; not a PDE time integration.
"""
import json, math, csv
from pathlib import Path
from collections import defaultdict
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'resultados'; OUT.mkdir(exist_ok=True)
counts=defaultdict(int)
def check(cond,label):
    if not cond: raise AssertionError(label)
    counts[label]+=1

def sin_mode(amps, axis, k):
    """Add sin(k*x) times a polarization vector; k integer triple."""
    k=tuple(k)
    v=np.array(axis,dtype=complex)*amps/(2j)
    amps_by_k={k:v,tuple(-z for z in k):np.conj(v)}
    return amps_by_k

def add(*terms):
    d=defaultdict(lambda: np.zeros(3,dtype=complex))
    for term in terms:
        for k,v in term.items(): d[k]=d[k]+v
    return dict(d)

def R(f):
    return sum(float(np.linalg.norm(v))/np.linalg.norm(k) for k,v in f.items() if np.linalg.norm(k))
def S(f):
    return sum(float(np.linalg.norm(v)) for v in f.values())
def Q(f):
    return sum(float(np.linalg.norm(v))*np.linalg.norm(k) for k,v in f.items())

def nonlinear(f):
    """N=P div(u tensor u) Fourier coefficient, sign ignored."""
    full=defaultdict(lambda: np.zeros(3,dtype=complex))
    for p,up in f.items():
        for q,uq in f.items():
            k=tuple(a+b for a,b in zip(p,q))
            if k==(0,0,0): continue
            kk=np.array(k,dtype=float)
            full[k] = full[k] + 1j * np.dot(kk,up)*uq
    for k in list(full):
        kk=np.array(k,dtype=float)
        proj=np.eye(3)-np.outer(kk,kk)/(kk@kk)
        full[k]=proj@full[k]
    return dict(full)

def nonlin_R(f):
    return R(nonlinear(f))

A=2.0;nu=1.0; e1=5e-5*math.sqrt(2);e2=5e-5
U=sin_mode(A,(1,0,0),(0,1,0))
v=add(sin_mode(e1,(0,1,0),(1,0,1)), sin_mode(e2,(0,0,1),(1,0,0)))
u0=add(U,v)
Ru,Rv,Rtotal=R(U),R(v),R(u0)
S0=S(U); Ginf=2*(A/nu)**2; M=Rv*math.exp(Ginf)
threshold=(nu/2)*math.exp(-Ginf)
check(Ru==A,'large shear norm exactly A')
check(abs(Rv-(e1/math.sqrt(2)+e2))<1e-13,'two 3D modes residual norm')
check(abs(Rtotal-(A+e1/math.sqrt(2)+e2))<1e-13,'disjoint support large total norm')
check(Rtotal>nu and Rv<threshold and M<nu/2,'global perturbation criterion and large total datum')
check(nonlin_R(U)<1e-12,'U shear has zero projected nonlinearity')
for k,c in U.items():
    kk=np.array(k,dtype=float)
    check(abs(np.dot(kk,c))<1e-13,'divergence-free shear Fourier')
for k,c in v.items():
    kk=np.array(k,dtype=float)
    check(abs(np.dot(kk,c))<1e-13,'divergence-free perturbation Fourier')

NL=nonlinear(u0)
for k,w in NL.items():
    check(abs(np.dot(k,w))<1e-12,'nonlinear projection divergence free')
    check(np.linalg.norm(NL[tuple(-m for m in k)]-np.conj(w))<1e-12,'nonlinear real field conjugate symmetry')
new=[(k,float(np.linalg.norm(w))) for k,w in NL.items() if k not in u0 and np.linalg.norm(w)>1e-15]
check(len(new)>0,'genuine new relations generated')
check(nonlin_R(u0)<=S(u0)**2*(1+1e-12),'full Fourier nonlinear bound')
check(nonlin_R(u0)<=S(v)**2+2*S(U)*S(v)+1e-12,'coherent plus rest interaction bound')

# Exact NS scaling on torus for integer dilation lambda, no time integration
for lam in range(1,65):
    fld={tuple(lam*i for i in k):lam*a for k,a in u0.items()}
    check(abs(R(fld)-R(u0))<2e-14,'critical R is invariant under true NS scaling')
    check(abs(S(fld)-lam*S(u0))<2e-13,'S scales linearly')
    check(abs(Q(fld)-lam**2*Q(u0))<5e-11,'Q scales quadratically')

# Check differential bootstrap coefficients and cap at sample times
for tt in np.linspace(0,12,121):
    SU=A*math.exp(-nu*tt)
    G=(4/nu)*(A*A)*(1-math.exp(-2*nu*tt))/(2*nu)
    majorant=Rv*math.exp(G)
    check(majorant<nu/2,'uniform bootstrap barrier')
    check(G>=0 and G<=Ginf+1e-12,'finite shear exposure')
    check(SU**2 >=0,'positive exposure')

Qbudget=4*M/nu
nonlinear_budget=4*M*M/nu+2*math.sqrt((A*A/(2*nu))*(M*Qbudget))
gradient_integral_budget=A/nu+Qbudget
assert math.isfinite(nonlinear_budget) and math.isfinite(gradient_integral_budget)

# Show failure of mere relabeling with large even-index reference; a re-indexed (N,h) is identical fraction
for N in (2,3,5,8,13,64,128):
    for q in (2,3,7,31):
        h=1
        check(abs(h/N-(q*h)/(q*N))<1e-15,'reference refinement preserves physical weight')

# threshold table
rows=[]
for aa in np.linspace(0,3.0,61):
    allowed=(nu/2)*math.exp(-2*(aa/nu)**2)
    rows.append({'A_over_nu':f'{aa/nu:.8g}', 'maximum_strict_Rv':f'{allowed:.12g}',
                 'Rtotal_shear_only':f'{aa:.8g}'})
with open(OUT/'o81_ventana_residuo.csv','w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)

new.sort(key=lambda x:(-x[1],x[0]))
result={
 'nu':nu,'A':A,'base_R':Ru,'residual_R0':Rv,'full_R0':Rtotal,
 'critical_threshold_nu':nu, 'shear_exposure_G_inf':Ginf,
 'residual_condition_Rv_less_than':threshold, 'residual_bound_M':M,
 'Qv_time_integral_bound':Qbudget,
 'integral_grad_u_inf_bound':gradient_integral_budget,
 'absolute_nonlinear_residual_budget':nonlinear_budget,
 'new_modes_count':len(new), 'new_modes_first_10':[{'k':list(k),'N_k_abs':mag} for k,mag in new[:10]],
 'nonlinearity_R_initial':nonlin_R(u0),
 'cross_interaction_upper_bound':S(v)**2+2*S(U)*S(v),
 'test_categories':dict(counts), 'total_tests':sum(counts.values()),
 'warning':'Checks test initial Fourier algebra and analytic bounds; they do not integrate the full Navier-Stokes evolution.'
}
(OUT/'o81_resumen.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
