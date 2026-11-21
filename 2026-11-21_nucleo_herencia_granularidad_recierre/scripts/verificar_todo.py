#!/usr/bin/env python3
"""Ejecuta todos los verificadores del paquete de publicación 3.5.

Los tres primeros usan solo la biblioteca estándar (aritmética exacta).
El laboratorio S–RA–01 requiere numpy; si no está instalado, se informa y se omite.
"""
import subprocess, sys, importlib.util
from pathlib import Path
root = Path(__file__).resolve().parents[1]
exactos = [
    root/'scripts'/'verificar_resultados.py',
    root/'laboratorios'/'2026-11-21_armonicos_granularidad'/'scripts'/'verificar_armonicos_y_granularidad.py',
    root/'scripts'/'verificar_ra01.py',
    root/'scripts'/'verificar_publicacion.py',
]
numerico = root/'laboratorios'/'2026-11-21_RA01_semilla_mobius'/'scripts'/'medir_semilla_mobius.py'
for program in exactos:
    print(f'\n=== {program.relative_to(root)} ===', flush=True)
    subprocess.run([sys.executable, str(program)], check=True, cwd=str(root))
print(f'\n=== {numerico.relative_to(root)} ===', flush=True)
if importlib.util.find_spec('numpy') is None:
    print('OMITIDO: el laboratorio S–RA–01 requiere numpy (pip install numpy).')
    print('\nRESULTADO: CONTROLES EXACTOS 3.5 SATISFACTORIOS; LABORATORIO NUMÉRICO PENDIENTE DE EJECUTAR')
else:
    subprocess.run([sys.executable, str(numerico)], check=True, cwd=str(root))
    print('\nRESULTADO: VERIFICACIÓN CONJUNTA 3.5 SATISFACTORIA')
