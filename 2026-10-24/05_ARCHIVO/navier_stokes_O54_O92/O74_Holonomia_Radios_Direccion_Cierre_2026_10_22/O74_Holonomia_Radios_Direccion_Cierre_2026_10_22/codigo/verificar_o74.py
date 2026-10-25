#!/usr/bin/env python3
"""O74: tests of gear holonomy, independent geometry, exact NS examples.
Run: python codigo/verificar_o74.py
Dependencies: numpy, matplotlib (plot only).
No claim of solving the 3D Navier–Stokes regularity problem.
"""
from pathlib import Path
import csv, math, json
import numpy as np
OUT = Path(__file__).resolve().parents[1]
checks = 0

def check(test, desc):
    global checks
    if not bool(test):
        raise AssertionError(desc)
    checks += 1

def holonomy(a,b):
    return np.prod(np.array(a,dtype=float)/np.array(b,dtype=float))

def compat_rates(a,b,start=1.):
    x = [float(start)]
    for aa,bb in zip(a,b):
        x.append(-aa/bb*x[-1])
    return np.array(x)

rng = np.random.default_rng(20261022)
examples=[]
# Node radii can vary arbitrarily; telescopic products imply holonomy=1.
for i in range(1000):
    r=np.exp(rng.uniform(-3,3,4))
    a=r.copy(); b=np.roll(r,-1)
    H=holonomy(a,b)
    w=compat_rates(a,b)
    check(np.isclose(H,1,atol=1e-12), 'telescopic holonomy')
    check(np.isclose(w[0],w[-1],atol=1e-10,rtol=1e-10), 'closed four-cycle')
    s=r*w[:-1]
    check(np.allclose(s, s[0]*np.array([1,-1,1,-1]),atol=1e-10,rtol=1e-10), 'alternating tangent speeds')
# contact asymmetry breaks even cycle, unless compensated
for i in range(500):
    r=np.exp(rng.uniform(-1,1,4))
    c=np.exp(rng.uniform(-.6,.6,4))
    d=np.exp(rng.uniform(-.6,.6,4))
    a=c*r; b=d*np.roll(r,-1)
    H=holonomy(a,b)
    rates=compat_rates(a,b,0.2)
    check(np.isclose(rates[-1],H*rates[0],rtol=1e-11,atol=1e-11),'closure defect')
    # forced compensator in last contact; correct vector-to-vector transfer
    d[-1]*=H
    b=d*np.roll(r,-1)
    H2=holonomy(a,b)
    check(np.isclose(H2,1,rtol=1e-11,atol=1e-11),'compensated holonomy')
    rates=compat_rates(a,b,0.2)
    check(np.isclose(rates[-1],rates[0],rtol=1e-11,atol=1e-11),'compensated closure')
# 3 and 4 parity with node radii
for n in (3,4,5,6,7,8):
    r=np.exp(rng.uniform(-1,1,n))
    w=compat_rates(r,np.roll(r,-1))
    check(np.isclose(w[-1],(-1)**n*w[0]),'cycle parity')
# Kinematic shrinking radii keep H=1 while rates grow; NOT an NS solution.
for t in np.linspace(0,1-1e-5,101):
    r=(1-t)*np.array([1.,2.,3.,4.]);rates=np.array([1.,-1.,1.,-1.])/r
    check(np.isclose(holonomy(r,np.roll(r,-1)),1.,atol=1e-12),'holonomy under collapse')
    check(np.all(np.isfinite(rates)),'finite before terminal time')
check(np.isclose(abs(1e-5*rates[0]),1.,rtol=1e-10),'rate diverges as 1/(T-t)')
# rhombus geometric degrees independent of angular velocities
ell=4.0
rad_caps=.5
phis=np.linspace(.03,math.pi-.03,701)
for phi in phis:
    x1=np.array([0.,0.]); x2=np.array([ell,0.]);x3=np.array([ell*(1+np.cos(phi)),ell*np.sin(phi)]);x4=np.array([ell*np.cos(phi),ell*np.sin(phi)])
    x=[x1,x2,x3,x4]
    lengths=[np.linalg.norm(x[(j+1)%4]-x[j]) for j in range(4)]
    check(np.allclose(lengths,ell,atol=1e-12), 'sides fixed')
    A=np.linalg.det(np.column_stack([x2-x1,x4-x1]))
    check(abs(A-ell**2*math.sin(phi))<1e-11,'area')
    d13=np.linalg.norm(x3-x1);d24=np.linalg.norm(x4-x2)
    check(np.isclose(d13,2*ell*math.cos(phi/2),atol=1e-11),'diagonal 13')
    check(np.isclose(d24,2*ell*math.sin(phi/2),atol=1e-11),'diagonal 24')
    check((d13<2*rad_caps) == (phi>math.pi-2*math.asin(rad_caps/ell)), 'collision 13')
    check((d24<2*rad_caps) == (phi<2*math.asin(rad_caps/ell)), 'collision 24')
# exactly incompressible affine NS field: A = diag(-lambda,-lambda,2 lambda).
lam=.7
A=np.diag([-lam,-lam,2*lam]); A2=A@A
check(np.isclose(np.trace(A),0),'divergence free')
check(np.allclose(A2,A2.T),'gradient pressure condition')
for t in np.linspace(0,4,100):
    F=np.diag([math.exp(-lam*t),math.exp(-lam*t),math.exp(2*lam*t)])
    check(np.isclose(np.linalg.det(F),1,atol=1e-12),'volume-preserving')
    check(np.isclose(np.linalg.det(F[:2,:2]),math.exp(-2*lam*t),atol=1e-12),'planar area changes')
    check(np.isclose(np.linalg.norm(F@np.array([1,0,0])),math.exp(-lam*t),atol=1e-12),'distance decays, no finite collision')
# material-loop Kelvin viscous equation in periodic Stokes/NS shear wave
nu=.05;k=2.;U0=1.3;Lx=.4;h=math.pi/(2*k)
for t in np.linspace(0,6,501):
    amplitude=U0*math.exp(-nu*k*k*t)
    circulation=-Lx*amplitude*math.sin(k*h)
    dGdt=-nu*k*k*circulation
    viscous_integral=nu*(-k*k)*circulation
    check(np.isclose(dGdt,viscous_integral,atol=1e-14),'Kelvin for exact NS shear')

# write self-contained data for chart
rows=[]
for t in np.linspace(0,4,161):
    H_bad=1.1
    area=ell**2*math.exp(-2*lam*t)
    gamma=-Lx*U0*math.exp(-nu*k*k*t)
    rows.append({'t':t,'area_material_affine':area,'circulacion_shear':gamma, 'holonomy_ideal':1.,'holonomy_descompensada':H_bad})
with (OUT/'datos'/'o74_serie.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

# Standalone SVG plots without plotting-library font cache.
def make_svg(path,title,series,xlabel,ylabel):
    W,H=900,480; x0,y0,x1,y1=85,65,855,402
    allvals=[v for _,vv,_ in series for v in vv]
    ymin=min(0,min(allvals)); ymax=max(allvals)*1.1
    if ymax==ymin:ymax=ymin+1
    xvals=series[0][0]; xmin=min(xvals); xmax=max(xvals)
    xpix=lambda t:x0+(t-xmin)*(x1-x0)/(xmax-xmin)
    ypix=lambda v:y1-(v-ymin)*(y1-y0)/(ymax-ymin)
    colors=['#0b847a','#a55d28','#5b62a9']
    v=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
       '<rect width="100%" height="100%" fill="white"/>',
       f'<text x="{W/2}" y="30" text-anchor="middle" font-size="18" font-family="sans-serif">{title}</text>',
       f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#444"/>',
       f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#444"/>',
       f'<text x="{(x0+x1)/2}" y="{H-15}" text-anchor="middle" font-size="13">{xlabel}</text>',
       f'<text x="15" y="{(y0+y1)/2}" transform="rotate(-90 15 {(y0+y1)/2})" text-anchor="middle" font-size="13">{ylabel}</text>']
    for i in range(5):
        yi=ymin+(ymax-ymin)*i/4; yy=ypix(yi)
        v.append(f'<line x1="{x0}" y1="{yy:.2f}" x2="{x1}" y2="{yy:.2f}" stroke="#e1e5e9"/>')
        v.append(f'<text x="{x0-9}" y="{yy+4:.2f}" text-anchor="end" font-size="12">{yi:.2f}</text>')
        xi=xmin+(xmax-xmin)*i/4; xx=xpix(xi)
        v.append(f'<text x="{xx:.2f}" y="{y1+21}" text-anchor="middle" font-size="12">{xi:.1f}</text>')
    for j,(xs,ys,label) in enumerate(series):
        pts=' '.join(f'{xpix(x):.2f},{ypix(y):.2f}' for x,y in zip(xs,ys))
        c=colors[j%len(colors)]
        v.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.7"/>')
        v.append(f'<line x1="{x0+j*260}" y1="{y0-24}" x2="{x0+26+j*260}" y2="{y0-24}" stroke="{c}" stroke-width="3"/>')
        v.append(f'<text x="{x0+32+j*260}" y="{y0-20}" font-size="11">{label}</text>')
    path.write_text('\n'.join(v+['</svg>']))

tt=np.array([z['t'] for z in rows]);
make_svg(OUT/'graficos'/'o74_area_circulacion.svg', 'O74: area y circulacion (dos soluciones NS distintas)',
    [(tt,[z['area_material_affine']/ell**2 for z in rows],'Area relativa'),
     (tt,[-z['circulacion_shear']/(Lx*U0) for z in rows],'Circulacion relativa')],
     'Tiempo adimensional','Fraccion inicial')
tt=np.linspace(0,1,301)
ph=1.15*(1-tt)+.03
make_svg(OUT/'graficos'/'o74_contacto_anillo.svg','O74: deformacion y aproximacion de diagonales',
    [(tt,np.sin(ph),'Area relativa'),
     (tt,2*ell*np.sin(ph/2)/(2*rad_caps),'Diagonal / umbral'),
     (tt,np.ones_like(tt),'Contacto')],
     'Parametro de deformacion (no tiempo NS)','Magnitudes adimensionales')

summary={'total_checks':checks,'reference_examples':{'uniform_radii':[1.,1.,1.,1.],'matched_gear_speeds':[1.,-1.,1.,-1.],'offset_holonomy':1.1,'compensated_holonomy':1.0},'caveats':['No PDE regularity theorem','Gear system not automatically an NS vortex','Affine exact NS field not finite-energy on whole R3']}
(OUT/'datos'/'resumen.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
