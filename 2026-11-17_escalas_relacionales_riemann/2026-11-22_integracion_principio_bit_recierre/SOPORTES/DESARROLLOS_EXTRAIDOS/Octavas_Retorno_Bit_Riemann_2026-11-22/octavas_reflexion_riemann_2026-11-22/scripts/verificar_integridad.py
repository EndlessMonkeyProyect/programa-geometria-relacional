#!/usr/bin/env python3
"""Verifica el manifiesto SHA-256 del paquete local."""
import hashlib
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = root / 'MANIFEST.sha256'
checks=0
for line in manifest.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    expected, name = line.split('  ', 1)
    f=root/name
    got=hashlib.sha256(f.read_bytes()).hexdigest()
    assert got==expected, f'FAIL: {name}'
    checks+=1
print(f'OK: {checks}/{checks} archivos SHA256 verificados')
