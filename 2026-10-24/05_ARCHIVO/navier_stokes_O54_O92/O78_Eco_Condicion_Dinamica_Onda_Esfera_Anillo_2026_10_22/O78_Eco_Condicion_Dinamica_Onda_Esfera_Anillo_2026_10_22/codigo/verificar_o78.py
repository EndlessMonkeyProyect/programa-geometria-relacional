#!/usr/bin/env python3
"""O78 reproducible: exact NS shear-wave, refinement and weighted tails.
No numerical solution of 3D generic Navier-Stokes is attempted.
"""
from __future__ import annotations
import csv
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'resultados'
OUTPUT.mkdir(exist_ok=True)
checks=[]

def ck(label, cond):
    checks.append({'prueba':label,'estado':'PASS' if bool(cond) else 'FAIL'})
    if not bool(cond): raise AssertionError(label)

# Exact symbolic verification of the traveling and viscously attenuating shear wave
A, nu, k, V, t, y, phi = sp.symbols('A nu k V t y phi', real=True)
f = A*sp.exp(-nu*k**2*t)*sp.sin(k*(y-V*t)+phi)
res = sp.simplify(sp.diff(f,t)+V*sp.diff(f,y)-nu*sp.diff(f,y,2))
ck('NS onda de cizalla exacta (componente x)', res == 0)
ck('divergencia cero por independencia de x', sp.diff(f,sp.Symbol('x')) == 0)
ck('fase arrastrada exacta', sp.simplify(sp.diff(k*(y-V*t)+phi,t)+V*sp.diff(k*(y-V*t)+phi,y)) == 0)

# Exact algebraic geometric/branch identities and Pell nested echo
for N in range(2,101):
    ck(f'identidad bilateral N={N}', N*N - (N-1)*(N+1) == 1)
for j in range(1,15):
    N=2**j; M=2*N
    ck(f'inclusion anidada {j}', M%N==0)
    ck(f'resto referenciado {j}', N*N*(M//N)**2 == M*M)  # 1/N² = (M/N)²/M²
N,m=3,2
pell=[]
for j in range(4):
    ck(f'Pell cuadratico paso {j}', N*N-2*m*m==1)
    pell.append({'j':j+1,'N':N,'m':m})
    Nnew = N*(4*N*N-3)
    mnew = m*(4*N*N-1)
    ck(f'Pell anidamiento {j}', Nnew%N==0)
    N,m=Nnew,mnew

# Fourier orthogonality in real-valued periodic shear flows
nu_val=0.025
rows=[]
for alpha in (1.,1.5,2.,3.):
    for J in (4,8,12,16):
        js=np.arange(1,J+1,dtype=float)
        w=np.power(2.,js)
        amps=np.power(2.,-alpha*js)
        E0=float(0.25*np.dot(amps,amps))
        W0=float(0.5*np.dot(w*amps,w*amps))
        P0=float(0.5*np.dot(w*w*amps,w*w*amps))
        ell0=math.sqrt(W0/P0)
        W1=float(0.5*np.sum((w*amps)**2*np.exp(-2*nu_val*w*w*0.1)))
        ck(f'escala positiva alpha={alpha},J={J}', 0<ell0<=0.5)
        ck(f'difusion disminuye vorticidad alpha={alpha},J={J}', W1<W0)
        rows.append({'alpha':alpha,'J':J,'energia_media_inicial':E0,'vorticidad_cuadratica_media_inicial':W0,'ell_omega_inicial':ell0,'vorticidad_t_0_1':W1})

# Exact endogenous spectral length law: Q=ell_omega^-2=<k^2>_enstrophy
# Q' = -2 nu Var_enstrophy(k^2) <= 0, so ell_omega is nondecreasing.
for alpha in (1.,1.5,2.):
    for J in (3,8,12):
        js=np.arange(1,J+1,dtype=float)
        kk=2.**js
        for T in (0.,.03,.3):
            weights=(kk*2.**(-alpha*js))**2 * np.exp(-2*nu_val*kk*kk*T)
            weights=weights/np.sum(weights)
            Q=float(np.sum(weights*kk*kk))
            variance=float(np.sum(weights*(kk*kk-Q)**2))
            qdot=-2*nu_val*variance
            ell=Q**(-.5)
            elldot=nu_val*variance/(Q**1.5)
            ck(f'variancia y monotonia alpha={alpha},J={J},t={T}', variance>=-1e-12 and qdot<=1e-12 and elldot>=-1e-12)
            if J==3 and T==0.:
                eps=1e-5
                wp=(kk*2.**(-alpha*js))**2*np.exp(-2*nu_val*kk*kk*eps)
                ep=1/math.sqrt(np.sum(wp*kk*kk)/np.sum(wp))
                ck(f'derivada escala diferencia finita alpha={alpha}', math.isclose((ep-ell)/eps,elldot,rel_tol=5e-4,abs_tol=1e-9))

# Alpha =1 gives exactly J/2 in mean squared vorticity; alpha=2 bounded by 1/6
for J in (1,4,8,12,32):
    j=np.arange(1,J+1,dtype=float)
    w1=0.5*np.sum(np.power(2.,2*(1.-1.)*j))
    w2=0.5*np.sum(np.power(2.,2*(1.-2.)*j))
    ck(f'crecimiento alfa 1 J={J}', math.isclose(w1,J/2,rel_tol=1e-12))
    ck(f'control alfa 2 J={J}', w2<1/6+1e-10)

# Direct quadrature across all modes, using independent spatial sampling
J=7; ngrid=2**13
ys=2*np.pi*np.arange(ngrid)/ngrid
for alpha in (1.,2.):
    for T in (0.,.03,.1):
        jj=np.arange(1,J+1)
        kk=2**jj
        amp=2.**(-alpha*jj)*np.exp(-nu_val*kk*kk*T)
        # independent sampling in physical space
        ux=np.sum(amp[:,None]*np.sin(kk[:,None]*ys[None,:]),axis=0)
        omega=np.sum((kk*amp)[:,None]*np.cos(kk[:,None]*ys[None,:]),axis=0)
        w_calc=np.mean(omega**2)
        e_calc=np.mean(ux**2)/2
        w_exact=np.sum((kk*amp)**2)/2
        e_exact=np.sum(amp**2)/4
        ck(f'Parseval vorticidad alpha={alpha} t={T}', abs(w_calc-w_exact)<3e-12)
        ck(f'Parseval energia alpha={alpha} t={T}', abs(e_calc-e_exact)<3e-12)

# Relational time countermodel: positive time-change and exact echo yet finite physical blowup
for j in range(1,19):
    t_j=1.0-2.0**(-j)
    N_j=2**j
    ell=1.0-t_j
    x=1.0/(1.0-t_j)
    s=-math.log(1.0-t_j)
    ck(f'normalizacion completa reloj Zeno j={j}', math.isclose(ell*x,1.,rel_tol=1e-12) and math.isclose(s,j*math.log(2.),rel_tol=1e-11))

with (OUTPUT/'o78_verificaciones.csv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=['prueba','estado']);wr.writeheader();wr.writerows(checks)
with (OUTPUT/'o78_cola_escalas.csv').open('w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=list(rows[0].keys()));wr.writeheader();wr.writerows(rows)
(OUTPUT/'o78_pell_anidado.json').write_text(json.dumps(pell,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'pruebas':len(checks),'superadas':sum(x['estado']=='PASS' for x in checks), 'fallidas':sum(x['estado']=='FAIL' for x in checks), 'estado':'exactitudes simbolicas, identidades aritmeticas, cuadratura periodica, y contraejemplo ODE sin pretension NS general', 'tabla_muestra':[r for r in rows if r['J']==12]}
(OUTPUT/'o78_resumen.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
