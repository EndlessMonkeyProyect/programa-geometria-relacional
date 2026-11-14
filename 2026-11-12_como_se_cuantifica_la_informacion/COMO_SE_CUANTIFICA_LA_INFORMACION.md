---
title: "¿Cómo se cuantifica la información de un sistema?"
subtitle: "De la indefinición a la referencia, el cierre propio y la economía del cálculo"
author: "Le Matt Ansatz Di Ego"
date: "12 de noviembre de 2026"
lang: es
---

**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program

**Documento de formalización integrada · Versión de trabajo 1.0 · Borrador para revisión independiente**  
**Ámbito:** hilo de información, laboratorios de paridad y restricción, continuidad, economía y puente con P frente a NP.  
**Criterio:** distinguir significado ontológico, definición de realización, resultado matemático, medición experimental y problema abierto.

# Resumen

Este documento ordena una ruta del Programa de Geometría Relacional: unidad e indefinición; reflexión y diferencia; comparación y distinción; referencia, determinante y relaciones; herencia, comunes y cierre propio; cuantificación de la información; y, finalmente, evaluación de economía bajo preguntas y procedimientos definidos.

La tesis metodológica distingue cuatro preguntas: **contar distinciones, reconstruir relaciones, conservar respuestas y comparar recursos**. Cada realización matemática declara su consulta y sus operaciones. La medida de Hartley, la entropía de Shannon, el rango de un grafo, la continuidad de una firma y el costo de una consulta ofrecen instrumentos específicos para esas preguntas.

Se demuestran dos resultados generales para grafos: el rango de las diferencias binarias es $`n-c`$ y, bajo la ecuación real $`s_u+s_v=0`$, la dimensión de soluciones es el número de componentes bipartitas. Se reproducen exhaustivamente $`1.099`$ casos de grafos simples etiquetados de uno a cinco vértices y el ensayo de cinco estados ($`336`$ continuaciones de confirmación y $`1.344`$ de revisión de una referencia anticipada). Se reformula un ejemplo de economía del tetraedro con **dos modelos de operaciones**: el umbral de conveniencia depende de la unidad de costo elegida. E9 y el caso de paridad con cláusulas OR se presentan con alcance delimitado.

# 1. Alcance, procedencia y estados

El texto formaliza el hilo desarrollado hasta el 12 de noviembre de 2026 y lo contrasta con *Imagen Total 3.9* (23 de octubre de 2026) y *¿Dónde se ahorra el cálculo?*, solicitud de revisión v2 (8 de noviembre de 2026). Identifica los resultados recalculados aquí y cita por separado los experimentos comunicados en documentos anteriores.

Para evitar afirmaciones de alcance impreciso, cada tramo distingue:

| Estado | Qué significa en este documento |
|:---|:---|
| Ontología | Significado y función conceptual del programa. |
| Definición | Contrato exacto: objetos, referencias, operaciones, consultas y supuestos. |
| Teorema | Proposición con demostración y dominio de validez. |
| Comprobación | Conteo o ensayo repetido en esta formalización. |
| Resultado previo | Dato de otro laboratorio citado, sin afirmar aquí su reproducción. |
| Puente propuesto | Correspondencia que requiere un mapa matemático adicional. |
| Abierto | Pregunta cuya respuesta general no se ha demostrado. |

La auditoría ROSI / ROS-1 Lite puede registrar estos estados y señalar cuándo un argumento convierte, sin justificación, una definición en teorema o una analogía en equivalencia. La clasificación es una metodología de control; no reemplaza pruebas.

# 2. Continuidad del lenguaje ontológico

## 2.1. La secuencia generativa

La **unidad inicial** designa una totalidad sin diferencias acreditadas y sin una posición exterior desde la cual observarla. La **indefinición** expresa lo que aún no queda determinado por las relaciones disponibles; no implica por sí sola una distribución aleatoria. La **reflexión** introduce la posibilidad de comparación dentro de ese espacio único. Una diferencia posible adquiere carácter de **distinción** cuando la comparación la acredita.

La ruta puede representarse en el orden siguiente:

> Unidad → indefinición → reflexión → diferencia → comparación → distinción acreditada → relaciones → cierre propio → nueva referencia y nueva comparación.

Este orden es un hilo ontológico, no una afirmación de que todo sistema concreto deba atravesar una sucesión cronológica idéntica. La **singularidad relacional** nombra una identidad sostenida por su propio cierre respecto de las continuaciones pertinentes. Una realización dinámica debe demostrar qué persiste y frente a qué transformaciones.

## 2.2. Distinciones léxicas que no deben colapsar

| Término | Función y límite de uso |
|:---|:---|
| Referencia | Organización desde la cual una comparación obtiene una respuesta. |
| Foco | Relación o posición interna donde se reconoce una lectura; no un observador externo presupuesto. |
| Determinante | Condición cuya variación cambia una distinción o respuesta en el contrato elegido. |
| Comunes | Relaciones simultáneas o compartidas; no demuestran por sí solas ascendencia. |
| Herencia | Procedencia lógica, temporal o constructiva demostrable de una relación. |
| Novedad | Distinción adicional respecto de lo que una firma anterior permitía reconocer. |
| Conservación | Permanencia de una distinción o respuesta válida bajo cambios o continuaciones declarados. |
| Cierre propio | Capacidad de una organización de sostener su identidad y responder desde sus relaciones. |
| Información | Diferencias reconocibles y recuperables bajo referencias y operaciones declaradas. |
| Economía | Comparación de recursos entre procedimientos que responden la misma pregunta. |

**Corrección de lenguaje.** «Conservada» no significa «almacenada en memoria». Registrar los seis valores de una tabla es una decisión de representación. Conservar una respuesta significa que, tras una transformación de referencia o una continuación admitida, se puede seguir acreditando la respuesta requerida. Tampoco se emplea «trabajo» como magnitud autónoma: cuando corresponda medir cálculo se especifican lecturas, escrituras, XOR, tiempo, memoria u otras operaciones y sus unidades.

**Principio de continuidad:** *lo resuelto no se des-resuelve*. Una pregunta más fina puede dividir clases que antes eran indistinguibles, sin invalidar las respuestas que eran correctas para el contrato original. Sí hay pérdida cuando una nueva representación impide recuperar una respuesta ya exigida.

## 2.3. Economía del lenguaje

El lenguaje participa en el mecanismo: una palabra delimita una distinción. Una expresión nueva se justifica cuando identifica una operación, separa casos antes confundidos, conserva una respuesta necesaria o permite una predicción contrastable. Cambiar «herencia» por «comunes», o «conservación» por «almacenamiento», puede borrar diferencias que el programa ya había reconocido. Antes de medir, debe fijarse **qué se relaciona, desde qué referencia, bajo qué determinante y con qué pregunta**.

# 3. Contrato matemático de una realización

Sea un sistema finito o efectivamente representable con los siguientes elementos:

- $`X`$: estados posibles de la realización.
- $`K\subseteq X`$: estados compatibles con las condiciones declaradas, con $`K\neq\varnothing`$ cuando se usa un logaritmo de conteo.
- $`Q`$: familia de consultas $`q:X\to Y_q`$.
- $`\Phi:X\to Z`$: firma o referencia operacional que reúne estados con una misma lectura.
- $`\mathcal{F}`$: transformaciones o continuaciones admitidas.
- $`\mathcal{M}`$: procedimientos permitidos para construir, actualizar, consultar y verificar representaciones.
- $`C_{\mathcal M}`$: recursos declarados para comparar procedimientos del mismo contrato.

Dos estados son indistinguibles por la firma si $`x\sim_{\Phi}y`$ exactamente cuando $`\Phi(x)=\Phi(y)`$. Para una familia de consultas, $`x\sim_Q y`$ cuando toda consulta produce la misma respuesta en ambos estados. Estas equivalencias dependen de la referencia y de la pregunta, no solo del nombre de los objetos.

## 3.1. Derivación y novedad: primer criterio exacto

**Proposición 1 (recuperabilidad de una consulta).** Una pregunta $`q:X\to Y`$ puede responderse solo desde la firma $`\Phi`$ si y solo si existe $`g`$ tal que

```math
q=g\circ\Phi.
```

Equivale a exigir que $`q`$ sea constante en cada clase de $`\sim_\Phi`$.

**Prueba.** Si $`q=g\circ\Phi`$, igual firma implica igual respuesta. En sentido inverso, cuando $`q`$ es constante en cada fibra se define $`g(z)=q(x)`$ para cualquier $`x`$ cuya firma sea $`z`$; el valor no depende del representante. $`\square`$

Un **testigo de novedad** es una pareja $`x,y`$ para la cual $`\Phi(x)=\Phi(y)`$ pero $`q(x)\ne q(y)`$. La ampliación $`(\Phi,q)`$ divide por lo menos una clase. No se sigue que divida todas las clases; esa extensión requiere otra hipótesis.

## 3.2. Continuidad de una representación

**Proposición 2 (actualización autónoma).** Dada $`F:X\to X`$, existe una transformación de firmas $`\widehat F`$ con

```math
\Phi\circ F=\widehat F\circ\Phi
```

si y solo si

```math
\Phi(x)=\Phi(y)\ \Longrightarrow\ \Phi(Fx)=\Phi(Fy).
```

La condición permite que estados representados por la misma firma sigan produciendo una única firma después de continuar. La demostración utiliza el mismo criterio de independencia respecto del representante que la Proposición 1. Es una realización operativa de continuidad; **no define por sí sola el cierre propio ontológico**.

## 3.3. Conservación al cambiar de referencia

Si se reemplaza $`\Phi`$ por $`\Psi`$, una consulta anterior $`q`$ permanece recuperable exactamente cuando existe $`h`$ con $`q=h\circ\Psi`$. Por tanto, un cambio de referencia puede ser válido para ciertas preguntas y borrar otras. Si las continuaciones son parte de la tarea, se exige la misma recuperabilidad para las consultas después de cada continuación relevante.

Para un conjunto de continuaciones $`T_c`$, la equivalencia pertinente puede definirse por

```math
x\equiv_{Q,\mathcal C} y\ \Longleftrightarrow\ q(T_cx)=q(T_cy)\quad\text{para todo }q\in Q,\ c\in\mathcal C.
```

Esta forma tiene una correspondencia precisa con la equivalencia por continuaciones de Myhill–Nerode cuando $`X`$ son historias, las continuaciones son sufijos y $`q`$ es aceptación. La correspondencia no identifica automáticamente los distintos significados ontológicos.

# 4. Cuantificar posibilidades, distinciones y probabilidades

## 4.1. Medida de posibilidades (Hartley)

Para un conjunto finito no vacío de configuraciones compatibles $`K`$:

```math
H_0(K)=\log_2|K|.
```

Esta magnitud mide el logaritmo del número de posibilidades. La longitud mínima de un código binario fijo que permita nombrarlas es $`\lceil\log_2|K|\rceil`$ bits. No establece probabilidades ni equivale, sin más, a indefinición ontológica.

## 4.2. Resolución de una referencia

Si $`\Phi`$ permite reconocer $`r`$ clases diferentes en un conjunto $`K`$, definimos

```math
D_\Phi(K)=\log_2|\Phi(K)|.
```

Así, contar posibilidades admisibles y contar distinciones reconocibles son operaciones distintas. En general, $`|\Phi(K)|\le |K|`$ y $`D_\Phi(K)\le H_0(K)`$. La desigualdad se refiere a un mismo dominio y una firma determinista.

## 4.3. Entropía de Shannon

Si, además, se declara una probabilidad $`p(x)`$ en $`K`$, la entropía de Shannon es

```math
H(X)=-\sum_{x\in K}p(x)\log_2p(x).
```

Para una firma determinista $`B=\Phi(X)`$ se cumple la identidad

```math
H(X)=H(B)+H(X\mid B).
```

Si la distribución es uniforme sobre $`K`$, $`H(X)=H_0(K)`$. En ausencia de esa hipótesis, no debemos llamar «entropía de Shannon» al simple logaritmo del número de configuraciones. El residuo $`H(X\mid B)`$ expresa incertidumbre probabilística condicionada, y no debe confundirse con el costo de una reconstrucción.

# 5. Primer laboratorio: cuadrado y tetraedro bajo paridad

Consideramos cuatro vértices etiquetados $`A,B,C,D`$, con estados $`s_v\in\mathbb F_2`$, y una relación en cada arista:

```math
b_{uv}=s_u\oplus s_v.
```

En el cuadrado $`C_4`$ las aristas son $`AB,BC,CD,DA`$. En el tetraedro $`K_4`$ se incorporan, además, $`AC`$ y $`BD`$. Los dos grafos son conexos y usan la **misma ley de paridad**.

Una firma independiente conveniente es $`(b_{AB},b_{BC},b_{CD})`$. Entonces:

```math
b_{AC}=b_{AB}\oplus b_{BC},\qquad b_{BD}=b_{BC}\oplus b_{CD},
```

```math
b_{DA}=b_{AB}\oplus b_{BC}\oplus b_{CD}.
```

La inversión simultánea $`s_v\mapsto s_v\oplus1`$ para los cuatro vértices no cambia ningún vínculo. De las $`2^4=16`$ asignaciones de vértices se obtienen exactamente ocho patrones de paridad. Por eso, bajo estas consultas, ambos grafos contienen tres bits de diferencias independientes. Para recuperar un estado absoluto, por ejemplo $`s_A`$, se requiere además una distinción binaria.

| Magnitud | Cuadrado $`C_4`$ | Tetraedro $`K_4`$ |
|:---|---:|---:|
| Vértices | 4 | 4 |
| Vínculos | 4 | 6 |
| Vínculos independientes | 3 | 3 |
| Vínculos derivados | 1 | 3 |
| Asignaciones de vértices | 16 | 16 |
| Patrones distinguibles de paridad | 8 | 8 |
| Información independiente | 3 bits | 3 bits |

**Resultado demostrado.** Igual dimensión de diferencias independientes no implica igual número de vínculos, igual organización ni igual demanda de operaciones para consultas concretas.

## 5.1. Teorema general para grafos de paridad

**Teorema 1.** Sea $`G=(V,E)`$ un grafo no dirigido con $`n`$ vértices y $`c`$ componentes conectadas, incluidos vértices aislados. Para las diferencias de paridad sobre $`\mathbb F_2`$:

```math
\operatorname{rango}(G)=n-c,\qquad |\Phi_G(\mathbb F_2^n)|=2^{n-c},\qquad D_G=n-c\text{ bits}.
```

**Demostración.** La aplicación que envía los estados de vértice a los vínculos tiene como núcleo las asignaciones constantes en cada componente: es posible invertir todos los vértices de una componente sin cambiar sus aristas, y no hay más libertades dentro de una componente conexa. Su núcleo posee $`2^c`$ elementos. Por rango–nulidad, la dimensión de la imagen es $`n-c`$ y su cardinal es $`2^{n-c}`$. De modo equivalente, los vínculos de un bosque generador son independientes y generan por XOR los restantes. $`\square`$

El resultado coincide con el rango clásico de la matriz de incidencia sobre $`\mathbb F_2`$. La contribución de este hilo es su uso como **control de las distinciones, las preguntas y la economía**, no presentarlo como un teorema nuevo.

# 6. Segundo laboratorio: la ley escalar cambia el determinante

Ahora no cambiamos los cuatro vértices; cambiamos **la ley de relación**. Exigimos, para cada arista,

```math
s_u+s_v=0,\qquad s_v\in\mathbb R.
```

Para $`C_4`$ existen las soluciones $`(a,-a,a,-a)`$, con $`a\in\mathbb R`$. En $`K_4`$, los triángulos obligan a $`a=-a`$, por lo que $`a=0`$ en los reales.

**Teorema 2.** Sea $`G`$ un grafo no dirigido. El espacio real de soluciones de $`s_u+s_v=0`$ sobre todas las aristas tiene dimensión

```math
\dim\operatorname{Sol}_{\mathbb R}(G)=\beta(G),
```

donde $`\beta(G)`$ es el número de componentes conectadas bipartitas, contando vértices aislados.

**Demostración.** En una componente bipartita, elegir el valor $`a`$ de un vértice determina todos los demás por alternancia de signo y genera una dimensión. En una componente que contiene ciclo impar, la alternancia exige $`a=-a`$; sobre $`\mathbb R`$ esto impone $`a=0`$, y toda la componente queda determinada en cero. Las componentes son independientes entre sí. $`\square`$

**Alcance.** El cuerpo de escalares importa: en característica dos, $`-a=a`$ y la conclusión cambia. Los dos teoremas de este documento no compiten: el primero tiene estados binarios y consulta diferencias XOR; el segundo tiene variables reales y exige una ecuación diferente. **El determinante no es solo cuántas relaciones hay, sino qué ley se les exige.**

# 7. Tercer laboratorio: cinco configuraciones entre ocho

Sea $`X=\mathbb F_2^3`$, con ocho puntos. Comenzamos declarando incompatibles tres puntos distintos; quedan cinco configuraciones admisibles $`K`$. En el espacio afín de dimensión tres existen catorce planos afines de cuatro puntos. Cada conjunto de cinco puntos contiene **exactamente uno** de esos planos y un punto adicional.

La propiedad se demuestra sin inspección manual: hay $`\binom{8}{5}=56`$ conjuntos de cinco puntos y $`14\times4=56`$ pares (plano, punto exterior). Dos planos distintos tienen unión de al menos seis puntos, por lo que no caben dos planos en un mismo conjunto de cinco. Esos 56 pares describen, por tanto, los 56 conjuntos de cinco.

Existen $`8\cdot7\cdot6=336`$ ternas ordenadas de exclusiones. Cada terna deja cinco puntos y admite cinco elecciones para una cuarta exclusión: una elimina el punto residual y deja el plano; las otras cuatro dejan un subconjunto de cuatro puntos que no es un plano afín.

| Etapa | Configuraciones compatibles | $`H_0=\log_2\lvert K\rvert`$ |
|:---|---:|---:|
| Inicio | 8 | 3 bits |
| Después de tres exclusiones | 5 | 2,321928 bits |
| Después de la cuarta | 4 | 2 bits |

Las $`336\times5=1.680`$ continuaciones se dividen en **336** que confirman el plano anticipado y **1.344** que obligan a revisar esa interpretación. Las diferencias de conteo son $`\log_2(8/5)\approx0,678072`$ y $`\log_2(5/4)\approx0,321928`$ bits, respectivamente.

**Distinción decisiva.** El reconocimiento de un plano en cinco puntos no significa que la cuarta exclusión esté determinada; la nueva condición puede confirmar o refutar la expectativa. «Revisión de referencia» no significa que una exclusión reintroduzca estados compatibles. Una lectura ontológica sobre cierre o reapertura es una correspondencia propuesta, no un teorema derivado únicamente del conteo.

# 8. Economía del tetraedro: declarar primero las operaciones

Para conectar el laboratorio de paridad con economía, fijamos una consulta y una continuación.

- **Consulta:** responder el valor del vínculo $`AC`$.
- **Continuación:** invertir el estado de $`A`$.
- **Tabla completa:** registrar los seis valores de paridad de $`K_4`$.
- **Firma reducida:** registrar solo $`AB,BC,CD`$; responder $`AC=AB\oplus BC`$.
- **Requisito común:** responder exactamente lo mismo para cualquiera de las $`16`$ asignaciones de vértices y después de cualquier sucesión de inversiones de $`A`$.

El cambio de $`A`$ modifica $`AB,AC,AD`$ en la tabla completa; en la firma reducida modifica solo $`AB`$. Esta es una afirmación sobre las relaciones de paridad. Para hablar de economía, además, debemos decir qué operación se cobra y qué no se cobra.

## 8.1. Modelo A: inversión atómica de un bit registrado

Se cuentan como operaciones elementales: **invertir un bit registrado**, **leer un bit** y **realizar XOR sobre dos valores leídos**; cada una vale una unidad. No se contabiliza la construcción inicial de ninguna representación. La consulta en la tabla completa requiere una lectura; en la reducida, dos lecturas y un XOR.

| Operación | Tabla completa | Firma reducida |
|:---|---:|---:|
| Bits registrados | 6 | 3 |
| Por inversión de $`A`$ | 3 unidades | 1 unidad |
| Por consulta $`AC`$ | 1 unidad | 3 unidades |

Si hay $`U`$ inversiones de $`A`$ y $`Q`$ consultas $`AC`$, entonces

```math
C_A^{\mathrm{completa}}=3U+Q,\qquad C_A^{\mathrm{reducida}}=U+3Q.
```

La firma reducida requiere menos operaciones exactamente cuando $`U>Q`$; ambas empatan si $`U=Q`$. No significa que una tenga siempre menor costo.

## 8.2. Modelo B: lecturas, XOR y escrituras por separado

Si invertir un valor registrado **no** es una primitiva, sino que requiere una lectura, un XOR con 1 y una escritura, cada vínculo actualizado cuesta tres unidades. La consulta mantiene los mismos costos de una o tres unidades.

```math
C_B^{\mathrm{completa}}=9U+Q,\qquad C_B^{\mathrm{reducida}}=3U+3Q.
```

En este segundo modelo la firma reducida es más económica cuando $`Q<3U`$. La desigualdad cambió porque **cambiamos el contrato de operaciones**, sin modificar ni el tetraedro ni la información distinguible.

**Corrección respecto de una formulación anterior del hilo.** La tabla $`3U+Q`$ frente a $`U+3Q`$ no puede justificarse afirmando simultáneamente que cada lectura, escritura y XOR se cobra individualmente. Requiere declarar la inversión atómica. La formulación actual mantiene separados ambos contratos y sus conclusiones. Costos iniciales, accesos a memoria, instrucciones reales y mezclas de otras consultas producirían comparaciones diferentes.

## 8.3. Qué queda demostrado

Hay tres afirmaciones independientes: (i) tres vínculos determinan los seis por paridad; (ii) el cambio de $`A`$ conserva la ley de paridad y admite actualización de las dos representaciones; y (iii) bajo costos y frecuencias declarados, una puede utilizar menos recursos que otra. Ninguna implica por sí sola las otras. En particular, **almacenar no define conservación** y **derivar no demuestra ahorro**.

# 9. Contraste E9: representación y conteo no son el mismo recurso

En el experimento E9, según el informe de economía del cálculo del 8 de noviembre de 2026, se mantiene la misma función con **6.561** soluciones y se modifica el orden de las variables. El rango máximo de las matrices de corte pasa de **256** a **2**. La razón entre los valores es $`256/2=128`$.

Lo acreditado por la fuente previa es una diferencia de rango máximo para las representaciones estudiadas. **No** es una demostración automática de una aceleración de tiempo por factor 128, ni autoriza confundir rango de corte, número de nodos, tamaño de memoria y costo de construcción. El ejemplo ilustra que la referencia elegida afecta una magnitud de representación sin cambiar la función contada.

El mismo informe documenta otro control: para una rejilla de tres colores de ancho diez, $`1.536`$ columnas posibles se reúnen en $`136`$ órbitas de simetría y la sucesión de conteos admite una representación lineal mínima de dimensión $`51`$. Se citan como **resultados previos declarados**; esta formalización no reejecuta aquí los experimentos E9 ni E5.

# 10. De la referencia explícita al problema de reconocerla

El siguiente paso del programa compara una organización conocida con una representación cuya ley puede no estar visible. En el tetraedro, la paridad es explícita y se demuestra inmediatamente la derivación. En una fórmula arbitraria, identificar una representación alternativa exacta requiere un procedimiento adicional y una verificación de equivalencia.

## 10.1. Caso parametrizado: paridad más cláusulas OR

Consideremos $`n`$ variables binarias, un sistema consistente $`Ax=b`$ sobre $`\mathbb F_2`$ de rango $`r`$ y $`k`$ cláusulas OR adicionales. La parte afín tiene $`2^{n-r}`$ soluciones. Para contar cuántas satisfacen todas las cláusulas puede emplearse inclusión–exclusión: para cada subconjunto de cláusulas se impone que esas cláusulas sean falsas y se cuenta la intersección mediante álgebra lineal.

Cada cláusula OR falsa equivale a fijar en falso cada uno de sus literales (valor 0 para un literal positivo y 1 para uno negativo); esto añade igualdades de variables y, si se agrupan, posibles contradicciones. En consecuencia, se resuelven a lo sumo $`2^k`$ sistemas lineales, cada uno en tiempo polinómico en el tamaño de la entrada bajo un modelo usual de operaciones de bits.

Para los parámetros del ensayo mencionado en el diálogo ($`n=96`$, $`r=81`$, $`k=8`$), la parte afín conserva $`96-81=15`$ grados de libertad y el procedimiento utiliza **a lo sumo 256 sistemas lineales**. No se atribuye aquí un número final de soluciones, porque no se incorporaron las matrices y cláusulas de esa instancia a este documento.

El procedimiento da una cota de la forma

```math
T(n,m,k)=2^k\,\operatorname{poly}(n,m,L),
```

donde $`L`$ representa la longitud total de las restricciones. Es polinómico **si $`k`$ permanece acotado**, pero en general es exponencial en $`k`$. No resuelve 3-SAT arbitrario ni establece $`P=NP`$ o $`P\ne NP`$.

## 10.2. La pregunta pendiente sobre reconocimiento

**Pregunta abierta del programa.** Para una familia declarada de restricciones, ¿cuándo existe una referencia exacta cuya estructura permita responder consultas con menos recursos totales que los procedimientos de comparación, y cuánto requiere reconocer, construir y verificar esa referencia?

La existencia matemática de una firma pequeña no implica que podamos encontrarla de manera eficiente. Tampoco implica que una consulta se responda eficientemente desde ella. La economía debe incluir: reconocimiento, construcción, comprobación de validez, almacenamiento, actualización, consulta y reconstrucción cuando sea necesaria.

El estudio del cubo de espejos introduce la intuición de cambios de referencia que reúnen o separan imágenes; la pared móvil sirve para preguntar qué varía sin cambiar el objeto. En las esferas, distancia y umbral proporcionan determinantes observacionales. Estas son **imágenes de investigación**: para trasladarlas a complejidad se debe definir una firma computable, una transformación, consultas, pruebas de exactitud y un modelo de costo. No hay un teorema de complejidad por la analogía óptica sola.

# 11. Puentes con teorías existentes y sus límites

**Hartley.** $`\log_2|K|`$ es la medida logarítmica de posibilidades; ayuda a cuantificar una realización finita sin volver probabilística la indefinición ontológica.

**Shannon.** La entropía y la entropía condicionada miden incertidumbre probabilística bajo una distribución dada; no miden por sí mismas la complejidad temporal de decidir una pregunta.

**Álgebra lineal y teoría de grafos.** Los rangos de incidencia y las dimensiones de solución constituyen teoremas clásicos que sirven de laboratorios de contraste para determinar el efecto de la ley elegida.

**Myhill–Nerode.** La equivalencia por continuaciones expresa cuándo dos historias admiten la misma respuesta en todos los futuros declarados. Es una correspondencia operativa con la continuidad de una referencia; no sustituye el cierre propio.

**Estadísticas suficientes.** En inferencia estadística, la suficiencia exige un contrato probabilístico y parámetros. Una firma suficiente para preguntas deterministas puede ser un concepto análogo, pero sus requisitos no son idénticos.

**Complejidad de Kolmogórov.** Longitud mínima de descripción de una cadena particular y dimensión de una familia de patrones son medidas diferentes. Tampoco equivalen automáticamente a tiempo de cálculo.

**Yang–Mills y otras teorías físicas.** El programa posee investigaciones paralelas sobre reflejos, holonomías y observables. Su conexión con las medidas de este documento requiere identificar un espacio de estados, una familia de operaciones y un observable común, y demostrar la correspondencia. Aquí se deja señalada como **ruta futura**, no como derivación establecida.

# 12. Protocolo de contraste y documentación reproducible

Para cada nuevo laboratorio debe registrarse, en este orden:

1. La pregunta; el dominio y las configuraciones admisibles.
2. La referencia, el foco, el determinante y la ley exigida entre las relaciones.
3. Las consultas y continuaciones que deben poder responderse.
4. La firma propuesta y el criterio de recuperabilidad de respuestas.
5. El resultado matemático, con hipótesis, prueba y posibles contraejemplos.
6. Las magnitudes medidas y sus unidades: clases, bits, rango, operaciones, tiempo o memoria.
7. El contrato de costo, los procedimientos comparados y los costos de construir/verificar la referencia.
8. La reproducción experimental y la procedencia exacta de cada dato.
9. El estado epistemológico: resuelto, condicionado, propuesto, abierto o refutado.

En esta versión se ejecutó una comprobación exhaustiva de las fórmulas de paridad para todos los grafos simples etiquetados de uno a cinco vértices: **1 + 2 + 8 + 64 + 1.024 = 1.099 grafos**. En cada caso, el número de firmas distintas por enumeración de estados coincidió con $`2^{n-c}`$.

Para el laboratorio de cinco estados se verificaron los 56 subconjuntos de cinco puntos de $`\mathbb F_2^3`$, sus 14 planos afines y todas las 1.680 continuaciones ordenadas: 336 coincidencias con el plano y 1.344 restantes. Las dimensiones escalares de $`C_4`$ y $`K_4`$ también se contrastaron mediante la bipartición de sus componentes. Estas comprobaciones apoyan las pruebas matemáticas; no las sustituyen. El archivo `verificar_cuantificacion.py`, en esta misma carpeta, las reproduce con aritmética exacta, extiende el contraste de la ley escalar a los 1.099 grafos y comprueba además los modelos de costo de la sección 8 y el procedimiento de inclusión–exclusión del anexo A.5 frente a enumeración directa.

# 13. Auditoría de afirmaciones y obligaciones abiertas

| Afirmación | Estado | Evidencia u obligación |
|:---|:---|:---|
| Recuperabilidad $`q=g\circ\Phi`$ | Teorema clásico, demostrado aquí | Constancia sobre fibras. |
| Continuidad $`\Phi F=\widehat F\Phi`$ | Teorema clásico, demostrado aquí | Congruencia de firmas ante $`F`$. |
| Rango binario $`n-c`$ | Teorema clásico, demostrado y contrastado | 1.099 grafos de hasta cinco vértices. |
| Dimensión escalar $`\beta(G)`$ sobre $`\mathbb R`$ | Teorema, demostrado aquí | Bipartición y ciclos impares. |
| Conteo 336/1.344 para cinco estados | Demostrado y comprobado | Enumeración finita y argumento combinatorio. |
| Umbrales del costo en $`K_4`$ | Demostrados dentro de cada contrato | Modelo A y modelo B distintos. |
| E9: 6.561; rango 256→2 | Resultado previo | Incorporar matriz, código y registro al expediente de este documento. |
| Caso 96 variables, rango 81, 8 OR | Caso parametrizado | Cota general $`2^k\operatorname{poly}`$; faltan datos de instancia para reproducir el conteo. |
| Compresión universal de fórmulas arbitrarias | Abierto | Dar algoritmo, cota global y prueba, o límite/contraejemplo. |
| Identificación con cierre óptico o físico | Puente propuesto | Definir mapa entre operaciones y observables; contrastarlo. |

**Precaución sobre P frente a NP.** Ninguna de estas proposiciones constituye una solución del problema general. El aporte aquí es una formulación de obligaciones de prueba, comparaciones controladas y distinciones de lenguaje.

# 14. Conclusión: qué caracteriza a una organización

Los laboratorios permiten responder parcialmente a la pregunta que condujo esta formalización: **qué determina la información independiente, qué permite continuar una identidad y qué determina la economía de operar con ella**.

La información distinguible se fija solo después de elegir estados, ley, referencia y consultas. Para grafos binarios de paridad, la conectividad determina exactamente $`n-c`$ bits; para el sistema escalar real, la bipartición determina la dimensión de soluciones. La continuidad de una firma exige demostrar que sus clases siguen dando respuestas definidas bajo las transformaciones admitidas. La economía depende de la tarea y del contrato de operaciones, y no procede automáticamente de la reducción del número de relaciones.

La ruta metodológica queda abierta, pero controlada: **una relación acreditada habilita nuevas comparaciones; una nueva comparación debe decir qué distingue; y una afirmación de economía debe probar su ventaja sin borrar las respuestas que el contrato exige**. Esa continuidad del significado es parte de la construcción del programa, no solo una elección editorial.

---

# Anexo A. Demostraciones y comprobaciones condensadas

**A.1. Rango de paridad.** En cada componente hay exactamente dos asignaciones de vértices compatibles con un patrón dado, relacionadas por inversión global. Con $`c`$ componentes hay $`2^c`$ preimágenes. Las $`2^n`$ asignaciones de vértices se distribuyen en $`2^{n-c}`$ patrones, y la dimensión es $`n-c`$.

**A.2. Soluciones escalares.** La relación en una arista obliga a invertir el signo. La consistencia alrededor de un ciclo par es automática; un ciclo impar exige $`a=-a`$ y, sobre $`\mathbb R`$, $`a=0`$. Cada componente bipartita aporta un parámetro.

**A.3. Cinco estados.** Hay siete formas lineales no nulas sobre $`\mathbb F_2^3`$ y dos fibras por forma, es decir, 14 planos afines. Cada plano tiene cuatro puntos fuera de él. Por unicidad del plano dentro de un conjunto de cinco, los 56 pares plano–punto exterior corresponden a los 56 subconjuntos de cinco puntos. En cada uno solo el punto exterior puede eliminarse para dejar el plano.

**A.4. Verificación de costos.** En el modelo A, restar costos da $`C_A^{\mathrm{completa}}-C_A^{\mathrm{reducida}}=2(U-Q)`$; en el modelo B, $`C_B^{\mathrm{completa}}-C_B^{\mathrm{reducida}}=2(3U-Q)`$. La señal de la diferencia define cuál procedimiento requiere menos unidades bajo el contrato correspondiente.

**A.5. Inclusión–exclusión.** Si $`V_j`$ es el conjunto de asignaciones afines que viola la cláusula $`j`$, las soluciones de $`Ax=b`$ que satisfacen todas las cláusulas se cuentan por $`\sum_{S\subseteq[k]}(-1)^{|S|}|\bigcap_{j\in S}V_j|`$. Cada intersección se describe por ecuaciones de paridad más fijaciones de variables y se resuelve por eliminación de Gauss.

# Anexo B. Fuentes y trazabilidad

**Fuentes internas consultadas para esta versión:**

- *Imagen Total 3.9: Ontología, lenguaje, formalización y laboratorios*, 23 de octubre de 2026; capítulos 1 y 2, en particular «El lenguaje conserva el hilo» y «La gramática matemática de la continuidad».
- *¿Dónde se ahorra el cálculo?*, solicitud de revisión independiente, versión 2, 8 de noviembre de 2026; sección «La economía entre referencias» y controles E9 / rejilla.
- Desarrollo conversacional del 12 de noviembre de 2026 sobre cuantificación de información, comparación $`C_4/K_4`$, laboratorio 5/8, continuidad y contrato de costo de consultas.

**Repositorio de referencia del programa:**  
<https://github.com/EndlessMonkeyProyect/programa-geometria-relacional>

**Informe de economía del cálculo:**  
<https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-08_economia_del_calculo/informe.md>

**Antecedentes conceptuales y matemáticos:** R. V. L. Hartley (1928), *Transmission of Information*; C. E. Shannon (1948), *A Mathematical Theory of Communication*; teorema de Myhill–Nerode; rango de matrices de incidencia sobre $`\mathbb F_2`$; estadística suficiente y complejidad de Kolmogórov. Se mencionan como antecedentes, no como resultados originales del programa.

---

**Endless Monkey Project**  
*Relational Geometry Program*
