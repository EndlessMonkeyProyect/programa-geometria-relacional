# Continuación verificable del laboratorio E-MIRROR
**Fecha:** 2026-10-18  
**Base:** `Programa_Geometria_Relacional_v3_4_1_IMAGEN_INTEGRAL_CANDIDATA_2026-10-18.zip`  
**Estado:** extensión exploratoria independiente; los ZIP 3.4.1 originales se conservan intactos.  
**Etiquetas:** `[DERIVADO]` resultado exacto del modelo indicado; `[CONDICIONAL]` válido únicamente bajo hipótesis descritas; `[HIPÓTESIS]` idea ontológica por contrastar.

## Pregunta motriz
¿Cómo puede una sola fuente conservar su unidad mientras los reflejos multiplican las imágenes, cambian de orientación, se superponen, pierden intensidad o quedan inaccesibles? La palabra **foco** se desdobla en: (1) foco óptico (convergencia de rayos), (2) posición de una imagen virtual, (3) procedencia común reconstruible. No son sinónimos.

## A. Modelo matemático y alternancia
Un espejo plano de normal unitaria `n` y desplazamiento `d` actúa en un punto `x` como

`R(x) = x - 2n(n·x - d)`.

Para espejos planos ideales `R∘R = identidad`. Su parte lineal tiene determinante −1. Una secuencia de longitud `k` tiene determinante `(−1)^k`, de modo que se alternan transformaciones **propias** (paridad par) e **impropias** (paridad impar). Esto es una propiedad geométrica de orientación, **no** una alternancia de valores positivos/negativos de luz ni una garantía de enfoque.

Tomamos tres planos por el origen, de normales `x`, `y`, `z`. Las reflexiones de signo forman un grupo de **8** transformaciones. Incorporar la reflexión en `x=y` produce **16**. Incorporar también `y=z` produce **48**. Son grupos de matrices de permutaciones con signo, con 4/4, 8/8 y 24/24 transformaciones de ambas paridades respectivamente. Para el punto asimétrico `(1,2,3)` generan respectivamente **8, 16 y 48 posiciones** virtuales distintas. `[DERIVADO]`

**Advertencia física:** contar transformaciones del grupo no equivale a contar imágenes que una persona realmente verá en un recinto construido. Los espejos materiales pueden obstruir las trayectorias, tener tamaño finito y absorber luz; en particular, los planos diagonales ideales se cruzarían con fuentes situadas en sus propios planos. Hace falta un diseño catadióptrico o una simulación de rayos con aperturas para realizar el montaje.

## B. Centro, cara, arista y vértice
En el submodelo de tres planos perpendiculares:

| Punto de la fuente | Transformaciones | Posiciones virtuales distintas |
|---|---:|---:|
| `(1,2,3)` | 8 | 8 |
| `(0,2,3)` — sobre una cara | 8 | 4 |
| `(0,0,3)` — sobre una arista | 8 | 2 |
| `(0,0,0)` — vértice | 8 | 1 |

`[DERIVADO]` En el vértice ideal las imágenes puntuales coinciden; las reflexiones **no** dejan de existir matemáticamente. Un cuerpo que ocupe volumen no puede colocarse literalmente dentro de planos de espejo que lo atraviesan. Al aproximarse al vértice, varias imágenes pueden volverse indistinguibles por resolución limitada sin destruirse la fuente.

Un segundo submodelo, **cubo cerrado de seis caras**, es diferente del anterior. Al desdoblar sus planos, una fuente en el centro `(1/2,1/2,1/2)` del cubo unidad aparece en celdas virtuales `(n_x+1/2,n_y+1/2,n_z+1/2)`, con `n∈ℤ³`. Las orientaciones dependen únicamente de `(n_x,n_y,n_z) mod 2`. En el bloque `−2≤n_i≤2` hay **125 celdas** pero solamente **8 firmas de orientación**: 63 de paridad par, 62 impar. `[DERIVADO]` La orientación sola no identifica la celda en la que se obtuvo la observación. Este resultado amplía la sección J del E-MIRROR 3.4.1.

**Conclusión puntual:** ocupar el centro no implica enfocar todos los rayos de espejos planos; los espejos planos no son lentes convergentes. Una posición muy simétrica puede, paradójicamente, hacer **menos identificable** la transformación que produjo una imagen.

## C. El objeto también es un filtro
Una **esfera homogénea** no revela su orientación propia: bajo una reflexión plana sigue siendo una esfera. En la acción del grupo de 48 sobre una esfera centrada en `(1,1,1)`, obtenemos solo **8 centros virtuales distintos**, y las transformaciones adicionales no se identifican mirando la orientación de la esfera. Si sustituimos la esfera por **cuatro puntos etiquetados** en posiciones tridimensionales asimétricas, el mismo grupo produce **48 configuraciones completas distintas**. `[DERIVADO en el modelo]`

No es un resultado experimental sobre las cuatro esferas físicas que se propusieron para otro laboratorio; ese trabajo queda en una nota separada. Es un **control nulo de simetría**: antes de decir que el sistema perdió una diferencia, comprobemos si el objeto usado era capaz de exhibirla.

## D. Reconstrucción de la fuente: la condición determinante
Representamos observaciones calibradas de un punto tridimensional `p` por `y_j = H_j T_j p`, donde `T_j` es la transformación conocida por reflejos y `H_j` representa proyección y filtros. Apilamos las matrices `H_j T_j`.

- Una proyección `xy` tiene rango **2**, así que no determina `z`.
- Repetir la dirección `xy` con inversión de `x` conserva rango **2**; más copias redundantes no incorporan profundidad.
- Agregar una segunda vista independiente, calibrada, que intercambia `x` con `z` eleva el rango a **3**: permite recuperar el punto `p` si se conocen correspondencias y transformaciones. `[DERIVADO/CONDICIONAL]`
- Si un filtro deja pasar **solo y**, el rango queda en **1**, aunque todos los espejos sigan siendo invertibles.

**Criterio exacto en este modelo lineal:** la fuente tridimensional se reconstruye unívocamente cuando la matriz de observación conjunta tiene rango 3. Con rangos menores, distintas fuentes son compatibles con los mismos datos. Este criterio NO resuelve reconstrucción de objetos opacos con correspondencias desconocidas, óptica no lineal o sistemas sin calibración. En particular, reflejar la misma fotografía plana nunca suministra por sí mismo una nueva vista 3D.

## E. Capas con reflectividad y opacidad
Un modelo idealizado de intensidad tras `k` rebotes es `I_k/I_0 = ρ^k`, con `ρ` reflectividad constante. Adoptamos un umbral *ilustrativo* de detección del **5 %** de la señal inicial:

| Reflectividad por rebote | Último rebote detectable en este modelo | Celdas virtuales hasta esa distancia Manhattan, solo conteo ideal |
|---:|---:|---:|
| 100 % | sin límite por atenuación | no finito |
| 90 % | 28 | 30 913 |
| 80 % | 13 | 3 303 |
| 50 % | 4 | 129 |

`[DERIVADO bajo el modelo elegido]` Las cifras de celdas NO son predicciones del número de imágenes físicamente visibles: no incluyen obstrucción, dispersión, aperturas, polarización ni capacidad óptica de un observador. Demuestran solamente cómo un cambio de reflectividad, sin modificar la geometría, produce un límite a las **capas accesibles** por intensidad.

Incluso con transmitancia positiva en todas las coordenadas (rango exacto 3), el ruido limita la resolución: una diferencia de `z=1`, vista por un canal de intensidad 1 %, causa una señal `0,01`, por debajo de un umbral de error 0,02. La información está en el modelo algebraico, pero no es distinguible bajo ese error. `[CONDICIONAL]`

## F. Corrección precisa sobre los ángulos
En el modelo de dos **rectas especulares infinitas**, reflejar sucesivamente equivale a girar dos veces el ángulo `θ`. Si `θ/π` es racional `a/b` en términos reducidos, el grupo abstracto tiene `2b` transformaciones. Por ejemplo:

| Ángulo | Transformaciones de simetría abstractas |
|---:|---:|
| 90° | 4 |
| 60° | 6 |
| 45° | 8 |
| **61°** | **360** |
| 60,1° | 3 600 |

`[DERIVADO]` Rectificación de una afirmación anterior: **pasar de 60° a 61° NO destruye necesariamente el cierre exacto**, sino que lo vuelve mucho más largo. Un cociente `θ/π` irracional produce un grupo infinito. Ninguno de estos tamaños es un conteo directo de imágenes visibles entre espejos finitos.

## G. Lo que aporta a la ontología, sin confundir niveles
- `[DERIVADO]` Reversibilidad geométrica, distingibilidad observacional y unicidad de reconstrucción son propiedades diferentes.
- `[DERIVADO]` Multiplicidad de imágenes de **una** fuente y alternancia de orientación pueden coexistir.
- `[DERIVADO]` Si el objeto es más simétrico, puede ocultar firmas del grupo de reflexión; la información observada depende tanto del marco como del objeto.
- `[HIPÓTESIS]` La capacidad reflexiva como principio de unicidad ontológica del programa requiere una formulación propia; un invariante geométrico de procedencia todavía **no demuestra** que tal principio sea necesario ni suficiente.
- `[HIPÓTESIS]` Una nueva «capa» puede entenderse como modificación de accesibilidad observacional sin creación/destrucción del estado subyacente, siempre que el modelo distinga estado físico y datos del observador.

La continuidad con la 3.4.1 es conceptual y reproducible. **No prueba P=NP, la brecha de masa de Yang–Mills ni la secuencia ontológica 4–8–16.**

## H. Ejecución
Requisitos: Python 3.10+ estándar, **sin paquetes de terceros**.

```bash
python laboratorio.py --salida resultados.json
python -m unittest -v test_laboratorio.py
```

El resultado auditable se guarda en `resultados.json`; las **8 pruebas** cubren conteos de grupos, paridad, degeneraciones de posición, rango de observación, ciclos virtuales, órdenes angulares, atenuación y comparación esfera/objeto etiquetado.

### Próximos experimentos propuestos (no ejecutados)
1. Simulación de rayos con cámara y fuente colocadas en el centro y desplazadas, paredes finitas y obstrucción; comparar posiciones virtuales **predichas** con imágenes visibles.
2. Agregar curvatura controlada y calcular caústicas/focos, sin confundirlos con una fuente común.
3. Medir observabilidad de fuente y reconstrucción de procedencia con reflectividad, opacidad y ruido cuantificados.
4. Retomar el laboratorio independiente de tres/cuatro esferas y su ambigüedad de extensión, con geometría de centros, distancias y quiralidad.
