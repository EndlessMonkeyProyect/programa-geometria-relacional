#!/usr/bin/env python3
"""Independent check of Reynolds stress closure for group projection.
P F(u)-F(Pu) = - FourierLeray div [mean_G Gu⊗Gu - Pu⊗Pu].
"""
import numpy as np,json
from scipy import fft
from pathlib import Path
from experimento_o70 import group_mats,proj,g_apply,norm,vel_rhs,from_real,state,op
ROOT=Path(__file__).resolve().parents[1]

def test(n):
    base,sys=state(n,0);up,_=state(n,.14)
    v=up-proj(up)
    u=base+v
    avg=proj(u)
    tau=sum((np.einsum('i...,j...->ij...',gu,gu) for gu in (g_apply(u,g) for g in group_mats())), start=np.zeros((3,3,n,n,n)))/8-np.einsum('i...,j...->ij...',avg,avg)
    # Tensor has frequency content above mask; resolve its low modes by FourierLeray projection.
    tauh=fft.fftn(tau,axes=(-3,-2,-1))
    k,k2,k2safe,mask,_=sys
    div=np.einsum('j...,ij...->i...',1j*k,tauh)
    grad=k*np.sum(k*div,axis=0)/k2safe
    rhs=fft.ifftn(-(div-grad)*mask,axes=(-3,-2,-1)).real
    measured=proj(vel_rhs(u,sys))-vel_rhs(avg,sys)
    e=norm(measured-rhs)
    d=norm(measured)
    trans=norm(proj(u-base))
    assert e < 1e-10 and d > 1e-5 and trans < 1e-11
    return dict(N=n,absolute_residual=e,relative_residual=e/d,reynolds_stress_rms=float(np.sqrt(np.mean(np.sum(tau*tau,axis=(0,1))))),dynamic_defect_norm=d,projected_initial_difference=trans)

if __name__=='__main__':
    out=[test(n) for n in (32,40)]
    print(json.dumps(out,indent=2))
    (ROOT/'resultados'/'verificacion_tension_residual.json').write_text(json.dumps(out,indent=2))
