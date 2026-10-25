---
title: "El hilo del dos: lenguaje, reflexión, genealogía, cápsulas y masa"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización y auditoría asistida; integra la v1 del 13-10-2026, la propuesta v4 «El hilo y el lenguaje» y el laboratorio R14.1"
version: "2.0 — 2026-10-13"
status: "Ontología del autor + resultados exactos nombrados + hipótesis con falsador; ninguna demostración de P=NP ni derivación física de masa"
---

# El hilo del dos

## Lenguaje, reflexión, genealogía, cápsulas y masa

> **Pregunta rectora.** ¿Cómo sostiene una sola referencia diferencias todavía no
> resueltas, cómo las nombra a medida que crece y qué conserva cuando, vista desde
> fuera, ya es una unidad?

Esta versión cambia tres cosas respecto de la v1. La asimetría entre el 7 y el 9
deja de ser un postulado y pasa a ser un teorema clásico. La «información
sostenida» recibe una medida precisa. Y la masa como complemento, usada con una sola
escala para todas las partículas, queda falsada para los leptones (precisado en la v2.6:
el complemento en sí es una definición exacta y no está falsado).

---

## 0. Cómo leer este documento

### 0.1 Cinco etiquetas

| Etiqueta | Significado |
|---|---|
| **DEFINICIÓN** | Objeto o convención adoptada; no se prueba ni se refuta |
| **POSTULADO** | Premisa ontológica del autor o regla de realización elegida |
| **DERIVADO** | Consecuencia demostrada de definiciones explícitas; se nombra el resultado clásico cuando existe |
| **CONTRASTE** | Hipótesis con falsador declarado; puede quedar sostenida o falsada |
| **ABIERTO** | Obligación sin prueba ni contraste todavía |

Equivalencias con versiones anteriores: `[O]` y `[P]` de la v1 son POSTULADO;
`[D]` es DEFINICIÓN; `[T]` es DERIVADO; `[H]` y `[C]` son CONTRASTE si tienen
falsador y ABIERTO si no; `[F]` es CONTRASTE; `[A]` es ABIERTO. En la v3.1,
`[CONDICIONAL]` y `[PUENTE FÍSICO]` pasan a CONTRASTE o ABIERTO con el mismo
criterio.

### 0.2 Qué cambia respecto de la v1

| Tema | v1 (13-10-2026) | v2 |
|---|---|---|
| Genealogía | Regla aditiva `[P-G]` sobre centros `2^k` | Se archiva: su primera aparición es sólo el tamaño del número. Se reemplaza por la genealogía multiplicativa |
| 7 frente a 9 | Asimetría declarada | Teorema: el centro 8 es la única excepción de Zsigmondy para la imagen superior |
| Recierre | Idea ontológica | Modelo exacto: la cadena de Fermat (centros 2, 4, 16, 256, 65536) |
| §25 | Problema abierto de orientación | Corregida: `r_V` es el radio de la propia clase y `r_m` la fracción ya distinguida |
| Información sostenida | Objeto relacional sin medida | Resolución, indeterminación y residuo interior, con su identidad |
| Masa | Complemento de la proyección con puente pendiente | El complemento es exacto (identidad relativista); con una sola escala, falsado para leptones; nueva hipótesis tipada como residuo interior |
| P frente a NP | Obligación O5 abierta | Por la dicotomía de Schaefer, O5 es exactamente P=NP; se proponen metas alcanzables |
| Teoremas | T1–T6 numerados | Se nombran como lo que son: diferencia de cuadrados, conteo por fibras, normalización |

---

# I. El punto de partida

## 1. El hilo `POSTULADO`

Partimos de una intuición: existe un hilo. No lo vemos entero; lo sostenemos. Es la
continuidad entre lo que ayer distinguíamos y lo que hoy distinguimos, y a eso
llamamos nuestra construcción de la realidad.

Lo real, para un sistema, es lo que puede describir. El lenguaje es la parte
inmaterial de esa construcción: se hereda, crece y se completa en una entidad
colectiva, y por selección busca la máxima eficiencia al describir. Reflexionar es
notarse a uno mismo dentro de una circunstancia mayor.

Este documento desarrolla el caso más simple de ese lenguaje: **contar**. La
pregunta es qué números puede nombrar una referencia que sólo dispone de su
primera distinción, el dos, y cómo crece ese vocabulario.

## 2. Las relaciones exigen representación `POSTULADO`

Una relación existe en el programa sólo si puede nombrarse dentro del lenguaje.
Formalmente, una relación ρ sobre realizaciones es representable en un lenguaje
con realidad Ω/∼ si respeta ∼: si x ∼ x′ e y ∼ y′, entonces ρ(x,y) ⇔ ρ(x′,y′).
Si no la respeta, decidirla exige refinar el lenguaje: es novedad. Ésta es la
**regla R** de la propuesta v4; aquí se usa en §14.

---

# II. Tipado

## 3. Los tres usos del uno `DEFINICIÓN`

| Función | Escritura | Qué expresa |
|---|---|---|
| Referencia universal | `1_ref` | La totalidad de partida permanece unidad |
| Residuo algebraico | `1_res` | Diferencia mínima de una reflexión concreta |
| Resolución única | `K_Q = 1` | Sólo queda una clase distinguible bajo las preguntas Q |

`1_ref = 1` no implica `K_Q = 1`. Una cápsula con ocho alternativas y otra con una
sola pueden ser, cada una, una unidad vista desde fuera.

## 4. Tres cantidades y sus medidas

Sea C un conjunto de realizaciones compatibles y Q una familia de preguntas, con
x ∼_Q y si toda pregunta responde igual. `DEFINICIÓN`

- **Profundidad h:** pasos de estructuración en el árbol de cierres.
- **Multiplicidad K_Q = |C/∼_Q|:** clases distinguibles. K_Q = 0 es inconsistencia;
  K_Q = 1, resolución; K_Q > 1, indeterminación sostenida.
- **Información:** con peso uniforme sobre C y clases F_k de peso μ_k = |F_k|/|C|,

```text
Res = Σ μ_k · log₂(1/μ_k)      lo que el lenguaje ya distingue
Ind = Σ μ_k · log₂|F_k|        lo que queda sin distinguir dentro de cada clase
```

**Identidad.** Res + Ind = log₂|C|. `DERIVADO` (cada clase aporta
μ_k·log₂|C|; puente posterior: es la regla de la cadena de Shannon). La totalidad
no cambia; cambia su reparto.

**Conteo por fibras.** Si cada solución x del nivel h tiene f(x) ∈ {0,1,2}
continuaciones, K_{h+1} = Σ f(x). `DERIVADO` (elemental). Más profundidad no implica
más soluciones: con f ≡ 1 la profundidad crece y K no.

---

# III. La reflexión del dos

## 5. Reflexión y residuo `DEFINICIÓN` · `DERIVADO`

La reflexión de una diferencia d sobre un centro N da dos imágenes:

```text
M_N(d) = (N − d, N + d),        0 < d < N
N² − (N − d)(N + d) = d²        (diferencia de cuadrados)
```

Para d = 1, las dos imágenes recomponen la autorreferencia del centro salvo un
residuo unitario: 3·5 = 16 − 1, 7·9 = 64 − 1. **Lectura** `POSTULADO`: el residuo es
el testigo de la diferencia mínima. La identidad es elemental; lo que importa es qué
estructura sostiene.

## 6. La genealogía aditiva de la v1, y por qué se archiva `DERIVADO`

La regla `[P-G]` refleja sobre cada centro 2^k todas las diferencias impares ya
acreditadas. Genera exactamente los impares hasta 2^(k+1) − 3. Pero su primera
aparición depende sólo del tamaño:

> un impar m ≥ 3 aparece en el menor centro 2^k con m ≤ 2^(k+1) − 3.

Es el orden natural agrupado en bloques diádicos. Por eso el 7 y el 9 aparecen en el
mismo paso: la regla no puede ver la asimetría que la motivó. Se conserva en el
laboratorio como antecedente y se reemplaza por la genealogía de §7.

## 7. La genealogía multiplicativa `DEFINICIÓN`

Un primo impar p **entra al lenguaje del dos** en el nivel

```text
ord_p(2) = menor n ≥ 1 con p | 2^n − 1
```

Un primo es una **palabra nueva** la primera vez que divide una imagen. Un número
cuyos primos ya estaban es una **frase heredada**: 9 = 3·3 se dice con una palabra
vieja. Recorrido de centros 2^k, imagen inferior y luego superior:

| Centro | Imagen inferior | Imagen superior |
|---:|---|---|
| 4 | 3 — nueva (orden 2) | 5 — nueva (orden 4) |
| 8 | 7 — nueva (orden 3) | **9 = 3² — heredada** |
| 16 | 15 = 3·5 — heredada | 17 — nueva (orden 8) |
| 32 | 31 — nueva (orden 5) | 33 = 3·11 — 11 nueva (orden 10) |
| 64 | 63 = 3²·7 — heredada | 65 = 5·13 — 13 nueva (orden 12) |
| 128 | 127 — nueva (orden 7) | 129 = 3·43 — 43 nueva (orden 14) |
| 256 | 255 = 3·5·17 — heredada | 257 — nueva (orden 16) |

Completo hasta el centro 65536 en `results/genealogia_multiplicativa.csv`.

## 8. El teorema que sostiene la asimetría `DERIVADO`

**Teorema de Zsigmondy** (Bang 1886 para base 2; Zsigmondy 1892). Para todo n ≥ 1,
2^n − 1 tiene un divisor primo que no divide a ningún 2^m − 1 con m < n, salvo
n = 1 y n = 6.

**Consecuencias para los centros 2^k, k ≥ 3.** `DERIVADO`

1. La imagen superior 2^k + 1 trae una palabra nueva (de orden 2k) **en todo centro
   salvo el 8**, donde 9 = 3² es pura herencia. Es la excepción n = 6: 7·9 = 63 = 2^6 − 1.
2. La imagen inferior 2^k − 1 trae una palabra nueva **exactamente cuando k es
   impar**. Si k es par, 2^k − 1 = (2^(k/2) − 1)(2^(k/2) + 1) es el producto de las
   imágenes del centro 2^(k/2): ya estaba dicho.
3. El primer nivel cuya imagen mezcla herencia y novedad es **15 = 3·5** (nivel 4).
   Coincide con el ε = 4 del programa y con la clasificación de factores heredados y
   primitivos de la v3.1.

**Lectura** `POSTULADO`: «8 → (7, 9), con 7 nuevo y 9 heredado» no es un capricho del
relato. Es la única excepción de un teorema clásico.

**Alcance.** Es aritmética. No dice que el 7 sea una dimensión ni que el 9 tenga
menos realidad física. Que el carácter primo sea testigo de novedad es una elección
de lenguaje, la del dos multiplicativo.

## 9. La cadena del recierre `DERIVADO`

Tomemos ahora centros que se elevan al cuadrado: 2, 4, 16, 256, 65536, es decir
N_m = 2^(2^m). Con los números de Fermat F_i = 2^(2^i) + 1:

```text
imagen inferior en N_m  =  N_m − 1  =  F_0 · F_1 ⋯ F_(m−1)
imagen superior en N_m  =  F_m,  coprimo con todos los anteriores
```

| Centro | Inferior: todo lo anterior, recerrado | Superior: novedad coprima |
|---:|---|---|
| 2 | 1 | 3 |
| 4 | 3 | 5 |
| 16 | 15 = 3·5 | 17 |
| 256 | 255 = 3·5·17 | 257 |
| 65536 | 65535 = 3·5·17·257 | 65537 |

(Producto de Fermat y coprimalidad dos a dos: resultado clásico atribuido a
Goldbach, 1730.)

**Lectura** `POSTULADO`: cada paso es herencia completa cerrada como una unidad más
una novedad que no comparte nada con lo anterior. La identidad N² − 1 = (N − 1)(N + 1)
es el recierre: el producto de la reflexión en N es la unidad heredada del centro N².

**Dos sucesiones distintas.** Duplicar (h → h + 1) mide profundidad. Elevar al
cuadrado (h → 2h) es recerrar. `ABIERTO`: el autor debe decidir si la reflexión
ontológica corresponde a duplicar, a recerrar o a ambas en planos distintos.

---

# IV. La geometría del hilo y la §25 corregida

## 10. Radio como profundidad de distinción `DERIVADO`

Sea Π_0 ≼ Π_1 ≼ … una cadena de refinamientos que parte de la unidad. Para dos
realizaciones x e y, sea d(x,y) el último nivel en que comparten clase y
δ(x,y) = 2^(−d(x,y)). Entonces δ es una ultramétrica:
δ(x,z) ≤ max(δ(x,y), δ(y,z)).

- La bola de radio 2^(−n) alrededor de x es su clase en el nivel n.
- La distancia entre dos cosas es el radio de la clase más pequeña que las contiene.
- Si cada clase se parte en dos mitades de igual peso, peso y radio coinciden.

(Límites inversos de particiones finitas; espacios ultramétricos.)

> **Precisión de la v2.7.** Esta ultramétrica mide profundidad de distinción, no la
> distancia que medimos. Esa nace en el paso del cuatro al cinco: dos distinciones dan
> cuatro referencias a igual distancia en tres ejes de comparación, y con la quinta
> aparece la primera relación obligada entre comparaciones (T8,
> `DEL_CUATRO_A_LA_DISTANCIA_Y_EL_TIEMPO_v2_7.md`).

## 11. Corrección de la §25 `DEFINICIÓN` · `DERIVADO`

La v1 leía que, al alejarse del tronco, crece «la fracción de proyección», y la
identificaba en tensión con r_V. Esa frase venía de otro contexto del autor y aquí
no se usa para identificar variables. La lectura correcta en la realización binaria:

| h | Radio de la propia clase r_V = 2^(−h) | Fracción ya distinguida r_m = 1 − 2^(−h) | Razón modal μ_h = √(2^h − 1) |
|---:|---:|---:|---:|
| 1 | 1/2 | 1/2 | 1 |
| 2 | 1/4 | 3/4 | √3 ≈ 1.73 |
| 3 | 1/8 | 7/8 | √7 ≈ 2.65 |
| 4 | 1/16 | 15/16 | √15 ≈ 3.87 |

- **Alejarse del tronco** es ganar profundidad h: más estructuración, no más espacio.
- **r_V** es lo que todavía no se distingue de uno: el radio de la propia clase. Baja.
- **r_m** es la parte de la totalidad que ya quedó distinguida. Sube. Es el
  complemento como diferencia inversa: r_V + r_m = 1.

**Enlace con §8** `DERIVADO`: r_m = (2^h − 1)/2^h y μ_h² = 2^h − 1. El numerador de
la fracción distinguida es exactamente el número cuya genealogía multiplicativa se
estudió arriba. En h = 4, r_m = 15/16 con 15 = 3·5: el primer nivel con herencia y
novedad.

---

# V. Cápsulas, interfaz y relaciones

## 12. Cápsula `DEFINICIÓN`

Una cápsula respecto de un continente E es 𝖢 = (X, ℛ, Q, E): realizaciones
internas, relaciones admitidas, preguntas exteriores habilitadas y sistema de
referencia. Dos interiores son equivalentes para el exterior si responden igual a
todo Q. Una cápsula resuelta por fuera puede tratarse como unidad sin que X tenga
una sola realización.

## 13. Interfaz suficiente `DERIVADO`

En un sector booleano finito, la cápsula R(I,B) queda caracterizada para todo
contexto que sólo consulta la frontera B por su invariante ∃I R(I,B) (antecedente
MF-34). El invariante puede ser exponencialmente grande: tener una interfaz
suficiente no dice cuánto cuesta construirla.

## 14. El radio cardinal no basta: regla R `DERIVADO`

A = {00, 11} y B = {01, 10} tienen la misma cardinalidad, pero «x = y» es verdadero
en A y falso en B. La relación «x = y» no desciende al lenguaje que sólo cuenta
soluciones: un radio que codifica cantidad no puede representarla. Enriquecer el
radio es exactamente refinar el lenguaje hasta que la relación descienda.

## 15. Cierre exterior con residuo interior `DEFINICIÓN` · `DERIVADO`

Sea E la partición que ve el exterior e I una descripción interior más fina. Con
peso uniforme:

```text
residuo = Res(I ∨ E) − Res(E)    lo que el interior distingue y el exterior no ve
déficit = Res(I ∨ E) − Res(I)    lo que el exterior distingue y el interior perdió
```

Una cápsula puede tener K_Q = 1 hacia fuera y residuo positivo adentro. Ejemplo
del laboratorio: cuatro estados, una sola respuesta exterior, dos clases interiores:
residuo de 1 bit, déficit 0.

**Evidencia sintética (R14.1)** `CONTRASTE`: en una red pequeña entrenada sólo con
lenguaje, el residuo interior cae de 0.965 a 0 bits al aumentar la presión de
selección. Desde un inicio cercano a la unidad, el interior crece sólo por
refinamiento: cero reorganizaciones en 10 corridas.

---

# VI. Información sostenida y masa

## 16. La hipótesis, bien tipada `CONTRASTE` · `ABIERTO`

La v1 enunciaba: la estructura sostiene información mientras una relación no alcanza
una única solución. Leída así, una partícula ya cerrada (K_Q = 1) no sostendría nada.
Pero el mismo enunciado del autor dice que la estructura sigue participando como
unidad después del cierre. La forma consistente es:

> **Hipótesis de masa como residuo.** Lo que una singularidad cerrada manifiesta
> como masa es su residuo interior: las distinciones que sostiene adentro y que la
> pregunta exterior no ve.

Consecuencias que la hipótesis debe enfrentar:

1. El residuo se mide en bits; una masa necesita una escala y una ley que los conecte.
2. En el laboratorio sintético, el residuo desaparece bajo presión de selección. La
   pregunta física pasa a ser **qué impide que se elimine**.
3. Profundidad y residuo son independientes (§4): la masa no puede leerse sólo de h.

## 17. El complemento con una sola escala, falsado `DERIVADO` · `CONTRASTE`

> **Precisión de la v2.6.** En el modelo fundacional la masa es el complemento de la
> proyección: ‖V‖² + ‖m‖² = 1. Esa definición es exacta y, con E = ħω_U, pc = ħω_V y
> mc² = ħω_m, coincide con E² = (pc)² + (mc²)² (r_V = β², r_m = 1/γ²). No está
> falsada. Lo que esta sección falsa es usarla con **una sola escala** común a todas
> las partículas. Las frecuencias sólo aparecen como comparaciones entre partes.

El puente histórico postula ω_U² = ω_V² + ω_m², r_m = ω_m²/ω_U² y m = ħω_m/c², de
donde

```text
m(h) = m* · √(1 − 2^(−h))
```

**Cota.** Para todo h ≥ 1, m(h) está entre m*/√2 y m*. Con una sola escala m*, dos
masas difieren a lo sumo en un factor √2 ≈ 1.414; si h ≥ 2, en 1.155. `DERIVADO`

| Cociente | Valor medido (PDG 2025) | Máximo posible con una escala |
|---|---:|---:|
| muón / electrón | 206.77 | 1.414 |
| tau / electrón | 3477.4 | 1.414 |

**Resultado** `CONTRASTE`, falsado: el complemento con una escala común no describe
los leptones cargados. Ajustar m* por partícula viola el falsador F2 de la v1: dejaría
de derivar la masa desde el cierre. Lo que falta es una regla que fije la escala de cada
singularidad desde la estructura: la razón de masas es (ω_U₁/ω_U₂)·√(r_m₁/r_m₂), y el
complemento sólo fija el segundo factor.

## 18. Qué contaría como explicación `ABIERTO`

- Un objeto físico identificado con el residuo, sin usar la masa que se quiere obtener.
- Una ley dimensional con su escala fijada fuera de los leptones.
- Reproducir los cocientes muón/electrón y tau/electrón sin escalas por partícula.
- Recuperar carga, espín y la diferencia entre generaciones.

**Control de exigencia.** La relación de Koide (1981),
Q = (Σm)/(Σ√m)² ≈ 2/3, se cumple con los valores PDG 2025 hasta Q = 0.666664. Una
fórmula simple puede acertar seis cifras sin explicar nada; toda propuesta
estructural se mide contra esa vara.

Las convenciones del electrón (A: h_e = 2; B: r_V = r_m = 1/2) siguen sin decidir.

---

# VII. Complejidad: qué está realmente en juego

## 19. La cápsula afín `DERIVADO`

Las ecuaciones XOR sobre GF(2) se resuelven por eliminación gaussiana: se detecta
contradicción, se cuenta K = 2^(b−r) y se obtiene un testigo en tiempo polinómico.
El laboratorio lo contrasta con enumeración en 300 sistemas aleatorios.

## 20. Dicotomía de Schaefer `DERIVADO`

**Teorema** (Schaefer, 1978). Un lenguaje de restricciones booleanas es resoluble en
tiempo polinómico si todas sus relaciones pertenecen a una misma de seis clases:
0-válidas, 1-válidas, Horn, dual-Horn, bijuntivas (2-SAT) o afines (XOR). En
cualquier otro caso es NP-completo.

El laboratorio clasifica relaciones por cierre bajo AND, OR, mayoría y x⊕y⊕z:

| Relación | Clases |
|---|---|
| x ⊕ y ⊕ z = 1 | 1-válida, afín |
| x ∨ y ∨ z | 1-válida, dual-Horn |
| ¬x ∨ ¬y ∨ ¬z | 0-válida, Horn |
| exactamente uno de tres | ninguna |
| {x ∨ y ∨ z, ¬x ∨ ¬y ∨ ¬z} juntas | sin clase común: NP-completo |

## 21. Consecuencia para la obligación O5 `DERIVADO`

La v1 pedía un lenguaje de cápsulas fuera del sector afín con Build, Compose e
IsEmpty polinómicos para una familia NP-completa. Por Schaefer, eso **es** P = NP.
No es el paso siguiente: es el problema entero.

Metas alcanzables `ABIERTO`:

1. Cápsulas exactas para las otras cinco clases tratables, con costos en bits.
2. Cápsulas para instancias de anchura de árbol acotada, con mensajes de tamaño
   2^tw (nota SAT de la v3.1). **Respondida en la v2.7** para el motor de tablas:
   todo orden cuesta al menos 3^(tw+1) y el mejor a lo sumo n·3^(tw+|B|+1); es
   polinómico exactamente con tw = O(log n), y ningún selector lo cambia (N1,
   `PISO_DEL_CAMINO_v2_7.md`).
3. Medir costos incluyendo la construcción de la interfaz sobre instancias
   adversariales.

---

# VIII. Matriz epistémica

| Enunciado | Etiqueta | Dónde se comprueba |
|---|---|---|
| Totalidad sin diferencia acreditada; reflexión inicial | POSTULADO | — |
| Lo real es lo describible; regla R | POSTULADO | `test_regla_r` |
| Res + Ind = log₂\|C\| | DERIVADO | `test_resolucion_mas_indeterminacion` |
| K_{h+1} = Σ f(x) | DERIVADO | — (elemental) |
| N² − (N − d)(N + d) = d² | DERIVADO | `test_residuo_es_diferencia_al_cuadrado` |
| La genealogía aditiva sólo ordena por tamaño | DERIVADO | `test_primera_aparicion_es_solo_tamano` |
| Excepciones de Zsigmondy en base 2: n = 1 y 6 | DERIVADO | `test_excepciones_de_zsigmondy` |
| Centro 8: única imagen superior sin palabra nueva | DERIVADO | `test_ocho_es_el_unico_centro_sin_novedad_superior` |
| Imagen inferior nueva sii k impar | DERIVADO | `test_prediccion_por_centro` |
| 15 = 3·5, primer nivel con herencia y novedad | DERIVADO | `test_quince_es_el_primer_nivel_con_herencia_y_novedad` |
| Cadena de Fermat como recierre | DERIVADO | `test_cadena_de_fermat` |
| Duplicar o recerrar como reflexión ontológica | ABIERTO | — |
| Ultramétrica del hilo | DERIVADO | `test_ultrametrica` |
| §25: r_V baja, r_m sube | DERIVADO | `test_radio_y_fraccion_distinguida` |
| Radio cardinal insuficiente | DERIVADO | `test_contraejemplo_cardinal` |
| Residuo interior bajo cierre exterior | DERIVADO | `test_cierre_exterior_con_residuo_interior` |
| Economía y crecimiento anidado en un aprendiz | CONTRASTE, sostenido en lo sintético | Paquete R14.1 |
| Masa como residuo interior | CONTRASTE pendiente | — |
| m(h) = m*√(1 − 2^(−h)) con una escala para leptones | CONTRASTE, falsado | `test_leptones_no_caben_en_una_escala` |
| Cápsula afín exacta y polinómica | DERIVADO | `test_gf2_contra_enumeracion` |
| Dicotomía de Schaefer en ejemplos | DERIVADO | `test_dicotomia_ejemplos` |
| Algoritmo polinómico para NP-completos | ABIERTO (equivale a P = NP) | — |
| Del cuatro a la distancia (T8) | DERIVADO | `test_del_cuatro_a_la_distancia_v2_7` |
| Piso del camino del motor de tablas (N1) | DERIVADO | `test_piso_del_camino_v2_7` |

---

# IX. Obligaciones siguientes

1. **O1 · Genealogía.** Decidir si la reflexión ontológica es duplicar, recerrar o
   ambas. Extender la genealogía multiplicativa a otras bases solo si el núcleo
   acredita una segunda distinción primera.
2. **O2 · Radio de cápsula.** Tratar el radio enriquecido como refinamiento del
   lenguaje: declarar qué relaciones deben descender y construir la partición mínima
   que lo logra.
3. **O3 · Profundidad e indeterminación.** Usar Res, Ind y residuo con sus nombres; no
   leer masa, radio o soluciones desde h.
4. **O4 · Puente físico.** Contrastar la hipótesis de masa como residuo con los
   cocientes leptónicos, sin escalas por partícula, y frente a la vara de Koide.
5. **O5 · Cómputo.** Cápsulas para las clases de Schaefer y para anchura acotada, con
   costos medidos.
6. **O6 · Lenguaje real.** Repetir R14.1 en un modelo pequeño real desde
   inicialización pequeña, midiendo residuo y orden de separación por capa.

---

# X. Matemática nombrada

| Resultado usado | Nombre | Sección |
|---|---|---|
| N² − (N − d)(N + d) = d² | Diferencia de cuadrados | §5 |
| Res + Ind = total | Regla de la cadena de Shannon (1948) | §4 |
| Orden de 2 módulo p | Orden multiplicativo | §7 |
| Primo nuevo en cada nivel salvo 1 y 6 | Bang (1886), Zsigmondy (1892) | §8 |
| 2^(2^m) − 1 = ∏ F_i; F_i coprimos | Números de Fermat; Goldbach (1730) | §9 |
| Distancia por profundidad de distinción | Ultramétricas; límites inversos | §10 |
| Invariante ∃I R(I,B) | Proyección existencial (MF-34) | §13 |
| Seis clases tratables | Dicotomía de Schaefer (1978) | §20 |
| Σm/(Σ√m)² ≈ 2/3 | Relación de Koide (1981), como control | §18 |

---

# XI. Trazabilidad

| Fuente | Identificación |
|---|---|
| Formalización v1, paquete del 13-10-2026 | SHA-256 del zip: `11306434ff6bdfe756194d655b8ed9fe127f94277cadeb3d37f7ecdc07c08753`; documento preservado en `antecedentes/` |
| Repositorio v3.1.0-review | SHA-256: `3df87210fd8477f6aa9d54a3addb474547a6882125c091478a225e218b08af66` |
| Paquete R14.1 (economía y hilo) | SHA-256: `5546cbfd74c5fc0e8b1a6425ed5f059be1ddf9826bc025aad32a8734c22ed066` |
| Propuesta v4 «El hilo y el lenguaje» | Documento de trabajo compartido, 11-10-2026 |

El laboratorio `experiments/laboratorio_hilo_v2.py` reproduce todo lo marcado
DERIVADO que tiene prueba asociada; `tests/` contiene 26 pruebas con biblioteca
estándar.

## Fuentes externas

- Zsigmondy's theorem, resumen y referencias: https://en.wikipedia.org/wiki/Zsigmondy%27s_theorem
- Allender et al., presentación de la dicotomía de Schaefer: https://eccc.weizmann.ac.il/report/2004/100/download
- Particle Data Group 2025, tabla de leptones: https://pdg.lbl.gov/2025/tables/rpp2025-sum-leptons.pdf

---

# Conclusión

El dos nombra al principio sólo lo que su primera distinción alcanza. Al crecer,
cada reflexión trae palabras nuevas o frases dichas con palabras viejas, y un
teorema clásico dice exactamente dónde: siempre hay novedad, salvo en el centro 8,
donde el 9 es pura herencia. Al recerrar, todo lo anterior se convierte en una
unidad y aparece una novedad que no comparte nada con ella.

La geometría que resulta mide cercanía por profundidad de distinción, y la §25 queda
en su lugar: el radio propio se achica y la fracción distinguida crece. La masa sigue
siendo una hipótesis, ahora tipada como residuo interior y libre de una fórmula que
los leptones ya falsaron. El cómputo general sigue siendo P frente a NP, y el
documento lo dice con su nombre.
