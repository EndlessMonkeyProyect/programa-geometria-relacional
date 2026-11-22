#!/usr/bin/env python3
"""Verificacion reproducible HC-02/HC-03 de bloques diadicos hasta 2**22.
   Distingue generadores primos de potencias heredadas. Python3 + numpy.
   No usa ni presupone RH; valores en aritmetica de punto flotante.
"""
import csv, math, json
from pathlib import Path
import numpy as np

MAX_J = 21                         # bloque final 2**21 <= n < 2**22
N = 1 << (MAX_J + 1)
base = Path(__file__).resolve().parent

isprime = np.ones(N, dtype=bool)
isprime[:2] = False
for k in range(2, math.isqrt(N-1)+1):
    if isprime[k]: isprime[k*k:N:k] = False
primes = np.flatnonzero(isprime)
assert int(np.count_nonzero(isprime[:1000])) == 168
new = np.zeros(N, dtype=np.float64)
hered = np.zeros(N, dtype=np.float64)
new[primes] = np.log(primes.astype(np.float64))
prime_power_count = 0
for p in primes:
    p = int(p)
    if p*p >= N: break
    q = p*p
    while q < N:
        hered[q] += math.log(p)
        prime_power_count += 1
        q *= p
assert np.count_nonzero(new*hered) == 0
assert abs(new[1024]) < 1e-12   # 1024 es potencia de 2
assert abs(hered[1024]-math.log(2)) < 1e-12
C0 = 4*math.log(2)+24/math.e    # cota de HC-02 para U(x)
rows = []
max_identity_discrep = 0.0
max_bound_overstep = 0.0
for j in range(1, MAX_J+1):
    L, U = 1<<j, 1<<(j+1)
    length = U-L
    steps = np.arange(1, length+1, dtype=np.float64)
    a = np.cumsum(new[L:U])-steps
    h = np.cumsum(hered[L:U])
    c = np.cumsum((new+hered)[L:U])-steps
    err = float(np.max(np.abs(c-(a+h))))
    max_identity_discrep = max(max_identity_discrep, err)
    b_t = float(np.max(np.abs(c)))
    b_p = float(np.max(np.abs(a)))
    h_end = float(h[-1])
    max_bound_overstep = max(max_bound_overstep, abs(b_t-b_p)-h_end)
    assert abs(b_t-b_p) <= h_end + 1e-7
    assert h_end <= C0*math.sqrt(U) + 1e-7
    rows.append({
        'j':j,'desde':L,'hasta_inclusive':U-1,
        'B_total':round(b_t,8),'B_primos_nuevos':round(b_p,8),
        'H_potencias_heredadas':round(h_end,8),
        'B_total_div_critico':round(b_t/(math.sqrt(L)*(j+1)**2),10),
        'B_primos_div_critico':round(b_p/(math.sqrt(L)*(j+1)**2),10),
        'H_div_raiz':round(h_end/math.sqrt(L),8),
        'posicion_max_total':int(L+np.argmax(np.abs(c))),
        'posicion_max_primos':int(L+np.argmax(np.abs(a))),
    })
with (base/'bloques_hc03_2_22.csv').open('w',newline='',encoding='utf-8') as f:
    wr=csv.DictWriter(f,fieldnames=list(rows[0]))
    wr.writeheader(); wr.writerows(rows)
result = {
 'hasta_exclusivo':N,'ultimo_bloque_inclusivo':[1<<MAX_J,N-1],
 'cantidad_primos':len(primes),'potencias_primas_heredadas':prime_power_count,
 'descomposicion_algebraica': 'C_j(m)=P_j(m)+H_j(m)',
 'cota_universal_HC02_U_x':C0,
 'error_maximo_de_descomposicion_flotante':max_identity_discrep,
 'exceso_maximo_en_desigualdad':max_bound_overstep,
 'ultimo_bloque': rows[-1],
 'algunos_bloques': [r for r in rows if r['j'] in [9,10,11,15,17,19,20,21]],
 'alcance': 'Calculo finito de las funciones clasicas. No prueba una cota uniforme al variar j.'
}
(base/'control.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2,ensure_ascii=False))
