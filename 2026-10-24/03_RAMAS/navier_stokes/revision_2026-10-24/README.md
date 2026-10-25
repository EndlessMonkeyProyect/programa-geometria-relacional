# Revisión de la rama Navier–Stokes · 24 de octubre de 2026

Notas de edición surgidas al revisar O93 y la rama integral O24–O93. No modifican ningún documento original.

## Comprobado

- O93 se reproduce bit a bit: `verificar_o93.py` y `simulacion_galerkin.py` regeneran los mismos JSON y CSV.
- Los verificadores de O80, O81, O82, O83, O84, O85, O86 y O92 regeneran sus 16 archivos de resultados idénticos.
- Los valores exactos de E3 (W = 95/9, B = 266/9, P = ±3/4) se confirman por otra vía en espacio físico: `verificar_W_B_P_espacio_fisico.py`.
- El certificado E5 se audita completo en O84: L = 6, M = 9, 𝔐₀ ≈ 0,5195 y 𝔐₁ ≤ 0,2717 son correctos.

## Para corregir en la próxima edición

1. **El criterio de O93 equivale a la conclusión.** Su integrando es ½·[(log W)′]₊, y en el toro toda singularidad hace explotar W. La integral es finita si y solo si no hay explosión. Decirlo explícitamente, o retirarlo como resultado principal.
2. **P = M³𝒯 sale por homogeneidad** (el término es cúbico); no requiere la dinámica de O92. Presentarlo como identidad de escala.
3. **`simulacion_galerkin.py` falla en Python 3.13** en la línea `__import__('importlib').util`. Se corrige con `import importlib.util` al inicio. El registro `ejecucion_galerkin_3_9.log` ya muestra el error.
4. **E4 no verifica nada independiente:** evalúa la fórmula y comprueba su signo (Cauchy–Schwarz). Compararla con una derivada calculada aparte.
5. **E6 es demasiado corto** (t = 0,08) para decir algo sobre regularidad. Si se conserva, que evalúe la integral del criterio.
6. **Citas:** Lei–Lin, Pizzocchero y Chemin–Gallagher–Paicu están en O80 y O81, pero no llegan a O93 ni al capítulo de la Imagen Total. El precedente directo de O82–O84 (certificados *a posteriori*, Chernyshenko, Constantin, Robinson y Titi, 2007) no aparece en ningún archivo.

## Vía propia

`../modelo_propio_O18/` contiene el único camino de la rama hacia un teorema sobre la ecuación propia: derivar las ganancias por octava gⱼ desde la regla del espejo antes de comparar con el umbral de Lions, Tao y Barbato–Morandin–Romito.
