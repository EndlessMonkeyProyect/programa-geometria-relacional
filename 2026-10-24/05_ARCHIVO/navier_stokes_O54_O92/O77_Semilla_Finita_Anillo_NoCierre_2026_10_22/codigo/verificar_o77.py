#!/usr/bin/env python3
"""O77: no-invarianza de un perfil toroidal gaussiano ante NS axisimétrico sin swirl.
Uso: python codigo/verificar_o77.py (salidas ../datos ../graficos)
Dependencias: sympy numpy matplotlib. No necesita internet.
"""
import json, csv
from pathlib import Path
import sympy as sp
import numpy as np

HOME=Path(__file__).resolve().parents[1]
OUT=HOME/'datos'; FIG=HOME/'graficos'; OUT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
y,z,A,al,be,b=sp.symbols('y z A al be b',real=True)
Q=al*(y-b)**2+be*z**2
E=sp.exp(-Q)
phi=A*E
ur=2*be*sp.sqrt(y)*z*phi
uz=(2-4*al*y*(y-b))*phi
# eta = omega_theta/r = -(phi_zz + 8 phi_y + 4y phi_yy)
eta=-(sp.diff(phi,z,2)+8*sp.diff(phi,y)+4*y*sp.diff(phi,y,2))
P=sp.factor(eta/(A*E))
# for u_r*∂r = 4*beta*y*z*A*e^-Q ∂y; u_z*∂z=(2-4alpha*y(y-b))*A*e^-Q ∂z
conv_poly=sp.factor(4*be*y*z*(sp.diff(P,y)-2*al*(y-b)*P)+(2-4*al*y*(y-b))*(sp.diff(P,z)-2*be*z*P))
conv=A*A*sp.exp(-2*Q)*conv_poly
lap5=8*sp.diff(eta,y)+4*y*sp.diff(eta,y,2)+sp.diff(eta,z,2)
bases=[sp.diff(eta,p) for p in (A,al,be,b)] + [-sp.diff(eta,z)]  # z0 shift

assert sp.simplify(eta-A*E*P)==0
assert sp.simplify((ur*(2*sp.sqrt(y)*sp.diff(eta,y)) + uz*sp.diff(eta,z)) - conv)==0
assert sp.expand(conv_poly).coeff(z,3)==16*be**3
assert sp.simplify(conv.subs(A,2*A)-4*conv)==0
assert sp.simplify(lap5.subs(A,2*A)-2*lap5)==0
assert sp.simplify(conv_poly.subs({al:sp.Rational(1,4),be:1,b:1,y:1,z:sp.Rational(1,2)}))==-2
# divergence-free: ∂r u_r + ur/r + ∂z u_z = 0
assert sp.simplify(2*sp.sqrt(y)*sp.diff(ur,y)+ur/sp.sqrt(y)+sp.diff(uz,z))==0
# eta formula from velocity
assert sp.simplify((sp.diff(ur,z)-2*sp.sqrt(y)*sp.diff(uz,y))/sp.sqrt(y) - eta)==0
# Control positivo independiente: vórtice Lamb–Oseen (columna, NO anillo).
G,w,nu_sym=sp.symbols('G w nu_sym',real=True,nonzero=True)
omegaO=G/(sp.pi*w)*sp.exp(-y/w)
assert sp.simplify(4*nu_sym*sp.diff(omegaO,w)-4*nu_sym*(sp.diff(omegaO,y)+y*sp.diff(omegaO,y,2)))==0

fun_eta=sp.lambdify((y,z,A,al,be,b),eta,'numpy', cse=True)
fun_adv=sp.lambdify((y,z,A,al,be,b),conv,'numpy', cse=True)
fun_diff=sp.lambdify((y,z,A,al,be,b),lap5,'numpy', cse=True)
fun_bases=[sp.lambdify((y,z,A,al,be,b),T,'numpy',cse=True) for T in bases]
fun_ur=sp.lambdify((y,z,A,al,be,b),ur,'numpy', cse=True)
fun_uz=sp.lambdify((y,z,A,al,be,b),uz,'numpy', cse=True)

# Quadrature en r≥0, z∈R: cortes fuera de la campana; los promedios se verifican con dos mallas.
def experiment(N,nu,params):
    r=np.linspace(0.001,2.35,N)
    zz=np.linspace(-1.2,1.2,N+9)
    RR,ZZ=np.meshgrid(r,zz,indexing='ij'); YY=RR**2
    pars=(YY,ZZ,*params)
    w=(RR*(r[1]-r[0])*(zz[1]-zz[0])).ravel() # measure r dr dz
    adv=np.asarray(fun_adv(*pars),float).ravel()
    visc=np.asarray(fun_diff(*pars),float).ravel()
    total=-adv+nu*visc
    BT=np.stack([np.broadcast_to(np.asarray(f(*pars),float),RR.shape).ravel() for f in fun_bases],axis=1)
    def fit(target):
        # scale basis for conditioning; least-squares weighted by cylindrical volume element
        W=np.sqrt(w)
        B=BT*W[:,None]
        norm=np.linalg.norm(B,axis=0)
        B=B/norm[None,:]
        coef=np.linalg.lstsq(B,target*W,rcond=1e-11)[0]/norm
        proj=BT@coef
        nr=np.sqrt(np.sum(w*(target-proj)**2))
        nt=np.sqrt(np.sum(w*target**2))
        return dict(norm=float(nt),residual=float(nr),relative=(float(nr/nt) if nt>0 else None),coefficients=[float(x) for x in coef])
    return {'N':int(N),'nu':float(nu),'params':dict(zip(['A','alpha','beta','b'],[float(x) for x in params])),
            'advection':fit(-adv),'viscosity':fit(nu*visc),'full_RHS':fit(total),
            'eta_max':float(np.max(np.abs(fun_eta(*pars)))),
            'velocity_rms':float(np.sqrt(np.sum(w*(np.asarray(fun_ur(*pars)).ravel()**2+np.asarray(fun_uz(*pars)).ravel()**2))/np.sum(w)))}

if __name__=='__main__':
    # R=1, a=.32 ⇒ alpha=1/(4 R²a²), beta=1/a²
    ra=.32; pars=(.24,1/(4*ra*ra),1/(ra*ra),1.)
    runs=[experiment(N,nu,pars) for N in (100,160) for nu in (0.0,0.025)]
    for x in runs: print('N,nu',x['N'],x['nu'],'relative adv',round(x['advection']['relative'],7), 'full',round(x['full_RHS']['relative'],7))
    assert all(x['advection']['relative']>0.05 for x in runs)
    assert all(x['full_RHS']['relative']>0.05 for x in runs)
    for nu in (0.0,.025):
        a1=[x for x in runs if x['N']==100 and x['nu']==nu][0]
        a2=[x for x in runs if x['N']==160 and x['nu']==nu][0]
        assert abs(a1['full_RHS']['relative']-a2['full_RHS']['relative'])<.02
    (OUT/'resultados_o77.json').write_text(json.dumps({'theory':{'advected_eta_coefficient_z3':'16*beta**3','nonzero_witness':'-2 at alpha=1/4,beta=b=y=1,z=1/2','no_gaussian_finite_param_invariance':True},'runs':runs},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with (OUT/'residuos_o77.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['N','nu','adveccion_relativa','RHS_relativo','RHS_norma'])
        for d in runs:w.writerow([d['N'],d['nu'],d['advection']['relative'],d['full_RHS']['relative'],d['full_RHS']['norm']])
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    rr=np.linspace(0,1.95,240); zz=np.linspace(-.88,.88,230); RR,ZZ=np.meshgrid(rr,zz,indexing='ij')
    data=np.asarray(fun_eta(RR**2,ZZ,*pars),float)
    plt.figure(figsize=(7,4.5));plt.pcolormesh(ZZ,RR,data,shading='auto',cmap='RdBu_r');plt.colorbar(label='eta = omega_theta/r');plt.xlabel('z');plt.ylabel('r');plt.title('O77: perfil toroidal de vorticidad inicial (modelo, no solución exacta)');plt.tight_layout();plt.savefig(FIG/'o77_toroide_eta.png',dpi=170);plt.close()
    zz=np.linspace(-.72,.72,350);yy=np.ones_like(zz)
    adv=-np.asarray(fun_adv(yy,zz,*pars),float)
    diff=.025*np.asarray(fun_diff(yy,zz,*pars),float)
    plt.figure(figsize=(7,4.2));plt.plot(zz,adv,label='Transporte no lineal -u·∇eta');plt.plot(zz,diff,label='Difusión viscosa νΔ₅eta');plt.plot(zz,adv+diff,label='Derivada total ∂t eta');plt.xlabel('z, a radio r=R');plt.ylabel('Tasa local');plt.title('O77: relaciones que la semilla gaussiana no conserva');plt.legend();plt.tight_layout();plt.savefig(FIG/'o77_transporte_perfil.png',dpi=170);plt.close()
    print('symbolic conditions: PASSED; numeric experiment: PASSED')
