#!/usr/bin/env python3
"""O68: aritmetica exacta de fases normalizadas y pruebas de limite.
Solo Python standard library. No es integracion de Navier-Stokes.
"""
from math import gcd, pi, sqrt, isclose
from fractions import Fraction

checks = 0

def verify(condition, explanation=''):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f'Fallo {checks}: {explanation}')


def bezout(a, b):
    """Devuelve (x,y,d) con x*a+y*b=d=gcd(a,b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s, old_t, old_r


def sync_coordinates(winding1, winding2):
    """Conteos primitivos (q,p), matriz entera de determinante -1.

    Phi = a*theta1 + b*theta2, Psi = p*theta1 - q*theta2.
    """
    q, p = winding1, winding2
    verify(q > 0 and p > 0 and gcd(q, p) == 1)
    a, b, d = bezout(q, p)
    verify(a*q + b*p == d == 1)
    verify(-a*q - b*p == -1)
    return a, b, p, -q


def test_arithmetic():
    pairs = 0
    for q in range(1, 31):
        for p in range(1, 31):
            if gcd(q, p) != 1:
                continue
            a,b,c,d = sync_coordinates(q,p)
            pairs += 1
            verify(a*d - b*c == -1, 'matriz unimodular')
            for L in range(1,9):
                turns_1 = L*q
                turns_2 = L*p
                # La direccion de cierre tiene cero desacople.
                phi_turns = a*turns_1 + b*turns_2
                psi_turns = c*turns_1 + d*turns_2
                verify(phi_turns == L, 'numero entero de ciclos de referencia')
                verify(psi_turns == 0, 'cancelacion exacta en el acoplamiento')
                verify(gcd(turns_1,turns_2) == L, 'multiplo de repeticion')
                # Reconstruccion: U^{-1} entero porque det(U)=-1.
                reconstructed_1 = -d*phi_turns + b*psi_turns
                reconstructed_2 = c*phi_turns - a*psi_turns
                verify(reconstructed_1 == turns_1 and reconstructed_2 == turns_2)
    return pairs


def test_phases_and_radius():
    q,p=3,2
    a,b,c,d=sync_coordinates(q,p)
    omega_common=1.0
    w1,w2=q*omega_common,p*omega_common
    verify(isclose(a*w1 + b*w2,omega_common))
    verify(isclose(c*w1 + d*w2,0,abs_tol=1.e-12))
    # Cambio real en radios con nueva velocidad tangencial que mantiene fases.
    r1,r2=1.0,2.0
    r1_new,r2_new=1.2,1.8
    v1,v2=r1*w1,r2*w2
    v1_new,v2_new=r1_new*w1,r2_new*w2
    verify(isclose(p*v1_new/r1_new-q*v2_new/r2_new,0,abs_tol=1.e-12))
    # Si las velocidades quedan fijas al cambiar radios, se pierde el acoplamiento.
    mismatch_fixed_speed=p*v1/r1_new-q*v2/r2_new
    verify(abs(mismatch_fixed_speed)>1.e-8)
    # Pequenio corrimiento de fase: no existe ya el invariante dinamico exacto.
    detuning=p*3.1-q*2.0
    verify(isclose(detuning,0.2,abs_tol=1.e-12))
    verify(isclose(pi/abs(detuning),5*pi,rel_tol=1.e-12))
    # Una razon irracional no puede ser p/q exactamente para enteros p,q.
    verify(not any(isclose(sqrt(2),p/q,rel_tol=0,abs_tol=1.e-14)
                   for q in range(1,201) for p in range(1,300)))
    # Un ejemplo NO adyacente: diferencia aritmetica unitaria de Bezout.
    a2,b2,c2,d2=sync_coordinates(5,3)
    verify(a2*5+b2*3==1)
    verify(a2*20+b2*12==4)
    verify(c2*20+d2*12==0)
    return mismatch_fixed_speed,detuning


def test_no_minimal_radius_from_lock():
    # Para los mismos winding counts, todas estas parejas geometricas
    # pueden satisfacer algebraicamente el acoplamiento eligiendo v_i=r_i*w_i.
    q,p=3,2
    w1,w2=3.0,2.0
    for scale in [1.e-12,1.e-9,1.e-6,0.001,1.,100.,1.e6]:
        r1,r2=scale,2*scale
        v1,v2=r1*w1,r2*w2
        verify(isclose(p*v1/r1-q*v2/r2,0,abs_tol=1e-12))
    # Mismo acoplamiento admite frecuencias arbitrariamente grandes.
    for multiplier in [1,10,1000,1000000]:
        verify(p*(q*multiplier)==q*(p*multiplier))

if __name__=='__main__':
    pairs=test_arithmetic()
    mismatch,detuning=test_phases_and_radius()
    test_no_minimal_radius_from_lock()
    print(f'PARES_PRIMITIVOS={pairs}')
    print(f'VERIFICACIONES={checks}')
    print('CASO_GIROS=(12,8), COCIENTE_PRIMITIVO=(3,2), MULTIPLO=4')
    print('PHI_VUELTAS=4, PSI_VUELTAS=0')
    print(f'DESACOPLE_POR_RADIOS_SIN_REAJUSTAR_VELOCIDADES={mismatch:.12f}')
    print(f'DERIVA_DE_FASE_EJEMPLO={detuning:.12f} rad/s')
    print('ESTADO=TODOS_LOS_CONTROLES_SUPERADOS')
