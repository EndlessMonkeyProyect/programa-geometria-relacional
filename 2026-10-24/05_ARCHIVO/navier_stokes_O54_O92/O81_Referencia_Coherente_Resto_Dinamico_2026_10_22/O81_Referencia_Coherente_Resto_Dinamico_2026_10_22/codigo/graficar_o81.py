#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
nu=1.0;aa=np.linspace(0,3.5,350)
threshold=nu/2*np.exp(-2*(aa/nu)**2)
fig,ax=plt.subplots(figsize=(9,4.7))
ax.semilogy(aa,threshold,label=r'$R_v(0)<(\nu/2)e^{-2(A/\nu)^2}$')
ax.scatter([2],[.0001],marker='o',label=r'Ejemplo: $A/\nu=2$, $R_v(0)=10^{-4}$')
ax.scatter([2],[.5*np.exp(-8)],marker='x',label=r'Umbral estricto para $A/\nu=2$')
ax.set_xlabel(r'Amplitud de la referencia $|A|/\nu$')
ax.set_ylabel(r'Maximo resto crítico permitido $R_v(0)/\nu$')
ax.set_title('O81: ventana de estabilidad alrededor de una referencia coherente')
ax.grid(alpha=.3)
ax.legend(loc='lower left',fontsize=9)
fig.tight_layout();fig.savefig(root/'graficos'/'o81_ventana_resto.png',dpi=180);plt.close(fig)

t=np.linspace(0,7,350);A=2.;R0=.0001
G=2*A**2*(1-np.exp(-2*t));Rbar=R0*np.exp(G)
fig,ax=plt.subplots(figsize=(9,4.7))
ax.plot(t,Rbar,label='Mayorante analítico del resto')
ax.axhline(.5,ls='--',label=r'Barrera $\nu/2$')
ax.set_xlabel('Tiempo físico t')
ax.set_ylabel(r'Mayorante para $R_v(t)$')
ax.set_title('O81: el resto permanece por debajo de la barrera')
ax.legend();ax.grid(alpha=.3)
fig.tight_layout();fig.savefig(root/'graficos'/'o81_barrera_dinamica.png',dpi=180);plt.close(fig)
