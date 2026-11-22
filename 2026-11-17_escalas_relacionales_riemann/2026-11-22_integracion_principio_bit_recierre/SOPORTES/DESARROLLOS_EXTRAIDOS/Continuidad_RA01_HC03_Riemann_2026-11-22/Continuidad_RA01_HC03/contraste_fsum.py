"""Contraste independiente de puntos seleccionados: Python stdlib y math.fsum.
Se sirve de posiciones publicadas en el CSV del ensayo principal. No es aritmetica
por intervalos ni certificacion de desigualdades sobre numeros reales.
"""
import bisect,csv,json,math
from pathlib import Path
base=Path(__file__).resolve().parent
rows=list(csv.DictReader((base/'bloques_hc03_2_22.csv').open(encoding='utf-8')))
N=1<<22
s=bytearray(b'\x01')*N
s[:2]=b'\x00\x00'
for p in range(2,math.isqrt(N-1)+1):
 if s[p]:s[p*p:N:p]=b'\x00'*(((N-1-p*p)//p)+1)
pr=[i for i in range(2,N) if s[i]]
powers=[]
for p in pr:
 q=p*p
 if q>=N:break
 while q<N:
  powers.append((q,math.log(p)))
  q*=p
powers.sort()
keys=[q for q,w in powers]
checks=[]
for j in [10,15,20,21]:
 r=rows[j-1];L=int(r['desde'])
 for m in [int(r['posicion_max_total']),int(r['posicion_max_primos']),int(r['hasta_inclusive'])]:
  low=bisect.bisect_left(pr,L);hi=bisect.bisect_right(pr,m)
  plog=math.fsum(math.log(p) for p in pr[low:hi])
  hlow=bisect.bisect_left(keys,L);hhi=bisect.bisect_right(keys,m)
  hlog=math.fsum(w for _,w in powers[hlow:hhi])
  pts=plog+hlog-(m-L+1)
  checks.append({'j':j,'m':m,'nuevos':plog-(m-L+1),'heredados':hlog,'total':pts})
(base/'contraste_fsum.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('cantidad controles independientes:',len(checks))
for r in checks:print(r['j'],r['m'],round(r['nuevos'],9),round(r['heredados'],9),round(r['total'],9))
