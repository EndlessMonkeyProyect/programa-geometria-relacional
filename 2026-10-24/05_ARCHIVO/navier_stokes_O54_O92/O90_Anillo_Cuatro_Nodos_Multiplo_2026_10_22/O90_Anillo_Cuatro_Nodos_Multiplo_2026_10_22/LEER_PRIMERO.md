# O90 — Ensayo directo del anillo vorticial

**Resultado:** datos suaves con soporte toroidal, dos giros y cuatro nodos; el bloqueo común 2:1 puede desaparecer bajo perturbaciones arbitrariamente pequeñas sin romper la evolución suave local. En el campo aproximado O69, una perturbación reduce la coherencia relativa de los cuatro nodos. **No hay prueba de regularidad 3D global.**

- `O90_FORMALIZACION.es.md`: demostración y alcance.
- `codigo/verificar_o90.py`: ejecutable autónomo relativo a esta carpeta (necesita NumPy, SciPy, Matplotlib).
- `codigo/o63_operadores.py`, `fuentes/ejecutar_o62_ORIGINAL.py`: componentes anteriores reutilizados.
- `resultados/resumen.json`, `resultados/fases_cuatro_nodos.csv`: números observados.
- `graficos/`: dos gráficos.

La distinción principal para el programa es entre **desfase común**, **desfase relativo** y **continuidad material**. Ninguna de las tres nociones por sí sola prueba regularidad global.
