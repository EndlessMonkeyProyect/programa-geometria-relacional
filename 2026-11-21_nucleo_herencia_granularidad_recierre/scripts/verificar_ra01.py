#!/usr/bin/env python3
"""Controles exactos RA–01. Comprueba aritmética finita y un modelo de Hilbert;
las desigualdades universales figuran demostradas en el documento.
No constituye un certificado de cierre funcional para la familia de zeta.
"""
from fractions import Fraction as F
from math import isqrt

def mobius(n):
    if n==1: return 1
    x=n; s=0; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; s+=1
            if x%p==0:return 0
            while x%p==0: x//=p
        p+=1
    if x>1:s+=1
    return (-1)**s

def test_focos():
    counts={}
    for N in (8,16,64,1024):
        active=0
        for n in range(N+1,2*N+1):
            before=sum(mobius(d) for d in range(1,N+1) if n%d==0)
            after=sum(mobius(d) for d in range(1,2*N+1) if n%d==0)
            assert before==-mobius(n) and after==0,(N,n,before,after)
            active += mobius(n)!=0
        counts[N]=active
    assert counts[1024]==621, counts
    return counts

def test_certificado_hilbert_finito():
    # Base ortonormal e1,e2,e3; chi=(1,2,3), W0=span(e1), W1=span(e1,e2)
    chi=[F(1),F(2),F(3)]
    r=[F(0),chi[1],chi[2]]
    g=[F(5),F(1),F(0)]
    u=[F(0),F(1),F(0)]
    dot=sum(x*y for x,y in zip(r,g))
    d=dot*dot/sum(x*x for x in u)
    e0=chi[1]*chi[1]+chi[2]*chi[2]
    e1=chi[2]*chi[2]
    assert d==F(4) and e0==F(13) and e1==F(9)
    assert d==e0-e1

def test_no_necesidad_para_semilla_fija():
    """Modelo exacto infinito: chi = sum_k 2^(-k-1) v_(2k+1).

    W_j=span(v_1,...,v_(2j)); semillas g_j=v_(2j+2) son nuevas
    y no nulas, pero ortogonales a chi. e_j^2=4^(-j)/3 -> 0;
    d_j=0 incluso con ganancia optima positiva en cada octava.
    """
    def chi_coord(k):
        # En las posiciones pares, la coordenada de chi es exactamente cero.
        return F(0) if k % 2 == 0 else F(1, 2**((k + 1)//2))

    for j in range(20):
        e2=F(1,3*4**j)
        siguiente=F(1,3*4**(j+1))
        optima=e2-siguiente
        indice_semilla=2*j+2  # g_j=v_(2j+2), nueva dirección
        producto=chi_coord(indice_semilla)
        norma_semilla=F(1)
        d=producto*producto/norma_semilla
        # Verifica 16 términos exactos de la cola y su resto geométrico.
        cola_parcial=sum((chi_coord(2*k+1)**2 for k in range(j,j+16)), F(0))
        cola_restante=F(1,3*4**(j+16))
        assert cola_parcial + cola_restante == e2
        assert optima==F(1,4**(j+1)) and optima>0
        assert d==0 and e2>0 and siguiente<e2
    # La identidad de la serie geométrica demuestra el límite para todo j.


def test_suma_divergente_modelo():
    # En l2(N>=1), chi=sum 2^{-n} e_n y W_j=span(e1,...,ej).
    # Serie geométrica exacta: e_j^2=(1/3)*4^{-j}; la semilla e_{j+1}
    # gana a_j=4^{-(j+1)}, por tanto a_j/E_j=3/4 en todo j.
    for j in range(0,18):
        E=F(1,3*4**j)
        a=F(1,4**(j+1))
        Enext=F(1,3*4**(j+1))
        assert E-a==Enext
        assert a/E==F(3,4)
    # Con j variable, la suma J*(3/4) diverge; la implicación es exacta

if __name__=='__main__':
    v=test_focos()
    test_certificado_hilbert_finito()
    test_suma_divergente_modelo()
    test_no_necesidad_para_semilla_fija()
    print('RA–01 | recierre Möbius exacto N=8,16,64,1024: OK; activos:',v)
    print('RA–01 | proyección y certificado por semilla racional: OK')
    print('RA–01 | modelo de acumulación exacto en l2: OK')
    print('RA–01 | contraejemplo racional: cierre óptimo con semilla de ganancia nula: OK')
    print('RESULTADO: CONTROLES RA–01 SATISFACTORIOS')
