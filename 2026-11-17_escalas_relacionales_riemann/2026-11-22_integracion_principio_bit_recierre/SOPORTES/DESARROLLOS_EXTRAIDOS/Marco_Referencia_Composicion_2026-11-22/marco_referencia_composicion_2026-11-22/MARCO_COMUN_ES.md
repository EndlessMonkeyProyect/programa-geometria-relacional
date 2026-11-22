# Referencia, composición, residuo y control de escala

**Nota matemática de comparación transversal — 22 de noviembre de 2026**  
**Ámbito:** aritmética de potencias primas (Riemann), contratos de continuación (P frente a NP) y composiciones de `SU(2)` (Yang–Mills).  
**Estado:** siete proposiciones con demostraciones; condiciones globales identificadas; comparación transversal estructural.  
**Tipo:** manuscrito técnico para revisión, con comprobaciones finitas reproducibles.

## Resumen

Se desarrolla un lenguaje común para estudiar la conservación de información bajo composición y el residuo necesario para actualizar una referencia. El primer ejemplo se obtiene de las equivalencias por continuaciones de un sistema de consultas. El segundo adopta la forma de acarreos modulares y permite probar una cota óptima de desbalance por período. El tercero es el defecto de conmutación de dos matrices de `SU(2)`, cuyo módulo se expresa mediante una traza gauge-invariante. En la especialización aritmética se demuestra una identidad exacta entre la desviación conjunta de acarreos y la función de Chebyshev, que conduce a un criterio equivalente a la hipótesis de Riemann. Los objetos aritméticos, computacionales y gauge admiten una misma organización de preguntas; cada uno conserva sus hipótesis y su condición de control global.

## 1. Definiciones y contrato de comparación

Sea `X` un monoide de configuraciones con producto asociativo, neutro `e`, y sea `O:X→Y` una consulta declarada. Para `x,y∈X` se define la equivalencia de contexto bilateral

\[
x\equiv_O y \quad\Longleftrightarrow\quad
O(uxv)=O(uyv)\quad \text{para todo }u,v\in X.
\]

Una referencia es una función de resumen `σ:X→Q`. Una ley de composición enriquecida por residuo consiste en funciones `κ:X×X→K` y `D:Q×Q×K→Q` que cumplen

\[
\sigma(xy)=D\bigl(\sigma(x),\sigma(y),\kappa(x,y)\bigr).
\tag{1}
\]

La utilidad operativa de un resumen depende de las dimensiones y de los costos de construir `σ`, obtener `κ` y aplicar `D`. La ecuación (1) registra la propiedad de reconstrucción; el costo es una condición adicional explícita.

### Proposición 1. Congruencia de las observaciones en todos los contextos

La relación `≡_O` es una congruencia del monoide `X`. En consecuencia, el producto de clases ` [x][y]=[xy] ` está bien definido en `X/≡_O`, y la consulta `O` es constante sobre cada clase.

**Demostración.** Reflexividad, simetría y transitividad se heredan de la igualdad en `Y`. Si `x≡_O y` y `w,z∈X`, para todo `a,b∈X` se tiene

\[
O(a(wxz)b)=O((aw)x(zb))=O((aw)y(zb))=O(a(wyz)b).
\]

Luego `wxz≡_O wyz`; en particular la equivalencia se conserva al multiplicar a izquierda o derecha. Por composición se obtiene la buena definición del producto cociente. La elección de `u=v=e` da `O(x)=O(y)`. ∎

**Lectura para P frente a NP.** El cociente identifica distinciones que ninguna continuación admitida puede recuperar. Para obtener consecuencias de complejidad es necesario proporcionar un método de construcción y actualización del resumen con cotas de tiempo y memoria para la clase de instancias estudiada.

## 2. Residuo modular y acarreos

Para un entero `q≥2`, escribimos `n=q h_q(n)+r_q(n)`, con `0≤r_q(n)<q`. Definimos

\[
\kappa_q(a,b)=\left\lfloor\frac{r_q(a)+r_q(b)}q\right\rfloor\in\{0,1\}.
\]

### Proposición 2. Reconstrucción exacta por acarreo

Para enteros no negativos `a,b`:

\[
r_q(a+b)\equiv r_q(a)+r_q(b)\pmod q,
\quad h_q(a+b)=h_q(a)+h_q(b)+\kappa_q(a,b).
\tag{2}
\]

**Demostración.** Sustituir `a=qh_q(a)+r_q(a)` y `b=qh_q(b)+r_q(b)` en `a+b` y efectuar la división euclídea de `r_q(a)+r_q(b)` entre `q`. Su cociente es `κ_q(a,b)` y su resto es `r_q(a+b)`. ∎

### Proposición 3. Identidad de coherencia del residuo (cociclo)

Para todos `a,b,c≥0`:

\[
\boxed{\kappa_q(a,b)+\kappa_q(a+b,c)
=\kappa_q(b,c)+\kappa_q(a,b+c).}
\tag{3}
\]

**Demostración.** Calcular `h_q(a+b+c)` con (2), primero agrupando `(a+b)+c` y luego `a+(b+c)`. Los términos `h_q(a)+h_q(b)+h_q(c)` son idénticos y se cancelan, dejando (3). ∎

**Interpretación.** La información residual de una composición se actualiza de manera coherente bajo reagrupación. Esta identidad es una propiedad algebraica de los acarreos; los residuos de otros sistemas requieren su propia ley.

## 3. Frecuencia y desbalance de las activaciones

Se define la activación de una referencia modular `q` por

\[
c_q(m)=\kappa_q(m,m)
=\left\lfloor\frac{2m}{q}\right\rfloor-2\left\lfloor\frac{m}{q}\right\rfloor.
\tag{4}
\]

Para un intervalo consecutivo `m=a,a+1,…,a+N−1`, se define

\[
\alpha_q=\frac{\lfloor q/2\rfloor}{q},\qquad
D_q(a,N)=\sum_{m=a}^{a+N-1}c_q(m)-N\alpha_q.
\]

### Proposición 4. Cota óptima por período

La sucesión `c_q` tiene período `q`, exactamente `k=⌊q/2⌋` activaciones consecutivas en cada período, y verifica

\[
\boxed{|D_q(a,N)|\leq \frac{k(q-k)}q
=\frac{\lfloor q/2\rfloor\lceil q/2\rceil}{q}.}
\tag{5}
\]

La constante se alcanza para un intervalo de longitud `k` que coincide con el bloque activo.

**Demostración.** De (4), `c_q(m)=1` precisamente cuando `r_q(m)≥⌈q/2⌉`. Si `N=tq+r` con `0≤r<q`, los `t` períodos enteros contribuyen desbalance cero. En un intervalo residual de longitud `r`, el número de activaciones está entre `max(0,r−(q−k))` y `min(r,k)`. Restando `rk/q`, el máximo de la desviación positiva y de la negativa está acotado por `k(q−k)/q`; ambos extremos se obtienen al tomar, respectivamente, `r=k` sobre el bloque activo o `r=q−k` sobre el bloque inactivo. ∎

### Proposición 5. Distribución conjunta para módulos coprimos

Si `q_1,…,q_s` son coprimos dos a dos, la distribución uniforme de `m` en un período de longitud `Q=q_1⋯q_s` hace independientes las variables `c_{q_i}(m)` y

\[
\frac1Q\#\{0\le m<Q:c_{q_i}(m)=1\ \forall i\}
=\prod_{i=1}^s\alpha_{q_i}.
\tag{6}
\]

**Demostración.** El teorema chino del resto establece la biyección entre clases módulo `Q` y tuplas de clases módulo `q_i`. Cada conjunto activo posee `⌊q_i/2⌋` residuos. Contar las tuplas activas y dividir entre `Q` da (6). ∎

**Alcance.** Las potencias de un mismo primo pueden presentar dependencias. Ejemplo: para `q=3` y `q=9`, la frecuencia conjunta es `2/9`, frente al producto `α_3 α_9=4/27`. La independencia coprima tampoco da, por sí sola, una cota uniforme del desbalance ponderado para intervalos de longitud arbitraria.

## 4. Composición no conmutativa de `SU(2)`

Para `U,V∈SU(2)`, se define el conmutador de grupo y su observable:

\[
C(U,V)=UVU^{-1}V^{-1},\quad
\nu(U,V)=1-\tfrac12\operatorname{ReTr}C(U,V).
\]

### Proposición 6. Defecto de conmutación y covariancia

\[
\boxed{\nu(U,V)=\tfrac14\|UV-VU\|_F^2,
\quad 0\le\nu(U,V)\le2.}
\tag{7}
\]

El observable se anula si y solo si `UV=VU`, y es invariante bajo conjugación simultánea `U↦gUg^{-1}`, `V↦gVg^{-1}` para `g∈SU(2)`.

**Demostración.** Al expandir la norma de Frobenius con `U†=U^{-1}` y `V†=V^{-1}` se obtiene `||UV−VU||_F²=4−2ReTr(UVU^{-1}V^{-1})`. Esto da la primera igualdad y la caracterización del cero. La traza de un elemento de `SU(2)` es real y pertenece a `[-2,2]`, por lo que `0≤ν≤2`. Finalmente, `C(gUg^{-1},gVg^{-1})=g C(U,V)g^{-1}` y la ciclicidad de la traza prueba la invariancia. ∎

**Distinción algebraica.** `κ_q` es un acarreo entero que satisface (3); `ν` es una norma cuadrática de un defecto no conmutativo. La correspondencia se encuentra en la necesidad de registrar información contextual al componer, no en la igualdad de los residuos ni en sus leyes de escala.

## 5. Especialización aritmética y condición de Riemann

Sean `m≥1` entero, `ψ(x)=∑_{p^j≤x}log p`, `E(x)=ψ(x)−x`, y

\[
S(m)=\sum_{p^j\le m}(c_{p^j}(m)-\alpha_{p^j})\log p,
\qquad H_{\mathrm{odd}}(m)=\sum_{\substack{p\text{ impar},\ j\ge1\\p^j\le m}}\frac{\log p}{p^j}.
\]

### Proposición 7. Identidad global de los acarreos y criterio equivalente

Para todo `m≥1` se cumple la identidad exacta

\[
\boxed{S(m)=\log\binom{2m}{m}-\psi(2m)
+\tfrac12\psi(m)+\tfrac12H_{\mathrm{odd}}(m).}
\tag{8}
\]

Además, cuando `m→∞`,

\[
\boxed{S(m)-\bigl(2\log2-\tfrac32\bigr)m
=-E(2m)+\tfrac12E(m)+O(1).}
\tag{9}
\]

Por consiguiente, el siguiente criterio es equivalente a la hipótesis de Riemann:

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
S(m)-\bigl(2\log2-\tfrac32\bigr)m
=O\bigl(\sqrt m\log^2m\bigr).}
\tag{10}
\]

**Demostración de (8).** La fórmula de Legendre da

\[
\log\binom{2m}{m}=\sum_{p^j\le2m}
\Bigl(\lfloor2m/p^j\rfloor-2\lfloor m/p^j\rfloor\Bigr)\log p.
\]

Los términos con `p^j>m` y `p^j≤2m` valen uno y suman `ψ(2m)−ψ(m)`. Los restantes son las activaciones `c_{p^j}(m)`. Como `α_{2^j}=1/2` y, para `p` impar, `α_{p^j}=1/2−1/(2p^j)`, se tiene

\[
\sum_{p^j\le m}\alpha_{p^j}\log p
=\tfrac12\psi(m)-\tfrac12H_{\mathrm{odd}}(m).
\]

Restar ambas igualdades da (8). ∎

**Demostración de (9).** La fórmula de Stirling proporciona

\[
\log\binom{2m}{m}=2m\log2-\tfrac12\log(\pi m)+O(m^{-1}).
\]

La estimación clásica de Mertens `∑_{p≤m}log p/p=log m+O(1)` y la convergencia de `∑_{p,j≥2}log p/p^j` implican `H_odd(m)=log m+O(1)`. Sustituir en (8) y escribir `ψ(x)=x+E(x)` demuestra (9). ∎

**Demostración de (10).** Bajo RH, el criterio clásico de von Koch afirma `E(x)=O(√x log²x)`; aplicado a (9) da la cota sobre `S`. Recíprocamente, supóngase esa cota para todos los enteros suficientemente grandes. Por (9) se obtiene

\[
E(2m)=\tfrac12 E(m)+O(\sqrt m\log^2m).
\]

Para un índice impar `n=2m+1`, la diferencia `E(n)−E(n−1)=Λ(n)−1=O(log n)` permite trasladar la relación anterior desde `2m` hasta `n`. Así, para cualquier entero suficientemente grande,

\[
E(n)=\tfrac12E(\lfloor n/2\rfloor)+O(\sqrt n\log^2 n).
\]

La iteración a través de `⌊n/2⌋,⌊n/4⌋,…` da una suma geométrica de errores, acotada por

\[
O\left(\sqrt n\log^2 n\sum_{j\ge0}(2\sqrt2)^{-j}\right)
=O(\sqrt n\log^2n).
\]

Para `x` real, `ψ(x)=ψ(⌊x⌋)` extiende la misma cota a `E(x)`, y el criterio clásico concluye RH. ∎

**Observación cuantitativa.** El término sistemático vale `(2log2−3/2)m≈−0.1137056389m`. La prueba de (10) formaliza la equivalencia de dos enunciados; establecer su estimación para todos los enteros grandes es la condición de investigación.

## 6. Convergencia formal y condiciones específicas

| Dominio | Referencia y operación | Objeto exacto | Resultado probado | Condición global de la investigación |
|---|---|---|---|---|
| Aritmética / Riemann | Residuos módulo potencias primas; adición | Acarreo `κ_q` y activación `c_q` | (2)–(6), (8)–(10) | Estimación de (10), uniforme en `m` |
| P frente a NP | Contratos de consulta y continuaciones; composición de restricciones | Clases de equivalencia y refinamientos de interfaz | Congruencia contextual (proposición 1) | Cotas de construcción, actualización y decisión para instancias generales |
| Yang–Mills | Holonomías; multiplicación no abeliana | Conmutador `C` y `ν` | Identidad e invariancia de (7) | Control coercivo uniforme y construcción del límite cuántico con brecha espectral |

El principio transversal verificable es que una referencia admite una ley de composición correcta cuando la información que se conserva y el residuo necesario están determinados bajo un contrato observacional. La transferencia de cotas depende de las hipótesis cuantitativas de cada dominio.

## 7. Procedencia y estado de las afirmaciones

| Elemento | Procedencia matemática | Estado en esta nota |
|---|---|---|
| Congruencia por contextos y cociente | Álgebra de monoides / semántica de observaciones | Prueba directa bajo las hipótesis declaradas |
| Acarreo modular y cociclo | División euclídea | Identidad clásica, prueba directa |
| Cota óptima periódica | Conteo de bloques consecutivos | Prueba directa para la familia `c_q` |
| Independencia en períodos coprimos | Teorema chino del resto | Prueba directa |
| Conmutador `SU(2)` y traza | Álgebra matricial y teoría gauge | Identidad clásica, prueba directa |
| Desviación conjunta `S` | Legendre, Stirling, Mertens, Chebyshev | Reformulación exacta y reducción a von Koch |
| Enlace simultáneo con P vs NP / Yang–Mills | Comparación estructural | Programa de investigación con contratos diferenciados |

**Referencias primarias de comparación documental:**

1. [¿Qué diferencias deben sobrevivir? — P vs NP (10/11 nov 2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-11_reflexion_mecanismo_p_np/REFLEXION_MECANISMO_P_NP.md).
2. [Yang–Mills: composición no abeliana y comparaciones sobre estados](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/06_yang_mills/README.md).
3. [Escalas relacionales y la hipótesis de Riemann](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-17_escalas_relacionales_riemann).

**Referencias matemáticas externas:** [Mertens — notas de teoría analítica de números](https://zteitler.github.io/analytic-number-theory-notes/sec-mertens.html); [Equivalencias clásicas de RH — Mathematical Association of America](https://old.maa.org/node/1401175).

## 8. Comprobaciones reproducibles

Ejecutar desde esta carpeta:

```bash
python3 verificar_marco.py
```

El verificador utiliza aritmética entera y racional en las propiedades discretas y matrices complejas con coeficientes enteros para el ejemplo `SU(2)`. La prueba de los cuantificadores infinitos se establece en las demostraciones; las pruebas de código son controles finitos de implementación.

---

**Endless Monkey Project / Relational Geometry Program**
