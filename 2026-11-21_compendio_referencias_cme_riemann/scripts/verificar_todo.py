#!/usr/bin/env python3
"""Orquestador de los controles del compendio. Requiere numpy para tres ensayos.
Ejecutar desde cualquier directorio: python3 scripts/verificar_todo.py
Duración típica: menos de un minuto (recalcular_gram.py ocupa casi todo el tiempo).
"""
import platform
import subprocess
import sys
from pathlib import Path

import numpy

base = Path(__file__).resolve().parent
scripts = ['verificar_puentes.py', 'verificar_reflexiones.py', 'verificar_periodos.py',
           'verificar_focos.py', 'ensayo_angulos.py', 'recalcular_gram.py']
print(f'Entorno: Python {platform.python_version()}; numpy {numpy.__version__}; '
      f'{platform.system()} {platform.machine()}')
for name in scripts:
    print(f'\n====== {name} ======', flush=True)
    subprocess.run([sys.executable, '-B', str(base / name)], cwd=base, check=True)
print('\nTODOS LOS CONTROLES PROGRAMADOS: PASS.')
print('Alcance: identidades y lemas enumerados, instancias finitas y cifras de Gram en float64.')
