#!/usr/bin/env python3
"""O80 — Validación independiente de identidades espectrales exactas de tiempo inicial.
Requiere numpy. NO es una simulación temporal de Navier-Stokes ni una demostración numérica de regularidad.
"""
import json, csv, math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'resultados'
checks=0

def ok(thing, description):
    global checks
    checks += 1
    if not bool(thing): raise AssertionError(description)

def v3(a): return np.array(a,dtype=float)
def ktuple(k): return tuple(int(x) for x in k)
def norm(x): return float(np.linalg.norm(x))

def compose(waves):
    """Each wave: (integer k, polarization vector, signed cosine coefficient, phase in rad)."""
    modes={}
    for k,polar,ampl,phase in waves:
        k=np.asarray(k,dtype=int); a=np.asarray(polar,dtype=float)
        ok(norm(k)>0,'k nonzero')
        ok(abs(np.dot(k,a))<1e-12,'solenoidality wave')
        coef=.5*ampl*np.exp(1j*phase)*a
        kp=ktuple(k); km=ktuple(-k)
        modes[kp]=modes.get(kp,np.zeros(3,complex))+coef
        modes[km]=modes.get(km,np.zeros(3,complex))+np.conj(coef)
    modes={k:v for k,v in modes.items() if norm(v)>1e-13}
    return modes

def measures(modes):
    R=sum(norm(v)/norm(k) for k,v in modes.items())
    A0=sum(norm(v) for v in modes.values())
    A1=sum(norm(k)*norm(v) for k,v in modes.items())
    Ymean=sum(norm(k)**2*np.vdot(v,v).real for k,v in modes.items())
    return dict(R=R, A0=A0,A1=A1,Ymean=Ymean)

def nonlinear(modes):
    """F_k = Fourier(-P div(u tensor u)), with P the Leray projector."""
    pre={}
    for p,up in modes.items():
        for q,uq in modes.items():
            k=tuple(a+b for a,b in zip(p,q))
            if k==(0,0,0): continue
            kv=v3(k)
            # divergence form k dot up = q dot up since p dot up=0
            pre[k]=pre.get(k,np.zeros(3,complex)) - 1j*np.dot(kv,up)*uq
    return {k: (np.eye(3)-np.outer(v3(k),v3(k))/norm(k)**2)@v for k,v in pre.items()}

def dplus_R(modes, nu, nonlin):
    """Right derivative of Wiener norm at 0, including creation of previously absent modes."""
    total=0.
    for k in set(modes)|set(nonlin):
        u=modes.get(k,np.zeros(3,complex)); F=nonlin.get(k,np.zeros(3,complex))
        D=-nu*norm(k)**2*u+F
        if norm(u)>1e-13:
            total += (np.vdot(u,D).real/norm(u))/norm(k)
        else: total+=norm(D)/norm(k)
    return total

base=[((1,0,0),(0,1,0),.04,0.),
      ((0,1,1),(1,0,0),.04,0.),
      ((1,1,1),(1,1,-2),.01,-np.pi/2),
      ((0,0,1),(1,0,0),.01,0.)]
nu=.10
reports=[]
for csign in [1.,-1.]:
    waves=base.copy()
    waves[2]=(waves[2][0],waves[2][1],.01*csign,waves[2][3])
    modes=compose(waves)
    S=measures(modes); F=nonlinear(modes)
    D=dplus_R(modes,nu,F)
    nl_energy=sum(np.vdot(modes[k],F.get(k,np.zeros(3,complex))).real for k in modes)
    ok(abs(nl_energy)<1e-12,'nonlinear energy cancellation')
    ok(S['A0']**2<= S['R']*S['A1']+1e-12,'critical interpolation')
    ok(D+nu*S['A1']<=S['A0']**2+1e-12,'fourier differential upper bound')
    ok(S['R']<nu,'genuine small data')
    reports.append(dict(csign=csign,nu=nu,**S,Dini_R=D, residual_budget=D+(nu-S['R'])*S['A1'],nl_energy=nl_energy,generated=sum(1 for k in F if k not in modes and norm(F[k])>1e-13)))

# 96 random-phase/amplitude finite Fourier datasets, with frequency changes and cross-triads.
rng=np.random.default_rng(20261022)
for case in range(96):
    f= rng.uniform(.001,.02,size=4)*rng.choice([-1.,1.],size=4)
    phases=rng.uniform(-np.pi,np.pi,size=4)
    waves=[(w[0],w[1],float(f[i]),float(phases[i])) for i,w in enumerate(base)]
    modes=compose(waves); S=measures(modes); F=nonlinear(modes)
    D=dplus_R(modes,nu,F)
    nl_energy=sum(np.vdot(modes[k],F.get(k,np.zeros(3,complex))).real for k in modes)
    ok(abs(nl_energy)<1e-10, f'energy cancellation case {case}')
    ok(S['A0']**2<=S['R']*S['A1']+1e-10,'interpolation')
    ok(D+(nu-S['R'])*S['A1']<=1e-10,'critical differential estimate')
    for k,v in modes.items():
        kn=tuple(-z for z in k)
        ok(norm(np.conj(v)-modes[kn])<1e-12,'real field symmetry')
        ok(abs(np.dot(v3(k),v))<1e-12,'divergence free')

# Exact finite dyadic shear data. Difference of no interactions is intended control.
rows=[]
for alpha in [0.5,1.,1.5,3.5]:
  for J in [2,4,6,8,10,12,14,16]:
    a0=.02
    amplitudes=np.array([a0*2.**(-alpha*j) for j in range(J)])
    n=np.array([2.**j for j in range(J)])
    R=float(np.sum(amplitudes/n))
    Y=float(.5*np.sum(n**2*amplitudes**2))
    analyticalR=a0*(1.-2.**(-(alpha+1)*J))/(1.-2.**(-(alpha+1)))
    ok(abs(R-analyticalR)<1e-12,'geometric sum exact')
    ok(R<nu,'finite dyadic smallness example')
    rows.append(dict(alpha=alpha,branches=J,R=R,Ymean=Y))
with (OUT/'dyadic_dilucion.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader();writer.writerows(rows)

# Scale conjugate triad predicted by O79: weighted low-frequency amplitudes.
triads=[]
for j in range(8):
    n=2**j
    ampl=.02*n**(-1.5)
    Rtrib=ampl*(1+1/math.sqrt(2)+math.sqrt(2)) / n
    Transfer=.5*n*ampl**3
    triads.append(dict(j=j,n=n,R_triade=Rtrib,abs_transfer_receptor=Transfer))
    ok(Rtrib>0,'nonzero Rbranch')
with (OUT/'triadas_diadicas.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(triads[0]));writer.writeheader();writer.writerows(triads)

# Cross-scale coupling: a sum of two triads is not two independent dynamics.
def triad_at(n, amplitude):
    return [((n,0,0),(0,1,0),amplitude,0.),
            ((0,n,n),(1,0,0),amplitude,.3),
            ((n,n,n),(1,1,-2),amplitude/4.,-np.pi/2)]
W1=compose(triad_at(1,.025)); W2=compose(triad_at(2,.025*2**(-1.5)))
WW=compose(triad_at(1,.025)+triad_at(2,.025*2**(-1.5)))
F1=nonlinear(W1);F2=nonlinear(W2);FW=nonlinear(WW)
allk=set(FW)|set(F1)|set(F2)
Fc={k:FW.get(k,np.zeros(3,complex))-F1.get(k,np.zeros(3,complex))-F2.get(k,np.zeros(3,complex)) for k in allk}
cross_crit=sum(norm(z)/norm(k) for k,z in Fc.items())
novel_cross=sum(1 for k,z in Fc.items() if norm(z)>1e-12 and k not in W1 and k not in W2)
ok(cross_crit>1e-7,'interscale cross-terms nonzero')
ok(novel_cross>0,'new interscale modes beyond original support')
Ssum=measures(WW)
ok(Ssum['A0']**2<=Ssum['R']*Ssum['A1']+1e-12,'two-scale interpolation')
Dsum=dplus_R(WW,nu,FW)
ok(Dsum+(nu-Ssum['R'])*Ssum['A1']<1e-10,'two-scale critical budget')
ok(Ssum['R']<nu,'two-scale smallness')

result={"checks_passed":checks,"model":"3D incompressible periodic no forcing; Fourier at initial instant, not time integration", "theorem":"D+R+nu A1 <= A0^2 <= R A1", "nu":nu,"two_phase_cases":reports,"random_4wave_cases":96,"dilution_rows":len(rows),"triads":len(triads),"cross_scale":{"initial_R":Ssum["R"],"cross_critical_norm":cross_crit,"new_cross_modes":novel_cross,"initial_Dini_R":Dsum}}
(OUT/'o80_resumen.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks_passed':checks,'phase_results':reports,'dilution_rows':len(rows)},ensure_ascii=False,indent=2))
