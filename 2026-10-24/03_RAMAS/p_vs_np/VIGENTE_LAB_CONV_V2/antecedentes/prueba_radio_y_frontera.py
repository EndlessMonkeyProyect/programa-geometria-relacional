#!/usr/bin/env python3
"""Falsadores de convergencia por un solo numero y radio de incertidumbre bajo metrica fija."""
import json
from itertools import product
from fractions import Fraction

COLORS=range(3)
B=list(product(COLORS,repeat=3))

def count_valid(edges):
    return sum(all(x[i]!=x[j] for i,j in edges) for x in B)

A=[(0,1)]
D=[(1,2)]
context=[(0,1)]
assert count_valid(A)==count_valid(D)==18
assert count_valid(A+context)==18
assert count_valid(D+context)==12

U=list(product((0,1),repeat=2))
def d(x,y):return sum(a!=b for a,b in zip(x,y))
def radius(S):return Fraction(max((d(x,y) for x in S for y in S),default=0),2)
base=U
initial=[x for x in base if x[0]==0]
repetition=[x for x in initial if x[0]==0]
more=[x for x in initial if x[1]==0]
parity=[x for x in base if (x[0]^x[1])==0]
assert list(map(radius,[base,initial,repetition,more,parity]))==[1,Fraction(1,2),Fraction(1,2),0,1]
print('Interfaces: mismo numero de soluciones (18) y distintas continuaciones (18 contra 12): PASS')
print('Radio diametral: antes 1, pregunta nueva 1/2, repeticion 1/2, pregunta siguiente 0: PASS')
print('Distincion independiente XOR puede no reducir radio diametral: radio 1: PASS')
out={'interfaces':{'casos_base':18,'A_y_contexto':18,'D_y_contexto':12},'radio_hamming':{'antes':1,'al_preguntar_x0':'1/2','al_repetir_x0':'1/2','al_preguntar_y0':0,'al_preguntar_xor0':1}}
with open('/mnt/data/continuacion_convergencia_2026_10_22/radio_frontera_resultados.json','w',encoding='utf8') as f:json.dump(out,f,indent=2,ensure_ascii=False)
