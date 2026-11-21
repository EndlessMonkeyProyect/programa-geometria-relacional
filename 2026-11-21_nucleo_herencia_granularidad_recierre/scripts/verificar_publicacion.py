#!/usr/bin/env python3
"""Chequea consistencia editorial del paquete 3.5 (no prueba RH)."""
from pathlib import Path
import re
import hashlib
root=Path(__file__).resolve().parents[1]
paths=[p for p in root.rglob('*.md') if 'fuentes' not in p.relative_to(root).parts]
for path in paths:
    s=path.read_text(encoding='utf-8')
    assert '\\\\(' not in s and '\\\\[' not in s, path
    assert '\\(' not in s and '\\[' not in s, path
    assert not re.search(r'0[,.]44\s*\\le',s), path
assert not (root/'RESULTADOS_VERIFICACION.txt').exists()
ra=(root/'anexos'/'RA-01_recuperacion_acumulada'/'documentos'/'PROPOSICION_RECUPERACION_ACUMULADA_2026-11-21.md').read_text(encoding='utf-8')
lab=(root/'laboratorios'/'2026-11-21_RA01_semilla_mobius'/'documentos'/'LAB_RA01_SEMILLA_MOBIUS_2026-11-21.md').read_text(encoding='utf-8')
assert '0{,}437' in ra and '0{,}437' in lab
assert '$$' in lab and '$$' in ra
assert 'supera' in ra and 'iguala' in ra
assert 'Burnol' in lab and 'D(\\lambda)' in lab
for ref in ('/pull/9','/pull/11'):
    assert ref in ra and ref in (root/'integracion'/'INSTRUCCIONES_ADMIN.md').read_text(encoding='utf-8')
# Revisión de A2, firma y cierre de delimitadores en el laboratorio armónico.
armonico = root/'laboratorios'/'2026-11-21_armonicos_granularidad'
texto = (armonico/'documentos'/'LAB_ARMONICOS_GRANULARIDAD_Y_RECIERRE_2026-11-21.md').read_text(encoding='utf-8')
assert re.search(r'\$\$\s*a\^2\+b\^2\+1=K\^2,.*?\\tag\{A2\}\s*\$\$', texto, re.S), 'A2: delimitadores matemáticos incorrectos'
assert texto.count('$$') % 2 == 0, 'Bloques matemáticos sin pareja en laboratorio armónico'
assert '**Le Matt Ansatz Di Ego**' in texto, 'Falta firma pública en laboratorio armónico'

# Manifiesto interno con comprobación multiplataforma (sin depender de sha256sum).
lineas = (armonico/'MANIFIESTO_SHA256.txt').read_text(encoding='utf-8').splitlines()
for linea in lineas:
    esperado, relativo = linea.split('  ', 1)
    archivo = armonico/relativo
    assert archivo.is_file() and archivo.resolve().is_relative_to(armonico.resolve()), archivo
    actual = hashlib.sha256(archivo.read_bytes()).hexdigest()
    assert actual == esperado, f'Hash del laboratorio distinto: {relativo}'
print(f'LABORATORIO ARMÓNICO: MANIFIESTO {len(lineas)}/{len(lineas)} OK')
print('RESULTADO: CONTROL EDITORIAL 3.5 SUPERADO; fuentes históricas intactas')
