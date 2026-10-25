#!/usr/bin/env python3
"""O23 — contratos mínimos sobre una interfaz triangular.

Toda la geometría se evalúa con fracciones exactas; sin bibliotecas externas.
Ejecutar: python laboratorio_o23.py  / python -m unittest laboratorio_o23 -v
"""
from __future__ import annotations
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
P0=(0,0,0)
A=(1,1,0);B=(1,0,1);C=(0,1,1)
T0=(P0,A,B,C)
FACE=(A,B,C)


def vec_add(a,b): return tuple(F(x)+F(y) for x,y in zip(a,b))
def vec_sub(a,b): return tuple(F(x)-F(y) for x,y in zip(a,b))
def scale(s,a): return tuple(F(s)*F(x) for x in a)
def dot(a,b): return sum(F(x)*F(y) for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dist2(a,b):return dot(vec_sub(a,b),vec_sub(a,b))
def centroid(pts):return tuple(sum(F(p[i]) for p in pts)/len(pts) for i in range(3))
def determinant(a,b,c):return dot(a,cross(b,c))
def tetra_volume(pts):
    p,a,b,c=pts
    return abs(determinant(vec_sub(a,p),vec_sub(b,p),vec_sub(c,p)))/6

def face_opposite_tetra_apex(apex,face):
    assert len(face)==3
    center=centroid(face)
    normal=cross(vec_sub(face[1],face[0]),vec_sub(face[2],face[0]))
    rel=vec_sub(apex,center)
    assert dot(normal,normal)!=0
    return vec_sub(apex,scale(2*dot(rel,normal)/dot(normal,normal),normal))

def continue_cell(apex,face,kind):
    """Ambas continuaciones usan cara y q; la especie fija las demás referencias."""
    assert kind in ('tetra','octa')
    face=tuple(face)
    c=centroid(face)
    q=face_opposite_tetra_apex(apex,face)
    if kind=='tetra':
        vertices=(*face,q)
    else:
        w=scale(F(1,2),vec_add(c,q))
        vertices=(*face,*(vec_sub(scale(2,w),p) for p in face))
    return {'kind':kind,'face':face,'fifth':q,'vertices':vertices,
            'center':centroid(vertices),'remote_center':q,
            'volume':tetra_volume(vertices) if kind=='tetra' else 4*tetra_volume((*face,q))}

def edges_squared(vertices):
    return [dist2(a,b) for a,b in combinations(vertices,2)]

def triangle_port_signature(face):
    return tuple(sorted(dist2(a,b) for a,b in combinations(face,2)))

def transform(point, s=F(1), shift=(0,0,0), axis_perm=(0,1,2), flips=(1,1,1)):
    return tuple(F(shift[i])+F(s)*F(flips[i])*F(point[axis_perm[i]]) for i in range(3))

def construct_face_map(N):
    """Grafo dual de la red tetra–octa sobre un toro N par, N>=4."""
    assert N>=4 and N%2==0
    mod=lambda p:tuple(x%N for x in p)
    groups=defaultdict(list)
    types={}
    for origin in product(range(N),repeat=3):
        # v even a paridad global fija
        vs=tuple(tuple(origin[i]+delta[i] for i in range(3)) for delta in product((0,1),repeat=3))
        vertices=[tuple(v) for v in vs if sum(v)%2==0]
        assert len(vertices)==4
        label=('T',)+origin
        types[label]='T'
        for face in combinations(vertices,3):
            groups[frozenset(map(mod,face))].append(label)
    for center in product(range(N),repeat=3):
        if sum(center)%2==0:continue
        label=('O',)+center
        types[label]='O'
        for signs in product((-1,1),repeat=3):
            face=[tuple(center[i]+signs[i]*(j==i) for i in range(3)) for j in range(3)]
            groups[frozenset(map(mod,face))].append(label)
    graph={x:set() for x in types}
    for face,cells in groups.items():
        assert len(face)==3 and len(cells)==2,(face,cells)
        a,b=cells
        assert types[a]!=types[b]
        graph[a].add(b);graph[b].add(a)
    return graph,types,groups

def two_colour_propagation(graph,initial):
    out={initial:0}
    queue=deque([initial])
    while queue:
        a=queue.popleft()
        for b in graph[a]:
            needed=1-out[a]
            if b in out:
                if out[b]!=needed:raise ValueError('Ciclo impar: contrato de alternancia incompatible')
            else:
                out[b]=needed;queue.append(b)
    if len(out)!=len(graph):raise ValueError('Grafo no conectado: precisa referencia por componente')
    return out


def results():
    t=continue_cell(P0,FACE,'tetra')
    o=continue_cell(P0,FACE,'octa')
    g4,types4,faces4=construct_face_map(4)
    assignments=two_colour_propagation(g4,('T',0,0,0))
    return {
        'quinta_referencia':list(map(str,t['fifth'])),
        'coincidencia_F_y_q':t['face']==o['face'] and t['fifth']==o['fifth'],
        'papel_q_tetra':'vertice_extremo',
        'papel_q_octa':'centroide_de_cara_opuesta',
        'volumen_tetra':str(t['volume']),
        'volumen_octa':str(o['volume']),
        'relacion_volumen':str(o['volume']/t['volume']),
        'cantidad_continuaciones_con_misma_F_y_q':2,
        'test_estructural_minimo': 'q pertenece al conjunto de vertices estructurales',
        'red_periodica_N4': {'celulas':len(g4),'caras':len(faces4), 'T':sum(v=='T' for v in types4.values()),'O':sum(v=='O' for v in types4.values()),'coloreadas':len(assignments)}
    }


class TestO23(unittest.TestCase):
    def setUp(self):
        self.t=continue_cell(P0,FACE,'tetra')
        self.o=continue_cell(P0,FACE,'octa')
    def test_common_metric(self):self.assertEqual(triangle_port_signature(FACE),(2,2,2))
    def test_fifth_reflection(self):self.assertEqual(self.t['fifth'],(F(4,3),)*3)
    def test_equal_face_and_fifth(self):
        self.assertEqual(self.t['face'],self.o['face']);self.assertEqual(self.t['fifth'],self.o['fifth'])
    def test_tetra_regular(self):self.assertEqual(set(edges_squared(self.t['vertices'])),{2})
    def test_octa_regular(self):
        self.assertEqual(edges_squared(self.o['vertices']).count(2),12)
        self.assertEqual(edges_squared(self.o['vertices']).count(4),3)
    def test_octa_far_face_centroid(self):self.assertEqual(centroid(self.o['vertices'][3:]),self.t['fifth'])
    def test_octa_center(self):self.assertEqual(self.o['center'],(1,1,1))
    def test_tetra_center(self):self.assertEqual(self.t['center'],(F(5,6),)*3)
    def test_q_tetra_vertex(self):self.assertIn(self.t['fifth'],self.t['vertices'])
    def test_q_octa_not_vertex(self):self.assertNotIn(self.o['fifth'],self.o['vertices'])
    def test_fifth_mean_is_octa_face_interior(self):
        far=self.o['vertices'][3:]
        self.assertEqual(self.o['fifth'],centroid(far))
        self.assertTrue(all(p!=self.o['fifth'] for p in far))
    def test_volumes(self):self.assertEqual((self.t['volume'],self.o['volume']),(F(1,3),F(4,3)))
    def test_fourfold_ratio(self):self.assertEqual(self.o['volume']/self.t['volume'],4)
    def test_all_four_faces(self):
        for apex in T0:
            face=tuple(v for v in T0 if v!=apex)
            t=continue_cell(apex,face,'tetra');o=continue_cell(apex,face,'octa')
            self.assertEqual(t['fifth'],o['fifth'])
            self.assertEqual(set(edges_squared(t['vertices'])),{2})
            self.assertEqual(edges_squared(o['vertices']).count(2),12)
            self.assertEqual(o['volume']/t['volume'],4)
            self.assertNotIn(t['fifth'],o['vertices'])
    def test_face_vertex_permutations(self):
        for ordered_face in permutations(FACE):
            t=continue_cell(P0,ordered_face,'tetra')
            o=continue_cell(P0,ordered_face,'octa')
            self.assertEqual(t['fifth'],self.t['fifth'])
            self.assertEqual(set(o['vertices']),set(self.o['vertices']))
    def test_affine_similarity_covariance(self):
        for s in (F(1,3),F(1),F(3,2),F(5)):
            for shift in ((0,0,0),(3,-2,5)):
                for axis_perm in permutations((0,1,2)):
                    for flips in ((1,1,1),(-1,1,1),(1,-1,-1)):
                        tx=lambda p:transform(p,s,shift,axis_perm,flips)
                        face=tuple(map(tx,FACE))
                        for kind in ('tetra','octa'):
                            c=continue_cell(tx(P0),face,kind)
                            original=self.t if kind=='tetra' else self.o
                            self.assertEqual(c['fifth'],tx(original['fifth']))
                            self.assertEqual(set(c['vertices']),set(map(tx,original['vertices'])))
                            self.assertEqual(c['volume'],s**3*original['volume'])
    def test_irregular_rescaling_breaks_metric(self):
        f=[(2*p[0],p[1],p[2]) for p in FACE]
        self.assertNotEqual(len(set(triangle_port_signature(f))),1)
    def test_oct_tet_distinction_not_in_port(self):
        # misma lectura geométrica, consulta posterior diferente
        self.assertEqual((triangle_port_signature(FACE),self.t['fifth']),
                         (triangle_port_signature(FACE),self.o['fifth']))
        self.assertNotEqual(self.t['fifth'] in self.t['vertices'],self.o['fifth'] in self.o['vertices'])
    def test_network_n4(self):
        g,t,f=construct_face_map(4)
        self.assertEqual(len(g),96);self.assertEqual(len(f),256)
        self.assertEqual(sum(x=='T' for x in t.values()),64)
        self.assertEqual(sum(x=='O' for x in t.values()),32)
        self.assertTrue(all(len(g[x])== (4 if t[x]=='T' else 8) for x in g))
    def test_network_n6(self):
        g,t,f=construct_face_map(6)
        self.assertEqual(len(g),324);self.assertEqual(len(f),864)
        self.assertTrue(all(t[x]!=t[y] for x in g for y in g[x]))
    def test_bipartite_global_reconstruct(self):
        for N in (4,6):
            g,t,_=construct_face_map(N)
            colors=two_colour_propagation(g,next(x for x in g if t[x]=='T'))
            self.assertEqual(len(colors),len(g))
            self.assertEqual({colors[x] for x in g if t[x]=='T'},{0})
            self.assertEqual({colors[x] for x in g if t[x]=='O'},{1})
    def test_odd_cycle_not_compatible(self):
        with self.assertRaises(ValueError):two_colour_propagation({'a':{'b','c'},'b':{'a','c'},'c':{'a','b'}},'a')
    def test_even_cycle_compatible(self):
        cycle={i:{(i-1)%4,(i+1)%4} for i in range(4)}
        self.assertEqual(two_colour_propagation(cycle,0),{0:0,1:1,2:0,3:1})
    def test_missing_initial_class_two_solutions(self):
        g,_,_=construct_face_map(4)
        c=two_colour_propagation(g,('T',0,0,0))
        self.assertNotEqual(c,{k:1-v for k,v in c.items()})
    def test_scale_contract_requires_same_length(self):
        # para empalmar caras isométricamente, escalas locales iguales
        a=triangle_port_signature(FACE)
        b=triangle_port_signature(tuple(scale(F(3,2),p) for p in FACE))
        self.assertNotEqual(a,b)
        self.assertEqual(b,tuple(F(9,4)*x for x in a))
    def test_midpoint_oct_requires_scale_two_and_new_placement(self):
        # O21: los seis puntos medios de aristas de K4 forman octaedro a escala a/2.
        mids=tuple(scale(F(1,2),vec_add(p,q)) for p,q in combinations(T0,2))
        self.assertEqual(edges_squared(mids).count(F(1,2)),12)
        center=centroid(mids)
        scaled=tuple(vec_add(center,scale(2,vec_sub(m,center))) for m in mids)
        self.assertEqual(edges_squared(scaled).count(2),12)
        self.assertEqual(centroid(scaled),center)
        self.assertNotEqual(center,self.o['center'])
    def test_results_json_reproduced(self):
        r=results();self.assertTrue(r['coincidencia_F_y_q']);self.assertEqual(r['relacion_volumen'],'4')


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestO23)
    run=unittest.TextTestRunner(verbosity=2).run(suite)
    if run.wasSuccessful():
        (HERE/'RESULTADOS_O23.json').write_text(json.dumps(results(),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    raise SystemExit(0 if run.wasSuccessful() else 1)
