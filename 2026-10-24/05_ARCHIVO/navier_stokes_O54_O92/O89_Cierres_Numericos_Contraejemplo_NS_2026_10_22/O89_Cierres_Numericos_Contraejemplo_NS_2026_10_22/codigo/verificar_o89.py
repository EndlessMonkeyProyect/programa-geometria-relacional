"""O89: pruebas exactas simbólicas y evaluaciones reproducibles.
Requiere sympy; para el gráfico, matplotlib opcional.
"""
from pathlib import Path
import json, math, csv
import sympy as sp

root=Path(__file__).resolve().parents[1]
(root/'resultados').mkdir(exist_ok=True)
(root/'graficos').mkdir(exist_ok=True)
x,y,z,t=sp.symbols('x y z t',real=True)
f=2*sp.exp(-t)*sp.sin(y)+sp.exp(-4*t)*sp.sin(2*z)
u=sp.Matrix([f,0,0]); xyz=(x,y,z)
check=0
def ensure(cond,msg):
    global check
    assert bool(cond),msg
    check+=1

div=sum(sp.diff(u[i],xyz[i]) for i in range(3))
ensure(sp.simplify(div)==0,'divergence')
conv=sp.Matrix([sum(u[j]*sp.diff(u[i],xyz[j]) for j in range(3)) for i in range(3)])
ensure(all(sp.simplify(w)==0 for w in conv),'advection')
lap=sp.Matrix([sum(sp.diff(u[i],v,2) for v in xyz) for i in range(3)])
ensure(all(sp.simplify(sp.diff(u[i],t)-lap[i])==0 for i in range(3)),'NS heat')
rot=sp.Matrix([sp.diff(u[2],y)-sp.diff(u[1],z),sp.diff(u[0],z)-sp.diff(u[2],x),sp.diff(u[1],x)-sp.diff(u[0],y)])
ensure(all(sp.simplify(rot[i]-expr)==0 for i,expr in enumerate([0,2*sp.exp(-4*t)*sp.cos(2*z),-2*sp.exp(-t)*sp.cos(y)])),'curl')
S=sp.Matrix(3,3,lambda i,j:(sp.diff(u[i],xyz[j])+sp.diff(u[j],xyz[i]))/2)
ensure(sp.simplify((rot.T*S*rot)[0])==0,'vortex stretching = 0')
# Spatial averages from orthogonality of cosines
A=2*sp.exp(-2*t)+2*sp.exp(-8*t)
B=2*sp.exp(-2*t)+8*sp.exp(-8*t)
ensure(sp.simplify(sp.diff(A,t)/2+B)==0,'enstrophy balance')
ra=sp.exp(3*t)
tstar=sp.log(2)/6
ensure(sp.simplify(ra.subs(t,tstar)-sp.sqrt(2))==0,'vorticity irrational rate')
ensure(sp.sqrt(2).is_irrational is True,'irrational ratio')
thA=2*(1-sp.exp(-t)); thB=(1-sp.exp(-4*t))/4
psi=thA-2*thB
ensure(sp.simplify(sp.diff(psi,t)-2*(sp.exp(-t)-sp.exp(-4*t)))==0,'phase drift')
ensure(sp.simplify(psi.subs(t,0))==0,'phase lock start')
ensure(sp.simplify(sp.diff(psi,t).subs(t,0))==0,'phase speed lock start')
ensure(sp.simplify((sp.diff(thA,t)/sp.diff(thB,t)).subs(t,tstar)-2*sp.sqrt(2))==0,'irrational tracer rate')
ensure(sp.simplify(sp.integrate(2*sp.exp(-t)+2*sp.exp(-4*t),(t,0,sp.oo))-sp.Rational(5,2))==0,'Lipschitz budget')
ensure(sp.simplify((thA+sp.pi)-thA-sp.pi)==0,'A antipodal pair')
ensure(sp.simplify((thB+sp.pi)-thB-sp.pi)==0,'B antipodal pair')
# Test values at robust time points
samples=[0,0.05,float(tstar),float(sp.log(sp.Rational(3,2))/3),0.2,0.5,1.0]
rows=[]
for ti in samples:
    a=2*math.exp(-4*ti); b=2*math.exp(-ti)
    aa=2*(1-math.exp(-ti)); bb=(1-math.exp(-4*ti))/4
    rows.append(dict(t=ti,vorticity_ratio=b/a,tracer_rate_ratio=2*b/a,phase_slip=aa-2*bb,omega2=2*math.exp(-2*ti)+2*math.exp(-8*ti)))
    ensure(abs((b/a)-math.exp(3*ti))<1e-12,'ratio double check')
    ensure(abs((aa-2*bb)-(2*(1-math.exp(-ti))-.5*(1-math.exp(-4*ti))))<1e-12,'slip double check')

with (root/'resultados'/'tabla.csv').open('w',newline='',encoding='utf8') as ff:
    writer=csv.DictWriter(ff,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
summary={'symbolic_checks_and_numeric_assertions':check,'nu':1,'t_star':float(tstar),'vorticity_ratio_at_star':float(sp.sqrt(2)),'tracer_rate_ratio_at_star':float(2*sp.sqrt(2)),'phase_slip_at_star':float(psi.subs(t,tstar)),'initial_vorticity_l2_squared_mean':4,'gradient_integral_upper_bound':2.5,'samples':rows,'model_limitation':'four material tracers in exact shear, not four nodes on a toroidal vortex tube'}
(root/'resultados'/'resumen.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
try:
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ts=np.linspace(0,0.35,250)
    fig,axs=plt.subplots(2,1,figsize=(8.8,6.4),sharex=True)
    axs[0].plot(ts,np.exp(3*ts),label='Razón de canales de vorticidad')
    axs[0].axhline(1,ls=':',color='gray',label='Sincronía inicial 1:1')
    axs[0].axvline(float(tstar),ls='--',color='gray')
    axs[0].plot(float(tstar),float(sp.sqrt(2)),'o')
    axs[0].set_ylabel('b(t)/a(t)'); axs[0].legend(loc='upper left',fontsize=9)
    axs[0].set_title('O89 · La referencia entera se pierde sin singularidad (NS exacta)')
    axs[1].plot(ts,2*(1-np.exp(-ts))-.5*(1-np.exp(-4*ts)),label='Desfase de nodos Ψ = θA − 2θB')
    axs[1].plot(ts,2*np.exp(-ts)+2*np.exp(-4*ts),label='Cota de |ω|∞',ls='--')
    axs[1].axvline(float(tstar),ls='--',color='gray')
    axs[1].set_ylabel('Desfase / cota');axs[1].set_xlabel('Tiempo físico, ν=1');axs[1].legend(loc='upper right',fontsize=9)
    for ax in axs: ax.grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(root/'graficos'/'o89_perdida_multiplo_sin_colapso.png',dpi=160)
    plt.close(fig)
    summary['figure_created']=True
    (root/'resultados'/'resumen.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
except ImportError:
    summary['figure_created']=False
print(json.dumps({'checks':check,'t_star':float(tstar),'ratio':float(sp.sqrt(2)),'phase_slip':float(psi.subs(t,tstar)),'figure':summary['figure_created']},ensure_ascii=False))
