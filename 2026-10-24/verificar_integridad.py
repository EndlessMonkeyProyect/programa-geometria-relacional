#!/usr/bin/env python3
"""Comprueba que cada archivo de esta carpeta coincide con MANIFIESTO_SHA256.txt.
Uso, desde esta carpeta:  python3 verificar_integridad.py
"""
import hashlib, sys
from pathlib import Path

raiz = Path(__file__).resolve().parent
manifiesto = raiz / 'MANIFIESTO_SHA256.txt'
esperado = {}
for linea in manifiesto.read_text(encoding='utf-8').splitlines():
    if linea.strip():
        h, ruta = linea.split('  ', 1)
        esperado[ruta] = h
errores, faltan = [], []
for ruta, h in esperado.items():
    f = raiz / ruta
    if not f.exists(): faltan.append(ruta)
    elif hashlib.sha256(f.read_bytes()).hexdigest() != h: errores.append(ruta)
presentes = {p.relative_to(raiz).as_posix() for p in raiz.rglob('*') if p.is_file()}
extra = sorted(presentes - set(esperado) - {'MANIFIESTO_SHA256.txt'})
print(f'Integridad: {len(esperado) - len(errores) - len(faltan)}/{len(esperado)} archivos correctos; '
      f'alterados={len(errores)}, faltantes={len(faltan)}, no registrados={len(extra)}')
for r in errores[:20]: print('ALTERADO', r)
for r in faltan[:20]: print('FALTA', r)
for r in extra[:20]: print('NO REGISTRADO', r)
sys.exit(bool(errores or faltan))
