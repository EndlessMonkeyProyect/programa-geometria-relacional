#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
P=Path(__file__).resolve().parents[1]
records=list(csv.DictReader(open(P/'resultados/triada_derivadas.csv')))
selected=[r for r in records if int(r['n'])==1 and int(r['N'])==16]
cases=['Fase A','Fase B']
transfer=[float(r['transfer_m']) for r in selected]
ell=[float(r['derivada_ell_omega']) for r in selected]
fig,ax=plt.subplots(figsize=(8.4,4.4))
xx=np.arange(2)
ax.bar(xx-.19,transfer,.38,label='Transferencia no lineal al modo')
ax.bar(xx+.19,ell,.38,label='Derivada de escala endógena')
ax.axhline(0,linewidth=.8)
ax.set_xticks(xx,cases)
ax.set_ylabel('Derivada instantánea (unidades del laboratorio)')
ax.set_title('Misma referencia inicial, dos reorganizaciones por fase')
ax.legend()
fig.tight_layout();fig.savefig(P/'graficos/o79_fase_transferencia_reloj.png',dpi=170);plt.close(fig)
fig,ax=plt.subplots(figsize=(8.4,4.8))
js=np.arange(0,9); ns=2.**js
for alpha in [0.9,1.,1.1,1.5]:
    val=1.5*ns**(3-3*alpha)
    ax.plot(js,val,marker='o',label=f'α={alpha}')
ax.set_yscale('log');ax.set_xlabel('Rama j (frecuencia n=2ʲ)')
ax.set_ylabel('Magnitud |transferencia a W_m| de una triada aislada')
ax.set_title('Dilución de las ramas vs. interacción triádica aislada')
ax.legend();ax.grid(True,alpha=.25)
fig.tight_layout();fig.savefig(P/'graficos/o79_dilucion_triada.png',dpi=170);plt.close(fig)
print('Graficas generadas')
