# Más allá de Yang–Mills: un marco relacional de su emergencia

**Autor:** Le Matt Ansatz Di Ego (Programa de Geometría Relacional)\
**Fecha:** 27 de octubre de 2026\
**Estado:** borrador para revisión. No es una solución del problema de la brecha de masa del Clay Mathematics Institute ni pretende serlo.

## Resumen

El problema de Yang–Mills del Clay Institute da la teoría por supuesta y pide demostrar la brecha de masa. Este trabajo hace una pregunta anterior: ¿por qué esa teoría? Proponemos un marco en el que Yang–Mills emerge de cuatro principios relacionales: las relaciones son transportes entre nodos; ninguna referencia local es privilegiada; lo independiente se multiplica; y cada cierre mínimo pesa según un defecto local que nunca es negativo y se anula cuando el cierre es perfecto. Mostramos que estos principios generan una familia de acciones de gauge locales. Si además el defecto tiene un término cuadrático positivo y no degenerado cerca de la identidad (una hipótesis adicional), su límite clásico para campos suaves tiene la forma de Yang–Mills. La acción de Wilson es la elección particular natural y estándar, no la única, y verificamos numéricamente su límite clásico, el de otra elección y el de un contraejemplo. Mostramos además que el observable de incompatibilidad del programa, ν = 1 − ½ tr(UVU⁻¹V⁻¹), es el defecto de plaqueta para transportes constantes. La familia completa de comparaciones ν distingue el centro del álgebra u(2) = su(2) ⊕ u(1): tres referencias que componen sin conmutar y una fase común. Declaramos explícitamente lo que el marco no explica: la brecha de masa, el mecanismo que da masa a tres modos electrodébiles, la identidad física del fotón, el valor del ángulo de Weinberg y la dirección del cambio de escala. Todos los resultados vienen con scripts reproducibles.

## 1. Motivación

La física describe con enorme precisión qué teorías de gauge rigen la naturaleza, pero rara vez se pregunta por qué esas y no otras. El Programa de Geometría Relacional parte de una ontología en la que lo primario son las relaciones y su cierre, no los objetos. Si esa ontología es fértil, debería ser capaz de explicar la forma de las teorías conocidas, no solo de reinterpretarlas. Este artículo pone a prueba esa capacidad con Yang–Mills.

Aclaramos el alcance desde el inicio: explicar la emergencia de una teoría no equivale a resolverla. La brecha de masa sigue siendo un problema abierto, y nada de lo que sigue la demuestra.

## 2. Cuatro principios relacionales

1. **Las relaciones son transportes entre nodos.** Cada relación se representa por un elemento de un grupo asignado a un enlace.
2. **Ninguna referencia local es privilegiada.** El peso de una configuración solo puede depender de lazos cerrados (invariancia de gauge), y cada relación se pondera con la medida uniforme del grupo (medida de Haar), la única que no favorece ninguna referencia.
3. **Lo independiente se multiplica.** La novedad actúa como factor multiplicativo; los pesos de cierres independientes se multiplican, de modo que el peso total es la exponencial de una suma de términos locales.
4. **Pesa el cierre mínimo según su defecto.** El término local es un defecto de cierre de la plaqueta, d(U), que nunca es negativo (nada se compara negativamente), es invariante bajo conjugación y se anula en la identidad (el cierre perfecto no pesa). La invariancia bajo conjugación la exige el principio 2: cambiar la referencia del nodo desde el que se recorre el lazo conjuga la plaqueta.

## 3. Resultado 1: los principios generan una familia de acciones; con la condición cuadrática, de la clase de Yang–Mills

Los cuatro principios dan una familia de pesos, uno por cada defecto admisible:

dμ = Π dHaar · exp(−β Σ d(U\_plaqueta)).

**Condición cuadrática.** Para recuperar la forma clásica de Yang–Mills hace falta una condición más, que no sale de los principios: el defecto debe tener cerca de la identidad un término cuadrático positivo y no degenerado, d(e^{iεX}) = κε²|x|² + O(ε³) con κ > 0 para X = x·σ/2, junto con la simetría, la localidad y una normalización que fija κ frente a β. En SU(2), la invariancia bajo conjugación obliga a que ese término sea igual en las tres direcciones del álgebra (lema de Schur), así que κ solo fija la normalización del acoplamiento. Con eso, para campos suaves, la suma de defectos tiende a 8κ veces (a⁴/8) Σ F².

**La elección de Wilson.** d\_W(U) = 1 − ½ Re tr U, con κ = 1/8, es la elección particular natural y estándar, pero no la única. Verificaciones: un cambio aleatorio de todas las referencias locales deja la acción idéntica; todos los defectos quedan entre 0 y 2; y para un campo suave el cociente entre la suma de defectos y (a⁴/8) Σ F² tiende a 1 (0,988; 0,997; 0,9993; 0,9998 para redes de 16 a 128).

**Otra elección y un contraejemplo.** La acción de Manton, d = θ²/8 con θ el ángulo de rotación de U, tiene el mismo término cuadrático y el mismo límite (0,989 → 0,9998). En cambio, d(U) = [1 − ½ Re tr U]² es no negativo, invariante y se anula solo en la identidad, pero empieza en orden cuatro. No reproduce el término cuadrático clásico: su cociente tiende a cero como a⁴ (1,4·10⁻³ → 3,4·10⁻⁷).

**Alcance.** Los principios no determinan la acción: definen una familia, y Wilson es una elección dentro de ella. La condición cuadrática es una hipótesis adicional, y el contraejemplo muestra que hace falta. Las comprobaciones del límite continuo son clásicas, para campos suaves: no demuestran universalidad ni la existencia de la teoría cuántica. Que el coeficiente 22/3 de la función beta de SU(2) sea común a toda la familia es un resultado de universalidad de la teoría cuántica de campos, no del programa.

## 4. Resultado 2: ν es el defecto del cierre mínimo

Cuando los transportes no varían de un punto a otro, la plaqueta coincide con el conmutador UVU⁻¹V⁻¹, y su defecto de Wilson es exactamente ν(U,V). Verificado en 2000 pares con error nulo. Con otra elección de la familia, el defecto del conmutador es una función de ν, porque en SU(2) toda función invariante bajo conjugación depende solo de la traza. Así, ν es la forma del defecto dinámico general en el caso de transportes constantes, y el objeto dinámico completo es el defecto de plaqueta.

## 5. Resultado 3: tres referencias y una fase común

Si las relaciones son transportes unitarios 2×2 generales (un cuaternión más una fase), el grupo es U(2), y la descomposición de su álgebra, u(2) = su(2) ⊕ u(1), es exacta y coincide con la del sector electrodébil. Escribimos los generadores como X = (cI + x·σ)/2 e Y = (dI + y·σ)/2. Entonces:

- ν es exactamente insensible a la fase: ν(e^{iφ}U, e^{iψ}V) = ν(U,V).
- Para transportes pequeños, ν(e^{iεX}, e^{iεY}) = ε⁴|x×y|²/8 + O(ε⁶): depende solo de las partes en su(2).
- Una sola comparación no distingue el centro: dos transportes no centrales alineados (y paralelo a x) dan ν = 0. Lo distingue la familia completa de comparaciones: una dirección es invisible frente a todas si y solo si su componente x es nula, es decir, si es central, porque las únicas direcciones que conmutan con todas las demás son las centrales.

Verificado numéricamente: la expansión, con resto de orden ε⁶, y el control, en el que dos transportes no centrales alineados dan ν = 0 exacto y dos no alineados dan 0,2331.

En el lenguaje del programa: una partícula tiene tres referencias para orientarse, tres espacios de comparación que al despejarse quedan a 90 grados (las i, j, k del cuaternión), y entre cualquier par de ellas el orden de comparación importa. La cuarta componente no es una referencia más, sino la fase común que comparten sin distinguirlas.

**Lectura del programa (interpretación, no derivación).** El autor identifica esa fase común con el tiempo: el vacío que se va cubriendo, el espejo que se desplaza, la relación cambiante entre el tamaño del universo y el de la partícula. Señalamos el apoyo y el límite de esta lectura: en mecánica cuántica la evolución temporal actúa como una fase, e^{−iEt}; pero la fase de u(1) es interna y no es el tiempo del espacio.

**Control.** Un 3+1 obtenido contando cuatro referencias en un grafo es trivial: cualquier grafo conexo de N nodos da un modo nulo y N−1 positivos, y su modo nulo es la mezcla uniforme, que nunca coincide con el fotón. El 3+1 de este trabajo, en cambio, está en el espacio de los generadores y no se elige a mano.

**Alcance.** La separación 3+1 es algebraica. No demuestra por sí misma el mecanismo electrodébil de masas, la identidad física del fotón ni el ángulo de Weinberg. Además, en U(2) el término cuadrático invariante del defecto tiene dos constantes independientes, una para su(2) y otra para u(1); los principios no fijan su cociente, que es el que distingue los dos acoplamientos.

## 6. El ángulo de Weinberg como comparación

En el Modelo Estándar, el fotón es una mezcla de la fase común y de una de las tres referencias. La fracción de su peso en la parte su(2) es exactamente sen²θ\_W = g′²/(g² + g′²): una comparación entre la parte de un acoplamiento y la totalidad de los dos. En la unificación SU(5) esa fracción vale 3/8 en la escala de unificación y luego corre con la escala, porque el inverso de cada acoplamiento suma un término proporcional a su logaritmo. Con el contenido del Modelo Estándar solo, esa evolución no reproduce el valor medido en la escala del bosón Z (cerca de 0,231); con supersimetría el acuerdo mejora.

En el marco, esa fracción depende del cociente entre las dos constantes cuadráticas del defecto en U(2), que los principios dejan libre. El autor propone que la fracción se hereda de escala en escala y que, al normalizar, la escala queda en el denominador como relación. Esto coincide en forma con la evolución conocida. Lo que el marco aún debe mostrar es cuantitativo: qué coeficientes de herencia corresponden a las tres referencias y a la fase común, y si reproducen sin ajustes el valor medido, partiendo de una fracción inicial que el propio marco fije.

## 7. Lo que el marco no explica

- **La brecha de masa.** Si la dinámica emergente es Yang–Mills, la brecha es exactamente el problema abierto. Cálculos complementarios en modelos de Ising (paquetes PR-05 y PR-06, que reproducen resultados conocidos) muestran que el lenguaje de cierre sostiene demostraciones reales donde existen las herramientas, y que la pieza faltante para gauge no abeliano es una desigualdad del tipo Simon–Lieb.
- **La dirección de escala.** En SU(2) puro los efectos no abelianos crecen a grandes distancias; no se apagan hacia U(1).
- **El mecanismo de masa.** En el Modelo Estándar tres modos adquieren masa por el campo de Higgs, observado a 125 GeV. El marco aún no lo reproduce ni lo reemplaza.
- **La identidad física del fotón.** La dirección ciega a ν es el centro u(1); que el fotón observado sea la mezcla que es, lo da el Modelo Estándar.
- **El valor de θ\_W.**
- **Por qué el grupo es U(2).** Requiere revisar si las hipótesis PC1–PC5 del programa obligan a que las relaciones lleven fase.

## 8. Falsadores

1. Si alguna acción de la familia con término cuadrático positivo y no degenerado tuviera un límite clásico suave que no fuera de la forma de Yang–Mills, la afirmación de la sección 3 fallaría.
2. Si las relaciones del programa no llevaran fase, no habría fase común y la separación 3+1 desaparecería.
3. Cualquier afirmación de 3+1 basada solo en contar referencias es vacía.
4. Si la regla de herencia propuesta no reproduce sin ajustes el valor medido de sen²θ\_W en la escala del Z (cerca de 0,231), la lectura del ángulo de mezcla queda refutada.

## 9. Conclusión

Este trabajo no resuelve Yang–Mills. Propone un marco de su emergencia: los principios relacionales generan una familia de acciones de gauge que, con la condición cuadrática, es de la clase de Yang–Mills, y la familia de comparaciones ν distingue en el álgebra electrodébil tres referencias y una fase común.

El eje de la investigación siguiente es la brecha, no la acción, y el camino ya tiene sus eslabones. La tabla indica cuáles son teorema y cuáles faltan.

| Eslabón | Enunciado | Estatus |
| --- | --- | --- |
| Criterio (PR-04) | La brecha es uniforme si y solo si la pérdida logarítmica acumulada entre escalas está acotada | Identidad exacta |
| Cierre por el borde (PR-06) | Si el flujo de correlación que sale por el borde de una ventana es menor que uno, las correlaciones decaen exponencialmente | Teorema en Ising, con el lema de Simon–Lieb citado |
| Del decaimiento a la brecha (YM-R3B) | Un decaimiento exponencial común de los correladores gauge-invariantes da una brecha espectral | Teorema espectral, ya en la rama Yang–Mills; requiere positividad de reflexión |
| Desigualdad de borde para gauge | Una cota del tipo Simon–Lieb para lazos gauge | Abierto. Primer caso natural: Z₂, donde valen las desigualdades de Griffiths; para SU(2) no se conoce un análogo |
| Continuo | Que el control valga uniformemente en unidades físicas al retirar la red | Abierto |

La ruta siguiente es formular el flujo por el borde para la teoría de gauge Z₂, comprobar si cierra, e identificar qué parte del mecanismo sobrevive o falla al pasar a SU(2).

## 10. Solicitud de revisión

Solicitamos revisión crítica en particular de: (a) la construcción de la familia de acciones a partir de los cuatro principios y el papel de la condición cuadrática; (b) la proposición de la separación 3+1 por la familia de comparaciones ν; (c) la pertinencia de la lectura de la fase común como tiempo; y (d) la viabilidad de una regla de herencia que fije el ángulo de mezcla.

## Material reproducible

Todo lo afirmado se regenera con los paquetes del 26 y 27 de octubre de 2026, en la carpeta `2026-10-27_mas_alla_de_yang_mills` del repositorio [github.com/EndlessMonkeyProyect/programa-geometria-relacional](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional). Cada paquete trae README, script de verificación, resultados y manifiesto SHA-256.

| Paquete | Qué establece | Estatus |
| --- | --- | --- |
| PR-01 | El resto de la unidad se conserva si la proyección respeta la duplicación | Teorema elemental; no informa sobre la brecha |
| PR-02 | Dónde vive la brecha al duplicar: modos heredados frente a nuevos | Lema exacto; controles en grafos |
| PR-03 | Cadena de Ising que crece por volumen: la brecha sobrevive a la interacción | Medición exacta; su argumento de sumabilidad se corrige en PR-04 |
| PR-04 | Criterio correcto: pérdida logarítmica por escala; Ising 2D con y sin brecha | Las medidas estructurales no deciden la brecha |
| PR-05 | Brecha uniforme de Ising 2D a alta temperatura: resolución local contra influencia | Teorema conocido, reproducido; β < 0,3322 |
| PR-06 | Masa positiva por cierre de ventanas: el flujo de correlación por el borde | Teorema con un lema citado; β < 0,4067 |
| PR-07 | De los principios a la familia de acciones, con Wilson como elección particular; separación 3+1 por ν; controles | Respaldo de las secciones 3 a 6 |

## Referencias principales

Wilson (1974); Osterwalder y Seiler (1978); Gross y Wilczek (1973); Politzer (1973); Georgi y Glashow (1974); Glashow (1961), Weinberg (1967), Salam (1968); Elitzur (1975); Simon (1980); Lieb (1980); Duminil-Copin y Tassion (2016); Bałaban (1980s); Fricke–Vogt y Procesi para los invariantes de SU(2).
