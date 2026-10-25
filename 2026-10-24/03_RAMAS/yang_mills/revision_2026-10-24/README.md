# Revisión de la rama Yang–Mills · 24 de octubre de 2026

Notas de edición surgidas al revisar R‑02. No modifican ningún documento original.

## Comprobado

- `verificar_r02.py` regenera `resultados_r02.json` idéntico.
- T1–T7 y F1–F3 son correctos.
- La dirección difícil de T3 (misma firma implica pares conjugados) no la prueba el verificador original. `T3_direccion_reciproca.py` la comprueba en 2.000 pares aleatorios, en ambas orientaciones, con error ≤ 1,5·10⁻¹³.

## Lectura que conviene conservar

La cantidad central 1 − x² − y² − z² + 2xyz es el determinante de Gram de tres vectores unitarios: es trigonometría de un triángulo esférico. Que no sea negativa es la desigualdad del triángulo, y el defecto ν se anula cuando el triángulo se aplana.

## Para la próxima edición

1. **T3 y la fórmula de ν son el teorema de Vogt–Fricke** (siglo XIX). Para k lazos, los invariantes son polinomios en trazas de palabras de longitud ≤ 3 (Procesi); para una red entera, los lazos de Wilson determinan la conexión salvo gauge (Giles, 1981). La pregunta abierta de la sección 9 ya tiene respuesta.
2. **R‑03 es renormalización por bloques en red.** Bałaban la llevó a nivel riguroso (1985–1988). Posicionar R‑03 frente a ese trabajo antes de abrirlo; el bloqueo pierde información a propósito, y la dificultad está en el flujo de la acción efectiva.
