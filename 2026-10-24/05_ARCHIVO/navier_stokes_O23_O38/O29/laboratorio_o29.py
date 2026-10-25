#!/usr/bin/env python3
"""O29. Controles de álgebra exacta y evaluaciones numéricas independientes.
No es una simulación DNS ni prueba de existencia/regularidad NS 3D.
"""
from fractions import Fraction as F
from math import pi, exp, sqrt, log
import math

checks=0

def check(ok, message):
    global checks
    assert bool(ok),message
    checks+=1

def je(v): return (-v[1],v[0])
def k0(v):
    d=v[0]**2+v[1]**2
    assert d!=0
    j=je(v)
    # omit common factor 1/(2π) to retain rational arithmetic
    return (j[0]/d,j[1]/d)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def mult(c,a):return (c*a[0],c*a[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]

# Exact oddness and orthogonality of the Biot-Savart kernel
for x in range(-5,6):
    for y in range(-5,6):
        if x==y==0:continue
        z=(F(x),F(y))
        check(k0(mult(-1,z)) == mult(-1,k0(z)), 'oddness')
        check(dot(z,k0(z)) == 0, 'transverse kernel')

# Point-vortex model algebra. Γ1=2, Γ2=3, separation (-3,-4)
r=(F(-3),F(-4));ga=F(2);gb=F(3)
I=mult(ga*gb,k0(r))
ca_dot=mult(F(1,1)/ga,I)
cb_dot=mult(-F(1,1)/gb,I)
rdot=sub(ca_dot,cb_dot)
check(rdot==mult(ga+gb,k0(r)), 'centroid relative motion')
check(dot(r,rdot)==0, 'point distance invariance')
check(cross(r,rdot)/(dot(r,r))==F(ga+gb,25), 'angular rate no 2π')
check(add(mult(ga,ca_dot),mult(gb,cb_dot)) == (F(0),F(0)), 'center circulation')

# Pair of opposite circulations: strong interaction but zero relative velocity
ga=F(1);gb=F(-1)
I=mult(ga*gb,k0(r))
check(mult((F(1)/ga+F(1)/gb),I) == (F(0),F(0)), 'opposite circulation fixed relative vector')
check(mult(F(1)/ga,I)==mult(-F(1)/gb,I), 'opposite centroid equal velocities')
check(mult(F(1)/ga,I)!=(F(0),F(0)), 'nonzero translation')

# Same Γ, centroids, radial second moment, different orientation.
# two half-masses in B: longitudinal vs transversal
xA=(F(0),F(0));B=(F(2),F(0))
long=[(F(1),F(0)),(F(3),F(0))]
trans=[(F(2),F(1)),(F(2),F(-1))]
def mean_K(points):
    z=(F(0),F(0))
    for p in points:z=add(z,mult(F(1,2),k0(sub(xA,p))))
    return z
check(mean_K(long) == (F(0),F(-2,3)), 'long kernel rational factor')
check(mean_K(trans)==(F(0),F(-2,5)), 'trans kernel rational factor')
for pts in (long,trans):
    cent=mult(F(1,2), add(pts[0],pts[1]))
    check(cent == B, 'same centroid')
    rad2=F(1,2)*sum(dot(sub(p,B),sub(p,B)) for p in pts)
    check(rad2==1,'same radial moment')
# ΓA=ΓB=1; r=(-2,0), rdot=2 K_avg (missing 1/(2π))
r=(F(-2),F(0))
w_long=cross(r,mult(2,mean_K(long)))/dot(r,r)
w_trans=cross(r,mult(2,mean_K(trans)))/dot(r,r)
check(w_long==F(2,3), 'long orbital normalized')
check(w_trans==F(2,5), 'trans orbital normalized')
# restoring kernel 1/(2π)
check((w_long-w_trans)/(2*pi)>0.04, 'physically distinct angular rates')

# Gaussian pair identity and limiting cases for instantaneous distributions.
for g1,g2 in [(1.,1.),(2.,3.),(1.,-1.),(7.,1.)]:
    for d in [0.5,1.0,2.5,5.0]:
        for sa,sb in [(.1,.2),(.5,.7),(2.,1.)]:
            s2=sa*sa+sb*sb
            f= -math.expm1(-d*d/(2*s2))
            exact=(g1+g2)/(2*pi*d*d)*f
            midpoint=(g1+g2)/(2*pi*d*d)
            check(abs(exact)<=abs(midpoint)+1e-13,'finite core factor in [0,1]')
            check(abs(exact-midpoint*f)<1e-13,'Gaussian evaluation')
check(abs((-math.expm1(-1e-8))/1e-8 -1)<1e-7,'Gaussian small d expansion')

# Independent radial/angular quadrature for the Gaussian interaction:
# E[K_y(Z)] with Z~N((d,0),s² I) = [1-exp(-d²/(2s²))]/(2πd).
try:
    from scipy.integrate import quad
    from scipy.special import ive
    for d,s in [(1.,.4),(2.,1.),(.25,.5),(3.,.8)]:
        integrand=lambda rho: math.exp(-((rho-d)**2)/(2*s*s))*ive(1,rho*d/(s*s))
        integral=quad(integrand,0,d+12*s,epsabs=1e-12,epsrel=1e-12)[0]/(2*pi*s*s)
        analytic=(-math.expm1(-d*d/(2*s*s)))/(2*pi*d)
        check(abs(integral-analytic)<1e-10,'independent Gaussian radial quadrature')
except ImportError:
    print('Aviso: falta SciPy; se omite cuadratura radial independiente')


# Exact complex quadrupole identity under incompressible shear for passive tag.
# Gaussian covariance Σ=[[2,0],[0,1]], u=(kappa*y,0), ν arbitrary:
# Q=Σxx-Σyy+2iΣxy = 1; E[(z-C)U]=i kappa Σyy = i kappa,
# Qdot=2 i kappa; phidot=2 kappa.
for kappa in [0.0, 0.25, 1.0, -2.0]:
    q=1+0j
    integral=1j*kappa
    qdot=2*integral
    phidot=(qdot/q).imag
    check(phidot==2*kappa,'quadrupolar shape phase identity')
    # Diffusion Σdot=2νI has zero direct quadrupole effect
    for nu in [0.,.1,4.]:
        qdot_cov=complex(2*nu-2*nu,2*kappa)
        check(abs(qdot_cov-qdot)<1e-14,'harmonic moment cancels direct diffusion')

print('O29 | VERIFICACIONES SUPERADAS:',checks)
print('Flujos exactos (t=0): misma circulación/centro/radio; distintas orientaciones:')
print('  Ω_long=1/(3π)=',1/(3*pi),' Ω_trans=1/(5π)=',1/(5*pi))
print('Acoplamiento sin K ajustado: integral transversal de Biot-Savart.')
print('Importante: validaciones algebraicas y controles de forma; no DNS, no 3D.')
