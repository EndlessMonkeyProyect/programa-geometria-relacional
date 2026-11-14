#!/usr/bin/env python3
"""Auditoría reducida, aritmética entera exacta y sin dependencias externas.

A: identidad octoniónica de ocho cuadrados (Anthropic, hexagon:2610.00577v1)
   y sus dos cortes con signos; transporte de los primeros momentos.
B: recuperación Hasse/Hermite con 3 nodos x 2 datos y coeficientes jet,
   imitando el esquema algebraico del artículo OpenAI, NO sus formas de sustitución.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

DIR=Path(__file__).resolve().parent
ZERO=(0,0,0)
ONE=(1,0,0)

def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def scale(k,a):return tuple(k*v for v in a)
def mul(a,b):return (a[0]*b[0], a[0]*b[1]+a[1]*b[0], a[0]*b[2]+a[1]*b[1]+a[2]*b[0])
def jet(n):return (1,n,comb(n,2))  # (1+u)^n mod u^3

def conj(a):
    if len(a)==1:return a
    half=len(a)//2
    return conj(a[:half])+tuple(-v for v in a[half:])
def cayley_dickson(a,b):
    if len(a)==1:return (a[0]*b[0],)
    half=len(a)//2
    x,y=a[:half],a[half:]
    c,d=b[:half],b[half:]
    ac=cayley_dickson(x,c)
    bd=cayley_dickson(conj(d),y)
    dx=cayley_dickson(d,x)
    ybc=cayley_dickson(y,conj(c))
    return tuple(p-q for p,q in zip(ac,bd))+tuple(p+q for p,q in zip(dx,ybc))

def signs():
    basis=[tuple(int(i==j) for i in range(8)) for j in range(8)]
    result={}
    for a,b in product(range(8),repeat=2):
        p=cayley_dickson(basis[a],basis[b])
        assert sum(v!=0 for v in p)==1 and p[a^b] in (-1,1)
        result[(a,b)]=p[a^b]
    return result

def exact_rank(M):
    A=[[Fraction(v) for v in row] for row in M]
    h=len(A); w=len(A[0]); r=0
    for c in range(w):
        p=next((i for i in range(r,h) if A[i][c]),None)
        if p is None: continue
        A[p],A[r]=A[r],A[p]
        inv=A[r][c]
        A[r]=[v/inv for v in A[r]]
        for i in range(r+1,h):
            t=A[i][c]
            if t:
                A[i]=[A[i][j]-t*A[r][j] for j in range(w)]
        r+=1
        if r==h:break
    return r

class Ops:
    def __init__(self): self.adds=0;self.mults=0
    def add(self,a,b):self.adds+=3;return add(a,b)
    def mul(self,a,b):self.mults+=6;self.adds+=3;return mul(a,b)
    def as_dict(self):return {'scalar_additions':self.adds,'scalar_multiplications':self.mults,'total':self.adds+self.mults}

def moments(a):return [a[0],a[1],a[1]+2*a[2]]

def check_anthropic():
    s=signs(); cuts={'R_row':[],'C_row':[],'R_col':[],'C_col':[]}
    nonzero=Counter(); negative=Counter(); total=[ZERO,ZERO,ZERO]
    dense_ops=Ops()
    # Exact identity evaluated at all 8^4=4096 inputs.
    for x,y,u,v in product(range(8),repeat=4):
        parity=(x^y^u^v)==0
        cross=(x==v and y==u)
        r=int(parity)*s[x,y]*s[v,u]
        c=int(parity)*s[x,u]*s[v,y]
        assert r+c==2*int(cross),(x,y,u,v)
        if parity:
            for term,sign,ab,cd in [(1,r,(x,y),(u,v)),(2,c,(x,u),(y,v))]:
                nonzero[term]+=1
                if sign==-1: negative[term]+=1
                left=jet(ab[0].bit_count()+ab[1].bit_count())
                right=jet(cd[0].bit_count()+cd[1].bit_count())
                p=dense_ops.mul(left,right)
                total[term]=dense_ops.add(total[term],scale(sign,p))
        # Weights on true crossings only (for direct independent check).
        if cross:
            w=sum(i.bit_count() for i in (x,y,u,v))
            total[0]=add(total[0],scale(2,jet(w)))
    assert total[0]==add(total[1],total[2])
    assert moments(total[0])==[128,768,5376]
    # Matrices in the two index arrangements: (x,y)|(u,v) and (x,u)|(y,v).
    for label in ('R_row','C_row','R_col','C_col'):
        M=[]
        for a,b in product(range(8), repeat=2):
            row=[]
            for c,d in product(range(8), repeat=2):
                if label.endswith('row'):x,y,u,v=a,b,c,d
                else:x,u,y,v=a,b,c,d
                parity=int((x^y^u^v)==0)
                row.append(parity*(s[x,y]*s[v,u] if label.startswith('R') else s[x,u]*s[v,y]))
            M.append(row)
        cuts[label]=M
    ranks={k:exact_rank(M) for k,M in cuts.items()}
    assert ranks=={'R_row':8,'C_row':64,'R_col':64,'C_col':8},ranks
    uniques={k:len({tuple(row) for row in M}) for k,M in cuts.items()}
    assert uniques['R_row']==uniques['C_col']==16
    # Group by XOR of endpoints and an integer sign in each compatible orientation.
    compressed_ops=Ops(); grouped=[]
    for direction in ['R_row','C_col']:
        # In either favorable cut the factors are sigma(a,b) and sigma(d,c).
        left=[ZERO]*8; right=[ZERO]*8
        for a,b in product(range(8),repeat=2):
            key=a^b
            left[key]=compressed_ops.add(left[key],scale(s[a,b],jet(a.bit_count()+b.bit_count())))
        for c,d in product(range(8),repeat=2):
            key=c^d
            right[key]=compressed_ops.add(right[key],scale(s[d,c],jet(c.bit_count()+d.bit_count())))
        out=ZERO
        for key in range(8):
            out=compressed_ops.add(out,compressed_ops.mul(left[key],right[key]))
        assert out==total[1 if direction=='R_row' else 2],(direction,out,total)
        grouped.append({'cut':direction,'eight_block_moments':moments(out),'input_states_each_side':64,'xor_classes':8})
    return {
        'article_identity':'2 [x=v][y=u] = [x xor y xor u xor v=0]*(sigma(x,y)sigma(v,u)+sigma(x,u)sigma(v,y))',
        'combinations_checked':8**4,
        'ranks_exact_rational':ranks,
        'unique_signed_row_vectors':uniques,
        'signed_terms_parity_nonzero':{'R':nonzero[1],'C':nonzero[2]},
        'negative_entries':{'R':negative[1],'C':negative[2]},
        'weighted_jet_terms':[list(v) for v in total],
        'moments_target_and_terms':[moments(v) for v in total],
        'factorized':grouped,
        'direct_pruned_operations':dense_ops.as_dict(),
        'factorized_operations':compressed_ops.as_dict(),
        'excluded_from_count':'XOR, sigma-table, sign negations, recognition and cache, bit-level costs; this is a local toy comparison, not running time for the Anthropic recursion.'
    }

def gauss_solve(matrix,rhs):
    n=len(rhs)
    A=[[Fraction(v) for v in row]+[Fraction(rhs[i])] for i,row in enumerate(matrix)]
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]),None)
        assert p is not None, 'singular'
        A[p],A[c]=A[c],A[p]
        z=A[c][c]
        A[c]=[v/z for v in A[c]]
        for i in range(n):
            if i==c:continue
            f=A[i][c]
            if f:A[i]=[a-f*b for a,b in zip(A[i],A[c])]
    return [A[i][-1] for i in range(n)]

def hs_jet(n,clauses,t):
    # Variable elimination with first order Hasse/Taylor in z and second in u.
    # Based on local factors (1+u)^x(1+(t+z)x), with clauses as Boolean factors.
    # No complete solution enumeration in this calculation.
    z=(ZERO,ZERO)
    unit=(ONE,ZERO)
    def tang_add(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
    def tang_mult(a,b):return (mul(a[0],b[0]),add(mul(a[0],b[1]),mul(a[1],b[0])))
    def table_val(scope, tab, env):return tab[tuple(env[i] for i in scope)]
    factors=[]
    for i in range(n):
        factors.append(((i,),{(0,):unit,(1,):(scale(1+t,jet(1)),jet(1))}))
    for clause in clauses:
        scope=tuple(sorted({abs(v)-1 for v in clause}))
        tab={}
        for bits in product((0,1),repeat=len(scope)):
            env=dict(zip(scope,bits))
            ok=any(env[abs(v)-1]==int(v>0) for v in clause)
            tab[bits]=unit if ok else z
        factors.append((scope,tab))
    for v in range(n):
        chosen=[f for f in factors if v in f[0]]
        factors=[f for f in factors if v not in f[0]]
        rem=tuple(sorted(set().union(*(set(f[0]) for f in chosen))-{v}))
        tab={}
        for assignment in product((0,1),repeat=len(rem)):
            env=dict(zip(rem,assignment));value=z
            for bit in (0,1):
                env[v]=bit
                cur=table_val(chosen[0][0],chosen[0][1],env)
                for f in chosen[1:]:cur=tang_mult(cur,table_val(f[0],f[1],env))
                value=tang_add(value,cur)
            tab[assignment]=value
        factors.append((rem,tab))
    assert all(scope==() for scope,tab in factors)
    out=unit
    for scope,tab in factors:out=tang_mult(out,tab[()])
    return out

def check_openai():
    # A degree <= 5 synthetic deformation: faithful to the mathematical Hasse
    # data interface, not OpenAI's specialized low-rank substitutions.
    n=5; clauses=[(1,2),(-3,4)]
    nodes=(1,2,3); q=2; degree=5
    V=[[comb(k,j)*t**(k-j) if k>=j else 0 for k in range(degree+1)]
       for t in nodes for j in range(q)]
    # Solve V^T * lambda = e0 so H(0) is a linear combination of six data.
    lam=gauss_solve(list(zip(*V)),[1,0,0,0,0,0])
    assert lam==list(map(Fraction,[-18,-9,9,-18,10,-3]))
    data=[]
    for t in nodes:
        h,dh=hs_jet(n,clauses,t)
        data.extend([h,dh])
    recovered=tuple(sum(lam[i]*data[i][k] for i in range(6)) for k in range(3))
    assert all(r.denominator==1 for r in recovered)
    recovered=tuple(int(r) for r in recovered)
    direct,_=hs_jet(n,clauses,0)
    assert recovered==direct
    # Audit only: exhaustive truth table to compare moments.
    expected=ZERO; solutions=0
    for bits in product((0,1),repeat=n):
        if all(any(bits[abs(l)-1]==int(l>0) for l in clause) for clause in clauses):
            solutions+=1
            expected=add(expected,jet(sum(bits)))
    assert expected==direct
    # A missing data coordinate i can change H(0), while keeping other 5
    # observed jets zero: polynomial coefficients V^{-1}e_i.
    missing_witness=[]
    for i in range(6):
        basis=[int(i==j) for j in range(6)]
        coeff=gauss_solve(V,basis)
        assert coeff[0]==lam[i] and lam[i]!=0
        missing_witness.append({'omitted_data':f'(t={nodes[i//2]}, j={i%2})','witness_H0':str(coeff[0])})
    # Example of a *different, constrained family*: H(T)=a+b*T^2+c*T^4.
    E=[[t**k for k in (0,2,4)] for t in nodes]
    weights=gauss_solve(list(zip(*E)),[1,0,0])
    assert weights==list(map(Fraction,[Fraction(3,2),Fraction(-3,5),Fraction(1,10)]))
    return {
        'model':'Exact 5-variable 2-CNF with degree<=5 deformation; three nodes and value+first Hasse derivative.',
        'clauses':[[1,2],[-3,4]], 'variables':n,
        'nodes':nodes, 'Hasse_order_per_node':q,
        'recovery_weights':[str(x) for x in lam],
        'recovered_jet_coefficients':list(recovered),
        'moments_N_S_Q':moments(recovered),
        'Hasse_data':[list(a) for a in data],
        'full_degree_5_all_six_data_necessary_for_fixed_scheme':True,
        'counterexample_if_any_jet_omitted':missing_witness,
        'structured_even_polynomial_three_value_weights':[str(x) for x in weights],
        'evenness_in_published_OpenAI_family_verified':False,
        'scope':'This experiment verifies the exact Hermite readout over jets, not fast construction of each jet nor its cost at OpenAI scale.'
    }

def main():
    a=check_anthropic(); b=check_openai()
    output={'date':'2026-11-13','anthropic_eight_square':a,'openai_hasse':b,
            'scope':'Verified precise algebraic operations from published methods in small instances; not full algorithmic reproduction or a new complexity bound.'}
    fn=DIR/'resultados.json';fn.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Anthropic:',a['combinations_checked'],'identity cases; ranks',a['ranks_exact_rational'])
    print('Anthropic jets N S Q:',a['moments_target_and_terms'],'direct:',a['direct_pruned_operations'],'factored:',a['factorized_operations'])
    print('OpenAI Hasse weights:',b['recovery_weights'],'N S Q:',b['moments_N_S_Q'])
    print('Confirmed: six jets necessary in unrestricted degree <=5 with these fixed observations.')
    print('Saved:',fn)
if __name__=='__main__':main()
