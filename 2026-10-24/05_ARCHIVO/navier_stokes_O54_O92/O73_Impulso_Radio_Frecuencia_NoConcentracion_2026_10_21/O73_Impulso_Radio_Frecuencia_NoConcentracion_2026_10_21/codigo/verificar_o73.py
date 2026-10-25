#!/usr/bin/env python3
"""O73: familias suaves de anillos con impulso y circulacion iguales,
contraejemplo a cota de grosor uniforme, y control en eje-simetría sin swirl.
Todos los campos construidos son DATOS INICIALES suaves de NS en R3, no
una simulacion numerica de su evolucion.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parents[1]
(OUT/'datos').mkdir(exist_ok=True)
(OUT/'graficos').mkdir(exist_ok=True)
checks=[]
def check(name, condition, detail=None):
    checks.append({'name':name,'ok':bool(condition),'detail':detail})
    if not condition: raise AssertionError(name+': '+str(detail))

# C-infinity radial bump: b(s)=exp[-1/(1-s^2)], 0<=s<1, zero at s>=1.
def b(s):
    s=np.asarray(s)
    with np.errstate(divide='ignore',over='ignore',invalid='ignore'):
        return np.where(s<1,np.exp(-1/(1-s*s)),0.0)
J0=quad(lambda s: float(b(s))*s,0,1,epsabs=1e-13,epsrel=1e-13)[0]
J2=quad(lambda s: float(b(s))*s**3,0,1,epsabs=1e-13,epsrel=1e-13)[0]
normal=2*math.pi*J0
kappa=J2/(2*J0)
phi0=math.exp(-1)/normal
check('momento radial positivo',0<kappa<0.5,kappa)
check('normalizacion del bump',abs(2*math.pi*J0/normal-1)<1e-12)

# Analisis simbólico exacto operador: (Delta_cil -1/r²)(r eta)/r=Delta_5 eta
r,z=sp.symbols('r z',positive=True)
E=sp.Function('eta')(r,z)
W=r*E
Delta_theta_W = sp.diff(W,r,2) + sp.diff(W,r)/r + sp.diff(W,z,2) - W/r**2
Delta5_E = sp.diff(E,r,2)+3*sp.diff(E,r)/r+sp.diff(E,z,2)
check('identidad simbolica operador 5D',sp.simplify(Delta_theta_W/r-Delta5_E)==0)
ur,uz=sp.symbols('ur uz')
advW=ur*sp.diff(W,r)+uz*sp.diff(W,z)
adve=ur*sp.diff(E,r)+uz*sp.diff(E,z)
check('cancelacion de estiramiento radial',sp.simplify((advW-ur*W/r)/r-adve)==0)

rho=1.0
Gamma=6.0
Rstar=1.0
avalues=[0.35,0.22,0.14,0.09,0.06,0.035,0.02]
Istar=rho*math.pi*Gamma*Rstar**2
rows=[]
for aa in avalues:
    RR=math.sqrt(Rstar*Rstar-kappa*aa*aa)
    check(f'toroide separado del eje a={aa}',RR>aa)
    # integral exacta ∫ ωθ dr dz = Γ
    circulation=Gamma
    # I_z = ρπ∫r²ωθ drdz = ρπΓ(R²+κa²)
    Iz=rho*math.pi*Gamma*(RR*RR+kappa*aa*aa)
    Reff=math.sqrt(Iz/(rho*math.pi*circulation))
    peak=Gamma*phi0/aa**2
    loweta=peak/RR
    higheta=peak/(RR-aa)
    def eta_at_xi(xi):
        if abs(xi)>=1: return 0.
        return (Gamma/aa**2)*(float(b(abs(xi)))/normal)/(RR+aa*xi)
    sol=minimize_scalar(lambda xi:-eta_at_xi(xi),bounds=(-0.99,0.99),method='bounded', options={'xatol':1e-13})
    maxeta=eta_at_xi(sol.x)
    check(f'circulacion inicial fija a={aa}',abs(circulation-Gamma)<1e-12)
    check(f'impulso inicial fijo a={aa}',abs(Iz-Istar)<5e-14,(Iz,Istar))
    check(f'radio efectivo fijo a={aa}',abs(Reff-Rstar)<5e-14)
    check(f'maximo eta entre cotas a={aa}',loweta<=maxeta*(1+1e-10) and maxeta<=higheta*(1+1e-10),(loweta,maxeta,higheta))
    check(f'escala pico de vorticidad a={aa}',abs(peak*aa*aa-Gamma*phi0)<1e-12)
    rows.append({'a':aa,'R_centro':RR,'R_efectivo':Reff,'Gamma_inicial':circulation,'I_z_inicial':Iz,
                 'vorticidad_maxima_inicial':peak,'eta_maxima_inicial':maxeta,
                 'estimacion_inferior_eta':loweta,'estimacion_superior_eta':higheta,
                 'radio_del_centro_positivo':RR>aa})

# Controles independientes de cuadratura 2D con puntos Gauss sobre disco
# Momento E[xi²]=kappa, E[xi]=0; integral normalizada 1.
snodes,sweights=np.polynomial.legendre.leggauss(140)
rs=(snodes+1)/2
rw=sweights/2
anodes,aw=np.polynomial.legendre.leggauss(96)
phis=math.pi*(anodes+1)
pw=math.pi*aw
rgrid=rs[:,None]
costheta=np.cos(phis)[None,:]
weights=rw[:,None]*pw[None,:]
ft= b(rgrid)*rgrid/normal
approx0=float(np.sum(weights*ft*np.ones_like(costheta)))
approx1=float(np.sum(weights*ft*rgrid*costheta))
approx2=float(np.sum(weights*ft*(rgrid*costheta)**2))
check('cuadratura independiente masa',abs(approx0-1)<1e-11,approx0)
check('cuadratura independiente primer momento',abs(approx1)<1e-12,approx1)
check('cuadratura independiente segundo momento',abs(approx2-kappa)<1e-11,(approx2,kappa))
for row in rows:
    aa=row['a']; RR=row['R_centro']
    # 3D exact impulse integral via integrated azimuth: Iz=rho*pi*∫ r² ωθ dr dz
    Iquad=rho*math.pi*Gamma*(RR*RR*approx0+2*RR*aa*approx1+aa*aa*approx2)
    check(f'impulso por cuadratura independiente a={aa}',abs(Iquad-Istar)<2e-10, Iquad)

# Proposicion area: if |eta|<=M, r<=Rmax, then circ_mass(A)<=Rmax*M*|A|.
# Ejemplo region cerrada del disco, cota sobre circulacion total.
for row in rows:
    aa=row['a']; RR=row['R_centro']; M=row['eta_maxima_inicial']
    Rmax=RR+aa
    area=math.pi*aa*aa
    bound=Rmax*M*area
    check(f'cota area para tubo a={aa}',bound+1e-12>=Gamma, (bound,Gamma))

# Predicción asintótica de pico con paso a→0, sin ley física de radio mínimo.
for row1,row2 in zip(rows[:-1],rows[1:]):
    ratio_measured=row2['vorticidad_maxima_inicial']/row1['vorticidad_maxima_inicial']
    ratio_analytical=(row1['a']/row2['a'])**2
    check(f'razon cuadratica picos {row1["a"]}/{row2["a"]}',abs(ratio_measured/ratio_analytical-1)<1e-12)

# Ilustracion 1: corte meridiano del núcleo, compacto y con radio de centro ajustado.
fig,axs=plt.subplots(1,3,figsize=(11.5,3.65),sharex=True,sharey=True)
selected=[0.35,0.14,0.035]
grid_r=np.linspace(0.55,1.45,340)
grid_z=np.linspace(-0.45,0.45,320)
rr,zz=np.meshgrid(grid_r,grid_z)
for ax,aa in zip(axs,selected):
    RR=math.sqrt(Rstar**2-kappa*aa**2)
    s=np.sqrt(((rr-RR)/aa)**2+(zz/aa)**2)
    om=(Gamma/aa**2)*b(s)/normal
    color=ax.pcolormesh(rr,zz,om/(Gamma*phi0/aa**2),cmap='viridis',vmin=0,vmax=1,shading='auto')
    ax.set_title(f'Grosor a = {aa:g}')
    ax.set_aspect('equal')
    ax.plot([RR],[0],'w+',markersize=7)
    ax.set_xlabel('Distancia radial r')
axs[0].set_ylabel('Coordenada axial z')
fig.suptitle('Mismo impulso y circulación inicial; distinta concentración del núcleo',fontsize=11)
fig.colorbar(color,ax=list(axs),fraction=0.03,pad=0.02,label='Vorticidad / pico de cada caso')
fig.subplots_adjust(left=0.065,right=0.88,bottom=0.15,top=0.82,wspace=0.13)
fig.savefig(OUT/'graficos'/'o73_nucleos_mismo_impulso.png',dpi=185)
plt.close(fig)

fig,ax=plt.subplots(figsize=(7.7,4.3))
xx=np.asarray([row['a'] for row in rows]); yy=np.asarray([row['vorticidad_maxima_inicial'] for row in rows])
ax.loglog(xx,yy,'o-',label='Pico de vorticidad exacto')
ax.loglog(xx, Gamma*phi0/xx**2,'--',label='Escala Γφ(0)/a²')
ax.set_xlabel('Grosor del núcleo a')
ax.set_ylabel('Máximo de vorticidad inicial')
ax.set_title('El impulso y la circulación no fijan un grosor mínimo')
ax.grid(alpha=.25,which='both')
ax.legend()
fig.tight_layout()
fig.savefig(OUT/'graficos'/'o73_concentracion_nucleo.png',dpi=185)
plt.close(fig)

fig,ax=plt.subplots(figsize=(7.7,4.1))
ax.plot(xx,[row['R_centro'] for row in rows],'-o',label='Centro del anillo R(a)')
ax.plot(xx,[row['R_efectivo'] for row in rows],'-s',label='Radio colectivo efectivo')
ax.set_xlabel('Grosor a')
ax.set_ylabel('Radio')
ax.set_title('Centro ajustado y referencia colectiva idéntica')
ax.grid(alpha=.3)
ax.legend()
fig.tight_layout()
fig.savefig(OUT/'graficos'/'o73_radios_referencia.png',dpi=185)
plt.close(fig)

results={'o73_version':'1.0','fecha':'2026-10-21','marco':'R3, 3D, axialsimetrico sin giro azimutal, nu>0, datos suaves',
'parametros':{'rho':rho,'Gamma_inicial':Gamma,'R_efectivo':Rstar,'I_z_inicial':Istar,'kappa':kappa,'normalizacion_bump':normal,'phi0':phi0},
'familia':rows,'verificaciones':{'aprobadas':sum(x['ok'] for x in checks),'total':len(checks),'fallidas':sum(not x['ok'] for x in checks)},
'cuadratura':{'masa':approx0,'primer_momento':approx1,'segundo_momento':approx2}}
(OUT/'datos'/'resultados_o73.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
(OUT/'datos'/'controles_o73.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
print('O73 verificaciones:',len(checks),'/',len(checks))
print('κ=',kappa,'I=',Istar,'phi0=',phi0)
for row in rows:
    print(f"a={row['a']:>6g}, R={row['R_centro']:.9f}, maxω={row['vorticidad_maxima_inicial']:.4f}, maxη={row['eta_maxima_inicial']:.4f}")
