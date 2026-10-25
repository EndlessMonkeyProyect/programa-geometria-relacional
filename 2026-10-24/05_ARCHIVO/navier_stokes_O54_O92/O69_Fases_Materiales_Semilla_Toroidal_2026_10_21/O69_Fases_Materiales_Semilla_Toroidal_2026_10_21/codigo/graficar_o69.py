#!/usr/bin/env python3
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader(open(B/'resultados'/'fases_O53_serie_larga.csv')))
fig,ax=plt.subplots(figsize=(9,5))
for n,eps in [(40,0.0),(40,.14),(48,0.0),(48,.14)]:
    d=[r for r in rows if int(r['N'])==n and float(r['epsilon'])==eps]
    t=np.array([float(r['t']) for r in d]);f=np.array([float(r['psi_3_4_turns']) for r in d])
    ax.plot(t,f,label=f'N={n}, perturbacion={eps:g}',linewidth=1.7,linestyle='-' if n==40 else '--')
ax.axhline(0,linewidth=.75,alpha=.65)
ax.set(xlabel='Tiempo adimensional',ylabel='Deriva de la fase 3θ₁ − 4θ₂ (vueltas)',title='O69: la coincidencia 3:4 no permanece congelada')
ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(B/'graficos'/'o69_deriva_semilla_3_4.png',dpi=165);plt.close(fig)

rows=list(csv.DictReader(open(B/'resultados'/'velocidades_angulares_desde_campo_NS.csv')))
fig,ax=plt.subplots(figsize=(9,5))
for n,eps in [(32,0.),(32,.14),(40,0.),(40,.14)]:
    d=sorted([r for r in rows if int(r['N'])==n and float(r['epsilon'])==eps and float(r['depth'])==.12], key=lambda r:int(r['azimuth_degrees']))
    xx=[int(r['azimuth_degrees']) for r in d]; yy=[float(r['azimuthal_rate']) for r in d]
    ax.plot(xx,yy,'-o',label=f'N={n}, perturbacion={eps:g}',linestyle='-' if n==32 else '--')
ax.axhline(0,linewidth=.75,alpha=.65)
ax.set(xlabel='Azimut inicial de marca (grados)',ylabel='Velocidad angular azimutal (rad/unidad de tiempo)',title='O69: el segundo giro material depende de la perturbación')
ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(B/'graficos'/'o69_giro_azimutal_del_campo.png',dpi=165);plt.close(fig)
print('Gráficas generadas')
