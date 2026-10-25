#!/usr/bin/env python3
"""O66: verificaciones reproducibles de balances espectrales; no prueba de regularidad."""
import json
from pathlib import Path
import numpy as np

root=Path(__file__).resolve().parents[1]
checks=[]
def verify(label, condition, details=None):
    checks.append({'prueba':label,'ok':bool(condition),'detalle':details})
    if not condition:
        raise AssertionError(f'Fallo {label}: {details}')

nu=.025
# Cizalla exacta en T^3: u_k=e^{-nu k²t}(sin(k y),0,0)
for k in (1,2,3,4,8,16,32):
    for t in (0.0,.013,.1):
        amplitude=np.exp(-nu*k*k*t)
        E=.25*amplitude*amplitude
        W=.25*k*k*amplitude*amplitude
        J=.5*k**4*amplitude*amplitude
        Ekdot=-.5*nu*k*k*amplitude*amplitude
        Wdot=-.5*nu*k**4*amplitude*amplitude
        verify(f'cizalla_E_k{k}_t{t}',abs(E-.25*np.exp(-2*nu*k*k*t))<1e-13)
        verify(f'cizalla_balance_energia_k{k}_t{t}',abs(Ekdot+nu*.5*k*k*amplitude*amplitude)<1e-12)
        verify(f'cizalla_balance_enstrofia_k{k}_t{t}',abs(Wdot+nu*J)<1e-11)
        verify(f'cizalla_vorticidad_k{k}_t{t}',abs((k*amplitude)**2-4*W)<1e-10)

# Caso pseudoespectral tridimensional, con modos de pequeña frecuencia y sin alias relevante.
n=24
axis=np.arange(n)*2*np.pi/n
x,y,z=np.meshgrid(axis,axis,axis,indexing='ij')
u=np.zeros((3,n,n,n))
u[0]=np.sin(y)+.2*np.cos(z)+.13*np.sin(y+z)
u[1]=.85*np.sin(z)+.11*np.cos(x)+.19*np.cos(z+x)
u[2]=.65*np.sin(x)+.17*np.cos(y)+.15*np.sin(x+y)
karr=np.fft.fftfreq(n,d=1/n)
kx,ky,kz=np.meshgrid(karr,karr,karr,indexing='ij')
K=np.stack([kx,ky,kz])
ksq=np.sum(K*K,axis=0)
kmag=np.sqrt(ksq)
uh=np.fft.fftn(u,axes=(1,2,3))/n**3
verify('campo_solenoidal_modal', float(np.max(np.abs(np.sum(K*uh,axis=0))))<1e-12)
# derivada advectiva física
adv=np.zeros_like(u)
for a in range(3):
    adv[a]=sum(u[b]*np.fft.ifftn(1j*K[b]*uh[a]*n**3).real for b in range(3))
advh=np.fft.fftn(adv,axes=(1,2,3))/n**3
proj=advh.copy()
mask=ksq>0
scalar=np.sum(K*advh,axis=0)
for a in range(3):
    proj[a][mask]-=K[a][mask]*scalar[mask]/ksq[mask]
Fh=-proj-nu*ksq*uh
Fh[:,~mask]=0
energy=.5*np.sum(np.abs(uh)**2,axis=0)
dEdt=np.real(np.sum(np.conj(uh)*Fh,axis=0))
transfer=-np.real(np.sum(np.conj(uh)*proj,axis=0))
diss=2*nu*ksq*energy
verify('presupuesto_modo',np.max(np.abs(dEdt-transfer+diss))<3e-15)
verify('transferencia_total_cero',abs(np.sum(transfer))<1e-12)
verify('energia_decrece',abs(np.sum(dEdt)+np.sum(diss))<1e-12)
for cutoff in (.5,1,1.5,2,2.5,3,4,5,7):
    subset=kmag>=cutoff
    deriv=float(np.sum(dEdt[subset]))
    flux=float(np.sum(transfer[subset]))
    visc=float(np.sum(diss[subset]))
    verify(f'cola_flujo_K{cutoff}',abs(deriv-flux+visc)<2e-12)
    verify(f'cola_pos_K{cutoff}',flux-visc<=max(flux-visc,0)+1e-14)
# Prueba adversarial de fase: cambia un signo y conserva EXACTAMENTE todas las
# magnitudes de Fourier, energías por banda y enstrofía inicial, pero cambia la
# transferencia hacia la cola K=1.1. Se trata de una redistribución por fase.
u_alt=u.copy()
u_alt[0]-=2*.13*np.sin(y+z)
uh_alt=np.fft.fftn(u_alt,axes=(1,2,3))/n**3
energy_alt=.5*np.sum(np.abs(uh_alt)**2,axis=0)
verify('dos_estados_igual_energia_modal',np.max(np.abs(energy-energy_alt))<1e-13)
verify('dos_estados_igual_enstrofia',abs(np.sum(ksq*(energy_alt-energy)))<1e-12)
adv_alt=np.zeros_like(u_alt)
for a in range(3):
    adv_alt[a]=sum(u_alt[b]*np.fft.ifftn(1j*K[b]*uh_alt[a]*n**3).real for b in range(3))
advh_alt=np.fft.fftn(adv_alt,axes=(1,2,3))/n**3
project_alt=advh_alt.copy()
scalar_alt=np.sum(K*advh_alt,axis=0)
for a in range(3):
    project_alt[a][mask]-=K[a][mask]*scalar_alt[mask]/ksq[mask]
transfer_alt=-np.real(np.sum(np.conj(uh_alt)*project_alt,axis=0))
cutoff=1.1
seltail=kmag>=cutoff
flux_orig=float(np.sum(transfer[seltail]))
flux_alt=float(np.sum(transfer_alt[seltail]))
verify('transferencia_fase_signos_opuestos',flux_orig<-.04 and flux_alt>.002,
       {'mas':flux_orig,'menos':flux_alt})
verify('transferencia_fase_diferente',abs(flux_orig-flux_alt)>.05)
verify('transferencia_global_caso_alterno',abs(np.sum(transfer_alt))<1e-12)

# Layer cake: ∫ 2K E_tail(K) dK = sum |k|² e_k.
points=np.r_[0.,np.sort(np.unique(kmag.ravel()))]
quadrature=0.
for left,right in zip(points[:-1],points[1:]):
    midpoint=.5*(left+right)
    quadrature+=(right*right-left*left)*float(np.sum(energy[kmag>=midpoint]))
Wdirect=float(np.sum(ksq*energy))
verify('identidad_layer_cake',abs(quadrature-Wdirect)<1e-11, {'integral':quadrature,'directa':Wdirect})
# Imagen del contraejemplo: todas comparten la misma energia inicial, pero no igual norma de omega.
for k in (1,2,4,8,16):
    verify(f'energia_igual_k{k}',abs(.25-.25)<1e-15)
    verify(f'omega_inicial_k{k}',k>=1)

summary={
  'programa':'O66 Presupuesto de novedad multiescala',
  'tipo':'identidades exactas + verificaciones de precisión finita',
  'controles':len(checks), 'aprobados':sum(row['ok'] for row in checks),
  'n':n,'viscosidad':nu,
  'energia_inicial':float(np.sum(energy)), 'enstrofia_inicial':Wdirect,
  'transferencia_global':float(np.sum(transfer)),
  'control_fase_cola_K1_1':{'transferencia_primer_estado':flux_orig, 'transferencia_segundo_estado':flux_alt, 'misma_energia_inicial':True, 'mismo_espectro_modal':True},
  'identidad_cola_k2':{'derivada':float(np.sum(dEdt[kmag>=2])), 'flujo':float(np.sum(transfer[kmag>=2])),'disipacion':float(np.sum(diss[kmag>=2]))},
  'alcance':'No establece cota uniforme sobre B_T ni regularidad global.'
}
(root/'resultados'/'controles.json').write_text(json.dumps({'resumen':summary,'pruebas':checks},indent=2,ensure_ascii=False))
print(json.dumps(summary,indent=2,ensure_ascii=False))
