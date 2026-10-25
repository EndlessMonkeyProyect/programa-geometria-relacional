#!/usr/bin/env python3
"""Comprueba que el suplemento no ha sufrido cambios desde su empaquetado."""
from pathlib import Path
import hashlib, json
base=Path(__file__).resolve().parent
manifest=json.loads((base/'MANIFEST_SHA256.json').read_text())
for name, expected in manifest['archivos'].items():
    actual=hashlib.sha256((base/name).read_bytes()).hexdigest()
    if actual!=expected:
        raise SystemExit(f'FALLÓ {name}: {actual} != {expected}')
print(f'PASS | {len(manifest["archivos"])} huellas SHA-256 verificadas | O61')
