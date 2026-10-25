# 08. Auditoría cruzada: qué une las ramas y qué no

## Diagrama de dependencias

`NARRATIVA → diferencia/comparación → firmas y fibras → cierre suficiente según preguntas → nueva referencia`.

**Luego** se bifurca:

- `P vs NP`: construir interfaz uniforme y polinómica para cualquier 3-SAT.
- `Yang–Mills`: relación gauge → comparador irreducible sobre estados → coercividad → Hamiltoniano físico → control RG/continuo y existencia.
- `Navier–Stokes`: vorticidad y forma → leyes de evolución 2D/3D → observables objetivos → control de concentración/regularidad global en 3D.
- `Masa/gravedad`: seleccionar un modelo físico → unidades/observables independientes → concordancia y falsación.
- `Lenguaje/ROSI`: interfaz semántica → prueba de reconstrucción y transferencia en datos no vistos.

## Tabla de fallos de inferencia

| Inferencia tentadora | Estado | Testigo crítico |
|---|---|---|
| aparece un nuevo máximo ⇒ hay mass gap | FALSA | dos gaussianas bajo ecuación del calor en ℝ²; `−Δ` sin brecha espectral |
| dos etiquetas se mezclan ⇒ nace nuevo remolino objetivo | FALSA | O37 depende de partición; misma ω admite otras etiquetas |
| mismo radio y primeros momentos ⇒ misma evolución | FALSA | O26: mismo H,A,B y diferente C / `dot n` |
| fases coinciden ⇒ formas completas persisten | FALSA | cizalla viscosa O30 con amplitudes que cambian |
| simetría inicial preservada ⇒ surge simetría nueva | NO JUSTIFICADA | O33 prueba conservación, O38 reorganización sin nueva simetría exacta |
| formas se acercan inicialmente ⇒ sincronización eterna | NO JUSTIFICADA | O36 acercamiento unilateral y ventana finita |
| ν(U,V)>0 alguna vez ⇒ brecha uniforme | NO JUSTIFICADA | U(1)/Cartan, estado vs configuración, límite continuo abiertos |
| cociente contextual compacto ⇒ P=NP | NO JUSTIFICADA | construir y consultar el cociente puede ser exponencial |
| `Rω=v_*` espectral ⇒ regla de remolinos y c | NO JUSTIFICADA | distintos radios/circulaciones físicas y reloj lógico |
| radio modelo ≈ radio RMS protón ⇒ QCD derivada | NO JUSTIFICADA | falta corriente y factor de forma dinámico |

## Punto más fértil a corto plazo: prueba de coercividad [A]

En una red pequeña SU(2), plantear una familia completa de comparadores gauge-invariantes y una forma cuadrática `D_rel`. Calcular su núcleo y construir un testigo no constante invisible o demostrar irreducibilidad. O38 enseña a **separar reorganización de forma y control espectral**. Si la coercividad falla, registrar cuál diferencia permanece no comparada; si funciona, medir cómo degenera con tamaño de red y escala. La importancia del puente solo puede afirmarse después de trasladarlo a la forma dinámica física.

## Requisitos de cierre publicable [A]

1. Especificar una proposición que diferencie al programa de una reformulación clásica.
2. Probarla bajo contratos completos o declarar experimento con criterio preregistrado.
3. Construir al menos un contraejemplo adversarial dentro de la misma clase de interés.
4. Probar independencia del resultado ante refinamiento, representaciones y parámetros relevantes.
5. Someter a evaluación externa sin afirmar solución de Clay mientras falten obligaciones.
