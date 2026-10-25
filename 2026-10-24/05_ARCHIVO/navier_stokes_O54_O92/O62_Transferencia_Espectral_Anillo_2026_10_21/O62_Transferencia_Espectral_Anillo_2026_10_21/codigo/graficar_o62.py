#!/usr/bin/env python3
import csv
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'resultados/transferencias_y_predicciones.csv').open()))
cases=[(0.,0,'Control O53'),(.14,0,'Perturbación 14 %'),(.14,1,'14 % · energía igualada')]
pre=[];obs=[]
for eps,match,label in cases:
 x=next(r for r in rows if int(r['N'])==48 and abs(float(r['epsilon'])-eps)<1e-10 and int(r['match_energy'])==match and abs(float(r['t'])-.08)<1e-9 and r['band']=='[2,4)')
 pre.append(1e6*float(x['predicted_nonlinear_change']))
 obs.append(1e6*float(x['observed_nonlinear_change']))
ind=np.arange(3)
fig,ax=plt.subplots(figsize=(10,5.4))
ax.bar(ind-.2,pre,width=.38,label='Pronóstico inicial (orden 2)')
ax.bar(ind+.2,obs,width=.38,label='Evolución NS-Galerkin')
ax.axhline(0,linewidth=.8)
ax.set_xticks(ind,[x[2] for x in cases]);ax.set_ylabel('E(NS) − E(Stokes), × 10⁶')
ax.set_title('O62 · Banda |k| ∈ [2,4), t = 0,08 · malla 48³')
ax.legend();fig.tight_layout();fig.savefig(root/'graficos/o62_prediccion_banda_2_4.png',dpi=190)
print(root/'graficos/o62_prediccion_banda_2_4.png')
