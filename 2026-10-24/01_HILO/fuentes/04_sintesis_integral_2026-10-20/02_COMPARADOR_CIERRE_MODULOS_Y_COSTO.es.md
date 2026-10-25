# 02. Comparador, cierre, interfaz suficiente, módulos y costo

## A. Parte resuelta y residuo [D]

El núcleo define `C(a,b)=(q,r)`, donde `q` es la comparación acreditada y `r` aquello que la arquitectura vigente aún no puede incorporar sin pérdida. **Resto no es una sustancia ni una fuerza.** La división euclidiana, fracciones continuas, cocientes contextuales, grafos o espectros son realizaciones posteriores, no el origen obligado de la comparación.

## B. Suficiencia contextual [T]

Dada una acción de continuaciones `C` sobre estados `X` y una consulta `Q:X→Y`, defina:

`x≡_Q y ⇔ ∀c∈C, Q(x·c)=Q(y·c)`.

Su cociente `I_Q=X/≡_Q` es estable ante continuaciones y es la interfaz semántica más grosera que conserva todas las respuestas admitidas. **Prueba**: si `x≡y` y se agrega `d`, cada continuación siguiente se absorbe por composición `d∘c`; la minimalidad se obtiene factorando por cualquier interfaz suficiente. Ver `02_formal_core/contextual_reclosure_and_resource_cost.es.md`.

Esta equivalencia requiere que el conjunto de continuaciones y las preguntas se **declaren**. No obliga a que `I_Q` tenga representación finita, computable o de bajo costo.

## C. Composición y autoconsistencia [T condicional]

Que una relación entre módulos sea reutilizable exige que la composición elegida sea congruente con la equivalencia contextual. En símbolos, para una operación `J`, si `x~x'` e `y~y'` debe cumplirse `J(x,y)~J(x',y')`. Sin esa congruencia, no hay operación inequívoca sobre clases. Un cierre propio como condición física persistente necesita todavía una ley temporal adicional.

## D. Ritmo y radio [T condicional]

En la familia modal de osciladores relacionales definida por `ω²=Γλ` y `R=λ⁻¹/²`, se obtiene `Rω=√Γ=:v_*`. No es universal sin compartir `Γ`, métrica y normalización. En MF-43, una fase por actualización lógica define comparaciones de ritmo, **no** segundos ni una identificación necesaria con `c`.

Para modos con frecuencias constantes positivas, existe una recurrencia temporal exactamente común si su cociente es racional. Dos modos con cociente `p/q` retornan en un período común. Esta identidad aritmética no es una ley de acoplamiento físico; incluso frecuencias inicialmente inconmensurables pueden bloquearse en modelos acoplados.

## E. No-go de confundir geometría y información [N]

- Una diferencia no acreditada puede seguir existiendo en la estructura completa; no proyectarla no equivale a destruirla.
- Independencia relacional no implica ortogonalidad hasta construir la métrica.
- Simetría de imagen no garantiza una misma continuación futura (O26).
- Un radio, circulación y cuadrupolo de vorticidad no constituyen en general un estado físico suficiente para toda evolución.
- Cierre semántico sin contabilidad de construcción, actualización, almacenamiento y consulta no demuestra eficiencia.

## F. Arquitectura 3–4–5–7 y GR3 [CONDICIONAL]

El tetraedro, su doble referencia, las clases de cierre `C4` y `C4×C4`, la métrica de foco y comparaciones modulares tienen teoremas exactos **dentro de sus sistemas combinatorios** y ejemplos donde nuevos vínculos dejan libertad de orientación. El paso a tres dimensiones físicas, a masa o a un radio universal continúa condicionado. Véanse `extensions/GR3/`, el `09_hilo_del_dos/` y O18–O23.
