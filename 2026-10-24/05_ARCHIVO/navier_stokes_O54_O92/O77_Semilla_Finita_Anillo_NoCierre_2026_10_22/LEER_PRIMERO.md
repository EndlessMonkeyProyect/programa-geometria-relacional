# O77 | Semilla finita para un anillo vorticial

**Resultado:** para una familia concreta de perfiles toroidales gaussianos suaves, la evolución exacta de Navier–Stokes genera términos que no pueden reconstruirse variando únicamente cinco parámetros (`A, α, β, b, z0`). Demostración analítica mediante `e^{-2Q}` y control computacional por proyección tangente. **No es una prueba de imposibilidad de toda semilla finita**, ni resuelve el problema general de Navier–Stokes.

## Archivos

- `O77_FORMALIZACION.es.md`: ontología, derivación, teorema de no invariancia, contraste con clase simétrica completa y Lamb–Oseen.
- `codigo/verificar_o77.py`: prueba simbólica y experimental, sin datos externos.
- `datos/resultados_o77.json` y `datos/residuos_o77.csv`: residuos reproducibles en dos resoluciones.
- `graficos/o77_toroide_eta.png`: sección de la distribución de vorticidad del perfil inicial.
- `graficos/o77_transporte_perfil.png`: transporte y difusión de la variable normalizada.
- `REGISTRO_AFIRMACIONES.csv`: clasificación de afirmaciones y límites.
- `MANIFIESTO_SHA256.txt`: huellas de integridad de los componentes.

## Ejecución

Desde el directorio del suplemento:

```bash
python codigo/verificar_o77.py
```

Dependencias: `numpy sympy matplotlib`. Una implementación rigurosa exacta del paso de no-cierre no depende de los valores de los gráficos. Los parámetros geométricos no se identifican con el múltiplo ontológico.

**No modifica los archivos previos O53–O76 ni la Imagen Total v3.8.1.**
