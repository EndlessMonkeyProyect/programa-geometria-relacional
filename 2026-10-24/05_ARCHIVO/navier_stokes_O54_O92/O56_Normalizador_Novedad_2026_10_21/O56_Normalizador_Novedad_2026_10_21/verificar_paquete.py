#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST_SHA256.json').read_text())
errors=[]
for name,expected in manifest['sha256'].items():
    p=root/name
    if not p.exists(): errors.append(name+': no existe');continue
    found=sha256(p.read_bytes()).hexdigest()
    if found!=expected:errors.append(name+': huella diferente')
if errors:
    raise SystemExit('ERROR:\n'+'\n'.join(errors))
print('PASS manifiesto: %s archivos comprobados' % len(manifest['sha256']))
