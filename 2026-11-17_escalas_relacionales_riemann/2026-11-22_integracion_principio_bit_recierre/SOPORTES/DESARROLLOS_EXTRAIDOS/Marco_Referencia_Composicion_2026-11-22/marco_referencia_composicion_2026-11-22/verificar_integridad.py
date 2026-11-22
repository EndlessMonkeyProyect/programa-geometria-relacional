#!/usr/bin/env python3
"""Verifica MANIFEST.sha256 con Python estándar, también en Windows."""
import hashlib
from pathlib import Path
base = Path(__file__).resolve().parent
entries = [line.split('  ', 1) for line in (base/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines() if line]
for digest, rel in entries:
    actual = hashlib.sha256((base/rel).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'ERROR: {rel}')
print(f'OK: {len(entries)}/{len(entries)} archivos coinciden con SHA-256.')
