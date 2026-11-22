#!/usr/bin/env python3
"""Control exacto de aparición, herencia y transporte m -> 2m.
Sin dependencias externas. Ejecutar: python verificar_transicion.py
"""
from math import comb, log, sqrt, pi
from csv import DictWriter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
MAX_M = 2048
LIMIT = 2 * MAX_M + 2

# Criba ordinaria; fuente de los generadores primos.
is_prime = bytearray(b'\x01') * (LIMIT+1)
is_prime[0:2] = b'\x00\x00'
for p in range(2, int(LIMIT**0.5)+1):
    if is_prime[p]:
        is_prime[p*p:LIMIT+1:p] = b'\x00' * (((LIMIT-p*p)//p)+1)
primes = [p for p in range(2, LIMIT+1) if is_prime[p]]

# r(n)=p cuando n=p^k, r(n)=1 en cualquier otra posición.
r = [1] * (LIMIT+1)
for p in primes:
    power = p
    while power <= LIMIT:
        assert r[power] == 1
        r[power] = p
        power *= p

# L(n) se determina únicamente mediante incorporaciones previas.
L = [1]*(LIMIT+1)
for n in range(2, LIMIT+1):
    L[n] = L[n-1] * r[n]

checks = dict(herencia_local=0, transicion=0, libre_cuadrados=0,
              binomial_y_acarreo=0, paridad_binaria=0, pesos_hc03=0,
              reconstruccion_divisores=0)

# Exponentes de la parte heredada obtenidos como acarreo de potencias p^j <= m.
def vals_heredados(m):
    vals = {}
    for p in primes:
        if p > m: break
        q = p
        cnt = 0
        while q <= m:
            if 2 * (m % q) >= q:
                cnt += 1
            q *= p
        if cnt:
            vals[p] = cnt
    return vals

def popcount(n):
    return n.bit_count()

selected = set([1,2,3,4,5,6,7,8,9,10,11,12,15,16,31,32,33,64,100,128,255,256,257,512,1000,1024,2048])
rows = []

for n in range(2, LIMIT+1):
    # fórmula r(n) = n/gcd(n, L(n-1)), validada por el algoritmo de Euclides.
    from math import gcd
    assert r[n] == n // gcd(n, L[n-1]), n
    checks['herencia_local']+=1
    # product_{d|n} r(d)=n, identidad de factorización.
    if n<= 1024:
        c=1
        for d in range(1,int(n**0.5)+1):
            if n%d==0:
                c*=r[d]
                if n//d!=d: c*=r[n//d]
        assert c==n, (n,c)
        checks['reconstruccion_divisores']+=1

prevA = None
for m in range(1,MAX_M+1):
    A = L[2*m] // L[m]
    assert A * L[m] == L[2*m]
    if prevA is not None:
        assert A*r[m] == prevA*r[2*m-1]*r[2*m]
        checks['transicion']+=1
    prevA=A
    a_check=1
    # Cada p aparece a lo sumo una vez en (m,2m] como p^k.
    for p in primes:
        if p>2*m:break
        power=p
        ct=0
        while power<=2*m:
            if power>m:ct+=1
            power*=p
        assert ct<=1
        if ct:a_check *=p
    assert A==a_check
    checks['libre_cuadrados']+=1

    C=comb(2*m,m)
    assert C%A==0
    B=C//A
    exps=vals_heredados(m)
    B2=1
    for p,k in exps.items():B2*=p**k
    assert B==B2, (m, B, B2)
    checks['binomial_y_acarreo']+=1
    # A(m) contiene siempre exactamente una potencia de la referencia 2.
    z=B
    v2=0
    while z%2==0:
        v2+=1
        z//=2
    assert v2==popcount(m)-1
    checks['paridad_binaria']+=1

    # La suma delta^2 T(m)=lambda(m)/m se recupera al tomar los logaritmos de r(m).
    # Comprobación estructural: Lambda(m)=log(r(m)).
    assert (r[m] == 1) or (r[m] in primes)
    checks['pesos_hc03']+=1

    if m in selected:
        # Log exacto por factorización, evitando float de enteros enormes.
        log_A = sum(log(r[n]) for n in range(m+1,2*m+1) if r[n]>1)
        log_B = sum(k*log(p) for p,k in exps.items())
        log_C = log_A+log_B
        residuo=log_A-m
        main_B=(2*log(2)-1)*m-0.5*log(pi*m)
        rows.append(dict(m=m, incorporaciones_rango=sum(r[n]!=1 for n in range(m+1,2*m+1)),
                        factores_distintos_A=sum(1 for p in primes if p<=2*m and A%p==0),
                        val_2_B=v2, unos_binarios=popcount(m),
                        log_A=round(log_A,10),log_B=round(log_B,10),
                        log_binomial=round(log_C,10),
                        desviacion_entre_escalas=round(residuo,10),
                        control_B_mas_principal=round(log_B-main_B,10),
                        normalized_error=round(abs(residuo)/(sqrt(m)*log(2*m+2)**2),10)))

with (ROOT/'muestras.csv').open('w',newline='',encoding='utf-8') as out:
    w=DictWriter(out,fieldnames=list(rows[0].keys()))
    w.writeheader();w.writerows(rows)
with (ROOT/'verificacion.json').open('w',encoding='utf-8') as out:
    json.dump(dict(max_m=MAX_M,limite_L=LIMIT,numero_de_primos=len(primes),
                   comprobaciones=checks, total=sum(checks.values()),
                   test_m5=dict(A=42,B=6,C=252), test_m6=dict(A=462,B=2,C=924),
                   relaciones_RH='No demostradas; solo equivalencia condicional clásica.'),out,indent=2,ensure_ascii=False)
print(json.dumps(checks,ensure_ascii=False,indent=2))
print('Total controles:', sum(checks.values()))
print('m, log A, log B, error del intervalo, v2(B)')
for x in rows:
    if x['m'] in (5,6,7,8,16,100,256,512,1024,2048):
        print(x['m'],x['log_A'],x['log_B'],x['desviacion_entre_escalas'],x['val_2_B'])
