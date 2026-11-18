# R–03 · Herencia espectral, normalización y ubicación de los ceros

**Continuación de R–01 / R–02 · Documento de examen, v0.2 · 18 de noviembre de 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

## Resumen

La transformación de Mellin de la discrepancia de criba hereda los ceros de la función zeta bajo cualquier referencia formada por un número finito de primos. Esta conservación es exacta y reversible dentro de la franja crítica abierta. Aquí se estudian tres consecuencias: la normalización que recupera la referencia común, la estabilidad cuantitativa de esa recuperación y la insuficiencia de la conservación finita para fijar los ceros en la línea `Re(s)=1/2`. Un contraejemplo de control permite separar simetría de localización. La hipótesis de Riemann permanece abierta.

**Palabras clave:** criba; herencia; transformada de Mellin; ceros de zeta; normalización; discrepancia; economía de información.

## 1. Referencia, discrepancia y transformada

Sea `S` un conjunto finito de números primos y sean

\[
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}(1-p^{-1}),\qquad
A_S(x)=\#\{1\le n\le x:\gcd(n,M_S)=1\},
\]

\[
E_S(x)=A_S(x)-x\delta_S,
\quad
F_S(s)=\int_0^\infty E_S(x)x^{-s-1}\,dx.
\]

La Proposición 1 de la [formalización publicada](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md) establece, en la franja `0<Re(s)<1`,

\[
F_S(s)=\frac{\zeta(s)}s P_S(s),\qquad
P_S(s)=\prod_{p\in S}(1-p^{-s}).\tag{R03.1}
\]

El operador de herencia `T_p f(x)=f(x)-f(x/p)` equivale, tras la transformada, a multiplicar por `1-p^{-s}`.

## 2. Proposición 1 — Herencia espectral exacta

**Para todo conjunto finito S, F_S y ζ tienen los mismos ceros, con las mismas multiplicidades, dentro de 0<Re(s)<1.**

*Demostración.* Para `s=σ+it`, `0<σ<1`, cada factor cumple `|p^{-s}|=p^{-σ}<1`. De ahí que `P_S(s)` no se anule. El factor `1/s` tampoco se anula ni tiene polos en la franja. Por (R03.1), `F_S(s)` es `ζ(s)` multiplicada por una función holomorfa sin ceros. La factorización local preserva los órdenes de anulación. □

**Interpretación:** una referencia finita conserva los ceros; añade una forma de observarlos, pero no altera su posición.

## 3. Proposición 2 — Normalización y referencia común

Defínase

\[
N_S(s)=\frac{F_S(s)}{P_S(s)}.\tag{R03.2}
\]

Para cada `S` finito y `0<Re(s)<1`,

\[
\boxed{N_S(s)=\frac{\zeta(s)}s.}\tag{R03.3}
\]

**Demostración.** Dividir (R03.1) entre el factor no nulo `P_S(s)`. □

La referencia normalizada es la misma para todas las colecciones finitas de primos. Este resultado expresa una invariancia exacta, no una compresión algorítmica demostrada: para evaluar `N_S` todavía es necesario conocer `F_S` y `P_S`, o disponer de otra representación de costo verificable.

## 4. Proposición 3 — Costo de la inversión y estabilidad

Fijado `σ₀` con `0<σ₀<1`, para `Re(s)≥σ₀` se cumple:

\[
\prod_{p\in S}(1-p^{-\sigma_0})
\le |P_S(s)|
\le\prod_{p\in S}(1+p^{-\sigma_0}).\tag{R03.4}
\]

Así, si una medición $\widetilde F_S$ de $F_S$ introduce un error absoluto $\varepsilon(s)$, la normalización satisface:

\[
\left|\frac{\widetilde F_S(s)}{P_S(s)}-\frac{\zeta(s)}s\right|
=\frac{|\varepsilon(s)|}{|P_S(s)|}
\le |\varepsilon(s)|\prod_{p\in S}(1-p^{-\sigma_0})^{-1}.\tag{R03.5}
\]

*Demostración.* Aplicar `1−|z|≤|1−z|≤1+|z|` a cada `z=p^{-s}`, multiplicar y dividir por `P_S(s)`. □

**Límite asintótico.** Para cualquier `0<σ₀<1`, al incorporar todos los primos hasta $p_k$, el valor real $P_{S_k}(\sigma_0)=\prod_{j\le k}(1-p_j^{-\sigma_0})$ tiende a cero, ya que $\sum_p p^{-\sigma_0}$ diverge (domina a la serie $\sum_p 1/p$). La inversión amplifica potencialmente los errores de medición. No hay una cota uniforme de condicionamiento basada solo en la finitud de cada referencia.

Esta proposición permite **medir una parte del costo de reconstrucción**. No determina por sí sola el costo total de computar la transformada o la ubicación de los ceros.

## 5. Proposición 4 — La conservación y el espejo no fijan la línea

Sea `a=1/5+i`, `z=s−1/2`, y defínase el polinomio

\[
H(s)=(z^2-a^2)(z^2-\overline a^{\,2}).\tag{R03.6}
\]

Satisface las simetrías

\[
H(1-s)=H(s),\qquad
H(\overline s)=\overline{H(s)}.\tag{R03.7}
\]

Sus cuatro ceros son

\[
\boxed{\,3/10\pm i,\qquad 7/10\pm i\,}.\tag{R03.8}
\]

Para cada conjunto finito `S`, la familia `H_S(s)=H(s)P_S(s)` conserva esos cuatro ceros dentro de la franja. **Esta familia, en general, no conserva la simetría `s↦1−s`**, pues `P_S(1−s)≠P_S(s)` en general. Conserva la simetría conjugada.

Para preservar ambas simetrías en **cada referencia finita**, introdúzcase el filtro simetrizado:

\[
\boxed{\widehat H_S(s)=H(s)P_S(s)P_S(1-s).}\tag{R03.8a}
\]

Entonces, para todo `s`,

\[
\widehat H_S(1-s)=\widehat H_S(s),\qquad
\widehat H_S(\overline s)=\overline{\widehat H_S(s)}.\tag{R03.8b}
\]

Para `0<Re(s)<1`, tanto `P_S(s)` como `P_S(1−s)` son holomorfos y no nulos; por tanto, los únicos ceros de `\widehat H_S` **dentro de esa franja** son los cuatro ceros de `H`, con idénticas multiplicidades.

*Prueba.* El cambio `s↦1−s` envía `z↦−z`, y `H` depende de `z²`, lo que da la primera simetría. La segunda se sigue del emparejamiento de los coeficientes conjugados. Los ceros cumplen `z=±a` o `z=±\bar a`; sus partes reales son `1/2±1/5`. Multiplicar por `P_S(s)` o por `P_S(s)P_S(1−s)` no añade ceros dentro de la franja, pues ambos factores son no nulos allí. El producto simetrizado es invariante al intercambiar `s` con `1−s`; los factores tienen coeficientes reales y respetan conjugación. □

**Conclusión lógica del control.** La simetría de espejo, la simetría conjugada y la multiplicación por filtros finitos no bastan, **por sí solas**, para obligar a todos los ceros de una función holomorfa a estar sobre una línea fija. El ejemplo **no** pretende sustituir las propiedades adicionales de `ζ` ni construir un contraejemplo a Riemann; delimita lo que puede deducirse exclusivamente de los mecanismos formalizados aquí.

## 6. Radio, fase y dato suplementario

Para un cero hipotético `ρ=β+iτ`, el multiplicador de herencia es

\[
\lambda_p(\rho)=1-p^{-\rho},\qquad
r_p(\rho)=|p^{-\rho}|=p^{-\beta}.\tag{R03.9}
\]

La amplitud del multiplicador completo depende también de la fase:

\[
|\lambda_p(\rho)|^2
=1+p^{-2\beta}-2p^{-\beta}\cos(\tau\log p).\tag{R03.10}
\]

El radio `r_p` y el módulo `|λ_p|` son objetos diferentes. La proposición

\[
\forall\rho:\ \ r_p(\rho)=p^{-1/2}
\]

para cualquier primo fijo `p>1` equivale a `Re(ρ)=1/2` para todos los ceros no triviales: **es una reformulación de la hipótesis de Riemann, no una consecuencia de (R03.9)**.

La frase «un número por cero» se refiere al número de **parámetros reales necesarios para describir la órbita simétrica**: en la línea basta la altura `τ`; fuera de ella hace falta también `β`. Este conteo de parámetros continuos no es automáticamente un conteo de bits ni una demostración de menor costo de cómputo.

## 7. Obligación matemática nueva

Para obtener una restricción sobre la ubicación de los ceros se necesita una condición verificable `Q` que, además de (R03.1), excluya un modo fuera de la línea. Una formulación susceptible de refutación es:

> Encontrar un funcional `Q`, definido a partir de las discrepancias `E_S` y sus relaciones entre ventanas incompletas, tal que (i) tenga una identidad o desigualdad demostrable independiente de la hipótesis de Riemann; (ii) controle el componente espectral después de quitar el factor estructural del cierre; y (iii) implique una cota puntual suficiente para `π(x)−li(x)=O(√x log x)`, o produzca un contraejemplo al propio criterio propuesto.

La energía por período conocida en R–01/R–02,

\[
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)E_k(x/p)\rangle=\frac1p\langle E_k^2\rangle,
\]

no cumple aún la condición (ii): es una media sobre períodos completos, mientras el cierre de la criba utiliza ventanas muy pequeñas respecto de `M_k`. Queda como **candidato de laboratorio**, no como prueba de una nueva cota.

### Protocolo de verificación

1. Integrar **independientemente** la discrepancia `E_S(x)` sobre intervalos de longitud uno, controlar explícitamente la cola y contrastar con (R03.1); verificar además la reconstrucción (R03.3).
2. Verificar el factor no nulo en ceros conocidos; esta comprobación no certifica todos los ceros.
3. Verificar la simetría de `H`, mostrar que `H_S=H P_S` suele romper la reflexión, y comprobar las dos simetrías y los cuatro ceros de `\widehat H_S=H P_S(s)P_S(1−s)`.
4. Medir el condicionamiento `|P_S(σ)|^{-1}` al aumentar `S`.
5. Mantener separadas: prueba simbólica, control numérico y problema abierto.

### Resultado de la integración independiente

El script `verificacion_R03.py` calcula `A_S(n)` directamente a partir de coprimalidad, integra exactamente en cada tramo entero la función lineal `E_S(x)=A_S(n)−δ_S x` (con aritmética de punto flotante) y controla la cola por periodicidad y media cero. Se evaluaron `S={2}`, `{2,3}`, `{2,3,5}` en `s=0.7` y `s=0.7+2.4i`, con corte `N=240000`, múltiplo de los tres períodos. El mayor error observado frente a la expresión de Mellin fue inferior a `4.8×10^−10`; la mayor cota analítica de la cola fue inferior a `1.5×10^−7`. Se permite un margen adicional de `2×10^−8` para el redondeo numérico, que no se presenta como cota rigurosa de la aritmética de máquina. Esta comprobación es independiente del **cálculo** de `F_S` por el lado derecho de (R03.1), pero no sustituye la demostración de la identidad.

## 8. Registro de resultados

| Afirmación | Estado |
|:--|:--|
| Ceros de `F_S` y `ζ` idénticos con multiplicidades para S finito | **Demostrado**, corolario de Mellin |
| Recuperación normalizada `F_S/P_S=ζ/s` | **Demostrado** |
| Cotas de estabilidad y pérdida de uniformidad al crecer S | **Demostrado** |
| Simetría más herencia finita no bastan por sí solas para localizar ceros | **Demostrado mediante filtro simetrizado y control** |
| Integración independiente de Mellin y cota de cola | **Verificación numérica**, no una prueba de RH |
| Todos los ceros de `ζ` en la línea `1/2` | **Abierto**, hipótesis de Riemann |
| Reducción demostrada del costo total de reconocer esos ceros | **Abierto** |

## Referencias y procedencia

- [R–01/R–02, «Las escalas relacionales de la criba», edición publicada de 17-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposición 1; §5, Proposición 2; §7, fórmula explícita.
- [«Un número por cero», edición publicada](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8, 11–13: radio, espejo y lectura del dato suplementario.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, para la identidad clásica de Mellin.
- H. Davenport, *Multiplicative Number Theory*, para las propiedades de la función zeta y el producto de Euler.

**Firma pública:** Le Matt Ansatz Di Ego.

**Nota de alcance.** R–03 es una explicitación y un control de los mecanismos de la publicación anterior. No reivindica una prueba de la hipótesis de Riemann ni originalidad de las identidades clásicas.
