#!/usr/bin/env python3
"""O67: comprobaciones algebraicas/espectrales, no demostracion de regularidad global."""
import json
from pathlib import Path
import numpy as np

BASE=Path(__file__).resolve().parents[1]
results=[]
def check(label,ok,extra=None):
    z={'control':label,'ok':bool(ok)}
    if extra is not None: z['detalle']=extra.tolist() if isinstance(extra,np.ndarray) else extra
    results.append(z)
    if not ok: raise AssertionError(z)

# Familia de cizallas exactas: mismo nivel de energia, distintas escalas.
nu=0.025
for m in [1,2,3,5,8,16,32,64]:
    for t in [0.,0.02,0.1,0.5]:
        A=np.exp(-nu*m*m*t)
        E=.25*A*A; W=.25*m*m*A*A; Z=.5*m**4*A*A
        check(f'cizalla_energia_m{m}_t{t}',np.isclose(E,.25*np.exp(-2*nu*m*m*t),rtol=1e-12,atol=1e-14))
        check(f'cizalla_relacion_escala_m{m}_t{t}',np.isclose(W/E,m*m,rtol=1e-12))
        check(f'cizalla_disipacion_W_m{m}_t{t}',np.isclose(-.5*nu*m**4*A*A+nu*Z,0,atol=1e-12))

# Una familia de funciones no negativas C1 por tramos, con L1 constante y L2 creciente.
# NO son soluciones NS: la inferencia logica sobre integrabilidad es solo funcional.
def integral_p(n,p):
    # y_n(t)= n sin^2(pi*n*(t-.25)) soportada en [1/4,1/4+1/n].
    # int (sin^2(pi s))^p ds para p=1,2 en [0,1].
    coeff={1: .5,2:3/8,3:5/16}[p]
    return n**(p-1)*coeff
for n in (2,4,8,16,32,64):
    check(f'pico_L1_constante_n{n}',abs(integral_p(n,1)-.5)<1e-12)
    check(f'pico_L2_creciente_n{n}',abs(integral_p(n,2)-3*n/8)<1e-12)
    check(f'pico_L3_creciente_n{n}',abs(integral_p(n,3)-5*n*n/16)<1e-12)

# Campo 3D del experimento O66, datos de fases diferentes.
L=24
axis=np.arange(L)*2*np.pi/L
x,y,z=np.meshgrid(axis,axis,axis,indexing='ij')
freq=np.fft.fftfreq(L,d=1/L)
kx,ky,kz=np.meshgrid(freq,freq,freq,indexing='ij')
K=np.array([kx,ky,kz]); ksq=np.sum(K*K,axis=0); kmag=np.sqrt(ksq)
mask=ksq>0
u=np.zeros((3,L,L,L),dtype=float)
u[0]=np.sin(y)+.2*np.cos(z)+.13*np.sin(y+z)
u[1]=.85*np.sin(z)+.11*np.cos(x)+.19*np.cos(z+x)
u[2]=.65*np.sin(x)+.17*np.cos(y)+.15*np.sin(x+y)

def analyze(velocity):
    h=np.fft.fftn(velocity,axes=(1,2,3))/L**3
    e=.5*np.sum(abs(h)**2,axis=0)
    sol=float(np.max(np.abs(np.sum(K*h,axis=0))))
    grads=np.array([[np.fft.ifftn(1j*K[j]*h[i]*L**3).real for j in range(3)] for i in range(3)])
    adv=np.einsum('jxyz,ijxyz->ixyz',velocity,grads)
    ah=np.fft.fftn(adv,axes=(1,2,3))/L**3
    aP=ah.copy(); s=np.sum(K*ah,axis=0)
    for i in range(3):aP[i,mask]-=K[i,mask]*s[mask]/ksq[mask]
    transfer=-np.real(np.sum(np.conj(h)*aP,axis=0))
    diss=2*nu*ksq*e
    tail_t={}; tail_d={}
    vmag=np.sort(np.unique(kmag))
    pos_budget=0.; signed_budget=0.; tail_zero=0.
    for left,right in zip(vmag[:-1],vmag[1:]):
        center=(left+right)*.5
        sel=kmag>=center
        ft=float(np.sum(transfer[sel])); dk=float(np.sum(diss[sel]))
        # K0=1: no contribution if right<=1.
        low=max(float(left),1.)
        if right>low:
            w=right*right-low*low
            pos_budget+=w*max(ft-dk,0.)
            signed_budget+=w*(ft-dk)
        if np.isclose(center,1.1,rtol=0,atol=.11):
            tail_zero=ft-dk
    nonlin=np.sqrt(np.sum(abs(aP)**2))
    lap=np.sqrt(np.sum((ksq**2)*np.sum(abs(h)**2,axis=0)))
    upper=lap*nonlin
    W=float(np.sum(ksq*e)); Z=float(np.sum(ksq**2*np.sum(abs(h)**2,axis=0)))
    return {'energy':float(np.sum(e)),'enstrophy':W,'Z':Z,'solenoidal':sol,
            'budget_pos':pos_budget,'signed_budget':signed_budget,
            'exact_cs_upper':upper,'total_transfer':float(np.sum(transfer)),
            'tail_K1_1':float(np.sum((transfer-diss)[kmag>=1.1])),
            'positive_budget_below_bound':bool(pos_budget<=upper+1e-10),
            'mode_energies':e,'nonlinearity_L2':nonlin}

alt=u.copy();alt[0]-=.26*np.sin(y+z)
r1,r2=analyze(u),analyze(alt)
check('campo_A_solenoidal',r1['solenoidal']<1e-12)
check('campo_B_solenoidal',r2['solenoidal']<1e-12)
check('energias_modales_identicas',np.allclose(r1['mode_energies'],r2['mode_energies'],atol=1e-12))
check('energia_total_identica',abs(r1['energy']-r2['energy'])<1e-12)
check('enstrofia_total_identica',abs(r1['enstrophy']-r2['enstrophy'])<1e-12)
check('transferencia_suma_cero_A',abs(r1['total_transfer'])<1e-12)
check('transferencia_suma_cero_B',abs(r2['total_transfer'])<1e-12)
check('transferencia_cola_signos_opuestos',r1['tail_K1_1']<0<r2['tail_K1_1'],[r1['tail_K1_1'],r2['tail_K1_1']])
check('presupuesto_positivo_no_negativo_A',r1['budget_pos']>=0)
check('presupuesto_positivo_no_negativo_B',r2['budget_pos']>=0)
check('presupuesto_cota_Cauchy_A',r1['positive_budget_below_bound'],[r1['budget_pos'],r1['exact_cs_upper']])
check('presupuesto_cota_Cauchy_B',r2['positive_budget_below_bound'],[r2['budget_pos'],r2['exact_cs_upper']])

# Desigualdad critica de Cauchy espectral Y^2 <= ||u||^2 Z, con norma sin normalizar
for name, rr in [('A',r1),('B',r2)]:
    V2=2*rr['energy'];Y=2*rr['enstrophy']; Z=rr['Z']
    check(f'Cauchy_frecuencias_{name}',Y*Y<=V2*Z+1e-12,[Y*Y,V2*Z])

# Comportamiento de escala (en R^3): ||u_lambda||_2=lambda^-1/2 ||u||_2
# ||grad u_lambda||_2=lambda^1/2||grad u||_2; chi invariante.
for lam in (0.125,.25,.5,1.,2.,4.,8.):
    base=2.;grad=3.; v=lam**(-.5)*base;g=lam**.5*grad
    check(f'indice_critico_escala_{lam}',abs(np.sqrt(v*g)-np.sqrt(base*grad))<1e-12)

summary={
 'programa':'O67 — cota crítica y barrera de cierre del presupuesto',
 'fecha':'2026-10-21',
 'numero_controles':len(results),
 'aprobados':sum(r['ok'] for r in results),
 'datos_fase_A':{k:v for k,v in r1.items() if k not in ('mode_energies',)},
 'datos_fase_B':{k:v for k,v in r2.items() if k not in ('mode_energies',)},
 'contraejemplo_funcional':{'L1':integral_p(64,1),'L2_n64':integral_p(64,2),'L3_n64':integral_p(64,3)},
 'limite':'Las pruebas numéricas respaldan identidades y desigualdades para estados finitos. NO se ha derivado una cota global universal ni resuelto NS sin forzamiento.'
}
(BASE/'resultados'/'controles.json').write_text(json.dumps({'resumen':summary,'controles':results},ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k not in ('datos_fase_A','datos_fase_B')},ensure_ascii=False,indent=2))
print('A/B budgets:',r1['budget_pos'],r2['budget_pos'],'Upper bounds:',r1['exact_cs_upper'],r2['exact_cs_upper'])
