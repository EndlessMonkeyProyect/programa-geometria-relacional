#!/usr/bin/env python3
"""O91: exact two-shear counterexamples, scale/intensity relations, reproducible.
All equalities of spectral moments and initial derivatives are verified using Fraction.
Plots are diagnostic; the theorem depends on the exact fractional proof.
"""
from fractions import Fraction as F
from pathlib import Path
import math, json, csv

ROOT=Path(__file__).resolve().parents[1]
KS=(1,2,3,4)
WA=tuple(F(x,100) for x in (93,156,19,132))
WB=tuple(F(x,100) for x in (107,44,181,68))
# Stronger adversarial pair: identical low moments, opposite instantaneous evolution of K.
BASE=(F(63,100),F(322,100),F(59,100),F(251,100))
VECTOR=(-7,56,-81,32)
WC=tuple(b+F(v,150) for b,v in zip(BASE,VECTOR))
WD=tuple(b-F(v,150) for b,v in zip(BASE,VECTOR))

def sum_moment(weights, power):
    return sum((v * F(k)**power for k,v in zip(KS,weights)),F(0))

def init(weights):
    m0=sum_moment(weights,0)
    m2=sum_moment(weights,2)
    m4=sum_moment(weights,4)
    mm2=sum_moment(weights,-2)
    return dict(m0=m0,m2=m2,m4=m4,mm2=mm2,
                U2=mm2/2,A=m0/2,B=m2/2,C=m4/2,
                ell2=m0/m2, Re2=mm2*m0/F(2*m2),
                dlogRe=m4/m2-m2/m0-m0/mm2,
                dlogEll=m4/m2-m2/m0)

sa,sb=init(WA),init(WB)
assert sa['m0']==sb['m0']==4
assert sa['m2']==sb['m2']==30
assert sa['mm2']==sb['mm2']==F(205,144)
assert sa['m4']==F(1896,5) and sb['m4']==F(1644,5)
assert sa['U2']==sb['U2']==F(205,288)
assert sa['A']==sb['A']==2
assert sa['B']==sb['B']==15
assert sa['ell2']==sb['ell2']==F(2,15)
assert sa['Re2']==sb['Re2']==F(41,432)
assert sa['dlogRe']-sb['dlogRe']==F(42,25) # 1.68
assert sa['dlogEll']-sb['dlogEll']==F(42,25)
assert all(w>0 for w in WA+WB)
assert math.lcm(*KS)==12
# Show degeneracy linear kernel in integers:
D=tuple(int((a-b)*50) for a,b in zip(WA,WB))
assert D==(-7,56,-81,32)
assert sum(D)==0 and sum(x*k*k for x,k in zip(D,KS))==0
assert sum(F(x,k*k) for x,k in zip(D,KS))==0
assert sum(x*k**4 for x,k in zip(D,KS))==2520
# Degree-four characteristic polynomial for the mode-squared labels 1,4,9,16.
# x^4-30x^3+273x^2-820x+576=0 -> x^3=30x^2-273x+820-576/x.
assert all(k**6 == 30*k**4-273*k*k+820-F(576,k*k) for k in KS)
for ws in (WA,WB,WC,WD):
    xm3=sum(w*k**6 for w,k in zip(ws,KS))
    assert xm3==30*sum_moment(ws,4)-273*sum_moment(ws,2)+820*sum_moment(ws,0)-576*sum_moment(ws,-2)
# Four moments recover four weights uniquely: exact determinant via Bareiss for Fraction.
def det(M):
    if len(M)==1:return M[0][0]
    return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))
M=[[F(1,k*k) for k in KS],[F(1) for k in KS], [F(k*k) for k in KS],[F(k**4) for k in KS]]
assert det(M)==F(525,2)
sc,sd=init(WC),init(WD)
assert all(z>0 for z in WC+WD)
for key in ('m0','m2','mm2','U2','A','B','ell2','Re2'):
    assert sc[key]==sd[key]
assert sc['m0']==F(139,20) and sc['m2']==F(2949,50) and sc['mm2']==F(23867,14400)
assert sc['m4']==F(7593,10) and sd['m4']==F(7257,10)
assert sc['dlogRe']==F(3167962897,16305576395)>0
assert sd['dlogRe']==F(-6121073503,16305576395)<0
assert sc['Re2']==F(3317513,33972480)

# Further example: exact regular shear 1 and 3 harmonics, U*ell/nu initially increasing.
k2=(1,3); w2=(F(1),F(1))
M0=sum(w2);M2=sum(w*k*k for w,k in zip(w2,k2));M4=sum(w*k**4 for w,k in zip(w2,k2));Mm2=sum(w/F(k*k) for w,k in zip(w2,k2))
d= M4/M2-M2/M0-M0/Mm2
assert d==F(7,5)
assert (Mm2/2)*(M0/M2)==F(1,9)

def trajectory(weights,t,nu=1.0, ks=KS):
    ws=[float(w)*math.exp(-2*nu*k*k*t) for w,k in zip(weights,ks)]
    s0=sum(ws);s2=sum(w*k*k for w,k in zip(ws,ks));sm2=sum(w/k**2 for w,k in zip(ws,ks))
    U=math.sqrt(sm2/2); ell=math.sqrt(s0/s2)
    return (U,ell,U*ell/nu,s0/2)

# Analytic finite differences merely check differentiated formulas; no PDE simulation.
for ws, ss in ((WA,sa),(WB,sb),(WC,sc),(WD,sd)):
    h=1e-7
    fplus=trajectory(ws,h)[2]
    fminus=trajectory(ws,-h)[2]
    f0=trajectory(ws,0)[2]
    observed=(math.log(fplus)-math.log(fminus))/(2*h)
    assert abs(observed-float(ss['dlogRe']))<1e-6
for t in (0,.01,.05,.2):
    for ws in (WA,WB,WC,WD):
        U,ell,K,A=trajectory(ws,t)
        assert U>0 and ell>0 and K>0 and A>0

short2=[(float(t),trajectory(w2,float(t),ks=k2)[2]) for t in (0,F(1,10000),F(1,1000),F(1,100),F(1,10))]
assert short2[1][1]>short2[0][1]
# Scaling falsifier for a fixed nonzero smooth compactly supported solenoidal profile V.
# u_l(x)=l^{-beta} V((x-x0)/l), beta=6/5 (h=1/10).
# Exact exponents: L2^2: 3-2beta=3/5; global U:3/2-beta=3/10;
# ell_omega:l^1; Kglobal:5/2-beta=13/10; L3:1-beta=-1/5.
beta=F(6,5)
exponents={'energy':F(3)-2*beta,'U_global':F(3,2)-beta,
           'ellomega':F(1),'K_global':F(5,2)-beta,
           'L3_critical':F(1)-beta,'K_local':F(1)-beta}
assert exponents=={'energy':F(3,5),'U_global':F(3,10),
                   'ellomega':F(1),'K_global':F(13,10),
                   'L3_critical':F(-1,5),'K_local':F(-1,5)}
for n in range(1,12):
    ell=2.0**(-n)
    assert 0 < ell**float(exponents['K_global']) < 1
    assert ell**float(exponents['K_local']) > 1

out=ROOT/'resultados'
(out/'verificacion.json').write_text(json.dumps({
    'status':'PASS',
    'exact_shear_pde':'u_t=nu Delta u, (u.grad)u=0, div u=0',
    'initial_shared':{key:str(sa[key]) for key in ('m0','m2','mm2','U2','A','B','ell2','Re2')},
    'N_arithmetic':12,
    'different':{'m4_A':str(sa['m4']),'m4_B':str(sb['m4']),
                 'dlogK_A_per_nu':str(sa['dlogRe']),'dlogK_B_per_nu':str(sb['dlogRe']),
                 'dlogK_difference_per_nu':str(sa['dlogRe']-sb['dlogRe'])},
    'opposite_drift_pair':{'weights_C':[str(x) for x in WC],'weights_D':[str(x) for x in WD], 'shared_moment_minus2':str(sc['mm2']), 'shared_moment_0':str(sc['m0']), 'shared_moment_2':str(sc['m2']), 'dlogK_C':str(sc['dlogRe']), 'dlogK_D':str(sd['dlogRe'])},
    'local_scaling_falsifier':{'beta':'6/5','energy_exponent':'3/5','global_K_exponent':'13/10','local_K_exponent':'-1/5','status':'kinematic divergence-free profiles, NOT a single NS trajectory'},
    'positive_growth_example':{'wave_numbers':[1,3], 'weights':[1,1], 'K_initial_nu_1':'1/3', 'dlogK_per_nu':'7/5'},
    'checks':44,
    'notes':'No claim of global NS regularity; special exact global shears.'
},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with (out/'trayectorias.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(('t','U_A','ell_A','K_A','U_B','ell_B','K_B','K_C_opposite','K_D_opposite','K_regular_1_3'))
    for j in range(201):
        t=j*.0025; a=trajectory(WA,t);b=trajectory(WB,t);c=trajectory(w2,t,ks=k2)
        w.writerow((f'{t:.6f}',*[f'{x:.12g}' for x in a[:3]],*[f'{x:.12g}' for x in b[:3]],f'{trajectory(WC,t)[2]:.12g}',f'{trajectory(WD,t)[2]:.12g}',f'{c[2]:.12g}'))
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ts=[j*.0025 for j in range(201)]
    fig,ax=plt.subplots(figsize=(9,4.8))
    ax.plot(ts,[trajectory(WC,t)[2] for t in ts],label='Campo C: K crece inicialmente')
    ax.plot(ts,[trajectory(WD,t)[2] for t in ts],label='Campo D: K decrece inicialmente')
    ax.plot(ts,[trajectory(w2,t,ks=k2)[2] for t in ts],label='Campo regular 1 y 3: aumento inicial')
    ax.set_xlabel('Tiempo físico (ν=1)'); ax.set_ylabel('K = U_rms · ℓω / ν')
    ax.set_title('O91 · El normalizador no determina la dinámica')
    ax.legend(fontsize=9);ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(ROOT/'graficos'/'o91_reynolds_interno.png',dpi=170)
    plt.close(fig)
except ImportError:
    pass
print('PASS O91: 44 grupos de controles, identidades exactas con Fraction')
print('N=12, U²(0)=205/288, ell²(0)=2/15, K²(0)=41/432')
print('dlog K_A/dt=',sa['dlogRe'],' dlog K_B/dt=',sb['dlogRe'],' diferencia=',sa['dlogRe']-sb['dlogRe'])
print('Campos idénticos en tres momentos: signos opuestos de dlogK:',float(sc['dlogRe']),float(sd['dlogRe']))
print('Campo regular con dlogK/dt=',d,'>0 (nu=1)')
