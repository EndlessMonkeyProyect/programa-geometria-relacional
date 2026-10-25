#!/usr/bin/env python3
"""O37: pruebas numéricas deterministas y control de resultados exactos.
La cuadratura de Biot-Savart evalúa solo la derivada inicial, NO evoluciona NS.
"""
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.integrate import quad

NU=0.02; GAMMA=1.; A=.9; B=.5; THETA=.35

def samples(theta=0.,d=12.,Nr=32,Nphi=64):
    # densidad radial C-infinito, soporte unitario, transformada elíptica
    rr,ww=leggauss(Nr); rr=(rr+1)/2; ww=ww/2
    aa=2*np.pi*np.arange(Nphi)/Nphi
    R, PH=np.meshgrid(rr,aa,indexing='ij')
    W0=ww[:,None]*R * np.exp(-1/(1-R*R)) * np.ones((1,Nphi)) * (2*np.pi/Nphi)
    W=W0.ravel(); W=W/W.sum()
    s=np.stack([R.ravel()*np.cos(PH.ravel()), R.ravel()*np.sin(PH.ravel())],axis=-1)
    base=np.column_stack([A*s[:,0],B*s[:,1]])
    cr,sr=np.cos(theta),np.sin(theta)
    x=np.column_stack([cr*base[:,0]-sr*base[:,1], sr*base[:,0]+cr*base[:,1]])
    return x,W

def samples_poly(theta=0., k=8, Nr=32, Nphi=64):
    # Densidad compacta C^(k-1): rho=(k+1)/pi * (1-|s|^2)^k en el disco.
    rr,ww=leggauss(Nr); rr=(rr+1)/2; ww=ww/2
    aa=2*np.pi*np.arange(Nphi)/Nphi
    R, PH=np.meshgrid(rr,aa,indexing='ij')
    W0=ww[:,None]*R*(1-R*R)**k*np.ones((1,Nphi))*(2*np.pi/Nphi)
    W=W0.ravel();W=W/W.sum()
    s=np.stack([R.ravel()*np.cos(PH.ravel()),R.ravel()*np.sin(PH.ravel())],axis=-1)
    base=np.column_stack([A*s[:,0],B*s[:,1]])
    cr,sr=np.cos(theta),np.sin(theta)
    x=np.column_stack([cr*base[:,0]-sr*base[:,1],sr*base[:,0]+cr*base[:,1]])
    return x,W

def cross_qdot(Axy,Aw,Bxy,Bw, cA, cB):
    # only U_B(x_A) from Biot-Savart, no advection by self; self-rate cancels
    dest=Axy+np.array(cA)
    src=Bxy+np.array(cB)
    U=np.empty_like(dest)
    for i in range(len(dest)):
        r=dest[i]-src
        rsq=np.einsum('ij,ij->i',r,r)
        v=np.stack([-r[:,1],r[:,0]],axis=1)/(2*np.pi*rsq[:,None])
        U[i]=GAMMA*(Bw[:,None]*v).sum(axis=0)
    zd=Axy[:,0]+1j*Axy[:,1]
    ud=U[:,0]+1j*U[:,1]
    return 2*np.sum(Aw*zd*ud)

def test_phase(d,theta=THETA,Nr=32,Nphi=64):
    xa,wa=samples(0,d,Nr,Nphi)
    xb,wb=samples(theta,d,Nr,Nphi)
    qA=np.sum(wa*(xa[:,0]+1j*xa[:,1])**2)
    qB=np.sum(wb*(xb[:,0]+1j*xb[:,1])**2)
    S=np.sum(wa*(xa**2).sum(axis=1))
    dqA=cross_qdot(xa,wa,xb,wb,(-d/2,0),(d/2,0))
    dqB=cross_qdot(xb,wb,xa,wa,(d/2,0),(-d/2,0))
    f=float(np.imag(dqA/qA-dqB/qB))
    psi=-2*theta
    dE=math.sin(psi)*f
    leading=-(GAMMA*S/(math.pi*qA.real*d*d))*(1-math.cos(2*theta))
    return dict(d=d,theta=theta,S=float(S),Qabs=float(abs(qA)),f=f,leading=leading,dE=float(dE),relative_error=float(abs(f-leading)/abs(leading)))

def radial_gaussian_overlap(t,s1=.36,s2=1.44,nu=.02):
    # Solución exacta NS para dos vorticidades radiales concéntricas gaussianas.
    sig1=s1+2*nu*t; sig2=s2+2*nu*t
    def fn(r):
        a=math.exp(-r*r/(2*sig1))/(2*math.pi*sig1)
        b=math.exp(-r*r/(2*sig2))/(2*math.pi*sig2)
        return 2*math.pi*r*a*b/(a+b) if a+b else 0
    val,err=quad(fn,0,40*math.sqrt(max(sig1,sig2)),epsabs=1e-12)
    return val

def get_m():
    x,w=samples(0)
    S=(w*(x*x).sum(axis=1)).sum()
    return float(S)

def main():
    results={}
    # exact algebra and covariance/weights checks
    x,w=samples(0)
    assert abs(w.sum()-1)<1e-13
    assert np.linalg.norm(np.sum(w[:,None]*x,axis=0))<1e-12
    S=float((w*(x*x).sum(axis=1)).sum()); Q=complex((w*(x[:,0]+1j*x[:,1])**2).sum())
    assert abs(Q.imag)<1e-13 and Q.real>0
    assert abs(S/Q.real - (A*A+B*B)/(A*A-B*B))<1e-12
    results['initial_moments']={'S':S,'Q':Q.real,'anisotropy':Q.real/S}
    # Caso con momentos cerrados y soporte realmente disjunto: rho proporcional a (1-r²)^8.
    pa,pwa=samples_poly(theta=0.,k=8,Nr=32,Nphi=64)
    pb,pwb=samples_poly(theta=-THETA,k=8,Nr=32,Nphi=64)
    Sp=float((pwa*(pa*pa).sum(axis=1)).sum())
    Qp=float(np.real(np.sum(pwa*(pa[:,0]+1j*pa[:,1])**2)))
    S_exact=(A*A+B*B)/(2*(8+2))
    Q_exact=(A*A-B*B)/(2*(8+2))
    assert abs(Sp-S_exact)<1e-12
    assert abs(Qp-Q_exact)<1e-12
    d_analytic=4000.
    # Cota explícita y rigurosa del resto multipolar para soportes en radio <= A
    bound_remainder=56*GAMMA*A**3/(d_analytic-2*A)**3
    bound_lead=GAMMA*S_exact*(1-math.cos(2*THETA))/d_analytic**2
    assert bound_remainder<bound_lead
    results['rigorous_compact_support_example']={'k':8,'a':A,'b':B,'theta_B':-THETA,'separation_certified':d_analytic,
       'S':S_exact,'Qabs':Q_exact,'leading_coefficient_after_divide_Q':bound_lead/(math.pi*Q_exact),
       'remainder_bound_after_divide_Q':bound_remainder/(math.pi*Q_exact)}
    # Biot-Savart instantáneo de las dos copias compactas y orientaciones opuestas (d=12).
    d_comp=12.
    dotQA=cross_qdot(pa,pwa,pb,pwb,(-d_comp/2,0),(d_comp/2,0))
    dotQB=cross_qdot(pb,pwb,pa,pwa,(d_comp/2,0),(-d_comp/2,0))
    QB=Q_exact*np.exp(-2j*THETA)
    phase_change=float(np.imag(dotQA/Q_exact-dotQB/QB))
    assert phase_change<0
    results['compact_pair_d12_instantaneous_diagnostic']={'d':d_comp,'phase_derivative_numerical':phase_change,
         'E_derivative_numerical':math.sin(2*THETA)*phase_change}
    # two nonlinear NS instantaneous pair cases with opposite angular signs
    cases=[]
    for d in (6.,12.,24.,48.):
        case=test_phase(d,+THETA,Nr=24,Nphi=48)
        other=test_phase(d,-THETA,Nr=24,Nphi=48)
        assert case['f']<0 and other['f']<0
        assert case['dE']>0 and other['dE']<0
        assert abs(case['f']-other['f'])<2e-12
        cases.append({'d':d,'theta_positive':case,'theta_negative':other})
    assert cases[-1]['theta_negative']['relative_error']<cases[0]['theta_negative']['relative_error']
    results['instantaneous_biot_savart']=cases
    # finite-time geometric separation from O31, k=2 for compact elliptical initial support
    M0_bound=2*GAMMA/(A*B) # conservative: each label max density <= Gamma/(a b), both -> 2 Gamma/(ab)
    GammaTotal=2*GAMMA
    U0=math.sqrt(2*GammaTotal*M0_bound/math.pi)
    d=12.
    def margin(t):return d-2*U0*t -4*(math.sqrt(S+4*NU*t)+U0*t)
    Tgeom=brentq(margin,0.,2.)
    assert Tgeom>0 and margin(0)>0
    H=lambda t: U0/(3*NU)*((S+4*NU*t)**1.5-S**1.5)+U0*U0*t*t
    Tquad=brentq(lambda t: H(t)-Q.real,0,1.)
    assert Tgeom>Tquad>0.
    results['geometry_bound']={'d':d,'U0_conservative':U0,'Tgeom_lower_certified_if_T_below':Tgeom,'Tquadrupole_lower_certified_if_T_below':Tquad,'initial_margin':margin(0)}
    # real exact NS radial Oseen benchmark for monotone overlap
    vals=[radial_gaussian_overlap(t) for t in (0,1,10,50,200)]
    assert all(v2>v1 for v1,v2 in zip(vals,vals[1:]))
    assert all(0<v<.5 for v in vals)
    results['radial_NS_exact_overlaps']=dict(zip(['t0','t1','t10','t50','t200'],vals))
    print(json.dumps({'status':'PASS','results':results},indent=2,ensure_ascii=False))

if __name__=='__main__':main()
