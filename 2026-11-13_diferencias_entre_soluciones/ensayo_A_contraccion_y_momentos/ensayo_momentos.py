#!/usr/bin/env python3
"""Ensayo verificable: momentos de #SAT por redes de factores e interpolacion.

Solo Python 3 (biblioteca estandar). Cada metodo usa operaciones exactas.
NO implementa los algoritmos completos de Anthropic u OpenAI.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb
import csv
import json
from pathlib import Path

@dataclass
class Counts:
    mult: int = 0
    add: int = 0

class Algebra:
    def __init__(self, jets=False):
        self.jets = jets
        self.ops = Counts()
        self.max_bits = 0
        self.zero = (0, 0, 0) if jets else 0
        self.one = (1, 0, 0) if jets else 1

    def check_bits(self, value):
        values = value if self.jets else (value,)
        self.max_bits = max(self.max_bits, *(max(1,abs(v).bit_length()) for v in values))

    def add(self, a, b):
        if self.jets:
            self.ops.add += 3
            v=(a[0]+b[0], a[1]+b[1], a[2]+b[2])
            self.check_bits(v)
            return v
        self.ops.add += 1
        v=a+b
        self.check_bits(v)
        return v

    def mul(self, a, b):
        if self.jets:
            # product modulo u^3: exactly 6 scalar products + 3 scalar sums
            self.ops.mult += 6
            self.ops.add += 3
            v=(a[0]*b[0], a[0]*b[1]+a[1]*b[0],
               a[0]*b[2]+a[1]*b[1]+a[2]*b[0])
            self.check_bits(v)
            return v
        self.ops.mult += 1
        v=a*b
        self.check_bits(v)
        return v

@dataclass
class Factor:
    scope: tuple[int,...]
    table: dict[tuple[int,...],object]
    def value(self, chosen: dict[int,int]):
        return self.table[tuple(chosen[v] for v in self.scope)]

def clauses_for(n: int, pattern: str):
    # Signed 1-indexed literals; clause length up to 3.
    clauses = [(i+1, -(i+2), i+3) for i in range(n-2)]
    clauses += [(-(i+1), i+2, -(i+3)) for i in range(0,n-2,3)]
    if pattern == 'cycle':
        clauses += [(n-1,n,-1),(-n,1,2)]
    if pattern == 'unsat':
        clauses += [(1,),(-1,)]
    return clauses

def satisfies_clause(clause: tuple[int,...], bits: tuple[int,...]):
    return any((bits[abs(lit)-1] == 1) if lit > 0 else (bits[-lit-1] == 0) for lit in clause)

def build_factors(n, clauses, A, t=None, fixed=frozenset()):
    ff=[]
    for i in range(n):
        table={}
        for b in (0,1):
            if A.jets:
                # Weight t^x at t=1+u; x=0 -> 1, x=1 -> 1+u
                table[(b,)] = (1, b, 0)
            else:
                table[(b,)] = int(b==1) if i in fixed else (t**b if t is not None else 1)
        ff.append(Factor((i,),table))
    for clause in clauses:
        scope=tuple(sorted({abs(v)-1 for v in clause}))
        tab={}
        for bits in product((0,1), repeat=len(scope)):
            env=dict(zip(scope,bits))
            is_ok=any((env[abs(lit)-1]==1) if lit>0 else (env[-lit-1]==0)
                      for lit in clause)
            val=int(is_ok)
            tab[bits] = (val,0,0) if A.jets else val
        ff.append(Factor(scope,tab))
    return ff

def contract(n, clauses, jets=False, t=None, fixed=()):
    A=Algebra(jets)
    ff=build_factors(n,clauses,A,t,frozenset(fixed))
    max_table=0
    def table_slots(factors):
        return sum(len(f.table)*(3 if jets else 1) for f in factors)
    def table_payload_bits(factors):
        def bits(v):
            vv = v if jets else (v,)
            return sum(max(1,abs(z).bit_length()) for z in vv)
        return sum(bits(v) for f in factors for v in f.table.values())
    peak_slots=table_slots(ff)
    peak_payload_bits=table_payload_bits(ff)
    for v in range(n):
        chosen=[f for f in ff if v in f.scope]
        ff=[f for f in ff if v not in f.scope]
        scope=tuple(sorted(set().union(*(f.scope for f in chosen))))
        remaining=tuple(k for k in scope if k!=v)
        tab={}
        for assignment in product((0,1), repeat=len(remaining)):
            base=dict(zip(remaining,assignment))
            acc=A.zero
            for bit in (0,1):
                env={**base, v:bit}
                prod_value=chosen[0].value(env)
                for f in chosen[1:]:
                    prod_value=A.mul(prod_value,f.value(env))
                acc=A.add(acc,prod_value)
            tab[assignment]=acc
        added=Factor(remaining,tab)
        ff.append(added)
        max_table=max(max_table,len(tab))
        peak_slots=max(peak_slots,table_slots(ff)+table_slots(chosen))
        peak_payload_bits=max(peak_payload_bits,table_payload_bits(ff)+table_payload_bits(chosen))
    assert len(ff)==1 and ff[0].scope==()
    return ff[0].table[()], A.ops, max_table, peak_slots, peak_payload_bits, A.max_bits

def brute(n, clauses):
    counts={}
    for bits in product((0,1), repeat=n):
        if all(satisfies_clause(c,bits) for c in clauses):
            weight=sum(bits)
            counts[weight]=counts.get(weight,0)+1
    return tuple(sum(m*w**j for w,m in counts.items()) for j in (0,1,2)), counts

def coeffs_from_points(points):
    # Exact interpolation using Lagrange basis: coefficient of t^k counts weight-k assignments.
    out=[Fraction(0) for _ in range(len(points))]
    for x,fx in points:
        basis=[Fraction(1)]
        den=Fraction(1)
        for y,_ in points:
            if y==x: continue
            next_poly=[Fraction(0)]*(len(basis)+1)
            for i,v in enumerate(basis):
                next_poly[i] += -y*v
                next_poly[i+1] += v
            basis=next_poly
            den*=x-y
        for i,c in enumerate(basis):
            out[i]+=Fraction(fx)*c/den
    assert all(c.denominator==1 for c in out)
    return [int(c) for c in out]

def rational_rank(matrix):
    rows = [[Fraction(v) for v in row] for row in matrix]
    nr, nc = len(rows), len(rows[0]) if rows else 0
    r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if rows[i][c]),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        value=rows[r][c]
        rows[r]=[v/value for v in rows[r]]
        for i in range(r+1,nr):
            factor=rows[i][c]
            if factor:
                rows[i]=[a-factor*b for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==nr: break
    return r

def evaluate_one(n,pattern):
    clauses=clauses_for(n,pattern)
    expected,dist=brute(n,clauses)
    # 1) Single contraction carrying jets, i.e. G(1+u) modulo u^3
    jets,jo,jmax,jslots,jpayload,jbits=contract(n,clauses,jets=True)
    joint=(jets[0],jets[1],jets[1]+2*jets[2])
    assert joint==expected,(joint,expected)
    # 2) Independent counts #F, #F&xi, #F&xi&xj
    cond= [()] + [(i,) for i in range(n)] + [(i,j) for i in range(n) for j in range(i+1,n)]
    vals=[]; so=Counts(); smax=0; sslots=0; spayload=0; sbits=0
    for constraints in cond:
        v,ops,ms,ps,pb,mb=contract(n,clauses,fixed=constraints)
        vals.append(v)
        so.mult+=ops.mult; so.add+=ops.add; smax=max(smax,ms); sslots=max(sslots,ps); spayload=max(spayload,pb); sbits=max(sbits,mb)
    separate=(vals[0],sum(vals[1:1+n]),sum(vals[1:1+n])+2*sum(vals[1+n:]))
    assert separate==expected,(separate,expected)
    # 3) Scalar evaluations of generating polynomial and exact interpolation
    sample_values=[]; io=Counts(); imax=0; islots=0; ipayload=0; ibits=0
    for t in range(n+1):
        v,ops,ms,ps,pb,mb=contract(n,clauses,t=t)
        sample_values.append((t,v)); io.mult+=ops.mult; io.add+=ops.add; imax=max(imax,ms); islots=max(islots,ps); ipayload=max(ipayload,pb); ibits=max(ibits,mb)
    coefficients=coeffs_from_points(sample_values)
    poly=(sum(coefficients), sum(j*c for j,c in enumerate(coefficients)),
          sum(j*j*c for j,c in enumerate(coefficients)))
    assert poly==expected,(poly,expected)
    assert coefficients==[dist.get(i,0) for i in range(n+1)]
    # Move the reference axis without resolving any individual solution.
    for axis in (0,1,2):
        translated=(expected[0],expected[1]-axis*expected[0],
                    expected[2]-2*axis*expected[1]+axis*axis*expected[0])
        direct=tuple(sum(m*(k-axis)**j for k,m in dist.items()) for j in (0,1,2))
        assert translated==direct
    moments=[sum(c*(k**j) for k,c in enumerate(coefficients)) for j in range(2*(n+1))]
    hankel=[[moments[i+j] for j in range(n+1)] for i in range(n+1)]
    hankel_rank=rational_rank(hankel)
    assert hankel_rank==len(dist)
    center=str(Fraction(expected[1],expected[0])) if expected[0] else 'undefined'
    variance=str(Fraction(expected[2],expected[0])-Fraction(expected[1],expected[0])**2) if expected[0] else 'undefined'
    return dict(pattern=pattern,n=n,clauses=len(clauses),solutions=expected[0],M1=expected[1],M2=expected[2],
                moments_jets=list(jets),support=len(dist),hankel_rank=hankel_rank,center=center,variance=variance,reference_translation_verified=True,joint_mult=jo.mult,joint_add=jo.add,
                separate_mult=so.mult,separate_add=so.add,
                interpolation_mult=io.mult,interpolation_add=io.add,
                separate_queries=len(cond),interpolation_evaluations=n+1,
                ratio_sep_primitive=round((so.mult+so.add)/(jo.mult+jo.add),3),
                ratio_interp_primitive=round((io.mult+io.add)/(jo.mult+jo.add),3),
                max_intermediate_entries=max(jmax,smax,imax),
                peak_slots_joint=jslots,peak_slots_separate=sslots,peak_slots_interp_eval=islots,
                peak_payload_bits_joint=jpayload,peak_payload_bits_separate=spayload,peak_payload_bits_interp_eval=ipayload,
                max_integer_bits_joint=jbits,max_integer_bits_separate=sbits,max_integer_bits_interp_eval=ibits,
                distribution={str(w):m for w,m in sorted(dist.items())},
                coefficients=coefficients)

def main():
    results=[]
    for pattern,n in [('path',4),('path',6),('path',8),('path',10),('cycle',6),('cycle',8),('cycle',10),('unsat',6)]:
        row=evaluate_one(n,pattern)
        results.append(row)
        print(f"{pattern:5} n={n:2} N={row['solutions']:5} M1={row['M1']:5} M2={row['M2']:6} "
              f"joint={row['joint_mult']+row['joint_add']:6} "
              f"cond={row['separate_mult']+row['separate_add']:6} "
              f"interp-eval={row['interpolation_mult']+row['interpolation_add']:6} "
              f"cond/joint={row['ratio_sep_primitive']:5.2f} "
              f"interp/joint={row['ratio_interp_primitive']:5.2f}")
    out=Path(__file__).parent
    with (out/'resultados.json').open('w',encoding='utf-8') as f:
        json.dump({'method':'Exact arithmetic, naive fixed-order variable elimination, no memoisation; interpolation arithmetic excluded from counts.',
                   'cases':results},f,indent=2,ensure_ascii=False)
    keep=['pattern','n','clauses','solutions','M1','M2','support','hankel_rank','center','variance','reference_translation_verified','separate_queries','interpolation_evaluations','joint_mult','joint_add','separate_mult','separate_add','interpolation_mult','interpolation_add','ratio_sep_primitive','ratio_interp_primitive','max_intermediate_entries','peak_slots_joint','peak_slots_separate','peak_slots_interp_eval','peak_payload_bits_joint','peak_payload_bits_separate','peak_payload_bits_interp_eval','max_integer_bits_joint','max_integer_bits_separate','max_integer_bits_interp_eval']
    with (out/'resultados.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=keep);w.writeheader();w.writerows({k:r[k] for k in keep} for r in results)

if __name__=='__main__': main()
