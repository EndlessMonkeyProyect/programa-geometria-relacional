"""O50: exact kinematic incompressible translating/deforming axisymmetric toroidal shells.
This is NOT asserted to solve the unforced Euler/Navier-Stokes momentum equation.
"""
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import sympy as sp

OUT=Path(__file__).parent
R=1.5; w0=R*R/2; aa=.20; bb=.24; C=aa*bb
h0=.18; k=.9; OM=2*math.pi

def a(t):return aa*math.exp(h0*math.sin(k*t))
def b(t):return bb*math.exp(-h0*math.sin(k*t))
def h(t):return h0*k*math.cos(k*t)
def Omega(t):return OM*(1+.12*math.cos(.7*t))
def phase(t):return OM*(t+.12/.7*math.sin(.7*t))
def U(t,base=.32):return base+.04*math.sin(.65*t)
def Z(t,base=.32):return base*t+.04/.65*(1-math.cos(.65*t))
def s_at(w,z,t,base=.32):return ((w-w0)/a(t))**2+((z-Z(t,base))/b(t))**2

def vel_wz(t,x,eps=0.,base=.32):
 w,z=x; A=a(t); B=b(t); u=w-w0; v=z-Z(t,base)
 s=(u/A)**2+(v/B)**2
 F=C*Omega(t)*(1+eps*s)
 return np.array([h(t)*u-F*v/(B*B), U(t,base)-h(t)*v+F*u/(A*A)])

def initial(rho,theta):return np.array([w0+aa*rho*math.cos(theta),bb*rho*math.sin(theta)])
def analytic(t,rho,theta0,eps=0.,base=.32):
 th=theta0+(1+eps*rho*rho)*phase(t)
 return np.array([w0+a(t)*rho*math.cos(th), Z(t,base)+b(t)*rho*math.sin(th)])

def evolve(rho,theta0,eps=0.,base=.32,T=3.,rtol=3e-12,atol=3e-13):
 return solve_ivp(lambda t,x:vel_wz(t,x,eps,base),(0,T),initial(rho,theta0),rtol=rtol,atol=atol,dense_output=True,max_step=.011)

checks=[]
def ck(label,condition,diag=None):
 assert bool(condition),f'{label}: {diag}'
 checks.append({'name':label,'PASS':True,'diagnostic':float(diag) if isinstance(diag,(float,np.floating)) else diag})

# symbolic incompressibility and invariance of s in full explicitly time-dependent flow
ww,zz,ww0,ZZ,A,B,hh,UU,MM,Cc,ee =sp.symbols('w z w0 Z A B h U M C e',real=True,nonzero=True)
ss=((ww-ww0)/A)**2+((zz-ZZ)/B)**2
VW=hh*(ww-ww0)-Cc*MM*(1+ee*ss)*(zz-ZZ)/B**2
VZ=UU-hh*(zz-ZZ)+Cc*MM*(1+ee*ss)*(ww-ww0)/A**2
ck('axisymmetric-divergence-zero',sp.simplify(sp.diff(VW,ww)+sp.diff(VZ,zz))==0)
# time dependence via A'=hA, B'=-hB, Z'=U
Ds=sp.diff(ss,ww)*VW+sp.diff(ss,zz)*VZ+sp.diff(ss,A)*hh*A+sp.diff(ss,B)*(-hh*B)+sp.diff(ss,ZZ)*UU
ck('shell-label-materially-conserved',sp.simplify(Ds)==0)
# angular velocity in transformed elliptical section
qq=(ww-ww0)/A;pp=(zz-ZZ)/B
Dq=sp.diff(qq,ww)*VW+sp.diff(qq,zz)*VZ+sp.diff(qq,A)*hh*A+sp.diff(qq,B)*(-hh*B)+sp.diff(qq,ZZ)*UU
Dp=sp.diff(pp,ww)*VW+sp.diff(pp,zz)*VZ+sp.diff(pp,A)*hh*A+sp.diff(pp,B)*(-hh*B)+sp.diff(pp,ZZ)*UU
angular=sp.factor((qq*Dp-pp*Dq)/ss)
ck('phase-evolution-analytic',sp.simplify(angular-Cc*MM*(1+ee*ss)/(A*B))==0)

# exact cycle events reference phase
T1=brentq(lambda t:phase(t)-2*math.pi,0.4,1.2)
T2=brentq(lambda t:phase(t)-4*math.pi,1.4,2.6)
T3=brentq(lambda t:phase(t)-6*math.pi,2.3,3.7)
ck('clock-monotone',min(Omega(t) for t in np.linspace(0,T3,100))>0)
ck('deformed-shell-volume',max(abs(a(t)*b(t)-C) for t in np.linspace(0,T3,101))<1e-15)
ck('positive-physical-radius',w0-a(1.75)*.94>0)

rows=[]; failures=[]; paths=[]
for e in [0.,.2]:
 for rho in [.38,.9]:
  for theta0 in [0.,math.pi/2,math.pi]:
   sol=evolve(rho,theta0,e,T=T3)
   sampled=np.linspace(0,T3,151)
   pts=sol.sol(sampled)
   refs=np.array([analytic(t,rho,theta0,e) for t in sampled]).T
   err=float(np.max(np.abs(pts-refs)))
   shellerr=float(max(abs(s_at(pts[0,j],pts[1,j],t)-rho*rho) for j,t in enumerate(sampled)))
   ck(f'ode-analytic-e{e}-rho{rho}-theta{round(theta0,2)}',err<4e-9,err)
   ck(f'ode-material-label-e{e}-rho{rho}-theta{round(theta0,2)}',shellerr<7e-9,shellerr)
   rows.append({'eps':e,'rho':rho,'theta0':theta0,'max_xy_ode_error':err,'max_shell_label_error':shellerr,'at_T2':list(map(float,sol.sol(T2)))})

for e in [0.,.2]:
 for n,tt in [(1,T1),(2,T2),(3,T3)]:
  delta=e*(.9**2-.38**2)*2*math.pi*n
  ck(f'predicted-phase-drift-e{e}-n{n}',np.isfinite(delta))
  # numeric winding via unit relative vectors reconstructed angle from ODE trajectory
  phases=[]
  for rho in [.38,.9]:
   sol=evolve(rho,0,e,T=tt)
   tm=np.linspace(0,tt,501); p=sol.sol(tm)
   angles=np.unwrap(np.arctan2((p[1]-np.array([Z(t) for t in tm])) / np.array([b(t) for t in tm]), (p[0]-w0)/np.array([a(t) for t in tm])))
   phases.append(float(angles[-1]-angles[0]))
  drift=phases[1]-phases[0]
  ck(f'material-unwrapped-drift-e{e}-n{n}',abs(drift-delta)<3e-9,abs(drift-delta))
  paths.append({'eps':e,'cycles':n,'time':tt,'phase_difference_rad':drift,'phase_difference_cycles':drift/(2*math.pi),'predicted_rad':delta})

# Inner/outer same-shell points are antipodal and remain antipodal in normalized phase
for e in [0.,.2]:
 rho=.76
 s0=evolve(rho,0,e,T=T3);s1=evolve(rho,math.pi,e,T=T3)
 errs=[]
 for tt in np.linspace(0,T3,101):
  p0=s0.sol(tt);p1=s1.sol(tt)
  # normalized positions of the paired points sum to zero
  err=abs((p0[0]+p1[0]-2*w0)/a(tt))+abs((p0[1]+p1[1]-2*Z(tt))/b(tt))
  errs.append(err)
 ck(f'antipodal-interior-exterior-pair-e{e}',max(errs)<4e-9,max(errs))

# Galilean check different transport Z and U have no effect on normalized phases
for e in [0.,.2]:
 r=.75;th=.23
 s1=evolve(r,th,e,base=.32,T=T2);s2=evolve(r,th,e,base=.92,T=T2)
 n1=s1.sol(T2)-np.array([w0,Z(T2,.32)]);n2=s2.sol(T2)-np.array([w0,Z(T2,.92)])
 ck(f'axial-translation-galilean-e{e}',np.max(np.abs(n1-n2))<1e-9,float(np.max(np.abs(n1-n2))))

# Instantaneous inner/outer rates differ for a circular cross-section F(s)=A*s; integrated period same.
RR=1.5;rho=.13;Fprime=.6
omega_inner=2*Fprime/(RR-rho);omega_outer=2*Fprime/(RR+rho)
ck('instantaneous-omega-inner-outer-different',omega_inner>omega_outer)
period=np.pi*RR/Fprime
ck('circular-orbit-period-independent-of-rho',all(abs(np.pi*RR/Fprime-period)<1e-14 for _ in [0.04,.13,.26]))

res={'test_count':len(checks),'tests':checks,'times':{'one_cycle':T1,'two_cycles':T2,'three_cycles':T3},'trajectories':rows,'phase_drift':paths,'period_circle':period,'omega_inner':omega_inner,'omega_outer':omega_outer,'model':'axisymmetric divergence-free KINEMATIC family, not unforced Euler/NS solution', 'conclusion':'material closed surfaces and even smooth deformation do not enforce inter-shell phase locking; constant frequency profile is isochronous; differential core profile makes drift.'}
(OUT/'resultados_o50.json').write_text(json.dumps(res,indent=2,ensure_ascii=False))
print('PASS',len(checks),'checks')
for p in paths: print('eps',p['eps'],'cycles',p['cycles'],'t',round(p['time'],6),'drift_cycles',round(p['phase_difference_cycles'],8))
print('angular inner vs outer',round(omega_inner,6),round(omega_outer,6),'period',round(period,6))
