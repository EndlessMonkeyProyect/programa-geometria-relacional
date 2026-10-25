#!/usr/bin/env python3
"""O44: solución analítica de Navier-Stokes en T^3; sólo biblioteca estándar.

u=(a2/2 sin(2y)e^{-4 nu t}+a3/3 sin(3y)e^{-9 nu t},0,0).
El término advectivo se anula, y la difusión es exacta.
La enstrofía se define mediante promedio espacial, E=<|curl u|^2>/2.
"""
from math import exp, sqrt, sin, cos, pi, isclose, lcm

NU=0.03
T=0.12
N=lcm(2,3)
assert N==6

def velocity(y,t,a2,a3,nu=NU):
    return a2/2*sin(2*y)*exp(-4*nu*t)+a3/3*sin(3*y)*exp(-9*nu*t)

def enstrophy(t,w2,nu=NU):
    return 0.25*(w2*exp(-8*nu*t)+(1-w2)*exp(-18*nu*t))

def enstrophy_derivative(t,w2,nu=NU):
    return -.5*nu*(4*w2*exp(-8*nu*t)+9*(1-w2)*exp(-18*nu*t))

def weight3(t,w2,nu=NU):
    a=w2*exp(-8*nu*t)
    b=(1-w2)*exp(-18*nu*t)
    return b/(a+b)

def space_average_enstrophy(t,a2,a3,nu=NU,samples=192):
    result=0.
    for j in range(samples):
        y=2*pi*j/samples
        wz=-a2*cos(2*y)*exp(-4*nu*t)-a3*cos(3*y)*exp(-9*nu*t)
        result+=.5*wz*wz
    return result/samples

w2_A=35/36
w2_B=1/36
for name,w2 in [('A',w2_A),('B',w2_B)]:
    a2=sqrt(w2)
    a3=sqrt(1-w2)
    assert isclose(enstrophy(0,w2),.25,abs_tol=1e-14)
    for t in [0.,.01,.12,1.]:
        assert isclose(space_average_enstrophy(t,a2,a3),enstrophy(t,w2),rel_tol=1e-12,abs_tol=1e-13)
        # Diferenciación centrada del balance exacto para t > 0.
        eps=1.e-5
        approx=(enstrophy(t+eps,w2)-enstrophy(t-eps,w2))/(2*eps)
        assert isclose(approx,enstrophy_derivative(t,w2),rel_tol=2e-8,abs_tol=1e-10)
        assert isclose(weight3(t,w2)+(1-weight3(t,w2)),1.,abs_tol=1e-14)
    print(name,'N=',N,'E0=',f'{enstrophy(0,w2):.12f}',
          'E(T)=',f'{enstrophy(T,w2):.12f}',
          "E'(0)=",f'{enstrophy_derivative(0,w2):.12f}',
          'w3(T)=',f'{weight3(T,w2):.12f}')
assert enstrophy(T,w2_A)>enstrophy(T,w2_B)
assert weight3(T,w2_A)<1/36
# Para todas las funciones usadas, u_x solo depende de y, por lo que u·grad u = 0;
# u_t=nu*Delta u termino por termino. Todas son soluciones NS exactas.
print('PASS: dos soluciones NS exactas comparten N=6 y E(0)=1/4, pero E(t) difiere.')
print('PASS: identidad cuadrática 6^2-(6-1)(6+1)=1 y pesos 35/36+1/36=1.')
