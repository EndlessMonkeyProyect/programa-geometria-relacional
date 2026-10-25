from pathlib import Path
import hashlib,json,sys
base=Path(__file__).resolve().parent
manifest=json.loads((base/'MANIFEST_SHA256.json').read_text())
for f,h in manifest['archivos'].items():
    actual=hashlib.sha256((base/f).read_bytes()).hexdigest()
    if actual != h:
        print('ERROR:',f,actual);sys.exit(1)
print('OK:',len(manifest['archivos']),'archivos verificados')
