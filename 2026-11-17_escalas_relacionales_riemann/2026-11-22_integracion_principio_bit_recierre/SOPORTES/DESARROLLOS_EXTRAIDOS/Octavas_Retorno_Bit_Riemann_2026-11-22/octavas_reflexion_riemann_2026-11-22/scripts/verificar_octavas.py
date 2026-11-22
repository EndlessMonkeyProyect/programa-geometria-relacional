#!/usr/bin/env python3
"""Controles finitos exactos: reflexion, retornos diadicos, Mersenne y acarreos.
No constituye una prueba de una estimacion asintotica ni de RH.
"""
from collections import defaultdict
from math import gcd


def sieve_primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * ((n-i*i)//i + 1)
    return [i for i in range(n+1) if sieve[i]]


def pp_list(n):
    out=[]
    for p in sieve_primes(n):
        q=p
        while q <=n:
            out.append((q,p))
            q*=p
    return sorted(out)


def c(q, m):
    return 1 if (m % q)*2 >= q else 0


def R(q,r):
    return q-1-r


def v_p_factorial(n, p):
    total=0
    while n:
        n//=p
        total+=n
    return total


def v_p_binom(m, p):
    return v_p_factorial(2*m,p)-2*v_p_factorial(m,p)


def order_2(q):
    if q==1: return 1
    assert q%2==1
    x=2%q
    k=1
    while x != 1:
        x=2*x%q
        k+=1
    return k


def run():
    counts=defaultdict(int)
    for q in range(2,301):
        for r in range(q):
            rr=R(q,r)
            assert R(q,rr)==r
            assert c(q,r)+c(q,rr)==1-int(q%2==1 and 2*r==q-1)
            assert (R(q,(2*r)%q)-((2*R(q,r))%q))%q==1%q
            counts['reflexion_y_defecto']+=1

    for q in range(3,302,2):
        ordq=order_2(q)
        for k in range(1,51):
            mk=(1<<k)-1
            assert c(q,mk)==c(q,(1<<(k+ordq))-1)
            counts['retorno_mersenne_periodico']+=1
        for r in range(q):
            d=gcd(r,q)
            ord_orbit=order_2(q//d)
            assert (r*pow(2,ord_orbit,q))%q==r
            counts['orden_orbita_impar']+=1

    for d in range(2,15):
        q=(1<<d)-1
        for k in range(1,65):
            assert c(q,(1<<k)-1)==0
            counts['mersenne_modulo_silencioso']+=1

    for k in range(1,70):
        mk=(1<<k)-1
        for a in range(1,70):
            assert c(1<<a,mk)==int(k>=a)
            counts['bit_potencia_dos_mersenne']+=1
        assert sum(c(1<<a,mk) for a in range(1,k)) == k-1
        counts['v2_B_mersenne']+=1

    qps=pp_list(5000)
    for m in range(1,2501):
        exp_m=defaultdict(int)
        exp_2m=defaultdict(int)
        inherited=defaultdict(int)
        born=defaultdict(int)
        for q,p in qps:
            if q<=m:
                exp_m[p]+=c(q,m)
                exp_2m[p]+=c(q,2*m)
                if p%2:
                    inherited[p]+=c(q,2*m)-c(q,m)
            elif q<=2*m:
                exp_2m[p]+=c(q,2*m)
                if p%2:
                    born[p]+=c(q,2*m)
            else:
                break
        assert exp_m[2] == exp_2m[2]
        counts['herencia_potencias_de_dos']+=1
        for p in sieve_primes(2*m):
            assert exp_2m[p]-exp_m[p]==inherited[p]+born[p]
            counts['transicion_por_primo']+=1
            val=v_p_binom(m,p)
            a_exp=int(any(q>m and q<=2*m and p0==p for q,p0 in qps))
            assert val-a_exp==exp_m[p]
            counts['factorizacion_Legendre']+=1

    assert [c(7,2**j) for j in range(0,3)]==[0,0,1]
    assert [c(7,3*(2**j)) for j in range(0,3)]==[0,1,1]
    assert [c(7,(1<<k)-1) for k in range(1,61)]==[0]*60
    assert [c(3,(1<<k)-1) for k in range(1,61)]==[0]*60
    assert [c(9,(1<<k)-1) for k in range(1,7)]==[0,0,1,1,0,0]
    counts['testigos_orbitas']+=5

    print('VERIFICACION FINITA EXACTA')
    for key,val in sorted(counts.items()): print(f'{key}: {val}')
    print('TOTAL:',sum(counts.values()))
    print('ESTADO: TODOS LOS CONTROLES PASARON')
    print('ALCANCE: identidades finitas; RH y cotas globales no evaluadas')

if __name__ == '__main__':
    run()
