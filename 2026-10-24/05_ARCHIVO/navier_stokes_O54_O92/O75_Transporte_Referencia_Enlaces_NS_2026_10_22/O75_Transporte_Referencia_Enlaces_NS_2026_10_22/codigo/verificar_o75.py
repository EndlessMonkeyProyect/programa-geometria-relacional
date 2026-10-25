#!/usr/bin/env python3
"""O75: enlace de deformación material con cierre relacional; ejemplos exactos de NS.
No es una prueba de regularidad global. Dependencias: numpy, scipy, matplotlib.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from numpy.linalg import norm, det
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'datos').mkdir(exist_ok=True)
(ROOT/'graficos').mkdir(exist_ok=True)
NU=0.05
U=1.0
L=np.pi/2
SQUARE_TG=np.array([[0.,0.,0.],[L,0.,0.],[L,L,0.],[0.,L,0.]])
a=.47
ROT=np.array([[np.cos(a),-np.sin(a),0.],[np.sin(a),np.cos(a),0.],[0.,0.,1.]])
SQUARE_ABC=np.array([[-.5,-.5,0.],[.5,-.5,0.],[.5,.5,0.],[-.5,.5,0.]])@(1.2*ROT.T)+np.array([.3,.6,.4])


def field(model, x, t, nu=NU, amp=U):
    """Returns u, grad u, Delta u, ∇(p/rho), ∂_t u; exact unforced NS."""
    x,y,z=x
    if model=='TG':
        A=amp*np.exp(-2*nu*t)
        f=np.array([np.sin(x)*np.cos(y),-np.cos(x)*np.sin(y),0.])
        j=A*np.array([[np.cos(x)*np.cos(y),-np.sin(x)*np.sin(y),0.],
                      [np.sin(x)*np.sin(y),-np.cos(x)*np.cos(y),0.],
                      [0.,0.,0.]])
        u=A*f
        gradp=-A*A*np.array([np.sin(x)*np.cos(x),np.sin(y)*np.cos(y),0.])
        return u,j,-2*u,gradp,-2*nu*u
    if model=='ABC':
        A=amp*np.exp(-nu*t)
        f=np.array([np.sin(z)+np.cos(y),np.sin(x)+np.cos(z),np.sin(y)+np.cos(x)])
        j=A*np.array([[0.,-np.sin(y),np.cos(z)],
                      [np.cos(x),0.,-np.sin(z)],
                      [-np.sin(x),np.cos(y),0.]])
        u=A*f
        gradp=-j.T@u  # p/rho=-|u|²/2 for Beltrami field
        return u,j,-u,gradp,-nu*u
    raise ValueError(model)


def incoming_outgoing(points):
    ein=[];eout=[]
    for i in range(4):
        v=points[i]-points[(i-1)%4]
        w=points[(i+1)%4]-points[i]
        ein.append(v/norm(v));eout.append(w/norm(w))
    return np.array(ein),np.array(eout)


def initial_rate(model, points):
    em,ep=incoming_outgoing(points)
    pieces=[]
    for i in range(4):
        _,g,*_=field(model,points[i],0)
        s=.5*(g+g.T)
        pieces.append(float(em[i]@s@em[i]-ep[i]@s@ep[i]))
    return float(sum(pieces)),pieces


def rhs(t,y,model):
    v=y.reshape(4,12)
    out=np.empty_like(v)
    for i in range(4):
        xyz=v[i,:3]
        F=v[i,3:].reshape(3,3)
        u,j,*_=field(model,xyz,t)
        out[i,:3]=u
        out[i,3:]=(j@F).reshape(-1)
    return out.reshape(-1)


def measure(model,points0,sol):
    em,ep=incoming_outgoing(points0)
    records=[]
    for k,t in enumerate(sol.t):
        v=sol.y[:,k].reshape(4,12)
        pos=v[:,:3]
        F=v[:,3:].reshape(4,3,3)
        a=np.array([norm(F[i]@em[i]) for i in range(4)])
        b=np.array([norm(F[i]@ep[i]) for i in range(4)])
        logh=float(np.log(a/b).sum())
        determinants=np.array([det(f) for f in F])
        # Oriented area projection onto initial normal
        normal0=np.cross(points0[1]-points0[0],points0[3]-points0[0]); normal0/=norm(normal0)
        area_vec=.5*sum(np.cross(pos[i],pos[(i+1)%4]) for i in range(4))
        projected=float(area_vec@normal0)
        stretches=[]
        for f in F:
            svals=np.linalg.svd(f,compute_uv=False)
            stretches.append([float(svals.min()),float(svals.max())])
        # physical instantaneous rate for log H
        rate=0.
        for i in range(4):
            _,g,*_=field(model,pos[i],t)
            strain=(g+g.T)/2
            tv=F[i]@em[i];tw=F[i]@ep[i]
            tv/=norm(tv);tw/=norm(tw)
            rate+=float(tv@strain@tv-tw@strain@tw)
        records.append(dict(t=float(t),H=float(np.exp(logh)),logH=logh,
                            dlogH=rate,area_projection=projected,
                            detF_min=float(determinants.min()),detF_max=float(determinants.max()),
                            min_stretch=float(min(q[0] for q in stretches)),
                            max_stretch=float(max(q[1] for q in stretches))))
    return records


def run_case(model, pts, duration=.9, nt=181):
    y0=np.hstack([pts,np.tile(np.eye(3).reshape(1,9),(4,1))]).reshape(-1)
    t_eval=np.linspace(0,duration,nt)
    sol=solve_ivp(lambda t,y:rhs(t,y,model),(0,duration),y0,t_eval=t_eval,
                  method='DOP853',rtol=5.e-12,atol=5.e-14)
    assert sol.success,sol.message
    return measure(model,pts,sol), sol


def vorticity_and_laplacian(model,x,t):
    """ω, ∇ω, ∆ω, ∂tω for the two exact fields."""
    u,j,lap,gradp,ut=field(model,x,t)
    if model=='ABC':
        return u,j,lap,ut  # Beltrami: curl u=u
    xx,yy,_=x
    A=U*np.exp(-2*NU*t)
    w=np.array([0.,0.,2*A*np.sin(xx)*np.sin(yy)])
    grad=np.zeros((3,3));grad[2,0]=2*A*np.cos(xx)*np.sin(yy);grad[2,1]=2*A*np.sin(xx)*np.cos(yy)
    return w,grad,-2*w,-2*NU*w


def test_pullback(model, sol):
    """Checks material-Cauchy formula with viscous source, one material point."""
    observed=[];source=[]
    for k,t in enumerate(sol.t):
        v=sol.y[:,k].reshape(4,12)
        X=v[0,:3];F=v[0,3:].reshape(3,3)
        omega,_,lapomega,_=vorticity_and_laplacian(model,X,t)
        observed.append(np.linalg.solve(F,omega))
        source.append(NU*np.linalg.solve(F,lapomega))
    observed=np.array(observed);source=np.array(source)
    integrated=observed[0]+cumulative_trapezoid(source,sol.t,axis=0,initial=0.)
    return float(np.max(np.linalg.norm(observed-integrated,axis=1)))


def check(cond, name, tests):
    assert cond,name
    tests.append(name)


def main():
    tests=[]
    rng=np.random.default_rng(76501)
    for model in ('TG','ABC'):
        for _ in range(150):
            x=rng.uniform(-3,3,3); t=rng.uniform(0,1.4)
            u,j,lap,gradp,ut=field(model,x,t)
            residual=ut+j@u+gradp-NU*lap
            check(norm(residual)<3e-14,'PDE_'+model+f'_{len(tests)}',tests)
            check(abs(np.trace(j))<2e-15,'DIV_'+model+f'_{len(tests)}',tests)
    for model in ('TG','ABC'):
        for _ in range(100):
            x=rng.uniform(-2,2,3);t=rng.uniform(0,1)
            u,j,*_=field(model,x,t)
            w,gradw,lapw,wt=vorticity_and_laplacian(model,x,t)
            residual=wt+gradw@u-j@w-NU*lapw
            check(norm(residual)<2e-14,'vorticity_eq_'+model+f'_{len(tests)}',tests)
    tg_rate,tg_parts=initial_rate('TG',SQUARE_TG)
    abc_rate,abc_parts=initial_rate('ABC',SQUARE_ABC)
    check(abs(tg_rate+2*U)<1e-12,'TG_dlogH0_minus_2U',tests)
    check(abs(abc_rate+.6718085063988544*U)<1e-12,'ABC_dlogH0',tests)
    paircases={'TG':run_case('TG',SQUARE_TG), 'ABC':run_case('ABC',SQUARE_ABC)}
    cases={model:pair[0] for model,pair in paircases.items()}
    for model,rec in cases.items():
        check(abs(rec[0]['H']-1)<1e-12,'H0_'+model,tests)
        check(abs(rec[0]['dlogH']-initial_rate(model,SQUARE_TG if model=='TG' else SQUARE_ABC)[0])<1e-12,'initial-rate_'+model,tests)
        det_err=max(max(abs(r['detF_min']-1),abs(r['detF_max']-1)) for r in rec)
        check(det_err<5e-9,'material-detF_'+model,tests)
        # derivative identity using 2nd order centered numerical difference
        step=rec[1]['t']-rec[0]['t']
        derivative_error=max(abs((rec[i+1]['logH']-rec[i-1]['logH'])/(2*step)-rec[i]['dlogH']) for i in range(1,len(rec)-1))
        check(derivative_error<1e-4,'dlogH-identity_'+model,tests)
        check(abs(rec[-1]['logH'])>1e-4,'H-not-conserved_'+model,tests)
        cauchy_error=test_pullback(model,paircases[model][1])
        check(cauchy_error<2e-4,'viscous-vorticity-pullback_'+model,tests)
        assert all(abs(r['area_projection'])>1e-5 for r in rec)
        print(model, 'initial rate=',initial_rate(model,SQUARE_TG if model=='TG' else SQUARE_ABC)[0],
              'H_end=',rec[-1]['H'],'max det error=',det_err,'dlogH difference=',derivative_error)
    # Exact no-closure theorem for unperturbed rigid translation and uniform affine motions:
    # For constant F, incoming and outgoing edge vectors telescope in cyclic ratios.
    em,ep=incoming_outgoing(SQUARE_ABC)
    for _ in range(300):
        M=rng.normal(size=(3,3))
        F=np.eye(3)+.1*M
        h=1.
        for i in range(4): h*=norm(F@em[i])/norm(F@ep[i])
        check(abs(h-1.)<1e-12,'uniform-F-telescoping_'+str(len(tests)),tests)
    # Incompressibility does not entail bounded stretching:
    for k in range(120):
        lam=.01*k
        F=np.diag([np.exp(lam),np.exp(-lam),1.])
        check(abs(det(F)-1)<1e-12,'volume-not-shape_'+str(k),tests)
    # Distinct exact shear solution shares both velocity AND gradient at selected x,y probes
    # initially with zero flow, yet nonzero local acceleration after applying heat operator.
    # w0(y)=sin(2y)^2 cos(2y); y=0 or π/2 => w=w'=0, w''=+8 at 0 and -8 at π/2.
    def w(y):return np.sin(2*y)**2*np.cos(2*y)
    def wp(y):return 4*np.sin(2*y)*np.cos(2*y)**2-2*np.sin(2*y)**3
    for y,sgn in [(0.,1.),(np.pi/2.,-1.)]:
        check(abs(w(y))<1e-14 and abs(wp(y))<1e-14,'invisible-shear-0jets_'+str(y),tests)
        delta=1e-4
        dd=(w(y+delta)-2*w(y)+w(y-delta))/delta**2
        check(abs(dd-8*sgn)<1e-6,'invisible-shear-second-jet_'+str(y),tests)
    # finite samples and initial gradients same, future acceleration differs: ∂_t u=ν w'' e_x
    for model,rec in cases.items():
        with open(ROOT/'datos'/f'o75_{model.lower()}_trayectorias.csv','w') as fh:
            fields=list(rec[0].keys());fh.write(','.join(fields)+'\n')
            for row in rec:fh.write(','.join(f'{row[k]:.16g}' for k in fields)+'\n')
    fig,axes=plt.subplots(2,1,figsize=(8.2,7.4),sharex=True)
    for model,rec in cases.items():
        tt=np.array([v['t'] for v in rec]); hh=np.array([v['H'] for v in rec]);area=np.array([v['area_projection'] for v in rec]);
        axes[0].plot(tt,hh,label=f'{model} — solución exacta NS')
        axes[1].plot(tt,area/area[0],label=model)
    axes[0].axhline(1,linestyle='--',linewidth=1,label='cierre inicial H = 1')
    axes[0].set_ylabel('H(t) — comparación de estiramientos')
    axes[1].set_xlabel('Tiempo del laboratorio (adimensional)')
    axes[1].set_ylabel('Área proyectada / área inicial')
    axes[0].legend(fontsize=9);axes[1].legend(fontsize=9)
    axes[0].grid(alpha=.2);axes[1].grid(alpha=.2)
    fig.suptitle('O75 · NS transporta las relaciones, pero no impone H = 1')
    fig.tight_layout()
    fig.savefig(ROOT/'graficos'/'o75_cierre_y_area.png',dpi=170)
    plt.close(fig)
    out={
        'titulo':'O75 — Transporte material y cierre de enlaces',
        'fecha':'2026-10-22',
        'NU':NU,'U':U,
        'condicion':'Ciclo de estiramientos direccionales F(X_i,t) entrantes/salientes',
        'TG_dlogH_0':tg_rate,'TG_partes':tg_parts,
        'ABC_dlogH_0':abc_rate,'ABC_partes':abc_parts,
        'resumen_casos':{name:{'H0':data[0]['H'],'H_final':data[-1]['H'],
                                'area_rel_final':data[-1]['area_projection']/data[0]['area_projection'],
                                'dlogH_0':data[0]['dlogH'],
                                'max_detF_error':max(max(abs(row['detF_min']-1),abs(row['detF_max']-1)) for row in data)} for name,data in cases.items()},
        'pruebas_aprobadas':len(tests),'grupos':['NS exacta TG','NS exacta ABC', 'H transportada por F', 'volumen local', 'vorticidad transportada con difusion', 'telescopía uniforme', 'contraejemplo cizalla invisible a primer orden'],
        'interpretacion':'No es demostracion de regularidad ni invariancia universal de holonomia.'}
    (ROOT/'datos'/'resumen.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
    print('Tests passed',len(tests),'written',ROOT)

if __name__=='__main__': main()
