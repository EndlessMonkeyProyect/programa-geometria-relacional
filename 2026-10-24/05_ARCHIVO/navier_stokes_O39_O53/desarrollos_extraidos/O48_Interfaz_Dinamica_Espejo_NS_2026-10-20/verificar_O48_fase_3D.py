#!/usr/bin/env python3
"""O48-B: dos campos iniciales NS3D con igual espectro de enstrofia
pero transferencia triadica opuesta. Requiere numpy. Verifica FFT 16^3,24^3,32^3.
"""
import numpy as np
import json
from pathlib import Path
from math import sqrt, exp

nu=0.03
modes=[((1,0,0),(0.,1.,1.)), ((0,2,0),(1.,0.,1.)), ((1,2,0),(2.,-1.,1.))]

def setup(N):
    k=np.fft.fftfreq(N,d=1/N)
    K=np.array(np.broadcast_arrays(k[:,None,None],k[None,:,None],k[None,None,:]))
    k2=np.sum(K*K,axis=0)
    inv=np.divide(1.0,k2,out=np.zeros_like(k2),where=k2!=0)
    mask=np.all(np.abs(K)<N/3,axis=0)
    return K,k2,inv,mask

def data(N,sign):
    h=np.zeros((3,N,N,N),complex)
    for j,(kv,pv) in enumerate(modes):
        coef=(1j*sign if j==2 else 1.0)*0.1*np.array(pv)
        h[(slice(None),)+tuple(x%N for x in kv)]+=N**3*coef
        h[(slice(None),)+tuple((-x)%N for x in kv)]+=N**3*coef.conjugate()
    return h

def compute(N,sign):
    K,k2,inv,mask=setup(N)
    h=data(N,sign)
    omega=1j*np.cross(K,h,axisa=0,axisb=0,axisc=0)
    u=np.fft.ifftn(h,axes=(-3,-2,-1)).real
    w=np.fft.ifftn(omega,axes=(-3,-2,-1)).real
    nonlin=np.cross(u,w,axisa=0,axisb=0,axisc=0)
    nonlin_hat=np.fft.fftn(nonlin,axes=(-3,-2,-1))*mask
    # Helmholtz projection. du/dt = P(u x omega) - nu |k|^2 u
    nonlin_hat-=K*np.sum(K*nonlin_hat,axis=0)[None,...]*inv
    du_hat=nonlin_hat-nu*k2*h
    d_omega=1j*np.cross(K,du_hat,axisa=0,axisb=0,axisc=0)
    nonlinear_omega=1j*np.cross(K,nonlin_hat,axisa=0,axisb=0,axisc=0)
    Ek=np.sum(np.abs(omega)**2,axis=0)/(2*N**6)
    Tk=np.real(np.sum(np.conj(omega)*nonlinear_omega,axis=0))/N**6
    E=float(np.sum(Ek)); m1=float(np.sum(k2*Ek))
    P=float(np.sum(Tk))
    v={'resolution':N,'sign':sign,'E':E,'kinetic_energy':float(np.sum(np.abs(h)**2)/(2*N**6)),
       'J':2*m1,'mirror':sqrt(E/m1),'P':P,
       'Eprime':float(np.real(np.sum(np.conj(omega)*d_omega))/N**6),
       'divergence':float(np.sqrt(np.mean(np.abs(np.fft.ifftn(1j*np.sum(K*h,axis=0)))**2)))}
    for z in [0,.1,.2]:
        suffix=f'z{z}'
        M=float(np.sum(Ek*np.exp(-z*k2)))
        T=float(np.sum(Tk*np.exp(-z*k2)))
        rhs=2*nu*float(np.sum(-k2*Ek*np.exp(-z*k2)))+T
        lhs=float(np.sum(np.real(np.sum(np.conj(omega)*d_omega,axis=0))/N**6*np.exp(-z*k2)))
        v['M_'+suffix]=M;v['T_'+suffix]=T;v['source_identity_error_'+suffix]=abs(lhs-rhs)
    v['Tmode_one_sided']={str(kv):float(Tk[tuple(q%N for q in kv)]) for kv,_ in modes}
    v['Ek_shell']={str(l):float(np.sum(Ek[k2==l])) for l in [1,4,5]}
    return v

checks=0
record={}
for N in [16,24,32]:
    plus=compute(N,1);minus=compute(N,-1)
    for key in ['E','kinetic_energy','J','mirror','M_z0','M_z0.1','M_z0.2']:
        assert abs(plus[key]-minus[key])<1e-11,(N,key)
        checks+=1
    for z in [0,.1,.2]:
        suffix=f'z{z}'
        assert abs(plus['T_'+suffix]+minus['T_'+suffix])<1e-12
        assert abs(plus['T_'+suffix])>1e-4
        assert plus['source_identity_error_'+suffix]<1e-11
        assert minus['source_identity_error_'+suffix]<1e-11
        expected=.004*exp(-z)+.032*exp(-4*z)-.06*exp(-5*z)
        assert abs(plus['T_'+suffix]-expected)<1e-12
        checks+=5
    assert abs(plus['E']-.4)<1e-12
    assert abs(plus['kinetic_energy']-.1)<1e-12
    assert abs(plus['J']-3.68)<1e-12
    assert abs(plus['P']+.024)<1e-12
    assert abs(minus['P']-.024)<1e-12
    assert max(plus['divergence'],minus['divergence'])<1e-12
    checks+=6
    record[str(N)]={'plus':plus,'minus':minus}

out={'module':'O48-B','nu':nu,'checks':checks,'results':record,
     'limits':'datos iniciales NS 3D; la identidad espectral y las derivadas son exactas en la familia trigonometrica; comparacion FFT finita, no regularidad global'}
path=Path(__file__).parent/'O48_RESULTADOS_FASE_3D.json'
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS',checks,'checks; E=.4, J=3.68, P=±.024, T(.1)=±.01132224843747')
