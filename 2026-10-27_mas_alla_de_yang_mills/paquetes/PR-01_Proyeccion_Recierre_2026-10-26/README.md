# PGR — PR-01: Proyección, diferencia y recierre coherente entre escalas

**Fecha:** 2026-10-26  
**Estado:** teorema exacto de geometría auxiliar; falsador exacto de una inferencia general; no demuestra la brecha física de Yang–Mills.  
**Procedencia conceptual:** MF-106 §3 y §8; MF-86, MF-97; MF-103 y MF-104; YM-R3B. Documento aditivo: no sustituye fuentes.

## 1. Narrativa ontológica

La unidad se conserva. Una proyección revela una parte y mantiene un resto respecto de la comparación. Su norma no puede ser negativa, pero la existencia de resto en cada profundidad no prueba un tamaño mínimo de resto en toda la familia de profundidades. El recierre puede conservar exactamente una diferencia ya acreditada si las interfaces respetan la misma pregunta al profundizar.

## 2. Contrato matemático

En H_n=R^(2^n), tomar el vector unitario u_n=(1,...,1)/sqrt(2^n). Para una proyección ortogonal coordenada P_{A,n} que conserva las coordenadas indexadas por A, el residuo cuadrático es

    δ_n(P)=||(I-P)u_n||²=(2^n-|A|)/2^n.

Esta norma es siempre no negativa; el radio de resto es sqrt(δ_n).

Tres familias admisibles **en este modelo Hilbertiano**, distintas entre sí:

- Foco de un átomo A={0}: δ_n=1-2^(-n) ≥1/2 para n≥1.
- Foco de una mitad A={0,...,2^(n-1)-1}: δ_n=1/2 en todo n.
- Proyección que retiene todo excepto una coordenada A={0,...,2^n-2}: δ_n=2^(-n)>0, pero inf_n δ_n=0.

**Advertencia sobre MF-106 §8:** allí `1-2^-n` es la proporción (N−1)/N del rango de incidencia de un grafo conectado (N=2^n), **no** una cota universal para el resto de cualquier proyección. Coincide numéricamente con el primer ejemplo por elección especial de P; no constituye identidad entre los dos contratos.

## 3. Teorema exacto: compatibilidad de recierre

Sea J_n:H_n→H_(n+1) una isometría, u_(n+1)=J_n u_n, y P_n y P_(n+1) proyecciones ortogonales. Si

    P_(n+1) J_n = J_n P_n,

entonces

    (I-P_(n+1))u_(n+1)=J_n (I-P_n)u_n,
    δ_(n+1)=δ_n.

La prueba usa solo linealidad e isometría. En consecuencia, δ_n0>0 implica δ_n=δ_n0>0 para la *misma referencia transportada* en todos los niveles siguientes.

Para la inclusión binaria J_n(e_i)=(e_(2i)+e_(2i+1))/sqrt(2), el foco en la primera mitad cumple la compatibilidad, y su residuo 1/2 se conserva. La familia 'todo salvo un átomo' no cumple esa compatibilidad, y su residuo tiende a cero.

## 4. Límite lógico / nuevo contrato necesario

No debemos presuponer que la proyección física selecciona uno de esos focos, ni que el cierre propio obliga a P_(n+1)J_n=J_nP_n. Esto debe derivarse a partir de las reglas de relación y de las continuaciones MF-97; si no se puede, el tercer ejemplo refuta la afirmación de una cota positiva **para todas las proyecciones ortogonales admisibles**.

Aun demostrando esta compatibilidad para un foco elegido, se habría conservado el residuo de ese foco, **no** una cota inferior para cada modo excitado en el sector completo de una teoría cuántica. El paso de la geometría de referencias al operador físico de transferencia sigue siendo una identificación independiente, no una redefinición de 'masa'.

### Cotejo con MF-86/MF-97

MF-86 exige suficiencia, idempotencia y composicionalidad del normalizador de una cápsula en un contrato de preguntas. MF-97 exige que las equivalencias de las interfaces se mantengan ante continuaciones admisibles. **Esas exigencias semánticas no implican, por sí solas, que el mapa de escala sea una isometría de Hilbert o que los proyectores conmuten con ese mapa.** Por ello la condición P_(n+1)J_n=J_nP_n se introduce aquí como hipótesis verificable, NO como una derivación ya encontrada en MF-86 o MF-97.

## 5. Falsadores en el lenguaje del programa

- F1: ¿MF-97 permite que el observador/proyección conserve todo menos un átomo nuevo? Si sí, no existe cota universal de residuo entre todas las preguntas admisibles.
- F2: ¿Un recierre coherente puede alterar el resto de una misma comparación? Si sí, debe localizarse qué hipótesis de compatibilidad falla.
- F3: ¿El contrato que fija una mitad se impone sin derivarlo de la estructura, o se deriva de las relaciones propias? La primera opción da un teorema condicional, no una deducción universal.
- F4: ¿La diferencia de un foco coincide con la mínima diferencia sobre **todos** los estados o continuaciones de la teoría física? Esta identificación no ha sido demostrada.

## 6. Ejecución

    python verificar.py

Genera `resultados.json` utilizando fracciones exactas y 16 niveles, verifica conservación o colapso y la compatibilidad de los soportes de ambos tipos de proyección. No utiliza datos físicos ni energía.
