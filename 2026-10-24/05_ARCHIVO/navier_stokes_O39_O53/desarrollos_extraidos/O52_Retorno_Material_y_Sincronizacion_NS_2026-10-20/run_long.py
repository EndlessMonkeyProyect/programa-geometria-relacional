#!/usr/bin/env python3
"""O52 — continuación O51, reproduce sin nuevos parámetros ajustados."""
import os,sys,json,time
sys.path.insert(0,os.path.dirname(__file__))
from o51_ns_ring import run
base='/mnt/data/O52_Retorno_Material_y_Sincronizacion_NS_2026-10-20'
for N in (40,48):
    start=time.time()
    j=run(N=N,T=2.4,dt=.004,nu=.025,Gamma=6.,R=1.,a=.35,sampler_every=5)
    with open(f'{base}/NS{N}_T2p4.json','w') as f:json.dump(j,f)
    print('DONE',N,'elapsed',round(time.time()-start,2),'maxturn',j['max_abs_phase_turns'],'dz',j['ring_center_displacement'],'phaseext',j['samples'][-1]['phase_difference_outer_layers_turns'],flush=True)
