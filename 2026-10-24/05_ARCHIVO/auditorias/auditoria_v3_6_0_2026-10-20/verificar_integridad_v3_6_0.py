from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
m=root/'23_auditoria_2026_10_20/MANIFEST_v3_6_0.json'
data=json.loads(m.read_text(encoding='utf8'))
expected={x['path']:x for x in data['files']}
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p!=m}
missing=sorted(expected.keys()-actual);extra=sorted(actual-expected.keys());errors=[]
for rel,rec in expected.items():
 p=root/rel
 if not p.is_file():continue
 raw=p.read_bytes()
 if len(raw)!=rec['bytes'] or hashlib.sha256(raw).hexdigest()!=rec['sha256']:errors.append(rel)
print(json.dumps({'edition':data['edition'],'files':len(expected),'missing':missing,'extra':extra,'hash_errors':errors,'passed':not(missing or extra or errors)},ensure_ascii=False,indent=2))
sys.exit(bool(missing or extra or errors))
