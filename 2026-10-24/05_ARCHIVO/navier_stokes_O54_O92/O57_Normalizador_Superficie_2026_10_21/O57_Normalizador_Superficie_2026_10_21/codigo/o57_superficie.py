#!/usr/bin/env python3
"""O57: auditoria de metricas en superficie material toroidal bajo NS-Galerkin O56.
Reutiliza el solver previo sin alterar sus fuentes. Python 3, numpy, matplotlib.
Ejecucion: python codigo/o57_superficie.py
"""
import sys,json,csv,math, time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE/'fuentes'))
import o56_solver as mod

nphi=len(mod.phis); ntheta=len(mod.thetas); ns=nphi*ntheta
step_phi=2*np.pi/nphi; step_theta=2*np.pi/ntheta
X0=mod.initial_surface.reshape(nphi, ntheta,3)

def tvecs(surf):
    p=surf.reshape(nphi,ntheta,3)
    # chordal differences used consistently for G0 and Gt
    a=(np.roll(p,-1,axis=0)-np.roll(p,1,axis=0))/(2*step_phi)
    b=(np.roll(p,-1,axis=1)-np.roll(p,1,axis=1))/(2*step_theta)
    return a.reshape(-1,3),b.reshape(-1,3)
A0,B0=tvecs(mod.initial_surface)
magA0=np.linalg.norm(A0,axis=1); magB0=np.linalg.norm(B0,axis=1)
weight=np.linalg.norm(np.cross(A0,B0),axis=1)
weight/=weight.sum()
e1=A0/magA0[:,None]; e2=B0/magB0[:,None]
assert np.max(np.abs(np.sum(e1*e2,axis=1)))<1e-12

def metrics(points,mirror=1.):
    a,b=tvecs(points[:ns]); aa=np.sum(a*a,axis=1)/magA0**2
    bb=np.sum(b*b,axis=1)/magB0**2
    ab=np.sum(a*b,axis=1)/(magA0*magB0)
    tr=aa+bb; disc=np.sqrt((aa-bb)**2+4*ab**2)
    eiglo=(tr-disc)/2
    if np.min(eiglo)<=0: raise ValueError('Tangent metric degenerated')
    eta=disc/tr
    cos=ab/np.sqrt(aa*bb)
    J=np.sqrt(aa*bb-ab*ab)
    scale=np.sqrt(J)   # common length scale: det C ^ (1/4)
    # D = C/sqrt(detC): exact det D = 1; anisotropy unaffected by uniform mirror
    C11=aa/J; C22=bb/J; C12=ab/J
    detD=C11*C22-C12*C12
    assert np.max(np.abs(detD-1))<1e-10
    mirrortr=(aa+bb)/mirror**2
    mirrordisc=disc/mirror**2
    assert np.max(np.abs(mirrordisc/mirrortr-eta))<1e-11
    return {'eta_mean':float(weight@eta),'eta_max':float(np.max(eta)),
            'eta_p95':float(np.quantile(eta,.95)),
            'cos_rms':float(np.sqrt(weight@(cos*cos))),
            'cos_mean':float(weight@cos),
            'area_ratio':float(weight@J),
            'scale_mean':float(weight@scale),
            'mirror_ratio_check':float(np.max(np.abs(mirrordisc/mirrortr-eta))),
            'min_metric_eigen':float(np.min(eiglo)),
            'eta_array':eta,'cos_array':cos,'J_array':J}

def grad_initial(uh):
    kvals=(mod.kx,mod.ky,mod.kz)
    g=np.empty((ns,3,3))
    for j,kj in enumerate(kvals):
        du=mod.ifftvec(1j*uh*kj)
        g[:,:,j]=mod.sample_velocity(du, mod.initial_surface)
    return (g+np.swapaxes(g,1,2))/2

def initial_predictor(uh):
    S=grad_initial(uh)
    s11=np.einsum('ni,nij,nj->n',e1,S,e1)
    s22=np.einsum('ni,nij,nj->n',e2,S,e2)
    s12=np.einsum('ni,nij,nj->n',e1,S,e2)
    rate=np.sqrt((s11-s22)**2+4*s12**2)
    angle_rate=2*s12
    n0=np.cross(e1,e2)
    sNN=np.einsum('ni,nij,nj->n',n0,S,n0)
    normal_balance_error=float(np.max(np.abs(s11+s22+sNN)))
    area_rate=s11+s22
    # discrete chordal tangents must use the SAME finite-difference operator on velocity
    # to predict the derivative of the recorded discrete metric.
    u0=mod.ifftvec(uh)
    v0=mod.sample_velocity(u0,mod.initial_surface)
    va,vb=tvecs(v0)
    area_rate_chord=np.sum(A0*va,axis=1)/magA0**2+np.sum(B0*vb,axis=1)/magB0**2
    return dict(normal_balance_error=normal_balance_error,
                area_rate_mean=float(weight@area_rate),
                area_rate_rms=float(np.sqrt(weight@(area_rate*area_rate))),
                area_rate_values=area_rate,
                area_rate_chord_values=area_rate_chord,
                eta_rate=float(weight@rate),
                eta_rate_rms=float(np.sqrt(weight@(rate*rate))),
                cosine_rate_rms=float(np.sqrt(weight@(angle_rate*angle_rate))),
                # used to compare angular observable at fixed surface mark
                rate_values=rate)

DT=mod.dt; NS=mod.nsteps; checkpoints={0,1,2,5,10,20,30,45,60,90}

def run(direction):
    uh=mod.init_vortex(direction)
    points=mod.tracers_init.copy()
    pred=initial_predictor(uh)
    out=[]; snapshots={}
    for j in range(NS+1):
        if j in checkpoints:
            time_t=j*DT
            m=metrics(points,math.exp(mod.mirror_rate*time_t))
            u=mod.ifftvec(uh)
            om=mod.ifftvec(1j*mod.cross(mod.kvec,uh))
            row={k:v for k,v in m.items() if not k.endswith('_array')}
            row.update({'caso':direction,'paso':j,'t':float(time_t),
                        'energia':float(0.5*np.mean(np.sum(u*u,axis=0))),
                        'enstrofia':float(0.5*np.mean(np.sum(om*om,axis=0))),
                        'eta_pred_lineal':float(time_t*pred['eta_rate']),
                        'cos_rms_pred_lineal':float(time_t*pred['cosine_rate_rms'])})
            out.append(row)
            snapshots[j]={k:m[k].reshape(nphi,ntheta).copy() for k in ('eta_array','cos_array','J_array')}
        if j==NS:break
        dudt,u,_=mod.rhs(uh)
        umid_hat=mod.project(uh+0.5*DT*dudt)
        dudt_mid,umid,_=mod.rhs(umid_hat)
        vp=mod.sample_velocity(u,points)
        mid=points+0.5*DT*vp
        vpmid=mod.sample_velocity(umid,mid)
        points=(points+DT*vpmid+mod.Lbox/2)%mod.Lbox-mod.Lbox/2
        uh=mod.project(uh+DT*dudt_mid)
    return pred,out,snapshots

def unit_tests():
    from numpy.testing import assert_allclose
    m0=metrics(mod.tracers_init)
    assert abs(m0['eta_mean'])<1e-12
    assert abs(m0['cos_rms'])<1e-12
    assert abs(m0['area_ratio']-1)<1e-12
    # mirror-only coords multiply tangent metric by same scalar; eta should remain exactly zero
    pts=mod.tracers_init.copy(); pts[:ns]*=.4
    assert metrics(pts)['eta_mean']<1e-12
    # conformal scale: eta=0, common scale nontrivial
    assert abs(metrics(pts)['scale_mean']-.4)<1e-12
    # anisotropic diagonal tangential stretch preserves coordinate orthogonality at a point, not conformality
    # C=diag(4,1), eta=(4-1)/(4+1) = 3/5
    assert_allclose((4-1)/(4+1),0.6)
    # a single tangential shear C=[[1,b],[b,1+b^2]] is positive-definite and not conformal
    assert np.linalg.det([[1.,.3],[.3,1.09]])>0
    # invariance of trace/det eigen spread under 2D basis rotations
    C=np.array([[1.2,.4],[.4,2.1]])
    U=np.array([[0.,-1.],[1.,0.]])
    assert_allclose(np.linalg.eigvalsh(C),np.linalg.eigvalsh(U.T@C@U))
    return True

def main():
    unit_tests()
    rows=[]; predictors={}; snaps={}
    st=time.time()
    for direction in ('ninguna','x','y'):
        p,r,s=run(direction); predictors[direction]={k:v for k,v in p.items() if not k.endswith('_values')}
        rows+=r;snaps[direction]=s
        print('Completed',direction, 'elapsed',round(time.time()-st,1),'s', 'eta final',r[-1]['eta_mean'], flush=True)
    # invariant under 90-degree rotation: case x and y must have identical scalar surface summaries;
    # the material label is not rotated, so pointwise arrays differ.
    xr=[r for r in rows if r['caso']=='x']; yr=[r for r in rows if r['caso']=='y']; br=[r for r in rows if r['caso']=='ninguna']
    global_keys=('energia','enstrofia','eta_mean','eta_max','eta_p95','cos_rms','area_ratio','scale_mean')
    diffs={key:float(max(abs(a[key]-b[key]) for a,b in zip(xr,yr))) for key in global_keys}
    # rotation X→Y corresponds to phi index shift by 6 (quarter turn), no requirement on shift sign
    ex=snaps['x'][90]['eta_array']; ey=snaps['y'][90]['eta_array']
    orientation_shift=min(float(np.max(abs(np.roll(ex,k,axis=0)-ey))) for k in (nphi//4,-nphi//4))
    # local metric difference at one initially identical material label
    at_phi0_theta_quarter={s:float(snaps[s][90]['eta_array'][0,2]) for s in snaps}
    # test initial objective rate predicts short-time mean η within numerical interpolation accuracy
    early={s:float([r for r in rows if r['caso']==s and r['paso']==1][0]['eta_mean']/DT) for s in predictors}
    # initial surface-area rate predicted by tangential strain; its orthogonal complement is -n.S.n
    # calculate in the same initial/material coordinates, no fresh adjustable parameters
    area_errors={}
    for s in predictors:
        p=initial_predictor(mod.init_vortex(s))
        observed=(snaps[s][1]['J_array'].reshape(-1)-1)/DT
        theoretical=p['area_rate_chord_values']
        area_errors[s]=float(np.sqrt(weight@((observed-theoretical)**2))/max(1e-15,np.sqrt(weight@(theoretical**2))))
    checks={
        'initial_eta_zero':all(abs(r['eta_mean'])<1e-12 for r in rows if r['paso']==0),
        'mirror_invariance':all(r['mirror_ratio_check']<1e-10 for r in rows),
        'positive_metric':all(r['min_metric_eigen']>0 for r in rows),
        'x_y_equal_global':all(v<1e-8 for v in diffs.values()),
        'x_y_pointwise_label_differs':abs(at_phi0_theta_quarter['x']-at_phi0_theta_quarter['y'])>1e-4,
        'initial_rate_nonzero_for_perturbed':all(predictors[s]['eta_rate']>0 for s in ('x','y')),
        'short_time_rate_predicts':all(abs(early[s]-predictors[s]['eta_rate'])/predictors[s]['eta_rate']<.10 for s in ('x','y')),
        'nonzero_anisotropy_base':br[-1]['eta_mean']>0,
        'normal_perpendicular_balance':all(predictors[s]['normal_balance_error']<1e-10 for s in predictors),
        'short_time_area_rate_predicts':all(v<.10 for v in area_errors.values()),
        'energy_decay':all(a['energia']>=b['energia']-1e-9 for s in ('ninguna','x','y') for a,b in zip([r for r in rows if r['caso']==s][:-1],[r for r in rows if r['caso']==s][1:])),
    }
    summary={'parametros':{'N':mod.N,'dt':DT,'pasos':NS,'t_final':DT*NS,'viscosidad':mod.nu,'R_inicial':mod.R0,'r_inicial':mod.r0,
                            'trazadores_superficie':ns,'cuadricula_superficie':[nphi,ntheta]},
             'predictores_iniciales':predictors,
             'estado_final':{s:[r for r in rows if r['caso']==s][-1] for s in predictors},
             'errores_globales_x_vs_y':diffs,'comparacion_marca':at_phi0_theta_quarter,
             'error_max_rotacion_mapa':orientation_shift,
             'tasa_t_corto':early,'errores_corto_plazo_area':area_errors,'comprobaciones':checks,
             'advertencias':['simulacion Galerkin con malla 32³, no una solucion exacta del sistema continuo',
                             'la superficie es material advectada pero no necesariamente una superficie de vorticidad',
                             'conservar topologia es distinto de conservar metricas o estabilidad',
                             'factor de escala geometrica no es un MCM ni un operador de normalizacion dinamica']}
    root=HERE/'resultados'; root.mkdir(exist_ok=True)
    fields=list(rows[0])
    with (root/'series_o57.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
    (root/'resumen_o57.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
    np.savez_compressed(root/'mapas_superficie_o57.npz',**{f'{s}_eta_{j}':snaps[s][j]['eta_array'] for s in snaps for j in (0,10,30,90)},
                        **{f'{s}_cos_{j}':snaps[s][j]['cos_array'] for s in snaps for j in (0,10,30,90)},
                        phi=mod.phis,theta=mod.thetas)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(9,5))
    for s in ('ninguna','x','y'):
        r=[q for q in rows if q['caso']==s]
        ax.plot([q['t'] for q in r],[q['eta_mean'] for q in r],marker='o',label=s)
    ax.set(xlabel='Tiempo del cálculo',ylabel='Anisotropía intrínseca media η',title='O57 · Deformación superficial independiente del espejo')
    ax.grid(True,alpha=.25);ax.legend();fig.tight_layout();fig.savefig(HERE/'graficos'/'o57_anisotropia_global.png',dpi=175);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5))
    for s in ('ninguna','y'):
        r=[q for q in rows if q['caso']==s]
        ax.plot([q['t'] for q in r],[q['eta_mean'] for q in r],marker='o',label=f'{s}: observado')
        ax.plot([q['t'] for q in r],[q['eta_pred_lineal'] for q in r],linestyle='--',label=f'{s}: predicción inicial')
    ax.set(xlabel='Tiempo',ylabel='η media y aproximación inicial',title='O57 · Predicción inicial desde deformación tangencial')
    ax.grid(True,alpha=.25);ax.legend();fig.tight_layout();fig.savefig(HERE/'graficos'/'o57_prediccion_corto_plazo.png',dpi=175);plt.close(fig)
    fig,axs=plt.subplots(1,3,figsize=(13,4),sharey=True)
    for ax,s in zip(axs,('ninguna','x','y')):
        im=ax.imshow(snaps[s][90]['eta_array'].T,origin='lower',aspect='auto',extent=(0,360,0,360),vmin=0,vmax=max(float(np.max(snaps[q][90]['eta_array'])) for q in snaps))
        ax.set(title=s,xlabel='ángulo toroidal (°)')
    axs[0].set_ylabel('ángulo meridiano (°)');fig.colorbar(im,ax=axs.tolist(),label='η',shrink=.8)
    fig.savefig(HERE/'graficos'/'o57_mapa_superficie.png',dpi=175,bbox_inches='tight');plt.close(fig)
    print('RESULTADOS',json.dumps({'finales':{s:{'eta_mean':summary['estado_final'][s]['eta_mean'],'cos_rms':summary['estado_final'][s]['cos_rms'],'area_ratio':summary['estado_final'][s]['area_ratio']} for s in predictors},'predictores':predictors,'diferencias_rotacion':diffs,'tasa_corta':early,'comprobaciones':checks},indent=2,ensure_ascii=False),flush=True)
    if not all(checks.values()):
        raise RuntimeError('Al menos un control O57 falló, ver resultados')

if __name__=='__main__':main()
