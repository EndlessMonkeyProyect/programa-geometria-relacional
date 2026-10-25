#!/usr/bin/env python3
"""Comprobaciones simbólicas de un ansatz toroidal O54; no es prueba global de NS."""
import sympy as sp

R, a, theta, alpha = sp.symbols('R a theta alpha', positive=True, real=True)
r, z, K, Omega, nu = sp.symbols('s z K Omega nu', real=True, nonzero=True)
S = R + a*sp.cos(theta)
J = a*S
# Campo con velocidades angulares constantes theta_dot=alpha y phi_dot=beta
D_const = sp.factor(sp.diff(J*alpha, theta)/J)
assert sp.simplify(D_const + a*alpha*sp.sin(theta)/S) == 0

# El campo reparado: theta_dot=K/S, phi_dot=Omega.
D_fixed = sp.factor(sp.diff(J*K/S, theta)/J)
assert D_fixed == 0

# Componentes cilíndricas (s,z,phi) del campo con ambos recorridos activos
ur, uphi, uz = -K*z/r, Omega*r, K*(r-R)/r
D_3d = sp.factor(sp.diff(r*ur,r)/r + sp.diff(uz,z))
assert D_3d == 0
lap = lambda q: sp.diff(q,r,2) + sp.diff(q,r)/r + sp.diff(q,z,2)
L_phi = sp.simplify(lap(uphi) - uphi/r**2)
a_phi = sp.factor(ur*(sp.diff(uphi,r) + uphi/r) + uz*sp.diff(uphi,z))
assert L_phi == 0
assert sp.simplify(a_phi + 2*K*Omega*z/r)==0
# La ecuación phi exigiría dp/dphi=2 K Omega z (imposible con p periódica y K*Omega !=0).
dp_dphi_required = sp.simplify(-r*(a_phi - nu*L_phi))
assert dp_dphi_required == 2*K*Omega*z

# Control positivo: rotación rígida solo azimutal K=0.
assert sp.simplify(D_3d.subs(K,0))==0
assert sp.simplify(((-uphi**2/r) + sp.diff(Omega**2*r**2/2,r)).subs(K,0))==0

print('PASS: geometría ortogonal y velocidades angulares constantes pueden producir divergencia no nula')
print('D_const =', D_const)
print('PASS: ritmos corregidos dan divergencia tridimensional cero')
print('D_fixed =', D_fixed, '; D_3d =', D_3d)
print('PASS: el ansatz estacionario doble viola momentum azimutal sin fuerza')
print('a_phi =',a_phi,'; laplaciano(u_phi)=',L_phi,'; dp/dphi requerido =',dp_dphi_required)
print('PASS: rotación solo azimutal, K=0, es control positivo exacto en dominio con pared deslizante')
