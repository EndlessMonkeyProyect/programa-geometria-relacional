#!/usr/bin/env python3
"""O49. Checks algebraic/kinematic identities and thin-core asymptotic benchmarks.
NOT a Navier-Stokes or Euler DNS; it does not prove physical synchronisation or regularity.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import sympy as sp

p = Path(__file__).resolve().parent
r,z,t,R,a,U,A,Gamma,V,nu = sp.symbols('r z t R a U A Gamma V nu', positive=True, real=True)
eta=sp.Function('eta')(r,z,t)
ur=sp.Function('ur')(r,z,t)
uz=sp.Function('uz')(r,z,t)
omega=r*eta
# Vorticity equation for axisymmetric NS without azimuthal fluid velocity.
Ltheta = (sp.diff(omega,t)+ur*sp.diff(omega,r)+uz*sp.diff(omega,z)-ur/r*omega
          -nu*(sp.diff(omega,r,2)+sp.diff(omega,r)/r+sp.diff(omega,z,2)-omega/r**2))
Letta = r*(sp.diff(eta,t)+ur*sp.diff(eta,r)+uz*sp.diff(eta,z)
          -nu*(sp.diff(eta,r,2)+3*sp.diff(eta,r)/r+sp.diff(eta,z,2)))
assert sp.simplify(Ltheta-Letta)==0

# Stream function with a closed meridional streamline around (R,0).
psi = U*r**2/sp.Integer(2) + A*((r-R)**2+z**2)
psi_relative=psi-U*r**2/sp.Integer(2)
assert sp.simplify(psi_relative.subs({r:R-a,z:0})-psi_relative.subs({r:R+a,z:0}))==0
v_r=-sp.diff(psi,z)/r
v_z=sp.diff(psi,r)/r
assert sp.simplify(sp.diff(r*v_r,r)+sp.diff(r*v_z,z))==0
balance=sp.integrate(r*(v_z-U),(r,R-a,R+a))
assert sp.simplify(balance)==0
U_by_boundary=2*(psi.subs({r:R+a,z:0})-psi.subs({r:R-a,z:0}))/((R+a)**2-(R-a)**2)
assert sp.simplify(U_by_boundary-U)==0
assert sp.simplify(2*sp.integrate(r*v_z,(r,R-a,R+a))/((R+a)**2-(R-a)**2)-U)==0

# Galilean invariance: add uniform axial velocity V.
psi_boosted=psi+V*r**2/sp.Integer(2)
U_boosted=U_by_boundary.subs(U,U+V)
assert sp.simplify(psi_boosted-(U+V)*r**2/2-psi_relative)==0
assert sp.simplify(U_boosted-(U+V))==0

# Uniform core vs hollow core Kelvin-Fetter asymptotic velocities.
U_solid=Gamma/(4*sp.pi*R)*(sp.log(8*R/a)-sp.Rational(1,4))
U_hollow=Gamma/(4*sp.pi*R)*(sp.log(8*R/a)-sp.Rational(1,2))
assert sp.simplify(U_solid-U_hollow-Gamma/(16*sp.pi*R))==0
Omega_core=Gamma/(2*sp.pi*a**2) # approximate solid-body core angular frequency
ratio=sp.simplify(U_solid/(a*Omega_core))
assert sp.simplify(ratio-a/(2*R)*(sp.log(8*R/a)-sp.Rational(1,4)))==0

eps=np.array([0.02,0.05,0.10,0.15,0.20],float)
rows=[]
for e in eps:
    radius=1.0; core=e; circ=1.0
    s=circ/(4*math.pi*radius)*(math.log(8*radius/core)-0.25)
    h=circ/(4*math.pi*radius)*(math.log(8*radius/core)-0.50)
    om=circ/(2*math.pi*core**2)
    rows.append({'a_over_R':float(e),'U_solid':s,'U_hollow':h,'U_over_a_Omega_solid':s/(core*om)})
for i in range(len(rows)-1):
    assert rows[i]['U_over_a_Omega_solid'] < rows[i+1]['U_over_a_Omega_solid']
assert math.isclose(float(sp.limit(ratio.subs({R:1,Gamma:1}),a,0,dir='+')),0.,abs_tol=1e-14)

# Direct quadrature of closed relative radial flux for three radial resolutions.
checks=[]
for n in [17, 257, 8193]:
    R0, a0, U0, A0=1.,.1,.37,.07
    rgrid=np.linspace(R0-a0,R0+a0,n)
    uz_grid=U0+2*A0*(rgrid-R0)/rgrid
    integral=np.trapezoid(rgrid*(uz_grid-U0),rgrid)
    assert abs(integral)<5e-15, (n,integral)
    checks.append({'points':n,'signed_flux_residual':float(integral),'inner_uz_minus_U':float(uz_grid[0]-U0),'outer_uz_minus_U':float(uz_grid[-1]-U0)})

result={'claims':[
    'Axisymmetric viscous vorticity ratio PDE is algebraically exact under no-swirl assumptions',
    'Moving-frame streamfunction constant along example meridional closed streamline',
    'Core radial weighted flux cancellation in translating frame',
    'Boundary-difference expression recovers axial speed',
    'Galilean invariance requires ambient-relative velocity',
    'Core profile affects classical thin-core axial velocity',
    'Axial-to-poloidal tangential speed ratio depends on slenderness and tends to zero'
    ],'thin_core_benchmark':rows,'flux_checks':checks,
    'limitations':['Streamfunction test case is kinematic, NOT asserted to solve NS/Euler momentum equation',
    'Thin-core speed is asymptotic and model-dependent',
    'No interior/exterior Lagrangian phase difference was inferred from radius or speed',
    'No regularity theorem for general 3D Navier-Stokes']}
(p/'resultados_o49.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PASS 7 algebraic/model groups + 3 quadrature resolutions')
for row in rows:print(f"eps={row['a_over_R']:.2f}, U={row['U_solid']:.8f}, U/(a*Omega)={row['U_over_a_Omega_solid']:.8f}")
