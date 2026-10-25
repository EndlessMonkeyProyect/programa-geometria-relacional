#!/usr/bin/env python3
"""Two separate reproducible static plots for the analytic O78 shear solutions."""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'graficos'; FIG.mkdir(exist_ok=True)
Js=np.arange(1,17)
plt.figure(figsize=(8.2,4.8))
for alpha in (1.,1.5,2.):
    vals=[0.5*sum(2.**(2*(1-alpha)*j) for j in range(1,J+1)) for J in Js]
    plt.plot(Js,vals,marker='o',markersize=3,label=f'α = {alpha:g}')
plt.xlabel('Número de ramas J')
plt.ylabel('Vorticidad cuadrática media inicial')
plt.title('O78 — Más ramas no implica dilución suficiente')
plt.legend();plt.grid(alpha=.2);plt.tight_layout()
plt.savefig(FIG/'o78_dilucion_ramas.png',dpi=160);plt.close()

nu=.025; J=8; jj=np.arange(1,J+1); kk=2.**jj
Ts=np.linspace(0,.5,350)
plt.figure(figsize=(8.2,4.8))
for alpha in (1.,1.5,2.):
    a=2.**(-alpha*jj)
    ell=[]
    for t in Ts:
        w=(kk*a)**2*np.exp(-2*nu*kk**2*t)
        ell.append(np.sqrt(np.sum(w)/np.sum(w*kk*kk)))
    plt.plot(Ts,ell,label=f'α = {alpha:g}')
plt.xlabel('Tiempo físico t (unidades del laboratorio)')
plt.ylabel('Longitud endógena ℓω(t)')
plt.title('O78 — Escala del flujo: crecimiento por difusión en el sector exacto')
plt.legend();plt.grid(alpha=.2);plt.tight_layout()
plt.savefig(FIG/'o78_reloj_escala_endogena.png',dpi=160);plt.close()
print('Figuras guardadas en',FIG)
