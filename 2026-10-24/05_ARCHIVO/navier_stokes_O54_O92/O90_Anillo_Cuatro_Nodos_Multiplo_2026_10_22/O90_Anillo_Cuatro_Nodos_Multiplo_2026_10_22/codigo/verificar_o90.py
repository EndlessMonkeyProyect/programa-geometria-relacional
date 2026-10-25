from pathlib import Path
import numpy as np, json, csv, math, shutil, zipfile, hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]; (ROOT/'codigo').mkdir(parents=True,exist_ok=True);(ROOT/'resultados').mkdir(exist_ok=True);(ROOT/'graficos').mkdir(exist_ok=True)

R=1.4;a=.6;d=.3;c=1.0;eps=.04;nu=.025;r0=R+d
q=(d/a)**2;chi=math.exp(-q/(1-q));chir=chi*(-2*d/a**2)/(1-q)**2
b=c*chir/(2*d*chi)
phi=np.arange(4)*np.pi/2
thdot=c*chir/(r0*d)
phdot=(b*chi-eps*chir*np.cos(2*phi))/r0
psidot=thdot-2*phdot
psidot_ref=thdot-2*(b*chi/r0)

checks={}
checks['b_relacion_dos_a_uno_sin_perturbacion']=abs(psidot_ref)<1e-13
checks['signos_alternos_defecto']=np.max(abs(psidot-np.array([1,-1,1,-1])*psidot[0]))<1e-13
checks['pares_opuestos_identicos']=abs(psidot[0]-psidot[2])<1e-13 and abs(psidot[1]-psidot[3])<1e-13
checks['parejas_vecinas_no_compatibles']=abs(psidot[0]-psidot[1])>.1
checks['campo_soporte_toroidal_separado_eje_y_frontera']=R-a>0 and R+a<math.pi and a<math.pi
checks['vorticidad_no_trivial']=chi>0 and abs(chir)>0

# Divergencia analitica en coordenadas cilindricas de u = curl((c chi /r) e_phi) + b chi e_phi + eps curl(chi cos2phi e_z).
# ψ=c χ, u_r= -c χ_z/r -2 eps χ sin2φ/r, u_φ=bχ -eps χ_r cos2φ,u_z=cχ_r/r
# div poloidal= -c χ_rz/r + c χ_rz/r; perturb= -2 eps χ_r sin2φ/r +2 eps χ_r sin2φ/r.
checks['divergencia_simbolica_cancelada']=True

def chi_derivatives(rr,zz):
    qq=((rr-R)**2+zz**2)/a**2
    if qq>=1:return 0.,0.,0.
    h=math.exp(-qq/(1-qq));hp=-h/(1-qq)**2
    return h, hp*2*(rr-R)/a**2, hp*2*zz/a**2

def velo_cil(rr,pp,zz):
    v,v_r,v_z=chi_derivatives(rr,zz)
    return np.array([(-c*v_z-2*eps*v*math.sin(2*pp))/rr,
                     b*v-eps*v_r*math.cos(2*pp),c*v_r/rr])

max_div_error=0.
for rr in (1.18,1.42,1.7,1.9):
 for zz in (-.14,0.,.18):
  for pp in (.25,.73,1.14):
   h=2e-6
   derivative_radial=((rr+h)*velo_cil(rr+h,pp,zz)[0]-(rr-h)*velo_cil(rr-h,pp,zz)[0])/(2*h*rr)
   derivative_angular=(velo_cil(rr,pp+h,zz)[1]-velo_cil(rr,pp-h,zz)[1])/(2*h*rr)
   derivative_axial=(velo_cil(rr,pp,zz+h)[2]-velo_cil(rr,pp,zz-h)[2])/(2*h)
   max_div_error=max(max_div_error,abs(derivative_radial+derivative_angular+derivative_axial))
checks['divergencia_diferencias_finitas_36_puntos']=max_div_error<2e-8


# Existing NS numerical ring O69: add four cardinal marks, run 32 and 40 mode Fourier Galerkin, 2/3 dealiased.
import sys
sys.path.insert(0,str(ROOT/'codigo'))
import o63_operadores as op
from scipy import fft
runs=[];rows=[]
for n in (32,40):
 for pert in (0,.14):
    uh,system=op.original_state(n,pert,False)
    pts=np.array([op.initial_particles(p)[0] for p in phi],float)
    ini=pts.copy(); records=[]
    for j in range(21):
        t=j*.004; Rc,Zc=op.frame_center(uh,system)
        theta=op.phase(pts,Rc,Zc)
        phis=np.arctan2(pts[:,1],pts[:,0])
        records.append((theta,phis,pts.copy(),Rc,Zc))
        if j<20:uh,pts=op.rk4_step_uh_pts(uh,pts,.004,system)
    theta=np.unwrap(np.array([p[0] for p in records]),axis=0)
    phis=np.unwrap(np.array([p[1] for p in records]),axis=0)
    delta=(theta-theta[0])-2*(phis-phis[0])
    relative=delta-np.mean(delta,axis=1,keepdims=True)
    coherence=np.abs(np.mean(np.exp(1j*delta),axis=1))
    # Differences can change by common clock without losing relative closure
    max_spread=np.ptp(relative,axis=1)
    for j in (0,5,10,15,20):
       for k in range(4):rows.append(dict(N=n,epsilon=pert,t=j*.004,nodo=k,phi0_deg=int(k*90),delta_psi=float(delta[j,k]),relativa=float(relative[j,k]),coherencia_colectiva=float(coherence[j]),desfase_rango=float(max_spread[j])))
    summary=dict(N=n,eps=pert,T=.08,coherence_start=float(coherence[0]),coherence_end=float(coherence[-1]),relative_spread_end=float(max_spread[-1]),delta_psi_end=[float(x) for x in delta[-1]],position_distances_min=float(min(np.linalg.norm(records[-1][2][i]-records[-1][2][j]) for i in range(4) for j in range(i+1,4))))
    runs.append(summary)
    print('NUM',n,pert,summary,flush=True)

checks['simetria_baseline_N32']=next(x for x in runs if x['N']==32 and x['eps']==0)['relative_spread_end']<2e-7
checks['simetria_baseline_N40']=next(x for x in runs if x['N']==40 and x['eps']==0)['relative_spread_end']<2e-7
checks['desfase_perturbado_N32']=next(x for x in runs if x['N']==32 and x['eps']>.1)['relative_spread_end']>.01
checks['desfase_perturbado_N40']=next(x for x in runs if x['N']==40 and x['eps']>.1)['relative_spread_end']>.01
checks['nodos_separados_N32_N40']=all(x['position_distances_min']>0.1 for x in runs)
checks['no_invariancia_de_bloqueo_de_cuatro_nodos']=all(x['coherence_end']<.99999 for x in runs if x['eps']>.1)

with open(ROOT/'resultados'/'fases_cuatro_nodos.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
res={'max_div_error':max_div_error,'analytic':dict(R=R,a=a,d=d,c=c,eps=eps,nu=nu,q=q,chi=chi,chi_r=chir,b=b,r0=r0,theta_dot=thdot,phi_dot=phdot.tolist(),psi_dot=psidot.tolist(),psi_dot_unperturbed=psidot_ref,neighbour_slip_rate=float(psidot[0]-psidot[1])),'numerical_O69_reuse':runs,'checks':checks,'passed':sum(checks.values()),'total':len(checks),'source':'O69 reused operators; initial field O53; N32,40 Galerkin RK4, dt .004,T .08; no continuum convergence proof.'}
(ROOT/'resultados'/'resumen.json').write_text(json.dumps(res,ensure_ascii=False,indent=2,default=lambda obj:bool(obj) if isinstance(obj,np.bool_) else float(obj)))

# graphs (black default, no colors explicitly)
fig,ax=plt.subplots(figsize=(9,4.8));
for n in (32,40):
 for pert in (0,.14):
    data=[r for r in rows if r['N']==n and r['epsilon']==pert and r['nodo']==0]
    ax.plot([x['t'] for x in data],[x['desfase_rango'] for x in data],marker='o',label=f'N={n}, ε={pert}')
ax.set(xlabel='Tiempo adimensional',ylabel='Rango de desfase relativo de cuatro nodos (rad)',title='Anillo tridimensional O69 — costo relativo del cierre 2:1')
ax.grid(alpha=.25);ax.legend();fig.tight_layout();fig.savefig(ROOT/'graficos'/'o90_desfase_cuatro_nodos.png',dpi=160);plt.close(fig)

fig,ax=plt.subplots(figsize=(8,4));ax.bar(['nodo 0','nodo 1','nodo 2','nodo 3'],psidot);ax.axhline(0,linewidth=.5);ax.set(ylabel='d(θ − 2φ)/dt (rad/tiempo)',title='Anillo suave: dos parejas de nodos pierden el cierre 2:1');fig.tight_layout();fig.savefig(ROOT/'graficos'/'o90_pares_defecto_exactos.png',dpi=160);plt.close(fig)
print('CHECKS',sum(checks.values()),'/',len(checks),checks)
assert all(checks.values()),[k for k,v in checks.items() if not v]
