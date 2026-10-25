"""Controles de robustez del barrido. El ranking depende de los supuestos."""
import json
from dataclasses import replace
from pathlib import Path
import numpy as np
from scipy.signal import find_peaks
from cuartos_acoplados import Config, coincidence_profile
P=Path(__file__).resolve().parent
out=[]
for R in [0.02,0.08,0.5,0.75,0.95,1.0]:
  for sigma in [0.05,0.12,0.30]:
    for N in [5,8,12]:
      c=Config(R=R,pulse_sigma_ns=sigma,max_returns=N)
      xx=np.arange(.35,2.0001,.001)
      yy=coincidence_profile(xx,c)
      idx,_=find_peaks(yy,distance=15)
      ranked=sorted([i for i in idx if xx[i]<1.95],key=lambda i:-yy[i])
      best=float(xx[ranked[0]]) if ranked else None
      out.append(dict(R=R,sigma_temporal_ns=sigma,max_returns=N,
                      best_nontrivial_depth_m=best,
                      highest_score=float(yy[ranked[0]]) if ranked else 0.0,
                      glass_transmission=1-R))
(P/'robustez_v5.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
summary={}
for R in [0.02,.08,.5,.75,.95,1.0]:
  a=[x for x in out if x['R']==R]
  summary[R]=(len(a),sum(x['best_nontrivial_depth_m'] is not None and abs(x['best_nontrivial_depth_m']-1)<.005 for x in a))
print(summary)
