#!/usr/bin/env python3
"""Genera evidencia visual adicional. Requiere matplotlib."""
import csv,math
from bisect import bisect_right
from pathlib import Path
from laboratorio import sieve,psi_ritz,h_term

HERE=Path(__file__).resolve().parent
N=1_000_000
GAMMA=.5772156649015328606
_,ps=sieve(N)
values=sorted(set(round(math.exp(math.log(1000)+(math.log(N)-math.log(1000))*i/129)) for i in range(130)))
rows=[]
for x in values:
    z=math.isqrt(x)
    subset=ps[:bisect_right(ps,z)]
    a=math.fsum(math.log(p)/(p-1) for p in subset)
    H=math.fsum(h_term(x,p) for p in subset)
    T=psi_ritz(x,ps)
    R=psi_ritz(x,ps,z)
    G=T-x*(math.log(x)-1-GAMMA)
    D=R-x*(math.log(x)-1-GAMMA-a)
    assert abs(D-H-G)<3e-7
    rows.append(dict(x=x,G_sqrt=G/math.sqrt(x),D_sqrt=D/math.sqrt(x),H_sqrt=H/math.sqrt(x)))
with (HERE/'serie_normalizada.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print('Muestreo:',len(rows),'puntos. Rango abs(G/sqrt)=',max(abs(r['G_sqrt']) for r in rows))
try:
    import matplotlib.pyplot as plt
    fig, ax=plt.subplots(figsize=(10,5.5))
    for key, label in [('G_sqrt','G(x) / raíz(x)'),('D_sqrt','D(x) / raíz(x)'),('H_sqrt','H(x) / raíz(x)')]:
        ax.plot([r['x'] for r in rows],[r[key] for r in rows],label=label,linewidth=1.6)
    ax.set_xscale('log')
    ax.set_xlabel('Escala x (logarítmica)')
    ax.set_ylabel('Magnitudes normalizadas por raíz(x)')
    ax.set_title('Separación exacta: G(x) = D(x) - H(x)')
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(HERE/'comparacion_escalas.png',dpi=170)
    plt.close(fig)
    print('Gráfico creado')
except ImportError:
    print('matplotlib no instalado; datos CSV guardados')
