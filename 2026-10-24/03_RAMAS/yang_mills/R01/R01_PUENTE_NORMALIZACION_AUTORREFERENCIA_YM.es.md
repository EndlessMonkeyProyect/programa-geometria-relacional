# R–01 | Novedad prima, múltiplo normalizado y autorreferencia

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**Fecha:** 23 de octubre de 2026  
**Naturaleza:** suplemento aditivo de síntesis y puente propuesto hacia Yang–Mills; no sustituye O40, O59, O60, MF-69, YM–01 ni YM–02.  
**Etiquetas:** [O] ontología; [D] definición; [T] demostración dentro del modelo; [H] hipótesis de correspondencia; [F] control adversarial; [A] abierto.

## 1. Enunciado generador [O]

Una diferencia que la referencia actual no puede distinguir constituye *novedad respecto de esa referencia*. En una realización multiplicativa, un primo nuevo es una dirección independiente, no simplemente el siguiente número. La nueva distinción puede establecer su **referencia interna** y convivir con las referencias acreditadas mediante un **múltiplo normalizador común**. El cierre propio no es la permanencia de una forma fija: exige que la identidad siga pudiendo reconocerse y actualizarse bajo las continuaciones pertinentes. Los caminos que convergen en el nuevo nodo pueden reconocerse después de la aparición de la distinción; no son, por decreto, su causa primera.

**Cadena propuesta:** novedad independiente → normalizador interno de la nueva relación → normalizador común que conserva referencias anteriores → autorrelación/cierre propio respecto de una familia de continuaciones → continuidad y nuevas convergencias. La existencia de una nueva coordenada de comparación es consecuencia formal posible de esta cadena, no su premisa ontológica.

## 2. Realización exacta aritmética [D/T]

### 2.1 Novedad y dos referencias

Sea el conjunto de caminos/enteros `X = Z`. La referencia anterior distingue `Φ_N(x)=x mod N`, con `N≥1`. Aparece la nueva consulta `d_p(x)=x mod p`, donde `p` es primo y `p∤N`. Declaramos:

- **Referencia interna nueva:** `p`, cuya firma normalizada es `θ_p(x)=(x mod p)/p` (tomando el representante entre `0` y `p−1`).
- **Referencia común:** `L=mcm(N,p)=Np`.
- **Referencia anterior:** `N`, que no desaparece.

**T1 — La nueva comparación no factoriza por la antigua.** No existe función `g` tal que `d_p=g∘Φ_N`.

**Prueba.** `Φ_N(0)=Φ_N(N)`, pero `d_p(0)=0` y `d_p(N)≠0`, pues `p∤N`. Por tanto una misma firma antigua debería producir dos respuestas nuevas distintas: imposible. ∎

**T2 — Cada clase antigua se divide en exactamente `p` nuevas clases.** La firma conjunta `(Φ_N,d_p)` equivale exactamente al residuo módulo `L` y

`Z/LZ ≅ Z/NZ × Z/pZ`.

**Prueba.** El teorema chino del resto se aplica porque `mcd(N,p)=1`. Una clase fija módulo `N` posee precisamente `L/N=p` representantes módulo `L`, con residuos distintos módulo `p`. ∎

**T3 — Continuidad aritmética del múltiplo normalizador.** En el modelo de fases `H_N={j/N mod 1}`, si `L=Np` entonces

`j/N = (pj)/L`.

La inclusión de fases `i_N^L(j mod N)=pj mod L` es inyectiva. En el **modelo diferente de residuos**, la proyección `π_N: Z/LZ → Z/NZ` conserva la firma vieja. No confundir la inclusión de fases con esa proyección: expresan contratos distintos y no tienen por qué ser inversas entre sí. ∎

**Interpretación exacta:** el primo `p` es un generador nuevo respecto de la divisibilidad de `N`. `L` guarda simultáneamente lo anterior y lo nuevo. Nada en T1–T3 afirma que todo primo sea una partícula, una dirección espacial o una brecha física de energía.

### 2.2 Autorreferencia interna que se sostiene bajo continuaciones

Declaremos las continuaciones `F_L([x]_L)=[ax+b]_L`, con `a,b∈Z`. Sus componentes internas son `F_N([x]_N)=[ax+b]_N` y `F_p([x]_p)=[ax+b]_p`. Entonces, exactamente,

`π_N ∘ F_L = F_N ∘ π_N`,  y  `π_p ∘ F_L = F_p ∘ π_p`.

**T4 — Cierre operativo por factores.** Cada referencia puede actualizar su respuesta desde su propio residuo, sin conocer el representante completo modulo `L`. Si `mcd(a,L)=1`, todas las distinciones de las dos firmas sobreviven al paso, porque `F_L` es biyectiva. ∎

Este resultado implementa una *autorreferencia operacional* relativa a transformaciones declaradas: la coordenada interna del primo posee una regla de actualización autónoma. No demuestra por sí solo un sostén físico espontáneo ni que la identidad numérica de cada estado permanezca fija durante la evolución.

**[F1]** Tomar `a=0` mantiene la conmutación de las proyecciones, pero destruye toda distinción entre estados. Por tanto **compatibilidad del normalizador ≠ persistencia de todas las diferencias**.

**[F2]** Si `N=6` y aparece `m=9`, `L=18` y la referencia gana tres subdivisiones por clase, pero no un primo nuevo: se profundiza el factor 3 ya presente. Por tanto **novedad representacional ≠ primo siempre nuevo**.

**[F3]** El mínimo común múltiplo garantiza representabilidad, no que un nuevo peso positivo quepa en una partición material previamente saturada. O40 da condiciones adicionales de compatibilidad aditiva.

## 3. Correspondencia controlada con Yang–Mills [H/T]

### 3.1 La diferencia no abeliana no es una factorización prima

En una red gauge `SU(2)` con dos caminos cerrados de punto base común, sean `U,V∈SU(2)` sus holonomías. Bajo cambio de referencia local en el punto base, ambas se conjugan simultáneamente. Consideremos observaciones antiguas `x=Tr(U)/2` y `y=Tr(V)/2`, y la consulta conjunta `z=Tr(UV)/2`.

**T5 — Testigo de novedad por composición.** Existen dos configuraciones con el mismo par `(x,y)` y distinto `z`.

**Prueba.** Sean `U=iσ_z`, `V_1=iσ_z`, `V_2=iσ_x`, con matrices de Pauli. En ambos casos `x=y=0`, pero `Tr(UV_1)/2=−1` y `Tr(UV_2)/2=0`. Las trazas son invariantes por conjugación simultánea. ∎

La composición distingue aquello que las comparaciones separadas no distinguían. El descriptor `ν(U,V)=1−Tr(UVU^{-1}V^{-1})/2` mide un defecto no abeliano y es gauge-invariante, pero **no** es por sí mismo un primo, una masa ni un Hamiltoniano.

### 3.2 Diccionario tentativo del puente

| Programa relacional | Realización aritmética [T] | Candidato gauge [H] |
|---|---|---|
| Diferencia nueva | `p∤N` y no-factorización | Nueva traza de palabra/lazo no reconstruible de firmas anteriores |
| Múltiplo interno | `p`, coordenada `x mod p` | Sector de relaciones de composición con observables gauge-invariantes |
| Normalizador común | `L=mcm(N,p)` | Familia de mapas de bloque/refinamiento entre escalas; **no** un MCM literal |
| Autorreferencia/cierre propio | Actualización compatible de `π_p`, `π_N` | Interfaz de lazos que permita actualizar comparaciones sin ambigüedad gauge |
| Continuidad | Proyecciones conmutan con `F` | Observables de escala fina reproducen, bajo mapa explícito, los de escala gruesa |
| Residuo/indefinición | Firmas aún indistinguibles | Diferencias físicamente medibles no resueltas por interfaz vigente |

**Contrato propuesto.** Para redes a escalas `a` y `2a`, especificar mapas de bloque `B_{a→2a}` en configuraciones gauge (o en sus clases físicas), una firma de lazos `Q_a` y un mapa entre firmas `R_{a→2a}`. Exigir y verificar la compatibilidad

`Q_{2a}∘B_{a→2a} = R_{a→2a}∘Q_a`.

Esta igualdad es un objetivo preciso de *conservación de respuestas*, no una ley física universal ya demostrada. Debe verificarse qué información de orden, fase, centro y lazos se pierde o se conserva al bloquear.

### 3.3 Prueba dinámica adicional [A]

El problema físico no termina al identificar el nuevo sector. Hay que derivar desde la dinámica Yang–Mills una desigualdad espectral gauge-invariante **uniforme en unidades físicas** al tomar volumen infinito y espaciamiento de red `a→0`, y construir el límite cuántico 4D. En particular, no basta `ν>0`: el defecto no abeliano puede ser positivo y arbitrariamente pequeño. Tampoco basta el gap de una celda finita con constante que se anule al refinar.

**Prueba adversarial obligatoria:** aplicar la misma metodología a `U(1)` en régimen Coulomb y verificar que un argumento basado solamente en normalización/compactitud no produzca un gap espurio. Para `SU(2)` conservar los sectores conmutantes de Cartan (`ν=0`), que no son configuraciones inexistentes.

## 4. Balance del puente

- **[T]** Independencia modular de un primo ajeno a `N`, refinamiento exacto de cada clase, conservación del valor referenciado, componentes autónomas para transformaciones afines; nuevo observable de composición de holonomías.
- **[O/H]** Interpretar la nueva componente como ámbito de autorreflexión/cierre propio sostenido por el resto; distinguir la novedad ontológica de su firma operacional.
- **[A]** Identificar un normalizador de escalas gauge con propiedades comparables, demostrar suficiencia dinámica, cota espectral uniforme y construcción de Yang–Mills cuántico 4D. No afirmar resuelto el problema del milenio.

## 5. Referencias del programa consultadas

O40 (`O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md`), O59 (`O59_AUTORREFERENCIA_Y_SECTORES.es.md`), O60 (`O60_FORMALIZACION.es.md`), MF-69 (registrado en fotografías de continuidad), O92 (`O92_FORMALIZACION.es.md`), rama `RAMA_YM_RESCATE_ACTUALIZACION_2026-10-22.md`, YM–01 y YM–02 (23 de octubre). Esto es un puente **aditivo**, no una reinterpretación retrospectiva de los teoremas físicos.
