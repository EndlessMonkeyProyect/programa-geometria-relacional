#!/usr/bin/env python3
"""Controles numéricos + manifiesto de integridad del suplemento O63."""
import csv,json,hashlib, math
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
summary=json.loads((BASE/'resultados/resumen.json').read_text())
checks={}
checks['contratos_dinamicos']=all(summary['checks'].values())
checks['doce_controles_calculo']=len(summary['checks'])==12
checks['reproduccion_o53']=summary['num_reproducciones']==24 and summary['max_error_reproduccion_O53']<1e-12
with (BASE/'resultados/resumen_distribucion.csv').open() as f:groups=list(csv.DictReader(f))
checks['seis_estados_azimutales']=len(groups)==6
checks['arm_2_control_vacio']=all(float(x['abs_harmonic_2'])<1e-10 for x in groups if float(x['eps'])==0)
checks['arm_2_perturbado_activado']=all(float(x['abs_harmonic_2'])>.1 for x in groups if float(x['eps'])>.1)
checks['arm_2_resoluciones_coinciden_aprox']=abs(next(float(x['abs_harmonic_2']) for x in groups if int(x['N'])==40 and float(x['eps'])>.1 and int(x['match'])==0)-next(float(x['abs_harmonic_2']) for x in groups if int(x['N'])==48 and float(x['eps'])>.1 and int(x['match'])==0))<.02
with (BASE/'resultados/desfases_predichos_y_calculados.csv').open() as f:prediction=list(csv.DictReader(f))
checks['pronosticos_no_ajustados']=len(prediction)==72
checks['derivada_cero_al_inicio']=all(abs(float(x['predicted_S']))<1e-14 for x in prediction if float(x['t'])==0)
checks['se_observa_error_tiempo_largo']=any(abs(float(x['error']))>.03 for x in prediction if abs(float(x['t'])-.08)<1e-8)
checks['control_evolucion_rotada']=summary['control_temporal_rotacion'][0]['max_difference']<1e-12
checks['fuentes_originales_presentes']=(BASE/'fuentes/O53_ORIGINAL_SIN_MODIFICAR.zip').exists() and (BASE/'fuentes/ejecutar_o62_ORIGINAL.py').exists()
checks['graficos_calculados']=all((BASE/'graficos'/name).stat().st_size>10000 for name in ('o63_prediccion_corta_vs_evolucion.png','o63_ritmos_alrededor_del_anillo.png'))
manifest_path=BASE/'MANIFEST_SHA256.json'
if manifest_path.exists():
    manifest=json.loads(manifest_path.read_text())
    checks['integridad_archivos']=all((BASE/p).exists() and hashlib.sha256((BASE/p).read_bytes()).hexdigest()==v for p,v in manifest['files'].items())
    checks['sin_entradas_omitidas']=set(str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.json' and '__pycache__' not in str(p))==set(manifest['files'])
else:checks['integridad_archivos']=False;checks['sin_entradas_omitidas']=False
print(json.dumps({'comprobaciones':checks,'aprobadas':sum(checks.values()),'total':len(checks)},ensure_ascii=False,indent=2))
assert all(checks.values())
