#!/usr/bin/env python3
import json, pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((BASE/'resultados/verificacion.json').read_text(encoding='utf8'))
r=data['lambda_records']; lam=[x['lambda_multiplier'] for x in r]; tim=[x['physical_interval'] for x in r]
fig,ax=plt.subplots(figsize=(8.4,4.8))
ax.loglog(lam,tim,'o-',label='Duración física de un certificado')
ax.set_xlabel('Multiplicador espacial λ')
ax.set_ylabel('Intervalo físico δ/λ²')
ax.set_title('O85 · Cada escala comprime el intervalo certificado')
ax.grid(alpha=.25,which='both'); ax.legend(); fig.tight_layout()
fig.savefig(BASE/'graficos/o85_escala_vs_tiempo.png',dpi=170)
plt.close(fig)

fig,ax=plt.subplots(figsize=(8.4,4.8))
ax.plot(lam,[x['M0_heat'] for x in r], 'o-',label='Referencia inicial: calor')
ax.plot(lam,[x['M1_updated_upper'] for x in r], 's-',label='Referencia actualizada: primera interacción')
ax.axhline(.5,ls='--',label='Umbral 0,5')
ax.set_xscale('log',base=2); ax.set_ylim(0,.65)
ax.set_xlabel('Multiplicador espacial λ')
ax.set_ylabel('Presupuesto crítico adimensional')
ax.set_title('O85 · Invariancia exacta del certificado por escala')
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
fig.savefig(BASE/'graficos/o85_certificado_invariante.png',dpi=170)
plt.close(fig)

s=data['abstract_stack']
fig,ax=plt.subplots(figsize=(8.4,4.8))
ax.plot([x['number_of_blocks'] for x in s],[x['lower_grad_cost'] for x in s],'o-',label='Costo gradiente, cota inferior de plantillas')
ax2=ax.twinx()
ax2.plot([x['number_of_blocks'] for x in s],[x['combined_physical_time'] for x in s],'s--',label='Tiempo físico total de las plantillas')
ax.set_xlabel('Cantidad de bloques abstractos')
ax.set_ylabel('Suma inferior de ∫Q(U)')
ax2.set_ylabel('Tiempo total')
ax.set_title('O85 · No implica una solución de Navier–Stokes ensamblada')
ax.grid(alpha=.25)
fig.tight_layout();fig.savefig(BASE/'graficos/o85_plantillas_no_solucion.png',dpi=170)
plt.close(fig)
print('Graficos O85 generados')
