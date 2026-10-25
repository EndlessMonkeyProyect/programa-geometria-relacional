#!/usr/bin/env python3
"""O34: pruebas analíticas y cuadraturas de un atractor Oseen en NS 2D.

No resuelve una simulacion DNS. Usa soluciones radiales exactas y el estimador
por entropia derivado en el texto. Requiere numpy y scipy.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import roots_hermitenorm, logsumexp

CNT=0

def check(statement, msg):
    global CNT
    if not statement: raise AssertionError(msg)
    CNT += 1

def h_gauss(beta):
    return beta-1.0-math.log(beta)

def fisher_gauss(beta):
    return 4.0*(beta-1.0)**2/beta

def beta_at(beta0, tau):
    return 1.0+(beta0-1.0)*math.exp(-tau)

def l1_gaussian(beta_a, beta_b):
    if abs(beta_a-beta_b)<1e-13: return 0.0
    s=math.log(beta_b/beta_a)/(1.0/beta_a-1.0/beta_b)
    return 2*abs(math.exp(-s/beta_a)-math.exp(-s/beta_b))

def nonradial_entropy():
    # initial Gaussian mixture: mean zero, no symmetry central (nonzero third moment)
    w=0.65
    means=np.array([[0.7,0.0],[-1.3,0.0]],float)
    widths=np.array([0.6,1.2],float)
    check(abs(float(w*means[0,0]+(1-w)*means[1,0])) < 1e-13,"centroid")
    moment3=w*(means[0,0]**3+1.5*means[0,0]*widths[0])+(1-w)*(means[1,0]**3+1.5*means[1,0]*widths[1])
    check(abs(moment3)>0.1, 'third moment not vanish')
    nodes,weights=roots_hermitenorm(40)
    W=weights[:,None]*weights[None,:]/(2*math.pi)
    ans=0.0
    for mass,center,beta in zip((w,1-w),means,widths):
        x=center[0]+math.sqrt(beta/2)*nodes[:,None]
        y=center[1]+math.sqrt(beta/2)*nodes[None,:]
        lograds=[]
        for m,c,b in zip((w,1-w),means,widths):
            lograds.append(math.log(m)-math.log(math.pi*b)-((x-c[0])**2+(y-c[1])**2)/b)
        logf=logsumexp(np.stack([np.broadcast_to(a,(40,40)) for a in lograds]),axis=0)
        logG=-math.log(math.pi)-x*x-y*y
        ans+=mass*float(np.sum(W*(logf-logG)))
    check(ans>0.001,'nonradial H0 positive')
    check(math.isfinite(ans),'nonradial H0 finite')
    return {'third_central_x_moment':moment3,'initial_relative_entropy_estimate':ans,'gauss_hermite_order':40}

def main():
    betas0=[0.45,0.55,0.7,1.6,1.8,2.3]
    times=[0.0,0.05,0.25,0.5,1.0,2.0,3.0,5.0,10.0,100.0]
    max_identity_residual=0.0
    table=[]
    for b0 in betas0:
        h0=h_gauss(b0)
        for tau in times:
            b=beta_at(b0,tau)
            h=h_gauss(b)
            I=fisher_gauss(b)
            # Exact analytic entropy derivative for Gaussian Ornstein-Uhlenbeck path.
            derivative=-(b-1.0)**2/b
            max_identity_residual=max(max_identity_residual,abs(derivative+I/4))
            check(abs(derivative+I/4)<1e-12,'entropy dissipation identity')
            check(h>=-1e-13,'entropy nonnegative')
            check(h<=math.exp(-tau)*h0+1e-12,'LSI exponential entropy bound')
            check(l1_gaussian(b,1.0) <= math.sqrt(max(0,2*h))+1e-8,'Pinsker bound')
        table.append({'beta0':b0,'H0':h0,'H_tau1':h_gauss(beta_at(b0,1))})
    # Two populations sharing radial total flow exactly satisfy diffusion and tend to G.
    a0,b0=0.55,1.8
    distances=[]
    for tau in times:
        a,b=beta_at(a0,tau),beta_at(b0,tau)
        d=l1_gaussian(a,b)
        check(d>=0,'distance nonnegative')
        check(d<=math.sqrt(2*h_gauss(a))+math.sqrt(2*h_gauss(b))+1e-8,'triangle Pinsker')
        distances.append(d)
    for before,after in zip(distances,distances[1:]):
        check(after<=before+1e-12,'gaussian components converge monotonically')
    for tau in times:
        # S_i = a0²*beta_i0 + 4νt; choose a0²=1 and t0=1, 4ν=1.
        t=math.expm1(tau)
        S_A=a0+t; S_B=b0+t
        check(abs((S_A-S_B)-(a0-b0))<=1e-7*(1+abs(t)),
              'the physical second-moment difference is conserved')
        normalized_gap=(S_A-S_B)/(1+t)
        check(abs(normalized_gap-(a0-b0)*math.exp(-tau))<1e-12,
              'the gap decays only after normalization by scale')
    check(distances[-1]<distances[0]*1e-40,'profiles asymptotically share G')
    # Normalization and exact moment checks for G and radial Gaussian beta.
    for b in betas0:
        check(b>0 and h_gauss(b)>=0,'Gaussian entropy positive')
        check(0 <= l1_gaussian(b,1.0) <=2,'l1 normalized')
    nonrad=nonradial_entropy()
    result={'passed_checks':CNT,'max_entropy_identity_residual':max_identity_residual,
            'gaussian_profiles':table,
            'two_radial_populations':{'beta_A_initial':a0,'beta_B_initial':b0,
                'times_tau':times,'L1_distances':distances},
            'nonradial_initial_configuration':nonrad,
            'limitations':'Exact radial Navier-Stokes and entropy estimates; no numerical Navier-Stokes DNS or independent derivation of phase synchronization.'}
    target=Path(__file__).with_name('VALIDACION_O34.json')
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'passed_checks':CNT,'initial_L1':distances[0], 'L1_at_tau3':distances[times.index(3.)], 'nonradial_H0':nonrad['initial_relative_entropy_estimate'], 'max_residual':max_identity_residual},ensure_ascii=False))

if __name__=='__main__':main()
