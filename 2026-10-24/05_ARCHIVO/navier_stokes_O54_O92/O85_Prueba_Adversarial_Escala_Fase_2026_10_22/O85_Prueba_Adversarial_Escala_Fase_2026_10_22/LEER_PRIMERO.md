# O85 · Guía de lectura y reproducción

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 22 octubre 2026**

O85 somete a prueba el esquema de referencias acumuladas de O84 mediante un escalado crítico exacto de Navier–Stokes sin fuerza. El resultado central no es una prueba de singularidad ni de regularidad general: es la **invariancia exacta del margen de certificación ante concentración espacial**. Agrega un control positivo global (familia ABC de Beltrami) y la persistencia de la información de fase de O79 bajo rescalado.

## Lectura

- `O85_FORMALIZACION.es.md`: formulación, pruebas y límites epistemológicos.
- `codigo/verificar_o85.py`: reproduce verificaciones de escalado, de la proyección de Leray, de ABC y de transferencias de fase.
- `codigo/graficar_o85.py`: genera las tres figuras incluidas.
- `resultados/verificacion.json`: 160 comprobaciones superadas en el estado actual.
- `REGISTRO_AFIRMACIONES.csv`: tabla de resultados etiquetados.
- `MANIFIESTO_SHA256.txt`: integridad de archivos incluidos, excepto el propio manifiesto.

## Ejecutar

```bash
python3 codigo/verificar_o85.py
python3 codigo/graficar_o85.py
```

Requiere Python 3, NumPy y Matplotlib para las figuras.

## Cuidado de interpretación

Las soluciones exactas ABC se justifican analíticamente. Las verificaciones computacionales comprueban identidades derivadas, no integran una solución 3D general. La sucesión de perfiles reescalados de la sección 5 es un **experimento de presupuestos**, no una sola trayectoria de Navier–Stokes ni un blow-up construido. El múltiplo geométrico del escalado **no se identifica** sin prueba con el normalizador cardinal O58.
