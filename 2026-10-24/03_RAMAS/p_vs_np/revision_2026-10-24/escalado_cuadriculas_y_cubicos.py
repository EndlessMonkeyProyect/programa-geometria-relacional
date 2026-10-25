import sys, random, time
sys.path.insert(0, sys.argv[1])
from laboratorio_v2 import eliminate, grid
from itertools import product
from math import comb

def stirling2(n,k):
    from functools import lru_cache
    @lru_cache(None)
    def S(n,k):
        if n==k==0: return 1
        if n==0 or k==0: return 0
        return k*S(n-1,k)+S(n-1,k-1)
    return S(n,k)
for k in (8,10):
    print("P3(%d)="%k, sum(stirling2(k,j) for j in range(1,4)), "vs 3^k=",3**k)

print("\n-- Cuadriculas k x k (bipartitas: 2-coloreables por BFS en tiempo lineal) --")
for k in range(3,10):
    V,E=grid(k,k); t=time.time()
    r=eliminate(V,E,policy='min_fill',orbit=True,cap=10**8)
    print(f"k={k} n={len(V):3d}  evals_S3={r['total_evaluations']:>9}  max_bag={r['max_bag']}  sat={r['satisfiable']}  {time.time()-t:.1f}s")

# independent backtracking solver
def bt(V,E):
    nbr={v:set() for v in V}
    for a,b in E: nbr[a].add(b); nbr[b].add(a)
    order=sorted(V,key=lambda v:-len(nbr[v])); col={}
    def rec(i):
        if i==len(order): return True
        v=order[i]; used={col[u] for u in nbr[v] if u in col}
        for c in range(3):
            if c not in used:
                col[v]=c
                if rec(i+1): return True
                del col[v]
        return False
    return rec(0)

print("\n-- Correccion vs solucionador independiente: 300 grafos aleatorios n=10..14 --")
rng=random.Random(7); bad=0; sats=0
for i in range(300):
    n=rng.randint(10,14); p=rng.uniform(0.2,0.5)
    V=set(range(n)); E={(a,b) for a in range(n) for b in range(a+1,n) if rng.random()<p}
    want=bt(V,E); got=eliminate(V,E,policy='min_fill',orbit=True,cap=10**8)
    sats+=want; bad+= (got['satisfiable']!=want)
print("discrepancias:",bad,"  satisfacibles:",sats,"/300")

def random_cubic(n,rng):
    while True:
        pts=[v for v in range(n) for _ in range(3)]; rng.shuffle(pts)
        E=set(); ok=True
        for i in range(0,len(pts),2):
            a,b=pts[i],pts[i+1]
            if a==b or (min(a,b),max(a,b)) in E: ok=False;break
            E.add((min(a,b),max(a,b)))
        if ok: return set(range(n)),E
print("\n-- Grafos 3-regulares aleatorios (ancho crece linealmente con n) --")
rng=random.Random(11)
for n in (16,24,32,40,48,56):
    V,E=random_cubic(n,rng); t=time.time()
    r=eliminate(V,E,policy='min_fill',orbit=True,cap=3*10**7)
    print(f"n={n:3d} evals_S3={r['total_evaluations']:>9} max_bag={r['max_bag']} capped={r['capped']} sat={r.get('satisfiable')} {time.time()-t:.1f}s")
