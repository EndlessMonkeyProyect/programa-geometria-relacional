#!/usr/bin/env python3
"""O22: Teselación tetra-octa mediante red D3/FCC, enteros y fracciones.

Python estándar; no introduce dinámica física. Ejecutar: python laboratorio_o22.py
"""
from __future__ import annotations
import itertools
import json
import math
import unittest
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
E=((1,0,0),(0,1,0),(0,0,1))
V0=(0,0,0); A=(1,1,0); B=(1,0,1); C=(0,1,1)
T0=(V0,A,B,C)
Q=(F(4,3),F(4,3),F(4,3))


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def times(k,v):return tuple(k*x for x in v)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dist2(a,b):return dot(sub(a,b),sub(a,b))
def det(a,b,c):return dot(a,(b[1]*c[2]-b[2]*c[1], b[2]*c[0]-b[0]*c[2], b[0]*c[1]-b[1]*c[0]))
def volume_tetra(points):
    p,a,b,c=points
    return F(abs(det(sub(a,p),sub(b,p),sub(c,p))),6)
def centroid(points):return tuple(sum(F(p[i]) for p in points)/len(points) for i in range(3))
def parity(x):return sum(x)%2

def cube_vertices(origin=(0,0,0)):
    return tuple(add(origin,d) for d in itertools.product((0,1),repeat=3))

def tetra_of_cube(origin=(0,0,0)):
    return tuple(v for v in cube_vertices(origin) if parity(v)==0)

def corner_piece(odd_corner,origin=(0,0,0)):
    assert odd_corner in cube_vertices(origin) and parity(odd_corner)==1
    neighbours=tuple(v for v in cube_vertices(origin) if parity(v)==0 and dist2(v,odd_corner)==1)
    assert len(neighbours)==3
    return (odd_corner,*neighbours)

def octa(center):
    assert parity(center)==1
    return tuple(add(center,times(s,e)) for e in E for s in (-1,1))

def barycentric_tetra(p,vertices):
    v,a,b,c=vertices
    d=det(sub(a,v),sub(b,v),sub(c,v))
    assert d!=0
    coeff=(F(det(sub(p,v),sub(b,v),sub(c,v)),d),
           F(det(sub(a,v),sub(p,v),sub(c,v)),d),
           F(det(sub(a,v),sub(b,v),sub(p,v)),d))
    return (1-sum(coeff),*coeff)

def inside_tetra(p,vertices,strict=False):
    b=barycentric_tetra(p,vertices)
    return all(x>0 if strict else x>=0 for x in b)

def octa_contains(p,center,strict=False):
    r=sum(abs(p[i]-center[i]) for i in range(3))
    return r<1 if strict else r<=1

def reflect_across_sum2(p):
    # reflection across the plane x+y+z=2
    shift=F(2*(2-sum(p)),3)
    return tuple(F(x)+shift for x in p)


def verify_cube_partition(origin=(0,0,0),denominator=11):
    tv=tetra_of_cube(origin)
    od=tuple(v for v in cube_vertices(origin) if parity(v)==1)
    pieces=(tv,*(corner_piece(v,origin) for v in od))
    volumes=[volume_tetra(piece) for piece in pieces]
    assert volumes==[F(1,3)]+[F(1,6)]*4
    tested=0;interior=0;boundary=0
    for a,b,c in itertools.product(range(1,denominator),repeat=3):
        p=tuple(origin[i]+F(k,denominator) for i,k in enumerate((a,b,c)))
        cover=[i for i,cell in enumerate(pieces) if inside_tetra(p,cell)]
        strict=[i for i,cell in enumerate(pieces) if inside_tetra(p,cell,strict=True)]
        assert cover, (origin,p)
        assert len(strict)<=1,(origin,p,strict)
        if len(cover)>1:
            assert not strict,(origin,p,cover,strict)
            boundary+=1
        else:interior+=1
        tested+=1
    return dict(volumes=[str(v) for v in volumes],total_volume=str(sum(volumes)),tested=tested,interior=interior,boundary=boundary)


def octant_piece(center, signs):
    return (center,*(add(center,times(s,e)) for s,e in zip(signs,E)))


def verify_octa_partition(center=(1,0,0),denominator=7):
    assert parity(center)==1
    pieces=[octant_piece(center,signs) for signs in itertools.product((-1,1),repeat=3)]
    assert all(volume_tetra(p)==F(1,6) for p in pieces)
    checked=0
    # sphere L1 ball, reduced finite rational grid
    for i,j,k in itertools.product(range(-denominator,denominator+1),repeat=3):
        p=tuple(center[a]+F(v,denominator) for a,v in enumerate((i,j,k)))
        in_octa=octa_contains(p,center)
        cover=[t for t,part in enumerate(pieces) if inside_tetra(p,part)]
        assert in_octa==bool(cover),(p,in_octa,cover)
        checked+=1
    return dict(octa_volume=str(sum(volume_tetra(p) for p in pieces)),tested=checked,octants=8)


def tet_faces(t):
    return tuple(frozenset(x) for x in itertools.combinations(t,3))

def octa_faces(center):
    return tuple(frozenset(add(center,times(s,e)) for s,e in zip(signs,E))
                 for signs in itertools.product((-1,1),repeat=3))


def periodic_face_counts(N):
    # For any N>=4 even, quotient torus (Z/N)^3 of the D3/FCC lattice
    assert N>=4 and N%2==0
    vertices=list(itertools.product(range(N),repeat=3))
    even=[p for p in vertices if parity(p)==0]
    odd=[p for p in vertices if parity(p)==1]
    mod=lambda v: tuple(x%N for x in v)
    tets=[frozenset(mod(q) for q in tetra_of_cube(p)) for p in vertices]
    octas=[frozenset(mod(q) for q in octa(p)) for p in odd]
    assert len(set(tets))==len(tets)
    assert len(set(octas))==len(octas)
    tetra_face_count={}
    octa_face_count={}
    for t in tets:
        for f in tet_faces(tuple(t)):tetra_face_count[f]=tetra_face_count.get(f,0)+1
    for p in odd:
        for f in octa_faces(p):
            f=frozenset(mod(q) for q in f)
            octa_face_count[f]=octa_face_count.get(f,0)+1
    all_faces=set(tetra_face_count)|set(octa_face_count)
    multiplicities={}
    for f in all_faces:
        key=(tetra_face_count.get(f,0),octa_face_count.get(f,0))
        multiplicities[key]=multiplicities.get(key,0)+1
    # faces types (1,1), (2,0) and (0,2), if any
    return dict(N=N, tetra=len(tets), octa=len(octas), vertices=len(even),
                face_multiplicity={str(k):v for k,v in multiplicities.items()},
                tetra_face_count=sum(tetra_face_count.values()),octa_face_count=sum(octa_face_count.values()),
                volume=F(len(tets),3)+F(4*len(octas),3))


class TestO22(unittest.TestCase):
    def test_parity_vertices_regular(self):
        for org in itertools.product(range(-2,3),repeat=3):
            t=tetra_of_cube(org)
            self.assertEqual(len(t),4)
            self.assertEqual({dist2(a,b) for a,b in itertools.combinations(t,2)},{2})
    def test_cell_volumes(self):
        for org in itertools.product((-1,0,1),repeat=3):
            t=tetra_of_cube(org)
            self.assertEqual(volume_tetra(t),F(1,3))
            odds=[v for v in cube_vertices(org) if parity(v)]
            self.assertEqual(sum(volume_tetra(corner_piece(v,org)) for v in odds),F(2,3))
    def test_cube_partition_all_even_odd(self):
        for org in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,1)]:
            self.assertEqual(verify_cube_partition(org,denominator=9)['total_volume'],'1')
    def test_five_cell_shape(self):
        pieces=(tetra_of_cube(),*(corner_piece(p) for p in cube_vertices() if parity(p)))
        self.assertEqual(len(pieces),5)
        self.assertEqual(sum(volume_tetra(p) for p in pieces),1)
    def test_corner_tetra_with_octa(self):
        for w in (p for p in cube_vertices() if parity(p)):
            for p in corner_piece(w):
                self.assertTrue(octa_contains(p,w))
    def test_octa_regular(self):
        for w in [(1,0,0),(1,1,1),(-1,0,0),(2,2,1)]:
            verts=octa(w)
            self.assertEqual(len(set(verts)),6)
            self.assertEqual(sorted({dist2(a,b) for a,b in itertools.combinations(verts,2)}),[2,4])
            self.assertEqual(sum(dist2(a,b)==2 for a,b in itertools.combinations(verts,2)),12)
            self.assertEqual(sum(dist2(a,b)==4 for a,b in itertools.combinations(verts,2)),3)
    def test_octa_is_8_cube_pieces(self):
        self.assertEqual(verify_octa_partition()['octants'],8)
    def test_central_tetra_touches_octa_exactly_one_face(self):
        w=(1,1,1)
        self.assertEqual(frozenset((A,B,C)),octa_faces(w)[0])
        self.assertEqual({sum(p) for p in (A,B,C)},{2})
        self.assertEqual(min(sum(p) for p in octa(w)),2)
        self.assertEqual(max(sum(p) for p in T0),2)
    def test_reflection_is_opposite_face_center(self):
        self.assertEqual(reflect_across_sum2(V0),Q)
        w=(1,1,1)
        opposite=(add(w,E[0]),add(w,E[1]),add(w,E[2]))
        self.assertEqual(centroid(opposite),Q)
        self.assertEqual({sum(p) for p in opposite},{4})
    def test_reflection_tetra_is_within_octa(self):
        w=(1,1,1)
        self.assertTrue(octa_contains(Q,w))
        # entire convex reflected tetra within convex octa
        for p in (A,B,C,Q):self.assertTrue(octa_contains(p,w))
        self.assertEqual(volume_tetra((A,B,C,Q)),F(1,3))
    def test_fifth_reflection_not_lattice_vertex(self):
        self.assertTrue(all(x.denominator==3 for x in Q))
        self.assertNotIn(Q,octa((1,1,1)))
    def test_face_vs_lattice_distinct_local_options(self):
        self.assertEqual({dist2(p,Q) for p in (A,B,C)},{F(2)})
        octa_center=(1,1,1)
        self.assertEqual(len(octa_faces(octa_center)),8)
        self.assertEqual(len(tet_faces(T0)),4)
    def test_growing_shell_ratio(self):
        center=centroid(T0)
        self.assertEqual(center,(F(1,2),)*3)
        self.assertEqual(dist2(center,Q),F(25,12))
        self.assertEqual(dist2(center,V0),F(3,4))
        self.assertEqual(dist2(center,Q)/dist2(center,V0),F(25,9))
    def test_face_dihedral_complement(self):
        self.assertAlmostEqual(math.acos(F(1,3))+math.acos(F(-1,3)),math.pi)
    def test_cube_8_tets_4_oct_contrib(self):
        # unit cube contains 1 tetra and four 1/8-octa sectors
        self.assertEqual(F(1,3)+4*F(1,6),1)
        self.assertEqual(8*F(1,6),F(4,3))
    def test_local_origin_vertex_incidence(self):
        p=(0,0,0)
        around=[add(p,t) for t in itertools.product((-1,0),repeat=3)]
        self.assertEqual(sum(p in tetra_of_cube(x) for x in around),8)
        octacenters=[add(p,times(s,e)) for e in E for s in (-1,1)]
        self.assertEqual(len(octacenters),6)
        self.assertTrue(all(parity(w)==1 and p in octa(w) for w in octacenters))
    def test_face_pairing_global(self):
        for N in (4,6):
            res=periodic_face_counts(N)
            self.assertEqual(res['face_multiplicity'],{'(1, 1)':4*N**3})
            self.assertEqual(res['volume'],N**3)
            self.assertEqual(res['tetra'],N**3)
            self.assertEqual(res['octa'],N**3//2)
    def test_volume_fraction_one_third_two_thirds(self):
        for N in (4,6):
            data=periodic_face_counts(N)
            self.assertEqual(F(data['tetra'],3),F(N**3,3))
            self.assertEqual(F(data['octa']*4,3),F(2*N**3,3))
    def test_fcc_translation_symmetry(self):
        for o in itertools.product(range(-1,2),repeat=3):
            for p in T0:
                self.assertEqual(parity(add(o,p)),parity(o))
    def test_internal_midpoint_octa_scale(self):
        ms=[tuple(F(a[i]+b[i],2) for i in range(3)) for a,b in itertools.combinations(T0,2)]
        edges=[dist2(a,b) for a,b in itertools.combinations(ms,2)]
        self.assertEqual(edges.count(F(1,2)),12)
        self.assertEqual(edges.count(F(1)),3)
        self.assertEqual(F(2),F(1,2)*4)
    def test_equivariant_under_cube_coordinate_rotations(self):
        # transform coordinates with permutations, preserving cube and lattice
        ts=set(tetra_of_cube())
        for pi in itertools.permutations((0,1,2)):
            mapped={tuple(v[i] for i in pi) for v in ts}
            self.assertEqual(mapped,ts)
    def test_no_independent_new_distances_for_matching_octa(self):
        F_points=(A,B,C)
        w=(1,1,1)
        self.assertEqual({dist2(p,q) for p,q in itertools.combinations(octa(w),2)}, {2,4})
        self.assertEqual({dist2(p,q) for p,q in itertools.combinations(F_points,2)}, {2})
    def test_all_four_tetra_faces_have_unique_octa_neighbour(self):
        for face in tet_faces(T0):
            eligible=[w for w in cube_vertices() if parity(w)==1 and face in octa_faces(w)]
            self.assertEqual(len(eligible),1)
        self.assertEqual(len({w for face in tet_faces(T0) for w in cube_vertices()
                              if parity(w)==1 and face in octa_faces(w)}),4)
    def test_edge_incidence_two_tetra_two_octa(self):
        p=(0,0,0);q=(1,1,0)
        cubes=[o for o in itertools.product((-1,0,1),repeat=3)
               if {p,q}.issubset(set(tetra_of_cube(o)))]
        self.assertEqual(len(cubes),2)
        centers=[w for w in itertools.product(range(-1,3),repeat=3)
                 if parity(w)==1 and {p,q}.issubset(set(octa(w)))]
        self.assertEqual(len(centers),2)
        self.assertAlmostEqual(2*math.acos(F(1,3))+2*math.acos(F(-1,3)),2*math.pi)
    def test_translation_cannot_fix_a_global_point(self):
        f=(F(1,2),F(1,2),F(1,2));t=(1,1,0)
        self.assertEqual(parity(t),0)
        self.assertNotEqual(add(f,t),f)
    def test_topology_and_dimensional_units(self):
        t=tetra_of_cube()
        self.assertEqual(len(t),4)
        self.assertEqual(len(set(sum((list(p) for p in t),[]))),2)
        self.assertEqual(len(octa((1,1,1))),6)


def results():
    cube=verify_cube_partition(denominator=13)
    cube_odd=verify_cube_partition((1,0,0),denominator=13)
    o=verify_octa_partition(denominator=8)
    torus=periodic_face_counts(4)
    c0=centroid(T0)
    return {
        'model':'Z3 even-parity lattice (D3/FCC) with tetrahedral Delaunay cells and octahedral complement',
        'base_tetra_vertices':T0,'base_tetra_center':[str(x) for x in c0],
        'tetra_edge_squared':'2','tetra_volume':'1/3',
        'octa_center':(1,1,1),'octa_vertices':octa((1,1,1)),'octa_volume':'4/3',
        'cube_partition_even':cube,'cube_partition_odd':cube_odd,
        'octa_partition':o,'periodic_torus_4':{k:str(v) if isinstance(v,F) else v for k,v in torus.items()},
        'reflected_vertex':[str(x) for x in Q],
        'opposite_octa_face':[(2,1,1),(1,2,1),(1,1,2)],
        'reflection_equals_opposite_face_centroid':centroid(((2,1,1),(1,2,1),(1,1,2)))==Q,
        'tiled_volume_fraction_tetra':'1/3','tiled_volume_fraction_octa':'2/3',
        'local_vertex_incidence':{'tetra':8,'octa':6},
        'epistemic_limit':'requires a Euclidean metric, uniform edge scale, parity lattice and global face-to-face continuation; not physical dynamics'
    }

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestO22)
    outcome=unittest.TextTestRunner(verbosity=2).run(suite)
    if outcome.wasSuccessful():
        HERE.joinpath('RESULTADOS_O22.json').write_text(json.dumps(results(),indent=2,ensure_ascii=False)+'\n',encoding='utf8')
        HERE.joinpath('PRUEBAS_EJECUTADAS.txt').write_text(f'O22: {outcome.testsRun} pruebas superadas; fallos=0; errores=0\n',encoding='utf8')
    raise SystemExit(0 if outcome.wasSuccessful() else 1)
