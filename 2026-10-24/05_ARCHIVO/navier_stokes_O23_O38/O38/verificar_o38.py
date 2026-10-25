#!/usr/bin/env python3
"""O38 reproducible controls: exact heat benchmark and algebraic symmetry.
Does not numerically integrate the nonlinear Navier-Stokes PDE.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad

sigma2=1.0; a=2.0; nu=0.5; gamma=1.0
Tc=(a*a-sigma2)/(2*nu)
def s2(t):return sigma2+2*nu*t

def hessian_log_origin(t):
    q=s2(t)
    return np.diag([(a*a-q)/(q*q), -1/q])

def intrinsic_B(t):
    q=s2(t); R2=2*q+a*a
    return R2 * np.linalg.eigvalsh(hessian_log_origin(t))[-1]

def density(xy,t=0,g=1):
    x,y=xy; q=s2(t)
    return g/(2*math.pi*q)*(math.exp(-((x-a)**2+y*y)/(2*q))+math.exp(-((x+a)**2+y*y)/(2*q)))

def intrinsic_from_hessian(H, R2):return R2*np.linalg.eigvalsh(H)[-1]

checks={}
for t in (0.0,0.5,1.25,2.999,3.0,3.001,6.0,10.0):
    q=s2(t)
    lam_expected=max((a*a-q)/(q*q), -1/q)
    vals=np.linalg.eigvalsh(hessian_log_origin(t))
    assert abs(vals[-1]-lam_expected)<1e-13
    checks[f'hessian_{t}']=True
assert intrinsic_B(0)>0 and intrinsic_B(6)<0 and abs(intrinsic_B(Tc))<1e-12
checks['sign_transition']=True
# The true NS theorem uses smooth dependence on gamma. This script does not test that theorem numerically.
# Independently verify the exact Hessian of log of the two-Gaussian heat profile by central differences.
for t in (0.0,3.0,6.0):
    h=1e-3
    f=lambda x,y:math.log(density((x,y),t))
    xx=(f(h,0)-2*f(0,0)+f(-h,0))/h**2
    yy=(f(0,h)-2*f(0,0)+f(0,-h))/h**2
    np.testing.assert_allclose([xx,yy],np.diag(hessian_log_origin(t)), atol=1e-5, rtol=1e-5)
checks['finite_difference_hessian']=True

# rotation, translation, positive scale and amplitude invariance of the module
H=hessian_log_origin(0); R2=2*sigma2+a*a
for ang in (0.0,.1,.7,1.1,math.pi):
    rot=np.array([[math.cos(ang),-math.sin(ang)],[math.sin(ang),math.cos(ang)]])
    for k in (.2,.7,1.,3.,9.):
        Hnew=rot@H@rot.T/k**2
        assert abs(intrinsic_from_hessian(Hnew,R2*k*k)-intrinsic_from_hessian(H,R2))<1e-12
checks['frame_scale_invariance']=True

# O37 label overlap ambiguity under two partitions of same vorticity.
# Natural labels: two centered Gaussians at +-a. Labels of half total give O=total_gamma/4=gamma/2.
def labeled_overlap(t):
    q=s2(t)
    # factor 1/cosh avoids overflow for the given finite parameters
    c=gamma/(2*math.sqrt(2*math.pi*q))*math.exp(-a*a/(2*q))
    return c*quad(lambda x: math.exp(-x*x/(2*q))/math.cosh(a*x/q),-20*math.sqrt(q),20*math.sqrt(q),epsabs=1e-12)[0]
for t in (0,1,3,6):
    natural=labeled_overlap(t)
    assert 0<natural<gamma/2
    checks[f'overlap_label_difference_{t}']=True
assert labeled_overlap(6)>labeled_overlap(3)>labeled_overlap(1)>labeled_overlap(0)
checks['overlap_increases_heat_example']=True

out={'parameters':{'sigma2':sigma2,'a':a,'nu':nu,'gamma_heat_reference':gamma},
     'critical_heat_time':Tc,
     'benchmarks':[{ 't':t, 'variance_s2':s2(t),'B':intrinsic_B(t),
                    'log_hessian_eigenvalues':np.linalg.eigvalsh(hessian_log_origin(t)).tolist(),
                    'natural_label_overlap':labeled_overlap(t)} for t in (0.,3.,6.)],
     'checks':checks,'checks_passed':len(checks),
     'scope':'Exact heat identities and invariance checks only. Nonlinear NS conclusion uses standard finite-time small-amplitude parabolic continuity, not DNS.'}
path=Path(__file__).with_name('resultados_o38.json');path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
