#!/usr/bin/env python3
"""Verifica SHA256SUMS.txt, salida ASCII para terminales Windows antiguas."""
from pathlib import Path
import hashlib
import sys

root=Path(__file__).resolve().parent
manifest=root/'SHA256SUMS.txt'
if not manifest.exists():
    print('ERROR: missing SHA256SUMS.txt')
    raise SystemExit(2)
checks=0
issues=0
for row in manifest.read_text(encoding='utf-8').splitlines():
    if not row.strip() or row.startswith('#'):
        continue
    try:
        expected, rel=row.split('  ',1)
        p=root/rel
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        ok=expected==actual
    except Exception:
        ok=False
    checks+=1
    issues+=not ok
    print(('OK: ' if ok else 'FAIL: ')+rel)
print('RESULT: '+str(checks-issues)+'/'+str(checks)+' passed')
raise SystemExit(1 if issues else 0)
