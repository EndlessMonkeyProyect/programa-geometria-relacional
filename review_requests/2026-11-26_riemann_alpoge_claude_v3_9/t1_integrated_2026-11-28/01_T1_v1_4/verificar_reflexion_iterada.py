"""T.1 v1.4: momentos de reflexión, cotas y control del resto.
Reutiliza exclusivamente el Gram de Vasyunin del paquete v1.3.
Ejecutar: python verificar_reflexion_iterada.py (NumPy).
Controles numéricos, no aritmética de intervalos.
"""
import json
from pathlib import Path
import numpy as np
from verificacion_independiente_T1 import ip, ip_chi, divisors, PRIMES, stage


def reflection(S, p):
    ds = divisors(S)
    G = np.array([[ip(d,e) for e in ds] for d in ds])
    C = np.array([[ip(d,p*e) for e in ds] for d in ds])
    b = np.array([ip_chi(d) for d in ds])
    bp = np.array([ip_chi(p*d) for d in ds])
    L = np.linalg.cholesky(G)
    A = np.sqrt(p)*np.linalg.solve(L,np.linalg.solve(L,C).T).T
    T = A.T @ A
    v = bp - C.T @ np.linalg.solve(G,b)
    Q = 1-b @ np.linalg.solve(G,b)
    z = np.sqrt(p/Q)*np.linalg.solve(L,v)
    lam, E = np.linalg.eigh(T)
    q = float(lam[-1])
    assert lam[0] >= -1e-12 and 0 <= q < 1
    weights = (E.T @ z)**2
    eta = float(z @ np.linalg.solve(np.eye(len(ds))-T,z))
    eta_spectral = float(np.sum(weights/(1-lam)))
    mu = float(z @ z)
    ref = stage(S,p)
    assert np.isclose(eta,ref['eta'],rtol=1e-8,atol=1e-11)
    assert np.isclose(eta,eta_spectral,rtol=1e-8,atol=1e-11)
    assert np.isclose(mu,ref['mu'],rtol=1e-8,atol=1e-11)
    cost = float(-0.5*np.sum(np.log1p(-lam)))
    assert np.isclose(cost,ref['KH'],rtol=1e-8,atol=1e-10)
    assert 1-q >= np.exp(-2*cost)-1e-12
    # R_j = sum_{i=0}^j <z,T^i z>; iterative route, no inverse.
    jhalf = max(0,int(np.ceil(np.log(0.5)/np.log(q)))-1) if q else 0
    depth = max(16,jhalf)
    w = z.copy(); total=0.; vals={}; moments=[]
    for j in range(depth+1):
        m = float(z @ w); assert m >= -1e-12
        total += m; moments.append(m)
        tail = q**(j+1)*eta
        assert -1e-9 <= eta-total <= tail+1e-9
        if j in (0,1,4,16,jhalf): vals[j]=total
        w=T@w
    assert vals[jhalf] >= eta/2-1e-9
    gammaG = mu**2/(mu-moments[1]) if mu else 0.
    assert np.isclose(gammaG/eta,ref['gammaG_over_eta'],rtol=1e-8)
    # An improved lower bound from the first two moments, and from a partial sum plus Jensen tail.
    # R_j + m_{j+1}^2/(m_{j+1}-m_{j+2}), valid when the denominator is positive.
    m1,m2=moments[1:3]
    improved=mu + m1*m1/(m1-m2) if m1>0 else mu
    assert gammaG <= improved+1e-9 and improved <= eta+1e-9
    return dict(p=p,r=len(ds),q=q,KH_from_angles=cost,mu=mu,eta=eta,gamma_G=gammaG,lower_jensen2=improved,
                R1_over_eta=vals[1]/eta,R4_over_eta=vals[4]/eta,R16_over_eta=vals[16]/eta,
                jhalf=jhalf,Rjhalf_over_eta=vals[jhalf]/eta,p_R4=p*vals[4],
                p_mu=p*mu,p_eta=p*eta,schur_error=abs(eta-ref['eta']),moments_0_2=moments[:3])

if __name__=='__main__':
    rows=[reflection(PRIMES[:i],p) for i,p in enumerate(PRIMES)]
    print('p    q         R1/eta   R4/eta   R16/eta  gammaG/eta  Jensen2/eta  jhalf   Rjhalf/eta')
    for t in rows:
        print(f"{t['p']:2d}  {t['q']:.7f}  {t['R1_over_eta']:.5f}  {t['R4_over_eta']:.5f}  {t['R16_over_eta']:.5f}  {t['gamma_G']/t['eta']:.5f}      {t['lower_jensen2']/t['eta']:.5f}    {t['jhalf']:4d}     {t['Rjhalf_over_eta']:.5f}")
    print('OK: Schur, momentos, colas, cota de media recuperación Jensen y costo angular.')
    Path(__file__).with_name('resultados_reflexion_iterada.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
