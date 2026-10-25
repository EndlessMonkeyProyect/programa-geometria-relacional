#!/usr/bin/env python3
"""O86: derivacion Fourier exacta y verificacion espectral de contraste de fases.
Requiere sympy, numpy, matplotlib para figura. No integra NS en tiempo.
"""
from pathlib import Path
from fractions import Fraction
import json, csv, math
import sympy as sp
import numpy as np

OUT = Path(__file__).resolve().parent.parent
(OUT/'resultados').mkdir(exist_ok=True)
(OUT/'graficos').mkdir(exist_ok=True)
I = sp.I
a,b,c,d,e = sp.symbols('a b c d e', real=True)
k=(1,0,0); l=(0,1,1); m=(1,1,1); h=(0,0,1)
A=sp.Matrix([0,1,0]); B=sp.Matrix([1,0,0]); C=sp.Matrix([1,1,-2]); D=sp.Matrix([1,0,0])
U={}
def add_mode(q, vector, trig):
    for sig in (1,-1):
        t = tuple(sig*j for j in q)
        U[t] = U.get(t,sp.zeros(3,1)) + (sp.Rational(1,2) if trig=='cos' else -sig*I/sp.Integer(2))*vector
add_mode(k,a*A,'cos'); add_mode(l,b*B,'cos'); add_mode(m,c*C,'sin'); add_mode(m,e*C,'cos'); add_mode(h,d*D,'cos')

def nl_at(q):
    qv=sp.Matrix(q); w=sp.zeros(3,1)
    for p,up in U.items():
        other=tuple(q[j]-p[j] for j in range(3))
        if other in U:
            w+=(sp.Matrix(other).dot(up))*U[other]
    proj=sp.eye(3)-qv*qv.T/(qv.dot(qv))
    return -I*proj*w

P=Aomega=Bomega=0
for q,uq in U.items():
    qv=sp.Matrix(q); q2=qv.dot(qv)
    cq=sp.Matrix([sp.conjugate(z) for z in uq])
    P+=q2*sp.re(cq.dot(nl_at(q)))
    Aomega+=q2*cq.dot(uq)
    Bomega+=q2*q2*cq.dot(uq)
P,Aomega,Bomega=(sp.factor(x) for x in (P,Aomega,Bomega))
assert sp.simplify(P-sp.Rational(3,4)*a*b*c)==0
assert sp.simplify(Aomega-(a*a+2*b*b+18*(c*c+e*e)+d*d)/2)==0
assert sp.simplify(Bomega-(a*a+4*b*b+54*(c*c+e*e)+d*d)/2)==0
phi_symbol=sp.symbols('phi',real=True)
phase_sub={a:1,b:1,d:sp.Rational(1,3),c:sp.cos(phi_symbol),e:sp.sin(phi_symbol)}
assert sp.trigsimp(P.subs(phase_sub)-sp.Rational(3,4)*sp.cos(phi_symbol))==0
assert sp.trigsimp(Aomega.subs(phase_sub)-sp.Rational(95,9))==0
assert sp.trigsimp(Bomega.subs(phase_sub)-sp.Rational(266,9))==0

# Campo genuinamente tridimensional: 4 vectores incluyendo 3 independientes.
from sympy import Matrix
assert Matrix.hstack(Matrix(k),Matrix(l),Matrix(h)).det()!=0
nu=sp.Rational(1,100)
base={a:1,b:1,d:sp.Rational(1,3),e:0}

def exact_case(sign):
    subs={**base,c:sign}
    pp=sp.factor(P.subs(subs)); aa=sp.factor(Aomega.subs(subs)); bb=sp.factor(Bomega.subs(subs));
    gam=sp.factor(pp/(nu*bb)); ell2=sp.factor(aa/bb); ee=sp.factor(pp-nu*bb)
    log_rate=sp.factor(2*ee/aa)
    assert sp.simplify(log_rate -2*nu/ell2*(gam-1))==0
    return {'P':str(pp),'A':str(aa),'B':str(bb),'ell2':str(ell2),
            'nu':str(nu),'gamma':str(gam),'Eprime':str(ee),
            'dlogA_dt':str(log_rate),'numeric':{'P':float(pp),'A':float(aa),'B':float(bb),
            'gamma':float(gam),'Eprime':float(ee),'ell2':float(ell2)}}
plus=exact_case(1);minus=exact_case(-1)
assert sp.factor(P.subs({a:1,b:1,c:-1,d:sp.Rational(1,3),e:0}))==-sp.Rational(3,4)
assert plus['A']==minus['A'] and plus['B']==minus['B']

# Datos espectrales y derivadas vía FFT: mismos P,A,B integrados.
def numerical(n, sign):
    xyz=np.arange(n)*2*np.pi/n
    xx,yy,zz=np.meshgrid(xyz,xyz,xyz,indexing='ij')
    # u_x=cos(y+z)+c sin(x+y+z)+d cos(z), u_y=cos(x)+c sin(x+y+z), u_z=-2c sin(x+y+z).
    u=np.stack((np.cos(yy+zz)+sign*np.sin(xx+yy+zz)+np.cos(zz)/3,
        np.cos(xx)+sign*np.sin(xx+yy+zz),
        -2*sign*np.sin(xx+yy+zz)),axis=0)
    wave=2*np.pi*np.fft.fftfreq(n,d=2*np.pi/n)
    kk=np.meshgrid(wave,wave,wave,indexing='ij')
    uh=np.fft.fftn(u,axes=(1,2,3))
    deriv=np.empty((3,3,n,n,n),dtype=float) # deriv[c,j]=d_j u_c
    for idx in range(3):
        for j in range(3):
            deriv[idx,j]=np.fft.ifftn(1j*kk[j]*uh[idx]).real
    div=sum(deriv[j,j] for j in range(3))
    vort=np.empty_like(u)
    for i,j,k_ in [(0,1,2),(1,2,0),(2,0,1)]:
        vort[i]=deriv[k_,j]-deriv[j,k_]
    s=0.5*(deriv+np.swapaxes(deriv,0,1))
    Sw=np.einsum('ijabc,jabc->iabc',s,vort)
    pp=float(np.mean(np.sum(vort*Sw,axis=0)))
    aa=float(np.mean(np.sum(vort*vort,axis=0)))
    # B by spectral derivatives of omega
    wh=np.fft.fftn(vort,axes=(1,2,3))
    Bnum=0.0
    for j in range(3):
        dw=np.fft.ifftn(1j*kk[j][None,:,:,:]*wh,axes=(1,2,3)).real
        Bnum+=float(np.mean(np.sum(dw*dw,axis=0)))
    return {'grid':n,'phase_sign':sign,'P_num':pp,'A_num':aa,'B_num':Bnum,'max_div':float(np.max(np.abs(div)))}
rows=[numerical(n,sign) for n in (16,24,40) for sign in (1,-1)]
for row in rows:
    target=plus if row['phase_sign']==1 else minus
    for name,expected in [('P_num','P'),('A_num','A'),('B_num','B')]:
        assert abs(row[name]-float(target['numeric'][expected]))<1e-11,(row,name)
    assert row['max_div']<1e-11

# Test exacto de reescalado amplitud c0: P~c0^3, A,B~c0^2, gamma~c0.
scale_checks=[]
for lamb in [sp.Rational(1,2),1,2,8]:
    sub={a:lamb,b:lamb,c:lamb,d:lamb/3,e:0}
    gamma=sp.factor(P.subs(sub)/(nu*Bomega.subs(sub)))
    assert sp.simplify(gamma-lamb*sp.Rational(675,266))==0
    scale_checks.append({'amplitude':str(lamb),'gamma':str(gamma)})

# Verificación exacta de campo ABC Beltrami.
x,y,z=sp.symbols('x y z',real=True)
abc=sp.Matrix([sp.sin(z)+sp.cos(y),sp.sin(x)+sp.cos(z),sp.sin(y)+sp.cos(x)])
curl=sp.Matrix([sp.diff(abc[2],y)-sp.diff(abc[1],z),sp.diff(abc[0],z)-sp.diff(abc[2],x),sp.diff(abc[1],x)-sp.diff(abc[0],y)])
lap=sp.Matrix([sum(sp.diff(ui,t,2) for t in (x,y,z)) for ui in abc])
assert all(sp.trigsimp(curl[i]-abc[i])==0 for i in range(3))
assert all(sp.trigsimp(lap[i]+abc[i])==0 for i in range(3))
assert sp.simplify(sp.diff(abc[0],x)+sp.diff(abc[1],y)+sp.diff(abc[2],z))==0

# Plot no se fijan colores, lineas separadas para casos.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
phi=np.linspace(-np.pi,np.pi,501)
cs=np.cos(phi)
pp=0.75*cs
bb=(1+4+54+1/9)/2 # Mantener magnitudes fijas: c=cos(phi), e=sin(phi).
G=pp/(float(nu)*bb)
fig,ax=plt.subplots(figsize=(9,4.6))
ax.plot(phi/np.pi,G,label=r'$\Gamma=P/(\nu B)$')
ax.axhline(1,linestyle='--',label=r'umbral instantáneo $\Gamma=1$')
ax.axhline(0,linestyle=':',alpha=.7)
ax.set_xlabel('Desfase relativo / π')
ax.set_ylabel('Razón de estiramiento a disipación')
ax.set_title('O86 — La fase cambia el signo del balance instantáneo')
ax.legend();ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(OUT/'graficos'/'o86_fase_y_compensacion.png',dpi=180);plt.close(fig)

report={'sympy':{'P':str(P),'A':str(Aomega),'B':str(Bomega)},'caso_mas':plus,
'caso_menos':minus,'malla_fourier':rows,'escalado_amplitud':scale_checks,
'desfase_continuo':{'P(phi)':'3*cos(phi)/4','A(phi)':'95/9','B(phi)':'266/9'},
'beltrami':{'curl_u_equals_u':True,'laplacian_u_equals_minus_u':True,'pressure_absorbs_nonlinearity':True},
'alcance':'Identidad instantanea exacta. No constituye prueba de regularidad global NS 3D.'}
(OUT/'resultados'/'verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/'resultados'/'verificacion_fourier.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('O86 VERIFICADO: P=',P,'A=',Aomega,'B=',Bomega)
print('Gamma +',plus['gamma'],'Gamma -',minus['gamma'])
print('Eprime +',plus['Eprime'],'Eprime -',minus['Eprime'])
print('Fourier grids pass',len(rows),'Beltrami pass; escala amplitud pass',len(scale_checks))
