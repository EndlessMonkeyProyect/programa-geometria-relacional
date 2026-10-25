---
title: "O58 — La estela de escalas: dos cuadrados, múltiplo normalizador y unidad pendiente"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento candidato aditivo; ontología, dos contratos cuadráticos, teoremas aritméticos exactos, puentes dinámicos abiertos"
parents: ["O40", "O43R", "O44N", "O45", "O53", "O54", "O55", "O56", "O57", "Imagen Total v3.8.1"]
---

# O58 — La estela de escalas y la unidad que vuelve a quedar pendiente

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 21 octubre 2026**

## 0. Qué corrige O58

El usuario corrige el énfasis de O54–O57: **el criterio rector no es que las tangentes permanezcan perpendiculares**, sino que *los múltiplos de las dos relaciones, al cuadrado, sean normalizables por una referencia común dejando una unidad pendiente*. Desde dentro se vive la continuidad; desde el conjunto de configuraciones se observa una **estela de escalas**. El normalizador que cerró una comparación es la referencia desde la cual puede reconstruirse la siguiente. La novedad no tiene por qué residir en una dirección adicional.

**[O — ontología del programa]** Unidad → reflexión → diferencia → dos relaciones comparables → múltiplo normalizador compartido → resto de una unidad → nueva circunstancia → reorganización, conservando las relaciones acreditadas bajo un contrato. El marco exterior que se mueve (espejo) no es, por ello, una deformación material del toroide. La *singularidad de cierre propio* no es una singularidad analítica (blow-up) de Navier–Stokes.

**[D — traducción candidata que necesita validación del autor]** Interpretamos provisionalmente «los dos al cuadrado dejan uno» como `a²+b²+1=N²` con enteros positivos a,b,N. Es una formulación **más fuerte y distinta** de la identidad canónica anterior `N²-(N−1)(N+1)=1`. Se estudian **ambas** y el puente entre ellas. No se adjudica al usuario una equivalencia todavía no discutida.

**[T]** En el contrato de dos cuadrados se prueban familias infinitas, condiciones de paridad, la incompatibilidad entre reescala pura y nuevo resto bruto 1, y una estela anidada donde cada normalizador es múltiplo del anterior. **[A]** No se deriva de la ecuación de Navier–Stokes la elección de los múltiplos, de los dos canales enteros o del siguiente estado.

## 1. Dos identidades distintas, y un puente exacto entre ellas

### A. Regla bilateral canónica [T]

Para cualquier entero `N>1`:

\[
\boxed{N^2-(N-1)(N+1)=1, \qquad 1=\frac{(N-1)(N+1)}{N^2}+\frac1{N^2}.}\tag{O58.1}
\]

Esta igualdad siempre se cumple. El producto bilateral `(N−1)(N+1)` **no** equivale por definición a la suma de *dos cuadrados de enteros*.

### B. Contrato fuerte de dos canales al cuadrado [D]

Un **estado cuadrático primitivo candidato** será una terna de enteros positivos `(a,b,N)` con:

\[
\boxed{a^2+b^2+1=N^2.}\tag{O58.2}
\]

Normalizado por `N²`:

\[
\underbrace{\frac{a^2}{N^2}}_{\text{primera relación}}+
\underbrace{\frac{b^2}{N^2}}_{\text{segunda relación}}+
\underbrace{\frac1{N^2}}_{\text{unidad pendiente}}=1.\tag{O58.3}
\]

El resto **bruto** es `1`; la fracción restante es `1/N²`. No convertir automáticamente esa celda residual en energía, tercera fuerza, eje espacial o partícula. `N` es cardinalidad de una representación aritmética; `R,r` son longitudes geométricas; `L(t)` es escala del espejo exterior. Se necesita un operador explícito para identificarlas.

### Puente aritmético exacto [T]

Por (O58.2), `N²−1=a²+b²`. Del lema de paridad (sección 2), `N=2k+1`, `a=2u`, `b=2v`; entonces:

\[
\boxed{u^2+v^2=k(k+1),\qquad k=(N-1)/2.}\tag{O58.4}
\]

Por tanto las dos figuras de la identidad bilateral `N−1,N+1` **sí pueden** reorganizarse en dos cuadrados, pero solamente para valores de `N` que admitan esta representación. No es un hecho universal.

Para `N=4`: `16−3\cdot5=1` satisface la identidad bilateral, pero `15` no es suma de dos cuadrados enteros, ya que `15≡3 (mod 4)`. **El cuatro del primer cierre ontológico no se puede identificar sin puente con `N=4` en (O58.2).**

## 2. Propiedades necesarias y demostración [T]

**Teorema O58-T1 (paridad).** Si `a,b` son enteros positivos y `N²−a²−b²=1`, entonces `N` es impar y `a,b` son pares.

*Prueba:* Los cuadrados módulo 4 son 0 o 1. Si N fuera par, `a²+b²≡−1≡3 mod 4`, imposible. Así N es impar, `N²≡1 mod 8`; luego `a²+b²≡0 mod 8`. Los cuadrados módulo 8 pertenecen a `{0,1,4}`; ninguna suma que involucre 1 puede dar 0 mod8. Ambos cuadrados son 0 o 4 módulo 8 y, en ambos casos, a,b son pares. ∎

**Teorema O58-T2 (primitividad).** `gcd(a,b,N)=1`.

*Prueba:* Si un entero d>1 dividiera a,b,N, su cuadrado dividiría `N²−a²−b²=1`, contradicción. ∎

La regla de resto uno **ya prohíbe duplicar mecánicamente** una configuración y seguir diciendo que queda una unidad.

## 3. Existencia de infinitas configuraciones, sin asignar física [T]

Con una simetría adicional opcional `a=b=m`, que sirve como *familia testigo* y no como axioma del toroide:

\[
\boxed{N^2-2m^2=1.}\tag{O58.5}
\]

Para todo entero `j≥1`, los enteros positivos definidos por

\[
\boxed{N_j+m_j\sqrt2=(3+2\sqrt2)^j}\tag{O58.6}
\]

satisfacen exactamente (O58.5), porque `(3+2√2)(3−2√2)=1`. La recurrencia es:

\[
\boxed{N_{j+1}=3N_j+4m_j,\quad m_{j+1}=2N_j+3m_j.}\tag{O58.7}
\]

| Índice | `a=b=m` | `N` | Igualdad |
|---:|---:|---:|---|
| 1 | 2 | 3 | `4+4+1=9` |
| 2 | 12 | 17 | `144+144+1=289` |
| 3 | 70 | 99 | `4900+4900+1=9801` |
| 4 | 408 | 577 | `166464+166464+1=332929` |
| 5 | 2378 | 3363 | `5654884+5654884+1=11309769` |

Los dos canales no están obligados a ser iguales: `(a,b,N)=(4,8,9)`, `(6,18,19)` también cumplen el contrato.

**Límite:** que haya infinitas soluciones enteras no significa que un fluido físico visite esa familia, mucho menos que lo haga en ese orden.

## 4. Dos significados de «cambiar de escala» [T/F]

Sea `(a,b,N)` admisible y `q` un entero positivo.

**A — Cambio puro de escala (sin novedad de relación):** `(a,b,N)→(qa,qb,qN)`. Conserva `a/N`, `b/N` y la proporción de los canales; pero:

\[
\boxed{(qN)^2-(qa)^2-(qb)^2=q^2.}\tag{O58.8}
\]

Para `q>1` el resto bruto es `q²`, **no uno**. Es la versión discreta de reexpresar la misma forma en otra escala: el normalizador transporta exactamente la representación anterior.

**B — Nuevo cierre con resto bruto uno:** `(a,b,N)→(a',b',N')` donde también `N'²−a'²−b'²=1`. Si `N'>N`, no pueden conservarse simultáneamente ambas fracciones `a²/N²` y `b²/N²`:

\[
\frac{a^2+b^2}{N^2}=1-\frac1{N^2}
\ne 1-\frac1{N'^2}=\frac{a'^2+b'^2}{N'^2}.\tag{O58.9}
\]

**Teorema O58-T3:** una nueva escala con resto bruto exactamente uno requiere alguna reorganización de las relaciones normalizadas. Por ello *escala puramente exterior* y *novedad interior de cierre* no son la misma operación. La segunda no implica destrucción de identidad: eso depende del contrato de comparaciones que se conserven.

## 5. Transporte de la referencia y la estela [T]

Sean dos estados admisibles `(a,b,N)` y `(a',b',M)` con `N|M` y `M>N`. Escriba `q=M/N`.

**Transportar la representación vieja** al denominador cuadrático `M²`:

\[
\frac{a^2}{N^2}=\frac{q^2a^2}{M^2},\quad
\frac{b^2}{N^2}=\frac{q^2b^2}{M^2},\quad
\boxed{\frac1{N^2}=\frac{q^2}{M^2}.}\tag{O58.10}
\]

La *nueva unidad primitiva* es `1/M²`; **no** es igual al viejo resto transportado `q²/M²`. La información de la vieja referencia sigue reconstruible, pero hay novedad en el reparto.

Defina los cambios de los dos canales (sobre la misma referencia):

\[
\Delta_a=\frac{a'^2-q^2a^2}{M^2},\qquad
\Delta_b=\frac{b'^2-q^2b^2}{M^2},\qquad
\Delta_r=\frac{1-q^2}{M^2}.\tag{O58.11}
\]

Restar ambas normalizaciones da la **identidad de balance de la estela**:

\[
\boxed{\Delta_a+\Delta_b+\Delta_r=0,\qquad
\Delta_a+\Delta_b=\frac{q^2-1}{M^2}.}\tag{O58.T4}
\]

Esta es conservación de *representación normalizada* para estados declarados, NO una ley de conservación de energía, enstrofía, volumen o masa de NS. Alguno de los canales puede disminuir mientras el otro aumenta. La estela es el registro de cómo cada cierre puede reconstruirse desde el siguiente normalizador.

### Dos destinos compatibles desde una misma referencia

**Ruta asimétrica:** `(2,2,3)→(4,8,9)`, con `q=3`. En unidades de `1/81`:

\[
(36,36,9)\longrightarrow(16,64,1).
\]

Los cambios son `(-20,+28,-8)`; suman cero. El resto pasa a una sola unidad y un canal se reorganiza a costa del otro.

**Ruta simétrica:** `(2,2,3)→(70,70,99)`, con `q=33`. En unidades de `1/9801`:

\[
(4356,4356,1089)\longrightarrow(4900,4900,1).
\]

Los cambios son `(+544,+544,-1088)`; suman cero.

**Conclusión:** existen al menos dos continuaciones incompatibles entre sí en detalle, pero ambas aritméticamente admisibles desde la misma referencia. La existencia de un múltiplo común no determina **cuál** continuación ocurre. Esto hace explícita la diferencia entre *continuidad acreditable* y *ley de selección de la novedad*.

## 6. Una estela anidada infinita [T]

No toda sucesión de soluciones de Pell respeta `N_j|N_{j+1}`: por ejemplo `3∤17`. Sin embargo, la subfamilia simétrica admite una estela **verdaderamente anidada**.

Dado `N²−2m²=1`, eleve al cubo el número algebraico `N+m√2`:

\[
\boxed{N'=N(4N^2-3),\quad m'=m(4N^2-1).}\tag{O58.12}
\]

La nueva pareja satisface `N'²−2m'²=1` y, por construcción, **`N|N'`**. Al iterar:

\[
\boxed{3\longrightarrow99\longrightarrow3\,880\,899\longrightarrow\cdots}\tag{O58.13}
\]

Cada paso conserva la capacidad de representar las fracciones anteriores sobre un denominador cuadrático posterior, pero cambia los pesos normalizados. El ejemplo demuestra **existencia**, no unicidad ni selección natural de esta cadena. El gran salto muestra además que no se ha derivado una cota del costo de escala ni un reloj físico.

## 7. El flujo, el espejo y los dos recorridos del toroide [O/D/A]

Para un toroide ideal `R>r>0`, su geometría intrínseca tiene dos recorridos; la métrica es:

\[
 ds^2=r^2d\theta^2+(R+r\cos\theta)^2d\varphi^2.\tag{O58.14}
\]

El cambio de referencia exterior `L(t)>0` reexpresa ambos radios como `(R/L(t),r/L(t))` y no altera `r/R`. La métrica física tampoco cambia por la mera modificación de coordenadas. **Esto es el caso A**, no una transición nueva de resto bruto uno.

El caso B sugeriría **un cambio de cierre de relaciones**: a medida que el flujo se reorganiza, un comparador obtiene una nueva referencia discreta `(a',b',N')`. Sin embargo, no se ha dado una aplicación `\mathcal Q[u,\omega,\text{recorridos}]=(a,b,N)` que sea físicamente observable, compatible con las unidades, estable bajo elección del observador y capaz de predecir `N'` antes de calcular la evolución. En particular, la métrica toroidal continua **no obliga** a producir enteros `a,b,N` con resto uno.

O54–O57 ya contienen geometría de superficies materiales y deformación; son variables auxiliares útiles para comprobar una eventual traducción, **pero no reemplazan el criterio aritmético** que el usuario acaba de precisar. No volver a identificar la perpendicularidad tangencial sola con el cierre ontológico.

**Prueba física futura bien definida:** (i) definir a partir de datos del flujo dos observables adimensionales asignables a los canales; (ii) justificar un normalizador entero `N` y la unidad pendiente, sin redondeos escogidos para forzar O58.2; (iii) derivar una regla de actualización de `N` o una ley de admisibilidad de transiciones; (iv) comprobar si la interfaz predice el siguiente estado y no solo lo reclasifica a posteriori; (v) confrontar flujos con igual firma y distinta evolución; (vi) solo entonces plantear desigualdades independientes para el estiramiento de vorticidad.

Las ecuaciones incompresibles de Navier–Stokes `∂_t u+(u·∇)u=−∇p+νΔu`, `∇·u=0`, **no contienen** una selección de estados enteros dada por (O58.2). El hecho de que una relación pueda normalizarse no implica que el vórtice físico permanezca estable ni que NS 3D sea globalmente regular. La anterior prueba O44N ya construyó una solución exacta donde `N=mcm(2,3)` permanece constante pero la fracción física del resto modal cambia.

## 8. Estatus, hallazgo y control de complejidad

| Enunciado | Estatus |
|---|---|
| `N²−(N−1)(N+1)=1` | [T] Exacto para cada `N` |
| Interpretar «dos cuadrados y queda uno» mediante `a²+b²+1=N²` | [D/H] Contrato por confirmar |
| Paridad, primitividad, infinitud de soluciones de Pell | [T] Demostrado |
| Estela anidada `3→99→3880899` | [T] Construida y verificada |
| Balance algebraico de resto entre dos cierres | [T] Exacto al declarar dos estados compatibles |
| Selección única del próximo múltiplo por el cierre | [F] No se sigue; hay ramificación `3→9` y `3→99` |
| Etiqueta `N` desde la geometría del toroide / vorticidad | [A] Abierto |
| Control de regularidad 3D de NS por este mecanismo | [A] Abierto |

**Lectura de la razón:** El mecanismo central queda reducido a dos operaciones, no a un plano complejo inimaginable: (1) transportar una relación normalizada a otra referencia y (2) acreditar una reorganización que vuelve a dejar una unidad bajo el nuevo cierre. Matemáticamente ambas existen y son distintas. **La ley física pendiente es determinar cuándo y cómo el flujo efectúa la segunda.**

## 9. Pregunta que conviene confirmar con el autor

¿«Los múltiplos de las dos al cuadrado dejan una unidad» exige literalmente la **suma de cuadrados enteros** `a²+b²+1=N²`, o designa la **pareja bilateral** `(N−1)(N+1)+1=N²` que el núcleo ya usa? El segundo contrato vale para todo N; el primero sólo para algunos N y crea una estela con ramificaciones. Su distinción es imprescindible para derivar algo sin imponerlo.

## 10. Reproducción

`python3 codigo/o58_verificar.py` regenera tablas y pasa todas las comprobaciones en aritmética entera y fracciones exactas, sin dependencias externas. Véanse `resultados/soluciones_hasta_200.csv`, `estela_pell.csv`, `estela_anidada.csv`, `ramas_compatibles_hasta_200.csv`, `verificacion.json`. El censo finito no constituye una demostración de infinitud: la prueba algebraica es (O58.6)–(O58.7), y el anidamiento se demuestra mediante (O58.12).

El suplemento no modifica la Imagen Total v3.8.1 ni el historial O40–O57. La bibliografía externa, cuando se incorpore, será contraste, no fundamento de la ontología.
