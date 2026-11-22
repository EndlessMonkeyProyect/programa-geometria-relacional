# Reflexión, frontera y coherencia del recierre aritmético

**Anexo de correspondencias y ensayo de transferencia**  
**Fecha:** 22 de noviembre de 2026  
**Continuidad:** Núcleo Generativo Canónico → CME–002 → Compendio Riemann–CME (Proposición F) → RA–01 / CR–6 → HC–02/03 → *Del principio de diferencia al recierre aritmético*  
**Estado:** identidades y proposiciones algebraicas **demostradas**; tablas **verificadas finitamente**; condición cuantitativa global **equivalente a una formulación clásica de RH y aún abierta**.  
**Función editorial:** anexo de correspondencias; preserva intactas las demostraciones previas y especifica la interfaz matemática de transferencia.

## Resumen

El principio de reflexión se realiza aritméticamente como una involución que intercambia la ausencia y presencia de un factor primo en un número libre de cuadrados. Esa involución invierte un signo binario, conserva la norma en una representación por permutaciones de estados y traslada la pareja reflejada a través de la frontera de cada octava. De esta estructura se deduce una identidad exacta: la suma de Möbius hasta una escala es igual a la suma de las orientaciones que permanecen en su frontera relativa a cualquier primo de referencia. La cantidad contenida en esa frontera puede medirse mediante la coherencia entre un vector de orientaciones normalizado y una familia de consultas de prefijos. La exigencia asintótica sobre esa coherencia equivale al criterio clásico de la hipótesis de Riemann (RH); la identidad de reflexión, por sí sola, determina el recierre y la ubicación de la información, no su tasa universal de compensación.

## 1. Principio y procedencia

La cadena generativa de septiembre se formula como totalidad → reflexión → diferencia → comparación → residuo → cierre → herencia y novedad → nueva referencia. La diferencia mínima binaria, la conservación de información y el carácter recursivo de la referencia pertenecen a esa formulación. En las realizaciones posteriores se distinguen las operaciones siguientes:

- **Reflexión:** intercambio involutivo entre dos orientaciones de una referencia.
- **Memoria:** una comparación conserva el origen y las relaciones ya acreditadas.
- **Recierre local:** una nueva referencia completa un conjunto de comparaciones y anula un defecto local.
- **Consulta:** una operación concreta pregunta cuánto de la información permanece orientado en cierta frontera.

El *Compendio Riemann–CME* del **21-XI-2026**, §4, ya contiene y demuestra la Proposición F: para `N<m≤2N`, `J_N(m)=-μ(m)` y `J_{2N}(m)=0`. Las *Notas de publicación v3.5* también registran esa identidad. Su repetición en la nota del 22-XI es **trazabilidad**, no prioridad ni resultado matemático nuevo. En HC–03 está demostrado el operador de aparición `Δ²T(n)=Λ(n)/n`, para otro contrato aritmético. En RA–01 se demuestra el criterio condicional de cierre a partir de ganancias de proyección.

## 2. Realización de la orientación binaria

Sea `S={n≥1: μ(n)≠0}` el conjunto de enteros libres de cuadrados. Para cada primo `p`, definamos

\[
T_p(n)=\begin{cases}pn,&p\nmid n,\\ n/p,&p\mid n,\end{cases}\qquad n\in S.
\tag{1}
\]

**Proposición 1 (reflexión del soporte primo; demostración elemental).** Para cada primo `p` y todo `n∈S`:

\[
\boxed{T_p^2(n)=n,\qquad \mu(T_p(n))=-\mu(n).}\tag{2}
\]

Además, `T_p T_q=T_q T_p` para primos distintos `p,q`.

**Demostración.** En un entero libre de cuadrados, el exponente de `p` es cero o uno. `T_p` conmuta esos dos valores y deja los demás exponentes intactos. Por tanto es involutivo y conmuta con los intercambios de otros primos. La fórmula `μ(n)=(-1)^{ω(n)}` sobre `S` cambia de signo al variar exactamente un factor. `□`

**Corolario 1 (unidad conservada).** En `ℓ²(S)` con base ortonormal `{e_n}`, la transformación `U_p e_n=e_{T_p(n)}` se extiende a un operador unitario involutivo:

\[
\boxed{U_p^2=I,\qquad \|U_p v\|_2=\|v\|_2.}\tag{3}
\]

El operador diagonal de orientación `D e_n=μ(n)e_n` satisface `D U_p=-U_p D`. Estas son igualdades exactas de una realización **aritmética** de reflexión. La identificación con los reflectores angulares del laboratorio CME–002 requiere, por separado, un morfismo que conserve sus relaciones de composición.

## 3. La frontera de la octava como efecto de la reflexión

**Proposición 2 (desplazamiento entre octavas).** Para `N<n≤2N` y un primo `p`, el número reflejado `T_p(n)` queda fuera de `(N,2N]`:

\[
\boxed{T_p(n)\le N\quad\text{o}\quad T_p(n)>2N.}\tag{4}
\]

**Demostración.** Si `p|n`, entonces `T_p(n)=n/p≤n/2≤N`. Si `p∤n`, entonces `T_p(n)=pn≥2n>2N`. `□`

Así, aunque la reflexión conserva la unidad del vector de estados, la **ventana diádica no es invariante** bajo ella. Especificando la proyección de frontera `P_I e_n=1_I(n)e_n`, su conmutador con la reflexión actúa por

\[
[P_I,U_p]e_n=\big(1_I(T_p n)-1_I(n)\big)e_{T_p n}.\tag{5}
\]

Para una octava `I=(N,2N]` y cualquier `n∈S∩I`, este vector tiene norma uno. Éste es el lugar exacto donde se distingue **norma global conservada** de **cantidad recuperable dentro de una consulta móvil**.

**Proposición 3 (identidad exacta de frontera).** Para todo primo `p` y real `X≥1`:

\[
\boxed{M(X)=\sum_{\substack{X/p<n\le X\\p\nmid n}}\mu(n),\qquad M(X)=\sum_{n\le X}\mu(n).}\tag{6}
\]

En particular,

\[
\boxed{M(X)=\sum_{\substack{X/2<n\le X\\ n\ \mathrm{impar}}}\mu(n).}\tag{7}
\]

**Demostración.** Toda contribución no nula de `M(X)` corresponde a un entero libre de cuadrados. Se agrupan las parejas `r,pr`, con `p∤r`. Si `r≤X/p`, ambos están en el prefijo y sus signos se compensan por (2). Cuando `X/p<r≤X`, únicamente el miembro `r` está en el prefijo. La suma de esas contribuciones da (6). `□`

**Interpretación precisa.** La reflexión cancela por parejas todas las contribuciones interiores que pueden emparejarse bajo el corte elegido. La suma total aparece íntegramente en una **frontera móvil**. La identidad fija dónde queda la diferencia recuperable; su amplitud depende de la orientación conjunta de los términos presentes en esa frontera.

## 4. Recierre local de Möbius — resultado previamente registrado

La comparación de divisores está dada por `d|m`. El defecto truncado es

\[
F_N(m)=\sum_{\substack{d\mid m\\ d\le N}}\mu(d).\tag{8}
\]

La Proposición F del compendio previo establece para `N<m≤2N`:

\[
\boxed{F_N(m)=-\mu(m),\qquad F_{2N}(m)=0.}\tag{9}
\]

La identidad `∑_{d|m}μ(d)=0` para `m>1` demuestra ambas ecuaciones: el único divisor que aún no se había incorporado es `m`. Por inversión de Dirichlet, la función con `a(1)=1` y `∑_{d|m}a(d)=0` para `m>1` es **únicamente** `a=μ`. Por eso el recierre local fija los coeficientes de orientación exactamente, y no solamente su patrón cualitativo.

Los saltos locales de (9), la suma de frontera de (6) y la distancia funcional `L²` de RA–01 son **tres observables distintos**; sus transformaciones mutuas deben documentarse cuando se usen para transferir cotas.

## 5. Coherencia de las orientaciones con una familia de consultas

Para cada octava `I_N=(N,2N]`, sean

\[
A_N=\sum_{N<n\le2N}\mu(n)^2,\qquad
S_N(t)=\sum_{N<n\le t}\mu(n),\quad N\le t\le2N.\tag{10}
\]

Para `A_N>0`, sobre `\mathbb R^N` definamos dos vectores normalizados respecto de la misma frontera:

\[
v_N=\frac{(\mu(N+1),\ldots,\mu(2N))}{\sqrt{A_N}},
\quad
w_{N,t}=\frac{(1_{N<n\le t})_{n=N+1}^{2N}}{\sqrt{N}}.\tag{11}
\]

Se cumplen `||v_N||₂=1` y `||w_{N,t}||₂≤1`. Su comparación es el **coeficiente de coherencia de prefijo**:

\[
\boxed{c_N(t)=\langle v_N,w_{N,t}\rangle
=\frac{S_N(t)}{\sqrt{N A_N}}.}\tag{12}
\]

**Proposición 4 (cota por conservación de unidad).** Para todos los prefijos,

\[
|c_N(t)|\le\sqrt{\frac{t-N}{N}}\le1.\tag{13}
\]

**Demostración.** Desigualdad de Cauchy–Schwarz y las normas de (11). `□`

Esta es la restricción universal que se obtiene *solo* de la unidad y la proyección. La aritmética de Möbius proporciona además un dato de densidad bien conocido:

\[
A_N=\frac{6}{\pi^2}N+O(\sqrt N),\tag{14}
\]

consecuencia de `μ²(n)=∑_{d²|n}μ(d)` y sumación elemental.

**Proposición 5 (equivalencia clásica expresada como coherencia).** La hipótesis de Riemann es equivalente a que para **cada** `ε>0` exista una constante `C_ε` tal que, para todo entero diádico `N=2^j` suficientemente grande y **todo** `t∈[N,2N]`, se tenga

\[
\boxed{\sup_{N\le t\le2N}|c_N(t)|
\le C_\varepsilon N^{-1/2+\varepsilon}.}\tag{15}
\]

**Demostración.** El criterio clásico `RH ⇔ M(x)=O_ε(x^{1/2+ε})` para todo `ε>0` implica `S_N(t)=M(t)-M(N)=O_ε(N^{1/2+ε})` en cada octava. La cota inferior `A_N\ge cN` para `N` grande, consecuencia de (14), transforma esta estimación en (15). Recíprocamente, como `A_N≤N`, (12) y (15) implican `|S_N(t)|≤C_ε N^{1/2+ε}`. Toda suma `M(x)` se descompone en una suma de bloques diádicos completos y el prefijo de uno más; la serie geométrica da la misma cota para `M(x)`, equivalente a RH. `□`

La Proposición 5 es una **reexpresión geométrica de una equivalencia clásica**, no una demostración independiente de RH. Explicita la obligación: mientras la conservación de la unidad solo da `|c_N|≤1`, la conclusión crítica exige un **decaimiento asintótico de su alineación con todas las consultas de prefijo**.

## 6. Ensayo finito y trazabilidad

El script `scripts/verificar_coherencia.py` comprueba con enteros exactos las proposiciones de recierre local, unicidad, reflexión por primos y frontera móvil; calcula `A_N`, la suma firmada final `S_N(2N)`, el máximo de prefijos `B_j=max_t|S_N(t)|` y la coherencia máxima para `N=2^j`, `4≤j≤17`.

| Octava `(N,2N]` | `A_N` | `B_j` | `max|c_N(t)|` |
|---:|---:|---:|---:|
| `(512,1024]` | 310 | 11 | 0,027611 |
| `(1024,2048]` | 621 | 17 | 0,021318 |
| `(2048,4096]` | 1246 | 32 | 0,020032 |
| `(16384,32768]` | 9958 | 105 | 0,008220 |
| `(131072,262144]` | 79672 | 145 | 0,001419 |

**Controles realizados:** 4.160 identidades enteras de recierre; 511 comprobaciones de unicidad de `μ`; 2.320 controles de reflexión y frontera; 14 bloques diádicos con cálculos exactos de recuentos y máximos (`B_j`). Los coeficientes se imprimen en decimal a partir de cocientes cuadrados racionales exactos. Coinciden los casos previamente registrados `N=1024` y `N=2048` del Compendio Riemann–CME.

Las comprobaciones finitas contrastan las ecuaciones; la condición asintótica (15) conserva su estado abierto.

## 7. Contrato de transferencia y siguiente obligación

La investigación fundacional debe concentrarse en la correspondencia entre **reflexión que preserva la unidad** y **consultas que cambian de frontera**. Un camino verificable consta de:

1. Identificar la transformación exacta de cada consulta de prefijo bajo `U_p`, a partir del conmutador (5) y de la identidad de frontera (6).
2. Estudiar si la composición de las transformaciones, junto con la multiplicatividad y la inversión de Möbius ya fijadas, produce una desigualdad cuantitativa para `c_N(t)` que no suponga la cota que se pretende deducir.
3. Si se busca transferencia a RA–01, construir y acotar un operador explícito que envíe el defecto de divisibilidad y sus consultas a las ganancias de proyección funcional en `L²`; la mera similitud entre normas no equivale a esa transferencia.

**Resultado disponible:** las identidades (2), (3), (4), (6), (9), (12) y la equivalencia (15). **Cuestión matemática abierta:** deducir la tasa de (15) desde principios aritméticos demostrables. Esa tasa es precisamente la dificultad equivalente a RH.

## 8. Procedencia y bibliografía interna

- *Núcleo Generativo Canónico*, septiembre de 2026, P0–P6, §10 y §12: reflexión, comparación, herencia, novedad y realización binaria.
- *Compendio Riemann–CME*, 21-XI-2026, §4.1, Proposición F (recierre de Möbius); §§3, 8–9 (norma de proyecciones, correspondencias y límites de transferencia).
- *Notas de publicación v3.5*, 21-XI-2026: registro de recierre local y RA–01.
- *Nota de auditoría RA–01 v5*, 21-XI-2026: criterio óptimo de contracción; suficiencia de semillas.
- *HC–03*, 21-XI-2026: reconstrucción exacta de las contribuciones de von Mangoldt por diferencias finitas.
- *Del principio de diferencia al recierre aritmético*, 22-XI-2026: primera integración explícita del recierre local con la suma firmada por octavas.
- Identidades aritméticas clásicas: inversión de Möbius, densidad de enteros libres de cuadrados, y criterio de Mertens `M(x)=O_ε(x^{1/2+ε}) ⇔ RH`.

---

**Endless Monkey Project / Relational Geometry Program**
