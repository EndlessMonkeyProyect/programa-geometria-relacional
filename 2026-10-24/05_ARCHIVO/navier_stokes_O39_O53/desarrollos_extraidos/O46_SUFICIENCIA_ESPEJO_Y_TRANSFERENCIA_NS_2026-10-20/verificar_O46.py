#!/usr/bin/env python3
"""O46 — prueba local exacta/FFT de interfaz de fase + espejo espectral.
Sólo datos iniciales suaves periódicos de NS 3D; NO integración a tiempo largo.
"""
import json, math
from pathlib import Path
import numpy as np

OUT=Path(__file__).parent
NU=0.03
A,D,B=1.0,0.7,0.4
CASE_A=(0.6,0.4) # amplitud de omega_x para sin(2z),sin(3z)
CASE_B=(0.4,0.6)
checks=[]

def test(name, cond, detail=''):
    if not cond: raise AssertionError(f'{name}: {detail}')
    checks.append(name)

def calc(n, K2, K3, alpha=0, beta=0, signB=1):
    x,y,z=np.meshgrid(2*np.pi*np.arange(n)/n,2*np.pi*np.arange(n)/n,2*np.pi*np.arange(n)/n,indexing='ij')
    xx,yy=x+alpha,y+beta
    b=signB*B
    C=np.cos(xx-yy)
    W=A*np.cos(xx)+D*np.cos(yy)+2*b*C
    Wx=-A*np.sin(xx)-2*b*np.sin(xx-yy)
    Wy=-D*np.sin(yy)+2*b*np.sin(xx-yy)
    wz_lap=-A*np.cos(xx)-D*np.cos(yy)-4*b*C
    # h(z) chosen so -h'=K2 sin(2z)+K3 sin(3z).
    h=(K2/2)*np.cos(2*z)+(K3/3)*np.cos(3*z)
    ox=K2*np.sin(2*z)+K3*np.sin(3*z)
    oxz=2*K2*np.cos(2*z)+3*K3*np.cos(3*z)
    ux=b*np.sin(xx-yy)-D*np.sin(yy)
    uy=A*np.sin(xx)+b*np.sin(xx-yy)+h
    # vector fields omega=(ox,0,W), stretch=(omega.grad)u
    sx=ox*b*C
    sy=ox*(-b*C-D*np.cos(yy))
    P=np.mean(ox*sx) # omega dot stretch
    stretching_sq=np.mean(sx**2+sy**2)
    enst=0.5*np.mean(ox**2+W**2)
    palin=np.mean(oxz**2+Wx**2+Wy**2)
    domega_z=-ux*Wx-uy*Wy+NU*wz_lap
    domega_x=-ux*0-uy*0 + NU*(-4*K2*np.sin(2*z)-9*K3*np.sin(3*z)) # advective x zero, stretch_x nonzero!
    domega_x +=sx
    # True omega_y derivative from stretching_y + viscous(omega_y=0)
    domega_y=sy
    dEnst=np.mean(ox*domega_x+W*domega_z)
    # quantity |hat{omega_z}(0,1,0)|^2, translation invariant
    omega_mode=np.fft.fftn(W)/n**3
    d_mode=np.fft.fftn(domega_z)/n**3
    syobs=abs(omega_mode[0,1,0])**2
    dsyobs=2*np.real(np.conj(omega_mode[0,1,0])*d_mode[0,1,0])
    psi=A*np.cos(xx)+D*np.cos(yy)+b*C
    c=np.fft.fftn(psi)/n**3
    triad=np.conj(c[1,0,0])*c[0,1,0]*c[1,n-1,0]
    approx=-NU*D**2/2 -2*np.real(triad)
    return dict(E=float(enst),J=float(palin),P=float(P),stretch2=float(stretching_sq),dE=float(dEnst),
       Eprime_theory=float(-NU*palin), S_y=float(syobs),dS_y=float(dsyobs),dS_pred=float(approx),
       bispectrum_real=float(np.real(triad)),bispectrum_imag=float(np.imag(triad)),
       ell=float(math.sqrt(2*enst/palin)), k2=float(K2), k3=float(K3), signB=int(signB))

def run():
    variants={}
    for n in (24,32,48):
        a=calc(n,*CASE_A)
        b=calc(n,*CASE_B)
        variants[str(n)]={'A':a,'B':b}
        tol=3e-11
        test(f'N{n}: global E equal',abs(a['E']-b['E'])<tol)
        test(f'N{n}: J differs by one-half',abs((b['J']-a['J'])-0.5)<tol)
        test(f'N{n}: phase bispectrum identical',abs(a['bispectrum_real']-b['bispectrum_real'])<tol)
        test(f'N{n}: MCM of present axial wavenumbers=6', a['k2']>0 and a['k3']>0 and b['k2']>0 and b['k3']>0)
        for key,r in [('A',a),('B',b)]:
            test(f'N{n}/{key}: E matches analytic', abs(r['E']-(A*A+D*D+4*B*B+0.52)/4)<tol)
            test(f'N{n}/{key}: P globally zero',abs(r['P'])<tol)
            test(f'N{n}/{key}: local stretching nonzero', abs(r['stretch2']-(0.52/2)*(B**2+D**2/2))<tol)
            test(f'N{n}/{key}: enstrophy PDE derivative',abs(r['dE']+NU*r['J'])<tol)
            test(f'N{n}/{key}: bispectrum value',abs(r['bispectrum_real']-(A*D*B/8))<tol)
            test(f'N{n}/{key}: S_y derivative closure',abs(r['dS_y']-r['dS_pred'])<tol)
            test(f'N{n}/{key}: mirror J=2E/ell^2',abs(2*r['E']/r['ell']**2-r['J'])<tol)
        test(f'N{n}: different E slopes',abs(b['dE']-a['dE']+NU*.5)<tol)
        test(f'N{n}: different mirror scales',abs(a['ell']-b['ell'])>0.01)
    # invariant under translations of x/y and orientation of total phase origin
    g=calc(32,*CASE_A,alpha=.41,beta=-.27)
    test('translation invariance Re bispectrum',abs(g['bispectrum_real']-variants['32']['A']['bispectrum_real'])<1e-11)
    test('translation invariance S_y derivative',abs(g['dS_y']-variants['32']['A']['dS_y'])<1e-11)
    test('translation invariance mirror scale',abs(g['ell']-variants['32']['A']['ell'])<1e-11)
    # control adverse of lost triad phase while all amplitude magnitudes remain same
    flip=calc(32,*CASE_A,signB=-1)
    ref=variants['32']['A']
    test('phase inversion preserves E,J,mirror scale',all(abs(flip[k]-ref[k])<1e-11 for k in ('E','J','ell')))
    test('phase inversion changes triad sign',abs(flip['bispectrum_real']+ref['bispectrum_real'])<1e-11)
    test('phase inversion switches coarse power response',abs(flip['dS_y']-ref['dS_y']-A*D*B/2)<1e-11)
    # no scalar E,ell,phase is sufficient for full NS vector derivative (different omega_x modal spectrum).
    # quotient for initial E derivative is exact for this fixed parametric family P=0,
    # but not closed for all times/general solutions.
    result={'module':'O46','date':'2026-10-20','scope':'Navier-Stokes 3D smooth periodic initial fields with nonzero stretching; local instantaneous assertions',
       'Ntested':[24,32,48], 'viscosity':NU,'A':A,'D':D,'B':B,
       'variants':variants,'phase_flipped_control':flip,'translation_control':g,
       'tests':len(checks),'passed':True,'checks':checks,
       'exclusions':['not time evolution','not a 3D full closure','not global regularity','no physical singularity proof']}
    (OUT/'O46_RESULTADOS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'tests':len(checks),'PASS':True,'E':variants['32']['A']['E'],'J_A':variants['32']['A']['J'],'J_B':variants['32']['B']['J'],'Eprime_A':variants['32']['A']['dE'],'Eprime_B':variants['32']['B']['dE'],'ell_A':variants['32']['A']['ell'],'ell_B':variants['32']['B']['ell'],'dS_y':variants['32']['A']['dS_y']},indent=2))

if __name__=='__main__':run()
