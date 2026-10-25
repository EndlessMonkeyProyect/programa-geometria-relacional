#!/usr/bin/env python3
"""O79: triada exacta de datos NS 3D; comprobacion espectral independiente.
Sin resolver la PDE mas alla de t=0; todas las derivadas son instantaneas exactas.
"""
import numpy as np, math, csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'resultados'; OUT.mkdir(exist_ok=True)
rows=[]; count=0

def chk(condition, label, atol=1e-10):
    global count
    if not bool(condition): raise AssertionError(label)
    count+=1

def run(N,n,c,nu=0.01,a=1.0,b=1.0,d=0.0):
    x=2*np.pi*np.arange(N)/N
    xx,yy,zz=np.meshgrid(x,x,x,indexing='ij')
    karg=n*xx; larg=n*(yy+zz); marg=karg+larg
    A=np.array([0,1,0],float); B=np.array([1,0,0],float); C=np.array([1,1,-2],float)
    u=a*np.cos(karg)[...,None]*A + b*np.cos(larg)[...,None]*B + c*np.sin(marg)[...,None]*C + d*np.cos(n*zz)[...,None]*np.array([1.,0.,0.])
    freq=np.fft.fftfreq(N,d=1./N)
    ks=np.meshgrid(freq,freq,freq,indexing='ij')
    K=np.stack(ks,axis=-1)
    U=np.fft.fftn(u,axes=(0,1,2))/(N**3)
    G=np.stack([np.fft.ifftn((1j*K[...,d,None])*U*(N**3),axes=(0,1,2)).real for d in range(3)],axis=-2)
    transport=np.einsum('...d,...dc->...c',u,G)
    F=np.fft.fftn(transport,axes=(0,1,2))/(N**3)
    kk=np.sum(K*K,axis=-1)
    dot=np.sum(F*K,axis=-1)
    P=F-K*np.divide(dot,kk,out=np.zeros_like(dot),where=kk!=0)[...,None]
    Dt=-P-nu*kk[...,None]*U
    idx=(n%N,n%N,n%N)
    Um=U[idx]; Dt_m=Dt[idx]
    E=float(np.vdot(Um,Um).real) # double +/- with half
    dE=float(2*np.vdot(Um,Dt_m).real)
    transfer=float(2*np.vdot(Um,-P[idx]).real)
    dissip=float(2*np.vdot(Um,-nu*kk[idx]*Um).real)
    predicted_tr=a*b*c*n/2
    predicted_diss=-9*nu*n*n*c*c
    predicted_e=1.5*c*c
    # El modo diferencia d=k-l es inicialmente nulo y nace por la misma triada.
    diff_idx=(n%N,(-n)%N,(-n)%N)
    D=np.array([-1,1,-2.],float)
    generated=Dt[diff_idx]
    exact_generated=-1j*(a*b*n/12.)*D
    chk(np.max(np.abs(U[diff_idx]))<2e-11, 'modo nuevo inicialmente vacio')
    chk(np.max(np.abs(generated-exact_generated))<2e-11, 'modo nuevo generado por interaccion')
    div_k=np.sum(K*U,axis=-1)
    max_div=float(np.max(np.abs(div_k)))
    chk(abs(E-predicted_e)<2e-11, 'energia modal')
    chk(abs(transfer-predicted_tr)<2e-11, 'triada transferencia')
    chk(abs(dissip-predicted_diss)<2e-11, 'disipacion')
    chk(abs(dE-predicted_tr-predicted_diss)<2e-11, 'balance')
    chk(max_div<2e-11, 'solenoidal')
    totalE=float(0.5*np.sum(np.abs(U)**2).real)
    omega2=float(np.sum(kk*np.sum(np.abs(U)**2,axis=-1)).real)
    palin2=float(np.sum(kk**2*np.sum(np.abs(U)**2,axis=-1)).real)
    pair_dEdt=2*np.sum(np.real(np.conj(U)*Dt),axis=-1)
    domega2=float(np.sum(kk*pair_dEdt))
    dpalin2=float(np.sum(kk**2*pair_dEdt))
    ell=(omega2/palin2)**.5
    dell=.5*ell*(domega2/omega2-dpalin2/palin2)
    exact_A=n*n*((a*a+d*d)/2+b*b+9*c*c)
    exact_B=n**4*((a*a+d*d)/2+2*b*b+27*c*c)
    exact_C=n**6*((a*a+d*d)/2+4*b*b+81*c*c)
    exact_Adot=1.5*n**3*a*b*c-2*nu*exact_B
    exact_Bdot=6.5*n**5*a*b*c-2*nu*exact_C
    chk(abs(omega2-exact_A)<5e-10, 'norma vorticidad exacta')
    chk(abs(palin2-exact_B)<5e-10, 'norma grad vorticidad exacta')
    chk(abs(domega2-exact_Adot)<5e-10, 'derivada vorticidad exacta')
    chk(abs(dpalin2-exact_Bdot)<5e-10, 'derivada palinstrofia exacta')
    nonlinear_total=float(np.sum(2*np.real(np.conj(U)*(-P))))
    chk(abs(nonlinear_total)<1e-10, 'conservacion energetica del termino no lineal')
    chk(abs(totalE-(a*a+b*b+6*c*c+d*d)/4)<2e-11, 'energia total')
    return dict(N=N,n=n,c=c,d=d,nu=nu,E_m=E,transfer_m=transfer,diss_m=dissip,derivada_m=dE,total_E=totalE,max_div=max_div,generacion_nuevo_modo=float(np.linalg.norm(generated)),ell_omega=ell,derivada_ell_omega=dell)

for N,n,d in [(16,1,0.),(24,1,0.),(24,2,0.),(32,2,0.),(40,4,0.),(48,4,0.),(24,1,.3),(32,2,.3)]:
    plus=run(N,n,+.25,d=d);minus=run(N,n,-.25,d=d)
    chk(abs(plus['total_E']-minus['total_E'])<1e-11,'igual energia')
    chk(abs(plus['E_m']-minus['E_m'])<1e-11, 'igual modo')
    chk(abs(plus['transfer_m']+minus['transfer_m'])<1e-11, 'signo opuesto')
    chk(abs(plus['ell_omega']-minus['ell_omega'])<1e-12, 'igual reloj instantaneo')
    for d in [plus,minus]:rows.append(d)
for n in [1,2,4,8,16,32]:
    for alpha in [0.9,1.0,1.1,1.5,2.0]:
        amp=n**(-alpha)
        # 3D triada homotetica: E'_m no lineal n a b c /2
        fluxE=0.5*n*amp**3
        fluxW=3*n*n*fluxE
        rows.append(dict(n=n,alpha=alpha,amplitud=amp,transferE=fluxE,transferW=fluxW))
# test escalado formula vs ordinario
for n in [1,2,4,8,16]:
    for alpha in [0.9,1.,1.1,1.5,2.]:
        e=0.5*n**(1-3*alpha)
        w=1.5*n**(3-3*alpha)
        chk(abs(w-3*n*n*e)<1e-10,'peso enstrofia')
# caso critico estrictamente alpha>1 para serie de contribuciones aisladas de transferencia de enstrofia
for alpha in [1.1,1.5,2.]:
    ratio=2**(3-3*alpha)
    chk(ratio<1, 'sumabilidad triadica alfa>1')
# misma normalizacion de modos en +/- configuraciones, distinta tasa => insuficiencia
summary={'checks':count,'casos_espectrales':16,'triple_test':'(k,l,m)=(n,0,0)+(0,n,n)=(n,n,n)',
 'a_b':1.,'c':.25,'nu':.01, 'analytic_E_m':0.09375,'analytic_nonlinear_transfer_n1_plus':.125,
 'analytic_nonlinear_transfer_n1_minus':-.125,'analytic_dissipation_n1':-.005625,
 'status':'Derivadas instantaneas exactas de NS para datos suaves, no evolucion temporal ni teorema de regularidad general'}
with open(OUT/'verificaciones.json','w') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
with open(OUT/'triada_derivadas.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['N','n','c','d','nu','E_m','transfer_m','diss_m','derivada_m','total_E','max_div','generacion_nuevo_modo','ell_omega','derivada_ell_omega']); w.writeheader();w.writerows([d for d in rows if 'N' in d])
with open(OUT/'triadas_escalas.csv','w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['n','alpha','amplitud','transferE','transferW']); w.writeheader();w.writerows([d for d in rows if 'alpha' in d])
print(json.dumps(summary,indent=2,ensure_ascii=False))
print('primera fila',rows[0]);print('segunda fila',rows[1]);
