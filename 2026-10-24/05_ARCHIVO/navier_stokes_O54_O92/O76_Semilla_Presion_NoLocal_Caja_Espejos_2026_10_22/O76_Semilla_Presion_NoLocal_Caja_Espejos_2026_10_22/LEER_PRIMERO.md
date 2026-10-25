# O76 | Semilla suficiente y presión no local — 22 octubre 2026

Paquete aditivo de investigación del Programa de Geometría Relacional. No modifica los archivos O70–O75 ni la Imagen Total.

**Lectura principal:** `O76_FORMALIZACION.es.md`.

## Hallazgos

1. Construcción analítica de un campo suave sin divergencia y de cuatro nodos cuyos valores de velocidad y derivadas hasta orden dos son idénticos a los de un fluido en reposo; pero sus aceleraciones relativas iniciales difieren por el gradiente de presión no local. Valor exacto para amplitud 1: `6912/5525 = 1.2510407239819…`.
2. Caja D₄: los dos campos tienen la misma proyección común inicial (cero), pero distintas derivadas del común; aparece un residuo cuadrático reproducible.
3. Contrapeso positivo: familia ABC/Beltrami de soluciones 3D exactas que posee una semilla finita `(A,B,C)` y una ley de evolución autónoma.
4. Estas afirmaciones **no resuelven Navier–Stokes 3D**, no infieren un mínimo de gota ni identifican la normalización aritmética de O68 con una cantidad física.

## Reproducir

```bash
python -m pip install numpy matplotlib
python codigo/verificar_o76.py --N 64
python codigo/verificar_o76.py --N 96
```

Se necesitan sólo NumPy para los controles, Matplotlib opcional para producir la gráfica. Los CSV y JSON de este paquete ya contienen salidas reproducidas y están listos para verificación. No hace falta conexión de Internet.

El archivo `REGISTRO_AFIRMACIONES.csv` identifica los estatus `[D]`, `[E]`, `[H]`, `[F]`. `MANIFIESTO_SHA256.txt` permite verificar integridad de los archivos principales.
