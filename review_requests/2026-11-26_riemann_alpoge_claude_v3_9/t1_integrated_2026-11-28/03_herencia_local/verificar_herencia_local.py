"""448 transiciones, coeficientes óptimos y defectos de herencia.
Requiere NumPy. Cálculo de Gram reutilizado de T.1 v1.4 (doble precisión).
Ejecutar en este directorio; los JSON se escriben junto al script.
"""
import itertools,json,math
from pathlib import Path
from collections import defaultdict
import numpy as np
from verificacion_independiente_T1 import ip,ip_chi,divisors,PRIMES
ROOT=Path(__file__).resolve().parent
D=divisors(PRIMES); pos={d:i for i,d in enumerate(D)}
G=np.array([[ip(d,e) for e in D] for d in D]); b=np.array([ip_chi(d) for d in D]); results=[]

def data(S):
    ds=divisors(S); ids=[pos[d] for d in ds]; g=G[np.ix_(ids,ids)]; a=np.linalg.solve(g,b[ids]); Q=1-b[ids]@a
    return ds,ids,g,a,float(Q)

def moebius(n):
    sign=1; q=2
    while q*q<=n:
        if n%q==0:
            n//=q;sign=-sign
            if n%q==0:return 0
        q+=1
    return -sign if n>1 else sign

def h(d):
    c=defaultdict(int); B=0
    for k in range(1,d+1):
        if d%k:continue
        m=moebius(d//k);c[k]-=m;c[k-1]+=m;B+=m
    return c,B

def norm_h_sum(ds):
    c=defaultdict(int);B=0
    for d in ds:
        cd,bd=h(d);B+=bd
        for k,v in cd.items():c[k]+=v
    return math.sqrt(sum(v*v*((k+1)**3-k**3)/3 for k,v in c.items())+c[0]*B+B*B)

for p in PRIMES:
    oth=[q for q in PRIMES if q!=p]
    for size in range(len(oth)+1):
        for S in itertools.combinations(oth,size):
            ds,i,g,a,Q=data(S); j=[pos[d*p] for d in ds]; C=G[np.ix_(i,j)]; L=np.linalg.cholesky(g)
            A=np.sqrt(p)*np.linalg.solve(L,np.linalg.solve(L,C).T).T; T=A.T@A
            v=b[j]-C.T@a; z=np.sqrt(p/Q)*np.linalg.solve(L,v)
            w=z.copy(); moments=[]
            for k in range(5):
                moments.append(float(z@w));w=T@w
            eta=float(z@np.linalg.solve(np.eye(len(i))-T,z)); _,_,_,_,Qp=data(tuple(S)+(p,))
            assert abs(eta-(Q-Qp)/Q)<1e-8
            assert sum(moments)<=eta+1e-10 and min(moments)>=-1e-11
            results.append(dict(S=S,p=p,p_R4=p*sum(moments),p_mu=p*moments[0],p_eta=p*eta,Q=Q,mean=float(1-a.sum()/2)))
results.sort(key=lambda a:a['p_R4'])
assert len(results)==448 and sum(x['p_R4']<1 for x in results)==208
(ROOT/'transiciones_448.json').write_text(json.dumps(results,indent=2)+'\n')
print('Transiciones:',len(results),'p R4 < 1:',sum(x['p_R4']<1 for x in results))
print('Minimo:',results[0])

# La misma proyeccion optima en la cadena natural. Extraccion independiente
# de coeficientes mediante promedios de intervalos y diferencias de saltos.
rows=[]; vectors=[]; norms=[]; pairs=[(1,2),(1,3),(1,5),(2,3),(3,2),(2,5)]
for k in range(len(PRIMES)+1):
    S=PRIMES[:k];ds,i,g,a,Q=data(S);coeff=dict(zip(ds,map(float,a))); s=sum(coeff[d]/d for d in ds)
    def average(n):return sum(c*((n+.5)/d-n//d) for d,c in coeff.items())
    def jump(n):return average(n)-average(n-1)-s
    for d in [1,2,3,5,6,10,15,30,4,9,12]:
        extracted=-sum(moebius(d//n)*jump(n) for n in range(1,d+1) if d%n==0)
        assert abs(extracted-coeff.get(d,0))<1e-9
        assert abs(coeff.get(d,0)+moebius(d))<=norm_h_sum([d])*math.sqrt(Q)+1e-10
    defects={f'{d},{p}':coeff.get(d,0)+coeff.get(d*p,0) for d,p in pairs}
    for d,p in pairs: assert abs(defects[f'{d},{p}'])<=norm_h_sum([d,d*p])*math.sqrt(Q)+1e-10
    row=dict(S=S,Q=Q,mean=float(1-a.sum()/2),slope=s,coefficients={str(d):coeff.get(d,0) for d in [1,2,3,5,6,10,15,30]},defects=defects)
    rows.append(row)
    vector=np.zeros(len(D));vector[i]=a;vectors.append(vector)
# Ortogonalidad de las recuperaciones y variacion finita de defectos.
inc=np.diff(np.array(vectors),axis=0); gg=inc@G@inc.T
assert np.max(np.abs(gg-np.diag(np.diag(gg))))<1e-8
assert np.allclose(np.diag(gg),-np.diff([r['Q'] for r in rows]),atol=1e-9)
for d,p in pairs:
    key=f'{d},{p}'; variation=sum(abs(y['defects'][key]-x['defects'][key]) for x,y in zip(rows,rows[1:]))
    upper=norm_h_sum([d,d*p])*math.sqrt(rows[0]['Q']-rows[-1]['Q'])
    assert variation<=upper+1e-9
(ROOT/'coeficientes_y_defectos.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Cadena natural:')
print('ultimo  Q            a1         a2        a3       a6       a1+a2     a1+a3')
for row in rows:
    c=row['coefficients'];f=row['defects'];print(f"{(row['S'] or [1])[-1]:3d} {row['Q']:.9f} {c['1']:10.6f} {c['2']:9.6f} {c['3']:9.6f} {c['6']:9.6f} {f['1,2']:9.6f} {f['1,3']:9.6f}")
print('OK: extraccion por saltos, cotas de defectos, ortogonalidad y variacion finita.')
