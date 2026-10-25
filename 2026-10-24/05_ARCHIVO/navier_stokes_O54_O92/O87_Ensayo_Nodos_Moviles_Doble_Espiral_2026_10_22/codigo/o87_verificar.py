#!/usr/bin/env python3
"""O87: torus surface kinematics, intrinsic phase and a divergence-free adversary.
Purely surface (2D) divergence-free flows: these are NOT asserted to solve 3D NS.
"""
from pathlib import Path
import json, csv
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
(root/'resultados').mkdir(exist_ok=True)
(root/'graficos').mkdir(exist_ok=True)
R,a,kappa,p,q,epsilon=2.0,0.6,0.8,1,2,0.25
T=14.0
times=np.linspace(0,T,1401)
initial_gammas=np.arange(4)*np.pi/2

def gamma_of_chi(c):
    return c+a/(q*R)*np.sin(q*c)
def chi_of_gamma(g):
    c=np.asarray(g).astype(float).copy()
    for j in range(10):
        c-= (gamma_of_chi(c)-g)/(1+a/R*np.cos(q*c))
    return c

g=initial_gammas[:,None]+kappa/R*times[None,:]
chi=chi_of_gamma(g)
theta=q*chi; phi=p*chi
psi=p*theta-q*phi
unequal_chi=(chi-chi[0:1,:]-initial_gammas[:,None])
# Physical surface velocity field has metric jacobian J=a*(R+a*cos(theta))
# Good model and an adversary with differential poloidal drive.
def rhs(t,Y,eps):
    y=Y.reshape(4,2)
    th,ph=y[:,0],y[:,1]
    denom=R+a*np.cos(th)
    dth=q*(kappa+eps*np.sin(ph))/denom
    dph=p*kappa/denom
    return np.stack([dth,dph],axis=1).ravel()

Y0=np.stack([q*initial_gammas,p*initial_gammas],axis=1).ravel()
base=solve_ivp(rhs,[0,T],Y0,args=(0.,),t_eval=times,atol=5e-12,rtol=5e-12,max_step=.016)
pert=solve_ivp(rhs,[0,T],Y0,args=(epsilon,),t_eval=times,atol=5e-12,rtol=5e-12,max_step=.016)
assert base.success and pert.success
base_Y=base.y.reshape(4,2,-1); pert_Y=pert.y.reshape(4,2,-1)
base_phase=p*base_Y[:,0,:]-q*base_Y[:,1,:]
pert_phase=p*pert_Y[:,0,:]-q*pert_Y[:,1,:]
base_chi=base_Y[:,1,:]/p
num_err=np.max(abs(base_chi-chi))
# Phase slip predicted exactly from the perturbation
pred_psi_dot=p*q*epsilon*np.sin(pert_Y[:,1,:])/(R+a*np.cos(pert_Y[:,0,:]))
psi_dot_now=(rhs(0,Y0,epsilon).reshape(4,2)[:,0]*p-rhs(0,Y0,epsilon).reshape(4,2)[:,1]*q)
pred_psi_initial=p*q*epsilon*np.sin(p*initial_gammas)/(R+a*np.cos(q*initial_gammas))
# Jacobian preservation: J theta_dot=a*q*(k+e sin phi), J phi_dot=a*p*kappa.
# Surface divergence: ∂theta(J*theta_dot)+∂phi(J*phi_dot)=0.
assert np.max(np.abs(psi))<1e-13
assert num_err<3e-9, num_err
assert np.max(np.abs(base_phase))<4e-10
assert np.max(np.abs(psi_dot_now-pred_psi_initial))<1e-14
assert np.max(np.abs(gamma_of_chi(chi)-g))<1e-12
assert np.max(np.abs(g-initial_gammas[:,None]-kappa/R*times[None,:]))<2e-14
assert np.max(np.abs(pert_phase))>0.1
# finite difference analytic surface area divergence as secondary computational check
rng=np.random.default_rng(1729)
th=rng.uniform(-np.pi,np.pi,200); ph=rng.uniform(-np.pi,np.pi,200)
h=1e-5

def flux_th(th,ph,eps):
    J=a*(R+a*np.cos(th)); return J*q*(kappa+eps*np.sin(ph))/(R+a*np.cos(th))
def flux_ph(th,ph,eps):
    J=a*(R+a*np.cos(th)); return J*p*kappa/(R+a*np.cos(th))
for e in [0,epsilon]:
    div=((flux_th(th+h,ph,e)-flux_th(th-h,ph,e))+(flux_ph(th,ph+h,e)-flux_ph(th,ph-h,e)))/(2*h)
    assert np.max(np.abs(div))<1e-9
# geometry diagnostic
raw_separation=chi[1,:]-chi[0,:]
lag_deviation=raw_separation-np.pi/2
normal_lag=((g[1,:]-g[0,:])-np.pi/2)
# Opposite pairs are maintained even though the neighboring gaps move.
assert np.max(np.abs(chi[2,:]-chi[0,:]-np.pi))<1e-12
assert np.max(np.abs(chi[3,:]-chi[1,:]-np.pi))<1e-12
# winding numbers baseline when gamma advances 2pi from each node: physical period=2pi*R/kappa
period=2*np.pi*R/kappa
g2=initial_gammas+2*np.pi
c0=chi_of_gamma(initial_gammas); c2=chi_of_gamma(g2)
assert np.max(np.abs(c2-c0-2*np.pi))<1e-11
# physical nodes on torus
x=(R+a*np.cos(theta))*np.cos(phi)
y=(R+a*np.cos(theta))*np.sin(phi)
z=a*np.sin(theta)
# plot spatial trajectory on surface for first winding, plus 4 initial nodes
fig=plt.figure(figsize=(8,6.4)); ax=fig.add_subplot(111,projection='3d')
θgrid=np.linspace(0,2*np.pi,38); φgrid=np.linspace(0,2*np.pi,60)
TH,PH=np.meshgrid(θgrid,φgrid)
ax.plot_surface((R+a*np.cos(TH))*np.cos(PH),(R+a*np.cos(TH))*np.sin(PH),a*np.sin(TH),color='#92bcca',alpha=.17,linewidth=0)
curve=np.linspace(0,2*np.pi,800)
ax.plot((R+a*np.cos(q*curve))*np.cos(p*curve),(R+a*np.cos(q*curve))*np.sin(p*curve),a*np.sin(q*curve),color='#a33e39',lw=2.5)
ax.scatter(x[:,0],y[:,0],z[:,0],c='#12405a',s=50,depthshade=False)
for i in range(4):
    ax.text(x[i,0],y[i,0],z[i,0]+.11,str(i+1),color='#15354e')
ax.set_box_aspect((1,1,.5));ax.view_init(elev=25,azim=35)
ax.set_title('Cuatro nodos de una doble vuelta sobre el toroide')
ax.set_axis_off();fig.tight_layout();fig.savefig(root/'graficos'/'o87_toro_nodos.png',dpi=180);plt.close(fig)
# plot spatial lag change while normalized lag invariant
fig,ax=plt.subplots(figsize=(8,4.8))
ax.plot(times,lag_deviation,label='Cambio del desfase geométrico entre nodos 1 y 2')
ax.plot(times,normal_lag,label='Cambio del desfase normalizado',linewidth=2)
ax.set_xlabel('Tiempo del modelo');ax.set_ylabel('Diferencia respecto al desfase inicial (rad)')
ax.legend(fontsize=9);ax.grid(alpha=.25);fig.tight_layout();fig.savefig(root/'graficos'/'o87_desfase_movil.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4.8))
for i in range(4):ax.plot(times,pert_phase[i,:],label=f'Nodo {i+1}')
ax.axhline(0,lw=1,color='black',alpha=.35)
ax.set_xlabel('Tiempo del modelo');ax.set_ylabel('Deriva de pθ − qφ (rad)')
ax.set_title('Flujo superficial suave e incompresible: pérdida del acoplamiento')
ax.legend(fontsize=9);ax.grid(alpha=.25);fig.tight_layout();fig.savefig(root/'graficos'/'o87_fase_desacoplada.png',dpi=180);plt.close(fig)

with (root/'resultados'/'nodos_tiempos.csv').open('w',newline='') as h:
    w=csv.writer(h);w.writerow(['tiempo','gamma_1','gamma_2','chi_1','chi_2','delta_chi_menos_pi2','psi_pert_nodo_1','psi_pert_nodo_2','psi_pert_nodo_3','psi_pert_nodo_4'])
    for j in range(len(times)):
        w.writerow([times[j],g[0,j],g[1,j],chi[0,j],chi[1,j],lag_deviation[j],*[pert_phase[i,j] for i in range(4)]])

metrics={'estado':'VERIFICADO EN MODELO CINEMATICO DE SUPERFICIE, NO NS 3D','R':R,'a':a,'kappa':kappa,'p_vueltas_exteriores':p,'q_vueltas_interiores':q,'epsilon_desacoplamiento':epsilon,'periodo_normalizado':period,'max_error_inversion_fase':float(np.max(np.abs(gamma_of_chi(chi)-g))),'max_error_ode':float(num_err),'desfase_normalizado_error_max':float(np.max(np.abs(normal_lag))),'error_max_pares_opuestos_rad':float(max(np.max(np.abs(chi[2,:]-chi[0,:]-np.pi)),np.max(np.abs(chi[3,:]-chi[1,:]-np.pi)))),'desfase_geometrico_variacion_max_abs':float(np.max(np.abs(lag_deviation))),'desfase_geometrico_variacion_min':float(lag_deviation.min()),'desfase_geometrico_variacion_max':float(lag_deviation.max()),'perdida_coherencia_max_abs_radianes':float(np.max(np.abs(pert_phase))),'drift_final_nodos_radianes':[float(v) for v in pert_phase[:,-1]],'fase_deriva_inicial':[float(v) for v in pred_psi_initial],'flujo_superficial_divergencia':'exactamente cero para ambos modelos'}
(root/'resultados'/'resumen.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
print(json.dumps(metrics,ensure_ascii=False,indent=2))
