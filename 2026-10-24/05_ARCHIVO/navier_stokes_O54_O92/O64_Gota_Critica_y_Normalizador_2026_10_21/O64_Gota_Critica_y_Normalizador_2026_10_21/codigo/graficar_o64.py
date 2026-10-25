#!/usr/bin/env python3
"""Graficación de relaciones analíticas, no simulación de dos fases."""
import sys, pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from verificar_o64 import d_hinze, torus_curvatures, SIGMA, NU
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=pathlib.Path(__file__).resolve().parents[1]
eps=np.geomspace(.001,10,160)
dh=np.array([d_hinze(e) for e in eps])
eta=(NU**3/eps)**.25
plt.figure(figsize=(8,5)); plt.loglog(eps,1000*dh,label='Diámetro de Hinze (mm)');plt.loglog(eps,1000*eta,label='Longitud de Kolmogorov (mm)',ls='--');plt.xlabel('Disipación ε (m²/s³)');plt.ylabel('Longitud (mm)');plt.title('O64: escalas críticas contextuales (ejemplo ilustrativo)');plt.legend();plt.grid(True,which='both',alpha=.2);plt.tight_layout();plt.savefig(ROOT/'graficos'/'o64_escalas_hinze_kolmogorov.png',dpi=165);plt.close()
theta=np.linspace(0,2*np.pi,241)
k=np.array([torus_curvatures(1,.35,float(t)) for t in theta]);
plt.figure(figsize=(8,5));plt.plot(theta,k[:,0],label='Curvatura meridiana 1/r');plt.plot(theta,k[:,1],label='Curvatura toroidal cosθ/(R+r cosθ)');plt.plot(theta,k.sum(axis=1),label='Suma de curvaturas');plt.xlabel('Ángulo meridiano θ (rad)');plt.ylabel('Curvatura (unidades inversas)');plt.title('O64: dos curvaturas, mismo toroide (R=1, r=0.35)');plt.legend();plt.grid(True,alpha=.2);plt.tight_layout();plt.savefig(ROOT/'graficos'/'o64_dos_curvaturas_toroidales.png',dpi=165);plt.close()
print('Graficas O64 creadas')
