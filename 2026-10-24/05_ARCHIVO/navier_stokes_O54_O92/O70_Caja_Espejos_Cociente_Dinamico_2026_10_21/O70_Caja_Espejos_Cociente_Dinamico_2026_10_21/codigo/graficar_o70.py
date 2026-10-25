from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((BASE/'resultados'/'series.csv').open()))
fig,ax=plt.subplots(figsize=(8,4.5))
for c in (0.,1.,2.):
    sub=sorted((r for r in rows if int(r['N'])==40 and float(r['c'])==c),key=lambda r: float(r['t']))
    ax.plot([float(r['t']) for r in sub],[float(r['difference_from_base_trajectory']) for r in sub],marker='o',label=f'Amplitud c={c:g}')
ax.set_xlabel('Tiempo adimensional')
ax.set_ylabel('Distancia entre referencias colectivas (norma RMS)')
ax.set_title('O70: misma referencia inicial; distintas evoluciones')
ax.legend(loc='upper left');ax.grid(alpha=.25)
fig.tight_layout();fig.savefig(BASE/'graficos'/'o70_misma_semilla_distinto_futuro.png',dpi=170)
plt.close(fig)

fig,ax=plt.subplots(figsize=(7,4.5))
for n in (32,40):
    sub=[r for r in rows if int(r['N'])==n and float(r['t'])==0.]
    xs=[float(r['c']) for r in sub];ys=[float(r['norm_defect']) for r in sub]
    ax.plot(xs,ys,marker='o',label=f'Malla N={n}')
ax.set_xlabel('Amplitud del sector no reconstruido')
ax.set_ylabel('Norma del defecto dinámico inicial')
ax.set_title('O70: efecto cuadrático de las relaciones no visibles')
ax.grid(alpha=.25);ax.legend();fig.tight_layout()
fig.savefig(BASE/'graficos'/'o70_defecto_cuadratico.png',dpi=170)
plt.close(fig)
print('Graficos O70 generados')
