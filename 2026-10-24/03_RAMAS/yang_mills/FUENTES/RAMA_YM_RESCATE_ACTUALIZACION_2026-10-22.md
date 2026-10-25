# Programa de Geometría Relacional — Rama Yang–Mills
## Rescate documental, reconstrucción y actualización del entronque

**Fecha de corte:** 22 de octubre de 2026  
**Autoría del programa:** Le Matt Ansatz Di Ego  
**Carácter:** acta de integración candidata (YM-R4), no sustitución de los originales ni afirmación de solución física.  
**Método:** narrativa → ontología y lenguaje → matemática → controles computacionales → puente físico → falsadores.

## 0. Regla de continuidad

No reiniciar el trabajo ni confundir un teorema de un modelo auxiliar con el resultado Yang–Mills cuántico 4D. Una tesis expresada por la ontología del programa se conserva en su nivel correcto y sólo se promueve cuando hay una implicación matemática o física demostrada. La bibliografía externa sirve como contraste crítico, no como origen de la ontología. Usar preferentemente **comunes, trama, familia de soluciones y cierre propio**, sin perder los nombres de variables y rótulos que aparecen en los textos históricos.

Etiquetas: **[O]** ontología del programa; **[D]** definición; **[T]** demostrado bajo contrato; **[C]** condicional; **[F]** falsador/no-go; **[P]** puente físico propuesto; **[A]** abierto.

## 1. Genealogía recuperada

| Fecha/documento | Lo que añade | Estatus |
|---|---|---|
| 1 oct, `Programa_Yang_Mills_v2_1.pdf`; 3 oct, `continuidad_Yang_Mills_programa_relacional_formalizada_v1.md` | No-factorización, testigo Q8, selección compacta mínima condicional de su(2), conmutador y descriptor ν, controles de centro, Cartan, U(1), escala RG | [T] algebra / [C] selección / [A] física |
| 8 oct, `PROGRAMA_GAP_RELACIONAL_YANG_MILLS_2026_10_08.md` | Laboratorio finito gauge-invariante, irreducibilidad y coercividad T1/T2; ciclo con gap que tiende a 0 | [T] modelo / [F] inferencia insuficiente |
| 8 oct, `AUDITORIA_YM_RELACIONAL_2026-10-08.md` | T3a desigualdad local entre varianzas condicionales y gradientes; matriz T1–T5 | [C] finito, T3b–T5 abiertos |
| 8 oct, `RECIERRE_ENTRE_ESCALAS_Y_GAP_YANG_MILLS.md` | YM-R3A: modelo SU(2)^2 con comparador de gap fijo y Hamiltoniano de gap colapsante. YM-R3B: decaimiento temporal común de correladores densos implica gap | [F] exacto auxiliar / [C] teorema espectral |
| 20 oct, dentro de `Imagen Total v3.7`, `06_yang_mills/two_cycle_dynamics.es.md` y `GAUSSIAN_CONTROL.md` | Coordenadas de dos ciclos, matriz de Gram, medida Haar proyectada y Hamiltoniano finito; control gaussiano abeliano por bloques | [T] fórmulas finitas / [E] controles de código |
| 21 oct, `Imagen Total v3.8.1` | Conserva la rama v3.7 dentro de una base comprimida v3.8.0; no reemplaza el estado de pruebas físicas YM | procedencia y preservación |
| 22 oct, O74, O92, LAB-CONV v2 | Distingue cierre multiplicativo escalar, información de orden, normalizador entre escalas, convergencia de caminos y suficiencia de firmas | [T] modelos propios; nuevo entronque propuesto con YM |

**Alcance de esta auditoría:** se inspeccionaron los documentos listados y la rama `06_yang_mills/` preservada en el ZIP de la imagen v3.8.1. No significa que cada fuente de los 1.476 elementos de v3.7 haya sido revalidada individualmente.

## 2. Narrativa y ontología conservadas

[O] La unidad sin diferencias acreditadas puede reflejarse, distinguir, comparar y conservar relaciones bajo una nueva referencia. Un número nuevo no es meramente el siguiente símbolo de una lista: es un **nodo al que convergen caminos de solución y estructuras**. La convergencia aritmética por valor, la equivalencia contextual y el reconocimiento estructural no son lo mismo.

[O] El **múltiplo que normalizó**, junto con el valor referenciado, transporta continuidad entre representaciones. Cambiar de referencia puede hacer visible una relación que el contrato anterior no distinguía. Lo resuelto no se «des-resuelve»: nuevas interfaces pueden incluirlo, refinarlo o revelar diferencias que antes no contaban como preguntas.

[O] El radio de incertidumbre cuantifica diferencias pendientes *después* de seleccionar comparador y métrica; la incertidumbre no equivale a azar. El signo relacional de escala (multiplicar/dividir respecto del referente) no es, sin puente, un signo físico de carga, espín o energía. El tiempo emerge como comparación de ritmos; la energía no se postula en el núcleo ontológico YM.

**Hipótesis de YM que se investiga:** ciertas diferencias de composición no son reconstruibles desde observaciones separadas, pero pueden acreditarse como nueva firma al cerrar rutas de comparación. Que ello explique el espectro físico exige una ley dinámica adicional; no se deduce del lenguaje por sí solo.

## 3. Núcleo algebraico rescatado

**3.1 [T] Novedad contextual.** Para firmas `C: Ω→Y` y `D: Ω→Z`, `D` es reconstruible desde `C` si existe `f` con `D=f∘C`. La novedad respecto de `C` se certifica con estados `ξ,η` tales que `C(ξ)=C(η)` y `D(ξ)≠D(η)`.

**3.2 [T] Testigo `Q8`.** Las unidades cuaterniónicas satisfacen `ij=k` y `ji=−k`. Una observación de los elementos aisladamente no decide el defecto de orden. El tamaño de `Q8` es mínimo para el contrato de dos elementos no conmutantes de orden cuatro, no una selección universal del grupo de gauge físico.

**3.3 [C] Continuo compacto.** Bajo las hipótesis PC1–PC5 del documento del 3 de octubre, la álgebra de Lie compacta no abeliana mínima es `su(2)≃so(3)` y sobre un plano rotatorio `J²=−I`, `J⁴=I`. No se infiere sin hipótesis la identidad del grupo global ni la acción Yang–Mills 4D.

**3.4 [T] Observable de composición.** Para dos holonomías en un punto base común,

\[
K(U,V)=UVU^{-1}V^{-1},\quad
\nu(U,V)=1-\tfrac12\operatorname{ReTr}K(U,V)=\tfrac14\|UV-VU\|_F^2.
\]

Por tanto `0≤ν≤2` y `ν=0 ⇔ UV=VU`. Si `x=Tr U`, `y=Tr V`, `z=Tr(UV)` (trazas completas),

\[
\nu=2-\tfrac12(x^2+y^2+z^2-xyz).
\]

Las dos trazas individuales no son suficientes para reconstruir `ν`; la firma triple sí lo es para esta expresión. El centro `±I` es invisible como signo de cada levantamiento en `ν(±U,±V)`; además `ν` también se anula en el sector Cartan de SU(2).

**3.5 [T] Descriptor de red.** `N_a(U)=Σ_{(p,q)}w_{pq}ν(U_p,U_q)`, con lazos transportados al mismo punto base y pesos no negativos, es gauge-invariante y no negativo bajo el contrato. Es descriptor de configuraciones, NO una forma sobre estados ni un Hamiltoniano.

## 4. Celda SU(2) de dos ciclos: formalización dinámica recuperada

[T/D] Definir las trazas ahora **normalizadas** `x=½Tr U`, `y=½Tr V`, `z=½Tr(UV)` y

\[
D=1-x^2-y^2-z^2+2xyz\ge0,\qquad\nu=2D.
\]

La región de clases conjugadas satisface `|z−xy|≤√((1−x²)(1−y²))`. Para los ejes vectoriales cuaterniónicos de U y V, `D=|a×b|²`: cuantifica un área de incompatibilidad de composición, NO una longitud física. La métrica de esfera unitaria y Haar producto proyectan la medida constante `dμ_H=(2/π²) dx dy dz` sobre esta región.

La matriz de Gram de gradientes en `(x,y,z)` es

\[
G=\begin{pmatrix}
1-x^2&0&y-xz\\
0&1-y^2&x-yz\\
y-xz&x-yz&2(1-z^2)
\end{pmatrix},\qquad\det G=(2-x^2-y^2)D.
\]

El operador de Laplace reducido `L F=∇·(G∇F)` permite declarar la dinámica finita `H_{κ,λ}=−κL+λν` con `κ>0`, `λ≥0`. Para `λ=0`, su gap entre constantes y primer modo no trivial en este sector es `3κ` bajo la normalización de la esfera unitaria. Con vacío positivo `φ₀` y `μ₀=φ₀² μ_H`, la transformación por estado fundamental da la forma cuadrática `κ∫(∇f)^T G∇f dμ₀`.

**Límite:** el operador, potencial y escala `κ,λ` fueron elegidos para una celda; no son la construcción del Hamiltoniano de Yang–Mills cuántico 4D, ni prueban el espectro del vacío interactuante. La herramienta `two_cycle_geometry.py` se ejecutó en este rescate en 300 instancias, con errores máximos de identidades y gauge del orden de `10⁻¹⁵`; esto respalda las identidades numéricas del laboratorio, no un límite físico.

## 5. Pruebas de alcance ya consolidadas

| Hito | Resultado exacto / condicional | Lo que NO autoriza |
|---|---|---|
| T1 | En redes finitas, bajo densidad positiva y acotada, núcleo de la forma por bloques = constantes | No da gap físico uniforme |
| T2 | Poincaré finito para Haar producto y medidas acotadamente equivalentes | No distingue SU(2) frente a U(1) en su física |
| T3a | `D_block^μ[f] ≤ C_G K E_∇^μ[f]`, `K=sup(b/a)<∞`; Wilson local: `K≤exp(2βq_max)` | No identifica la forma de gradiente con el Hamiltoniano físico |
| YM-R3A | Sobre SU(2)^2, `H_a=a(-Δ_U−Δ_V)` tiene `Δ_a=3a/4→0` mientras el comparador de remuestreo mantiene Poincaré óptima `1` | No es un contramodelo de Yang–Mills 4D, sino de la inferencia inadecuada |
| YM-R3B | Si todos los correladores físicos centrados generadores densos decaen `≤K_A e^(−m_* t)` con `m_*>0` común, el teorema espectral da `gap≥m_*` | El decaimiento común NO se derivó desde la acción |
| Control gaussiano | Modelo `Q=dᵀd+m²I` con diagnóstico `R=Var/D_ℓ` para observables declarados; `L=4,6` y `m²=0,0.1,0.5` documentados | Un solo observable o seis matrices no fijan la constante uniforme ni el caso no abeliano |

La escala renormalizada `Λ_YM` no constituye demostración de `Δ>0`, ni `Z₂`, ni el número 4 ni la proporción 1/16 seleccionan por sí mismos una masa Yang–Mills.

## 6. Entronque nuevo con O74/O92 y los nodos de convergencia

**6.1 [T, contraste] Cierre escalar del anillo vs. holonomía gauge.** O74 usa cocientes reales positivos para cuatro contactos `H=∏(a_i/b_i)`; en el caso telescópico `a_i=r_i`, `b_i=r_{i+1}`, su `H=1` es una identidad de productos **conmutativos**. Su validez no demuestra que el orden de composición sea indiferente en una estructura no abeliana.

En una base común tomemos `U=iσ_x`, `V=iσ_y`, de `SU(2)`. Dos recorridos con exactamente las mismas cuatro piezas `U,V,U⁻¹,V⁻¹` ofrecen:

\[
W_\mathrm{cancelado}=UVV^{-1}U^{-1}=I,
\quad W_\mathrm{conmutador}=UVU^{-1}V^{-1}=-I.
\]

Así `½Tr W_cancelado=1`, `½Tr W_conmutador=−1` y `ν(U,V)=2`. **[T]** Mismo inventario de piezas, distinta composición ordenada, distinta respuesta gauge-invariante. Es un testigo directo de la *novedad por el orden* y de por qué el cierre multiplicativo de un anillo de engranes no es una holonomía SU(2). Esta identidad algebraica es estándar; el aporte aquí consiste en hacer el entronque explícito con O74 y la jerarquía del programa.

**6.2 [P] De número/nodo a firma gauge.** El laboratorio de convergencias advierte que el número o el radio solos no certifican equivalencia contextual. En el par SU(2), la firma `(x,y)` deja trayectorias no distinguidas; `(x,y,z)` guarda la relación de composición que reconstruye `ν`. En una red, ni ese trío ni `ν` bastan por definición para todos los observables futuros: debe declararse la familia de continuaciones gauge-invariantes, sus transportes de base y el operador de comparación.

**6.3 [D] Medida radial candidata, NO radio físico.** Se puede **definir** `r_comp=√(ν/2)=√D=|a×b|∈[0,1]` como amplitud adimensional de apertura no abeliana para la celda. Esta reparametrización exacta sirve para confrontar la intuición de “radio de incertidumbre cuantificado” sin llamarlo radio de partícula ni inferir brecha energética. En el sector conmutante `r_comp=0` persisten observables no triviales: no representa toda la incertidumbre física o contextual.

**6.4 [P] Normalizador entre escalas.** O40/O92 distinguen transportes de valor, etiquetado de rama, fase y normalización del sistema. Para YM el análogo que merecería investigarse no es un múltiplo entero importado, sino una **familia explícita de mapas de bloque gauge-equivariantes** y un comparador de observables que preserve clases físicas. Debe demostrarse la compatibilidad entre refinamientos y cómo se comporta su costo/espectro con `a`, `L` y `g(a)`.

## 7. Frontera matemática y física exacta

**[A] T3b:** demostrar una desigualdad de formas que compare una forma relacional *independiente* y la forma del Hamiltoniano YM físico en el espacio gauge-invariante, con dominios, vacío/medida y dimensiones definidos. La identidad de cambio por el estado fundamental de la celda no resuelve este paso, pues reutiliza la propia dinámica elegida.

**[A] T4:** demostrar control uniforme en el límite de volumen infinito y `a→0` con normalización física correcta, distinguiendo SU(2) de U(1) Coulomb. Las constantes de comparación finitas pueden divergir.

**[A] T5:** construcción cuántica no trivial en 4D bajo los axiomas exigidos, reconstrucción/reflexión positiva y transferencia de una cota espectral positiva. La obligación Clay comprende cada grupo gauge compacto simple; SU(2) por sí solo sería parcial.

Enlace oficial del problema: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ (continúa etiquetado **Unsolved** el 22 de octubre de 2026).

## 8. Nueva pregunta de trabajo, falsable

¿Existe un operador de **recierre de bloques físicos** derivado de la acción Wilson SU(2), construido sobre observables gauge-invariantes y compatible con el transporte de holonomías, cuya contracción de correlaciones a una separación física fija pueda acotarse uniformemente en volumen y al retirar el regulador? ¿Qué hipótesis no abeliana específica impide que ese argumento atribuya indebidamente gap a U(1) en fase de Coulomb?

**Contrato de siguiente ensayo:** fijar red 4D euclídea y espacio de observables, separar las pruebas de `G` y `U(1)`, declarar los bloques a longitud física fija y el generador de transferencia, medir las constantes como funciones de `β, a, L`, probar el contraejemplo `H_a=aℒ`, estudiar Cartan y centros. Si sólo existe cota a red finita, registrar únicamente eso. Si no existe control de correlaciones, aportar un falsador; no rebautizar una reescritura como prueba espectral.

## 9. Proveniencia reproducible

Fuentes prioritarias de la Biblioteca: `continuidad_Yang_Mills_programa_relacional_formalizada_v1.md`; `PROGRAMA_GAP_RELACIONAL_YANG_MILLS_2026_10_08.md`; `AUDITORIA_YM_RELACIONAL_2026-10-08.md`; `RECIERRE_ENTRE_ESCALAS_Y_GAP_YANG_MILLS.md`; `03_ENTRONQUE_MF108_Y_ESTATUS_FISICO.md`; `CONTINUIDAD_PROGRAMA_GEOMETRIA_RELACIONAL_2026-10-22.md`; `O74_FORMALIZACION.es.md`; `O92_FORMALIZACION.es.md`; `LAB_CONV_V2_NODOS_Y_FRONTERAS.md`.

Fuente preservada en Imagen Total: `Programa_Geometria_Relacional_Imagen_Total_v3_8_1_C4_VINCULOS_2026-10-21(2).zip` → `archivo/BASE_V3_8_0_INTACTA.zip` → `archivo/BASE_V3_7_0.zip` → `06_yang_mills/{README.md, GAUSSIAN_CONTROL.md, two_cycle_dynamics.es.md, scripts/*.py}`. El documento fuente `two_cycle_dynamics.es.md` identifica su antecedente MF109. La investigación anterior a esta nota mantiene su integridad y prioridad documental.

**Cierre de esta acta:** algebra y geometría finita recuperadas; falsa inferencia de gap descartada; puente a dinámica de YM 4D, escala uniforme y continuo siguen abiertos. El entronque O74/O92 aporta una pregunta algebraica y una disciplina para las interfaces, **no una nueva prueba física**.
