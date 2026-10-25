import json,time
from pathlib import Path
from o53_perturbed_ring import run
print('BEGIN energy-matched epsilon=.14',flush=True)
t=time.time();r=run(N=40,T=2.4,dt=.004,epsilon=.14,match_energy=True,sample_every=5)
Path('NS_N40_eps14_equienergia.json').write_text(json.dumps(r,indent=2,ensure_ascii=False))
print('END energy-matched',time.time()-t,json.dumps(r['stats']),flush=True)
