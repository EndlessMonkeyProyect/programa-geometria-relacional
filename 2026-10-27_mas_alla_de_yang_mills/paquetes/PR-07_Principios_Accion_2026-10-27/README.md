# PGR — PR-07: De los principios relacionales a la acción, y la separación tres más una

**Fecha:** 2026-10-27 (revisado el mismo día tras dos revisiones externas)  
**Estado:** muestra que cuatro principios del programa generan una **familia de acciones de gauge locales**, una por cada defecto de cierre admisible. Si además el defecto tiene un término cuadrático positivo y no degenerado cerca de la identidad, su límite clásico para campos suaves tiene la forma de Yang–Mills; esa condición es una hipótesis adicional, no una consecuencia de los principios. La acción de Wilson es la elección particular natural y estándar, no la única. Muestra además que la **familia completa** de comparaciones ν distingue el centro de `u(2) = su(2) ⊕ u(1)`: tres más una. Incluye controles. Todo verificado numéricamente.  
No determina la acción, no trata el límite cuántico ni la universalidad, no resuelve la brecha, no demuestra el mecanismo electrodébil de masas ni la identidad física del fotón, y no fija el ángulo de Weinberg.  
**Procedencia:** discusión del 27-oct. El objetivo del programa no es sólo resolver Yang–Mills sino **explicarlo**. A la pregunta de qué pondera las configuraciones, la respuesta fue: "la geometría como relaciones". La hipótesis de trabajo es que SU(2) y U(1) son lo mismo visto a distintas escalas, y que el tres describe esa relación.

## 1. Narrativa

El problema de Clay da la teoría por supuesta y pide la brecha. Este documento hace la pregunta anterior: **¿por qué esa teoría?** El programa responde que las configuraciones se ponderan por su geometría como relaciones. Aquí esa respuesta se traduce en una familia de pesos concretos, y se separa lo que esos pesos explican de lo que todavía no.

## 2. Cuatro principios y la familia de pesos que generan

| principio del programa | consecuencia precisa |
|---|---|
| 1. Las relaciones son transportes entre nodos | las variables son elementos de un grupo, uno por enlace |
| 2. Ninguna referencia local es privilegiada | el peso sólo depende de lazos cerrados (invariancia de gauge), y cada relación se pondera con la medida uniforme del grupo (Haar), la única que no prefiere ninguna referencia |
| 3. Lo independiente se multiplica | el peso es la exponencial de una suma de términos locales |
| 4. Pesa el cierre mínimo según su defecto, que nunca es negativo | un término por plaqueta, `d(U_□)`, con `d ≥ 0`, **invariante bajo conjugación** y **nulo en la identidad** |

La invariancia bajo conjugación no es una hipótesis aparte: cambiar la referencia del nodo desde el que se recorre el lazo, o cambiar ese nodo, conjuga la plaqueta. Lo exige el principio 2.

**La familia.** `dμ = Π dHaar · exp(−β Σ_□ d(U_□))`, un peso por cada defecto admisible.

**Condición para la forma clásica de Yang–Mills (hipótesis adicional).** El defecto debe tener cerca de la identidad un término cuadrático positivo y no degenerado: `d(e^{iεX}) = κ ε² |x|² + O(ε³)`, con `κ > 0`, para `X = x·σ/2`. A eso se suman la simetría y la localidad de arriba, y una normalización que fija κ frente a β. En SU(2) la invariancia bajo conjugación obliga a que ese término sea igual en las tres direcciones. Es el lema de Schur: su(2) es simple, y toda forma cuadrática invariante es un múltiplo de la de Killing. Por eso κ sólo cambia la normalización del acoplamiento, y para campos suaves `Σ d(U_□) → 8κ · (a⁴/8) Σ F^a F^a`.

**La elección de Wilson:** `d_W(U) = 1 − ½ Re tr U`, con κ = 1/8. Es natural y estándar, pero no única:
- **Otra elección admisible:** la acción de Manton, `d_M(U) = θ²/8`, con θ ∈ [0, 2π] el ángulo de rotación de U. Tiene el mismo término cuadrático y el mismo límite clásico.
- **Contraejemplo:** `d(U) = [1 − ½ Re tr U]²` es no negativo, invariante y se anula sólo en la identidad, pero empieza en orden cuatro (κ = 0). No reproduce el término cuadrático clásico: su suma, dividida por `(a⁴/8) Σ F²`, tiende a cero como a⁴.

**Comprobado (A):** cambiar todas las referencias locales al azar deja la acción de Wilson idéntica (36,8102 antes y después), y cada defecto queda entre 0 y 2.

**Comprobado (C):** con un campo suave, `Σ d_W / ((a⁴/8) Σ F^a F^a)` vale 0,988, 0,997, 0,9993 y 0,9998 para redes de 16, 32, 64 y 128.

**Comprobado (G):** sobre 1000 pares aleatorios, y en las mismas redes que C:

| defecto | error de invariancia | κ medido | `Σ d / ((a⁴/8) Σ F²)`, redes 16 → 128 |
|---|---|---|---|
| Wilson, `1 − ½ Re tr U` | 8·10⁻¹⁶ | 0,125 | 0,988 → 0,9998 |
| Manton, `θ²/8` | 1·10⁻¹⁵ | 0,125 | 0,989 → 0,9998 |
| `[1 − ½ Re tr U]²` | 2·10⁻¹⁵ | 1,6·10⁻⁸ = ε²/64, con ε = 10⁻³: tiende a 0 | 1,4·10⁻³ → 3,4·10⁻⁷, dividido por 16 en cada duplicación |

κ es el mismo en 23 direcciones distintas (3 de la base y 20 al azar), con diferencias menores que 10⁻¹².

**Alcance.**
- Los principios no determinan la acción: definen una familia, y Wilson es una elección dentro de ella.
- La condición cuadrática no sale de los cuatro principios. Es una hipótesis adicional, y el contraejemplo muestra que hace falta.
- Las comprobaciones C y G son **clásicas, para campos suaves**. No demuestran universalidad, ni la existencia ni la equivalencia de los límites cuánticos.
- Que el coeficiente 22/3 de la función beta sea común a la familia es un resultado de universalidad de la teoría cuántica de campos, no del programa.
- La acción de Wilson cumple además la positividad de reflexión (Osterwalder–Seiler 1978), necesaria para construir la teoría cuántica. Para otras elecciones hay que comprobarlo en cada caso.

## 3. ν es el defecto del cierre mínimo

Si los transportes no varían de un punto a otro, la plaqueta es exactamente el conmutador: `U_□ = UVU⁻¹V⁻¹`. Con la elección de Wilson, por lo tanto, **`1 − ½ tr U_□ = ν(U,V)`**. Comprobado (B) en 2000 pares, con error 0.

Con otra elección de la familia, el defecto es `d(UVU⁻¹V⁻¹)`. El conmutador está en SU(2), y en SU(2) toda función invariante bajo conjugación depende sólo de ½ tr. Así que ese defecto es una función de ν: ν sigue siendo el invariante del cierre mínimo.

El objeto dinámico general es el defecto de la plaqueta, y ν es su forma cuando los transportes son constantes. Esto resuelve la objeción sobre U(1): ahí el conmutador de dos elementos siempre es trivial, pero la plaqueta no lo es.

## 4. La separación tres más una

**Proposición.** Supongamos que las relaciones son transportes unitarios 2×2 en general, es decir, un cuaternión más una fase. Entonces el grupo es U(2), y la descomposición de su álgebra `u(2) = su(2) ⊕ u(1)` es exacta; es la del sector electrodébil. Escribimos `X = (c·I + x·σ)/2` y `Y = (d·I + y·σ)/2`. Entonces:

1. `ν(e^{iφ}U, e^{iψ}V) = ν(U,V)`: ν es ciego a la fase.
2. Forma cerrada: `ν(e^{iεX}, e^{iεY}) = 2 sen²(ε|x|/2) sen²(ε|y|/2) sen²∠(x,y)`. Por lo tanto `ν = ε⁴ |x×y|² / 8 + O(ε⁶)`, que no depende de c ni de d.
3. **Una sola comparación no aísla el centro.** Si `y ∥ x`, ν = 0 aunque ninguna de las dos direcciones sea central. A primer orden, lo que no ve una comparación con una X no central es un plano: el centro más la propia dirección de x.
4. **La familia completa de comparaciones sí lo aísla.** Una dirección X es invisible frente a todas las comparaciones si y sólo si x = 0, es decir, si es central. Las únicas direcciones que conmutan con todas las demás son las centrales.

Por lo tanto, la familia de comparaciones ν separa u(2) en el centro u(1), de dimensión 1, y su(2), de dimensión 3.

**Prueba.** Las fases conmutan con todo y se cancelan en el conmutador. La forma cerrada sale de `ν = 2|a×b|²` (R-02), con `a = sen(ε|x|/2) x̂` y `b = sen(ε|y|/2) ŷ`; al desarrollar queda ε⁴|x×y|²/8. Esa expresión se anula para toda y si y sólo si x = 0. ∎

**Comprobado (D, primera versión):**
- error de la ceguera de fase: 4·10⁻¹⁶;
- sensibilidad de la dirección central: 1,8·10⁻¹¹, es decir, nula (es redondeo; ver §10);
- sensibilidad de una dirección de su(2): 0,125 = 1/8;
- sensibilidad de una mezcla con 0,3 en su(2): 0,0112 = 0,3²/8. Sólo cuenta la parte en su(2).

**Comprobado (H):**
- forma cerrada contra cálculo directo, en 500 pares con ε = 1: error 9·10⁻¹⁶;
- desviación relativa respecto de `ε⁴|x×y|²/8`, máxima sobre 200 pares: 0,31; 0,086; 0,022 y 0,0056 para ε = 0,4; 0,2; 0,1 y 0,05. Se divide casi por 4 cada vez que ε se divide por 2, y el resto dividido por ε⁶ se mantiene entre 14 y 16: el resto es O(ε⁶);
- **control:** dos transportes no centrales alineados, `X = (0,7·I + x·σ)/2` y `Y = (−1,3·I + 1,7·x·σ)/2`, dan ν = 0 exacto. Con y perpendicular a x, ν = 0,2331, igual a la forma cerrada;
- dimensión de lo que no ve una comparación, a primer orden: 4 si X es central, 2 si no lo es. Lo que no ve ninguna comparación tiene dimensión 1, y es el centro.

[Lectura] La familia de comparaciones ν divide la relación unitaria en **tres direcciones que, por pares, componen sin conmutar** (las de i, j, k) **y una que conmuta con todas**.

**Alcance de §4.** Es una separación algebraica. **No demuestra por sí misma el mecanismo electrodébil de masas, la identidad física del fotón ni el ángulo de Weinberg.** Además, en U(2) el término cuadrático invariante del defecto tiene dos constantes independientes, una para su(2) y otra para u(1). Con `d_W` son iguales (cociente 1); con `d_W + (1 − Re det U)`, que también es admisible, el cociente es 5 (comprobado G). Los principios no fijan ese cociente, y es justamente el que distingue g de g′.

## 5. Control: cuatro referencias en un grafo

La propuesta del otro modelo era que cuatro referencias conectadas dan 3 + 1. Las comprobaciones (E) muestran por qué no sirve:

- **Es conteo.** En 500 grafos conexos al azar, de 3 a 8 referencias, siempre hay un cero y `N − 1` positivos. El "tres" es sólo cuatro menos uno.
- **Su modo nulo es siempre la mezcla uniforme.** El fotón, en la base `(W¹, W², W³, B)`, es `(0, 0, sen θ_W, cos θ_W)`. Su solape con la mezcla uniforme nunca pasa de 1/√2, así que nunca coinciden.
- **Ajustar pesos no lo arregla.** Ajustando los 6 pesos se reproduce exactamente el espectro `(0, g², g², g²+g′²)`, pero el modo nulo sigue siendo uniforme. Ajustar reproduce las masas, no el fotón.

El 3 + 1 del tetraedro es conteo, en el espacio equivocado. El de §4 está en el espacio de los generadores y no se elige a mano.

## 6. La teoría electrodébil en el lenguaje de ν

La matriz de masas conocida (F), a orden árbol y con acoplamientos aproximados en la escala del Z (`g = 0,6517`, `g′ = 0,3576`, `v = 246,22 GeV`), da `M_W ≈ 80,2` y `M_Z ≈ 91,5` GeV. Los valores medidos son 80,4 y 91,2. El fotón queda en `(0, 0, 0,481, 0,877)`.

**Lectura exacta en el programa:** la fracción del fotón que cae en la parte que ν ve, `su(2)`, es **exactamente `sen²θ_W ≈ 0,231`**. El resto, `cos²θ_W`, cae en el eje que ν no ve. Es una lectura del resultado conocido, no una derivación: el fotón y su mezcla vienen del Modelo Estándar.

El número abierto, dicho en el lenguaje del programa, es éste: **¿por qué la dirección que sobrevive pone el 23 % de su peso en la parte que compone sin conmutar?**

Hay un precedente de cómo se responde algo así: la unificación SU(5) fija `sen²θ_W = 3/8` en la escala de unificación a partir de cómo se encaja el grupo, y luego ese valor corre con la escala. El análogo en el programa sería una regla estructural que fije el cociente entre las dos constantes cuadráticas de §4, es decir, la normalización del eje ciego frente a los tres sensibles.

## 7. Lo que esto explica y lo que no

**Explica**, a nivel clásico: por qué, con la condición cuadrática, el peso pertenece a la clase de Yang–Mills, y por qué el álgebra electrodébil se parte en 3 + 1 tal como la ve la familia de comparaciones ν.

**No explica:**
- **La dirección de escala.** En SU(2) puro, los efectos no abelianos **crecen** a grandes distancias (confinamiento); no se apagan hacia U(1). La hipótesis tiene que reformularse: lo que cambia con la escala es qué relaciones distingue una referencia, no el grupo.
- **Por qué tres direcciones adquieren masa y una no.** En el Modelo Estándar lo hace el Higgs, observado a 125 GeV; el programa todavía no lo reproduce ni lo reemplaza. Además, una simetría gauge local no se rompe espontáneamente (Elitzur), así que la descripción tiene que ser invariante.
- **La identidad física del fotón.** La dirección ciega a ν es el centro u(1); que el fotón observado sea la mezcla que es, lo da el Modelo Estándar.
- **El valor de θ_W y la escala de masa.** Los principios no fijan el cociente entre las dos constantes cuadráticas de U(2) (G).
- **La brecha de masa**, que sigue exactamente como en PR-06.
- **Por qué el grupo es U(2).** Falta revisar las hipótesis PC1–PC5 de la v2.1 para ver si salen de los principios o se suponen.

## 8. Falsadores

- **F1.** Si alguna acción de la familia con término cuadrático positivo y no degenerado tuviera un límite clásico suave que no fuera de la forma de Yang–Mills, §2 fallaría. El argumento de Schur dice que no ocurre; el falsador sirve para poner a prueba ese argumento.
- **F2.** Si las relaciones fueran sólo cuaterniones unitarios, sin fase, el grupo sería SU(2) o SO(3). Entonces ν vería las tres direcciones, no habría ninguna dirección ciega y no habría candidato a fotón. **El 3 + 1 exige que las relaciones lleven fase.** Es una condición verificable sobre el programa.
- **F3.** Cualquier afirmación de 3 + 1 basada en contar referencias es vacía, por E.
- **F4.** La fracción `sen²θ_W` supone la normalización usual de los campos. Cambiar el cociente entre las dos constantes cuadráticas cambia la fracción. Es justamente la ambigüedad que la unificación resuelve, y el programa necesita su propia regla para resolverla.

## 9. Siguiente

1. Revisar PC1–PC5 para ver si el programa obliga a relaciones con fase (U(2)) o las supone.
2. Buscar una regla del programa que fije el cociente entre las constantes cuadráticas de u(1) y su(2), y comparar su `sen²θ_W` con 3/8 y con 0,231.

## 10. Ejecución y reproducibilidad

    python verificar.py

Dependencias: `numpy`, `scipy`; unos 6 segundos. Regenera `resultados.json`.

Las secciones A–F son las de la primera versión y dan exactamente los mismos valores. G y H usan un generador aleatorio aparte (semilla 20261028).

Tres valores de la primera versión son numéricamente sensibles. El complemento los compara con una tolerancia específica, justificada en `comparar_resultados.py`; todo lo demás conserva la tolerancia general.
- `D_U2/sensibilidad_mezcla`: ν ≈ 7·10⁻⁸ se calcula como `1 − ½ tr` de una matriz próxima a la identidad. La cancelación deja un error relativo de unos 2·10⁻⁹, que cambia con la biblioteca de álgebra lineal.
- `D_U2/sensibilidad_direccion_central`: su valor exacto es 0. Lo almacenado es redondeo, y se compara en absoluto.
- `E_control_grafo/espectro_ajustado`: sale de un ajuste por mínimos cuadrados con autovalores degenerados, que se detiene con tolerancia de unos 10⁻⁸.

Esos valores se conservan tal cual. Las secciones nuevas calculan ν sin cancelación: si el conmutador es `c0·I + i c·σ`, se usa `ν = |c|²/(1 + c0)`.

Los pesos ajustados de E no son únicos: con otras versiones de numpy y scipy cambian hasta un 50 %. Por eso se compara el espectro que producen, no los pesos.

**Alcance:** familia clásica de acciones y estructura del álgebra. No límite cuántico, no universalidad, no mecanismo de masas, no identidad del fotón, no θ_W, no brecha.
