#!/usr/bin/env python3
"""Control exhaustivo de T-EXT-01, estándar Python.
Verifica para n=4,6 todos los subconjuntos de A x B y cada consulta D_uv.
Este ensayo finito complementa, pero no reemplaza, la prueba general.
"""
import itertools, json, pathlib, hashlib


def three_colorable(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        if a == b: return False
        adj[a].add(b); adj[b].add(a)
    colors = [-1]*n
    order = sorted(range(n), key=lambda x: (-len(adj[x]), x))
    def backtrack(i):
        if i == n: return True
        v = order[i]
        used = {colors[w] for w in adj[v] if colors[w] >= 0}
        for c in range(3):
            if c not in used:
                colors[v] = c
                if backtrack(i+1): return True
        colors[v] = -1
        return False
    return backtrack(0)

def run(n):
    left = tuple(range(n//2))
    right = tuple(range(n//2, n))
    pairs = list(itertools.product(left, right))
    seen = set(); checks=0
    for mask in range(1 << len(pairs)):
        edges = {p for k, p in enumerate(pairs) if mask & (1 << k)}
        assert three_colorable(n, edges)
        sig = 0
        for k, (u,v) in enumerate(pairs):
            # fresh a,b: ab, au,av,bu,bv
            a,b = n,n+1
            gadget = {(a,b),(a,u),(a,v),(b,u),(b,v)}
            answer = three_colorable(n+2, edges | gadget)
            assert answer == ((u,v) not in edges), (n,mask,u,v)
            checks += 1
            if answer: sig |= 1 << k
        assert sig not in seen
        seen.add(sig)
    return {'n':n, 'left_size':len(left),'right_size':len(right),
            'possible_edges':len(pairs),'graphs_checked':1<<len(pairs),
            'probes_checked':checks,'distinct_response_signatures':len(seen),
            'minimum_signature_bits':len(pairs),'status':'PASS'}

if __name__=='__main__':
    result = {'theorem':'T-EXT-01', 'protocol':'full-vertex boundary; two fresh exterior vertices and five edges',
              'claim':'G union D_uv is 3-colorable iff uv is absent for E subset A x B',
              'tests':[run(4),run(6)]}
    result['total_probes_checked']=sum(t['probes_checked'] for t in result['tests'])
    dest=pathlib.Path(__file__).with_name('RESULTADOS_T_EXT_01.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
