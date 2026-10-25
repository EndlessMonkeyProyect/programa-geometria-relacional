#!/usr/bin/env python3
"""Validacion independiente: enumeracion de coloraciones vs eliminacion y contracciones."""
import json
from itertools import combinations, product
from random import Random
from pathlib import Path
from laboratorio_v2 import eliminate, diamond_reduce, canon, rgs, test_boundary, k4, anchors, graph_c5


def count_colorings(V,E):
    nodes=sorted(V)
    index={v:i for i,v in enumerate(nodes)}
    return sum(1 for t in product(range(3), repeat=len(nodes)) if all(t[index[a]]!=t[index[b]] for a,b in E))


def verify_graph(V,E):
    want=count_colorings(V,E)>0
    o=eliminate(V,E,orbit=True,policy='min_fill')
    r=eliminate(V,E,orbit=False,policy='min_fill')
    assert not o['capped'] and not r['capped']
    assert o['satisfiable']==r['satisfiable']==want,('eliminate',V,E)
    U,F,d=diamond_reduce(V,E)
    if d['contradiction']:
        assert not want,('false-contradiction',V,E,d['trace'])
    else:
        # By bijection, number of original proper colorings equals number of reduced proper colorings.
        assert count_colorings(U,F)==count_colorings(V,E),('merge-lost-solutions',V,E,d['trace'])
        oo=eliminate(U,F,orbit=True,policy='min_fill')
        assert oo['satisfiable']==want,('reduced-eliminate',V,E)
    return bool(d['contradiction']), len(d['trace'])


def main():
    stats={'exhaustive':{},'random_6':{},'symmetry_counterexample_with_fixed_color':True}
    for n in (4,5):
        V=set(range(n));pairs=list(combinations(range(n),2))
        N=1<<len(pairs); merges=0; contradictions=0
        for mask in range(N):
            E={pairs[j] for j in range(len(pairs)) if (mask>>j)&1}
            neg,nstep=verify_graph(V,E)
            contradictions+=int(neg);merges+=nstep
        stats['exhaustive'][str(n)]={'graphs':N,'total_reductions_and_contradictions':merges,'local_unsat_witnesses':contradictions,'all_ok':True}
        print('EXHAUSTIVO n=',n,N,'PASSED')
    rng=Random(20261022);V=set(range(6));pairs=list(combinations(range(6),2))
    merges=0; contradictions=0
    for i in range(250):
        E={p for p in pairs if rng.randrange(2)}
        neg,nstep=verify_graph(V,E)
        contradictions+=int(neg);merges+=nstep
    stats['random_6']={'graphs':250,'seed':20261022,'total_reductions_and_contradictions':merges,'local_unsat_witnesses':contradictions,'all_ok':True}
    # Canonicalization by color permutations is NOT correct with absolute color pinning:
    assert canon((0,))==canon((1,)) and ((0,)==(0,)) and ((1,)!=(0,))
    assert test_boundary()['intersections']==[18,12]
    # A direct exact check: forced equality iff the added inequality makes 3-color impossible.
    # Separate UNSAT: there are no compatible colorings, so a universal equality is vacuous.
    V,E=anchors(5)
    ncol=count_colorings(V,E)
    uv=(2,3)
    assert uv not in E and ncol>0 and count_colorings(V,E|{uv})==0
    V,E=graph_c5()
    assert count_colorings(V,E)>0 and count_colorings(V,E|{(0,2)})>0
    V,E=k4();V|={4,5}
    assert count_colorings(V,E)==0 and count_colorings(V,E|{(4,5)})==0
    stats['forced_equality_trivalent']={'anchors_5_leaves':'forced','C5_0_2':'not_forced','K4_plus_isolates':'unsatisfiable_not_forced','all_ok':True}
    output=Path(__file__).parent/'controles_exhaustivos.json' 
    output.write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASSED total:',64+1024+250,'graphs')
if __name__=='__main__':main()
