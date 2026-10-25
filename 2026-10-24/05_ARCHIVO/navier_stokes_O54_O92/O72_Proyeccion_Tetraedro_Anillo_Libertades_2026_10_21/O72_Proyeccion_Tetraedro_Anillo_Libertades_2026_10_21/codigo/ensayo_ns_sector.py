#!/usr/bin/env python3
"""O72 Fourier-Galerkin NS: parity sector of quarter-turn (C4) vs O71's mixed sectors.
Reuses the O70 solver and initial data. N=32, 8 steps, dt=0.004.
"""
from pathlib import Path
import json
import numpy as np
from scipy import fft
import experimento_o70_BASE as p
ROOT=Path(__file__).resolve().parents[1]

N=32; dt=.004; steps=8
u0,sys=p.state(N,0); up,_=p.state(N,.14)
rot=p.group_mats()[1]
def U(u,j=1):return p.g_apply(u,np.linalg.matrix_power(rot,j))
def even(u):return sum((U(u,j) for j in range(4)),start=np.zeros_like(u))/4
def odd(u):return sum(((-1)**j*U(u,j) for j in range(4)),start=np.zeros_like(u))/4

a=even(u0);w=odd(up-p.proj(up))
u_plus=a+w;u_minus=a-w
assert p.norm(w)>.01

def evolve(u):
    uh=p.from_real(u,sys)
    samples=[]
    for step in range(steps+1):
        field=fft.ifftn(uh,axes=(-3,-2,-1)).real
        samples.append(field)
        if step==steps:break
        def F(x):return p.op.evaluate(x,*sys,nu=p.op.NU)[0]
        k1=F(uh);k2=F(uh+dt*k1/2);k3=F(uh+dt*k2/2);k4=F(uh+dt*k3)
        uh=(uh+dt/6*(k1+2*k2+2*k3+k4))*sys[3]
    return samples
sp=evolve(u_plus);sm=evolve(u_minus)
records=[]
for i,(u,v) in enumerate(zip(sp,sm)):
    rec={'t':i*dt,'rotated_equals_minus_error':p.norm(U(u)-v),'same_common_error':p.norm(even(u)-even(v)),'two_sector_remainder':p.norm(u-even(u)-odd(u)),'parity_error':p.norm(U(odd(u))+odd(u))}
    assert rec['rotated_equals_minus_error']<1e-10,rec
    assert rec['same_common_error']<1e-10,rec
    assert rec['two_sector_remainder']<1e-10,rec
    records.append(rec)
res={'name':'O72 ns C4 parity sector','n':N,'dt':dt,'steps':steps,'odd_mode_norm_initial':p.norm(w),'tests_passed':4*len(records)+1,'max_rotated_equals_minus_error':max(x['rotated_equals_minus_error'] for x in records),'max_same_common_error':max(x['same_common_error'] for x in records),'max_two_sector_remainder':max(x['two_sector_remainder'] for x in records),'records':records,'limitation':'Short-time finite Fourier Galerkin computation; no proof of global 3D NS regularity or of gear coupling to NS.'}
(ROOT/'datos'/'ensayo_ns_sector_o72.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k!='records'},indent=2))
