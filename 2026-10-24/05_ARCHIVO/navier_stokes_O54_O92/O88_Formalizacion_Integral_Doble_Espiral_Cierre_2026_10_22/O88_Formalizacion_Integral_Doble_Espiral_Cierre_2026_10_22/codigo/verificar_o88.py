#!/usr/bin/env python3
"""Reproduce SOLO las identidades algebraicas/cinemáticas de O88.
No integra Navier-Stokes ni pretende certificar regularidad PDE.
"""
from __future__ import annotations
import csv, json, math, pathlib, random
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'resultados'
OUT.mkdir(exist_ok=True)
R, a, kappa, p, q = 2., .6, .8, 1, 2
checks = 0
rng = random.Random(88)


def check(cond, label, payload=None):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(f'Falla {checks}: {label}: {payload}')


def gamma(chi):
    return chi + a / (q * R) * math.sin(q * chi)


def inv_gamma(g):
    # gamma is strictly increasing, gamma(x)-x bounded by a/(qR)
    margin = 1+a/(q*R)
    lo, hi = g-margin, g+margin
    for _ in range(75):
        mid = (lo+hi)/2
        if gamma(mid) < g: lo=mid
        else: hi=mid
    return (lo+hi)/2

# 1. Normalization of moving nodes, phase preserving while geometrical intervals change.
rows = []
for step in range(41):
    t = step / 10
    phases = [.1 + i*math.pi/2 + kappa/R*t for i in range(4)]
    chis = [inv_gamma(g) for g in phases]
    for i, (g, chi) in enumerate(zip(phases, chis)):
        check(abs(gamma(chi) - g) < 2e-14, 'invertible normalized phase')
        phidot = p*kappa/(R+a*math.cos(q*chi))
        thetadot = q*kappa/(R+a*math.cos(q*chi))
        check(abs(p*thetadot-q*phidot)<1e-14, 'locked phase derivative')
        check(abs((1+a/R*math.cos(q*chi))*(kappa/(R+a*math.cos(q*chi))) - kappa/R)<1e-14,'gamma uniform derivative')
    check(abs(chis[2]-chis[0]-math.pi) < 2e-14, 'first opposite pair')
    check(abs(chis[3]-chis[1]-math.pi) < 2e-14, 'second opposite pair')
    rows.append([round(t,8), *(round(ch,12) for ch in chis), round(chis[1]-chis[0]-math.pi/2, 12)])

# 2. Divergence, derivatives of area flux (analytically constant and single-variable)
for i in range(100):
    theta = rng.uniform(-math.pi, math.pi)
    phi = rng.uniform(-math.pi, math.pi)
    eps = 0.25
    J = a*(R+a*math.cos(theta))
    ft = J*(q*(kappa+eps*math.sin(phi))/(R+a*math.cos(theta)))
    fp = J*(p*kappa/(R+a*math.cos(theta)))
    check(abs(ft - a*q*(kappa+eps*math.sin(phi))) < 1e-14, 'theta area-flux independent of theta')
    check(abs(fp - a*p*kappa)<1e-14,'phi area-flux independent of phi')
    Dpsi = p*q*eps*math.sin(phi)/(R+a*math.cos(theta))
    check(abs(p*q*(kappa+eps*math.sin(phi))/(R+a*math.cos(theta)) - q*p*kappa/(R+a*math.cos(theta)) - Dpsi) < 1e-14, 'phase drift exact')

# 3. Primitive pair and unimodular Bézout mapping. Exhaust modest pairs.
def egcd(a,b):
    if b==0: return (1,0,a)
    u,v,g = egcd(b,a%b)
    return (v,u-(a//b)*v,g)

for q_ in range(1,18):
    for p_ in range(1,18):
        if math.gcd(q_,p_) != 1: continue
        b,c,gcd=egcd(q_,p_)
        check(gcd==1 and b*q_+c*p_==1, 'bezout')
        check(-b*q_-c*p_==-1,'unimodular determinant')
        for _ in range(5):
            th=rng.uniform(-10,10); ph=rng.uniform(-10,10)
            Phi=b*th+c*ph; Psi=p_*th-q_*ph
            check(abs(q_*Phi+c*Psi-th)<1e-12 and abs(p_*Phi-b*Psi-ph)<1e-12, 'bezout inverse')

# 4. Cover map z -> N z, N^2 preimages exactly recovered with label h.
for N in range(2,10):
    for _ in range(20):
        y0 = rng.uniform(0, 2*math.pi)
        y1 = rng.uniform(0, 2*math.pi)
        seen=set()
        for h0 in range(N):
            for h1 in range(N):
                x0=(y0+2*math.pi*h0)/N
                x1=(y1+2*math.pi*h1)/N
                seen.add((h0,h1))
                check(abs((N*x0-y0)/(2*math.pi)-h0)<2e-15 and abs((N*x1-y1)/(2*math.pi)-h1)<2e-15,'scale inversion with sheet')
        check(len(seen)==N*N,'N² distinct branch tags')

# 5. Four-gear holonomy, exact fractions, not a fluid law.
for _ in range(200):
    r=[Fraction(rng.randint(1,20),rng.randint(1,15)) for i in range(4)]
    H=Fraction(1)
    for i in range(4): H *= r[i]/r[(i+1)%4]
    check(H==1,'telescoping four-contact holonomy')
    speeds=[(-1)**i/r[i] for i in range(4)]
    for i in range(4): check(r[i]*speeds[i]+r[(i+1)%4]*speeds[(i+1)%4]==0, 'gear contact')

# 6. Common-frame angular origin cancels in inter-node phase differences.
for _ in range(300):
    th1, th2 = rng.uniform(-3,3), rng.uniform(-3,3)
    ph1, ph2 = rng.uniform(-3,3), rng.uniform(-3,3)
    alpha,beta=rng.uniform(-5,5),rng.uniform(-5,5)
    psi=(p*th1-q*ph1)-(p*th2-q*ph2)
    transformed=(p*(th1-alpha)-q*(ph1-beta))-(p*(th2-alpha)-q*(ph2-beta))
    check(abs(psi-transformed)<1e-14,'common-frame gauge invariance')

with (OUT/'o88_nodos_fases.csv').open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['tiempo','chi_0','chi_1','chi_2','chi_3','separacion_vecinal_menos_pi_2'])
    w.writerows(rows)
summary={
    'fecha': '2026-10-22',
    'verificaciones': checks,
    'mensaje': 'Identidades algebraicas y cinemáticas O88: verificadas; NO es un experimento Navier-Stokes 3D.',
    'R':R,'a':a,'kappa':kappa,'p':p,'q':q,
    'desfase_vecinal_max_abs': max(abs(row[-1]) for row in rows),
    'limite': 'No se deriva conservación física universal, regularidad PDE ni nodos físicos desde estas identidades.'
}
(OUT/'verificacion_o88.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2,ensure_ascii=False))
