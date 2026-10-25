#!/usr/bin/env python3
"""Sensibilidad observacional del laboratorio v4 al mover lateralmente una cámara."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from identidad_mirrors import C1,S1,S2,sensor,appearances,fit_spots

BASELINES=np.array([0,.01,.02,.025,.03,.035,.04,.05,.06,.08,.10,.15])
SEEDS=list(range(31,41))

def main():
    rows=[]
    for b in BASELINES:
        c=C1+np.array([0,b,0])
        n_detected=0
        for seed in SEEDS:
            im=sensor(c,[S1,S2],seed=seed)
            n_detected+=(fit_spots(im)['n_spots']==2)
        img=appearances(c,[S1,S2])
        d=float(np.linalg.norm([img[0][k]-img[1][k] for k in ('x','y')]))
        rows.append({'desplazamiento_m':float(b),'separacion_sensor_px':d,'dos_detectadas_en_10_ensayos':n_detected})
    out=Path(__file__).resolve().parent
    (out/'estudio_umbral.json').write_text(json.dumps({'estudio':'repeticiones con 10 semillas de ruido, sin incertidumbre geométrica','ensayos':rows},indent=2,ensure_ascii=False),encoding='utf8')
    fig,ax=plt.subplots(figsize=(8.5,4.6),layout='constrained')
    ax.plot([r['desplazamiento_m']*100 for r in rows],[r['dos_detectadas_en_10_ensayos'] for r in rows],'-o')
    ax.set(xlabel='Desplazamiento lateral de la cámara (cm)',ylabel='Ensayos que identificaron 2 manchas / 10',title='Resolución depende del marco y del ruido',ylim=(-.5,10.5))
    ax.grid(alpha=.22)
    fig.savefig(out/'figura_umbral.png',dpi=160);plt.close(fig)
    print(json.dumps(rows,ensure_ascii=False))

if __name__=='__main__':main()
