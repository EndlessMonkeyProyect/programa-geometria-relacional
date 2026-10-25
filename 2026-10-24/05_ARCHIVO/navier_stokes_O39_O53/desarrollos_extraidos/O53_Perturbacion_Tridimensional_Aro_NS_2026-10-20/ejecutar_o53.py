import json,sys,time
from pathlib import Path
from o53_perturbed_ring import run
cases=[(40,0.0),(40,0.07),(40,0.14),(48,0.0),(48,0.14)]
for N,e in cases:
    start=time.time()
    print('BEGIN',N,e,flush=True)
    r=run(N=N,T=2.4,dt=.004,epsilon=e,sample_every=5)
    out=f'NS_N{N}_eps{int(round(e*100)):02}.json'
    Path(out).write_text(json.dumps(r,ensure_ascii=False,indent=2))
    print('END',N,e, 'time',round(time.time()-start,2),'output',out,'stats',json.dumps(r['stats']),flush=True)
