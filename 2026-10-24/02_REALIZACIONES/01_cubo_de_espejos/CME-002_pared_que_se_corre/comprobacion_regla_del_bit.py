# Regla del bit: un ±1 en cada nodo (cambiar signo = espejo) y el intercambio de dos nodos (espejo).
# ¿Qué ángulos π/k aparecen entre espejos, y cuántas orientaciones genera? Además: órdenes ord_p(2).
import itertools, numpy as np, sympy as sp
def grupo(gens):
    key=lambda A: tuple(A.astype(int).ravel()); n=gens[0].shape[0]
    vistos={key(np.eye(n))}; frente=[np.eye(n)]
    while frente:
        nuevo=[]
        for A in frente:
            for g in gens:
                P=g@A
                if key(P) not in vistos: vistos.add(key(P)); nuevo.append(P)
        frente=nuevo
    return [np.array(k).reshape(n,n) for k in vistos]
def orden(A):
    n=A.shape[0]; P=np.eye(n); 
    for k in range(1,50):
        P=P@A
        if np.allclose(P,np.eye(n)): return k
for n in (2,3,4):
    flip=[np.diag([(-1 if j==i else 1) for j in range(n)]) for i in range(n)]
    swap=[]
    for i in range(n-1):
        M=np.eye(n); M[[i,i+1]]=M[[i+1,i]]; swap.append(M)
    G=grupo(flip+swap)
    refl=[A for A in G if round(np.linalg.det(A))==-1 and round(np.trace(A))==n-2]
    ks=sorted({orden(A@B) for A,B in itertools.combinations(refl,2)})
    print(f"n={n} nodos: {len(G)} orientaciones (2^n·n! = {2**n*sp.factorial(n)}), {len(refl)} espejos, ángulos π/k con k en {ks}")
print("órdenes ord_p(2) de los primos nuevos de tu genealogía (centros 4..256):")
for p in [3,5,7,17,31,11,13,127,43,257]: print(f"  p={p}: ord={sp.n_order(2,p)}")
print("enteros n<=40 sin primo con ord_p(2)=n (Zsigmondy):",[n for n in range(1,41) if not any(sp.n_order(2,p)==n for p in sp.primefactors(2**n-1))])
