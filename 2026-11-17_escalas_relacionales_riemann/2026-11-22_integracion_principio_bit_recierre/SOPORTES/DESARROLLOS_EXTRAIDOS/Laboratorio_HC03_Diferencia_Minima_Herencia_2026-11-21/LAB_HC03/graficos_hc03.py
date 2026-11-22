#!/usr/bin/env python3
"""Gráficos de las mediciones de HC-03 (matplotlib opcional)."""
import csv
import math
from pathlib import Path
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
with (root/'bloques_diadicos.csv').open(encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
js=[int(r['j']) for r in rows]
ratios=[float(r['razon_certificado']) for r in rows]
fig,ax=plt.subplots(figsize=(9,4.8),layout='constrained')
ax.plot(js,ratios,'o-',linewidth=1.6)
ax.set(xlabel='Nivel de escala diádico j (n ~ 2^j)',ylabel='Máximo observado / [2^(j/2)(j+1)^2]',
       title='HC-03 · Certificado por ventanas — observación finita')
ax.grid(True,alpha=.25)
fig.savefig(root/'certificado_bloques.png',dpi=170)
plt.close(fig)
with (root/'control_pesos.csv').open(encoding='utf-8') as f:
    r=list(csv.DictReader(f))
xs=[int(a['N']) for a in r]
orig=[float(a['discrepancy_original'])/math.sqrt(int(a['N'])) for a in r]
mod=[float(a['discrepancia_pesos_ajustados'])/math.sqrt(int(a['N'])) for a in r]
fig,ax=plt.subplots(figsize=(9,4.8),layout='constrained')
ax.plot(xs,orig,'o-',label='Pesos originales Λ(p^k) = log p')
ax.plot(xs,mod,'s-',label='Control: pesos ajustados Λ*(p^k) = log p + 1')
ax.set(xscale='log',xlabel='Escala N',ylabel='(Acumulado − referencia) / √N',
       title='HC-03 · Mismo soporte de potencias primas, distinto peso')
ax.legend()
ax.grid(True,alpha=.25)
fig.savefig(root/'control_genealogia.png',dpi=170)
plt.close(fig)
