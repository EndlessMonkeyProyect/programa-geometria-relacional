#!/usr/bin/env python3
"""Prueba exacta: momentos desde coeficientes y conteos restringidos; rango de Hankel."""
from itertools import product
import sympy as sp
x,t = sp.symbols('x t')

def moments_newton_monic(coeffs,nmax):
    """Momentos de raíces vía identidades de Newton; no calcula ninguna raíz."""
    d=len(coeffs)-1
    assert coeffs[0]==1
    out=[sp.Integer(d)]
    # coefficients coeffs[j]=a_j for x^(d-j)
    for k in range(1,nmax+1):
        if k<=d:
            val=-sum(coeffs[j]*out[k-j] for j in range(1,k)) - k*coeffs[k]
        else:
            val=-sum(coeffs[j]*out[k-j] for j in range(1,d+1))
        out.append(sp.simplify(val))
    return out

print('1. MOMENTOS DE RAICES: SOLO COEFICIENTES Y STURM')
for name, pol, localcount, m4 in [
    ('P1',sp.Poly(x**4-10*x**2+9,x),2,164),
    ('P2',sp.Poly(x**4-10*x**2+16,x),0,136),
]:
    M=moments_newton_monic(pol.all_coeffs(),4)
    # Sturm exacto: solo signos en extremos racionales, sin encontrar raíces
    n_axis=sp.polys.polytools.count_roots(pol,-sp.Rational(5,4),sp.Rational(5,4))
    assert M[1]==0 and M[2]==20 and M[4]==m4 and n_axis==localcount
    print(name,{'M0..4': list(map(str,M)), 'cuenta_intervalo': n_axis})


def FA(z):
    a,b,c=z
    return ((a+b+c)%2==0) and bool(a or b or c)
def FB(z):
    a,b,c=z
    return (a==0) and ((b==0) or (c==1))

def restricted(F, index_set, n):
    # Oráculo de conteo simulado por enumeración para auditar el ejemplo pequeño
    return sum(bool(F(z)) and all(z[i] for i in index_set) for z in product((0,1),repeat=n))

def test_sat(F,expected):
    n=3
    N=restricted(F,[],n)
    Ai=[restricted(F,[i],n) for i in range(n)]
    Bij={(i,j):restricted(F,[i,j],n) for i in range(n) for j in range(i+1,n)}
    S1=sum(Ai)
    S2=sum(Ai)+2*sum(Bij.values())
    axis=sp.Rational(S1,N)
    scatter=sp.Rational(S2,N)-axis**2
    Z=sp.expand(sum(t**sum(z) for z in product((0,1),repeat=n) if F(z)))
    mom=[sp.diff(Z,t,k).subs(t,1) for k in range(1)] # not used below
    power_moments=[sum(sum(z)**k for z in product((0,1),repeat=n) if F(z)) for k in range(5)]
    H3=sp.Matrix([[power_moments[i+j] for j in range(3)] for i in range(3)])
    assert (N,S1,S2)==expected
    assert sp.simplify(Z.subs(t,1))==N
    print({'N':N,'cotas_primera':Ai,'cotas_doble':Bij,'S1':S1,'S2':S2,'eje':axis,'dispersion':scatter,'Z(t)':str(Z),'momentos_0_a_4':power_moments,'H3_det':H3.det(),'H3_rango':H3.rank()})
    return H3.rank()

print('2. CONTEOS RESTRINGIDOS Y RANGO DE HANKEL')
rA=test_sat(FA,(3,6,12))
rB=test_sat(FB,(3,3,5))
assert (rA,rB)==(1,3)
print('TODAS LAS PRUEBAS EXACTAS: OK')
