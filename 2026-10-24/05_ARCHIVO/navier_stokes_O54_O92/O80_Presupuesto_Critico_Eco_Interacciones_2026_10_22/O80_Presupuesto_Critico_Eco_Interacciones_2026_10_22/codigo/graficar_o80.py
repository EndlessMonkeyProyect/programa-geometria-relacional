#!/usr/bin/env python3
import csv, json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'resultados'/'dyadic_dilucion.csv').open()))
fig,ax=plt.subplots(figsize=(8.8,4.9))
for alpha in [0.5,1,1.5,3.5]:
    subset=[r for r in rows if float(r['alpha'])==alpha]
    ax.plot([int(r['branches']) for r in subset],[float(r['Ymean']) for r in subset],marker='o',label=f'α={alpha}')
ax.set_yscale('log');ax.set_xlabel('Cantidad de ramas diádicas');ax.set_ylabel('Vorticidad cuadrática media (log)')
ax.set_title('O80 · Amplitud diluida no siempre controla el gradiente')
ax.legend(ncol=2); ax.grid(True,alpha=.25)
fig.tight_layout();fig.savefig(ROOT/'graficos'/'o80_dilucion_gradientes.png',dpi=165);plt.close(fig)

fig,ax=plt.subplots(figsize=(8.8,4.9))
for alpha in [.5,1.,1.5,3.5]:
    subset=[r for r in rows if float(r['alpha'])==alpha]
    ax.plot([int(r['branches']) for r in subset],[float(r['R']) for r in subset],marker='o',label=f'α={alpha}')
ax.set_xlabel('Cantidad de ramas diádicas');ax.set_ylabel('R = Σ |ûₖ|/|k|')
ax.set_title('O80 · Convergencia del presupuesto crítico en las ramas')
ax.legend(ncol=2);ax.grid(True,alpha=.25)
fig.tight_layout();fig.savefig(ROOT/'graficos'/'o80_presupuesto_critico.png',dpi=165);plt.close(fig)
print('2 figuras generadas')
