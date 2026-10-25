#!/usr/bin/env python3
"""R–02: controles algebraicos exactos y numéricos, SIN certificación de Yang–Mills 4D.
Ejecutar: python verificar_r02.py
"""
from __future__ import annotations
import json, math, random
from pathlib import Path
import numpy as np
import sympy as s

SEED = 20261023
rng = np.random.default_rng(SEED)
I = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]],dtype=complex)
sy = np.array([[0,-1j],[1j,0]],dtype=complex)
sz = np.array([[1,0],[0,-1]],dtype=complex)
sigma = (sx,sy,sz)

def su2_random():
    q = rng.standard_normal(4)
    q = q / np.linalg.norm(q)
    return q[0]*I + 1j*sum((q[i+1]*sigma[i] for i in range(3)),start=np.zeros((2,2),complex))

def inv(U):
    return U.conj().T

def trn(U):
    return float(np.trace(U).real/2)

def Q(U,V):
    return (trn(U),trn(V),trn(U@V))

def nu(U,V):
    K=U@V@inv(U)@inv(V)
    return 1-trn(K)

# Parte simbólica exacta
im=s.I
ex=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-im],[im,0]])
Z=s.Matrix([[1,0],[0,-1]])
U=im*X; V=im*Y
W=s.simplify(U*V)
assert W == -im*Z
assert s.simplify(U*V*U.inv()*V.inv()) == -ex
assert s.simplify(ex*(-im*Z)) == W
assert s.simplify(ex*(-im*Z)*ex.inv()*(-im*Z).inv()) == ex
# Diferencia marginal invisible: misma x,y, distinta z
assert s.trace(im*Z)==s.trace(im*X)==0
assert s.trace((im*Z)*(im*Z))/2 == -1
assert s.trace((im*Z)*(im*X))/2 == 0

# CRT: independencia prima y conservación de comparación anterior.
N,p=6,5
L=math.lcm(N,p)
assert L==30
for r in range(N):
    poss=[x for x in range(L) if x % N == r]
    assert len(poss)==p and set(x%p for x in poss)==set(range(p))
for a in range(L):
    for b in range(L):
        # actualización afín y proyección a residuos
        assert ((7*a+b)%L)%N == (7*(a%N)+b)%N
        assert ((7*a+b)%L)%p == (7*(a%p)+b)%p

# Parte numérica: leyes gauge en cadenas y pares de lazos.
num=1200
maxerr=0.0
for t in range(num):
    g0,g1,g2,g3=[su2_random() for _ in range(4)]
    T01,T12,T23=[su2_random() for _ in range(3)]
    P = T23@T12@T01
    Tp01=g1@T01@inv(g0)
    Tp12=g2@T12@inv(g1)
    Tp23=g3@T23@inv(g2)
    maxerr=max(maxerr,float(np.linalg.norm(Tp23@Tp12@Tp01 - g3@P@inv(g0))))
    # una subdivisión artificial: T = T2 T1, gauge nuevo nodo se cancela
    A=su2_random(); T=su2_random(); h=su2_random()
    T1=A; T2=T@inv(A)
    maxerr=max(maxerr,float(np.linalg.norm(T2@T1-T)))
    T1p=h@T1@inv(g0)
    T2p=g2@T2@inv(h)
    maxerr=max(maxerr,float(np.linalg.norm(T2p@T1p - g2@T@inv(g0))))
    U,V=su2_random(),su2_random()
    h0=su2_random(); Up=h0@U@inv(h0); Vp=h0@V@inv(h0)
    maxerr=max(maxerr,*[abs(a-b) for a,b in zip(Q(U,V),Q(Up,Vp))])
    maxerr=max(maxerr,abs(nu(U,V)-nu(Up,Vp)))
    x,y,z=Q(U,V)
    right=2*(1-x*x-y*y-z*z+2*x*y*z)
    maxerr=max(maxerr,abs(nu(U,V)-right))
    assert -1e-11 <= nu(U,V) <= 2+1e-11

assert maxerr<1e-11, maxerr
# Información perdida por bloqueo equivarante B(U,V)=UV.
U1,V1 = 1j*sx,1j*sy
U2,V2 = I,-1j*sz
assert np.allclose(U1@V1,U2@V2)
assert abs(nu(U1,V1)-2)<1e-12
assert abs(nu(U2,V2))<1e-12

# Independencia de nuevo lazo y no suficiencia dinámica de la firma vieja.
oldU,oldV=I,I
S1,S2=I,-I
assert Q(oldU,oldV)==(1.0,1.0,1.0)
assert trn(S1)!=trn(S2)
# F(U,V,S) = (US,V,S): covariante por conjugación simultánea;
# dos estados con misma firma antigua generan respuestas distintas.
assert Q(oldU@S1,oldV) != Q(oldU@S2,oldV)

# No-go de brecha física por sola invariancia de identidad.
aseq=[1/2**k for k in range(1,13)]
qs=[math.exp(-a) for a in aseq]
assert all(0<q<1 for q in qs)
assert qs[-1]>qs[0]
assert all(abs((-math.log(q))-a)<1e-13 for a,q in zip(aseq,qs))

out={
    'semilla':SEED,
    'controles_matriciales_aleatorios':num,
    'error_maximo':maxerr,
    'caso_bloqueo':{
        'traza_bloque_ambas':trn(U1@V1),
        'nu_composicion_noabeliana':nu(U1,V1),
        'nu_composicion_conmutante':nu(U2,V2),
        'misma_matriz_bloqueada':True,
    },
    'refinamiento_modular':{'N':N,'p':p,'L':L,'subdivisiones_por_clase':p},
    'continuidad_espectral_auxiliar':{'gap_primero':aseq[0],'gap_ultimo':aseq[-1],'q_ultimo':qs[-1]},
    'resultado':'Todos los controles finitos y simbólicos pasaron; NO es prueba del gap Yang–Mills.'
}
path=Path(__file__).with_name('resultados_r02.json')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
