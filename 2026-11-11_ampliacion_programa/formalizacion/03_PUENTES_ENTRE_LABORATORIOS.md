# Puentes de prueba entre la caja, las esferas y los modelos

El principio de transporte es explícito: **declarar estados de origen, estados de llegada, transformación, observables conservados y falsador del puente**. Una imagen útil abre un experimento; la correspondencia matemática depende de la función que une los dos contratos.

| Laboratorio | Contrato verificable | Qué conserva | Determinante | Próxima prueba |
|---|---|---|---|---|
| Caja de espejos | `x∈Q`, reflexiones `x→−x`, `x→2L−x` | firma de órbita `ρ_L(x)=dist(x,2L Z)` bajo `L` fijo | posición de pared `L` | probar si la firma vieja factoriza la consulta nueva |
| Normalización modular | estados `Z_lcm(N,m)`, residuos mod `N,m` | proyecciones a referencias antiguas | incorporación de un módulo | medir suplemento de bits y costo de construirlo |
| Esferas geométricas | cuatro puntos etiquetados en `R³`, distancias | seis distancias bajo isometrías | orientación etiquetada | distinguir volumen orientado y reflexión |
| Tetraedro binario | cuatro bits, seis comparaciones XOR | paridades por par y complemento global | añadir un bit/nueva arista | probar tres generadores independientes de las seis relaciones |
| Contactos | grafo etiquetado; aristas por contacto | incidencia y recorridos | quinta esfera/arista | declarar la regla de signos en cada enlace |
| CSP / 3-coloración | asignaciones y restricciones, consultas de existencia/conteo | respuestas frente a continuaciones declaradas | añadir cláusula/arista | determinar frontera suficiente y costo de reconocimiento |
| Óptica de resolución | fuentes, señales y umbral `ε` | distinciones dentro del error declarado | cambio de escala/umbral | comparar error, estabilidad y costo frente al caso exacto |
| Yang–Mills [I/A] | caminos, operadores de transporte, holonomías | observables de traza bajo hipótesis de gauge | composición ordenada | probar mapa que preserve composición, no solo la analogía |
| Gravedad/tiempo [I/A] | ritmos, métricas, evolución | invariantes definidos en un modelo físico | cambio de reloj/escala | producir ley dinámica y contraste físico |
| Navier–Stokes [I/A] | campos, flujo y residuos | cantidades conservadas bajo ecuaciones | actualización del campo | acotar error al conservar una firma reducida |

## 1. Caja de espejos: cálculo exacto [T/E]

Para espejos ideales en `0` y `L>0`, las imágenes de `x` están en `2kL±x` con `k∈Z`. La órbita queda identificada por `ρ_L(x)=min(x mod 2L,2L-(x mod 2L))` en `[0,L]`. El par `x=1/4`, `y=9/4` tiene la misma firma para `L=1` y firmas diferentes para `L=2`.

Se obtiene una prueba finita de que la firma anterior no recupera la lectura posterior. La incorporación de una nueva firma restaura esa consulta, pero todavía hay que medir el costo de construirla.

## 2. Tetraedro: distancia y orientación [T/E]

Las configuraciones de cuatro puntos etiquetados `p0=(0,0,0)`, `p1=(1,0,0)`, `p2=(0,1,0)`, `p3=(0,0,±1)` conservan todas las distancias al invertir `p3`, mientras cambia el signo de `det(p1−p0,p2−p0,p3−p0)`. El bit de orientación **depende de una convención orientada y etiquetada**. Esta construcción no atribuye quiralidad intrínseca al tetraedro regular.

Las seis relaciones `a_i XOR a_j` de cuatro bits etiquetados dependen solo de tres bits relativos a `a_0`; las 16 asignaciones se reúnen en ocho patrones al identificar el complemento global. Es un **segundo contrato**, algebraico: el vínculo con distancias debe especificarse en cada uso.

## 3. Distinciones y conteo [I/A]

La proposición B mide cuántas etiquetas nuevas se necesitan para distinguir una nueva consulta. Los resultados de rango de corte del artículo del 8-XI miden dimensión de representaciones **lineales secuenciales sobre un campo elegido**; las mediciones del 10-XI miden costos de algoritmos sobre familias particulares. Son magnitudes diferentes. Para unirlas, fijar una conversión de representación, algoritmos de descubrimiento y una comparación completa de recursos.

## 4. Falsador común [F]

Si dos estados tienen la misma firma y una continuación permitida da respuestas distintas, la firma no constituye un cierre contextual suficiente para ese contrato. Si la firma se actualiza, repetir el test para **cada** transformación permitida. Si el coste de obtenerla excede el ahorro posterior en la secuencia de consultas evaluada, la supuesta economía es negativa para ese caso.
