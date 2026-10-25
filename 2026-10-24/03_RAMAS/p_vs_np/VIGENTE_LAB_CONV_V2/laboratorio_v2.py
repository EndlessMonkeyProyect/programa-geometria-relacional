#!/usr/bin/env python3
"""Programa de Geometria Relacional | LAB-CONV v2: cierre exacto por frontera, simetria y falsadores.
Solo biblioteca estandar. Sin SAT. Contrato: grafos simples no orientados, 3 colores sin anclajes.
"""
import json
from collections import deque
from dataclasses import dataclass
from itertools import product, combinations
from pathlib import Path
import argparse

COLORS=3


def canon(s):
    colors={}
    output=[]
    for x in s:
        if x not in colors: colors[x]=len(colors)
        output.append(colors[x])
    return tuple(output)


def rgs(n, max_colors=3):
    if n==0:
        yield ()
        return
    def rec(prefix, used):
        if len(prefix)==n:
            yield tuple(prefix)
        else:
            for j in range(min(used+1,max_colors)):
                prefix.append(j)
                yield from rec(prefix,max(used,j+1))
                prefix.pop()
    yield from rec([0],1)


def all_valuations(k, orbit):
    return rgs(k) if orbit else product(range(COLORS),repeat=k)

@dataclass
class Factor:
    scope: tuple
    support: set
    orbit: bool
    def accepts(self, t):
        return (canon(t) if self.orbit else tuple(t)) in self.support


def edge_factors(edges, orbit):
    return [Factor((a,b), {canon((x,y)) if orbit else (x,y) for x in range(3) for y in range(3) if x!=y}, orbit) for a,b in sorted(edges)]


def primal_order(V, E, policy):
    if policy=='reverse': return sorted(V,reverse=True)
    if policy=='natural': return sorted(V)
    nbr={v:set() for v in V}
    for a,b in E: nbr[a].add(b); nbr[b].add(a)
    remain=set(V)
    order=[]
    while remain:
        def score(v):
            adj=sorted(nbr[v]&remain)
            fill=sum((b not in nbr[a]) for a,b in combinations(adj,2))
            return (fill,len(adj),v)
        v=min(remain,key=score)
        adj=sorted(nbr[v]&remain)
        for a,b in combinations(adj,2):
            nbr[a].add(b);nbr[b].add(a)
        remain.remove(v);order.append(v)
    return order


def eliminate(V, E, policy='min_fill', orbit=False, cap=150000):
    factors=edge_factors(E,orbit)
    if not E: return dict(satisfiable=True, order=primal_order(V,E,policy), steps=[], total_evaluations=0, total_trials=0, max_bag=0, peak_relation_size=0, capped=False)
    order=primal_order(V,E,policy)
    data=[];total_evals=0;trials=0;peak=0;max_bag=0
    for v in order:
        group=[f for f in factors if v in f.scope]
        if not group: continue
        factors=[f for f in factors if v not in f.scope]
        scope=sorted(set().union(*(set(f.scope) for f in group)))
        B=tuple(z for z in scope if z!=v)
        max_bag=max(max_bag,len(scope))
        allowed=set();evaluations=0;step_trials=0;lookups=0
        for b_t in all_valuations(len(B),orbit):
            evaluations+=1
            if total_evals+evaluations>cap:
                return dict(capped=True, cap=cap, stopped_at=v, order=order, steps=data,total_evaluations=total_evals+evaluations,total_trials=trials,max_bag=max_bag,peak_relation_size=peak)
            env=dict(zip(B,b_t))
            for c in range(COLORS):
                step_trials+=1
                env[v]=c
                good=True
                for f in group:
                    lookups+=1
                    if not f.accepts(tuple(env[z] for z in f.scope)):
                        good=False
                        break
                if good:
                    allowed.add(tuple(b_t));break
        total_evals+=evaluations;trials+=step_trials
        peak=max(peak,len(allowed))
        factors.append(Factor(B,allowed,orbit))
        data.append(dict(eliminated=v,bag=len(scope),boundary=len(B),frontier_candidates=evaluations,frontier_valid=len(allowed),extension_trials=step_trials,factor_checks=lookups))
        # An empty projected relation on ANY boundary disproves global feasibility.
        if not allowed:
            return dict(satisfiable=False,order=order,steps=data,total_evaluations=total_evals,total_trials=trials,max_bag=max_bag,peak_relation_size=peak,capped=False,contradiction_at=v,contradiction_frontier=list(B))
    return dict(satisfiable=all(bool(f.support) for f in factors),order=order,steps=data,total_evaluations=total_evals,total_trials=trials,max_bag=max_bag,peak_relation_size=peak,capped=False)


def graph_c5():
    return set(range(5)),{tuple(sorted((i,(i+1)%5))) for i in range(5)}


def mycielski(V,E):
    n=len(V);assert V==set(range(n))
    extra=set(E)
    for u,v in E:
        extra.add(tuple(sorted((u,v+n))))
        extra.add(tuple(sorted((v,u+n))))
    for v in V:
        extra.add(tuple(sorted((v+n,2*n))))
    return set(range(2*n+1)),extra


def wheel(k):
    V=set(range(k+1));E={tuple(sorted((i,(i+1)%k))) for i in range(k)}
    E|={(i,k) for i in range(k)}
    return V,E


def grid(rows,cols):
    V=set(range(rows*cols)); E=set()
    for i in range(rows):
        for j in range(cols):
            u=i*cols+j
            if i+1<rows: E.add((u,(i+1)*cols+j))
            if j+1<cols: E.add((u,u+1))
    return V,E


def ladder(k): return grid(2,k)


def k4():return set(range(4)),set(combinations(range(4),2))


def anchors(m):
    V=set(range(m+2)); E={(0,1)}
    E|={(u,v) for v in range(2,m+2) for u in (0,1)}
    return V,E


def graph_neighbors(V,E):
    nbr={v:set() for v in V}
    for a,b in E: nbr[a].add(b);nbr[b].add(a)
    return nbr


def diamond_count(V,E):
    nbr=graph_neighbors(V,E)
    return sum(len(list(combinations(nbr[a]&nbr[b],2))) for a,b in E)


def neighborhood_odd_cycle(V,E):
    """Sound: if N(v) contains an odd cycle, neighbors require only 2 colors -> contradiction."""
    nbr=graph_neighbors(V,E)
    for v in sorted(V):
        U=nbr[v]
        parity={}; parent={}
        for root in sorted(U):
            if root in parity: continue
            parity[root]=0;parent[root]=None
            q=deque([root])
            while q:
                x=q.popleft()
                for y in sorted(nbr[x]&U):
                    if y not in parity:
                        parity[y]=1-parity[x];parent[y]=x;q.append(y)
                    elif parity[y]==parity[x]:
                        # Construct odd cycle as independently checkable witness.
                        ax=[];p=x
                        while p is not None:ax.append(p);p=parent[p]
                        ay=[];p=y
                        while p is not None:ay.append(p);p=parent[p]
                        positions={u:i for i,u in enumerate(ay)}
                        ix=next(i for i,u in enumerate(ax) if u in positions)
                        iy=positions[ax[ix]]
                        cycle=ax[:ix+1]+list(reversed(ay[:iy]))
                        assert len(cycle)>=3 and len(cycle)%2==1
                        assert all(tuple(sorted((cycle[i],cycle[(i+1)%len(cycle)]))) in E for i in range(len(cycle)))
                        assert set(cycle)<=U
                        return dict(vertex=v,odd_cycle=cycle)
    return None


def diamond_reduce(V, E):
    """Contract every certified same-color diamond pair; detect impossible adjacent pair.
    Every contraction preserves a bijection of properly 3-colored labeled assignments.
    """
    U=set(V);edges=set(E)
    origin_to_node={v:v for v in V}
    steps=[]; scans=0
    while True:
        nbr=graph_neighbors(U,edges)
        found=None
        for a,b in sorted(edges):
            common=sorted(nbr[a]&nbr[b])
            for u,v in combinations(common,2):
                scans+=1
                found=(a,b,u,v)
                break
            if found:break
        if not found:
            return U,edges,dict(contradiction=False,trace=steps,scan_pairs=scans,origin_to_node=origin_to_node)
        a,b,u,v=found
        if (min(u,v),max(u,v)) in edges:
            steps.append(dict(action='contradiction',anchors=[a,b],forced_equal=[u,v],reason='forced equal but adjacent'))
            return U,edges,dict(contradiction=True,trace=steps,scan_pairs=scans,origin_to_node=origin_to_node)
        keep,remove=min(u,v),max(u,v)
        new_edges=set()
        for x,y in edges:
            x=keep if x==remove else x
            y=keep if y==remove else y
            if x==y:
                raise AssertionError('nonadjacent merge generated a loop')
            new_edges.add((min(x,y),max(x,y)))
        U.remove(remove);edges=new_edges
        for old,rep in origin_to_node.items():
            if rep==remove: origin_to_node[old]=keep
        steps.append(dict(action='merge',anchors=[a,b],forced_equal=[u,v],keep=keep,remove=remove,n_remaining=len(U)))


def brute_satisfiable(V,E):
    """Independent verifier, exhaustive small instances only."""
    nodes=sorted(V)
    for t in product(range(3),repeat=len(nodes)):
        env=dict(zip(nodes,t))
        if all(env[a]!=env[b] for a,b in E):return True
    return False


def partition_histogram(k):
    reps=list(rgs(k));hist={1:0,2:0,3:0}
    for x in reps:hist[len(set(x))]+=1
    return dict(k=k,full_states=3**k,orbit_states=len(reps),partitions=hist)


def test_boundary():
    # A: a!=b; D: b!=c, same scalar cardinality. New comparison: a!=b.
    seq=list(product(range(3),repeat=3))
    A={x for x in seq if x[0]!=x[1]}
    D={x for x in seq if x[1]!=x[2]}
    C={x for x in seq if x[0]!=x[1]}
    assert len(A)==len(D)==18 and len(A&C)==18 and len(D&C)==12
    orbit_A={canon(x) for x in A};orbit_D={canon(x) for x in D}
    def diam(S):
        return max(sum(x!=y for x,y in zip(a,b)) for a in S for b in S)
    assert diam(A)==diam(D)==3
    return dict(cards=[len(A),len(D)],intersections=[len(A&C),len(D&C)],hamming_diameters=[diam(A),diam(D)],half_diameters=[diam(A)/2,diam(D)/2],orbit_signature_A=[''.join(map(str,x)) for x in sorted(orbit_A)],orbit_signature_D=[''.join(map(str,x)) for x in sorted(orbit_D)])


def main():
    out=Path(__file__).parent
    C,E=graph_c5();M,ME=mycielski(C,E)
    C7,EC7=wheel(7); # W7
    # Mycielski C7 by hand cycle 7
    V7=set(range(7)); CE7={tuple(sorted((i,(i+1)%7))) for i in range(7)}
    M7,EM7=mycielski(V7,CE7)
    V9=set(range(9));CE9={tuple(sorted((i,(i+1)%9))) for i in range(9)}
    M9,EM9=mycielski(V9,CE9)
    cases=[('C5',C,E),('K4',*k4()),('W5',*wheel(5)),('W7',C7,EC7),('Grotzsch_M_C5',M,ME),('Mycielski_C7',M7,EM7),('Mycielski_C9',M9,EM9),('ladder_2x5',*ladder(5)),('ladder_2x8',*ladder(8)),('grid_4x4',*grid(4,4)),('grid_5x5',*grid(5,5)),('anchors_9',*anchors(9))]
    report={'contract':'exact existential 3-colorability, no pinned colors; symmetry by global S3 color renaming only', 'cases':[], 'boundary_test':test_boundary(), 'orbit_counts':[partition_histogram(k) for k in (2,3,5,8,10)]}
    for name,V,E in cases:
        reduced_V,reduced_E,contraction=diamond_reduce(V,E)
        row={'graph':name,'n':len(V),'m':len(E),'diamonds':diamond_count(V,E),'neighborhood_odd_cycle':neighborhood_odd_cycle(V,E),'diamond_reduction':contraction,'reduced_n':len(reduced_V),'reduced_m':len(reduced_E),'results':{}}
        if not contraction['contradiction']:
            row['reduced_result']=eliminate(reduced_V,reduced_E,policy='min_fill',orbit=True,cap=130000)
        for policy in ('min_fill','reverse'):
            for orbit in (False,True):
                label=policy+('_orbit' if orbit else '_raw')
                result=eliminate(V,E,policy=policy,orbit=orbit,cap=130000)
                row['results'][label]=result
            a=row['results'][policy+'_raw'];b=row['results'][policy+'_orbit']
            if not a['capped'] and not b['capped']:
                assert a['satisfiable']==b['satisfiable'],(name,policy,'SYM_FAIL')
        fast=row['results']['min_fill_orbit']
        if name in ('C5','K4','W5','Grotzsch_M_C5'):
            assert not fast['capped'] and fast['satisfiable']==brute_satisfiable(V,E),name
        if name in ('W5','W7','K4'):
            assert row['neighborhood_odd_cycle'] is not None,name
        if name in ('Grotzsch_M_C5','Mycielski_C7','Mycielski_C9'):
            assert row['diamonds']==0 and row['neighborhood_odd_cycle'] is None,name
        if not fast['capped'] and not contraction['contradiction'] and not row['reduced_result']['capped']:
            assert fast['satisfiable']==row['reduced_result']['satisfiable'],(name,'contraction failed')
        if contraction['contradiction'] and not fast['capped']:
            assert fast['satisfiable']==False,(name,'unsound contradiction')
        report['cases'].append(row)
        print(name, len(V),len(E), 'diamond',row['diamonds'],'neigh-odd',bool(row['neighborhood_odd_cycle']), 'contractions',len(contraction['trace']), 'to',len(reduced_V),'contradiction',contraction['contradiction'])
        for policy in ('min_fill','reverse'):
            for sym in ('raw','orbit'):
                r=row['results'][policy+'_'+sym]
                print(' ',policy,sym,'YES' if r.get('satisfiable') else 'NO', 'CAPPED' if r['capped'] else '', 'evals',r['total_evaluations'],'bag',r['max_bag'],'peak_valid',r['peak_relation_size'])
    (out/'resultados_v2.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('OK',len(cases),'cases; outputs resultados_v2.json')

if __name__=='__main__':main()
