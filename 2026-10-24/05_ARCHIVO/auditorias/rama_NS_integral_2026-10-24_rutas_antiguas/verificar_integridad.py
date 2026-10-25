from pathlib import Path
import csv,hashlib,sys
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'07_MAPAS_Y_AUDITORIA/INVENTARIO_ARCHIVOS.csv').open(encoding='utf-8')))
errors=[]
for a in rows:
 f=root/a['ruta']
 if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=a['sha256']:errors.append(a['ruta'])
print(f'Integridad: {len(rows)-len(errors)}/{len(rows)} archivos registrados; errores={len(errors)}')
for e in errors[:20]:print('ERROR',e)
sys.exit(bool(errors))
