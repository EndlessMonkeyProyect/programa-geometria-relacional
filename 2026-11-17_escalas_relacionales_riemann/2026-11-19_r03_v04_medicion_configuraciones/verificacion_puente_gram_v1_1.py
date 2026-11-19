#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Medición de Gram R–RH–01 ↔ R–01/R–02 ↔ R–03.

Dos rutas independientes para d_2: (i) matriz y vector obtenidos
INTEGRAMENTE por cuadratura analítica de cada tramo [n,n+1] hasta N;
(ii) matriz y vector exactos con constantes clásicas, solo como comparación.

La rutina reporta un encierro matemático de la distancia real mediante
la cola acotada de un candidato explícito. No demuestra RH.
Dependencia: mpmath. Ejecución: python verificacion_puente_gram_v1_1.py
"""
import argparse
import mpmath as mp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--N', type=int, default=3000, help='Truncamiento y∈(0,N), entero N≥2')
    parser.add_argument('--dps', type=int, default=45, help='Dígitos decimales de mpmath')
    args = parser.parse_args()
    if args.N < 2 or args.dps < 20:
        parser.error('Se requiere N≥2 y dps≥20')
    N = args.N
    mp.mp.dps = args.dps
    den = [mp.mpf(1), mp.mpf(1)/2]
    bounds = [mp.mpf(1), mp.mpf(1)/2]

    def count(j,n):
        # A_empty(n)=n; A_{2}(n)=ceil(n/2), para n entero.
        return mp.mpf(n if j == 0 else (n + 1)//2)

    def gram_trunc(j,k):
        # (0,1): E_j(y)=-delta_j*y.
        t = den[j]*den[k]
        for n in range(1,N):
            a,b = count(j,n),count(k,n)
            # E_j(y)=a-delta_j*y en [n,n+1).
            # Integración exacta del integrando racional por tramos.
            t += (a*b/(n*(n+1))
                  - (a*den[k]+b*den[j])*mp.log1p(mp.mpf(1)/n)
                  + den[j]*den[k])
        return t

    def b_trunc(j):
        # b_j=-∫_1^N E_j(y)/y² dy; la cola no se inyecta desde fórmula exacta.
        return mp.fsum(-count(j,n)/(n*(n+1))
                       + den[j]*mp.log1p(mp.mpf(1)/n)
                       for n in range(1,N))

    G = mp.matrix([[gram_trunc(i,j) for j in range(2)] for i in range(2)])
    b = mp.matrix([b_trunc(j) for j in range(2)])
    assert G[0,0]>0 and mp.det(G)>0
    c = mp.lu_solve(G,b)
    chi_norm_trunc_sq = 1-mp.mpf(1)/N
    dN_sq = chi_norm_trunc_sq - (b.T*c)[0]
    assert dN_sq>0
    # Por ser mínimo sobre 0<y<N, dN² <= d∞².
    # Para y>N, χ(1/y)=1; |E_empty(y)|<=1, |E_{2}(y)|<=1/2.
    # Con los coeficientes c_N, el residuo tiene módulo <= 1+Σ|c_j|C_j.
    tail_upper_sq = (1+sum(abs(c[j])*bounds[j] for j in range(2)))**2 / N
    low = mp.sqrt(dN_sq)
    high = mp.sqrt(dN_sq+tail_upper_sq)

    # Control independiente de exactitud: fórmulas cerradas NO empleadas arriba.
    A = mp.log(2*mp.pi)-mp.euler
    B = A/2+(mp.log(mp.pi)-mp.euler)/4
    G_exact = mp.matrix([[A,A-B],[A-B,mp.log(2)/2]])
    b_exact = mp.matrix([1-mp.euler,(1-mp.euler-mp.log(2))/2])
    d_exact = mp.sqrt(1-(b_exact.T*mp.lu_solve(G_exact,b_exact))[0])
    assert low <= d_exact <= high, 'La referencia exacta no cae en el intervalo de cola'
    for i in range(2):
        assert abs(b_exact[i]-b[i]) <= bounds[i]/N + mp.mpf('1e-34')
        for j in range(2):
            assert abs(G_exact[i,j]-G[i,j]) <= bounds[i]*bounds[j]/N + mp.mpf('1e-34')

    f = lambda z, digits=20: mp.nstr(z,digits)
    print('Puente de Gram: dos referencias {∅,{2}}, h_∅=f1, h_{2}=f1−f2')
    print(f'N={N}, mpmath dps={mp.mp.dps}, sin azar')
    print('Matriz desde integrales truncadas (sin usar constantes exactas):')
    for i in range(2):
        print('  ',*[f(G[i,j]) for j in range(2)])
    print('Vector b desde integrales truncadas:',*[f(b[j]) for j in range(2)])
    print('Coeficientes óptimos truncados:',*[f(c[j]) for j in range(2)])
    print('Distancia óptima TRUNCADA:',f(mp.sqrt(dN_sq)))
    print('Intervalo por cota analítica de cola [',f(low),',',f(high),'] (redondeo no certificado)')
    print('Distancia por constantes cerradas (control independiente):',f(d_exact))
    print('Diferencia entre global exacta y truncada:',f(d_exact-low))
    print('Cotas de cola (Gram y b): verificadas')
    print('OK: matrices, proyección por integral truncada y encierro. RH abierta.')

if __name__ == '__main__':
    main()
