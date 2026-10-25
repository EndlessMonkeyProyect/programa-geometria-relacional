#!/usr/bin/env python3
"""O36: verifica relaciones invariantes y pruebas instantáneas (NO evolución PDE)."""
import json, math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from verificar_o35 import observation

DIR=Path(__file__).resolve().parent
checks=0

def ck(cond,reason):
    global checks
    if not bool(cond):raise AssertionError(reason)
    checks+=1

def zmod(Qa,Qb,r,p,q):
    ck(abs(Qa)>0 and abs(Qb)>0 and abs(r)>0, 'domain')
    return (Qa/abs(Qa))**q*(Qb.conjugate()/abs(Qb))**p*(r.conjugate()/abs(r))**(2*(q-p))

def check_gauge():
    global checks
    qa=.56*np.exp(.15j); qb=.84*np.exp(-.37j); r=3.9*np.exp(.74j)
    rng=np.random.default_rng(36020)
    for p,q in [(1,1),(1,2),(2,1),(2,3),(4,3)]:
      z=zmod(qa,qb,r,p,q)
      ck(abs(abs(z)-1)<1e-12,'Z not unitary')
      for i in range(25):
        angle=float(rng.uniform(-10,10)); factor=float(np.exp(rng.uniform(-2,2)))
        qa2=factor**2*np.exp(2j*angle)*qa
        qb2=factor**2*np.exp(2j*angle)*qb
        r2=factor*np.exp(1j*angle)*r
        ck(abs(zmod(qa2,qb2,r2,p,q)-z)<1e-11,'Z not rigid/scale gauge invariant')

def check_parity():
    table=[]
    for d in [5.5,6.,6.5,8.,20.]:
      for t in [.005,.01,.02,.05,.1,.2,.3,.35,.4,.5]:
        m=observation(-t,d=d)
        pp=observation(+t,d=d)
        ck(abs(m['dot_psi']-pp['dot_psi'])<3e-10, 'evenness broken')
        ck(abs(m['dot_E']+pp['dot_E'])<3e-10, 'odd drift sign broken')
        ck(m['dot_E']<0 and pp['dot_E']>0,'one-sided sign broken in sampled parameter grid')
        ck(abs(m['psi']+pp['psi'])<3e-10, 'psi parity broken')
      t0=observation(0,d=d)
      ck(abs(t0['dot_psi'])<3e-11,'f_d(0) must vanish')
      table.append({'d':d,'theta_B':-0.35,'dotE_negative':observation(-.35,d=d)['dot_E']})
    return table

def check_order():
    theta_vals=[.005,.01,.02,.05,.1]
    rates=[]
    for t in theta_vals:
      o=observation(-t,d=6)
      E=1-math.cos(o['psi'])
      rate=o['dot_E']/E
      ck(o['dot_psi']<0 and o['dot_E']<0 and rate<0,'approach negative')
      rates.append({'theta_abs':t,'dot_psi':o['dot_psi'],'dot_psi_over_theta2':o['dot_psi']/(t*t),'dot_E_over_E':rate})
    ck(abs(rates[0]['dot_psi_over_theta2']/rates[1]['dot_psi_over_theta2']-1)<2e-4,'quadratic near-zero order')
    ck(abs(rates[1]['dot_E_over_E']/rates[0]['dot_E_over_E']-2)<.01,'rate relative linear order')
    return rates

def check_quadratures():
    cases=[]
    for theta,d in [(-.35,6.),(.35,6.),(-.35,8.),(.35,8.)]:
      l=observation(theta,d=d,method='laplace')
      h=observation(theta,d=d,method='gh')
      ck(abs(l['dot_E']-h['dot_E'])<3e-6,'independent quadratures differ')
      ck(abs(l['dot_psi']-h['dot_psi'])<3e-6,'independent quadratures differ in dotpsi')
      cases.append({'theta_B':theta,'d':d,'dot_E':l['dot_E'],'dot_psi':l['dot_psi']})
    ck(abs(cases[0]['dot_E']+0.003060279)<3e-7,'known approach value mismatch')
    return cases

def check_separation_bound():
    a,b,nu,d0=.9,.5,.02,6.
    G=2.;M=2./(2*math.pi*a*b)
    U=math.sqrt(2*G*M/math.pi)
    F=lambda t:4*math.sqrt(a*a+b*b+4*nu*t)+6*U*t-d0
    T=float(brentq(F,0,2))
    ck(abs(T-.32174474639782)<1e-9,'geom horizon mismatch')
    ck(F(.3)<0 and F(.35)>0,'separation sign bounds incorrect')
    # This is a geometric concentration guarantee only, not a phase-contraction bound.
    return {'d0':d0,'viscosity':nu,'total_circulation':G,'M0_upper_bound':M,'U0_upper_bound':U,'S0_each':a*a+b*b,'T_geom_supremum':T,'guarantee':'Two tagged disjoint 75% concentration disks if 0<=T<T_geom; no certified phase-locking horizon.'}

def main():
    check_gauge()
    parity=check_parity()
    rates=check_order()
    crosses=check_quadratures()
    sep=check_separation_bound()
    output={'module':'O36','status':'PASS','assertions':checks,
            'basis':'exact instantaneous NS 2D moment identities; numerical quadratures validate examples only',
            'gauge':'p:q phase invariant under translation, rotation, positive dilation',
            'sampled_parity_signs':parity,'near_zero_scaling':rates,
            'independent_quadrature_comparison':crosses,'separation':sep,
            'limitations':['No full PDE time integration','No interval-arithmetic certification for d=6 sign',
                           'Uniform local contraction interval in theorem is existential and only for compact set away from exact alignment',
                           'No proof of global phase synchronization/attractor']}
    (DIR/'VALIDACION_O36.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','assertions':checks,'approximate_first_approach':crosses[0],
                      'geometric_window_upper':sep['T_geom_supremum'],'near_zero_rate':rates[:2]},indent=2))

if __name__=='__main__':main()
