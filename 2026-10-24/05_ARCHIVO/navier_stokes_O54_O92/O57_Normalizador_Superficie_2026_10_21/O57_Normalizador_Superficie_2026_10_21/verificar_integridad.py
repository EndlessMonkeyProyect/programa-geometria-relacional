#!/usr/bin/env python3
import json, hashlib
from pathlib import Path
r=Path(__file__).resolve().parent
m=json.loads((r/'MANIFEST_SHA256.json').read_text())
for entry in m['archivos']:
    f=r/entry['path']
    assert f.is_file(),entry['path']
    assert hashlib.sha256(f.read_bytes()).hexdigest()==entry['sha256'],entry['path']
print(f"OK: {len(m['archivos'])} archivos y huellas SHA256")
