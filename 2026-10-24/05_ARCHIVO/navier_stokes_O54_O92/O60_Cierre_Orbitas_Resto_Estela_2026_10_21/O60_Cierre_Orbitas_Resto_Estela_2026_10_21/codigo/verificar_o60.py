#!/usr/bin/env python3
"""O60: laboratorio finito exacto de ocupacion D4, cierre cuadratico y refinamiento.
Sin dependencias externas. Autoria del programa: Le Matt Ansatz Di Ego.
"""
from math import isqrt
from collections import Counter
from functools import lru_cache
from pathlib import Path
import csv, json

OUT=Path(__file__).resolve().parents[1]/'resultados'
OUT.mkdir(exist_ok=True)

def symmetries(p):
    x,y=p
    return {(x,y),(x,-y),(-x,y),(-x,-y),(y,x),(y,-x),(-y,x),(-y,-x)}

@lru_cache(maxsize=None)
def orbits(N):
    assert N%2==1 and N>=3
    h=(N-1)//2
    grid={(i,j) for i in range(-h,h+1) for j in range(-h,h+1)}
    ans=[]
    while grid:
        p=min(grid)
        orb=symmetries(p)
        assert orb <= grid
        grid-=orb
        ans.append(orb)
    return sorted(ans,key=lambda o:(-len(o),-max(x*x+y*y for x,y in o),min(o)))

def choose_cells(N,target):
    """D4-invariant subset of prescribed cardinality divisible by 4, center excluded."""
    assert target%4==0 and 0<=target<=N*N-1
    dic={4:[],8:[]}
    for orbit in orbits(N):
        if len(orbit)==1:continue
        dic[len(orbit)].append(orbit)
    for n8 in range(min(len(dic[8]),target//8),-1,-1):
        rem=target-8*n8
        if rem>=0 and rem%4==0 and rem//4<=len(dic[4]):
            chosen=dic[8][:n8]+dic[4][:rem//4]
            pts=set().union(*chosen) if chosen else set()
            assert len(pts)==target
            assert (0,0) not in pts
            assert all(symmetries(p)<=pts for p in pts)
            return pts
    raise AssertionError('No subset found; orbit count theorem violation')

def coloring(N,a,b):
    assert a>0 and b>0 and N*N-a*a-b*b==1
    assert N%2 and a%2==b%2==0
    A=choose_cells(N,a*a)
    h=(N-1)//2
    grid={(i,j) for i in range(-h,h+1) for j in range(-h,h+1)}
    B=grid-A-{(0,0)}
    assert len(B)==b*b
    return {p:('A' if p in A else 'B' if p in B else '.') for p in grid}

def counts(grid):return Counter(grid.values())

def orbit_invariant(grid):return all(grid[p]==grid[q] for p in grid for q in symmetries(p))

def refine(parent,N,a,b,Nnew,anew,bnew):
    assert Nnew%N==0
    k=Nnew//N
    assert k%2==1
    assert N*N==a*a+b*b+1 and Nnew*Nnew==anew*anew+bnew*bnew+1
    dA=anew*anew-k*k*a*a
    dB=bnew*bnew-k*k*b*b
    assert dA+dB==k*k-1
    if min(dA,dB)<0:
        return {'admisible':False,'k':k,'deltaA':dA,'deltaB':dB}
    fillers=choose_cells(k,dA)
    grid={}
    h=(k-1)//2
    for (i,j),v in parent.items():
        for di in range(-h,h+1):
            for dj in range(-h,h+1):
                pos=(k*i+di,k*j+dj)
                if v!='.':grid[pos]=v
                elif (di,dj)==(0,0):grid[pos]='.'
                else:grid[pos]='A' if (di,dj) in fillers else 'B'
    assert len(grid)==Nnew*Nnew and counts(grid)==Counter({'A':anew*anew,'B':bnew*bnew,'.':1})
    assert orbit_invariant(grid)
    return {'admisible':True,'k':k,'deltaA':dA,'deltaB':dB,'grid':grid}

def orbit_cube_1d(p,N):
    """Discretized opposing mirrors at 0 and 1, image residues modulo 2N."""
    return {p%(2*N),(-p)%(2*N)}

def run():
    checks=0
    for N in [3,5,9,17,51,99]:
        obs=orbits(N)
        c=Counter(map(len,obs))
        assert c[1]==1 and c[4]==N-1 and c[8]==(N-1)*(N-3)//8
        assert sum(map(len,obs))==N*N
        checks+=4
        targets=list(range(0,N*N,4)) if N<=17 else sorted(set([0,4,8,12,16,20,24,28,32, (N*N-1)//4*4]+[((N*N-1)//4 - d)*4 for d in [1,2,3,4,16,128] if (N*N-1)//4-d>=0]))
        for t in targets:
            cells=choose_cells(N,t)
            assert len(cells)==t and all(symmetries(p)<=cells for p in cells)
            checks+=1
    # N=4 accepts reflection-grid normalization but no positive quadratic closure
    assert not any(a*a+b*b==15 for a in range(1,4) for b in range(1,4));checks+=1
    # same denominator, different orbits: novelty need not increase N
    assert orbit_cube_1d(1,3)=={1,5};checks+=1
    assert orbit_cube_1d(2,3)=={2,4};checks+=1
    assert orbit_cube_1d(1,3).isdisjoint(orbit_cube_1d(2,3));checks+=1
    # finite subset of all square closures, and their reflected realization
    examples=[]
    for N in range(3,36,2):
        for a in range(2,N,2):
            b=isqrt(N*N-1-a*a) if N*N-1-a*a>0 else 0
            if b>=a and b%2==0 and a*a+b*b+1==N*N:
                cl=coloring(N,a,b)
                assert orbit_invariant(cl) and counts(cl)==Counter({'A':a*a,'B':b*b,'.':1})
                examples.append({'a':a,'b':b,'N':N,'orbitas':len(orbits(N))})
                checks+=2
    assert examples
    base=coloring(3,2,2)
    assert orbit_invariant(base)
    fail=refine(base,3,2,2,9,4,8)
    assert not fail['admisible'] and (fail['deltaA'],fail['deltaB'])==(-20,28)
    checks+=2
    # First example with monotone embedding and new occupation in one channel
    win51=refine(base,3,2,2,51,34,38)
    assert win51['admisible'] and (win51['deltaA'],win51['deltaB'])==(0,288)
    assert win51['grid'][(0,0)]=='.'
    checks+=2
    # Symmetric Pell extension (3 + 2 sqrt(2)) cubed
    win99=refine(base,3,2,2,99,70,70)
    assert win99['admisible'] and (win99['deltaA'],win99['deltaB'])==(544,544)
    checks+=2
    assert 99*99-2*70*70==1
    assert 3880899**2-2*2744210**2==1
    assert 3880899%99==0
    checks+=3
    # Include independent proof of geometry != literal contiguous squares
    cells=[{(i,j) for i in range(x,x+2) for j in range(y,y+2)} for x in (0,1) for y in (0,1)]
    assert all(cells[i]&cells[j] for i in range(4) for j in range(i+1,4));checks+=1
    with (OUT/'patron_3x3.txt').open('w') as f:
        for j in (1,0,-1):f.write(' '.join(base[(i,j)] for i in (-1,0,1))+'\n')
    with (OUT/'configuraciones_revisadas.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['a','b','N','orbitas']);w.writeheader();w.writerows(examples)
    result={
        'checks':checks,
        'modelo_D4':'Red finita N x N, reflexión por signos y permutación de coordenadas',
        'N3':dict(counts(base)),
        'contrato_nuevo':'a²+b²+1=N² provisional; no es la única identidad cuadrática del programa',
        'orbits_3':dict(Counter(map(len,orbits(3)))),
        'orbits_51':dict(Counter(map(len,orbits(51)))),
        'orbits_99':dict(Counter(map(len,orbits(99)))),
        '3_a_9':fail,
        '3_a_51':{k:v for k,v in win51.items() if k!='grid'},
        '3_a_99':{k:v for k,v in win99.items() if k!='grid'},
        'ejemplos_examinados':len(examples),
        'contraejemplo_optico':'1/3 y 2/3 son órbitas diferentes en dos espejos pero tienen denominador 3',
        'limites':'No es Navier–Stokes; un canal puede reunir varias órbitas; no demuestra ley dinámica ni a²+b²+1=N² ontológico',
    }
    (OUT/'resumen_o60.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
