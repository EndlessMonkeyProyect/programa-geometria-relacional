# LAB-CONV-2026-10-22 — El nodo convergente frente a la totalidad

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 22 de octubre de 2026**  
**Carácter:** suplemento de investigación aditivo, sin reemplazar fuentes. Se evita la etiqueta O61, ya asignada a una rama de Navier–Stokes en el repositorio.  
**Orden:** narrativa → ontología → lenguaje → matemática → experimento → obligación P/NP.

## 1. Narrativa y ontología [O]

«Cada número nuevo que aparece es un nodo de caminos para llegar a él como soluciones donde convergen estructuras.» Una pluralidad de caminos puede adquirir una referencia común. El cierre propio no exige que todas las historias interiores desaparezcan; exige que las diferencias pertinentes a futuras comparaciones continúen acreditables. La cuantificación radial de la incertidumbre no debe contar como información nueva una relación repetida. La nueva circunstancia puede revelar una dependencia conjunta no visible en un análisis por pares.

La semilla numérica, el múltiplo que la normalizó y la procedencia del nodo no se identifican automáticamente. El radio relacional no es necesariamente una distancia en metros, una entropía ni el radio espectral de otro modelo.

## 2. Definiciones y contratos [D]

- **Camino:** historia de composiciones/reflexiones con una referencia de procedencia.
- **Valor emergente:** etiqueta numérica `v(p)` asignada a un camino; puede coincidir para caminos no equivalentes.
- **Familia de continuaciones:** monoide `C` de operaciones admitidas.
- **Convergencia acreditada:** `p ≡_Q q` si y solo si para toda continuación `c∈C` se tiene `Q(p·c)=Q(q·c)` (MF-97).
- **Nodo candidato:** clase contextual `[p]_{≡Q}` con su valor `v` si tiene sentido, regla de normalización, interfaz suficiente y procedencia reconstruible en el nivel requerido. No identificar `v` con la clase.
- **Interfaz de 3-coloración:** para grafo/módulo `H(I,B)`, `Γ_H(b)=∃i H(i,b)`; conserva factibilidad para contextos que interactúan exclusivamente por `B` (CR-6).
- **Radio contextual de ensayo [D, NO físico]:** elegida una métrica fija `d` sobre realizaciones comparables, `R(C)=diam_d(C)/2` para cada cápsula `C`. Una definición experimental para cuantificar la extensión de diferencia pendiente, no el radio canónico derivado de la ontología.

## 3. Teorema heredado de MF-97 — cierre ante continuaciones [T]

La relación `p ≡_Q q` es una equivalencia estable ante las continuaciones. Por tanto `[p]·c=[p·c]` está bien definida: cualquier camino de una clase puede sustituirla sin alterar el observable Q tras operaciones del contrato. Esta suficiencia es semántica, no una garantía de cálculo económico. MF-86 añade suficiencia, idempotencia y composición para normalizadores que satisfagan sus condiciones.

## 4. Aplicación exacta de CR-6: mismo número, distinto nodo [T/E]

Sean fronteras etiquetadas `(a,b,c)` de tres colores. El módulo `A` exige `a≠b` y el módulo `D` exige `b≠c`. Ambos admiten 18 asignaciones de frontera. Sin embargo, si la nueva circunstancia exige `a≠b`, el módulo `A` mantiene 18 y `D` conserva solo 12. **Igual cardinalidad no implica equivalencia contextual.** Una coincidencia de número no acredita cierre para toda continuación posible. Ver `prueba_radio_y_frontera.py`.

## 5. Lema condicional de radio por extensión [T]

Para una métrica fija `d` y conjuntos no vacíos `C'⊆C`, `diam_d(C') ≤ diam_d(C)` por ser un supremo sobre menos parejas. Así `R(C')≤R(C)`. Si se repite una pregunta que no subdivide la cápsula, `C'=C` y `R` permanece igual.

En cuatro estados de dos bits con distancia de Hamming: `R({00,01,10,11})=1`; al preguntar `x=0` queda `{00,01}` con `R=1/2`; repetir la pregunta conserva `R=1/2`; fijar también `y=0` produce `R=0`. La pregunta `x XOR y=0` deja `{00,11}`: agrega distinción pero no reduce el diámetro (sigue 1). Por tanto `radio menor` no mide universalmente toda nueva información; la medida depende del contrato métrico. No equiparar esta fórmula al radio modal de la pseudoinversa `R_i=1/sqrt(beta λ_i)`: ése depende de pesos del comparador y puede cambiar ante registros repetidos.

## 6. Primera barrera adversarial: un conjunto global incompatible [E/T]

Se reprodujeron tres casos directamente con un algoritmo exacto de 3-coloración y detección de diamantes:

| Caso | V | E | Triángulos | Diamantes | 3-coloreable | Todas las eliminaciones de un vértice 3-coloreables |
|---|---:|---:|---:|---:|---|---|
| C5 | 5 | 5 | 0 | 0 | Sí | Sí |
| K4 | 4 | 6 | 4 | 6 | No | Sí |
| M(C5), grafo de Grötzsch | 11 | 20 | 0 | 0 | No | Sí |

El grafo de Grötzsch se construye por Mycielski aplicado al ciclo C5. Es 4-cromático y triangularmente libre; el ensayo comprueba una 3-coloración fallida en el todo y 11 3-coloraciones posibles al eliminar, de una en una, cada vértice. Como todo subgrafo inducido propio se contiene en alguna de esas eliminaciones, **cada subgrafo inducido propio es 3-coloreable**. No existe testigo diamante porque un diamante contiene triángulos. Este dato no prueba cotas inferiores de complejidad para todos los algoritmos: un invariante global podría detectar la contradicción sin enumeración.

## 7. La dificultad computacional que ya reconocieron CR-6/E25 [T]

Para una frontera vacía `B=∅`, `Γ_H(∅)` es un único bit: indica si el grafo H admite alguna 3-coloración. Construirlo para grafos arbitrarios equivale a decidir 3-coloración, NP-completo. Así, **firma de salida mínima** no implica **construcción mínima**. El resultado de E25 sobre paridades ternarias demuestra que las proyecciones por pares pueden ser insuficientes cuando la nueva comparación es conjunta. Estos son resultados existentes, no una nueva prueba de P=NP.

## 8. Pregunta de avance [A]

Buscar un operador de convergencia tipado sobre grafos generales que, cuando fusiona nodos, entregue un certificado verificable de preservación de `Γ_H` para las continuaciones pertinentes, o un testigo de contradicción. Medir por separado tiempo de descubrir el testigo, tiempo de verificarlo, tamaño de la interfaz, ancho inducido de eliminación, costo de actualización y decisión global. Contrastar especialmente con M(C5), ruedas impares y extensiones adversariales; no solo con XOR, K4 o diamantes.

**Criterio de éxito hacia P=NP:** un algoritmo determinista uniforme, correcto para toda entrada de 3-coloración, con costos de construcción, normalización, actualización, consulta y decisión `poly(|G|)`. Ninguna de las pruebas aquí revisadas acredita todavía ese resultado.

## 9. Reproducibilidad y límites

```bash
python prueba_convergencia_grafos.py
python prueba_radio_y_frontera.py
```

Archivos: `resultados.json` y `radio_frontera_resultados.json`. Pruebas ejecutadas localmente el 22 de octubre de 2026; solo comprueban los casos finitos descritos. Teoremas universales citados de MF-86, MF-97, CR-6, E11, E19 y E25 deben leerse en sus fuentes originales. Este suplemento no supone demostración de P=NP, ni equipara un radio métrico, espectral o físico sin un puente específico.
