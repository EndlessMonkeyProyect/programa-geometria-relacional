# O72 — Del tetraedro al anillo coplanar: libertad, giro alternado y referencia transportable

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**21 de octubre de 2026 · Suplemento autónomo y aditivo de O68–O71**  
**Estado:** proposiciones geométricas y de grafos [D], experimento espectral Navier–Stokes [E], analogías físicas limitadas [H/A]. **No constituye una solución al problema de regularidad global de Navier–Stokes.**

## 0. Narrativa y prioridad ontológica

**[N]** La cápsula tiene cierre propio. Un conjunto de cápsulas ocupa relaciones compartidas y puede volver a expresar una diferencia entre sus giros. El tetraedro es una organización de cuatro nodos donde todos los pares están enlazados. Al proyectar su organización hacia el anillo coplanar, las relaciones que dejan de actuar como restricciones pueden quedar disponibles, no necesariamente destruidas. El movimiento común sería una ejecución compatible de diferencias, semejante al engrane, sin requerir las mismas moléculas como portadoras permanentes.

**[O]** En el lenguaje del programa, la identidad se sostiene mientras el cambio pueda absorberse en la referencia normalizadora manteniendo el cierre propio; el múltiplo que hizo posible la normalización se conserva como referencia de comparación. La indefinición no se identifica con azar: expresa libertades todavía no fijadas por las relaciones activas. Una relación deja de estar habitada en la proyección sin por ello salir de la totalidad. **No se postula que todas las relaciones y magnitudes físicas se reduzcan a engranajes.**

**Pregunta formal.** ¿Qué libertad se recupera cuando la estructura de seis enlaces del tetraedro se reduce a cuatro enlaces periféricos coplanares, y puede esa libertad determinar por sí misma un avance dirigido o una no-reintegración?

## 1. Separar tres operaciones que parecían la misma

**[D/A]** Distinguimos:

1. **Proyección geométrica:** observar las coordenadas tridimensionales de cuatro puntos en un plano. Esta operación, por sí sola, **no elimina** los seis enlaces del grafo completo.
2. **Selección de enlaces activos:** pasar del grafo completo `K4` (seis pares) al circuito `C4` (cuatro pares). Las diagonales dejan de imponer condiciones en el modelo proyectado. Esto es una reducción adicional de restricciones, no un efecto automático de proyectar.
3. **Ley física de contacto o sincronía:** exigir `r_i ω_i + r_j ω_j = 0` en un enlace. Esta es la idealización de engranajes externos sin deslizamiento; **no es una condición que Navier–Stokes imponga en general sobre regiones de un fluido**.

El mínimo de cuatro cápsulas que se obtiene aquí es **mínimo dentro de la regla de engranaje exterior en un circuito simple no trivial**, no una escala mínima universal de gotas, una discretización obligatoria del anillo físico ni un teorema de la ontología.

## 2. Teorema de paridad del circuito — [D]

Sea `G=(V,E)` un grafo conectado, simple, con `n` nodos. A cada nodo le asociamos radio de contacto `r_i>0`, velocidad angular con signo `ω_i` y velocidad tangencial `s_i=r_i ω_i`. Cada enlace activo `{i,j}` cumple

\[
\boxed{s_i+s_j=0}.\tag{72.1}
\]

Sea `Q_G` la **matriz de incidencia sin signos**, con dos unos por fila, en los extremos de cada arista. Las velocidades compatibles forman el núcleo

\[
Q_G s=0.\tag{72.2}
\]

**Teorema O72.1 (conocido en teoría elemental de grafos; aplicación al laboratorio).** Si `G` es conectado, entonces

\[
\dim\ker Q_G=\begin{cases}1& G\text{ es bipartito},\\0&G\text{ contiene un ciclo impar}.\end{cases}\tag{72.3}
\]

**Demostración.** Desde un nodo de valor `s`, cada enlace obliga a alternar el signo. Si el grafo es bipartito, toda trayectoria entre nodos de la misma parte tiene paridad par; la asignación alternada es consistente y queda un parámetro real libre. Si existe un ciclo impar, al regresar al mismo nodo se exige `s=-s`, de donde `s=0`; como el grafo es conectado, todos los demás valores también son cero. QED.

Consecuencias inmediatas:

| Grafo | Enlaces | Rango `Q` | Dimensión del núcleo |
|---|---:|---:|---:|
| Triángulo `C3` | 3 | 3 | **0** |
| Tetraedro completo `K4` | 6 | 4 | **0** |
| Circuito `C4` | 4 | 3 | **1** |
| `C4` más **una** diagonal | 5 | 4 | **0** |

Para `C4`:

\[
\boxed{s=(a,-a,a,-a)}\qquad\bigl(\omega_i=s_i/r_i\bigr),\tag{72.4}
\]

con `a` real libre. **No es necesario eliminar las dos diagonales para perder la libertad: basta que vuelva a actuar cualquiera de ellas para anular el movimiento alternado si todos los enlaces se rigen por (72.1).**

**Limitación:** los seis acoplamientos de engranajes exteriores en `K4` no son necesariamente realizables por engranajes circulares ordinarios en una disposición física; tratamos un **grafo de restricciones abstracto**. Que el núcleo sea cero no dice que un tetraedro material no pueda desplazarse o rotar como cuerpo rígido.

## 3. Teorema de libertad geométrica del anillo — [D]

Un tetraedro genérico de cuatro puntos en 3D tiene `12` coordenadas, de las cuales `6` corresponden a traslaciones y rotaciones globales. Sus seis longitudes de enlace independientes dejan `12−6−6=0` libertades internas.

Un cuadrilátero articulado genérico de cuatro vértices en el plano tiene `8` coordenadas; `3` corresponden a movimientos rígidos planos y `4` a longitudes de enlaces periféricos. Queda `8−3−4=1` libertad interna. Las matrices jacobianas de las longitudes al cuadrado tienen rangos `6` (tetraedro 3D `K4`) y `4` (anillo plano `C4`) en el ejemplo exacto, respectivamente.

Un testigo explícito es el paralelogramo:

\[
X_1=(0,0),\quad X_2=(\ell,0),\quad X_3=(\ell+\ell\cos\varphi,\ell\sin\varphi),\quad X_4=(\ell\cos\varphi,\ell\sin\varphi).\tag{72.5}
\]

Sus cuatro lados mantienen longitud `ℓ`; el ángulo `φ` permanece libre en el interior del intervalo `(0,π)`, y el área orientada es

\[
\boxed{A_z=\ell^2\sin\varphi}.\tag{72.6}
\]

**Son dos libertades distintas:** la amplitud de giro `a` de (72.4) y la flexión geométrica `φ` de (72.5). No hemos derivado una ecuación que obligue a una en función de la otra. Si las combinamos sin imponer más vínculos, tenemos dos parámetros libres, no una única variable física.

## 4. Proyección y pérdida de profundidad — [D]

Consideremos los vértices de un tetraedro regular:

\[
X_1=(1,1,1),\quad X_2=(-1,1,-1),\quad X_3=(-1,-1,1),\quad X_4=(1,-1,-1).\tag{72.7}
\]

Sus seis distancias entre pares son `√8`. La proyección sobre `xy` dibuja un cuadrado. Si reflejamos `z→−z`, obtenemos **la misma** proyección plana, pero el volumen orientado cambia de `−8/3` a `+8/3`:

\[
V_{\rm orientado}=\frac16\det(X_2-X_1,X_3-X_1,X_4-X_1).\tag{72.8}
\]

La proyección es incapaz de reconstruir por sí sola de qué lado estaba la componente de profundidad. Esto **no** prueba que dicha información desaparezca del sistema físico; dice que el observador plano no la recupera solo con las coordenadas proyectadas.

Aunque la sombra forme un cuadrado, el tetraedro proyectado mantiene seis pares identificables. El **modelo de anillo** aparece sólo cuando escogemos cuatro pares como enlaces activos y declaramos que las dos diagonales ya no restringen los giros ni las distancias.

## 5. El signo compartido frente a los espejos — [D]

Sea el patrón de cuatro contactos

\[
x_a=a(1,-1,1,-1).\tag{72.9}
\]

La rotación cíclica de un cuarto de vuelta `T` cumple `T x_a=−x_a`, `T²x_a=x_a`. Por tanto, el promedio de sus cuatro reflejos rotados lo anula:

\[
\underbrace{\frac14(I+T+T^2+T^3)x_a}_{\text{común escalar}}=0.\tag{72.10}
\]

El promedio de sus cuadrados es `a²`, independiente del signo de `a`. Pero si conservamos **la orientación de los nodos** podemos extraer el signo mediante

\[
\boxed{m_1(x)=\frac14\sum_{i=1}^{4}(-1)^{i-1}x_i=a}.\tag{72.11}
\]

La tercera potencia orientada vale `m_3(x)=a³`; no es estrictamente necesaria para recuperar `a` en este pequeño modelo. **La cantidad `m_1` no es invariante ante renumerar los nodos con un cuarto de vuelta:** recupera un signo relativo a una orientación de referencia que debe definirse; no hemos demostrado que el propio flujo seleccione autónomamente esa orientación. **No confundamos el escalar orientado (72.11) con el residuo cúbico específico de O71.**

Interpretación relacional: la caja puede perder el *sentido de ejecución* al registrar solo el común de las cuatro posiciones; su cuadrado aún registra actividad, pero no el sentido. El sentido reaparece al conservar la etiqueta u orientación de los enlaces. Esta es una instancia computable de «una relación existente no visible en la proyección común».

### 5.1 Subespacio par/impar exacto de Navier–Stokes — [D]

Una observación más fuerte que la analogía. Sea `T` la acción geométrica de rotar el **campo vectorial completo**, incluidos argumentos y componentes, `90°` alrededor del eje del anillo. Para un campo inicial que cumple `T²u=u`, pongamos

\[
a=\tfrac12(u+Tu),\quad w=\tfrac12(u-Tu),\qquad Ta=a,\quad Tw=-w.\tag{72.12}
\]

Para Navier–Stokes sin forzamiento en un dominio compatible con `T`, denotemos `Lu=νΔu` y `B(v,z)=−\mathbb P\nabla\cdot(v\otimes z)` con la convención bilineal. Por equivariancia de las ecuaciones se obtiene, **mientras exista solución suficientemente regular**:

\[
\boxed{\begin{aligned}
a_t &= La+B(a,a)+B(w,w),\\
w_t &= Lw+B(a,w)+B(w,a).
\end{aligned}}\tag{72.13}
\]

Éste es un **cierre exacto de dos sectores de simetría**, no una reducción a dos números: `a` y `w` siguen siendo **campos espaciales completos** con infinitos grados de libertad en el continuo. El sector `w` no crea por la no linealidad cuadrática otros sectores de representación, pues `(-1)×(-1)=+1` y `(+1)×(-1)=−1`.

La pareja `u_+=a+w`, `u_-=a-w=Tu_+` corresponde a **la misma órbita de la rotación**. Por unicidad local de soluciones suaves y equivariancia, sus partes comunes satisfacen `a_+(t)=a_-(t)` mientras ambas existan. Esto no contradice O71: sus datos `a±v` contienen una diferencia `v` con más sectores de simetría, de manera que cambiar globalmente su signo no equivale, en general, a una sola operación del grupo.

**[E]** En el esquema Fourier–Galerkin de O70, para `N=32`, `ν=0.025`, paso `Δt=0.004`, ocho pasos, se verificó `\|T u_+(t)-u_-(t)\|` con máximo `1.30×10⁻¹⁶` y diferencia máxima entre las partes comunes `8.14×10⁻¹⁷`. Estos errores son de redondeo, no evidencias de un nuevo teorema PDE ni certifican convergencia del límite continuo. Reproducible en `codigo/ensayo_ns_sector.py`.

**Resultado conceptual nuevo para el hilo:** el giro alternado sí puede ser *una parte del movimiento ausente del reflejo común* que realimenta al común mediante `B(w,w)`, pero **su inversión de signo aislada no basta para diferenciar el futuro del común**. La novedad dinámica genuina requiere otra información que no sea pura equivalencia bajo simetría.

## 6. La dirección y el impulso no aparecen automáticamente del engrane — [D/F/H]

La orientación de un circuito plano ordenado determina un vector de área

\[
\boxed{\mathbf A=\frac12\sum_{i=1}^{4}X_i\times X_{i+1}},\quad X_5=X_1.\tag{72.14}
\]

La orientación, y no solamente las distancias, decide el signo de esa normal. En un modelo de **filamento vorticial fino** con circulación firmada `Γ` y densidad `ρ`, el impulso hidrodinámico tiene la aproximación

\[
\boxed{\mathbf I\simeq \rho\,\Gamma\,\mathbf A}.\tag{72.15}
\]

Para una circunferencia de radio `R`, `|A|=πR²`. Este puente físico es clásico y puede derivarse formalmente de `\mathbf I=(\rho/2)\int x\times\omega\,dV` para vorticidad concentrada en un filamento cerrado. Fuente contextual: *Dynamics of thin vortex rings*, J. Fluid Mech. 609 (2008), y la sección del teorema de Kelvin en *Modern Classical Physics* de Blandford y Thorne (2017). El circuito cuadrado articulado es una representación **geométrica**, no un filamento físico de esquinas infinitamente agudas. Un anillo real requiere un núcleo suave, autoinducción y condiciones de evolución.

**No derivamos `Γ` a partir de `a`.** El parámetro de giro alternado `a` y el sentido de la circulación vorticial son objetos físicos distintos a menos que establezcamos un puente comprobable. La orientación del plano deja dos signos posibles; sólo combinar geometría, circulación y dinámica permite determinar una dirección física de avance. **El modo de engranaje no garantiza ni produce automáticamente sustentación, traslación o vorticidad.**

## 7. Absorción de cambio de radios y condición que falta — [D/A]

Si los radios efectivos de los cuatro contactos varían en el tiempo pero permanecen positivos, el modo de acoplamiento geométrico de engranajes permite escribir instantáneamente

\[
\boxed{\omega_i(t)=(-1)^{i-1}\frac{a(t)}{r_i(t)}}.\tag{72.16}
\]

Esta relación explica cómo **puede** absorberse un cambio de radios manteniendo la coincidencia de velocidades tangenciales. No dice que el fluido lo haga necesariamente: se necesita una ecuación para `a(t)` y las `r_i(t)`, así como condiciones de contacto compatibles con desplazamientos radiales.

**Contraejemplo a «sincronía implica no reintegración».** En la familia (72.5) hacemos que `φ(t)→0` en un tiempo finito `T`, sin cambiar ninguno de los cuatro lados ni romper el patrón de giros (72.4). El área `ℓ² sinφ(t)→0`: el paralelogramo colapsa en una línea en `T`. La sincronía del anillo **no impide** esta degeneración. Es una construcción cinemática, no una solución de Navier–Stokes.

Para formalizar «no reintegrarse» hace falta demostrar *dinámicamente* una no-degeneración, por ejemplo

\[
\inf_{0\le t\le T}|A_z(t)|>0
\quad\text{o una cota de distancia positiva entre cápsulas},\tag{72.17}
\]

para las clases de evoluciones admisibles. Una normalización de fases no da esa cota por sí misma.

### Prueba dinámica auxiliar declaradamente artificial

Podemos activar gradualmente las diagonales mediante una ley **elegida** de relajación de incompatibilidades:

\[
\dot s=-\bigl(Q_{C4}^{\!T}Q_{C4}+\alpha Q_{\rm diag}^{\!T}Q_{\rm diag}\bigr)s,\quad \alpha\ge0.\tag{72.18}
\]

El modo alternado `s(0)=a_0(1,-1,1,-1)` sigue exactamente

\[
\boxed{a(t)=a_0e^{-2\alpha t}}.\tag{72.19}
\]

Si `α=0`, perdura indefinidamente en este modelo. Si `α>0`, decae. **No es Navier–Stokes, no es una ley de las cápsulas y no debe utilizarse como prueba de mecanismo universal.** Es un test de sensibilidad a relaciones que vuelven a estar activas.

## 8. El límite físico, formulado sin energía como fundamento

**[F]** Para un fluido viscoso de densidad constante y sin fuerzas no conservativas, la circulación de un circuito material `C(t)` satisface

\[
\frac{d}{dt}\oint_{C(t)}u\cdot d\ell
=\nu\oint_{C(t)}\Delta u\cdot d\ell.\tag{72.20}
\]

Por ello la circulación no tiene que permanecer exactamente constante bajo Navier–Stokes viscoso. En el régimen inviscido bajo las hipótesis de Kelvin, la circulación material sí se conserva. La no-reintegración de las cápsulas y la sincronía exacta de giros no se deducen de (72.20); demandan otras relaciones físicas. Véase la derivación de Kelvin para el caso viscoso de Blandford y Thorne, *Modern Classical Physics*, cap. 14.

**[A]** Aun si demostramos no colapso geométrico de una familia de anillos, eso no controla la vorticidad de *todos los datos suaves* y por lo tanto no resuelve la regularidad global tridimensional. O66–O67 identificaron una obligación más fuerte: una cota dinámica de concentración entre escalas. La semilla O72 proporciona **candidatos de organización** para estudiar esa obligación, no la satisface todavía.

## 9. Qué demostramos, qué no y el siguiente falsador

| Etiqueta | Afirmación | Estado |
|---|---|---|
| [D] | Teorema de núcleo de incidencia sin signos: bipartito ↔ una libertad (grafo conexo) | Demostrado |
| [D] | `K4 → C4` libera modo alternado si se desactivan diagonales | Demostrado bajo enlace ideal (72.1) |
| [D] | Un cuatro-barras plano admite flexión interna; tetraedro rígido no | Demostrado genéricamente y testado |
| [D] | La sombra de un tetraedro no conserva el signo de volumen | Demostrado mediante coordenadas |
| [D] | Alternancia `C4` invisible en promedio cíclico, recuperable con etiqueta orientada | Demostrado |
| [D] | Sector `+/-` de giro del campo forma sistema exacto (72.13) si `T²u=u` | Derivado por equivariancia |
| [E] | Simulación 32³ confirma (72.13) y equivalencia `u_- = T u_+` a precisión flotante | Verificado en 8 pasos |
| [D] | Engranaje y longitudes de barras conservadas **no** impiden colapso del área | Contraejemplo explícito |
| [H] | El momento ontológico compartido se representa físicamente por `Γ A` | Correspondencia tentativa, **no** derivada |
| [A] | El sistema general de NS conserva siempre una semilla finita que garantiza regularidad | **No demostrado** |

**Próximo paso O73.** En lugar de deducir movimiento a partir de una figura, construir un observable colectivo **orientado** para el anillo físico: proyección del campo bajo la representación alternada de la rotación `90°`, junto con circulación/impulso y área. Después medir su evolución y comprobar si un dato de radios y fases basta para predecirlo; mantener separado el sector residual de O70–O71. El falsador es claro: si dos campos con la misma propuesta de semilla orientada muestran distintas derivadas del observable, la propuesta todavía es insuficiente.

## 10. Reproducción

```bash
python codigo/verificar_o72.py
python codigo/ensayo_ns_sector.py
```

- `codigo/verificar_o72.py`: grafos conexos aleatorios/exhaustivos; rangos, signos, tetraedro y proyección, cuatro-barras, colapso, dinámicas de prueba, gráficas.
- `codigo/ensayo_ns_sector.py`: ensayo Fourier–Galerkin `32³` sobre datos O53/O70, ecuación de dos sectores, condición de simetría, paso temporal `0.004`.
- `fuentes/ejecutar_o62_ORIGINAL.py`, `codigo/o63_operadores.py`, `codigo/experimento_o70_BASE.py`: fuentes previas reproducidas para ejecutar autónomamente el ensayo físico; **no** se sustituyen las versiones anteriores ni se afirma que estén certificadas para el PDE infinito.
- `datos/`: controles JSON, incluyendo errores del ensayo temporal.
- `graficos/`: figuras de geometría y sensibilidad a activación de enlaces.

### Referencias físicas utilizadas como contraste

- R. Blandford y K. Thorne, *Modern Classical Physics* (2017), cap. 14, evolución viscosa de circulación, https://eclass.uoa.gr/modules/document/file.php/PHYS181/%CE%92%CE%B9%CE%B2%CE%BB%CE%B9%CE%B1/Blandford%2C%20Roger%20D._%20Thorne%2C%20Kip%20S%20-%20Modern%20classical%20physics_%20optics%2C%20fluids%2C%20plasmas%2C%20elasticity%2C%20relativity%2C%20and%20statistical%20physics-Princeton%20University%20Press%20%282017%29.pdf
- *Dynamics of thin vortex rings*, *Journal of Fluid Mechanics* **609** (2008), https://www3.nd.edu/~bolster/Diogo_Bolster/Research_6_-_Vortex_Rings_files/5%20-%20dynamics%20of%20thin%20vortex%20rings.pdf

**Nota de autoría:** ontología y programa atribuidos a **Le Matt Ansatz Di Ego**. Las referencias externas verifican expresiones físicas estándar; no son fundamento ni fuente de la derivación ontológica.
