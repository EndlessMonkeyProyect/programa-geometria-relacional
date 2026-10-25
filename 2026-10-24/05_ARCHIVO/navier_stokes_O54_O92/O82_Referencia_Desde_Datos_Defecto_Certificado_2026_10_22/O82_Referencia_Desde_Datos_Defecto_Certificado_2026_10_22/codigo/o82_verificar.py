#!/usr/bin/env python3
"""O82: certificado a priori para la referencia U=e^{nu t Delta} P_F u0.
Todo se construye a partir del dato inicial y constantes exactas de Fourier.
Requiere Python 3, numpy y matplotlib para graficar, pero la verificacion basica solo usa numpy.
"""
from __future__ import annotations
import numpy as np, math, json, csv, pathlib, sys
from itertools import product
BASE=pathlib.Path(__file__).resolve().parent.parent
NU=1.0
DELTA=NU/2
AMP=(2.0,5e-5,5e-5)
MODES=((0,1,0),(0,0,1),(1,0,0))
UNITS=((1.,0.,0.),(0.,1.,0.),(0.,0.,1.))
EPS=1.e-11

def plus(a,b):return tuple(i+j for i,j in zip(a,b))

def seed(A,B,C):
    coeff={}
    for amp,k,e in zip((A,B,C),MODES,UNITS):
        coeff[k]=-1j*amp/2*np.asarray(e,dtype=complex)
        coeff[tuple(-j for j in k)]=1j*amp/2*np.asarray(e,dtype=complex)
    return coeff

def nonlinear(U):
    """F=P div(U tensor U), Fourier: Fhat(k)=i Pk sum_{p+q=k}(k.u_p)u_q."""
    raw={}
    for p,up in U.items():
        for q,uq in U.items():
            k=plus(p,q)
            if k==(0,0,0): continue
            vec=np.asarray(k,dtype=float)
            raw[k]=raw.get(k,np.zeros(3,dtype=complex))+1j*np.dot(vec,up)*uq
    out={}
    for k,a in raw.items():
        kv=np.asarray(k,dtype=float)
        a=a-kv*np.dot(kv,a)/np.dot(kv,kv)
        if np.linalg.norm(a)>1e-14: out[k]=a
    return out

def norms(U):
    return {
        'R':float(sum(np.linalg.norm(v)/np.linalg.norm(k) for k,v in U.items())),
        'S':float(sum(np.linalg.norm(v) for k,v in U.items())),
        'Q':float(sum(np.linalg.norm(v)*np.linalg.norm(k) for k,v in U.items())),
    }

def defect_norm(U):
    N=nonlinear(U)
    return float(sum(np.linalg.norm(v)/np.linalg.norm(k) for k,v in N.items()))

def certificate(A,B,C, reference):
    full=seed(A,B,C)
    if reference=='zero':
        U0={}
    elif reference=='shear':
        U0={k:v for k,v in full.items() if k in ((0,1,0),(0,-1,0))}
    elif reference=='heat-all':
        U0=full
    else: raise ValueError(reference)
    v0={k:v for k,v in full.items() if k not in U0}
    s0=norms(U0)['S']
    r0=norms(v0)['R']
    # All selected initial modes have |k|=1; the heat flow damps as e^{-nu t}.
    b0=defect_norm(U0)
    g_inf=2*s0*s0/(NU*NU)
    b_int=b0/(2*NU)
    loose=math.exp(g_inf)*(r0+b_int) if g_inf<700 else float('inf')
    if g_inf>0:
        weighted_b=b0*(1-math.exp(-g_inf))/(2*NU*g_inf)
    else:
        weighted_b=b_int
    weighted=math.exp(g_inf)*(r0+weighted_b) if g_inf<700 else float('inf')
    return dict(reference=reference,R_total=norms(full)['R'],R0=r0,S_U0=s0,D0=b0,
                G_inf=g_inf,D_integral=b_int,loose_bound=loose,weighted_bound=weighted,
                delta=DELTA,certified=bool(loose<DELTA))

def assert_near(x,y,rtol=1.e-10,atol=1.e-12):
    assert math.isclose(float(x),float(y),rel_tol=rtol,abs_tol=atol), (x,y)

def run():
    num=0
    for a in (0.4,1.,2.,3.):
      for b in (0.001,0.02,0.12):
       for c in (-0.03,0.003):
        U=seed(a,b,c); N=nonlinear(U)
        assert len(N)==12,(a,b,c,len(N));num+=1
        nrm=norms(U)
        assert_near(nrm['S'],abs(a)+abs(b)+abs(c));num+=1
        assert_near(nrm['R'],abs(a)+abs(b)+abs(c));num+=1
        assert_near(defect_norm(U),(abs(a*b)+abs(a*c)+abs(b*c))/math.sqrt(2));num+=1
        for k,v in U.items():
            assert abs(np.dot(np.asarray(k,dtype=float),v))<1e-13;num+=1
        for k,v in N.items():
            assert abs(np.dot(np.asarray(k,dtype=float),v))<1e-13;num+=1
        for k,v in N.items():
            neg=tuple(-i for i in k)
            assert np.max(np.abs(N[neg]-np.conjugate(v)))<1e-12;num+=1
    R=[certificate(*AMP,ref) for ref in ('zero','shear','heat-all')]
    for rec in R:
        if rec['reference']=='zero': assert not rec['certified'];num+=1
        else:
            assert rec['certified'];num+=1
            assert rec['R_total']>NU;num+=1
            assert rec['weighted_bound']<=rec['loose_bound'];num+=1
    assert R[2]['D0']>0;num+=1
    assert R[1]['D0']==0;num+=1
    assert R[2]['weighted_bound']<R[2]['loose_bound'];num+=1
    results=BASE/'resultados'
    results.mkdir(parents=True,exist_ok=True)
    with (results/'referencias.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=R[0].keys());w.writeheader();w.writerows(R)
    raw={'amplitudes':AMP,'nu':NU,'delta':DELTA,'mode_count_of_defect':len(nonlinear(seed(*AMP))),
         'tests_passed':num,'references':R,'status':'Verification of explicit finite-mode algebra; global theorem proved separately.'}
    (results/'resultado.json').write_text(json.dumps(raw,indent=2,ensure_ascii=False))
    print(json.dumps(raw,indent=2,ensure_ascii=False))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        times=np.linspace(0,5,301)
        s=sum(AMP)
        gamma=2*s*s/(NU*NU)
        d0=defect_norm(seed(*AMP))
        G=gamma*(1-np.exp(-2*NU*times))
        rhs=d0/(2*NU*gamma)*(np.exp(G)-1)
        fig,ax=plt.subplots(figsize=(8.5,4.5))
        ax.plot(times,rhs,label='Cota ponderada para el resto')
        ax.axhline(DELTA,linestyle='--',label='Umbral de estabilidad ν/2')
        ax.set(xlabel='Tiempo físico t',ylabel='Presupuesto R_v',title='O82 · Referencia obtenida exclusivamente del dato inicial')
        ax.legend();ax.grid(alpha=.2)
        fig.tight_layout();fig.savefig(BASE/'graficos/o82_certificado_defecto.png',dpi=180);plt.close(fig)
    except ImportError: pass
    print('PASS',num)

if __name__=='__main__':run()
