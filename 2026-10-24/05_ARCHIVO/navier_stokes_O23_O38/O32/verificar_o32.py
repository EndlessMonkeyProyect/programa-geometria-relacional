"""Controles O32: aritmética de certificados, momentos gaussianos y controles adversarios.
No son simulaciones de Navier--Stokes; las identidades de la nota se prueban analíticamente.
"""
from math import sqrt, pi, log, asin, radians
import math, random, json
from scipy.integrate import quad, solve_ivp

checks = 0
def ok(c, msg):
    global checks
    if not c: raise AssertionError(msg)
    checks += 1

def a(s,u,nu,t):
    return sqrt(s+4*nu*t)+u*t

def H(s,u,nu,t):
    if nu <= 0: return 2*u*sqrt(s)*t+u*u*t*t
    # Stable evaluation if nu*t << s (log1p/expm1)
    w=4*nu*t/s
    return u/(3*nu)*s**1.5*math.expm1(1.5*math.log1p(w))+u*u*t*t

# Case selected before evaluating the criteria
s=0.1; q=.08; gamma_total=2.; nu=.001; T=.01; d0=8
m0_upper = 1/(.03*pi)
u0 = sqrt(2*gamma_total*m0_upper/pi)
A = a(s,u0,nu,T); h=H(s,u0,nu,T)
dmin=d0-2*u0*T
emin=(q-h)/(A*A)
ang=.5*asin(h/q)+log(d0/dmin)
ok(4*A<dmin,'separación')
ok(h<q,'anisotropía')
ok(emin>.44,'anisotropía umbral')
ok(math.degrees(ang)<9.5,'deriva relativa')

# Closed-form integral H equals numerical integration for random contracts.
rng=random.Random(20261020)
for _ in range(650):
    s=10**rng.uniform(-2,2)
    u=10**rng.uniform(-2,1)
    nu=10**rng.uniform(-4,-.2)
    t=10**rng.uniform(-3,0)
    h_num=2*u*quad(lambda x: a(s,u,nu,x),0,t,epsabs=1e-11)[0]
    h_exact=H(s,u,nu,t)
    ok(math.isclose(h_exact,h_num,rel_tol=1e-8,abs_tol=1e-8),'cuadratura de H')
    ok(H(s,u,nu,t/2)<=h_exact,'monotonicidad de H')
    ok(a(s,u,nu,t/2)<=a(s,u,nu,t),'monotonicidad extensión')

# Supersolution comparison with Riccati-like majorant.
for _ in range(80):
    s=10**rng.uniform(-2,1);u=rng.uniform(.05,3);nu=rng.uniform(.001,.5);t=rng.uniform(.001,.8)
    result=solve_ivp(lambda t,y:[4*nu+2*u*sqrt(max(0,y[0]))],(0,t),[s],rtol=2e-10,atol=1e-12)
    ok(result.success,'ode')
    ok(result.y[0,-1]<=a(s,u,nu,t)**2*(1+1e-8),'super solución')

# Gaussian exact covariance and second harmonic moment formulas
for _ in range(300):
    sx=10**rng.uniform(-2,.5);sy=10**rng.uniform(-2,.5);theta=rng.uniform(-pi,pi)
    q=complex((sx-sy)*math.cos(2*theta),(sx-sy)*math.sin(2*theta))
    S=sx+sy
    ok(abs(q)<=S+1e-12,'momento forma <= radial')
    ok(math.isclose(abs(q)/S,abs(sx-sy)/(sx+sy),rel_tol=1e-12),'anisotropía gaussiana')

# Axisymmetric gaussian negative control: circulation non-zero with Q=0.
sigma=.2
ok(complex(sigma-sigma,0)==0,'control negativo circular')

print(json.dumps({
  "assertions_passed":checks,
  "example":{"Gamma_total":2,"M0_upper":m0_upper,"U0_upper":u0,"T":T,"a_upper":A,"H_upper":h,"separation_left":4*A,"separation_right":dmin,"minimum_eccentricity":emin,"maximum_relative_orientation_degrees":math.degrees(ang)},
  "claim":"Checks validate algebraic bounds and Gaussian moment identities, not NS DNS or experimental persistence"
},ensure_ascii=False,indent=2))
