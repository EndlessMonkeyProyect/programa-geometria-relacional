#!/usr/bin/env python3
"""O72: tests for graph bipartiteness, linkage ranks, parity under mirrors, and conditional flow analogy.
Dependencies: numpy, matplotlib. Execute from anywhere: python verificar_o72.py
"""
from pathlib import Path
import json,itertools,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'datos').mkdir(parents=True,exist_ok=True)
(ROOT/'graficos').mkdir(parents=True,exist_ok=True)
pass_count=0

def check(condition, name):
    global pass_count
    if not condition:
        raise AssertionError(name)
    pass_count += 1

def Qmat(n,edges):
    q=np.zeros((len(edges),n),dtype=float)
    for k,(i,j) in enumerate(edges):q[k,i]=q[k,j]=1
    return q

def connected(n,edges):
    if not edges: return n==1
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen={0};stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]-seen:seen.add(j);stack.append(j)
    return len(seen)==n

def is_bipartite(n,edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    colors={}
    for root in range(n):
        if root in colors:continue
        colors[root]=0;stack=[root]
        while stack:
            i=stack.pop()
            for j in adj[i]:
                if j not in colors: colors[j]=1-colors[i];stack.append(j)
                elif colors[j]==colors[i]:return False
    return True

def rank(A):return int(np.linalg.matrix_rank(A,tol=1e-9))

def rigid_jacobian(pts,edges):
    n,d=pts.shape
    J=np.zeros((len(edges),n*d))
    for k,(i,j) in enumerate(edges):
        dx=2*(pts[i]-pts[j]); J[k,i*d:(i+1)*d]=dx;J[k,j*d:(j+1)*d]=-dx
    return J

def orient_area(pts):
    return 0.5*sum(pts[i,0]*pts[(i+1)%len(pts),1]-pts[i,1]*pts[(i+1)%len(pts),0] for i in range(len(pts)))

C4=[(0,1),(1,2),(2,3),(3,0)]
K4=list(itertools.combinations(range(4),2))
TRI=[(0,1),(1,2),(0,2)]
DIAG=[(0,2),(1,3)]
sigma=np.array([1.,-1.,1.,-1.])
qc=Qmat(4,C4); qt=Qmat(4,K4); qtri=Qmat(3,TRI)

check(rank(qc)==3,'C4 rank3')
check(rank(qt)==4,'K4 rank4')
check(rank(qtri)==3,'triangle rank3')
check(np.allclose(qc@sigma,0),'C4 alternating mode')
check(rank(Qmat(4,C4+[DIAG[0]]))==4,'single diagonal blocks alternation')
check(rank(Qmat(4,C4+[DIAG[1]]))==4,'other diagonal blocks alternation')
# Analytic graph kernel theorem: connected bipartite nullity1; odd cycles nullity0.
for n in range(3,20):
    E=[(i,(i+1)%n) for i in range(n)]
    check(n-rank(Qmat(n,E)) == int(n%2==0),f'C{n} nullity')
for n in [4,5,6]:
    all_edges=list(itertools.combinations(range(n),2))
    # exhaustive graphs n=4/5; reproducibly sampled for n=6
    if n<=5: masks=range(1<<len(all_edges))
    else: masks=np.random.default_rng(72021).integers(0,1<<len(all_edges),size=300)
    for mask in masks:
        es=[e for k,e in enumerate(all_edges) if int(mask)&(1<<k)]
        if connected(n,es):
            actual=n-rank(Qmat(n,es))
            expected=int(is_bipartite(n,es))
            check(actual==expected,f'graph n{n} mask{mask}')

# Uniform but unequal gear radii. These are effective contact radii, not torus ring radii.
r=np.array([1.1, 2.2, .7, 1.8]); s=3.0
om=s*sigma/r
check(np.allclose(qc@(r*om),0),'arbitrary radii gear compatibility')
r2=np.array([2.3,1.5,1.4,.8]); omega2=s*sigma/r2
check(np.allclose(qc@(r2*omega2),0),'radial change absorbed if rates compensate')
check(np.linalg.norm(qc@(r2*om))>.1,'same omega incompatible after general radial change')

# Four vertices of a regular tetrahedron, projected onto the xy plane: square with both diagonals visible.
T=np.array([[1.,1.,1.],[-1.,1.,-1.],[-1.,-1.,1.],[1.,-1.,-1.]])
Tmir=T.copy();Tmir[:,2]*=-1
V=lambda p: np.linalg.det(np.column_stack([p[1]-p[0],p[2]-p[0],p[3]-p[0]]))/6
check(np.allclose(T[:,:2],Tmir[:,:2]),'same projection mirrored tetrahedra')
check(abs(V(T))>0 and np.isclose(V(T),-V(Tmir)),'projection loses handedness')
D=np.linalg.norm(T[:,None]-T[None,:],axis=-1)
check(np.allclose(D[np.triu_indices(4,k=1)],np.sqrt(8)),'regular tetrahedron all equal edges')
check(rank(rigid_jacobian(T,K4))==6,'tetra has six independent length constraints')
check(rank(rigid_jacobian(T[:,:2],C4))==4,'planar four bar has four independent constraints')
check(rank(rigid_jacobian(T[:,:2],K4))==5,'planar K4 is rigid modulo Euclidean motions')

# Family of planar rhombi: equal constant edge lengths, one free shape angle.
def rhombus(phi, length=2.):
    return np.array([[0,0],[length,0],[length+length*np.cos(phi),length*np.sin(phi)],[length*np.cos(phi),length*np.sin(phi)]],dtype=float)
phis=np.linspace(.04,np.pi-.04,180)
areas=[]
for phi in phis:
    P=rhombus(phi)
    perimeter=np.array([np.linalg.norm(P[i]-P[(i+1)%4]) for i in range(4)])
    check(np.allclose(perimeter,2),'four-bar side lengths remain fixed')
    check(np.isclose(orient_area(P),4*np.sin(phi)),'rhombus area formula')
    areas.append(orient_area(P))
check(abs(orient_area(rhombus(0.0)))<1e-12,'collapse possible even with four gear links')
check(np.allclose(qc@sigma,0),'gear mode remains after geometric collapse')

# Discrete mirror representation: 90deg cyclic relabeling sends alternating pattern to its negative.
x=s*sigma
rotate=np.roll(x,1)
check(np.allclose(rotate,-x),'quarter-turn anti-invariant mode')
check(np.isclose(sum(np.mean(np.roll(x,k)) for k in range(4))/4,0),'mirror common misses alternation')
check(np.isclose(np.mean(x*x),np.mean((-x)*(-x))),'unsigned second order indistinguishable')
check(np.isclose(np.mean(sigma*x),s),'oriented linear projection recovers signed mode')
check(np.isclose(np.mean(sigma*x**3),s**3),'oriented third order distinguishes sign')

# Dynamic diagnostic: adding diagonal coupling weakly leads exact exponential relaxation of this mode.
qdiag=Qmat(4,DIAG)
check(np.allclose(qdiag.T@qdiag@sigma,2*sigma),'diagonals give eigenvalue2')
check(np.allclose(qc.T@qc@sigma,0),'perimeter zero eigenvalue')
times=np.linspace(0,2.5,251)
arr={}
for alpha in (0.,.1,.5,1.):
    M=qc.T@qc+alpha*qdiag.T@qdiag
    check(np.allclose(M@sigma,2*alpha*sigma),f'decay eig {alpha}')
    arr[str(alpha)]=list(map(float,s*np.exp(-2*alpha*times)))

plt.figure(figsize=(7,6)); ax=plt.axes(projection='3d')
for i,j in K4:
    P=T[[i,j]]
    ax.plot(P[:,0],P[:,1],P[:,2],lw=1.8)
ax.scatter(T[:,0],T[:,1],T[:,2],s=85)
for k,(a,b,c) in enumerate(T):ax.text(a+.10,b+.10,c+.11,str(k+1))
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Tetraedro: 4 nodos, 6 enlaces activos')
ax.set_box_aspect((1,1,1)); plt.tight_layout()
plt.savefig(ROOT/'graficos'/'o72_tetraedro_6_enlaces.png',dpi=180);plt.close()

plt.figure(figsize=(7,5.5))
P=T[:,:2]
for i,j in C4:plt.plot(P[[i,j],0],P[[i,j],1],lw=2.7)
for i,j in DIAG:plt.plot(P[[i,j],0],P[[i,j],1],ls=':',alpha=.5)
plt.scatter(P[:,0],P[:,1],s=100)
for i,(a,b) in enumerate(P):plt.text(a+.11,b+.11,str(i+1))
plt.axis('equal');plt.xlabel('x');plt.ylabel('y')
plt.title('Proyección: 4 enlaces activos; diagonales sin imponer')
plt.tight_layout();plt.savefig(ROOT/'graficos'/'o72_anillo_cuatro_enlaces.png',dpi=180);plt.close()

plt.figure(figsize=(7,4.8))
for alpha in (0.,.1,.5,1.):
    plt.plot(times,arr[str(alpha)],label=f'Diagonales: acoplamiento {alpha:g}')
plt.xlabel('Parámetro del modelo de relajación')
plt.ylabel('Amplitud de giro alternado s(t)')
plt.title('Si se activan diagonales, se pierde el modo libre')
plt.legend();plt.grid(alpha=.25);plt.tight_layout()
plt.savefig(ROOT/'graficos'/'o72_activacion_enlaces.png',dpi=180);plt.close()

plt.figure(figsize=(7,4.8))
plt.plot(phis,areas)
plt.xlabel('Ángulo interno entre enlaces (rad)')
plt.ylabel('Área orientada del paralelogramo')
plt.title('Anillo articulado: enlaces fijos, área variable')
plt.grid(alpha=.25);plt.tight_layout()
plt.savefig(ROOT/'graficos'/'o72_area_vs_indefinicion.png',dpi=180);plt.close()

result={
    'date':'2026-10-21','chapter':'O72', 'tests_passed':pass_count,
    'gear_graph':{'K4_rank':rank(qt),'K4_nullity':4-rank(qt),'C4_rank':rank(qc),'C4_nullity':4-rank(qc),'C3_rank':rank(qtri),'C3_nullity':3-rank(qtri),'one_diagonal_rank':rank(Qmat(4,C4+[DIAG[0]]))},
    'projection':{'signed_tetra_volume':V(T),'signed_mirror_volume':V(Tmir),'tetra_edge_squared':8,'tetra_rigidity_rank':rank(rigid_jacobian(T,K4)),'planar_ring_rigidity_rank':rank(rigid_jacobian(T[:,:2],C4)),'planar_full_projection_rank':rank(rigid_jacobian(T[:,:2],K4))},
    'dynamics':{'mode_initial':s,'diag_coupling_eigenvalue_per_unit_alpha':2,'formula':'s(t)=s0 exp(-2 alpha t)','interpretation':'artificial relaxation law, not Navier-Stokes'},
    'meaning':'Demonstrates freedom introduced by relaxing graph constraints. Does not derive vortex ring creation, stability, non-merger or NS regularity.'
}
(ROOT/'datos'/'resultados_o72.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2,ensure_ascii=False))
