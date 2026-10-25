#!/usr/bin/env python3
"""Control O47-B: iguala E,J, energía cinética, bispectro y N=60; J' es distinto.
Momento cinético axial = sum K_k^2/k^2, nulo adicional al esquema O47-A.
"""
import json, math
from pathlib import Path
import verificar_O47 as o
base={k:.25 for k in (2,3,4,5)}
vector={2:-48/125,3:243/125,4:-64/25,5:1}
eps=.03
caseA={k:.5 for k in base}
caseB={k:math.sqrt(base[k]+eps*vector[k]) for k in base}

def moment(c,p):return sum(k**p*a*a for k,a in c.items())
def check(a,b,tol=1e-8):assert abs(a-b)<tol,(a,b)
for p in (0,2,-2):check(moment(caseA,p),moment(caseB,p),1e-12)
d4=moment(caseB,4)-moment(caseA,4)
check(d4,3.6288,1e-10)
result={'module':'O47 control_B energia cinematica matched','bands':list(base.keys()),'N_lcm':60,'caseA':caseA,'caseB':caseB,'moments':{'sumK2':moment(caseA,0),'sumk2K2':moment(caseA,2),'sumK2_over_k2':moment(caseA,-2),'delta_sumk4K2':d4},'nu':o.nu,'T':.12,'dt':.004,'simulations':{}}
for n in (32,48):
 a=o.simulate(n,caseA,.004,.12);b=o.simulate(n,caseB,.004,.12)
 a0=a['readings'][0];b0=b['readings'][0]
 for key in ('E','J','ell','kinetic','P','beta_real','beta_imag','triad_phase','dE_from_PDE'):
  check(a0[key],b0[key],1e-8)
 check(b0['dJ_from_PDE']-a0['dJ_from_PDE'],-o.nu*d4,1e-8)
 assert abs(b['readings'][-1]['ell']-a['readings'][-1]['ell'])>1e-6
 result['simulations'][str(n)]={'A':a,'B':b,'Jprime_diff':b0['dJ_from_PDE']-a0['dJ_from_PDE'], 'end_ell_diff':b['readings'][-1]['ell']-a['readings'][-1]['ell'],'end_clock_diff':b['readings'][-1]['clock']-a['readings'][-1]['clock'],'end_E_diff':b['readings'][-1]['E']-a['readings'][-1]['E']}
 print('N',n,'matched initial E J kinetic beta','dJ diff',result['simulations'][str(n)]['Jprime_diff'],'end ell diff',result['simulations'][str(n)]['end_ell_diff'],flush=True)
(O:=Path(__file__).parent).joinpath('O47_CONTROL_ENERGIA.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
