#!/usr/bin/env python3
"""O31 tests: deterministic numerical controls, not a Navier–Stokes DNS."""
from __future__ import annotations
import json, math, random
from pathlib import Path

def bound_u(gamma, m):
    return math.sqrt(2*gamma*m/math.pi)

def aradius(s0, nu, u, t):
    return math.sqrt(s0+4*nu*t)+u*t

def margin(s1, s2, nu, u, d0, t, k):
    return d0-2*u*t - k*(aradius(s1,nu,u,t)+aradius(s2,nu,u,t))

def run():
    rng=random.Random(190031)
    checks=0
    for _ in range(2500):
        gamma=10**rng.uniform(-2,2)
        m=10**rng.uniform(-2,2)
        nu=10**rng.uniform(-5,0)
        s=10**rng.uniform(-5,2)
        t=rng.random()*2
        u=bound_u(gamma,m)
        h=math.sqrt(s+4*nu*t)
        a=h+u*t
        derivative_sup=2*a*(2*nu/h+u)
        rhs=4*nu+2*u*a
        assert derivative_sup>=rhs-1.e-11*max(1,abs(rhs)), (derivative_sup,rhs)
        checks+=1
    # Monotonic margin: sufficient to check only at the end of [0,T].
    for _ in range(300):
        s1,s2=[10**rng.uniform(-4,0) for _ in range(2)]
        u,nu,d0,k=10**rng.uniform(-2,1),10**rng.uniform(-5,-1),10**rng.uniform(-1,2),rng.uniform(1.1,4)
        T=rng.random()*2
        for i in range(1,21):
            assert margin(s1,s2,nu,u,d0,i*T/20,k)<=margin(s1,s2,nu,u,d0,(i-1)*T/20,k)+1e-12
            checks+=1
    # Worked Gaussian initial data; bound of max vorticity is deliberately conservative.
    a=.2;nu=.005;T=.25;k=2.;G=2.;M=2/(math.pi*a*a);d0=8.
    U=bound_u(G,M)
    s0=a*a
    q=aradius(s0,nu,U,T)
    dmin=d0-2*U*T
    coremargin=margin(s0,s0,nu,U,d0,T,k)
    assert math.isclose(U,2*math.sqrt(2)/(math.pi*a),rel_tol=1e-14);checks+=1
    assert coremargin>0 and k*(2*q)<dmin;checks+=1
    assert abs(U-4.501581580785531)<1e-12; checks+=1
    assert abs(coremargin-.3990994913978474)<1e-12; checks+=1
    # Exact 2D Lamb–Oseen radial Gaussian: S(t)=a²+4νt and its mass in disk k√S(t) is 1−exp(−k²).
    for _ in range(200):
        a=10**rng.uniform(-3,1);nu=10**rng.uniform(-5,0);t=rng.random()*10;k=1+rng.random()*4
        variance=a*a+4*nu*t
        exact=1-math.exp(-k*k)
        markov_lower=1-1/(k*k)
        assert exact+1e-12>=markov_lower
        assert math.sqrt(variance)<=aradius(a*a,nu,0,t)+1e-12
        checks+=2
    # Circulation dominance condition for both fractions.
    for _ in range(400):
        g1=10**rng.uniform(-2,2);g2=10**rng.uniform(-2,2)
        k=math.sqrt(1+max(g1/g2,g2/g1))+0.1
        assert (1-1/k**2)*g1>g2/k**2
        assert (1-1/k**2)*g2>g1/k**2
        checks+=2
    out={
        "status":"PASS","checks":checks,
        "disclaimer":"Algebraic inequalities, Gaussian single-vortex check, and finite examples; NOT a DNS or proof of physical vortex identity.",
        "example":{"nu":.005,"time":.25,"initial_separation":8,"circulation_each":1,
                   "max_vorticity_upper_bound":M,"U0_upper_bound":U,"radius_each_upper_bound":q,
                   "sum_disk_radii":4*q,"separation_lower_bound":dmin,
                   "positive_margin":coremargin,"guaranteed_fraction_each":.75}
    }
    Path(__file__).with_name("VALIDACION_O31.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__':run()
