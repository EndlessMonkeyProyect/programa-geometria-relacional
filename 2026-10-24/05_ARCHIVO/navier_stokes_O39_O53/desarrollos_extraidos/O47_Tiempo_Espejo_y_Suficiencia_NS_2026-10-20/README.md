# O47 — Tiempo relacional y continuidad del espejo

Este suplemento se añade a los trabajos O25/O41/O45/O46 **sin reemplazarlos**.

## Hallazgos exactos

- O47-A: mismo MCM=12, misma E/J/escala/fase; diferencia de primera derivada de palinstrofía de -0.0756.
- O47-B: MCM=60 y misma E/J/escala/fase **y energía cinética**; diferencia de primera derivada de palinstrofía de -0.108864.

## Reproducir

Desde la carpeta del suplemento, con Python 3 y NumPy:

```
python verificar_O47.py --N 24 32 48 --T .12 --dt .004
python verificar_O47.py --N 32 --T .12 --dt .002
python verificar_O47_control_energia.py
```

La primera y segunda orden de ejecución del script principal escriben `O47_RESULTADOS.json`; para preservar ambos resultados, copiar el JSON entre ejecuciones o consultar los JSON nombrados que ya vienen en el paquete.

## Límites

Solver numérico Galerkin finito y trazadores trilineales. No existe prueba de regularidad global de Navier–Stokes ni tiempo propio relativista derivado. La referencia material es un marcador operativo, no una singularidad ontológica físicamente identificada.
