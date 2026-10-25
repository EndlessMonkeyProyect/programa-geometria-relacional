#!/usr/bin/env python3
"""Ensayos finitos independientes. Biblioteca estándar; ningún caso prueba P=NP."""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb, isclose, sqrt
import json

checks = []
def check(name, cond, **evidence):
    assert cond, f"FALLO: {name} {evidence}"
    checks.append(dict(test=name, passed=True, evidence=evidence))

# 1. 2^n recorridos binarios con convergencia por la suma, consulta de suma total.
n=18
ways={0:1}
for i in range(n):
    nxt=Counter()
    for k,m in ways.items():
        nxt[k] += m      # prefijo extendido por 0
        nxt[k+1] += m    # prefijo extendido por 1
    ways=dict(nxt)
check('familias_de_caminos',len(ways)==n+1 and sum(ways.values())==2**n,
      caminos=2**n,nodos_finales=len(ways),profundidad=n)
check('multiplicidad_binomial',all(ways[k]==comb(n,k) for k in range(n+1)),
      distribucion=[ways[k] for k in range(n+1)])
# A mismo largo, dos caminos con misma suma aceptan exactamente las mismas
# continuaciones cuando la unica pregunta futura es la suma total.
for d in range(6):
    strings=[''.join(s) for s in product('01',repeat=d)]
    for p in strings:
        for q in strings:
            if p.count('1') == q.count('1'):
                for ell in range(5):
                    for suffix in product('01',repeat=ell):
                        s=''.join(suffix)
                        assert (p+s).count('1') == (q+s).count('1')
check('congruencia_suma_sufijos',True,profundidades_probadas=6,longitud_sufijo_max=4)
check('nuevo_observable_refina', '01'.count('1')=='10'.count('1') and '01'[0]!='10'[0],
      caminos=['01','10'],suma=1,primera_marca=['0','1'])

# 2. Cubo ideal (un eje), firma plegada, aritmetica exacta.
def folded(x, L=Fraction(1)):
    # Distancia a la reticula 2L*Z en [0,L], exacta en rationals.
    r=x % (2*L)
    return min(r, 2*L-r)/L
p=Fraction(1,4)
images=[2*k+eps*p for k in range(-3,4) for eps in [-1,1]]
check('espejo_orbita',all(folded(x)==p for x in images), muestras=len(images))
check('espejo_otra_orbita',folded(Fraction(3,4))!=folded(p),
      firma_p=str(folded(p)),firma_distinta=str(folded(Fraction(3,4))))

# 3. Igual cardinal y margenes por pares, incompatibilidad ternaria.
universe=set(product((0,1),repeat=3))
even={x for x in universe if sum(x)%2==0}
odd={x for x in universe if sum(x)%2==1}
proj=lambda S,ij: {tuple(x[i] for i in ij) for x in S}
check('igual_cardinal_no_igual_cierre',len(even)==len(odd)==4 and not(even&odd),
      cardinal_par=len(even),cardinal_impar=len(odd),interseccion=0)
check('proyecciones_binarias_indistinguibles',
      all(proj(even,ij)==proj(odd,ij) for ij in combinations(range(3),2)),
      parejas=3)

# 4. E11, traza de ecuaciones XOR.
def count_xor(constr):
    return sum(all(((bits[i]^bits[j])==b) if j is not None
                    else bits[i]==b for i,j,b in constr)
               for bits in product((0,1),repeat=3))
steps=[[],[(0,1,1)],[(0,1,1),(1,2,0)],
       [(0,1,1),(1,2,0),(0,None,0)],
       [(0,1,1),(1,2,0),(0,None,0),(0,2,1)],
       [(0,1,1),(1,2,0),(0,None,0),(0,2,1),(0,2,0)]]
trace=[count_xor(s) for s in steps]
check('traza_E11',trace==[8,4,2,1,1,0],traza=trace)

# 5. No-go: duplicar una misma comparacion cambia el radio gaussiano bruto.
# x real con G=C^T C, beta=1. C=[1] vs C=[1,1] (misma observacion exacta repetida).
beta=1.0
radius1=1/sqrt(beta*1)
radius2=1/sqrt(beta*2)
check('radio_no_invariante_por_duplicacion',
      radius1!=radius2 and isclose(radius2,radius1/sqrt(2)),
      lambda_original=1,lambda_repetida=2,R_original=radius1,R_repetido=radius2,
      nota='Al repetir comparacion cambia el peso G, pero no las clases de equivalencia exacta')

# 6. Test de conservación de normalizador aritmético.
h,N,L=2,3,99
check('transporte_multiplo', L%N==0 and Fraction(h,N)==Fraction(h*(L//N),L),
      antigua=str(Fraction(h,N)),nueva=str(Fraction(h*(L//N),L)),multiplo=L//N)

result={'title':'Convergencia contextual, radios y caminos','date':'2026-10-22',
        'total_tests':len(checks),'tests':checks,
        'scope':'Controles algebraicos y finitos; no resuelven P vs NP ni derivan radios físicos'}
with open('resultados_verificacion.json','w',encoding='utf-8') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'pasadas':len(checks),'caminos':2**n,'nodos_suma':n+1,
                  'traza_xor':trace,'radio_reredundante':[radius1,radius2]},ensure_ascii=False))
