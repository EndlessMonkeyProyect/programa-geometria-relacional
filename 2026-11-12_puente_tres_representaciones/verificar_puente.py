#!/usr/bin/env python3
"""Puente local exacto entre una firma canónica, SWAP y deformación Cauchy.
No reproduce algoritmos completos de Anthropic ni OpenAI.
"""
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as sp

BASE=Path(__file__).resolve().parent
BITS=list(product([0,1], repeat=3))
Q=list(product([None,0,1],repeat=3))
F_CLAUSES=((1,2,-3),(1,-2,3),(-1,2,3),(-1,-2,-3),(1,2,3))

def sat_clause(x,cl):
    return any(x[abs(i)-1]==(1 if i>0 else 0) for i in cl)

def f_star(x):
    return int(all(sat_clause(x,c) for c in F_CLAUSES))

def f_alt(x):
    return int(x[0]==0 and not(x[1]==1 and x[2]==1))

def pin(p,y):
    return int(all(v is None or v==y[i] for i,v in enumerate(p)))

def truth_vector(f):
    return sp.Matrix([f(x) for x in BITS])

F=truth_vector(f_star)
Falt=truth_vector(f_alt)
assert sum(F)==3 and sum(Falt)==3 and F!=Falt
assert [x for x in BITS if f_star(x)]==[(0,1,1),(1,0,1),(1,1,0)]

# Anthropic style: SWAP acting on first two indices, identity on third.
S=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
Pm=sp.Matrix([[0,0,0,0],[0,sp.Rational(1,2),-sp.Rational(1,2),0],
              [0,-sp.Rational(1,2),sp.Rational(1,2),0],[0,0,0,0]])
assert S==sp.eye(4)-2*Pm
S3=sp.kronecker_product(S,sp.eye(2))
# Reorder input column vector so row y uses f(y), after swapped wire.
P=sp.zeros(8)
for i,x in enumerate(BITS):
    xp=(x[1],x[0],x[2])
    P[i,BITS.index(xp)]=1
assert S3*P==sp.eye(8)
SA=sp.kronecker_product(sp.eye(4)-2*Pm,sp.eye(2))*P
assert SA==sp.eye(8)

# OpenAI Cauchy polynomial local W(T) with packets of L=2; two packets (4 ports incl dummy).
T=sp.symbols('T')
L=2
C=sp.prod(T-z for z in range(-L,L))
Cp0=sp.diff(C,T).subs(T,0)
W2=sp.Matrix(2,2,lambda i,j:sp.cancel(C/(Cp0*(T-(j-i)))))
W4=sp.diag(W2,W2)
assert W4.subs(T,0)==sp.eye(4)

def ell(bit,z):
    return z if bit else 1-z

# Canonical 8x8 kernel K(T) on padded assignment x3=0 (0-based fourth position).
def pad(x):
    return x+(0,)

def kernel_at(t):
    w=W4.subs(T,t)
    m=sp.zeros(8)
    for j,x in enumerate(BITS):
        wx=w*sp.Matrix(pad(x))
        for i,y in enumerate(BITS):
            m[i,j]=sp.prod(ell(pad(y)[k],wx[k]) for k in range(4))
    return m

assert kernel_at(0)==sp.eye(8)
# Each factor has degree <=3, 4 factors => deg(K_ij)<=12.
DEGREE=4*(2*L-1)
NODES=list(range(1, DEGREE+2)) # 1,...,13
# Lagrange weights at zero for consecutive nodes: (-1)^(t-1) binom(13,t).
WEIGHTS=[(-1)**(t-1)*comb(len(NODES),t) for t in NODES]
assert sum(WEIGHTS)==1
M=sp.zeros(8)
matrices=[]
for t,w in zip(NODES,WEIGHTS):
    mat=kernel_at(t)
    matrices.append(mat)
    M+=w*mat
assert M==sp.eye(8)
assert M*F==SA*F==F
assert M*Falt==SA*Falt==Falt

# Recover 27 partial-pinned counts, not just total count.
counts_star=[]
counts_alt=[]
for p in Q:
    sel=sp.Matrix([[pin(p,y) for y in BITS]])
    expected=int((sel*F)[0])
    recovered=int((sel*M*F)[0])
    swap=int((sel*SA*F)[0])
    assert expected==recovered==swap
    counts_star.append({'pin': ''.join('-' if k is None else str(k) for k in p), 'count':expected})
    alt=int((sel*Falt)[0])
    assert alt==int((sel*M*Falt)[0])
    counts_alt.append(alt)

# Refinement property across every partial assignment.
lookup={row['pin']:row['count'] for row in counts_star}
for p in Q:
    for i,v in enumerate(p):
        if v is None:
            p0=list(p);p0[i]=0
            p1=list(p);p1[i]=1
            key=lambda a:''.join('-' if k is None else str(k) for k in a)
            assert lookup[key(p)]==lookup[key(p0)]+lookup[key(p1)]

# Stronger non-injectivity of scalar query: F_star and F_alt count both 3,
# but one query (x1=0) yields 1 vs 3.
p=(0,None,None)
assert sum(f_star(x)*pin(p,x) for x in BITS)==1
assert sum(f_alt(x)*pin(p,x) for x in BITS)==3

# One independent symbolic entry confirms degree bound locally.
Kpoly00=sp.expand(sp.prod(ell(pad(BITS[0])[k],(W4*sp.Matrix(pad(BITS[-1])))[k]) for k in range(4)))
assert sp.degree(Kpoly00,T)<=DEGREE

ranks=[int(m.rank()) for m in matrices]
max_abs=max(abs(int(z)) for m in matrices for z in m)
res={
 'hypotheses':'3 variables, all 27 partial pin queries, exact rationals; local SWAP and 2x Cauchy packets of length 2',
 'common_formula':{'solutions':[''.join(map(str,x)) for x in BITS if f_star(x)], 'Z':int(sum(F))},
 'Anthropic_local':{'SWAP=I-2Pminus':True,'8x8_bridge_S3P=I':bool(SA==sp.eye(8))},
 'OpenAI_local':{'packet_length':L,'packet_count':2,'padded_ports':4,'W2':[[str(z) for z in row] for row in W2.tolist()], 'W4_at_0_is_I':True,'K_polynomial_degree_bound':DEGREE,'interpolation_nodes':NODES,'interpolation_weights':WEIGHTS,'sum_weighted_kernel_is_I8':True,'ranks_of_Kt':ranks,'max_abs_kernel_entry':str(max_abs)},
 'full_27_query_family':{'all_exact':True,'counts':[z for z in counts_star],'all_refinement_identities':True},
 'scalar_noninjectivity':{'F_star_Z':3,'F_alt_Z':3,'partial_pin':'0--','F_star_pinned_Z':1,'F_alt_pinned_Z':3},
 'cost_accounting':{'number_of_output_memberships':8,'number_of_partial_pin_queries':27,'number_of_auxiliary_evaluations':13,'kernel_size_per_evaluation':'8 x 8','dense_arithmetic_upper_bound_entry_products':13*8*8},
 'status':'Local exact bridge for operator-valued signatures; no subexponential algorithm equivalence.'
}
(BASE/'resultados_puente.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print('OK: S3 P = I8, sum_t w_t K_t = I8, all 27 pinned counts exact; ranks:',ranks)
print('Count Fstar 3, Falt 3; pinned 0-- differs 1 vs 3')
print('Bounds: 13 evaluations of 8x8 auxiliary kernels, polynomial degree <=12')
