#!/usr/bin/env python3
"""Verificación externa reproducible: el detector local anterior no ve
patrones de paridad 3/4; el reconocedor distribuido sí ve compuertas XOR.
Ejecutar dentro de esta carpeta: python CONTROL_ANTES_DESPUES.py
"""
from laboratorio_relaciones_distribuidas import gen,extract
from laboratorio_anterior_local import extract as extract_local
for n,u in [(12,1),(24,2),(32,3),(96,3)]:
    g=gen(n,2,981+n*7+2,partial=u)
    before=extract_local(g['variables'],g['cnf'],True)
    after=extract(g['cnf'],g['variables'])
    assert len(before['full'])==len(before['near'])==0
    assert after['xor_gates']==n and after['n_near']==u
    print(f'n={n} | antiguo: 0 completos/0 parciales | nuevo: '
          f"{after['xor_gates']} XOR2 y {after['n_near']} raíces parciales")
print('PASS')
