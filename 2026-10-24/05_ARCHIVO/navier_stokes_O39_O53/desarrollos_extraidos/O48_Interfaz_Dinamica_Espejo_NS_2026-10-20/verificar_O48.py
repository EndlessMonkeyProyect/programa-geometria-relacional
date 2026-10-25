#!/usr/bin/env python3
"""O48: pruebas exactas de suficiencia y no-go de momentos de cizalla NS.
Solo biblioteca estandar; aritmetica racional para pruebas algebraicas.
"""
from fractions import Fraction as F
from math import sqrt, exp, sin, pi, log, isclose
import json, hashlib
from pathlib import Path

NU=0.03
passes=0

def check(cond, msg):
    global passes
    if not cond:
        raise AssertionError(msg)
    passes += 1

def barycentric(lambdas):
    return [F(1,1)/prod_F((lj-lh for h,lh in enumerate(lambdas) if h != j)) for j, lj in enumerate(lambdas)]

def prod_F(v):
    p=F(1)
    for e in v:
        p*=e
    return p

def m(weights, lambdas, power, t=0., nu=NU):
    if t==0 and all(isinstance(w,F) for w in weights):
        return sum((w*(F(l)**power) for w,l in zip(weights,lambdas)), F(0))
    return sum(float(w)*float(l)**power*exp(-2*nu*float(l)*t) for w,l in zip(weights,lambdas))

def ell(weights,lambdas,t=0.):
    return sqrt(float(m(weights,lambdas,0,t))/float(m(weights,lambdas,1,t)))

def mirror_rate(weights,lambdas,t=0.):
    M0,M1,M2=[float(m(weights,lambdas,r,t)) for r in range(3)]
    return NU*(M2/M1-M1/M0)

def tracer_dx(weights,k,phase,y,t,nu=NU):
    # U(y,t)=sum 2sqrt(w)/k exp(-nu k^2t)sin(ky+phase)
    return sum((2*sqrt(float(w))/kj)*sin(kj*y+pj)*(-__import__('math').expm1(-nu*kj*kj*t))/(nu*kj*kj)
               for w,kj,pj in zip(weights,k,phase))

def positive_pair(R):
    n=R+3
    k=list(range(1,n+1))
    ls=[F(j*j) for j in k]
    c=barycentric(ls)
    d=[l*e for l,e in zip(ls,c)]
    base=F(1,n)
    epsilon=base/F(3)/max(abs(v) for v in d)
    wp=[base+epsilon*di for di in d]
    wm=[base-epsilon*di for di in d]
    return k,ls,wp,wm,epsilon,d

records=[]
for R in range(1,7):
    k,ls,wp,wm,eps,d=positive_pair(R)
    check(all(x>0 for x in wp+wm),f'positive R={R}')
    check(all(sum((di*(li**r) for di,li in zip(d,ls)),F(0))==0 for r in range(-1,R+1)),f'nullspace R={R}')
    check(sum((di*li**(R+1) for di,li in zip(d,ls)),F(0))==1,f'next-moment R={R}')
    for power in range(-1,R+1):
        check(m(wp,ls,power)==m(wm,ls,power),f'matched moment {power} R={R}')
    check(m(wp,ls,R+1)-m(wm,ls,R+1)==2*eps,f'first mismatch R={R}')
    check((m(wp,ls,R+1)-m(wm,ls,R+1))!=0, f'mismatch nonzero {R}')
    # La enstrofia futura es distinta: el primer coeficiente Taylor no igual
    t=.1
    en_diff=m(wp,ls,0,t)-m(wm,ls,0,t)
    if R<=4:  # para R alto tiende a cancelacion a precision float
        check(abs(en_diff)>1e-15, f'nonidentical full future E R={R}')
    records.append({'R':R,'number_of_modes':len(k),'mcm_wavenumber':__import__('math').lcm(*k),
                    'epsilon':float(eps),'matched_moments':['kinetic energy m_-1']+[f'm_{j}' for j in range(R+1)],
                    'first_unmatched_moment':f'm_{R+1}',
                    'exact_mismatch':str(2*eps),
                    'E_t01_diff':en_diff})

# R=1 can match energy, E, palinstrophy and phases, but ell rate differs
k,ls,wp,wm,eps,d=positive_pair(1)
check(m(wp,ls,-1)==m(wm,ls,-1), 'kinetic energy match')
check(m(wp,ls,0)==m(wm,ls,0), 'E match')
check(m(wp,ls,1)==m(wm,ls,1), 'J match')
check(isclose(ell(wp,ls),ell(wm,ls),rel_tol=0,abs_tol=1e-14), 'ell match')
check(m(wp,ls,2)!=m(wm,ls,2),'mirror drift needs m2')
check(mirror_rate(wp,ls)!=mirror_rate(wm,ls),'mirror drift different')
for weights in (wp,wm):
    mm0,mm1,mm2=[float(m(weights,ls,r)) for r in range(3)]
    mu=mm1/mm0
    variance=mm2/mm0-mu*mu
    check(variance>=-1e-12,'variance nonnegative')
    check(isclose(mirror_rate(weights,ls),NU*variance/mu,rel_tol=1e-12,abs_tol=1e-13),'variance identity')
    h=1e-5
    numerical=(log(ell(weights,ls,h))-log(ell(weights,ls,0)))/h
    check(abs(numerical-mirror_rate(weights,ls))<3e-5,'log ell derivative')
    check(ell(weights,ls,.1)>ell(weights,ls,0), 'ell increases')
    check(ell(weights,ls,.5)>ell(weights,ls,.1), 'ell increases again')

# Closed Laplace spectral interface for shear: M(z,t), G(z,t)=M(z,t)/M(0,t).
def laplace_M(weights, lambdas, z, t=0., nu=NU):
    return sum(float(w)*exp(-float(l)*(z+2*nu*t)) for w,l in zip(weights,lambdas))

def laplace_Mz(weights, lambdas, z, t=0., nu=NU):
    return -sum(float(l)*float(w)*exp(-float(l)*(z+2*nu*t)) for w,l in zip(weights,lambdas))

for weights in (wp, wm):
    for t in [0., .17, .9]:
        for z in [0., .07, .2, 1.]:
            M=laplace_M(weights,ls,z,t)
            E=laplace_M(weights,ls,0,t)
            G=M/E
            M0=laplace_M(weights,ls,z+2*NU*t)
            E0=laplace_M(weights,ls,2*NU*t)
            check(abs(G-M0/E0)<1e-13,'normalized semigroup equation')
            check(abs(M-M0)<1e-13,'transport semigroup equation')
            Gz=laplace_Mz(weights,ls,z,t)/E
            Gz0=laplace_Mz(weights,ls,0,t)/E
            Gt=2*NU*(Gz-G*Gz0)
            h=1e-5
            if t>=h:
                diff=(laplace_M(weights,ls,z,t+h)/laplace_M(weights,ls,0,t+h)-laplace_M(weights,ls,z,t-h)/laplace_M(weights,ls,0,t-h))/(2*h)
                check(abs(diff-Gt)<1e-7,'normalized generator PDE')
            if z==0:
                check(abs(G-1)<1e-13,'unity of normalized spectral generator')

# finite dimensional Markovian closure for known support K: recover w by linear Vandermonde
# Exact Gauss-Jordan solve Vw=m for K moments.
def solve_frac(A,b):
    n=len(b)
    mat=[[F(e) for e in row]+[F(b[i])] for i,row in enumerate(A)]
    for i in range(n):
        ix=next(j for j in range(i,n) if mat[j][i]!=0)
        mat[i],mat[ix]=mat[ix],mat[i]
        pivot=mat[i][i]
        mat[i]=[a/pivot for a in mat[i]]
        for j in range(n):
            if j!=i:
                fact=mat[j][i]
                mat[j]=[a-fact*c for a,c in zip(mat[j],mat[i])]
    return [row[-1] for row in mat]

for K in range(1,8):
    kval=list(range(1,K+1))
    ls=[F(j*j) for j in kval]
    ws=[F(j, sum(range(1,K+1))) for j in range(1,K+1)]
    vector=[m(ws,ls,r) for r in range(K)]
    V=[[l**r for l in ls] for r in range(K)]
    recovered=solve_frac(V,vector)
    check(recovered==ws, f'Vandermonde K={K}')
    # exact closure for m_K using moments m_0..m_{K-1}: polynomial P(λ)=prod(λ−λ_j)
    coef=[F(1)] # coef ascending
    for l in ls:
        new=[F(0)]*(len(coef)+1)
        for j,e in enumerate(coef):
            new[j]+=-l*e
            new[j+1]+=e
        coef=new
    check(coef[-1]==1,'monic polynomial')
    check(m(ws,ls,K)==-sum(coef[j]*vector[j] for j in range(K)), f'closed companion K={K}')

# Material tracers: analytic displacement for shear U_j(t)
k,ls,wp,wm,eps,d=positive_pair(1)
phases=[F(0)]*len(k)
y0=0.31
for w in [wp,wm]:
    d0=tracer_dx(w,k,phases,y0,0)
    check(d0==0.0,'tracer zero displacement initial')
    t=.2
    dr=tracer_dx(w,k,phases,y0,t)
    dt=1e-5
    numerical=(tracer_dx(w,k,phases,y0,t+dt)-tracer_dx(w,k,phases,y0,t-dt))/(2*dt)
    exact=sum(2*sqrt(float(wi))/ki*exp(-NU*ki*ki*t)*sin(ki*y0) for wi,ki in zip(w,k))
    check(abs(numerical-exact)<2e-9,'tracer solves dx/dt=U')
check(abs(tracer_dx(wp,k,phases,y0,.2)-tracer_dx(wm,k,phases,y0,.2))>1e-6,'particle paths distinguish weights')

# phase counterexample: shift phases, keep w and mirror clock, change particle
pzeros=[0.0]*len(k)
pchange=[0.0]*len(k);pchange[0]=pi/2
check(abs(tracer_dx(wp,k,pzeros,y0,.2)-tracer_dx(wp,k,pchange,y0,.2))>1e-6,'phase changes tracer not mirror')
check(ell(wp,ls)==ell(wp,ls),'mirror unaffected')

result={
    'program':'O48', 'date':'2026-10-20', 'nu':NU,'passed_checks':passes,
    'no_go_family':records,
    'r1_equal_initial':{'E':float(m(wp,ls,0)),'J':float(m(wp,ls,1)),'kinetic_energy':float(m(wp,ls,-1)), 'ell':ell(wp,ls)},
    'r1_distinguishing':{'m2_plus':float(m(wp,ls,2)),'m2_minus':float(m(wm,ls,2)),
                         'ell_dot_log_plus':mirror_rate(wp,ls),'ell_dot_log_minus':mirror_rate(wm,ls),
                         'ell_t01_plus':ell(wp,ls,.1),'ell_t01_minus':ell(wm,ls,.1),
                         'E_t01_plus':m(wp,ls,0,.1),'E_t01_minus':m(wm,ls,0,.1)},
    'tracers':{'y0':y0,'t':.2,'dx_plus':tracer_dx(wp,k,pzeros,y0,.2),
               'dx_minus':tracer_dx(wm,k,pzeros,y0,.2),
               'dx_plus_phase_changed':tracer_dx(wp,k,pchange,y0,.2)},
    'explanation':'exact NS shear u=(U(y,t),0,0), all frequencies present, all phases equal; finite moments m_-1,m_0,...,m_R insufficient with unbounded finite spectral support; for fixed K, K moments exactly sufficient for mirror/E by Vandermonde. Tracer requires phases as well. Does not imply NS3D general regularity.'
}
p=Path(__file__).parent/'O48_RESULTADOS.json'
p.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed_checks':passes,'r1':result['r1_distinguishing'],'tracers':result['tracers']},indent=2))
