# O65 — La misma corriente, diferentes condiciones interfaciales

**Autoría del programa:** Le Matt Ansatz Di Ego · 21 de octubre de 2026

Suplemento independiente de la Imagen Total; **no modifica** O64 ni las versiones anteriores.

## Hallazgo

- **[T] Solución particular exacta de dos fases:** una gota esférica transportada por velocidad uniforme mantiene su radio para cualquier `σ>0`; su presión interior cambia mediante `Δp=2σ/s`.
- **[M/E] Misma intensidad turbulenta impuesta:** si `σ` cambia, cambia `d_H∝σ^{3/5}`. Para `d=5 mm`, `ρ=1000 kg/m³` y `ε=0,1m²/s³`, `σ=0,036,0,072,0,144 N/m` da `d_H=3,9275;5,9530;9,0231 mm`. Se trata de diagnóstico de modelo, **no** DNS bifásico ni certidumbre de ruptura.
- **[F]** El mismo múltiplo entero de O58 y la misma geometría no distinguen esas respuestas si se omite `σ`; la relación capilar debe ser visible en cualquier interfaz predictiva para esta pregunta.
- **[A]** No hay derivación de la unidad de área física `A₀`, normalizador entero ni solución general del problema de estabilidad NS.

## Cómo ejecutar

Desde esta carpeta: `python codigo/o65.py`.

Genera `datos/o65_tensiones.csv`, `datos/o65_resumen.json`, `graficos/o65_diametro_vs_tension.png`, `graficos/o65_weber_relativo.png` y muestra el resultado de controles.

El documento `O65_FORMALIZACION.es.md` incluye contrato, pruebas, resultados, falsador, límites y procedencia. `MANIFIESTO_SHA256.txt` contiene las huellas de los archivos incluidos en el paquete, excepto sí mismo.
