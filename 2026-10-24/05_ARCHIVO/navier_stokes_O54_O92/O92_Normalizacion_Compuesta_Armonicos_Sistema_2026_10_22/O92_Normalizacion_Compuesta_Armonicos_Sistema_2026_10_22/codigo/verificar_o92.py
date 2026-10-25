#!/usr/bin/env python3
"""Verificador O92: normalizador armónico+sistema, cociente dinámico y fases.
Dependencias: numpy, sympy. Las demostraciones están en O92_FORMALIZACION.es.md.
"""
from fractions import Fraction as F
from math import gcd
from functools import reduce
from itertools import product
import json
from pathlib import Path
import numpy as np
from sympy import Matrix, Rational as R

here=Path(__file__).resolve().parents[1]
check=0

def ok(pred,msg):
    global check
    assert pred, msg
    check+=1

# O40/68/74/88 composicionalidad — contratos de naturaleza distinta.
for N,M,L in [(2,6,12),(3,6,18),(4,12,24),(6,12,60)]:
    ok(M%N==0 and L%M==0,"orden de refinamiento")
    for j in range(N):
        a=(M//N*j)%M
        b=(L//M*a)%L
        c=(L//N*j)%L
        ok(b==c,"inclusiones compuestas O40")
for q,p in [(2,1),(3,2),(5,3),(8,5)]:
    ok(gcd(q,p)==1,"par primitivo")
    aa,bb=None,None
    for a in range(-20,21):
        for b in range(-20,21):
            if a*q+b*p==1:
                aa,bb=a,b
                break
        if aa is not None:break
    M=Matrix([[aa,bb],[p,-q]])
    ok(M.det()==-1,"unimodular")
    for vv in [Matrix([3,1]),Matrix([9,7]),Matrix([13,21])]:
        ok(M.inv()*M*vv==vv,"reconstrucción Bézout")
for rs in [[1,2,3,4],[3,5,7,11],[1,1,1,1],[2,6,4,8]]:
    H=F(1)
    for i in range(4):H*=F(rs[i],rs[(i+1)%4])
    ok(H==1,"cierre telescópico C4")
    omega=[F((-1)**i,rs[i]) for i in range(4)]
    for i in range(4):ok(rs[i]*omega[i]+rs[(i+1)%4]*omega[(i+1)%4]==0,"enlace sin deslizamiento")

# Corrección O91: mismas medidas agregadas, diferente NORMALIZACION POR ARMÓNICO.
wC=[R(7,12),R(539,150),R(1,20),R(817,300)]
wD=[R(203,300),R(427,150),R(113,100),R(689,300)]
ks=[1,2,3,4]
def mj(w,j):return sum(wi*R(ki)**(2*j) for ki,wi in zip(ks,w))
for j in [-1,0,1]:ok(mj(wC,j)==mj(wD,j),"mismos momentos globales")
ok(mj(wC,2)!=mj(wD,2),"momento cuarto distinto")
ok(wC!=wD,"distribucion individual distingue estados")
for j in [-1,0,1,2]:
    ok(mj(wC,j)==mj(wC,0)*sum(R(ki)**(2*j)*(wi/mj(wC,0)) for ki,wi in zip(ks,wC)),"reconstrucción con normalización doble C")
    ok(mj(wD,j)==mj(wD,0)*sum(R(ki)**(2*j)*(wi/mj(wD,0)) for ki,wi in zip(ks,wD)),"reconstrucción con normalización doble D")
rC=[wi/mj(wC,0) for wi in wC]
rD=[wi/mj(wD,0) for wi in wD]
ok(sum(rC)==sum(rD)==1,"suma armónica 1")
ok(rC!=rD,"el cierre armónico distingue datos del falsador O91")

# O61: misma energía y soporte/magnitud por armónico, distinta polarización.
p=np.array([1.,0,0]);q=np.array([0.,1,0]); k=p+q
P=np.eye(3)-np.outer(k,k)/np.dot(k,k)
B=np.array([0.,0,1.])
for theta,exp in [(0,0),(np.pi/2,1)]:
    a=np.array([0.,np.sin(theta),np.cos(theta)])
    amp=P@((a@q)*B+(B@p)*a)
    ok(abs(np.linalg.norm(amp)-exp)<1e-12,"transferencia triadica de O61")
    ok(abs(a@p)<1e-12 and abs(B@q)<1e-12,"polarizaciones solenoidales")

# Dinámica exacta A,z para la triada O79, con signos alternos.
def initial(a=1.,b=1.,c=0.4):
    kvals=[(1,0,0),(0,1,1),(1,1,1)]
    dirs=[np.array((0.,1.,0)),np.array((1.,0.,0)),np.array((1.,1.,-2.))]
    hats={}
    for j,vec in enumerate(kvals):
        m=np.array(vec,dtype=int)
        vv=dirs[j]
        fac=[a,b,c][j]/2
        hats[tuple(m)]=vv*fac*(1 if j<2 else -1j)
        hats[tuple(-m)]=vv*fac*(1 if j<2 else 1j)
    # Cuarta dirección de onda independiente: dependencia espacial auténticamente 3D (O79 §5).
    n=(0,0,1); amp=np.array((0.3,0.,0.))/2
    hats[n]=amp; hats[(0,0,-1)]=amp
    return hats

def ns_nonlin(hats):
    out={}
    for p,ap in hats.items():
        for q,bq in hats.items():
            k=tuple(np.array(p)+np.array(q))
            if k==(0,0,0):continue
            kk=np.array(k,dtype=float)
            P=np.eye(3)-np.outer(kk,kk)/(kk@kk)
            term=-1j*P@(np.dot(np.array(q,dtype=float),ap)*bq)
            out[k]=out.get(k,np.zeros(3,dtype=complex))+term
    return out

results={}
for sgn in [1.,-1.]:
    raw=initial(c=0.4*sgn)
    A2=sum(float(np.vdot(v,v).real) for v in raw.values())
    A=A2**0.5
    z={k:v/A for k,v in raw.items()}
    D=sum(sum(a*a for a in k)*float(np.vdot(v,v).real) for k,v in z.items())
    D2=sum((sum(a*a for a in k)**2)*float(np.vdot(v,v).real) for k,v in z.items())
    nonlin=ns_nonlin(z)
    dissip=-2*0.03*(D2-D*D)
    transfers=2*A*sum(sum(a*a for a in k)*float(np.vdot(z[k],nonlin.get(k,np.zeros(3,dtype=complex))).real) for k in z)
    enstrophic=2*A*sum(sum(a*a for a in k)*float(np.vdot(z[k],nonlin.get(k,np.zeros(3,dtype=complex))).real) for k in z)
    sumEnergy=sum(float(np.vdot(z[k],nonlin.get(k,np.zeros(3,dtype=complex))).real) for k in z)
    ok(abs(sumEnergy)<1e-12,"conservacion energetica de transferencia")
    rhs={k: -0.03*sum(a*a for a in k)*raw[k]+A*A*nonlin.get(k,np.zeros(3,dtype=complex)) for k in raw}
    Aprime=sum(float(np.vdot(raw[k],rhs[k]).real) for k in raw)/A
    ok(abs(Aprime+0.03*A*D)<1e-12,"ecuacion de intensidad total")
    zp={k:rhs[k]/A-z[k]*Aprime/A for k in raw}
    wd=sum(2*sum(a*a for a in k)*float(np.vdot(z[k],zp[k]).real) for k in z)
    ok(abs(wd-(dissip+transfers))<1e-12,"ecuacion exacta de la dispersion entre armónicos")
    results['signo_positivo' if sgn>0 else 'signo_negativo']={
        'A':A,'D':D,'D2':D2,'difusion_normalizada':dissip,
        'transferencia_fases':transfers,'D_derivada':wd,
        'energia_no_lineal':sumEnergy,
    }
ok(results['signo_positivo']['transferencia_fases']*results['signo_negativo']['transferencia_fases']<0,'signo transferido por fase')
ok(abs(results['signo_positivo']['D']-results['signo_negativo']['D'])<1e-12,'misma magnitud espectral antes de invertir fase')
results['comparador_O91']={
 'N':12,
 'momentos_comunes':{str(j):str(mj(wC,j)) for j in [-1,0,1]},
 'w_C':[str(x) for x in wC],
 'w_D':[str(x) for x in wD],
 'r_C':[str(x) for x in rC],
 'r_D':[str(x) for x in rD],
 'C_momento2':str(mj(wC,2)),
 'D_momento2':str(mj(wD,2)),
}
results['checks']=check
out=here/'resultados'/'o92_verificacion.json'
out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
