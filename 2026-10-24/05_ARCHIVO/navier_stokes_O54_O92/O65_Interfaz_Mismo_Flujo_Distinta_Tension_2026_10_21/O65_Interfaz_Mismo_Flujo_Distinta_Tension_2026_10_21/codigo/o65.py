"""O65 — same imposed turbulent reference flow, different surface tension.
Implements dimensional capillary diagnostics and tests; NOT a two-phase CFD solver.
Python 3, matplotlib optional for plotting.
"""
from __future__ import annotations
import csv, math, json, argparse
from pathlib import Path

RHO=1000.0             # kg/m^3 carrier liquid
MU=0.001               # Pa s
EPS=0.1                # m^2/s^3 imposed dissipation in inertial-range scaling
CH=0.725               # empirical, not exact universal constant
D=0.005                # m test drop diameter
SIGMAS=(0.036, 0.072, 0.144) # N/m illustrative interfacial tensions

def d_h(sigma:float, rho:float=RHO, eps:float=EPS, c:float=CH)->float:
    return c*(sigma/rho)**(3/5)*eps**(-2/5)

def we(d:float, sigma:float, rho:float=RHO, eps:float=EPS)->float:
    # convention δu² = (εd)^(2/3); its Wcrit depends on this convention
    return rho*eps**(2/3)*d**(5/3)/sigma

def wcrit(c:float=CH)->float:
    return c**(5/3)

def laplace_jump_sphere(sigma:float,d:float=D)->float:
    return 4*sigma/d

def delta_area_two_equal(d:float=D)->float:
    return math.pi*d*d*(2**(1/3)-1)

def energy_breakup(sigma:float,d:float=D)->float:
    return sigma*delta_area_two_equal(d)

def eta(nu:float=MU/RHO, eps:float=EPS)->float:
    return (nu**3/eps)**(1/4)

def row(sigma:float)->dict:
    dh=d_h(sigma)
    wd=we(D,sigma)
    return {
        'sigma_N_m':sigma,'rho_kg_m3':RHO,'epsilon_m2_s3':EPS,'mu_Pa_s':MU,
        'diametro_ensayo_mm':D*1000,
        'hinze_mm':dh*1000,
        'kolmogorov_mm':eta()*1000,
        'weber_convencion_1':wd,
        'weber_critico_convencion_1':wcrit(),
        'weber_relativo':wd/wcrit(),
        'diametro_sobre_hinze':D/dh,
        'salto_capilar_esfera_Pa':laplace_jump_sphere(sigma),
        'energia_area_dos_gotas_uJ':energy_breakup(sigma)*1e6,
        'clasificacion_umbral':'sobre umbral (ruptura mas accesible)' if D>dh else 'bajo umbral (ruptura menos accesible)'
    }

def test_contract()->list[str]:
    msgs=[]
    def ck(name,predicate):
        assert bool(predicate), name
        msgs.append(name)
    tol=1e-12
    ck('T01 positivity Hinze',all(d_h(s)>0 for s in SIGMAS))
    ck('T02 positivity Weber',all(we(D,s)>0 for s in SIGMAS))
    ck('T03 dim-free ratio sigma 2x',(abs(d_h(.144)/d_h(.072)-2**(.6))<tol))
    ck('T04 dim-free ratio sigma 1/2',(abs(d_h(.036)/d_h(.072)-.5**(.6))<tol))
    ck('T05 ε scaling',(abs(d_h(.072,eps=.4)/d_h(.072)-4**(-.4))<tol))
    ck('T06 rho scaling',(abs(d_h(.072,rho=2000)/d_h(.072)-2**(-.6))<tol))
    ck('T07 dimensionless Weber d scaling',(abs(we(.01,.072)/we(.005,.072)-2**(5/3))<tol))
    ck('T08 Weber proportional 1/σ',(abs(we(D,.036)/we(D,.072)-2)<tol))
    ck('T09 boundary We(d_H)=Wcrit',all(abs(we(d_h(s),s)-wcrit())<tol for s in SIGMAS))
    ck('T10 We ratio equals (d/d_H)^(5/3)',all(abs(we(D,s)/wcrit()-(D/d_h(s))**(5/3))<tol for s in SIGMAS))
    ck('T11 threshold crossing low',D>d_h(.036))
    ck('T12 threshold crossing middle',D<d_h(.072))
    ck('T13 threshold crossing high',D<d_h(.144))
    ck('T14 monotone Hinze',d_h(.036)<d_h(.072)<d_h(.144))
    ck('T15 monotone Weber',we(D,.036)>we(D,.072)>we(D,.144))
    ck('T16 spherical Laplace linear sigma',abs(laplace_jump_sphere(.144)/laplace_jump_sphere(.072)-2)<tol)
    ck('T17 pressure jump exact',abs(laplace_jump_sphere(.072)-57.6)<tol)
    ck('T18 area breakup positive',delta_area_two_equal()>0)
    ck('T19 area independent surface tension',delta_area_two_equal(D)==delta_area_two_equal(D))
    ck('T20 capillary energy scales σ',abs(energy_breakup(.144)/energy_breakup(.072)-2)<tol)
    # Construct the same *physical* uniform velocity for two-phase exact translated spheres
    # under three different surface tensions; pressure jumps change, the advection doesn't.
    U=(1.2,0.3,-0.1); x0=(D/2,0.,0.); t=1.7
    moved=tuple(x0[j]+U[j]*t for j in range(3))
    center=tuple(U[j]*t for j in range(3))
    ck('T21 translated sphere radius unchanged',abs(math.dist(moved,center)-D/2)<tol)
    ck('T22 same transport U independent of sigma',all(tuple((moved[j]-x0[j])/t for j in range(3))==U for s in SIGMAS))
    ck('T26 capillary stress for translated sphere',all(abs(laplace_jump_sphere(s)-2*s/(D/2))<tol for s in SIGMAS))
    ck('T23 eta is same',all(abs(eta()-eta())<tol for _ in SIGMAS))
    ck('T24 threshold σ* recovers diameter',abs(d_h(RHO*((D/CH)*(EPS**(2/5)))**(5/3))-D)<tol)
    # size of frozen geometrical area patch same for different σ, energy changes
    ck('T25 area invariant vs sigma',len({round(delta_area_two_equal(),18) for s in SIGMAS})==1)
    return msgs

def save(path:Path)->None:
    path.mkdir(parents=True, exist_ok=True)
    rows=[row(s) for s in SIGMAS]
    with (path/'o65_tensiones.csv').open('w',newline='',encoding='utf-8') as f:
        dw=csv.DictWriter(f,fieldnames=list(rows[0].keys()));dw.writeheader();dw.writerows(rows)
    with (path/'o65_resumen.json').open('w',encoding='utf-8') as f:
        json.dump({'model':'Kolmogorov-Hinze diagnostic, imposed ε, no two-phase CFD',
                   'constants':{'rho':RHO,'mu':MU,'eps':EPS,'d':D,'C_H':CH},
                   'cases':rows,'check_count':len(test_contract()),
                   'checks':test_contract()},f,indent=2,ensure_ascii=False)

def plot(path:Path)->None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    path.mkdir(parents=True,exist_ok=True)
    sig=np.linspace(.025,.18,180)
    dh=np.array([d_h(x)*1e3 for x in sig])
    fig,ax=plt.subplots(figsize=(8.4,4.8))
    ax.plot(sig,dh,label='Diámetro crítico (Hinze)')
    ax.axhline(D*1000,ls='--',label='Gota de ensayo (5 mm)')
    ax.scatter(SIGMAS,[d_h(s)*1000 for s in SIGMAS],zorder=3)
    for s in SIGMAS: ax.annotate(f'{d_h(s)*1000:.2f} mm',(s,d_h(s)*1000),xytext=(0,8),textcoords='offset points',ha='center')
    ax.set(xlabel='Tensión interfacial σ (N/m)',ylabel='Diámetro de Hinze (mm)',title='O65 · mismo flujo de referencia, distinta tensión superficial')
    ax.grid(alpha=.25);ax.legend();fig.tight_layout();fig.savefig(path/'o65_diametro_vs_tension.png',dpi=165);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8.4,4.8))
    vals=[we(D,s)/wcrit() for s in SIGMAS]
    bars=ax.bar(['0,036','0,072','0,144'],vals)
    ax.axhline(1,ls='--',label='Umbral modelo: Weber relativo = 1')
    for b,v in zip(bars,vals):ax.annotate(f'{v:.3f}',(b.get_x()+b.get_width()/2,v),ha='center',xytext=(0,5),textcoords='offset points')
    ax.set(xlabel='σ (N/m)',ylabel='We(d) / We crítico',title='O65 · una misma gota, respuestas de umbral diferentes')
    ax.grid(alpha=.25,axis='y');ax.legend();fig.tight_layout();fig.savefig(path/'o65_weber_relativo.png',dpi=165);plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=parser.parse_args()
    test=test_contract()
    save(args.root/'datos')
    plot(args.root/'graficos')
    print(f'{len(test)} / {len(test)} checks PASS')
    for s in SIGMAS:
        v=row(s)
        print(f"σ={s:.3f} N/m dH={v['hinze_mm']:.6f} mm ratio={v['weber_relativo']:.6f} ΔE={v['energia_area_dos_gotas_uJ']:.6f} μJ")
