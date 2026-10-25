#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O71: same D4 collective field and Reynolds stress, different second derivative.

Finite Fourier–Galerkin Navier–Stokes; no claim of global regularity.
Run python codigo/experimento_o71.py from any directory.
"""
from pathlib import Path
import json,csv
import numpy as np
from scipy import fft
from experimento_o70 import state,proj,g_apply,G,from_real,vel_rhs,norm,op

ROOT=Path(__file__).resolve().parents[1]


def projection_tensor(w):
    ret=np.zeros((3,3)+w.shape[1:],dtype=np.float64)
    for g in G:
        v=g_apply(w,g)
        ret+=np.einsum('i...,j...->ij...',v,v,optimize=True)
    return ret/len(G)


def tau_full(u):
    a=proj(u)
    return projection_tensor(u)-np.einsum('i...,j...->ij...',a,a,optimize=True)


def tensor_norm(t):
    return float(np.sqrt(np.mean(np.sum(t*t,axis=(0,1)))))


def time_derivative_tau(u,F):
    w=u-proj(u)
    wt=F(u)-proj(F(u))
    t=np.zeros((3,3)+w.shape[1:],dtype=np.float64)
    for g in G:
        v=g_apply(w,g);dv=g_apply(wt,g)
        t+=np.einsum('i...,j...->ij...',v,dv,optimize=True)
        t+=np.einsum('i...,j...->ij...',dv,v,optimize=True)
    return t/len(G)


def stress_acceleration(t,sys):
    k,k2,k2safe,mask,_=sys
    tah=fft.fftn(t,axes=(-3,-2,-1))
    div=np.einsum('j...,ij...->i...',1j*k,tah,optimize=True)
    gradient=k*np.sum(k*div,axis=0)/k2safe
    return fft.ifftn(-(div-gradient)*mask,axes=(-3,-2,-1)).real


def vorticity_weighted_geometry(u,sys):
    # Equivalent observable under D4, includes all the fine-scale vorticity.
    n=u.shape[-1]
    h=from_real(u,sys)
    vort=fft.ifftn(sys[4](h),axes=(-3,-2,-1)).real
    weight=np.sum(vort*vort,axis=0)
    line=np.arange(n)*2*np.pi/n-np.pi
    x,y,z=np.meshgrid(line,line,line,indexing='ij')
    rho=np.hypot(x,y)
    s=np.sum(weight)
    R=float(np.sum(rho*weight)/s)
    Z=float(np.sum(z*weight)/s)
    r=float(np.sqrt(np.sum(((rho-R)**2+(z-Z)**2)*weight)/s))
    return {'R_vorticidad':R,'Z_vorticidad':Z,'r_rms_vorticidad':r,'ratio_r_R':r/R,
            'enstrofia_proxy':float(np.mean(weight))}


def collective_phase_rates(a,ap):
    n=a.shape[-1]
    ah=fft.fftn(a,axes=(-3,-2,-1))/n**3
    dh=fft.fftn(ap,axes=(-3,-2,-1))/n**3
    chosen=((2,1,1,1),(2,1,1,2))
    out=[]
    for idx in chosen:
        amp=ah[idx]
        if abs(amp)<1e-10:
            raise ValueError(f'collective phase Fourier mode vanishes {idx}')
        out.append({'index':list(idx),'amplitud':float(abs(amp)),
                    'fase':float(np.angle(amp)),
                    'frecuencia_instantanea':float(np.imag(dh[idx]/amp)/(2*np.pi))})
    return out


def second_derivative(u,F):
    # F is affine-linear plus quadratic: exact centered polarization,
    # not a numerical derivative approximation from finite time steps.
    d=F(u)
    h=.125
    return proj((F(u+h*d)-F(u-h*d))/(2*h))


def rk4(u,dt,F):
    k1=F(u)
    k2=F(u+dt*k1/2)
    k3=F(u+dt*k2/2)
    k4=F(u+dt*k3)
    return u+dt*(k1+2*k2+2*k3+k4)/6


def one_resolution(n):
    base,sys=state(n,0)
    full,_=state(n,.14)
    # Antialiasing estricto: para N divisible por tres, incluir |k|=N/3
    # genera alias de extremos (16+16 -> -16 en N=48).
    # La regla |k_j|<N/3 lo evita y conserva simetría D4.
    strict=np.logical_and.reduce([np.abs(sys[0][axis])<n/3 for axis in range(3)])
    strict=strict & sys[3]
    sys=(sys[0],sys[1],sys[2],strict,sys[4])
    base=fft.ifftn(fft.fftn(base,axes=(-3,-2,-1))*strict,axes=(-3,-2,-1)).real
    full=fft.ifftn(fft.fftn(full,axes=(-3,-2,-1))*strict,axes=(-3,-2,-1)).real
    a0=proj(base)
    v=full-proj(full)
    F=lambda u:vel_rhs(u,sys)
    checks={}
    checks['base_symmetrical']=norm(base-a0)<1e-12
    checks['zero_common_v']=norm(proj(v))<1e-12
    result=[]
    a_record={}
    for sign in (1,-1):
        u=base+sign*v
        a=proj(u); f=F(u);ap=proj(f)
        geom=vorticity_weighted_geometry(u,sys)
        tau=tau_full(u)
        taup=time_derivative_tau(u,F)
        d2=second_derivative(u,F)
        a_record[sign]=(u,a,ap,tau,taup,d2,geom,collective_phase_rates(a,ap))
        result.append({'sign':sign,**geom,'tensor_tau_norm':tensor_norm(tau),
                       'tensor_tau_prime_norm':tensor_norm(taup),
                       'freq':collective_phase_rates(a,ap)})
    pos,neg=a_record[1],a_record[-1]
    checks['equal_common']=norm(pos[1]-neg[1])<1e-11
    checks['equal_tau_tensor']=tensor_norm(pos[3]-neg[3])<1e-11
    checks['equal_common_derivative']=norm(pos[2]-neg[2])<1e-11
    checks['same_radii_full_field']=max(abs(pos[6][k]-neg[6][k]) for k in pos[6])<1e-11
    checks['same_collective_frequencies']=max(abs(x['frecuencia_instantanea']-y['frecuencia_instantanea']) for x,y in zip(pos[7],neg[7]))<1e-10
    delta_d2=pos[5]-neg[5]
    delta_tauprime=pos[4]-neg[4]
    predicted=stress_acceleration(delta_tauprime,sys)
    checks['nonzero_tauprime_difference']=tensor_norm(delta_tauprime)>1e-6
    checks['nonzero_second_derivative_difference']=norm(delta_d2)>1e-6
    checks['second_derivative_resolved_by_tauprime']=norm(delta_d2-predicted)<1e-10
    # CUBIC LAW: 2nd derivative separation ∝ c^3 in this constructed twin family.
    cubic=[]
    for c in (.5,1.,2.):
        d2difference=second_derivative(base+c*v,F)-second_derivative(base-c*v,F)
        cubic.append({'c':c,'second_derivative_distance':norm(d2difference),
                      'ratio_to_cubed':norm(d2difference)/(c**3)})
    checks['cubic_amplitude_scaling']=max(q['ratio_to_cubed'] for q in cubic)-min(q['ratio_to_cubed'] for q in cubic)<1e-9
    # Evolve both states in finite-dimensional system without phase locking.
    p=pos[0].copy();m=neg[0].copy()
    time_rows=[]
    dt=.004
    for it in range(9):
        t=it*dt
        separation=norm(proj(p)-proj(m))
        second_order=.5*t*t*norm(delta_d2)
        time_rows.append({'N':n,'t':t,'distancia_comun':separation,
                          'prediccion_orden2':second_order,
                          'razon_taylor':separation/second_order if t else None})
        if it<8:
            p=rk4(p,dt,F);m=rk4(m,dt,F)
    checks['different_future_reference']=time_rows[-1]['distancia_comun']>1e-6
    checks['short_time_taylor_valid']=.75<time_rows[1]['razon_taylor']<1.25
    summary={'N':n,'v_rms':norm(v),'a0_rms':norm(a0),
             'same_initial_geometry':pos[6],
             'phase_rates_common':pos[7],
             'same_tau_initial_norm':tensor_norm(pos[3]),
             'tau_prime_difference':tensor_norm(delta_tauprime),
             'second_derivative_difference':norm(delta_d2),
             'stress_identity_error':norm(delta_d2-predicted),
             'first_derivative_difference':norm(pos[2]-neg[2]),
             'cubic':cubic,'checks':{k:bool(val) for k,val in checks.items()},'future':time_rows}
    print('N',n,'d2 gap',norm(delta_d2),'tau prime gap',tensor_norm(delta_tauprime),'prediction error',norm(delta_d2-predicted),flush=True)
    assert all(checks.values()),checks
    return summary,time_rows


def main():
    summaries=[];series=[]
    for n in (32,40,48):
        obj,rows=one_resolution(n)
        summaries.append(obj);series.extend(rows)
    checks={f'N{entry["N"]}_{key}':v for entry in summaries for key,v in entry['checks'].items()}
    assert all(checks.values())
    result={'checks':checks,'checks_passed':sum(checks.values()),'checks_total':len(checks),'experiments':summaries}
    (ROOT/'resultados'/'resumen.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    with (ROOT/'resultados'/'evolucion.csv').open('w',newline='') as fl:
        writer=csv.DictWriter(fl,fieldnames=['N','t','distancia_comun','prediccion_orden2','razon_taylor'])
        writer.writeheader();writer.writerows(series)
    print('PASSED',sum(checks.values()),'/',len(checks),flush=True)

if __name__=='__main__':
    main()
