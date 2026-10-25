#!/usr/bin/env python3
"""Renderizaciones de datos calculados, sin imágenes sintéticas."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parents[1]
a=pd.read_csv(BASE/'resultados/distribucion_azimutal.csv')
fig,ax=plt.subplots(figsize=(8.3,4.6))
for eps,match,label in [(0,0,'Control O53'),(.14,0,'Perturbación 14 %'),(.14,1,'Perturbación 14 %, energía igualada')]:
    d=a[(a.N==48)&(a.eps==eps)&(a.match==match)].sort_values('azimuth_degrees')
    ax.plot(d.azimuth_degrees,d.slope,marker='o',markersize=2.5,label=label)
ax.set(xlabel='Ángulo azimutal de la marca (grados)',ylabel='Desfase inicial (vueltas / tiempo)',
       title='O63: ritmos locales de fase sobre el mismo anillo')
ax.grid(alpha=.3);ax.legend(fontsize=8);fig.tight_layout();fig.savefig(BASE/'graficos/o63_ritmos_alrededor_del_anillo.png',dpi=160);plt.close(fig)

a=pd.read_csv(BASE/'resultados/desfases_predichos_y_calculados.csv')
fig,ax=plt.subplots(figsize=(8.3,4.6))
for eps,match,label in [(0,0,'Control'),(.14,0,'Perturbación'),(.14,1,'Igualando energía')]:
    d=a[(a.N==48)&(a.eps==eps)&(a.match==match)&(a.azimuth=='0')].sort_values('t')
    ax.plot(d.t,d.measured_S,marker='o',label=f'{label} — calculado')
    ax.plot(d.t,d.predicted_S,linestyle='--',label=f'{label} — Taylor inicial')
ax.set(xlabel='Tiempo',ylabel='Desfase externo (vueltas)',title='O63: la derivada inicial no determina el horizonte largo')
ax.grid(alpha=.3);ax.legend(fontsize=8,ncol=2);fig.tight_layout();fig.savefig(BASE/'graficos/o63_prediccion_corta_vs_evolucion.png',dpi=160);plt.close(fig)
print('Gráficas verificadas')
