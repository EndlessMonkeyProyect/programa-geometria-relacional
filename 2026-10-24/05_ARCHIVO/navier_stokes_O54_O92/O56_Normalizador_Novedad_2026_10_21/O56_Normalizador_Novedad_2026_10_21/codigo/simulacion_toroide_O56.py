"""O55: exploratory incompressible 3D spectral Navier--Stokes vortex-ring test.
Run: python O55_simulacion.py
Uses 3D periodic box, spectral Leray projection, 2/3 dealiasing,
explicit midpoint time stepping, and material surface tracers.
This is a numerical exploratory test, not a proof of vortex persistence.
"""
from pathlib import Path
import numpy as np
import csv, json

OUT=Path(__file__).resolve().parents[1]
N=32
Lbox=8.0
dx=Lbox/N
nu=0.025
dt=0.014
nsteps=90
R0=1.60
r0=0.48
shear_amp=0.22
mirror_rate=0.23
xgrid=(np.arange(N)-N//2)*dx
xx,yy,zz=np.meshgrid(xgrid,xgrid,xgrid,indexing='ij')
rho=np.sqrt(xx**2+yy**2)
k=2*np.pi*np.fft.fftfreq(N,d=dx)
kx,ky,kz=np.meshgrid(k,k,k,indexing='ij')
kvec=np.stack([kx,ky,kz])
k2=kx**2+ky**2+kz**2
k2safe=k2.copy(); k2safe[0,0,0]=1
modes=np.fft.fftfreq(N)*N
m1,m2,m3=np.meshgrid(modes,modes,modes,indexing='ij')
filter_23=(np.abs(m1)<N/3)&(np.abs(m2)<N/3)&(np.abs(m3)<N/3)
filter_23[0,0,0]=True

def fftvec(x): return np.fft.fftn(x,axes=(-3,-2,-1))
def ifftvec(h): return np.fft.ifftn(h,axes=(-3,-2,-1)).real

def cross(a,b):
    return np.stack([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])

def project(h):
    kd=kx*h[0]+ky*h[1]+kz*h[2]
    result=h-kvec*(kd/k2safe)
    result[:,0,0,0]=0
    return result*filter_23

def init_vortex(perturbed):
    omega_phi=1.8*np.exp(-((rho-R0)**2+zz**2)/(r0**2))
    rh=np.maximum(rho,1e-12)
    w=np.stack([-omega_phi*yy/rh,omega_phi*xx/rh,np.zeros_like(rho)])
    wh=project(fftvec(w))
    # curl(u) = omega => uhat = i*(k cross omega_hat)/|k|^2
    uh=1j*cross(kvec,wh)/k2safe
    uh[:,0,0,0]=0
    if perturbed:
        shear=np.stack([np.zeros_like(rho),shear_amp*np.sin(2*np.pi*zz/Lbox),np.zeros_like(rho)])
        uh+=project(fftvec(shear))
    return project(uh)

def rhs(uh):
    u=ifftvec(uh)
    w=ifftvec(1j*cross(kvec,uh))
    # rotational form: u_t = P(u cross omega)+nu Delta u
    nh=project(fftvec(cross(u,w)))
    return nh-nu*k2*uh, u, w

def sample_velocity(u, p):
    # periodic trilinear interpolation (p: number_of_tracers x 3)
    pos=((p+Lbox/2)/dx)%N
    lo=np.floor(pos).astype(int)
    f=pos-lo
    values=np.zeros_like(p)
    for ix in (0,1):
        wx=(f[:,0] if ix else 1-f[:,0])
        ii=(lo[:,0]+ix)%N
        for iy in (0,1):
            wy=(f[:,1] if iy else 1-f[:,1])
            jj=(lo[:,1]+iy)%N
            for iz in (0,1):
                wz=(f[:,2] if iz else 1-f[:,2])
                kk=(lo[:,2]+iz)%N
                values += (wx*wy*wz)[:,None]*u[:,ii,jj,kk].T
    return values

phis=np.linspace(0,2*np.pi,24,endpoint=False)
thetas=np.linspace(0,2*np.pi,16,endpoint=False)
P,T=np.meshgrid(phis,thetas,indexing='ij')
initial_surface=np.column_stack([((R0+r0*np.cos(T))*np.cos(P)).ravel(),
                                  ((R0+r0*np.cos(T))*np.sin(P)).ravel(),
                                  (r0*np.sin(T)).ravel()])
nsurf=len(initial_surface)
th=np.pi/4
xc=np.array([R0+r0*np.cos(th),0,r0*np.sin(th)])
a0=np.array([0.,1.,0.])
b0=np.array([-np.sin(th),0,np.cos(th)])
epsilon=0.028
tracers_init=np.concatenate([initial_surface, np.array([xc,xc+epsilon*a0,xc+epsilon*b0])],axis=0)

def summary(uh,pts,t):
    u=ifftvec(uh)
    omega=ifftvec(1j*cross(kvec,uh))
    div=ifftvec((1j*(kx*uh[0]+ky*uh[1]+kz*uh[2]))[None])[0]
    energy=0.5*np.mean(np.sum(u*u,axis=0))
    enstrophy=0.5*np.mean(np.sum(omega*omega,axis=0))
    surf=pts[:nsurf]
    rr=np.sqrt(surf[:,0]**2+surf[:,1]**2)
    Reff=np.mean(rr)
    zc=np.mean(surf[:,2])
    reff=np.sqrt(np.mean((rr-Reff)**2+(surf[:,2]-zc)**2))
    p0,pa,pb=pts[-3:]
    av=pa-p0; bv=pb-p0
    angle_cos=np.dot(av,bv)/(np.linalg.norm(av)*np.linalg.norm(bv))
    # pure observational mirror: L_ref grows; no effect on physical velocity
    Lref=np.exp(mirror_rate*t)
    return dict(t=float(t),E=float(energy),Z=float(enstrophy),
                divergence_max=float(np.max(np.abs(div))),
                R_eff=float(Reff),r_eff=float(reff),q=float(reff/Reff),
                R_observed=float(Reff/Lref),r_observed=float(reff/Lref),
                L_ref=float(Lref),angle_cos=float(angle_cos),
                local_angle_deg=float(np.degrees(np.arccos(np.clip(angle_cos,-1,1)))),
                z_surface_mean=float(zc),
                max_u=float(np.max(np.sqrt(np.sum(u*u,axis=0)))))

def simulate(perturbed):
    uh=init_vortex(perturbed)
    pts=tracers_init.copy()
    records=[]
    for j in range(nsteps+1):
        if j%10==0 or j==nsteps:
            row=summary(uh,pts,j*dt)
            row['condition']='perturbado' if perturbed else 'simetrico'
            records.append(row)
        if j==nsteps: break
        dudt,u,_=rhs(uh)
        umid_hat=project(uh+0.5*dt*dudt)
        dudt_mid,umid,_=rhs(umid_hat)
        vp=sample_velocity(u,pts)
        pts_mid=pts+0.5*dt*vp
        vpmid=sample_velocity(umid,pts_mid)
        pts=(pts+dt*vpmid+Lbox/2)%Lbox-Lbox/2
        uh=project(uh+dt*dudt_mid)
    return records, pts


# O56 addendum: con el MISMO perfil base vorticial, se agrega cizalla x/y,
# amplitud y espectro idénticos en ambas preparaciones; sin forzamiento.
_init_vortex_base = init_vortex
def init_vortex(direction):
    uh = _init_vortex_base(False)
    if direction in ('x','y'):
        wave=shear_amp*np.sin(2*np.pi*zz/Lbox)
        zero=np.zeros_like(wave)
        perturbation = np.stack([wave,zero,zero]) if direction=='x' else np.stack([zero,wave,zero])
        uh=project(uh+project(fftvec(perturbation)))
    elif direction!='ninguna':
        raise ValueError('direccion desconocida')
    return uh

if __name__=='__main__':
    data=[]
    fin={}
    for direction in ['ninguna','x','y']:
        records,points=simulate(direction)
        for row in records:
            row['condition']=direction
        data.extend(records)
        fin[direction]={'E_inicial':records[0]['E'],'Z_inicial':records[0]['Z'],
                'q_inicial':records[0]['q'],'angulo_inicial':records[0]['local_angle_deg'],
                'angulo_final':records[-1]['local_angle_deg'],
                'q_final':records[-1]['q'],'E_final':records[-1]['E'],
                'div_max':records[-1]['divergence_max']}
    assert abs(fin['x']['E_inicial']-fin['y']['E_inicial']) < 1e-10
    assert abs(fin['x']['Z_inicial']-fin['y']['Z_inicial']) < 1e-10
    assert all(abs(fin[s]['q_inicial']-0.3)<1e-12 for s in fin)
    import csv,json
    with (OUT/'resultados'/'toroide_N32_orientaciones.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(data[0]));wr.writeheader();wr.writerows(data)
    (OUT/'resultados'/'toroide_N32_resumen.json').write_text(json.dumps({'preparaciones':fin,'N':N,'dt':dt,'nsteps':nsteps,'nu':nu,
         'limites':'ensayo NS Galerkin a baja resolucion, no flujo analitico exacto ni prueba global'},indent=2,ensure_ascii=False))
    print(json.dumps(fin,indent=2,ensure_ascii=False))
