#!/usr/bin/env python3
"""O83: rigorous elementary bounds plus finite Fourier cross-check, 2D NS embedded in 3D.
Uses numpy for Fourier bookkeeping; printed analytic inequalities do not depend on floating integration.
"""
import numpy as np
import math, json, csv, pathlib
from fractions import Fraction as F
from math import factorial
root=pathlib.Path(__file__).resolve().parents[1]
(root/'resultados').mkdir(parents=True,exist_ok=True)
(root/'graficos').mkdir(parents=True,exist_ok=True)
nu=1.; A=B=4.; delta=0.01125
sqr5=math.sqrt(5)
T=3*A*B/sqr5 # Wiener S of nonlinear projected term W
L=A+B
# heat reference g(s)=4 S(U)^2, Bheat(s)=3AB/5 exp(-5s)
gmin=4*(A*math.exp(-4*delta)+B*math.exp(-delta))**2
bmin=3*A*B/5*math.exp(-5*delta)
heat_lower=bmin*math.expm1(gmin*delta)/gmin
heat_upper=(3*A*B/5)*delta*math.exp(4*delta*L**2)
# Picard reference upper bounds on [0,delta]
Gpic_upper=4*delta*(L+T*delta)**2
Bpic_integral_upper=L*T*delta**2+(T*T/3)*delta**3
Mpic_upper=math.exp(Gpic_upper)*Bpic_integral_upper
# O82 global lower for selection ALL: weighted cost >= integral B(t), with B(t)=3AB/5 exp(-5t)
global_integral_B=3*A*B/25
# Fourier operations for 2d real vector fields
cplx=complex
zero=lambda:np.zeros(2,dtype=complex)
def add_sin(d,k,component,amp):
  k=tuple(k)
  m=tuple(-x for x in k)
  d.setdefault(k,zero())[component]+=amp/(2j)
  d.setdefault(m,zero())[component]-=amp/(2j)
def linear(t):
  d={}
  add_sin(d,(0,2),0,A*math.exp(-4*t))
  add_sin(d,(1,0),1,B*math.exp(-t))
  return d
def nonlinear(u,v):
  d={}
  for p,up in u.items():
    for q,vq in v.items():
      k=(p[0]+q[0],p[1]+q[1])
      if k==(0,0): continue
      kk=np.asarray(k,dtype=float)
      # N=P div (u tensor v), with (u tensor v)_ij = u_i v_j; choose advection (u.grad)v
      val=1j*np.dot(kk,up)*vq
      proj=val-kk*np.dot(kk,val)/np.dot(kk,kk)
      d[k]=d.get(k,zero())+proj
  return {k:v for k,v in d.items() if np.linalg.norm(v)>1e-12}
def S(d):return float(sum(np.linalg.norm(v) for v in d.values()))
def R(d):return float(sum(np.linalg.norm(v)/math.hypot(*k) for k,v in d.items()))
U0=linear(0)
W=nonlinear(U0,U0)
assert len(W)==4,(len(W),list(W))
assert abs(S(W)-T)<1e-11,(S(W),T)
assert abs(R(W)-3*A*B/5)<1e-11,(R(W),3*A*B/5)
checks=0
rows=[]
for t in np.linspace(0,delta,111):
    V=linear(t)
    D={k:-t*math.exp(-5*t)*w for k,w in W.items()}
    U=dict(V)
    for k,d in D.items():U[k]=U.get(k,zero())+d
    F1=nonlinear(U,U)
    F0=nonlinear(V,V)
    for k,w in F0.items(): F1[k]=F1.get(k,zero())-w
    F1={k:w for k,w in F1.items() if np.linalg.norm(w)>1e-11}
    exact=R(F1)
    envelope=2*S(V)*S(D)+S(D)**2
    assert exact <=envelope+1e-9,(t,exact,envelope)
    assert abs(R(nonlin:=nonlinear(V,V)) - (3*A*B/5)*math.exp(-5*t))<1e-10
    # real and solenoidal Fourier
    for k,w in U.items():
        assert np.linalg.norm(w-np.conj(U[tuple(-x for x in k)]))<1e-10
        assert abs(np.dot(k,w))<1e-10
        checks+=2
    rows.append((float(t),exact,envelope, R(nonlin)))
# Rational bounds: prove strict inequalities without depending on floating integration.
d=F(9,800)  # 0.01125
heat_g_lower=4*(8-20*d)**2  # e^{-s}>=1-s
heat_b_lower=F(48,5)*(1-5*d)
x0=heat_g_lower*d
heat_M_rational_lower=heat_b_lower/heat_g_lower*sum(x0**j/F(factorial(j)) for j in range(1,9))
Tbar=F(2147,100)  # 48/sqrt(5)<21.47
x1=4*d*(8+Tbar*d)**2
exp_upper=sum(x1**j/F(factorial(j)) for j in range(21)) + x1**21/F(factorial(21))/(1-x1/F(22))
picard_M_rational_upper=exp_upper*(8*Tbar*d**2+Tbar**2*d**3/3)
assert heat_M_rational_lower>F(1,2)
assert picard_M_rational_upper<F(1,2)
assert heat_lower>.5 and Mpic_upper<.5
assert global_integral_B>.5
np.savetxt(root/'resultados'/'defecto_comparado.csv',rows,header='t,Picard_defecto_R,Picard_cota_envolvente,calor_defecto_R',delimiter=',',comments='')
report={
 'amplitudes':{'A':A,'B':B,'viscosidad':nu,'delta':delta},
 'certificado_calor_cota_inferior':heat_lower,
 'certificado_calor_cota_inferior_racional':float(heat_M_rational_lower),
 'certificado_picard_cota_superior_racional':float(picard_M_rational_upper),
 'certificado_calor_cota_superior_simple':heat_upper,
 'certificado_picard_cota_superior':Mpic_upper,
 'picard_cota_B_integrada':Bpic_integral_upper,
 'picard_cota_exposicion_G':Gpic_upper,
 'umbral':nu/2,
 'Bcalor_integrado_global':global_integral_B,
 'R_inicial_sin_modo':min(A/2,B),
 'S_W':S(W),'R_W':R(W),
 'modos_W':len(W),'chequeos_de_simetria_y_divergencia':checks,
 'comparacion_rigurosa':'calor M>0.5303>0.5; Picard M<0.4667<0.5 por cotas racionales',
 'estado':'Análisis local exacto, control espectral numérico; no prueba NS 3D general ni iteración global'
}
(root/'resultados'/'verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
try:
  import matplotlib.pyplot as plt
  t=np.array([z[0] for z in rows]); f=np.array([z[1] for z in rows]); e=np.array([z[2] for z in rows]); b=np.array([z[3] for z in rows])
  fig,ax=plt.subplots(figsize=(8,4.6))
  ax.plot(t,b,label='Defecto de referencia de calor')
  ax.plot(t,f,label='Defecto de referencia Picard 1')
  ax.plot(t,e,linestyle='--',label='Cota analítica de Picard 1')
  ax.set(xlabel='Tiempo físico t',ylabel='Norma crítica del defecto',title='O83 · incorporar la primera interacción reduce el defecto local')
  ax.grid(alpha=.2);ax.legend();fig.tight_layout()
  fig.savefig(root/'graficos'/'o83_comparacion_defectos.png',dpi=160)
  plt.close(fig)
except Exception as ex:
 print('Gráfico omitido:',ex)
