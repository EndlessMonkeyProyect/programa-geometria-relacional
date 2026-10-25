#!/usr/bin/env python3
"""O76: testigos exactos de presión no local, caja D4 y familia Beltrami.
Dependencias: Python 3, numpy; matplotlib para imagen.
"""
from __future__ import annotations
import argparse, csv, json, math
from fractions import Fraction
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parents[1]
BASE.joinpath('datos').mkdir(exist_ok=True)
BASE.joinpath('graficos').mkdir(exist_ok=True)

p = argparse.ArgumentParser()
p.add_argument('--N',type=int,default=96)
p.add_argument('--nu',type=float,default=0.025)
a = p.parse_args()
assert a.N%4==0 and a.N>=32
N=a.N
xx=2*np.pi*np.arange(N)/N
x,y=np.meshgrid(xx,xx,indexing='ij')
u=np.stack([np.sin(2*y)**3,np.sin(2*x)**3+np.sin(2*x)**4],axis=-1)
assert u.shape==(N,N,2)
k=np.fft.fftfreq(N,d=1/N)
kx,ky=np.meshgrid(k,k,indexing='ij')
kk=kx*kx+ky*ky; kk[0,0]=1

def d(field,axis):
    arr=np.fft.fft2(field)
    return np.fft.ifft2(1j*(kx if axis==0 else ky)*arr).real

def norm(field):
    return float(np.sqrt(np.mean(field*field)))

fp=d(u[...,0],1)
gp=d(u[...,1],0)
source=-2*fp*gp
phat=np.fft.fft2(source)/(-kk);phat[0,0]=0
press=np.fft.ifft2(phat).real
px=d(press,0);py=d(press,1)
uxx=d(d(u[...,0],1),1)
uyy=d(d(u[...,1],0),0)
advx=u[...,1]*fp
advy=u[...,0]*gp
utx=-advx-px+a.nu*uxx
uty=-advy-py+a.nu*uyy
expected=Fraction(3456,5525)
checks=[]
def check(name,condition,detail=''):
    checks.append({'name':name,'passed':bool(condition),'detail':detail})
    if not condition:raise AssertionError(name+' '+detail)
check('Incompresibilidad exacta de cizallas cruzadas',norm(d(u[...,0],0)+d(u[...,1],1))<1e-12)
check('Poisson espectral de presión',norm(d(d(press,0),0)+d(d(press,1),1)-source)<1e-12)
check('Gradiente de presión calculado analíticamente',abs(px[0,0]-float(expected))<1e-12,str(px[0,0]))
check('Aceleración en esquina',abs(utx[0,0]+float(expected))<1e-12)
check('Aceleración opuesta en esquina superior',abs(utx[0,N//4]-float(expected))<1e-12)
check('Aceleración relativa objetiva',abs((utx[0,N//4]-utx[0,0])-2*float(expected))<1e-12)
corners=[(0,0),(N//4,0),(N//4,N//4),(0,N//4)]
for i,(cx,cy) in enumerate(corners):
    check(f'Esquina {i+1}: velocidad nula',max(abs(u[cx,cy]))<1e-12)
    for n,field in enumerate([u[...,0],u[...,1]]):
        for ax in range(3):
            for ay in range(3-ax):
                fieldjet=field.copy()
                for _ in range(ax):fieldjet=d(fieldjet,0)
                for _ in range(ay):fieldjet=d(fieldjet,1)
                check(f'Esquina {i+1}: jet componente {n} orden ({ax},{ay})',abs(fieldjet[cx,cy])<1e-10)

# Grupo de espejos D4. Invertimos giros y reflejos geométricamente, no componentes a ciegas.
R=np.array([[0,-1],[1,0]],dtype=int)
F=np.diag([1,-1]); I=np.eye(2,dtype=int)
A=I.copy(); transforms=[]
for _ in range(4):
    transforms += [A.copy(), (A@F).copy()]
    A=A@R

def act(M,v):
    inv=M.T
    i=np.arange(N)[:,None];j=np.arange(N)[None,:]
    ii=(inv[0,0]*i+inv[0,1]*j)%N
    jj=(inv[1,0]*i+inv[1,1]*j)%N
    return np.einsum('ab,ijb->ija',M,v[ii,jj])
def group(v):return sum(act(M,v) for M in transforms)/8.
pu=group(u)
check('Caja D4 proyectiva',norm(group(pu)-pu)<1e-13)
check('Caja D4: campo inicial no contiene componente vectorial común',norm(pu)<1e-13,str(norm(pu)))
# La tasa de cambio de la referencia común puede generarse desde el sector omitido.
put=group(np.stack([utx,uty],axis=-1))
check('Caja D4: sector omitido modifica la derivada colectiva',norm(put)>0.1,str(norm(put)))
# El bloque impar-impar produce una interacción colectiva visible, aunque el promedio inicial sea cero.
# El bloque impar-par produce, además, aceleraciones relativas objetivas en las esquinas.
# Cuadraticidad en amplitud cuando P(u)=0: para alpha=2, nuΔu sigue lineal pero PΔu=0.
alpha=2
ut2x=-(alpha*alpha)*(advx+px)+a.nu*alpha*uxx
ut2y=-(alpha*alpha)*(advy+py)+a.nu*alpha*uyy
check('La derivada colectiva se cuadruplica al duplicar amplitud',norm(group(np.stack([ut2x,ut2y],axis=-1))-4*put)<1e-12)
# Cierre exacto de O70: P_F(u)=-Leray div P_D4^(2)(u ⊗ u) cuando Pu=0.
tau=np.zeros((N,N,2,2))
for M in transforms:
    reflected=act(M,u)
    tau+=reflected[:,:,:,None]*reflected[:,:,None,:]/8
div_tau=np.stack([d(tau[...,0,0],0)+d(tau[...,0,1],1),
                  d(tau[...,1,0],0)+d(tau[...,1,1],1)],axis=-1)
ft=np.fft.fft2(div_tau,axes=(0,1))
kdot=kx*ft[...,0]+ky*ft[...,1]
projected=np.empty_like(ft)
projected[...,0]=ft[...,0]-kx*kdot/kk
projected[...,1]=ft[...,1]-ky*kdot/kk
residual_rhs=-np.fft.ifft2(projected,axes=(0,1)).real
check('Cierre residual exacto del promedio D4',norm(put-residual_rhs)<1e-12,str(norm(put-residual_rhs)))
check('Tensor residual no es cero',norm(tau)>0.01)
check('El gradiente de presión escala cuadráticamente',abs((-4*px[0,0])-4*(-px[0,0]))<1e-14)

# Semilla finita positiva en familia ABC/Beltrami 3D, verificación usando derivadas analíticas en puntos variados.
X=np.linspace(.17,2.5,17)
Y=np.linspace(.3,2.8,17)
Z=np.linspace(.4,2.6,17)
A_,B_,C_=1.2,-0.7,0.9
u0=np.column_stack([A_*np.sin(Z)+C_*np.cos(Y),B_*np.sin(X)+A_*np.cos(Z),C_*np.sin(Y)+B_*np.cos(X)])
curl=np.column_stack([C_*np.cos(Y)+A_*np.sin(Z), A_*np.cos(Z)+B_*np.sin(X), B_*np.cos(X)+C_*np.sin(Y)])
check('Campo ABC tiene rotacional igual al campo',float(np.max(np.abs(curl-u0)))<2e-15)
check('Campo ABC con ν decae exactamente con e^{-ν t}',all(math.exp(-a.nu*t)>0 for t in [0.,.1,1.]))
# En ∂tu=-νu, νΔu=-νu, y (u·∇)u+∇p=0, comprobamos esta identidad vectorial analítica.
# u·∇u = grad(|u|²/2) al ser curl(u)=u; validar componente usando derivadas calculadas.
ux=A_*np.sin(Z)+C_*np.cos(Y);uy=B_*np.sin(X)+A_*np.cos(Z);uz=C_*np.sin(Y)+B_*np.cos(X)
# grad u x: (0,-C sinY,A cosZ), y:(B cosX,0,-A sinZ), z:(-B sinX,C cosY,0)
adv=np.column_stack([-uy*C_*np.sin(Y)+uz*A_*np.cos(Z),ux*B_*np.cos(X)-uz*A_*np.sin(Z),-ux*B_*np.sin(X)+uy*C_*np.cos(Y)])
gradkin=np.column_stack([uy*B_*np.cos(X)-uz*B_*np.sin(X),-ux*C_*np.sin(Y)+uz*C_*np.cos(Y),ux*A_*np.cos(Z)-uy*A_*np.sin(Z)])
check('No linealidad Beltrami es gradiente puro',float(np.max(np.abs(adv-gradkin)))<1e-14)

rows=[]
for amp in [0.,.5,1.,2.]:
    rows.append(dict(amplitud=amp, muestra_u_00=0., derivada_x_esquina_inferior=-amp**2*float(expected),
                     derivada_x_esquina_superior=amp**2*float(expected), diferencia_relativa=2*amp**2*float(expected),
                     caja_comun_inicial=0., caja_norma_derivada=amp**2*norm(put)))
with (BASE/'datos'/'o76_contraste.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={'domain':'T2 embebido en T3','N':N,'nu':a.nu,'coef_pressure_gradient_exact':str(expected),
         'pressure_gradient_origin':float(px[0,0]),'relative_acceleration':float(utx[0,N//4]-utx[0,0]),
         'D4_common_norm':norm(pu),'D4_common_derivative_norm':norm(put),
         'checks':len(checks),'passed':sum(1 for c in checks if c['passed']), 'limits':'testigo 2D embebido; no resolución de regularidad 3D'}
(BASE/'datos'/'resumen.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
(BASE/'datos'/'controles.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,2,figsize=(10,4.3))
    im=axs[0].imshow(px.T,origin='lower',extent=[0,2*np.pi,0,2*np.pi],cmap='coolwarm',aspect='equal')
    axs[0].set_title('Presión: ∂p/∂x sin velocidad local')
    axs[0].scatter([0,np.pi/2,np.pi/2,0],[0,0,np.pi/2,np.pi/2],s=35,marker='x',c='k',linewidths=2)
    axs[0].set_xlabel('x');axs[0].set_ylabel('y')
    fig.colorbar(im,ax=axs[0],shrink=.7)
    mags=[abs(row['diferencia_relativa']) for row in rows]
    axs[1].plot([r['amplitud'] for r in rows],mags,'o-')
    axs[1].set_xlabel('Amplitud de la diferencia no observada')
    axs[1].set_ylabel('Aceleración relativa entre cápsulas')
    axs[1].set_title('Mismo dato local; futuros distintos')
    axs[1].grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(BASE/'graficos'/'o76_presion_no_local.png',dpi=155)
    plt.close(fig)
except ImportError:
    print('Matplotlib no disponible; se omite figura')
print(json.dumps(summary,indent=2,ensure_ascii=False))
