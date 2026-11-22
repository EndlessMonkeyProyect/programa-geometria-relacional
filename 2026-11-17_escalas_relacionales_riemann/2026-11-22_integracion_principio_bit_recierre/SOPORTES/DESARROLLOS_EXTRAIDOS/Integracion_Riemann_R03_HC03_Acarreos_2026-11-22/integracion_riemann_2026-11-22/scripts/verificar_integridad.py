#!/usr/bin/env python3
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent.parent
entries=(root/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines()
for line in entries:
    expected,name=line.split('  ',1)
    p=root/name
    assert p.is_file(),f'MISSING: {name}'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,f'MISMATCH: {name}'
print(f'OK: {len(entries)} / {len(entries)} archivos verificados SHA256')
