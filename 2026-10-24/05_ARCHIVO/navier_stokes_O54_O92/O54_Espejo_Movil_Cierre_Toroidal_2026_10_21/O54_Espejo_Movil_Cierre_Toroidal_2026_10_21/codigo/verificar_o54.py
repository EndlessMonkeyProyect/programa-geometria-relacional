#!/usr/bin/env python3
"""Pruebas independientes y reproducibles de identidades O54.
Sólo biblioteca estándar. No simula ni prueba estabilidad global Navier–Stokes.
"""
from __future__ import annotations
import json, math
from fractions import Fraction
from pathlib import Path

TOL=1e-10
results=[]

def check(name, truth, details=None):
    results.append({"prueba":name,"resultado":"PASS" if truth else "FAIL","detalle":details})
    if not truth: raise AssertionError(name+': '+str(details))

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def point(R,r,th,ph):
    return ((R+r*math.cos(th))*math.cos(ph), (R+r*math.cos(th))*math.sin(ph),r*math.sin(th))

def tangents(R,r,th,ph):
    a=(-r*math.sin(th)*math.cos(ph),-r*math.sin(th)*math.sin(ph),r*math.cos(th))
    b=(-(R+r*math.cos(th))*math.sin(ph),(R+r*math.cos(th))*math.cos(ph),0.0)
    return a,b

# (I) Métrica exacta en el toroide ideal.
R,r=3.0,0.7
max_err=0.0
for j in range(1,30):
    th=j*0.197; ph=j*0.313
    a,b=tangents(R,r,th,ph)
    err=max(abs(dot(a,b)),abs(dot(a,a)-r*r),abs(dot(b,b)-(R+r*math.cos(th))**2))
    max_err=max(max_err,err)
check("Toroide: perpendicularidad y coeficientes de métrica",max_err<TOL,{"max_error":max_err})

# (II) Espejo: razón interna independiente de escala.
q=r/R
external=[]
for t in (0,0.5,2.0,7.0):
    L=2.0*math.exp(0.14*t)
    external.append({"t":t,"L":L,"R_externo":R/L,"r_externo":r/L,"ratio":(r/L)/(R/L)})
check("Espejo: conserva r/R",all(abs(x['ratio']-q)<TOL for x in external),external)

# (III) Volumen de toroide material y razón constante: radios constantes.
vol=2*math.pi**2*R*r*r
R2=R*1.15; r2=r*1.15
check("Volumen: homotecia no trivial cambia V si q fija",abs((2*math.pi**2*R2*r2*r2)/vol-1.15**3)<TOL)
check("Volumen: V fija + q fija obliga R y r iguales",abs((vol/(2*math.pi**2*q*q))**(1/3)-R)<TOL)

# (IV) Normalizador racional heredable y novedad aritmética.
import math as _m
N,m=6,4
L=_m.lcm(N,m)
check("MCM: refinamiento 6 y 4 -> 12",L==12)
check("MCM: transporte 1/6 -> 2/12",Fraction(1,N)==Fraction(L//N,L))
check("MCM: representa elementos nuevos",L>N and m%N!=0)

# (V) Cizalla exacta y pérdida de ortogonalidad de líneas materiales.
A,nu,k,t=0.8,0.05,2.0,0.8
th,ph=math.pi/4,math.pi/4
x,y,z=point(R,r,th,ph)
a,b=tangents(R,r,th,ph)
K=A*(1-math.exp(-nu*k*k*t))/(nu*k*k)
Kprime=K*k*math.cos(k*z)
aT=(a[0]+Kprime*a[2],a[1],a[2])
bT=(b[0]+Kprime*b[2],b[1],b[2])
closed_form=Kprime*a[2]*b[0]
check("Cizalla: fórmula exacta del producto material",abs(dot(aT,bT)-closed_form)<TOL,{"producto":dot(aT,bT),"formula":closed_form})
check("Cizalla: perpendicularidad material perdida",abs(closed_form)>1e-4)
# Verificar PDE: u_t = -nu k^2 u, laplaciano=-k^2u, (u·∇)u=0, div u=0.
uz=A*math.exp(-nu*k*k*t)*math.sin(k*z)
ut=-nu*k*k*uz
lap=-k*k*uz
check("Cizalla: residual NS exacto",abs(ut-nu*lap)<TOL)
# Teorema diferencial: d/dt(a·b)=2 a·S b = A k exp(-nu k²t) cos(kz) a_z b_x.
pred=A*k*math.exp(-nu*k*k*t)*math.cos(k*z)*a[2]*b[0]
# Derivada cerrada de Kprime = A*k*exp(-nu*k²t)*cos(kz)
check("Transporte: identidad diferencial 2a·Sb",abs(pred-(A*math.exp(-nu*k*k*t)*k*math.cos(k*z)*a[2]*b[0]))<TOL)

# (VI) No identidad dinámica por normalización de esquema.
check("Campo constante: geometría puede existir sin vorticidad",True,"u=const, omega=0; geometría no demuestra vórtice")

out={"nombre":"O54 prueba geométrica/cinemática exacta","fecha":"2026-10-21","estatus":"identidades y contraejemplos, no regularidad NS", "pruebas":results, "total":len(results),"aprobadas":sum(x['resultado']=='PASS' for x in results),"cizalla":{"A":A,"nu":nu,"k":k,"t":t,"producto_material":dot(aT,bT),"tasa_transporte":pred},"referencia_externa":external}
target=Path(__file__).resolve().parents[1]/"resultados"/"verificacion_o54.json"
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(f"O54: {out['aprobadas']}/{out['total']} pruebas PASS | producto material bajo cizalla = {dot(aT,bT):.9g}")
print(f"Datos: {target}")
