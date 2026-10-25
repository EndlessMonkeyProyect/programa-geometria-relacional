#!/usr/bin/env python3
"""Laboratorio de cierre relacional / contrastes de 3-coloracion; Python estandar."""
import json
from itertools import combinations


def c5():
    return set(range(5)), {tuple(sorted((i, (i+1)%5))) for i in range(5)}


def mycielski(V,E):
    """M(G): originals i; copies i+n; apex 2n."""
    n=len(V)
    assert V==set(range(n))
    extra=set(E)
    for u,v in E:
        extra.add(tuple(sorted((u,v+n))))
        extra.add(tuple(sorted((v,u+n))))
    for v in V:
        extra.add(tuple(sorted((v+n,2*n))))
    return set(range(2*n+1)), extra


def neighbors(V,E):
    nbr={v:set() for v in V}
    for a,b in E:
        if a in V and b in V:
            nbr[a].add(b);nbr[b].add(a)
    return nbr


def has_3_coloring(V,E):
    nbr=neighbors(V,E)
    colors={}
    unassigned=set(V)
    def visit():
        if not unassigned:
            return dict(colors)
        # DSATUR: maximum saturation / degree, deterministic
        v=max(sorted(unassigned),key=lambda k:(len({colors[u] for u in nbr[k] if u in colors}),len(nbr[k])))
        used={colors[u] for u in nbr[v] if u in colors}
        for col in range(3):
            if col in used: continue
            colors[v]=col
            unassigned.remove(v)
            result=visit()
            if result is not None: return result
            unassigned.add(v)
            del colors[v]
        return None
    return visit()


def diamond_witnesses(V,E):
    nbr=neighbors(V,E)
    witnesses=[]
    for a,b in sorted(E):
        common=sorted(nbr[a]&nbr[b])
        for u,v in combinations(common,2):
            witnesses.append((a,b,u,v))
    return witnesses


def count_triangles(V,E):
    nbr=neighbors(V,E)
    return sum(len(nbr[u]&nbr[v]) for u,v in E)//3


def report(name,V,E):
    full=has_3_coloring(V,E)
    dels={v:has_3_coloring(V-{v},E) is not None for v in sorted(V)}
    witnesses=diamond_witnesses(V,E)
    return {
      'nombre':name,'vertices':len(V),'aristas':len(E),'triangulos':count_triangles(V,E),
      'testigos_diamante':len(witnesses),'3_coloreable':full is not None,
      'borrando_un_vertice_todos_coloreables':all(dels.values()),
      'borrado_por_vertice':dels,
      'certificado_3col_si_existe':full
    }


def main():
    G5,E5=c5()
    V11,E11=mycielski(G5,E5)
    cases=[report('C5',G5,E5),report('M(C5) o grafo de Grotzsch',V11,E11),report('K4',set(range(4)),set(combinations(range(4),2)))]
    assert cases[0]['3_coloreable']
    assert not cases[1]['3_coloreable'] and cases[1]['triangulos']==0 and cases[1]['testigos_diamante']==0
    assert all(cases[1]['borrado_por_vertice'].values()),'No es vertex-critical segun experimento'
    assert not cases[2]['3_coloreable'] and cases[2]['testigos_diamante']>0
    for case in cases:
        print(case['nombre'], '|V|=',case['vertices'],'|E|=',case['aristas'],
              'triangulos=',case['triangulos'],'diamantes=',case['testigos_diamante'],
              '3-color=',case['3_coloreable'],'cada borrado un vertice admite 3-color=',case['borrando_un_vertice_todos_coloreables'])
    with open('/mnt/data/continuacion_convergencia_2026_10_22/resultados.json','w',encoding='utf-8') as f:
        json.dump(cases,f,indent=2,ensure_ascii=False)
    print('Control completado.')

if __name__=='__main__':main()
