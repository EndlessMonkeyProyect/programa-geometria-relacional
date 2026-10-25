"""Segunda auditoría: se incluyen cruces de vidrio en una red de dos cavidades.
Analiza firmas de recorridos sin atribuir automáticamente intensidades detectadas.
"""
import collections
import json
import math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from cuartos_acoplados import paths_for_coupled_rooms,round_trip_ns
ROOT=Path(__file__).resolve().parent

def analyze(L):
    paths=paths_for_coupled_rooms(LB=L,R=.5,depth=8)
    groups=collections.defaultdict(lambda:dict(signature_set=set(),histories=[]))
    for h in paths:
        g=groups[(round(h['time_ns'],7),h['side'])]
        g['signature_set'].add((h['path'].count('A'),h['path'].count('B')))
        g['histories'].append(h['path'])
    mixed=[]
    for (t,side),g in groups.items():
        if len(g['signature_set'])>1:
            mixed.append(dict(time_ns=t,side=side,signatures=sorted(g['signature_set']),
                              number_of_paths=len(g['histories'])))
    return dict(length_B_m=L,total_histories=len(paths),distinct_time_side_bins=len(groups),
                bins_with_distinct_length_signatures=len(mixed),
                examples=sorted(mixed,key=lambda r:(r['time_ns'],r['side']))[:12],
                parity_tied_to_side=all((h['side']=='A') == (h['reflection_parity']=='impar') for h in paths))

if __name__=='__main__':
    Ls=[('Iguales (1:1)',2.0),('Mitad (1:2)',1.0),('Dos tercios (2:3)',4/3),
        ('Tres cuartos (3:4)',1.5),('Raíz de 2',math.sqrt(2)),('Cerca (1,10 m)',1.1)]
    values=[]
    for name,L in Ls:
        d=analyze(L);d['caso']=name;values.append(d)
    (ROOT/'auditoria_rutas_v5.json').write_text(json.dumps(values,ensure_ascii=False,indent=2)+'\n')
    fig,ax=plt.subplots(figsize=(11,4.8))
    ax.bar([v['caso'] for v in values],[v['bins_with_distinct_length_signatures'] for v in values])
    ax.set_ylabel('Coincidencias entre rutas con distinta ocupación A/B')
    ax.set_title('Red acoplada: reorganización de caminos en longitudes conmensurables')
    ax.tick_params(axis='x',rotation=25)
    ax.grid(axis='y',alpha=.2)
    fig.tight_layout();fig.savefig(ROOT/'05_rutas_coupled.png',dpi=160);plt.close(fig)
    print([(x['caso'],x['bins_with_distinct_length_signatures']) for x in values])
