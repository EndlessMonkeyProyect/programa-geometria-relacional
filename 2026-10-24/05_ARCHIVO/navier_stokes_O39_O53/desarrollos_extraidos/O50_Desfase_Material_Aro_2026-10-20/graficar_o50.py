import json
from pathlib import Path
import matplotlib.pyplot as plt
p=Path(__file__).parent
r=json.loads((p/'resultados_o50.json').read_text())
fig,ax=plt.subplots(figsize=(8.2,4.8))
for e,label in [(0.0,'Perfil isócrono'),(0.2,'Perfil con cizallamiento radial')]:
 dat=[x for x in r['phase_drift'] if x['eps']==e]
 ax.plot([0]+[x['cycles'] for x in dat],[0]+[x['phase_difference_cycles'] for x in dat],marker='o',lw=2,label=label)
ax.set_xlabel('Vueltas del reloj de referencia')
ax.set_ylabel('Desfase entre capas (vueltas)')
ax.set_xticks([0,1,2,3]);ax.grid(alpha=.25)
ax.set_title('O50 · Frontera cerrada ≠ sincronización de capas')
ax.legend(loc='upper left');fig.tight_layout()
fig.savefig(p/'graficos_o50.png',dpi=170)
print('Plot ready')
