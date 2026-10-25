#!/usr/bin/env python3
"""Verify SHA256 of the O58 supplement; manifest excludes itself."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST_SHA256.json').read_text(encoding='utf-8'))
files=manifest['files']
errors=[]
for rel,sha in files.items():
    p=root/rel
    if not p.is_file():errors.append('falta '+rel);continue
    if hashlib.sha256(p.read_bytes()).hexdigest()!=sha:errors.append('digest diferente '+rel)
existing={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.json'}
extra=existing-set(files)
missing=set(files)-existing
errors.extend('no manifestado '+x for x in sorted(extra))
errors.extend('no existe '+x for x in sorted(missing))
print('PASS integridad:',len(files),'archivos' if not errors else 'FAIL integridad')
for e in errors: print('ERROR',e)
sys.exit(bool(errors))
