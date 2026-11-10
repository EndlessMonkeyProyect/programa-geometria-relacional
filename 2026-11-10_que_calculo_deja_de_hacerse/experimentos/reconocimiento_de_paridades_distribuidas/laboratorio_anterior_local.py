#!/usr/bin/env python3
"""GR3–ROSI–CAG: extracción certificable de paridad oculta en 3-CNF.
Incluye bloques completos (cuatro cláusulas), casi completos (tres)
y cláusulas OR arbitrarias. Solo librería estándar.
"""
from collections import defaultdict
from itertools import product
import json,random,time,sys

def parity(b): return sum(b)&1

def norm(cl):
    d={}
    for z in cl:
        if z==0: raise ValueError('literal cero')
        if abs(z) in d and d[abs(z)]!=z: return None
        d[abs(z)]=z
    return tuple(sorted(d.values(),key=lambda z:abs(z)))

def block(T,rhs,missing=None):
    T=tuple(sorted(T)); out=[]
    for b in product((0,1),repeat=3):
        if parity(b)==1-rhs and b!=missing:
            out.append(tuple(-v if f else v for v,f in zip(T,b)))
    return out

def extract(n,clauses,near=True):
    unique=set(); taut=dups=0
    for cl in clauses:
        c=norm(cl)
        if c is None: taut+=1
        elif c in unique: dups+=1
        else:
            assert all(abs(z)<=n for z in c)
            unique.add(c)
    groups=defaultdict(dict); raw=[]
    for cl in unique:
        if len(cl)==3:
            T=tuple(abs(z) for z in cl)
            groups[T][tuple(int(z<0) for z in cl)]=cl
        else: raw.append(cl)
    full=[]; part=[]
    for T, pats in sorted(groups.items()):
        unused=set(pats)
        for bad in (0,1):
            matching={b for b in unused if parity(b)==bad}
            if len(matching)==4:
                full.append((T,1-bad)); unused-=matching
        if near:
            for bad in (0,1):
                matching={b for b in unused if parity(b)==bad}
                if len(matching)==3:
                    miss=next(b for b in product((0,1),repeat=3)
                              if parity(b)==bad and b not in matching)
                    part.append((T,1-bad,miss)); unused-=matching
        raw.extend(pats[b] for b in unused)
    return {'full':full,'near':part,'raw':sorted(raw),
            'n_original':len(clauses),'n_unique':len(unique),
            'taut':taut,'dups':dups}

def certificate_ok(clauses,ex):
    """Verificación SINTÁCTICA: las restricciones extraídas son exactamente las
    mismas cláusulas normalizadas, incluida la conservación del residuo.
    """
    orig={norm(cl) for cl in clauses}; orig.discard(None)
    derived=set(ex['raw'])
    for T,rhs in ex['full']:
        derived.update(norm(c) for c in block(T,rhs))
    for T,rhs,missing in ex['near']:
        derived.update(norm(c) for c in block(T,rhs,missing))
    return orig==derived

class Counter:
    def __init__(self):
        self.xors=self.insertions=self.nodes=self.leaves=self.branches=0
        self.heredadas=self.imposibles=self.activas=0
    def add(self,B,mask,rhs):
        self.insertions+=1
        for p,(m,r) in sorted(B.items(),reverse=True):
            if mask>>p&1:
                mask^=m;rhs^=r;self.xors+=1
        if mask==0: return B if rhs==0 else None
        out=B.copy();out[mask.bit_length()-1]=(mask,rhs);return out
    def addall(self,B,eqs):
        for mask,rhs in eqs:
            B=self.add(B,mask,rhs)
            if B is None: return None
        return B
    def violate(self,B,cl):
        return self.addall(B,((1<<(abs(z)-1),int(z<0)) for z in cl))
    def ie(self,n,B,raw):
        active=[]
        for cl in raw:
            bb=self.violate(B,cl)
            if bb is None:self.heredadas+=1
            elif len(bb)==len(B):
                self.imposibles+=1;return 0
            else:self.activas+=1;active.append(cl)
        def rec(i,B,sign):
            self.nodes+=1
            if i==len(active):
                self.leaves+=1
                return sign*(1<<(n-len(B)))
            ans=rec(i+1,B,sign)
            bb=self.violate(B,active[i])
            if bb is not None:ans+=rec(i+1,bb,-sign)
            return ans
        return rec(0,B,1)
    def solve(self,n,ex):
        B={}
        for T,r in ex['full']:
            B=self.add(B,sum(1<<(v-1) for v in T),r)
            if B is None:return 0
        def near_rec(i,B):
            if i==len(ex['near']):
                self.branches+=1
                return self.ie(n,B,ex['raw'])
            T,r,miss=ex['near'][i]
            a=self.add(B,sum(1<<(v-1) for v in T),r)
            ans=near_rec(i+1,a) if a is not None else 0
            b=self.addall(B,((1<<(v-1),bit) for v,bit in zip(T,miss)))
            if b is not None:ans+=near_rec(i+1,b)
            return ans
        return near_rec(0,B)

def count(n,clauses,near=True):
    t0=time.perf_counter_ns();ex=extract(n,clauses,near)
    assert certificate_ok(clauses,ex), 'extracción no conserva la 3-CNF'
    t1=time.perf_counter_ns();c=Counter();val=c.solve(n,ex)
    dt=round((time.perf_counter_ns()-t0)/1000,2)
    return {'count':val,'full':len(ex['full']),'near':len(ex['near']),
            'raw':len(ex['raw']),'branches':c.branches,'leaves':c.leaves,
            'nodes':c.nodes,'xors':c.xors,'insertions':c.insertions,
            'heredadas':c.heredadas,'activas':c.activas,'imposibles':c.imposibles,
            'total_us':dt,'extraccion_us':round((t1-t0)/1000,2)}

def brute(n,clauses):
    count=0
    for a in range(1<<n):
        count+=all(any(((a>>(abs(z)-1))&1)!=int(z<0) for z in cl) for cl in clauses)
    return count

def formula(n,r,u,k,seed):
    rng=random.Random(seed);planted=[rng.randrange(2) for _ in range(n)];used=set();out=[]
    def triple():
        while True:
            T=tuple(sorted(rng.sample(range(1,n+1),3)))
            if T not in used:used.add(T);return T
    for _ in range(r):
        T=triple();rhs=parity(planted[v-1] for v in T)
        out.extend(block(T,rhs))
    for _ in range(u):
        T=triple();rhs=parity(planted[v-1] for v in T)
        missing=rng.choice([b for b in product((0,1),repeat=3) if parity(b)==1-rhs])
        out.extend(block(T,rhs,missing))
    for _ in range(k):
        T=triple();bits=[rng.randrange(2) for _ in range(3)]
        if all(planted[v-1]==z for v,z in zip(T,bits)):bits[0]^=1
        out.append(tuple(-v if z else v for v,z in zip(T,bits)))
    rng.shuffle(out)
    return out

def k4_control():
    E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    position={e:i for i,e in enumerate(E)};C=Counter();B={}
    for t in ((0,1,2),(0,1,3),(0,2,3)):
        a,b,c=t
        mask=sum(1<<position[e] for e in ((a,b),(a,c),(b,c)))
        B=C.add(B,mask,0)
    return {'aristas':6,'ecuaciones_independientes':len(B),
            'patrones_compatibles':1<<(6-len(B)),'bits_minimos':6-len(B)}

def count_components(n,clauses):
    """Producto exacto sobre componentes de incidencia independientes.
    Cada componente se procesa por reconocimiento de raíz+residuo.
    La lectura y construcción de componentes se incluyen en tiempo total.
    """
    t0=time.perf_counter_ns()
    parent=list(range(n+1))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb:parent[ra]=rb
    clean=[]
    for clause in clauses:
        c=norm(clause)
        if c is None:continue
        clean.append(c)
        ids=[abs(z) for z in c]
        for v in ids[1:]:union(ids[0],v)
    pieces=defaultdict(lambda:{'vars':[], 'clauses':[]})
    for v in range(1,n+1):pieces[find(v)]['vars'].append(v)
    for c in clean:
        if c:pieces[find(abs(c[0]))]['clauses'].append(c)
        else:return {'conteo':0,'componentes':len(pieces),'tiempo_us':(time.perf_counter_ns()-t0)/1000}
    ans=1;maxsize=0;nodes=0
    for part in pieces.values():
        ids=part['vars'];trans={v:i+1 for i,v in enumerate(ids)}
        local=[tuple((1 if z>0 else -1)*trans[abs(z)] for z in c) for c in part['clauses']]
        z=count(len(ids),local)
        ans*=z['count'];maxsize=max(maxsize,len(ids));nodes+=z['nodes']
    return {'conteo':ans,'componentes':len(pieces),'max_variables_componente':maxsize,
            'nodos':nodes,'tiempo_us':round((time.perf_counter_ns()-t0)/1000,2)}

def run():
    result={'GR3':k4_control()}
    T=(1,2,3);near=block(T,0,missing=(0,0,1))
    result['ROSI']={'5_estados':count(3,near)['count'],
                    'tras_exclusion_raiz':count(3,near+[(1,2,3)])['count'],
                    'incorrecto_si_se_descarta_residuo':3,
                    'raiz':4,'residuo':1}
    assert result['GR3']['bits_minimos']==3
    assert result['ROSI']['5_estados']==5 and result['ROSI']['tras_exclusion_raiz']==4
    local=0
    for rhs in (0,1):
        f=block(T,rhs)
        assert count(3,f)['count']==4
        local+=1
        for b in product((0,1),repeat=3):
            if parity(b)==1-rhs:
                F=block(T,rhs,missing=b)
                assert count(3,F)['count']==5
                local+=1
    result['local_exhaustivo']={'casos':local,'todos_coinciden':True}
    edges=[]
    for clauses,n,expected in ((block(T,0)+block(T,1),3,0),
                               (block(T,0)+block(T,1,missing=(0,0,0)),3,1),
                               ([()],3,0),
                               ([(1,),(1,),(-1,2)],3,2)):
        v=count(n,clauses)
        assert v['count']==expected and v['count']==brute(n,clauses)
        edges.append({'n':n,'clausulas':len(clauses),'conteo':v['count'],
                      'full':v['full'],'near':v['near']})
    result['casos_limite']=edges
    samples=[]
    for i in range(60):
        n=6+i%6;f=formula(n,1+i%3,(i//3)%3,i%4,seed=7200+i)
        if i%7==0:f.extend((f[0],(1,-1,2)))
        fast=count(n,f);truth=brute(n,f)
        bypart=count_components(n,f)
        assert bypart['conteo']==truth
        if fast['count']!=truth:raise ValueError((i,fast,truth,f))
        samples.append((i,n,truth))
    result['aleatorios']={'casos':len(samples),'coinciden':True,'ejemplos':samples[:5]}
    benchmark=[]
    for n,r,u,k,seed in ((12,5,1,1,9),(18,8,2,2,11),(24,12,3,2,12),
                         (36,18,4,2,13),(48,26,4,2,14),(72,38,5,2,15),
                         (96,58,4,2,16)):
        f=formula(n,r,u,k,seed)
        a=count(n,f,True);b=count(n,f,False)
        if a['count']!=b['count']:raise ValueError(('bench',n,a,b))
        benchmark.append({'n':n,'clausulas':len(f),'conteo':a['count'],
                          'full':a['full'],'near':a['near'],'raw_puente':a['raw'],
                          'raw_sin_puente':b['raw'],'nodos_puente':a['nodes'],
                          'nodos_sin_puente':b['nodes'],
                          'tiempo_puente_us':a['total_us'],
                          'tiempo_sin_puente_us':b['total_us'],
                          'xor_puente':a['xors'],'xor_sin_puente':b['xors']})
    result['crecimiento']=benchmark
    negative=[]
    for n,k in ((9,8),(12,11),(16,13)):
        f=formula(n,0,0,k,seed=400+n)
        x=count(n,f);assert x['count']==brute(n,f)
        negative.append({'n':n,'clausulas':k,'conteo':x['count'],
                         'full':x['full'],'near':x['near'],
                         'nodos':x['nodes'],'tiempo_us':x['total_us']})
    result['sin_paridad']=negative
    # Familia con muchas raíces locales independientes, no solo u=O(log n).
    # Cada triple de tres cláusulas admite 5 estados, así que el producto es 5^u.
    disjoint=[]
    for u in (1,3,6,12,40,100,300):
        clauses=[]
        for t in range(u):
            T=(3*t+1,3*t+2,3*t+3)
            clauses.extend(block(T,0,missing=(0,0,1)))
        out=count_components(3*u,clauses)
        assert out['conteo']==5**u and out['componentes']==u
        disjoint.append({'n':3*u,'raices_locales':u,'clausulas':3*u,
                         'soluciones':str(out['conteo']),
                         'componentes':out['componentes'],
                         'nodos':out['nodos'],'tiempo_us':out['tiempo_us']})
    result['componentes_independientes']=disjoint
    result['estado']='PASS: todos los conteos coinciden con los controles'
    result['entorno']={'python':sys.version.split()[0],'observacion':
                        'Tiempos de una ejecución: orientativos, sin velocidad garantizada'}
    return result

if __name__=='__main__':
    t=time.perf_counter();R=run();R['entorno']['segundos']=round(time.perf_counter()-t,3)
    with open('resultados_puente.json','w',encoding='utf-8') as fp:
        json.dump(R,fp,indent=2,ensure_ascii=False)
    print(R['estado']);print('K4',R['GR3'],'ROSI',R['ROSI'])
    for a in R['crecimiento']:
        print('n=%3d clauses=%3d near=%d raw=%d/%d nodes=%d/%d time_us=%g/%g' %
              (a['n'],a['clausulas'],a['near'],a['raw_puente'],
               a['raw_sin_puente'],a['nodos_puente'],a['nodos_sin_puente'],
               a['tiempo_puente_us'],a['tiempo_sin_puente_us']))
    print('Tiempo total de controles',R['entorno']['segundos'])
