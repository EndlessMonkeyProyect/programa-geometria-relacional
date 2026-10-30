#!/usr/bin/env python3
"""Controles compactos de la solicitud (ed. 30/10/2026).

Python 3, biblioteca estándar. No reemplaza laboratorios históricos ni sus
cotas asintóticas. Produce resultados reproducibles para ejemplos finitos.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).with_name('RESULTADOS_VERIFICACION.json')


def folded(x, length):
    """Distancia exacta a 2L Z, para x y L racionales positivas."""
    t = 2 * length
    y = x % t
    return min(y, t - y)


def colorings(n, edges, k=3):
    for c in itertools.product(range(k), repeat=n):
        if all(c[u] != c[v] for u, v in edges):
            yield c


def boundary(n, edges, B):
    return sorted(set(tuple(c[i] for i in B) for c in colorings(n, edges)))


def canon_partition(p):
    classes = {}
    for i, k in enumerate(p):
        classes.setdefault(k, []).append(i)
    return tuple(sorted(tuple(v) for v in classes.values()))


def all_partitions3(n):
    return sorted(set(canon_partition(a) for a in itertools.product(range(3), repeat=n)
                      if len(set(a)) == 3))


def valid3(parts, edges):
    idx = {}
    for i, part in enumerate(parts):
        for v in part:
            idx[v] = i
    return all(idx[a] != idx[b] for a,b in edges)


def graph_edges(n, code):
    pairs = list(itertools.combinations(range(n), 2))
    return frozenset(p for i,p in enumerate(pairs) if code & (1<<i))


def graph_p3(n, edges, partitions):
    return frozenset(p for p in partitions if valid3(p, edges))


def mycielski(n):
    """M(C_n); vertices: v_i=i, u_i=n+i, w=2n."""
    E=set()
    for i in range(n):
        E.add(tuple(sorted((i,(i+1)%n))))
        E.add(tuple(sorted((n+i,(i-1)%n))))
        E.add(tuple(sorted((n+i,(i+1)%n))))
        E.add((n+i,2*n))
    return frozenset(E)


def bags_myci(n):
    return [frozenset((2*n,0,n,i,n+i,i+1,n+i+1)) for i in range(1,n-1)]


def verify_path_decomp(n):
    edges = mycielski(n)
    bags = bags_myci(n)
    assert set.union(*(set(b) for b in bags)) == set(range(2*n+1))
    for e in edges:
        assert any(set(e) <= b for b in bags), ('edge-not-covered',n,e)
    for v in range(2*n+1):
        indices = [i for i,b in enumerate(bags) if v in b]
        assert indices == list(range(indices[0],indices[-1]+1)), ('interval-failed',n,v)
    assert max(len(b) for b in bags) <= 7
    return len(edges),len(bags),max(len(b) for b in bags)-1


def main():
    a = Fraction(1,4)
    b = Fraction(9,4)
    assert folded(a,1) == folded(b,1) == a
    assert folded(a,2) == a and folded(b,2)==Fraction(7,4)

    # R5, sobre exactamente el mismo conjunto de cuatro vértices.
    # 0=a, 1=b, 2=u, 3=v.
    A={(0,1),(0,2),(0,3),(1,2),(1,3)}
    D={(0,1)}
    assert len(boundary(4,A,(0,1))) == len(boundary(4,D,(0,1))) == 6
    assert boundary(4,A,(0,1)) == boundary(4,D,(0,1))
    assert len(boundary(4,A|{(2,3)},(0,1))) == 0
    assert len(boundary(4,D|{(2,3)},(0,1))) == 6

    # R6, familias sin nombres de color.
    p5=all_partitions3(5)
    Eab={(0,1)}; Ecd={(2,3)}
    assert len(p5)==25
    assert len(graph_p3(5,Eab,p5))==19
    assert len(graph_p3(5,Ecd,p5))==19
    assert len(graph_p3(5,Eab|Ecd,p5))==14

    # Identidad de intersección, y cada diferencia admite un contexto separador.
    p4=all_partitions3(4)
    matrices=[]
    for code in range(1<<6):
        E=graph_edges(4,code)
        matrices.append((E,graph_p3(4,E,p4)))
    tested=0; separating=0
    for E, PE in matrices:
        for F, PF in matrices:
            assert graph_p3(4,E|F,p4)==(PE & PF)
            tested+=1
            if PE != PF:
                p=next(iter(PE ^ PF))
                T=frozenset(tuple(sorted((u,v))) for u in range(4) for v in range(u+1,4)
                            if not any(u in block and v in block for block in p))
                common_E=graph_p3(4,E|T,p4)
                common_F=graph_p3(4,F|T,p4)
                assert (common_E == frozenset({p}) and not common_F) or \
                       (common_F == frozenset({p}) and not common_E)
                separating+=1

    # Estructura de diamante sobre rueda: centro + tres vértices consecutivos.
    for r in range(5,102,2):
        v={0,1,2,r}
        allwheel = {tuple(sorted((i,(i+1)%r))) for i in range(r)}|{(i,r) for i in range(r)}
        edges={e for e in allwheel if set(e)<=v}
        assert len(edges)==5 and len(list(colorings(4,[(sorted(v).index(u), sorted(v).index(w))
                    for u,w in edges])))>0

    myci_cases={r:verify_path_decomp(r) for r in range(5,102,2)}
    assert all(out[2] <=6 for out in myci_cases.values())

    result={
        'version':'2026-10-30-v3-controles-heredados',
        'espejos':{'L1':['1/4','1/4'],'L2':['1/4','7/4']},
        'R5':{'firmas_antes':[6,6],'firmas_despues':[0,6]},
        'R6':{'particiones_5_vertices':25,'un_arista':19,'dos_aristas_disjuntas':14,
              'pares_de_grafos_4_vertices_comprobados':tested,
              'pares_separados_por_contexto':separating},
        'diamantes_ruedas':{'ruedas_comprobadas':49,'r_min':5,'r_max':101},
        'mycielski':{'configuraciones':len(myci_cases),'r_min':min(myci_cases),
                     'r_max':max(myci_cases),'anchura_max':max(x[2] for x in myci_cases.values()),
                     'bolsas_para_M_C5':myci_cases[5][1], 'aristas_para_M_C5':myci_cases[5][0]},
        'alcance':'Controles finitos y estructurales; no recomputa rho(M(C_r)) ni N1-B'
    }
    OUT.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
