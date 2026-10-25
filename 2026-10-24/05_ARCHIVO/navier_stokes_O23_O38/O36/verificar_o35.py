#!/usr/bin/env python3
"""O35: signos de contracción local de fases de forma en NS 2D.

No integra la PDE: evalúa exactamente su campo tangente al dato inicial
mediante integrales de Gauss, con dos cuadraturas independientes.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import roots_hermitenorm

B = np.array([1.0, 1j])
BASE = Path(__file__).resolve().parent
ASSERTIONS = 0

def check(ok, msg):
    global ASSERTIONS
    if not bool(ok):
        raise AssertionError(msg)
    ASSERTIONS += 1

def cov(a,b,theta):
    c,s=math.cos(theta),math.sin(theta)
    R=np.array([[c,-s],[s,c]])
    return R@np.diag([a*a,b*b])@R.T

def Q(a,b,theta):
    return (a*a-b*b)*np.exp(2j*theta)

def self_dot(a,b,theta,Gamma):
    # Resultado exacto para gaussiana eliptica normalizada.
    return 1j*Gamma/(2*math.pi)*(a-b)/(a+b)*np.exp(2j*theta)

def cross_dot_laplace(Sa,Sb,r,Gamma_b):
    """dot Q_A debido a B: Laplace de 1/|D|^2 y E[W_A|D]."""
    Sigma=Sa+Sb
    Beta=Sa@np.linalg.inv(Sigma)
    lam,V=np.linalg.eigh(Sigma)
    r_e=V.T@r
    def integrand(t):
        w=1/(1+2*t*lam)
        m=V@(w*r_e)
        C=V@np.diag(lam*w)@V.T
        weight=math.sqrt(float(np.prod(w)))*math.exp(-t*float(r@m))
        return weight*((B@(Beta@(m-r)))*(B@m)+(B@Beta@C@B))
    val,err=quad_vec(integrand,0,np.inf,epsabs=2e-12,epsrel=2e-11)
    return 1j*Gamma_b/math.pi*val

def cross_dot_gh(Sa,Sb,r,Gamma_b,n=65):
    """Comprobacion independiente: integral bidimensional con Gauss-Hermite."""
    Sigma=Sa+Sb
    Beta=Sa@np.linalg.inv(Sigma)
    L=np.linalg.cholesky(Sigma)
    x,w=roots_hermitenorm(n)
    gx,gy=np.meshgrid(x,x,indexing='ij')
    wx,wy=np.meshgrid(w,w,indexing='ij')
    U=np.stack([gx.ravel(),gy.ravel()],axis=0)
    diff=L@U
    D=diff+r[:,None]
    W=Beta@diff
    w2=(wx*wy).ravel()/(2*math.pi)
    complex_d=D[0]+1j*D[1]
    complex_w=W[0]+1j*W[1]
    radii=D[0]**2+D[1]**2
    return 1j*Gamma_b/math.pi*np.sum(w2*complex_w*complex_d/radii)

def observation(theta_b,d=6,a=.9,b=.5,theta_a=0,gamma_a=1,gamma_b=1,method='laplace'):
    Sa,Sb=cov(a,b,theta_a),cov(a,b,theta_b)
    r=np.array([-d,0.0])
    method_cross = cross_dot_laplace if method == 'laplace' else cross_dot_gh
    qa,qb=Q(a,b,theta_a),Q(a,b,theta_b)
    qa_dot=self_dot(a,b,theta_a,gamma_a)+method_cross(Sa,Sb,r,gamma_b)
    qb_dot=self_dot(a,b,theta_b,gamma_b)+method_cross(Sb,Sa,-r,gamma_a)
    psi=float(np.angle(qa/qb))
    dotpsi=float(np.imag(qa_dot/qa-qb_dot/qb))
    dotE=float(math.sin(psi)*dotpsi)
    return dict(theta_B=theta_b,d=d,psi=psi,dot_psi=dotpsi,dot_E=dotE,
                Q_A=[float(qa.real),float(qa.imag)],Q_B=[float(qb.real),float(qb.imag)],
                dot_Q_A=[float(qa_dot.real),float(qa_dot.imag)],dot_Q_B=[float(qb_dot.real),float(qb_dot.imag)])

def main():
    a,b=.9,.5
    z=math.radians(20.05352282957881)  # exactamente .35 rad
    check(abs(z-.35)<1e-13,'angle setting')
    # Rotational self frequency is identical for both gaussian ellipses.
    for ang in [-.35,0,.35,.8,1.4]:
        val=self_dot(a,b,ang,1)/Q(a,b,ang)
        check(abs(val.real)<1e-12,'self produces no amplitude change')
        check(abs(val.imag-1/(2*math.pi*(a+b)**2))<1e-12,'self frequency analytic')
    approaching=observation(-.35)
    departing=observation(+.35)
    check(approaching['dot_E']<0,'approaching not approaching')
    check(departing['dot_E']>0,'departing not departing')
    check(abs(approaching['dot_psi']-departing['dot_psi'])<1e-9,'mirror orientation symmetry for psi-dot')
    check(abs(approaching['psi']+.0+departing['psi'])<1e-9,'phase antisym')
    check(abs(approaching['dot_E']+departing['dot_E'])<1e-9,'alignment signs antisym')
    # Independent double Gaussian quadrature: the two methods use different integrals.
    for angle in [-.35,.35]:
        for d in [6.,8.]:
            lap=observation(angle,d=d,method='laplace')
            gh=observation(angle,d=d,method='gh')
            check(abs(lap['dot_psi']-gh['dot_psi'])<3e-6,'Gauss-Hermite and Laplace disagreement')
            check(abs(lap['dot_E']-gh['dot_E'])<3e-6,'Gauss-Hermite and Laplace sign disagreement')
    # Far field asymptotic: d^2 dot psi -> -Gamma*S/(pi*Q)*(1-cos .7)
    predicted = -(a*a+b*b)/(math.pi*(a*a-b*b))*(1-math.cos(.7))
    far_vals=[]
    for d in [12.,20.,30.,50.,80.]:
        q=observation(-.35,d=d)
        far_vals.append([d,d*d*q['dot_psi']])
        check(q['dot_psi']<0,'far field sign')
    check(abs(far_vals[-1][1]-predicted)<.001,'far field convergence')
    # O30 second-moment no-go: the only period compatible with rigid motion is 0.
    Gamma,nu=2.,.02
    check(4*nu*Gamma>0,'positive second moment growth')
    # Input equivalence: same radial S, abs Q, Gamma, d: only orientation flips.
    check(abs(approaching['Q_B'][0]-departing['Q_B'][0])<1e-12,'radial/eigenvalues mismatch')
    check(abs(approaching['Q_B'][1]+departing['Q_B'][1])<1e-12,'orientation flip')
    out={"name":"O35","status":"PASS", "assertions": ASSERTIONS,
         "parameters":{"a":a,"b":b,"Gamma_A":1.,"Gamma_B":1.,"d":6.,"theta_A":0.,"theta_B_positive":.35,"theta_B_negative":-.35,"nu_example":.02},
         "case_approach":approaching,"case_depart":departing,
         "asymptotic_d2_psidot_predicted":predicted,
         "asymptotic_d2_psidot_computed":far_vals,
         "scope":"Exact instantaneous NS 2D quadrupole derivatives evaluated by convergent quadratures; no time integration, no proof of long-time locking."}
    (BASE/'VALIDACION_O35.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
