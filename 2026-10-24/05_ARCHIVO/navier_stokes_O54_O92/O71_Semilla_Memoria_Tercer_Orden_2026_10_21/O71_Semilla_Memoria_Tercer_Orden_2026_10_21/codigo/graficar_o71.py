#!/usr/bin/env python3
from pathlib import Path
import csv,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'resultados'/'evolucion.csv').open() as f: rows=list(csv.DictReader(f))
fig,ax=plt.subplots(figsize=(9,5.4))
for n in (32,40,48):
    r=[q for q in rows if int(q['N'])==n]
    t=[float(q['t']) for q in r]
    ax.plot(t,[float(q['distancia_comun']) for q in r],marker='o',label=f'Distancia calculada N={n}')
    ax.plot(t,[float(q['prediccion_orden2']) for q in r],linestyle='--',label=f'Predicción ½ Δa″ t², N={n}')
ax.set_xlabel('Tiempo adimensional')
ax.set_ylabel('Distancia RMS entre referencias colectivas')
ax.set_title('O71 — Misma referencia y misma tensión residual; futuros diferentes')
ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.tight_layout();fig.savefig(ROOT/'graficos'/'o71_misma_tau_segunda_derivada_distinta.png',dpi=165)
plt.close(fig)
with (ROOT/'resultados'/'resumen.json').open() as f: data=json.load(f)
fig,ax=plt.subplots(figsize=(7.8,4.9))
for item in data['experiments']:
    c=[q['c'] for q in item['cubic']]
    d=[q['second_derivative_distance'] for q in item['cubic']]
    ax.loglog(c,d,marker='o',label=f'Cálculo N={item["N"]}')
    ax.loglog(c,[d[1]*(x/c[1])**3 for x in c],linestyle='--',label=f'Ley cúbica N={item["N"]}')
ax.set_xlabel('Amplitud de la diferencia no visible')
ax.set_ylabel('Distancia entre aceleraciones de la referencia')
ax.set_title('O71 — Tercer orden en la relación no observada')
ax.grid(alpha=.22);ax.legend(fontsize=9)
fig.tight_layout();fig.savefig(ROOT/'graficos'/'o71_ley_cubica.png',dpi=165)
print('2 gráficas escritas')
