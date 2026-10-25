# O70 — Laboratorio reproducible de caja de espejos y referencia colectiva

Documento principal: `O70_FORMALIZACION.es.md`.

**Resultado:** ocho operaciones de simetría calculan una referencia común `Pu`; dos campos con el mismo `Pu` producen distinta evolución proyectada. Una identidad exacta de Navier–Stokes exhibe el término residual `τ`. Dos mallas y comprobaciones numéricas reproducibles. No es una prueba de regularidad global.

## Reproducir

```bash
python -m pip install numpy scipy matplotlib
OPENBLAS_NUM_THREADS=1 python codigo/experimento_o70.py
OPENBLAS_NUM_THREADS=1 python codigo/verificar_cierre_o70.py
python codigo/graficar_o70.py
```

Ejecutar desde cualquier directorio; los archivos usan rutas relativas a su ubicación. El código original reutilizado se incluye en `codigo/o63_operadores.py` y `fuentes/ejecutar_o62_ORIGINAL.py`, no necesita archivos adicionales O69 ni conexión de red.

## Contenido

- `codigo/experimento_o70.py`: proyección D4, campos idénticos en la caja, integración NS RK4 y 14 aserciones.
- `codigo/verificar_cierre_o70.py`: comprobación numérica de identidad del tensor residual en dos resoluciones.
- `codigo/graficar_o70.py`: gráficos.
- `resultados/series.csv`: referencias y residuos en t∈[0,.032].
- `resultados/resumen.json` y `verificacion_tension_residual.json`: observables y verificaciones.
- `graficos/`: imágenes de los resultados.
- `REGISTRO_AFIRMACIONES.csv`: alcance epistemológico.
- `MANIFIESTO_SHA256.txt`: hashes de integridad.

**No confundir:** el grupo D4 no es toda la caja óptica O59; el divisor 8 no es el múltiplo ontológico; el cierre de la proyección no es un cierre físico autónomo.
