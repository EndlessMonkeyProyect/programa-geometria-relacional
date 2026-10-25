#!/usr/bin/env python3
"""Ensayo exacto de cierre común de cuatro reflexiones tetraédricas.

Usa sólo Python stdlib y fracciones racionales. Tres contratos separados:
  A. Cuatro caras de un tetraedro BASE fijo (operaciones independientes).
  B. Caras recalculadas tras cada reflexión (espejo móvil).
  C. Coincidencia de posiciones 3D vs proyección de observador.
No postula primalidad, nueva raíz aritmética ni cierre ontológico universal.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from collections import Counter
from math import sqrt
from pathlib import Path
import json, csv

OUT = Path(__file__).resolve().parent
V = [tuple(Q(x) for x in xyz) for xyz in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]

def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def scaled(k,x): return tuple(k*y for y in x)
def dot(a,b): return sum((x*y for x,y in zip(a,b)), Q(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sqdist(a,b): return dot(minus(a,b),minus(a,b))
def centroid(pts):return scaled(Q(1,len(pts)),tuple(sum(p[i] for p in pts) for i in range(3)))
def reflect(p,face):
    a,b,c=face
    n=cross(minus(b,a),minus(c,a))
    return minus(p,scaled(Q(2)*dot(minus(p,a),n)/dot(n,n),n))
def js(x):
    if isinstance(x,Q): return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
    if isinstance(x,(tuple,list)):return [js(y) for y in x]
    if isinstance(x,dict):return {k:js(y) for k,y in x.items()}
    return x

def next_face(t,i):
    new=list(t);new[i]=reflect(t[i], [t[j] for j in range(4) if j!=i]);return tuple(new)

# Contract A: do not recompute reference face from the current shell.
W=[reflect(V[i],[V[j] for j in range(4) if j!=i]) for i in range(4)]
assert all(W[i]==scaled(Q(-5,3),V[i]) for i in range(4))
assert sum((p[0] for p in V),Q(0))==0
assert all(dot(V[i],V[j])==Q(-1) for i,j in combinations(range(4),2))
assert len(set(W))==4
rows=[]
for mask in range(16):
    indices=[i for i in range(4) if mask & (1<<i)]
    pts=tuple(W[i] if i in indices else V[i] for i in range(4))
    edge_sq=sorted(set(sqdist(pts[i],pts[j]) for i,j in combinations(range(4),2)))
    cm=centroid(pts)
    k=len(indices)
    # Complete 4-vertex active set, not all underlying/retained original vertices
    row={'mascara':format(mask,'04b'),'caras_reflejadas':[i+1 for i in indices],
         'k':k,'regular':len(edge_sq)==1,'d2_distintas':js(edge_sq),
         'centro_xyz':js(cm),'centro_norma2':js(dot(cm,cm)),
         'mantiene_foco_original':cm==(Q(0),Q(0),Q(0)),
         'puntos_xyz':js(pts)}
    rows.append(row)
    assert dot(cm,cm)==Q(4,9)*k*(4-k)
    assert row['regular']==(k in (0,1,4))
    assert row['mantiene_foco_original']==(k in (0,4))

# Closure of normals: rank 3, unique positive dependence up to scale.
# Face outward normals are -v_i / sqrt(3). We use unnormalized -v_i.
N=[scaled(-1,p) for p in V]
assert tuple(sum(n[i] for n in N) for i in range(3))==(Q(0),)*3
triple=dot(N[0],cross(N[1],N[2]));assert triple!=0
# Solve sum a_i n_i=0 => a0=a1=a2=a3 for 4-vector family,
# proved also by linear independence of n0,n1,n2 and n3=-(n0+n1+n2).
assert N[3]==scaled(-1,tuple(sum(N[i][j] for i in range(3)) for j in range(3)))

# 24 orders of face snapshot updates always return the same shell if
# individual targets are computed once from the same base.
fixed_order_final=set()
for order in permutations(range(4)):
    shell=list(V)
    for i in order:shell[i]=W[i]
    fixed_order_final.add(tuple(shell))
assert len(fixed_order_final)==1

# Contract B: now recompute each mirror face as the active shell changes.
mobile_01=next_face(next_face(tuple(V),0),1)
mobile_10=next_face(next_face(tuple(V),1),0)
assert mobile_01!=mobile_10
# Both faces are congruent but the 2-step paths differ.
assert all(set(sqdist(t[i],t[j]) for i,j in combinations(range(4),2))=={Q(8)} for t in (mobile_01,mobile_10))

# Contract C: two distinct 3D images may coincide under one observation.
# Projection along (0,1,1): P(x,y,z)=(x,y-z); e.g. images 1 and 2.
P=lambda p:(p[0],p[1]-p[2])
projected=[P(p) for p in W]
assert W[0]!=W[1] and projected[0]==projected[1]
assert len(set(projected))<len(set(W))

counts={str(k):{'configuraciones':sum(r['k']==k for r in rows),
                'regulares':sum(r['k']==k and r['regular'] for r in rows),
                'foco_original':sum(r['k']==k and r['mantiene_foco_original'] for r in rows)}
         for k in range(5)}
results={
 'contrato':'base regular en R^3, cara reflejada respecto del tetra original salvo cuando se declara espejo móvil',
 'referencias_base':js(V),'imagenes_caras':js(W),
 'normales_exteriores_sin_normalizar':js(N),
 'producto_pares_normales_unitarias':'-1/3',
 'rango_normales':3,'equilibrio_con_pesos_positivos':'a1=a2=a3=a4, únicamente, salvo escala',
 'distancia_cuadrada_original':'8','distancia_cuadrada_capa_completa':'200/9',
 'factor_radial_y_lados_capa_completa':'5/3',
 'estados_de_activacion':rows,'conteos_por_numero_de_caras':counts,
 'orden_fijo':{'permutaciones':24,'resultados_finales_distintos':len(fixed_order_final),'orden_independiente':True},
 'espejo_movil':{'orden_1_luego_2':js(mobile_01),'orden_2_luego_1':js(mobile_10),'conmutan':False},
 'observacion':{'imagenes_tridimensionales_1_y_2_iguales':False,
                'proyeccion_1_y_2_iguales':True,
                'proyeccion_elegida':'P(x,y,z)=(x,y-z), mirada a lo largo de (0,1,1)'},
 'interpretacion':'El cierre global es una condición geométrica declarada, no raíz prima ni raíz relacional acreditada por coincidencia puntual.'
}
with (OUT/'resultados_exactos.json').open('w',encoding='utf-8') as f:json.dump(results,f,indent=2,ensure_ascii=False)
with (OUT/'16_estados.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['mascara','k','caras_reflejadas','regular','mantiene_foco_original','centro_norma2','d2_distintas'])
    writer.writeheader()
    for r in rows:
        data={k:r[k] for k in writer.fieldnames};data['caras_reflejadas']=';'.join(map(str,data['caras_reflejadas']));data['d2_distintas']=';'.join(data['d2_distintas']);writer.writerow(data)
print('PASS: 16/16 configuraciones verificadas con fracciones exactas')
for k,c in counts.items():print('k=',k,':',c)
print('PASS: 24 órdenes con foco fijo producen exactamente la misma capa global')
print('PASS: los dos órdenes con foco móvil difieren')
print('PASS: coincidencia en proyección no implica coincidencia espacial')
