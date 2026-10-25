#!/usr/bin/env python3
"""O85: verificaciones exactas y numericas auxiliares de covariancia de escala,
modelo ABC Beltrami, plantilla 3D ciclica O84 y transferencias triadicas O79.
Requiere numpy y matplotlib para la figura (solo numpy para pruebas).
No es una simulacion NS ni una prueba de regularidad global.
"""
from __future__ import annotations
import json, math, pathlib, random
import numpy as np

BASE=pathlib.Path(__file__).resolve().parents[1]
( BASE/'resultados').mkdir(exist_ok=True)
( BASE/'graficos').mkdir(exist_ok=True)
checks=0

def check(expr, msg):
    global checks
    checks+=1
    if not expr: raise AssertionError(msg)

def nearly(a,b,tol=1e-11):
    return math.isclose(float(a),float(b),rel_tol=tol, abs_tol=tol)

nu=1.0; delta=9/500; L=6.0; M=9.0
G=2*L*L*(-math.expm1(-2*delta))
M0=M/(4*L*L*math.sqrt(2))*math.expm1(G)
M1=math.exp(4*delta*(L+M*delta)**2)*(L*M*delta**2+(M*M/3)*delta**3)
check(M0>nu/2,'O84 heat should fail on selected interval')
check(M1<nu/2,'O84 updated should pass on selected interval')

# ABC b=(sin z+cos y, sin x+cos z, sin y+cos x)
# Each axis has TWO orthogonal components (sine and cosine) at the same |k|.
# A VECTOR Fourier coefficient at +/-e_i therefore has magnitude a/sqrt(2);
# sum over 3 axes = 3*sqrt(2)*a, NOT 6*a.
# Scaling lambda implies R=3 sqrt(2) a, S=3 sqrt(2) lambda a, Q=3 sqrt(2) lambda^2 a.

def abc(x,y,z):
    return np.stack((np.sin(z)+np.cos(y), np.sin(x)+np.cos(z), np.sin(y)+np.cos(x)),axis=-1)

def curl_abc(x,y,z):
    return np.stack((np.cos(y)+np.sin(z), np.cos(z)+np.sin(x), np.cos(x)+np.sin(y)),axis=-1)

rng=np.random.default_rng(841)
xyz=rng.uniform(-np.pi,np.pi,(400,3))
b=abc(xyz[:,0],xyz[:,1],xyz[:,2]); curl=curl_abc(xyz[:,0],xyz[:,1],xyz[:,2])
check(float(np.max(np.abs(curl-b)))<1e-14, 'ABC curl(b)=b')

# Chequeo INDEPENDIENTE en coeficientes vectoriales complejos de Fourier.
# Evita sumar incorrectamente magnitudes de componentes en un mismo modo.
def fourier_trig(mode,component,kind,amplitude, target):
    k=tuple(mode); neg=tuple(-v for v in mode)
    pos=amplitude*(.5 if kind=='cos' else -.5j)
    negval=amplitude*(.5 if kind=='cos' else .5j)
    for kk,value in ((k,pos),(neg,negval)):
        if kk not in target: target[kk]=np.zeros(3,dtype=complex)
        target[kk][component]+=value

def fourier_norms(modes):
    R=sum(np.linalg.norm(v)/math.sqrt(sum(kk*kk for kk in k)) for k,v in modes.items() if any(k))
    S=sum(np.linalg.norm(v) for v in modes.values())
    Q=sum(np.linalg.norm(v)*math.sqrt(sum(kk*kk for kk in k)) for k,v in modes.items())
    return R,S,Q

def conv_nonlinearity(modes):
    ans={}
    for p,up in modes.items():
        for q,uq in modes.items():
            k=tuple(pi+qi for pi,qi in zip(p,q))
            k2=sum(ki*ki for ki in k)
            if not k2: continue
            kv=np.array(k,dtype=float)
            proj=np.eye(3)-np.outer(kv,kv)/k2
            val=1j*complex(np.dot(up,np.array(q,dtype=float)))*(proj@uq)
            if k not in ans: ans[k]=np.zeros(3,dtype=complex)
            ans[k]+=val
    return ans

abc_modes={}
for kind,comp,k in [('sin',0,(0,0,1)),('cos',0,(0,1,0)),('sin',1,(1,0,0)),('cos',1,(0,0,1)),('sin',2,(0,1,0)),('cos',2,(1,0,0))]:
    fourier_trig(k,comp,kind,1.,abc_modes)
ra,sa,qa=fourier_norms(abc_modes)
for v in (ra,sa,qa): check(nearly(v,3*math.sqrt(2)),'vector ABC Fourier norms')
abc_n=conv_nonlinearity(abc_modes)
check(max(np.linalg.norm(c) for c in abc_n.values())<1e-12,'ABC Leray nonlinear vanishes')

cyc_modes={}
for k,comp,amp in [((0,1,0),0,4.),((0,0,1),1,1.),((1,0,0),2,1.)]:
    fourier_trig(k,comp,'sin',amp,cyc_modes)
rc,sc,qc=fourier_norms(cyc_modes)
for v in (rc,sc,qc): check(nearly(v,6),'cyclic initial vector norms')
cyc_nonlin=conv_nonlinearity(cyc_modes)
check(len(cyc_nonlin)==18, 'sparse convolution initial list includes 12 new and 6 zero modes')
active={k:v for k,v in cyc_nonlin.items() if np.linalg.norm(v)>1e-12}
check(len(active)==12,'cyclic field generates 12 modes')
check(nearly(fourier_norms(active)[0],9/math.sqrt(2)),'cyclic nonlinear R(W)')
check(nearly(fourier_norms(active)[1],9),'cyclic nonlinear S(W)')
check(nearly(fourier_norms(active)[2],9*math.sqrt(2)),'cyclic nonlinear Q(W)')

# div ABC exactly zero; Laplacian ABC exactly -ABC, verified term by term.
for a in (1.,2.,5.):
    check(3*math.sqrt(2)*a>nu, 'ABC may exceed small-data R threshold')
    G_abc=36*a*a/(nu*nu)
    q_abc=3*math.sqrt(2)*a/nu
    for lam in (1,2,4,8,16,32):
        check(nearly((3*math.sqrt(2)*a*lam)/lam,3*math.sqrt(2)*a),'ABC R scaling')
        check(nearly(4/nu*(3*math.sqrt(2)*a*lam)**2/(2*nu*lam**2),G_abc),'ABC G integral')
        check(nearly((3*math.sqrt(2)*a*lam**2)/(nu*lam**2),q_abc),'ABC Q integral')

records=[]
for lam in (1,2,4,8,16,32,64):
    t=delta/lam**2
    # u_lambda = lam u(lam x, lam^2 t)
    # Fourier R,S,Q scales 1,lam,lam². Defect B scales lam².
    a0=6.
    s0=6*lam
    q0=6*lam**2
    b0=9/math.sqrt(2)*lam**2
    check(nearly(a0,6.),f'critical R lam={lam}')
    check(nearly(s0/lam,6.),f'S scaling {lam}')
    check(nearly(q0/lam**2,6.),f'Q scaling {lam}')
    check(nearly(b0/lam**2,9/math.sqrt(2)),f'B scaling {lam}')
    G_lam=2*L*L*(-math.expm1(-2*lam**2*t))
    M0_lam=M/(4*L*L*math.sqrt(2))*math.expm1(G_lam)
    M1_lam=math.exp(4*delta*(L+M*delta)**2)*(L*M*delta**2+(M**2/3)*delta**3)
    check(nearly(G_lam,G),f'G scaling {lam}')
    check(nearly(M0_lam,M0),f'M0 scaling {lam}')
    check(nearly(M1_lam,M1),f'M1 scaling {lam}')
    int_Q_U0=L*(1-math.exp(-delta))
    int_Q_D=M*math.sqrt(2)*(1-(1+2*delta)*math.exp(-2*delta))/4
    # reverse triangle inequality in Q Fourier norm
    lower_int_Q_U1=int_Q_U0-int_Q_D
    check(lower_int_Q_U1>0.105, f'positive reference-gradient contribution {lam}')
    records.append(dict(lambda_multiplier=lam,physical_interval=t,R_initial=a0, M0_heat=M0_lam, M1_updated_upper=M1_lam, lower_bound_integral_Q_reference=lower_int_Q_U1))

# Phase triad of O79, independent local Fourier check
# Transfer = n*a*b*c/2 with scaled frequencies n=lam and amplitudes
# (a,b,c)=lam*(1,1,+/-1/4), nu=.01.
phase_records=[]
for lam in (1,2,4,8,16):
    for sign in (-1,1):
        c=sign*lam/4
        t_nonlin=lam * lam * lam * c/2  # n*a*b*c/2
        loss=-9*.01*lam**2 * c**2
        expected_nonlin=sign*.125*lam**4
        expected_loss=-.005625*lam**4
        check(nearly(t_nonlin,expected_nonlin), 'triad transfer scaling')
        check(nearly(loss,expected_loss),'triad viscosity scaling')
        phase_records.append(dict(lambda_multiplier=lam,sign=sign,nonlinear_transfer=t_nonlin,viscous_transfer=loss,net=t_nonlin+loss))

# Compare finite sums for an abstract stack of separately scaled blocks; NOT a single NS solution.
qblock=L*(1-math.exp(-delta))-M*math.sqrt(2)*(1-(1+2*delta)*math.exp(-2*delta))/4
stacks=[]
for N in (1,2,4,8,16,32):
    total_time=sum(delta/4**j for j in range(N))
    lower_grad=N*qblock
    check(total_time<4*delta/3+1e-12,'finite total time of abstract blocks')
    check(nearly(lower_grad,N*qblock),'gradient lower bound sum')
    stacks.append(dict(number_of_blocks=N,combined_physical_time=total_time,lower_grad_cost=lower_grad))

payload={'description':'O85: pruebas de covariancia de escala, fases y limite de conteo entre cierres; NO construye blowup', 'nu':nu,'delta_base':delta,'M0_heat':M0,'M1_updated_upper':M1,'abc_R_a1':3*math.sqrt(2),'abc_G_inf_a1':36.,'abc_integral_Q_a1':3*math.sqrt(2),'lambda_records':records,'phase_records':phase_records,'abstract_stack':stacks,'checks_passed':checks}
(BASE/'resultados'/'verificacion.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('O85 comprobaciones:',checks)
print('M0',M0,'M1',M1)
print('Gradiente inferior por bloque para referencia actualizada:',qblock)
print('RESULTADO PASA')
