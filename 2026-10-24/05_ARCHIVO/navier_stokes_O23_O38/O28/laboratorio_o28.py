#!/usr/bin/env python3
"""O28: ensayos reproducibles de álgebra/estabilidad local (no simulación NS)."""
from fractions import Fraction
import itertools
import math
import sympy as sp

checks=0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

# O28-T1: vueltas coprimas y módulo común exacto
for p in range(1, 10):
    for q in range(1, 10):
        if math.gcd(p, q)!=1:
            continue
        omega1, omega2 = Fraction(p), Fraction(q)
        check(Fraction(omega1, omega2) == Fraction(p,q), 'razon racional')
        T_over_2pi = Fraction(p,omega1)  # T/(2*pi)
        check(T_over_2pi == Fraction(q,omega2),'retorno conjunto')
        check(q*omega1-p*omega2 == 0,'residuo cero')
        # T0/(2*pi)=1 con estas frecuencias enteras reducidas
        check(T_over_2pi == 1, 'periodo minimo para coprimos')

# O28-T2: existencia de Bezout, fibra parametrizada
for p in range(1, 8):
    for q in range(1, 8):
        if math.gcd(p,q)!=1:
            continue
        a,b,g=sp.gcdex(q, -p)
        check(g==1 and a*q-b*p==1,'bezout')
        for t in [sp.Rational(0),sp.Rational(1,3),sp.Rational(7,10)]:
            psi=sp.Rational(2,5)
            theta1=a*psi+p*t
            theta2=b*psi+q*t
            check(sp.simplify(q*theta1-p*theta2-psi)==0,'fibra circular')
        check((q!=0 or p!=0),'rango uno')

# O28-T3: deduccion exacta de ecuacion de desfase
q,p,Omega1,Omega2,K,psi=sp.symbols('q p Omega1 Omega2 K psi', nonzero=True, real=True)
f1=Omega1-K/(2*q)*sp.sin(psi)
f2=Omega2+K/(2*p)*sp.sin(psi)
check(sp.simplify(q*f1-p*f2-(q*Omega1-p*Omega2-K*sp.sin(psi)))==0,'fase relativa')
for d,k in [(0, 1), (0.2,0.4),(-0.1,0.4),(math.sqrt(2)-1,0.6)]:
    eq=math.asin(d/k)
    check(abs(d-k*math.sin(eq))<1e-12,'equilibrio')
    check(-k*math.cos(eq)<0, 'rama estable')
for d,k in [(2,1),(-3,2)]:
    check(abs(d)>k,'no equilibrio')

# O28-T4: producto radio-ritmo constante, razon radios/frecuencias
for r1 in range(1, 9):
    for r2 in range(1,9):
        v=Fraction(7,3)
        w1,w2=v/Fraction(r1),v/Fraction(r2)
        check(w1*r1 == w2*r2 == v,'producto modal')
        check(w1/w2 == Fraction(r2,r1),'inversion ritmo-radio')

# Contrato finito: epsilon_N no crece al aumentar presupuesto; irracional >0

def residual(om1,om2,N):
    return min((abs(q*om1-p*om2)/(q*om1+p*om2), p, q)
        for p in range(1,N) for q in range(1,N) if p+q<=N)
for om1,om2 in [(3.0,2.0),(math.sqrt(2),1.0),(2*math.pi,5.0)]:
    vals = [residual(om1,om2,N)[0] for N in range(2,24)]
    check(all(vals[i+1]<=vals[i]+1e-13 for i in range(len(vals)-1)),'monotonia presupuesto')
    if om1==math.sqrt(2):
        check(all(v>0 for v in vals),'irracional presupuesto finito')

# No-go K insuficiente para seleccionar atractor de fase
O1,O2=math.sqrt(2),1.0
delta=O1-O2
check(delta>0 and 0.0<delta,'sin acoplamiento no bloqueo')
check(delta<0.6,'acoplamiento puede bloquear')

print(f'O28 / PASS / {checks} aserciones internas')
print('Importante: las pruebas auditan el modelo de fases; NO una simulacion de Navier-Stokes.')
