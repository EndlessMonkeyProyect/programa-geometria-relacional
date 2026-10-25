#!/usr/bin/env python3
"""O58 exact algebraic checks; Python stdlib only; no physical-fluid solver."""
from fractions import Fraction
from math import gcd, isqrt, lcm
import csv, json
from pathlib import Path

HERE=Path(__file__).resolve().parent.parent
OUT=HERE/'resultados'; OUT.mkdir(exist_ok=True)
checks=[]
def check(label,condition,detail=None):
    assert condition, f'FAILED: {label} {detail}'
    checks.append({'test':label,'pass':True,'detail':detail})

def pell_step(N,a):
    return 3*N+4*a, 2*N+3*a

def pell_cube(N,a):
    return N*(4*N*N-3), a*(4*N*N-1)

def witness(N,a,b):
    return {'a':a,'b':b,'N':N,'a2':a*a,'b2':b*b,
            'residuo_bruto': N*N-a*a-b*b,
            'a2_normalizado':str(Fraction(a*a,N*N)),
            'b2_normalizado':str(Fraction(b*b,N*N)),
            'resto_normalizado':str(Fraction(1,N*N))}

# Finite exact census; independently search all squares for N <= 200.
allw=[]
for N in range(2,201):
    for a in range(1,N):
        b2=N*N-a*a-1
        if b2>0:
            b=isqrt(b2)
            if b>=a and b*b==b2:
                allw.append((N,a,b))
                check('suma_cuadrados_'+str(N)+'_'+str(a)+'_'+str(b),a*a+b*b+1==N*N)
check('hay_soluciones_no_simétricas',any(a!=b for N,a,b in allw),len(allw))
check('N_es_impar_en_censo',all(N%2==1 for N,a,b in allw))
check('a_b_son_pares_en_censo',all(a%2==0 and b%2==0 for N,a,b in allw))
check('primitivos_en_censo',all(gcd(gcd(a,b),N)==1 for N,a,b in allw))
check('4_no_admite_dos_cuadrados',not any(N==4 for N,a,b in allw))
check('5_no_admite_dos_cuadrados',not any(N==5 for N,a,b in allw))
check('9_admite_4_8', (9,4,8) in allw)
check('19_admite_6_18', (19,6,18) in allw)

pell=[]
N,a=3,2
for i in range(8):
    check('pell_'+str(i),N*N-2*a*a==1)
    pell.append(witness(N,a,a)|{'indice':i})
    N,a=pell_step(N,a)
check('pell_3_17_99',[row['N'] for row in pell[:3]]==[3,17,99])

nested=[]
N,a=3,2
for i in range(5):
    check('anidada_'+str(i),N*N-2*a*a==1)
    nested.append(witness(N,a,a)|{'paso':i})
    newN,newa=pell_cube(N,a)
    check('anidamiento_divisibilidad_'+str(i),newN%N==0)
    N,a=newN,newa
check('anidada_3_99_3880899',[row['N'] for row in nested[:3]]==[3,99,3880899])

# Explicit distinction: pure homothety conserves normalized ratios,
# but residual grows as square; primitive-one residual implies changed ratios.
for n,a,b in allw:
    for k in (2,3,5):
        check('homotecia_resto_'+str(n)+'_'+str(a)+'_'+str(b)+'_'+str(k),
              (k*n)**2-(k*a)**2-(k*b)**2==k*k)
        check('homotecia_proporciones_'+str(n)+'_'+str(a)+'_'+str(b)+'_'+str(k),
              Fraction(k*a,k*n)==Fraction(a,n) and Fraction(k*b,k*n)==Fraction(b,n))

# Old unit re-expressed on a compatible squared grid, while new unit differs.
for left,right in zip(nested,nested[1:]):
    oldN,newN=left['N'],right['N']; k=newN//oldN
    check('transporte_celda_'+str(oldN)+'_'+str(newN),
          Fraction(1,oldN*oldN)==Fraction(k*k,newN*newN))
    check('nuevo_resto_vs_anterior_'+str(oldN)+'_'+str(newN),
          Fraction(1,oldN*oldN)!=Fraction(1,newN*newN))

# Branches with exact N|M: the scale relation alone does not determine the next state.
links=[]
for N,a,b in allw:
    for M,c,d in allw:
        if M>N and M%N==0:
            factor=M//N
            da=Fraction(c*c,M*M)-Fraction(a*a,N*N)
            db=Fraction(d*d,M*M)-Fraction(b*b,N*N)
            dr=Fraction(1,M*M)-Fraction(1,N*N)
            check('balance_'+str(N)+'_'+str(a)+'_'+str(b)+'__'+str(M)+'_'+str(c)+'_'+str(d), da+db+dr==0)
            links.append({'N':N,'a':a,'b':b,'M':M,'c':c,'d':d,'factor':factor,'delta_a':str(da),'delta_b':str(db),'delta_resto':str(dr)})
check('ramificacion_N3',len({r['M'] for r in links if r['N']==3})>=2)
check('ramal_3_a_9',any(r['N']==3 and r['M']==9 and r['a']==2 and r['b']==2 and r['c']==4 and r['d']==8 for r in links))
check('ramal_3_a_99',any(r['N']==3 and r['M']==99 and r['c']==70 and r['d']==70 for r in links))
with (OUT/'ramas_compatibles_hasta_200.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(links[0]));w.writeheader();w.writerows(links)

# Comparison to the distinct bilateral identity used in O40.
for N in range(2,201):
    check('identidad_bilateral_'+str(N),N*N-(N-1)*(N+1)==1)

with (OUT/'soluciones_hasta_200.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['N','a','b','es_simetrica','resto_normalizado'])
    w.writeheader()
    for N,a,b in allw:
        w.writerow({'N':N,'a':a,'b':b,'es_simetrica':int(a==b),'resto_normalizado':str(Fraction(1,N*N))})
with (OUT/'estela_pell.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(pell[0]))
    w.writeheader(); w.writerows(pell)
with (OUT/'estela_anidada.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(nested[0]))
    w.writeheader();w.writerows(nested)
record={'name':'O58 verificacion aritmetica exacta','status':'PASS','number_of_checks':len(checks),
        'census_Nmax':200,'count_unordered_positive_pairs':len(allw),'count_divisibility_edges':len(links),
        'first_20_unordered_pairs':allw[:20],
        'pell_first_5':pell[:5], 'nested_first_3':nested[:3],
        'test_results':checks}
(OUT/'verificacion.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
print('PASS:',len(checks),'comprobaciones; ',len(allw),'pares positivos no ordenados para 2<=N<=200')
print('Pell N:',[e['N'] for e in pell[:5]])
print('Anidada N:',[e['N'] for e in nested[:3]])
print('Primeras soluciones:',allw[:16])
