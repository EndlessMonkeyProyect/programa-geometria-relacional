---
title: "La unidad autorreferenciada y su radio relacional"
subtitle: "Reflexión, incertidumbre contextual y cierre en sí · Programa de Geometría Relacional"
author: "Le Matt Ansatz Di Ego · Programa de Geometría Relacional"
date: "30 de octubre de 2026"
lang: es-CR
---

# La unidad autorreferenciada y su radio relacional

**Reflexión, incertidumbre contextual y cierre en sí**  
*Reconstrucción ontológica y articulación lógico-matemática para revisión independiente*  
**Le Matt Ansatz Di Ego · Programa de Geometría Relacional · 30 de octubre de 2026**

## Resumen

Una unidad constituye un espacio autorreferenciado definido por el radio de las relaciones que la sostienen. Su incertidumbre es la indefinición de su naturaleza respecto de una referencia y una consulta determinadas, no una entidad adicional. Desde el exterior, una unidad puede ser reconocible sin que todas sus relaciones interiores queden determinadas; desde el interior, mantiene distinciones que pueden adquirir relevancia cuando cambian las relaciones o el marco de comparación. La reflexión manifiesta relaciones entre referencias; la normalización permite compararlas; el cierre en sí expresa la continuidad de una organización autorreferenciada bajo las transformaciones que la definen. Unidades así reconocidas pueden participar en unidades mayores, cada una con su propia referencia y alcance relacional.

Esta formulación recupera la genealogía del Programa de Geometría Relacional y la conecta con realizaciones ya desarrolladas: la congruencia y los normalizadores comunes de R–01; los cocientes y las equivalencias por continuaciones de MF-97/MF-106; las órbitas de la caja de espejos de O59; las firmas de frontera de R5; la novedad circunstancial de R6; y la separación entre indefinición, radio de determinación y certificado de R–04. Se identifican las propiedades matemáticas respaldadas por esos contratos, las interpretaciones del programa y las preguntas adecuadas para una evaluación externa.

**Términos clave:** unidad, autorreferencia, radio relacional, incertidumbre contextual, reflexión, cierre en sí, normalización, interfaz, novedad, ROSI.

## 1. La unidad como punto de partida

**Definición ontológica de trabajo.** Una unidad es un **espacio autorreferenciado cuyo radio determina el alcance de las relaciones que la definen**. La unidad no es el resultado de reunir imágenes por una operación de compresión. Su reconocimiento depende de una relación interna de referencia y de las relaciones que puede sostener con otras unidades.

El **radio relacional** no se introduce como distancia euclidiana obligatoria, superficie material o número universal. Nombra el alcance desde el cual una unidad reconoce y sostiene sus relaciones. Según la realización, ese alcance podrá representarse mediante conjuntos de vínculos, interfaces, recorridos, escalas o una medida numérica definida explícitamente. Por eso el radio pertenece a la caracterización de la unidad, no a un recipiente geométrico añadido desde fuera.

La **incertidumbre** expresa la naturaleza que permanece indefinida para una referencia dada. No equivale automáticamente a una distribución de probabilidad ni a un movimiento aleatorio. Una unidad puede sostener su cierre propio y, aun así, conservar relaciones interiores indeterminadas para una consulta exterior.

La **singularidad**, en el lenguaje del programa, se reconoce desde el marco considerado: desde fuera puede manifestarse como una unidad con propiedades relacionales observables y un interior no determinado por esa referencia; desde dentro hay relaciones que sostienen su propio espacio de comparación. Esta lectura es ontológica. Una singularidad física de relatividad general o de teoría cuántica requiere definiciones y ecuaciones propias.

Esta formulación describe directamente el **espacio de relaciones** y evita convertirlo en una envoltura física, una deformación espacial o una operación de compresión algorítmica.

## 2. Reflexión, referencia e incertidumbre

La **reflexión** relaciona una unidad con sus manifestaciones respecto de una referencia. Dos recorridos que llegan a un mismo foco pueden coincidir para una observación de posición sin coincidir en orientación, procedencia o fase. El foco es una referencia del propio sistema: no hace falta imaginarlo como un observador exterior.

La misma relación puede resultar determinada en un marco e indefinida en otro. Así, «incertidumbre» califica una **relación entre estados compatibles, referencia y consulta**. No debe confundirse con la inexistencia de relaciones en el interior de la unidad.

El orden conceptual que se adopta es:

**Unidad → autorreferencia → radio relacional → incertidumbre contextual → reflexión → normalización → cierre en sí → nuevas relaciones entre unidades.**

Este orden es una **organización del lenguaje del programa**, no una afirmación de dependencia causal única: una unidad puede reflejarse sin que esa reflexión baste para acreditar cierre en sí, y una referencia puede ser suficiente para unas preguntas e insuficiente para otras.

### 2.1. Realización operacional de la incertidumbre

Sea `X` un conjunto de estados, `F ⊆ X` la familia de estados compatibles y `q:F→Y` una consulta. La incertidumbre de la respuesta, en esta realización, corresponde a una imagen `q(F)` con más de un valor. Si `F` no es vacío y `|q(F)|=1`, la consulta está determinada; si `F=∅`, las condiciones son incompatibles. R–04 fija esta distinción para el bit `q_uv(c)=[c(u)=c(v)]` de 3-coloración.

Una segunda propiedad, diferente, es la **insuficiencia de la firma**: dos estados `x,y` pueden compartir una lectura exterior `Φ(x)=Φ(y)` y diferir en una consulta `d(x)≠d(y)`. La incertidumbre de una consulta y la insuficiencia de una firma se relacionan, pero no son sinónimos.

## 3. El radio y el cierre en sí: contrato de reconocimiento

La definición ontológica identifica el radio como determinante del espacio autorreferenciado; una realización matemática debe declarar **cómo** se reconoce ese alcance. Una traducción candidata, sin imponerla a todos los laboratorios, consiste en describir la unidad mediante una familia de estados internos `X_U`, relaciones declaradas `R_U`, una referencia interna `Ψ_U` y una colección `T_U` de transformaciones relevantes.

Bajo ese contrato, decimos que la referencia interna es **estable para `T_U`** cuando cada transformación `T∈T_U` induce una actualización bien definida sobre las firmas alcanzables. Formalmente, para cada `T` existe `t` tal que:

`Ψ_U(Tx) = t(Ψ_U(x))`.

Esto ocurre exactamente cuando:

`Ψ_U(x)=Ψ_U(y)  ⇒  Ψ_U(Tx)=Ψ_U(Ty)`.

Es el criterio estándar de descenso al cociente de MF-97, aplicado aquí como **prueba candidata de continuidad bajo transformaciones declaradas**. No identifica por sí solo todos los sentidos posibles de «cierre en sí». Para afirmar ese cierre en una realización concreta deben especificarse la referencia interna, las transformaciones, los observables pertinentes y qué se preserva.

El **radio** de este contrato puede representarse por el soporte relacional que participa en el reconocimiento de `Ψ_U`: no se deduce de ello que tenga un valor real, que sea idéntico a una distancia física o que deba coincidir con una medida combinatoria como `ρ(G)`.

### 3.1. Equivalencia contextual y continuaciones

Sean `Q:X→Y` una consulta y `C` una familia de continuaciones `T_c`. La equivalencia respecto de todas las continuaciones declaradas se expresa mediante:

`x ≡_(Q,C) y  ⇔  Q(T_c x)=Q(T_c y)` para todo `c∈C`.

Si `C` contiene la identidad y es cerrada por composición, las continuaciones descienden al cociente por esta equivalencia. Es un principio conocido de equivalencia observacional, relacionado con Myhill–Nerode. La lectura propia del programa consiste en preguntar qué referencia conserva esas distinciones cuando el marco crece, se mueve o establece nuevos vínculos.

**Existencia, memoria y costo son magnitudes diferentes.** Que exista un cociente o una actualización bien definida no significa que una firma pueda calcularse, almacenarse y consultarse eficientemente.

## 4. Unidades de unidades: composición por relaciones e interfaces

Una unidad puede participar en otra de escala o alcance mayor. La unidad mayor no tiene por qué perder las referencias interiores de sus componentes; establece nuevas relaciones entre ellas y dispone de un radio relacional propio. Una construcción recursiva exige declarar qué información pasa de una unidad a otra y qué continuaciones preserva.

R5 contiene una realización matemática exacta. Para una región de grafo `H` con frontera etiquetada `B`, su firma exterior de 3-coloración es:

`Γ_H(B) = {c|_B : c es una 3-coloración válida de H}`.

Si dos regiones comparten exactamente esa frontera, sus interiores son disjuntos y no se introducen aristas adicionales entre interiores, entonces su unión es 3-coloreable si y solo si:

`Γ_H1(B) ∩ Γ_H2(B) ≠ ∅`.

El resultado reconoce la composición a través de una interfaz **para ese contrato de continuación**. No autoriza a sustituir todo el interior por su firma exterior cuando también se permiten modificaciones internas.

El contraejemplo de R5 lo muestra: en los vértices `a,b,u,v`, la región `A` posee aristas `ab,au,av,bu,bv`, mientras `D` contiene únicamente `ab` y deja `u,v` aislados. Ambas ofrecen las mismas seis asignaciones exteriores de `a,b`. Al incorporar `uv`, `A` se convierte en `K₄` y ya no es 3-coloreable, mientras `D` conserva seis asignaciones de frontera. **La misma manifestación exterior puede corresponder a interiores con respuestas distintas frente a una relación nueva.**

Esta es una realización precisa de la distinción interior/exterior; la recursión general de unidades de unidades requiere una definición adicional de interfaces, composición y operaciones permitidas para cada nivel.

## 5. Novedad circunstancial, normalización y continuidad

La novedad no está determinada únicamente por la incorporación de una relación. Depende de **qué posibilidades distingue o modifica dentro de la circunstancia considerada**. R6 desarrolla esta idea para la familia `P₃(G)` de particiones válidas en exactamente tres clases independientes, sin nombres de color, sobre un conjunto fijo de vértices:

`P₃(G∪H) = P₃(G) ∩ P₃(H)`

`Δ_G(e) = P₃(G) \ P₃(G+e)`.

Si `Δ_G(e)=∅`, la nueva arista es redundante respecto de esa familia de soluciones; si no, elimina distinciones anteriormente compatibles. La cardinalidad sola no identifica cuáles son las posibilidades: en cinco vértices, dos grafos con una arista distinta pueden admitir 19 particiones cada uno y responder de modo diferente a una misma incorporación, con resultados 19 y 14. Una referencia debe conservar la **familia pertinente**, no solamente su cantidad.

En R–01 aparece la continuidad por una referencia común. Si `Φ_N(x)=x mod N` y se incorpora `d_p(x)=x mod p`, con `p` primo y `mcd(N,p)=1`, la referencia conjunta es:

`L = mcm(N,p) = Np`.

El teorema chino del resto identifica las clases módulo `L` con pares de clases módulo `N` y `p`. Cada clase anterior se refina en `p` clases; la proyección hacia la anterior sigue definida. Para las fases de un círculo normalizado, `j/N=(pj)/L` es una **inclusión de etiquetas de fase**, distinta de la proyección de residuos `ℤ/Lℤ→ℤ/Nℤ`.

Las actualizaciones afines `F_L([x])=[ax+b]_L` conmutan con las proyecciones correspondientes. Si `mcd(a,L)=1` conservan las distinciones mediante una permutación; con `a=0` pueden colapsarlas aunque el diagrama continúe conmutando. Así, **compatibilidad de referencias y conservación de todas las diferencias no son la misma propiedad**. Esta es una realización aritmética; la aplicación a una dinámica física o a cualquier unidad ontológica requiere un mapa adicional.

## 6. El laboratorio de la caja de espejos

En el modelo unidimensional ideal de O59, dos espejos situados en `0` y `L` actúan como:

`s₀(x)=−x` y `s_L(x)=2L−x`.

Sus composiciones generan posiciones `x↦±x+2kL`, con `k∈ℤ`. La coordenada:

`ρ_L(x)=dist(x,2Lℤ)`

identifica exactamente la órbita bajo esas reflexiones. Para `L=1`, las posiciones `1/4` y `9/4` poseen la misma coordenada `1/4`; si la pared se desplaza hasta `L=2`, sus lecturas son `1/4` y `7/4`. La referencia antigua no basta para actualizar ambas sin información suplementaria.

El encuentro de las imágenes no constituye automáticamente un cierre en sí. La geometría permite demostrar relaciones entre órbitas; para conocer información sobre sentido de propagación, orientación o fase hay que declarar observables adicionales. También importa distinguir **ampliar el grupo de reflexiones**, que puede reunir órbitas, de **ampliar las preguntas**, que puede separar estados antes indistinguibles.

Los grupos de reflexión CME-001–003 agregan ejemplos de cierre finito, repetición y crecimiento abierto, con generadores y objetos contados diferentes. Son referencias geométricas que motivan la investigación del costo; por sí solos no equivalen a algoritmos de 3-coloración.

## 7. Esferas y circuitos: condiciones distintas de cierre

En el laboratorio de esferas, los centros y contactos se estudian como relaciones. Tres centros no alineados determinan un plano; cuatro centros de esferas iguales mutuamente tangentes forman un tetraedro regular; un anillo de cuatro esferas coplanares que conserva únicamente contactos periféricos define otro sistema de relaciones. No son contratos intercambiables.

En el modelo escalar ideal del circuito `C₄`, la regla `s_i+s_j=0` para cada enlace admite el modo `(a,−a,a,−a)`. Si se aplican las mismas igualdades a todas las aristas de `K₄`, el modo no nulo desaparece. La conclusión pertenece a ese sistema algebraico declarado, no a una ley óptica general.

La función de ambos laboratorios consiste en **mostrar qué relaciones sostienen una estructura y cómo cambia su posibilidad de cierre cuando se modifican esas relaciones**. La formalización de una jerarquía física de unidades exige además leyes de interacción y observables de cada escala.

## 8. Radio de determinación, certificado y complejidad

El radio que define ontológicamente una unidad **no se identifica** con el radio de determinación `ρ(G)` de R–04. Este último es una medida particular: el mínimo tamaño de un subgrafo inducido propio, 3-coloreable, en el cual alguna consulta de igualdad o diferencia entre vértices no adyacentes queda determinada.

En las ruedas impares, `ρ(W_r)=4`: un diamante local obliga a igualar las dos puntas y la clausura por diamantes conduce a la incompatibilidad. En las construcciones de Mycielski `M(C_r)`, los radios registrados son:

Los valores exactos **reportados en R–04** son: `ρ(M(C₅))=9` (11 vértices), `ρ(M(C₇))=12` (15 vértices), `ρ(M(C₉))=16` (19 vértices) y `ρ(M(C₁₁))=20` (23 vértices). Estos cuatro valores corresponden a verificaciones finitas, no a una fórmula general.

El patrón `ρ(M(C_r))=2r−2` para `r≥7` impar figura como **conjetura**. Para esta familia existe además una descomposición en camino de ancho a lo sumo 6 y una construcción de refutaciones de resolución de ancho a lo sumo 21 bajo la codificación booleana indicada en la solicitud revisada. Así, una determinación puede requerir reunir gran parte de un grafo y, aun así, admitir un certificado global de ancho acotado.

La consecuencia para la investigación es la separación entre **alcance de una consulta, estructura de un certificado y costo de construir o verificar la respuesta**. R–04 ofrece casos verificables de esa separación, no una cota universal de complejidad.

Para una familia de procedimientos computacionales deben declararse la entrada codificada, estados internos, operaciones de incorporación, lectura, memoria, tiempo y sistema de pruebas al que eventualmente se traduzcan sus corridas. N1-A analiza un motor extensional por tablas; N1-B propone una simulación más específica por resolución cuya constante `3/2·total_candidates` está identificada para auditoría en su documento propio. La eficiencia de una firma y la existencia de un algoritmo de decisión son cuestiones diferentes.

## 9. Otras ramas y reflexión del lenguaje: ROSI

El complemento de Yang–Mills desarrolla un ejemplo de matrices `SU(2)` en que las trazas individuales de dos transportes no fijan necesariamente la traza del producto `UV`. Es una realización algebraica de insuficiencia de observaciones separadas. No debe identificarse directamente con una brecha de masa física.

En Navier–Stokes, las proyecciones por simetrías examinadas en O70/O71 pueden compartir la misma parte proyectada y diferir en términos residuales que afectan su evolución. Se vuelve a preguntar **qué relaciones conserva una referencia y cuáles son necesarias para actualizarla**, sin suponer que el mismo objeto matemático explica todas las ramas.

ROSI se sitúa en el nivel de la **reflexión sobre el propio lenguaje**: debe relacionar cada concepto con su referencia, sus determinantes, su fuente, su prueba y sus límites, e identificar cuándo una palabra cambia de sentido al pasar de una realización a otra. En esta edición identifica especialmente estas diferencias:

- Una unidad autorreferenciada no es simplemente la clase de estados que una firma exterior no distingue.
- El radio constitutivo de una unidad no es necesariamente un radio geométrico o el `ρ(G)` de R–04.
- Una reflexión o encuentro de trayectorias no constituye por sí solo un cierre en sí.
- Una firma suficiente para una consulta exterior puede ser insuficiente para continuaciones interiores.
- Una coordenada nueva de comparación no equivale a una dimensión física nueva.

Estas distinciones conservan el hilo del programa sin sustituir las reglas de los laboratorios por afirmaciones ontológicas automáticas.

## 10. Solicitud de revisión independiente

La pregunta central puede plantearse ahora con mayor fidelidad al programa: **¿qué relaciones y transformaciones permiten que un espacio autorreferenciado, definido por su radio, conserve su continuidad al cambiar de referencia y al participar en unidades mayores?**

La pregunta lógico-matemática complementaria es: **¿qué firmas, interfaces y condiciones de composición preservan exactamente las observaciones y continuaciones declaradas, y cuáles requieren recuperar información interior?**

En complejidad computacional, la instancia concreta pregunta: **¿cuál es el costo de conservar o reconstruir esas distinciones para decidir 3-coloración en familias explícitas de grafos y clases declaradas de procedimientos?**

### Preguntas para quienes revisen

1. ¿Qué definición formal de radio relacional y autorreferencia puede emplearse en cada laboratorio, y qué propiedades identifica sin equiparar modelos diferentes?
2. ¿Qué condiciones adicionales a la factorización por una firma permiten distinguir cierre en sí, simple equivalencia exterior y continuidad de la referencia interna?
3. ¿Es correcta la interpretación de MF-97/MF-106 mediante cocientes, equivalencia observacional y continuaciones? ¿Dónde termina su suficiencia?
4. ¿R5 y R6 permiten caracterizar de forma exacta las interfaces que admiten actualización interior? ¿Qué teoría conocida ofrece la mejor formulación recursiva?
5. ¿Qué propiedades de R–01 sobreviven al cambio de referencia: proyecciones, compatibilidad, invertibilidad y conservación de distinciones?
6. ¿Qué relaciones del cubo y de las esferas son geométricas o algebraicas y cuáles requieren una ley óptica o física adicional?
7. ¿Cómo se relacionan el radio de determinación de R–04, la estructura del certificado y el costo algorítmico en familias que no admiten el cierre local por diamantes?
8. ¿Qué simulaciones por sistemas de pruebas describen realmente los motores de firma propuestos, y qué barreras conocidas se transfieren bajo hipótesis y codificaciones explícitas?

**Alcance.** Esta solicitud reúne una definición ontológica revisada, realizaciones matemáticas con sus hipótesis, resultados finitos reportados y un protocolo de evaluación. Las posibles implicaciones sobre P frente a NP siguen dependiendo de teoremas de complejidad todavía no establecidos por el programa.

## 11. Procedencia de las construcciones

- **Unidad, reflexión, novedad y cierre.** Síntesis integrada del 27-09 y *Hilo ontológico* del 24-10: genealogía del lenguaje.
- **Normalización y múltiplo común.** R–01 (23-10): resultados aritméticos bajo las hipótesis coprimas declaradas.
- **Equivalencia por continuaciones.** MF-97 y MF-106: cocientes y principios estándar de actualización.
- **Espejos y órbitas.** O59 y CME-001–003: fórmulas geométricas con sus generadores y controles.
- **Interior y exterior.** R5 (29-10): firmas de frontera y contraejemplo exacto.
- **Novedad circunstancial.** R6 (29-10): intersección de familias, diferencia y contexto separador.
- **Estados de consulta, radio y certificado.** R–04 (29-10): definiciones, demostraciones particulares y mediciones finitas.
- **Esferas y anillo C₄.** *Imagen Total 3.9* y laboratorio de esferas: modelos geométricos y algebraicos con reglas específicas.
- **Otras realizaciones.** Yang–Mills (R–01) y Navier–Stokes (O70/O71): controles de suficiencia de referencias; puentes físicos sujetos a hipótesis adicionales.
- **Reflexión del lenguaje.** ROSI/ROS-1 y 08_language: auditoría de conceptos, pruebas y determinantes.

**Control documental.** La presente versión conserva las fórmulas y ejemplos de las fuentes identificadas. Se han reformulado las definiciones ontológicas y la terminología editorial; los resultados computacionales históricos se describen como reportados y no se presentan como verificaciones realizadas en esta edición. Las proposiciones generales mantienen sus hipótesis y las conjeturas siguen identificadas como tales.

## Anexo. Registro de cambios de lenguaje y criterio

- **Unidad:** se retira la metáfora de un recipiente de incertidumbre; se formula como espacio autorreferenciado definido por un radio relacional.
- **Encuentro:** la coincidencia de imágenes puede revelar información que una referencia no registra; no se la toma como génesis necesaria de una unidad.
- **Reflexión y operaciones:** se distingue reflexión geométrica de representación, consulta, actualización y normalización computacionales.
- **Radio:** se separa el alcance constitutivo de una unidad de medidas específicas como `ρ(G)`.
- **Incertidumbre:** se interpreta como indefinición relativa a consulta y referencia, sin postular una entidad física adicional.
- **Cierre en sí:** se relaciona con reglas internas de reconocimiento y continuidad declaradas, no con la mera coincidencia de recorridos.

**Repositorio del programa:** https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
