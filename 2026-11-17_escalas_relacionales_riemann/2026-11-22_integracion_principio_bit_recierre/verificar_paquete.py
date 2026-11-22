#!/usr/bin/env python3
"""Verificador autocontenido: integridad y controles finitos exactos.
No es una prueba de la hipotesis de Riemann.
"""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import hashlib, zipfile, sys
ROOT=Path(__file__).resolve().parent

def io_path(p):
 if sys.platform=='win32':
  return Path('\\\\?\\'+str(p))
 return p

def sha(p):
 h=hashlib.sha256()
 with io_path(p).open('rb') as f:
  for block in iter(lambda:f.read(1024*1024), b''):h.update(block)
 return h.hexdigest()

def mu_sieve(N):
 mu=[1]*(N+1); mu[0]=0
 for p in range(2,N+1):
  if all(p%k for k in range(2,isqrt(p)+1)):
   for n in range(p,N+1,p):mu[n]*=-1
   pp=p*p
   for n in range(pp,N+1,pp):mu[n]=0
 return mu

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def c(q,m):return (2*m)//q-2*(m//q)

def pruebas():
 m=mu_sieve(8192)
 ntests=0
 for N in [1,2,3,4,8,16,32,64,128,256,512,1024]:
  for n in range(N+1,2*N+1):
   D=sum(m[d] for d in range(1,n+1) if n%d==0 and d<=N)
   E=sum(m[d] for d in range(1,n+1) if n%d==0 and d<=2*N)
   assert D==-m[n] and E==0
   ntests+=1
 for X in range(1,2049):
  total=sum(m[1:X+1])
  for p in (2,3,5,7,11):
   boundary=sum(m[n] for n in range(X//p+1,X+1) if n%p)
   assert boundary==total,(X,p,boundary,total)
   ntests+=1
 for k in range(1,400):
  assert (2**(2*k)-1)==(2**k-1)*(2**k+1)
  ntests+=1
 for n in range(1,1000):
  for a in range(1,13):
   assert c(2**(a+1),2*n)==c(2**a,n)
   assert c(2,2*n)==0
   ntests+=1
 # Recuperacion de Delta^2 T, separando coeficientes racionales por log p.
 # T(k)=sum_{p^a<=k} log(p) (k-p^a)/p^a
 def terms(k):
  coef={}
  for p in range(2,k+1):
   if not prime(p):continue
   q=p
   while q<=k:
    coef[p]=coef.get(p,Fraction(0))+Fraction(k-q,q)
    q*=p
  return coef
 vals=[terms(k) for k in range(72)]
 for n in range(2,70):
  primepow={}
  for p in range(2,n+1):
   if prime(p):
    q=p
    while q<n:q*=p
    if q==n:primepow[p]=Fraction(1,n)
  got={p:vals[n+1].get(p,0)-2*vals[n].get(p,0)+vals[n-1].get(p,0)
       for p in set(vals[n+1])|set(vals[n])|set(vals[n-1])}
  assert {p:v for p,v in got.items() if v}==primepow,(n,got,primepow)
  ntests+=1
 return ntests

def main():
 manifest=ROOT/'MANIFIESTO_SHA256.txt'
 assert manifest.exists(), 'Missing manifest'
 count=0
 for row in manifest.read_text(encoding='utf-8').splitlines():
  if not row or row.startswith('#'):continue
  h,rel=row.split('  ',1)
  assert not Path(rel).is_absolute() and '..' not in Path(rel).parts, f'Unsafe: {rel}'
  p=ROOT/rel
  assert io_path(p).is_file(), f'Missing: {rel}'
  assert sha(p)==h, f'Mismatch: {rel}'
  count+=1
 assert not (ROOT/'SOPORTES'/'FUENTES_CONCEPTUALES'/'version_mejorada_mersenne_orientacional.tex').exists(), 'Excluded source present'
 zips=list((ROOT/'SOPORTES'/'PAQUETES_HISTORICOS').glob('*.zip'))
 assert len(zips)==16, 'Expected 16 historical packages'
 for z in zips:
  with zipfile.ZipFile(io_path(z)) as f:assert f.testzip() is None, f'Corrupt: {z.name}'
 n=pruebas()
 print('OK integridad archivos:',count)
 print('OK ZIP historicos:',len(zips))
 print('OK controles aritmeticos exactos:',n)
 print('Alcance: verificaciones finitas; no demuestra RH/GRH.')

if __name__=='__main__':
 try:main()
 except Exception as e:
  print('ERROR:',str(e));sys.exit(1)
