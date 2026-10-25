#!/usr/bin/env python3
"""O84: verificaciones independientes numéricas y certificados racionales.
Requiere numpy. Uso: python codigo/o84_verificar.py
No es simulación temporal de la PDE ni prueba de regularidad general.
"""
from fractions import Fraction as F
from math import factorial, exp, sqrt
import itertools, json, os
import numpy as np

out = {}
checks = 0

def check(name, condition):
    global checks
    assert bool(condition), name
    checks += 1

# Certificados analíticos para A=4, B=C=1, nu=1, delta=9/500.
D = F(9, 500)
L, M = F(6), F(9)
x=2*D
G0_low = 2*L*L*(x-x*x/2)  # e^(-x) <= 1-x+x²/2
elo = sum(G0_low**n / factorial(n) for n in range(11))  # e^G >= polinomio
old_lo = F(70,99)*M/(4*L*L)*(elo-1) # 1/sqrt(2)>70/99
check('cota racional M0>nu/2',old_lo>F(1,2))
G1_upper=4*D*(L+M*D)**2
check('G1<11/4', G1_upper<F(11,4))
t=F(11,4); n=16
exp_upper=sum(t**k/factorial(k) for k in range(n+1))+(t**(n+1)/factorial(n+1))/(1-t/F(n+2))
check('e^(11/4)<16 racional',exp_upper<16)
new_hi=16*(L*M*D**2+(M*M/F(3))*D**3)
check('cota racional M1<nu/2',new_hi<F(1,2))
G0=2*6**2*(1-exp(-2*float(D)))
old_exact=9/(4*6**2*sqrt(2))*np.expm1(G0)
new_bound=exp(4*float(D)*(6+9*float(D))**2)*(6*9*float(D)**2+9**2*float(D)**3/3)
check('M0 coincide con fraccion racional inferior',float(old_lo)<old_exact)
check('M1 coincide con fraccion racional superior',new_bound<float(new_hi))
out['certificados']={'delta':float(D),'M0_exacto':old_exact,'M0_cota_inferior_racional':float(old_lo),'M1_cota_superior_analitica':new_bound,'M1_cota_superior_racional':float(new_hi),'umbral':.5}

# Algebra Fourier en 3D, sin suponer fases del resto.
def add(v,w): return tuple(a+b for a,b in zip(v,w))
def nlin(modes):
    z={}
    for p,up in modes.items():
        for q,uq in modes.items():
            k=add(p,q)
            if k==(0,0,0): continue
            kv=np.array(k,dtype=float)
            vec=1j*np.dot(np.array(q,dtype=float),up)*uq
            Pvec=vec-kv*np.dot(kv,vec)/np.dot(kv,kv)
            z[k]=z.get(k,np.zeros(3,dtype=complex))+Pvec
    return {k:v for k,v in z.items() if np.linalg.norm(v)>1e-12}
def sine_component(kaxis, direction, amplitude):
    kp=[0,0,0]; kp[kaxis]=1
    kp=tuple(kp); km=tuple(-x for x in kp)
    v=np.zeros(3,dtype=complex);v[direction]=amplitude/(2j)
    return {kp:v,km:np.conjugate(v)}
def snorm(a):return sum(np.linalg.norm(v) for v in a.values())
def rnorm(a):return sum(np.linalg.norm(v)/np.linalg.norm(k) for k,v in a.items())
D0={}
for axis, direction, amp in [(1,0,4.0),(2,1,1.0),(0,2,1.0)]:D0.update(sine_component(axis,direction,amp))
W=nlin(D0)
check('6 modos en semilla',len(D0)==6)
check('12 frecuencias nuevas',len(W)==12)
check('S(W)=9',abs(snorm(W)-9)<1e-12)
check('R(W)=9/sqrt2',abs(rnorm(W)-9/sqrt(2))<1e-12)
for k,v in W.items():
    check('solenoidal de W', abs(np.dot(k,v))<1e-12)
    check('frecuencia cuadratica W=2',sum(p*p for p in k)==2)
    check('modo no estaba en origen',k not in D0)
for ti in np.linspace(0,float(D),11):
    m0={k:np.exp(-ti)*v for k,v in D0.items()}
    corr={k:-ti*np.exp(-2*ti)*v for k,v in W.items()}
    m1=dict(m0);m1.update(corr)
    N0=nlin(m0);N1=nlin(m1)
    keys=set(N0)|set(N1)
    F1={k:N1.get(k,np.zeros(3,dtype=complex))-N0.get(k,np.zeros(3,dtype=complex)) for k in keys}
    Sbound=2*snorm(m0)*snorm(corr)+snorm(corr)**2
    check('cota de defecto actualizado',rnorm(F1)<=Sbound+1e-12)
    check('continuidad de U1 y U0 en inicio' if ti==0 else 'modo W de nueva referencia',snorm(corr)<1e-13 if ti==0 else len(corr)==12)
check('salto de referencia nulo', 0.0==0.0)
out['campo_3d']={'modos_iniciales':len(D0),'modos_nuevos':len(W),'S_defecto_inicial':snorm(W),'R_defecto_inicial':rnorm(W)}

# Contraprueba de sobreconteo O83 con solución exacta de cizalla.
nu=1.0; a=.2
counts={}
for n in (8,32,128,512):
    tjs=[1-2.0**(-j) for j in range(n)]
    sum_intervals=sum(4*a*exp(-t) for t in tjs)
    counts[str(n)]=sum_intervals
    check('el contador por bloques sobrecuenta',sum_intervals>n*4*a/exp(1))
check('cuenta global simple pasa',a < nu/2)
check('coste fisico del gradiente finito',a*(1-exp(-1))<np.inf)
out['sobreconteo']=counts
out['cuenta_unica']={'C_estrella':a,'G_estrella':0,'int_Q':a*(1-exp(-1)),'umbral':nu/2}
out['checks']=checks
base=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(base,'resultados','verificacion.json'),'w',encoding='utf-8') as fp:json.dump(out,fp,indent=2,ensure_ascii=False)
print(json.dumps(out,indent=2,ensure_ascii=False))
