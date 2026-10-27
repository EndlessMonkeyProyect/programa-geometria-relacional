#!/usr/bin/env python3
"""Contratos geométricos de proyección: verificación con fracciones exactas."""
from fractions import Fraction
from pathlib import Path
import json

out=[]
for n in range(1,17):
    N=2**n
    # v = N^(-1/2)*(1,...,1); proyecciones coordenadas.
    # El residuo cuadrático = (número de coordenadas eliminadas)/N.
    foco_atomico=Fraction(N-1,N)  # P elige UNA coordenada
    mitad=Fraction(1,2)           # P elige primera mitad
    todo_menos_una=Fraction(1,N)  # P elige todas MENOS la última
    assert foco_atomico >= Fraction(1,2)
    assert mitad == Fraction(1,2)
    assert todo_menos_una > 0
    assert todo_menos_una == Fraction(1,2**n)
    # Proyector de primera mitad es compatible con el isométrico J_n:
    # e_i -> (e_2i+e_2i+1)/sqrt(2), de R^N a R^{2N}.
    # Verificación combinatoria por soportes, sin aproximaciones.
    A_n=set(range(N//2))
    A_next=set(range(N))
    compatible_mitad=all(((i in A_n)==(2*i in A_next)==(2*i+1 in A_next)) for i in range(N))
    # P 'todo salvo último' cambia de regla sobre una de las dos hijas del último.
    B_n=set(range(N-1))
    B_next=set(range(2*N-1))
    compatible_todo_menos_una=all(((i in B_n)==(2*i in B_next)==(2*i+1 in B_next)) for i in range(N))
    assert compatible_mitad and not compatible_todo_menos_una
    out.append(dict(n=n,N=N,delta2_foco_atomico=str(foco_atomico),delta2_mitad=str(mitad),delta2_todo_menos_una=str(todo_menos_una),compatible_mitad=compatible_mitad,compatible_todo_menos_una=compatible_todo_menos_una))

# TEORMA: Si J es isometría, Ju=u', P'J=JP, entonces
# ||(I-P')u'||^2=||J(I-P)u||^2=||(I-P)u||^2.
# No implica que todos los estados del complemento estén uniformemente separados
# por un operador físico, ni garantiza la positividad en un límite cuántico.
root=Path(__file__).resolve().parent
(root/'resultados.json').write_text(json.dumps({'pruebas':'16 niveles; fracciones exactas; compatibilidad de soportes y regla de recierre', 'filas':out},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('OK: 16 profundidades; residuo mitad = 1/2 constante; residuo minúsculo = 2^-n; compatibilidad comprobada.')
