# Encargo de investigación abierta

*Versión en inglés: `brief.md`.*

¿Cómo emerge la economía del cálculo a partir de las relaciones entre referencias?

Endless Monkey Project
Relational Geometry Program

---

INSTRUCCIÓN PARA EL MODELO INVESTIGADOR

Actúa como investigador matemático independiente. Examina el problema que se presenta a continuación desde la matemática, la física, la lógica, la teoría de la información y la computación.

Tu objetivo no es confirmar una hipótesis ni reproducir una solución conocida. Es identificar relaciones, construir argumentos, encontrar mecanismos, formular demostraciones y, cuando corresponda, descubrir contradicciones.

Conserva la ontología descrita, pero no limites la metodología.

Puedes utilizar cualquier herramienta matemática, computacional o conceptual que resulte pertinente. También puedes introducir nuevos objetos, formalizaciones y perspectivas, siempre que expliques su relación con la estructura original.

No se establece de antemano que la solución tenga que ser polinómica, subexponencial ni pertenecer a ninguna clase determinada de complejidad.

La economía, si existe, deberá surgir como consecuencia demostrable del mecanismo, no como una condición impuesta a la investigación.

## 1. Ontología de partida

El Programa de Geometría Relacional investiga cómo surgen las distinciones, las referencias, la herencia, la incompatibilidad, la singularidad y el cierre a partir de relaciones entre estructuras.

Sus elementos conceptuales incluyen:

- Referencia: una distinción adquiere significado dentro de una relación entre estructuras.
- Relación entre radios: el radio de una estructura, su distancia respecto de otra y sus cambios relativos determinan qué diferencias resultan observables desde una referencia.
- Reflexión: una transformación puede producir correspondencias, equivalencias y nuevas relaciones entre elementos.
- Herencia: las relaciones ya establecidas pueden permanecer contenidas en las estructuras posteriores.
- Novedad: una relación introduce distinciones que no estaban determinadas por las referencias heredadas.
- Cierre: determinadas relaciones producen configuraciones cuya descripción puede estabilizarse.
- Singularidad relacional: diferentes elementos o configuraciones pueden quedar reunidos bajo una referencia sin que ello implique su desaparición física o matemática.
- Reapertura: un cambio de referencia puede permitir distinguir elementos anteriormente reunidos.

Estas nociones constituyen el lenguaje inicial de investigación. No deben confundirse con teoremas generales ya demostrados.

La formulación central es:

Una estructura puede contener muchas relaciones y, sin embargo, manifestar un número reducido de distinciones respecto de otra estructura.

La economía observada podría surgir de esa relación, sin que exista una operación externa que seleccione arbitrariamente qué información conservar.

## 2. Laboratorio conceptual: cubo de espejos y esferas

El programa utiliza un cubo de espejos con una pared móvil como laboratorio de referencia.

Las reflexiones sucesivas permiten estudiar equivalencias, orientación, simultaneidad, desfase y cambios en las distinciones.

La pared móvil representa un cambio en las relaciones del sistema, no simplemente un mecanismo externo de compresión.

Las esferas permiten investigar configuraciones sin dirección privilegiada y la aparición de diferencias mediante vínculos, orientaciones y referencias compartidas.

El tetraedro, las estructuras de diamante y las configuraciones de múltiples esferas sirven para estudiar cierre, incompatibilidad y nuevas relaciones.

ROSI y el laboratorio de la caja de espejos forman parte del lenguaje utilizado para investigar estas transformaciones.

No es obligatorio utilizar directamente estas representaciones geométricas en toda demostración. Lo indispensable es conservar y explicar su correspondencia ontológica cuando se propone una formalización alternativa.

## 3. Resultados disponibles

El programa cuenta con varios laboratorios y resultados parciales.

### A. Herencia modular

Para una referencia modular heredada H y una observación nueva de período m:

```math
H'=\operatorname{mcm}(H,m)
```

La cantidad de clases nuevas dentro de cada clase heredada es:

```math
\frac{H'}{H} = \frac{m}{\operatorname{mcd}(H,m)}
```
Por ejemplo:

```math
\operatorname{mcm}(15,9)=45
```

Aquí aparece una distinción adicional respecto de la herencia.

En cambio:

```math
\operatorname{mcm}(315,9)=315
```

La segunda observación no introduce nuevas clases modulares.

Esta regla es exacta bajo las hipótesis del modelo y tiene antecedentes matemáticos conocidos. Su aplicación general a otros mecanismos sigue abierta.

### B. Economía en representaciones combinatorias

En experimentos anteriores se observaron reducciones de estados y transiciones mediante equivalencias estructurales.

Para una rejilla de tres colores de ancho diez se reportó una reducción de 1536 estados a 136 estados bajo una representación por simetrías.

También se obtuvieron resultados de recurrencias y rangos modulares de Hankel.

Estas comprobaciones no demuestran por sí solas una construcción general de representaciones mínimas ni una mejora de complejidad para problemas arbitrarios.

### C. Laboratorio óptico v5.1

Se mantiene fija una estructura de cinco fuentes y se cambia la distancia de observación.

Bajo los criterios ópticos implementados, las componentes distinguibles siguen la secuencia:

```math
5\longrightarrow4\longrightarrow3\longrightarrow2\longrightarrow1
```

Al invertir el desplazamiento, las distinciones pueden reaparecer.

El experimento incluye resolución angular, distancia, velocidad relativa, frecuencias, reflexión y fases modulares.

Se verificó que dos distribuciones internas diferentes pueden presentar los mismos observables simplificados a una distancia grande y diferenciarse al cambiar la referencia.

Esto no significa que toda la información interna permanezca recuperable desde la observación reducida.

La equivalencia es relativa a los observables utilizados.

### D. Límites conocidos del procedimiento

Los trabajos sobre 3-coloración muestran que determinadas incompatibilidades globales no son detectadas mediante cierres locales de tamaño fijo.

Las familias de Mycielski constituyen controles relevantes.

Por tanto, no puede suponerse que toda estructura global tenga automáticamente una representación pequeña o una clausura local suficiente.

Estos límites deben incorporarse a cualquier generalización.

## 4. El problema principal

Consideremos una estructura cuyo tamaño y número de relaciones aumentan.

Desde una referencia pueden manifestarse muchas distinciones. Desde otra, varias de ellas pueden coincidir.

En la óptica, esto sucede con una estructura extensa observada desde una distancia grande: múltiples fuentes pueden presentarse como una sola componente espacial, mientras algunos observables espectrales permanecen diferenciados.

La estructura original no necesariamente cambia.

Lo que cambia es la relación desde la cual se la distingue.

Pregunta principal:

¿Puede la economía computacional emerger de las equivalencias, herencias y nuevas distinciones que produce una relación entre referencias, de manera que el costo de resolver un problema dependa de esa estructura y no necesariamente de la enumeración de todas sus configuraciones?

No presupongas que la respuesta sea afirmativa.

Investiga en qué condiciones ocurre, cuándo fracasa y cómo puede demostrarse.

## 5. Correspondencia con problemas computacionales

Se desea investigar si el mecanismo tiene consecuencias en problemas de satisfacción de restricciones, conteo de soluciones, grafos, recurrencias, sistemas algebraicos y otras familias matemáticas.

Los trabajos recientes de OpenAI y Anthropic sobre SAT y algoritmos subexponenciales constituyen referencias de comparación, no soluciones que deban reproducirse.

Verifica independientemente el alcance, las hipótesis, las cotas y el estado de validación de esos trabajos.

Distingue rigurosamente entre:

- Decidir si existe una solución.
- Contar exactamente todas las soluciones.
- Construir una representación de las soluciones.
- Reducir distinciones observables.
- Reducir operaciones computacionales efectivas.

No supongas que una reducción en cualquiera de estas magnitudes implica automáticamente una reducción equivalente en las demás.

Busca correspondencias estructurales cuando existan, pero no fuerces equivalencias.

## 6. Libertad de investigación

No se solicita una metodología específica.

Puedes investigar mediante geometría, combinatoria, teoría de categorías, teoría de grupos, lógica, álgebra, teoría espectral, información, complejidad computacional, sistemas dinámicos, óptica matemática o cualquier otra perspectiva.

También puedes desarrollar formalismos completamente nuevos.

Se valorarán especialmente las propuestas que:

1. Identifiquen un principio general derivado de las relaciones entre referencias.
2. Distingan los resultados conocidos de las consecuencias realmente nuevas.
3. Construyan modelos matemáticos que puedan comprobarse.
4. Encuentren ejemplos extremos donde las relaciones sean numerosas o estén muy separadas.
5. Identifiquen contraejemplos que delimiten el alcance del mecanismo.
6. Permitan deducir cotas matemáticas sin imponer previamente su forma.

Una solución que demuestre una limitación fundamental también es un resultado válido.

## 7. Preguntas abiertas

Investiga especialmente:

Primera. ¿Bajo qué condiciones dos configuraciones pueden considerarse equivalentes respecto de una referencia sin perder la capacidad de resolver una consulta exacta?

Segunda. ¿Puede determinarse esa equivalencia a partir de las relaciones heredadas, sin enumerar primero todas las configuraciones?

Tercera. ¿Qué propiedades determinan que una nueva relación introduzca una distinción independiente y no simplemente una redundancia?

Cuarta. ¿Cómo cambia el costo de representar y resolver una estructura cuando aumenta su tamaño, la distancia entre sus relaciones o la cantidad de singularidades?

Quinta. ¿Existen familias donde una gran cantidad de relaciones pueda expresarse mediante un número reducido de referencias sin perder exactitud?

Sexta. ¿Existen familias donde esa reducción resulte imposible y pueda demostrarse por qué?

Séptima. ¿Puede establecerse una correspondencia matemática rigurosa entre la reducción óptica de distinciones y alguna reducción computacional exacta?

Octava. ¿Qué consecuencias de complejidad surgen del mecanismo, si se demuestra su validez para alguna familia? No se presupone ninguna cota objetivo.

## 8. Resultado que se solicita al investigador

Desarrolla una investigación independiente.

Comienza reconstruyendo la ontología mediante conceptos y relaciones, identificando qué elementos están matemáticamente definidos y cuáles necesitan formalización.

Después identifica distintas rutas posibles de solución.

No te limites a una sola interpretación ni descartes prematuramente perspectivas incompatibles.

Para las rutas que consideres más prometedoras, intenta producir resultados concretos: definiciones, proposiciones, demostraciones, contraejemplos, construcciones o experimentos reproducibles.

Distingue claramente entre resultados demostrados, evidencia experimental, hipótesis y preguntas abiertas.

Si encuentras un mecanismo conocido equivalente, explica la correspondencia exacta y qué aporta —o no aporta— la formulación propuesta.

Si descubres una contradicción, identifícala y determina qué parte de la construcción queda afectada.

Si aparece una nueva relación, explica cómo surge de los elementos originales.

No es necesario alcanzar una respuesta definitiva. Se busca ampliar el espacio de soluciones sin abandonar la ontología de partida.

## 9. Criterio de evaluación

Utiliza, cuando sea pertinente, una evaluación inspirada en ROSI y ROS-1 Lite.

Distingue entre relaciones:

- Resueltas: existe una demostración o comprobación suficiente dentro de hipótesis explícitas.
- Abiertas: falta información o una demostración.
- Superpuestas: distintas interpretaciones o construcciones permanecen compatibles con la evidencia.
- Prematuramente cerradas: una conclusión se ha afirmado sin las condiciones necesarias.

No confundas consistencia conceptual con demostración matemática.

Tampoco confundas semejanza entre mecanismos con equivalencia de algoritmos.

## 10. Pregunta final

La cuestión fundamental no es cómo obligar a una estructura a utilizar menos información.

Es comprender qué distinciones existen, cuáles permanecen bajo una referencia, cuáles se heredan, cuáles se reúnen y cuáles reaparecen al cambiar las relaciones.

A partir de ello:

¿Qué puede demostrarse sobre la economía natural de las representaciones y sus posibles consecuencias para el cálculo?

Investiga libremente, conserva la ontología y permite que los resultados determinen las conclusiones.

---

Endless Monkey Project
Relational Geometry Program
