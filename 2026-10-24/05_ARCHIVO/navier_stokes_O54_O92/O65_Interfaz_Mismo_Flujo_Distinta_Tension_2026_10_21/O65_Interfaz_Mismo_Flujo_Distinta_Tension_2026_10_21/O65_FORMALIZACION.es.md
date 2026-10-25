---
title: "O65 — La misma corriente, diferentes condiciones interfaciales"
subtitle: "Discriminación física por tensión superficial, comparadores suficientes y alcance del cierre relacional"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento independiente: solución exacta bifásica particular, diagnóstico Hinze condicionado, pruebas reproducibles; no es DNS bifásica"
parents: ["O40", "O45", "O53", "O58", "O60", "O61", "O62", "O63", "O64", "Imagen Total v3.8.1"]
---

# O65 — La misma corriente, diferentes condiciones interfaciales

## 0. Conclusión central y contrato de lectura

El planteamiento viene de O64: mantener **el mismo flujo** y variar exclusivamente una condición de la frontera que distingue interior y exterior de una gota: su tensión superficial `σ`. Queremos saber si la comparación basta para acreditar una novedad física y qué información debe conservar un normalizador orientado a preguntas sobre fragmentación.

**Resultado:** en el diagnóstico turbulento Kolmogorov–Hinze, para el mismo flujo de referencia (`ρ_c` y tasa disipativa `ε` fijas), la escala crítica depende de `σ^{3/5}`; así, **la geometría y los datos de flujo solamente no son una interfaz predictiva suficiente para esta pregunta**. En contraste, existe una **solución exacta particular** de Navier–Stokes bifásico donde cambiar `σ` cambia el salto de presión pero no deforma ni rompe la gota. Por tanto la diferencia de tensión introduce una condición física que *puede* alterar la respuesta bajo ciertas condiciones, no una necesidad universal de ruptura.

Etiquetas: **[O]** ontología atribuida al programa; **[T]** identidad/teorema exacto bajo hipótesis; **[M]** modelo de umbral empírico/dimensional; **[E]** cómputo numérico del modelo, no experimento físico; **[F]** falsador de una interfaz insuficiente; **[A]** pregunta abierta.

No hemos demostrado tamaño mínimo de gota, selección natural de `A₀` o de un entero `N`, condición universal de persistencia, ni regularidad global de NS 3D.

## 1. Ontología primero: unidad, totalidad y referencia

En el programa, las relaciones pueden existir aunque ninguna imagen particular las habite. El cierre propio de una unidad no agota la totalidad. Una referencia puede permitir reconstruir las relaciones ya acreditadas en otra escala y dejar novedad todavía pendiente. La dirección geométrica es consecuencia del cierre relacional, no la fuente ontológica de la unidad.

La pregunta física no es «¿se conserva el ángulo de dos direcciones?» ni «¿podemos contar cuadrados?», sino **qué datos deben permanecer dentro de la comparación para no confundir unidades que responden distinto a la misma corriente**. Una gota incorpora una frontera física con costo de área `σ A`; a diferencia de O53, no se trata de un vórtice monofásico que pretendamos llamar gota por semejanza.

El espejo móvil puede cambiar coordenadas o escalas de observación. Un cambio de referencia **no debe confundirse** con variar efectivamente la tensión superficial, que es una diferencia física entre preparaciones.

## 2. Primer control: misma corriente física, solución exacta en dos fases [T]

Sea un dominio periódico suficientemente grande para contener una esfera de radio `s>0`, advectada con rapidez constante `U∈R³` (las coordenadas se interpretan periódicamente). Tomamos en ambas fases velocidad constante:

\[
\boxed{u_1(x,t)=u_2(x,t)=U,\qquad \Gamma(t)=\partial B_s(Ut).}\tag{65.1}
\]

Para cada `σ>0`, elegimos presiones constantes por fase tales que

\[
\boxed{p_{\rm in}=p_{\rm out}+\frac{2\sigma}{s}.}\tag{65.2}
\]

En el interior y exterior se cumplen **exactamente** las ecuaciones incompresibles bifásicas sin forzamiento: `∂_t u=0`, `(u·∇)u=0`, `Δu=0`, `∇·u=0`, `∇p=0`. La interfaz satisface la condición cinemática `\dot\Gamma=U` y el salto de tensión normal `p_in−p_out=σ(1/s+1/s)` (tomada la convención de orientación apropiada); al ser `D(u)=0`, no hay esfuerzos viscosos. Así, **la misma geometría material y velocidad son compatibles con infinitos valores de tensión superficial**, variando la diferencia de presión interfacial.

**Teorema O65-T1.** Bajo el contrato anterior, un cambio de `σ` no obliga a ruptura, cambio de radio ni activación de deformación, aunque produce un cambio físico en `Δp` y en la energía superficial `σ A`.

**Límite:** esto no es una solución turbulenta ni garantiza que una gota real permanezca intacta frente a esfuerzos del entorno. Precisamente evita deducir `ruptura ⇐ σ cambió`.

Para `d=5 mm`, `s=d/2`, los saltos de presión `4σ/d` son respectivamente `28,8`, `57,6` y `115,2 Pa` para `σ∈{0,036;0,072;0,144} N/m`, sin cambio geométrico en esta solución exacta.

## 3. Segundo control: mismo flujo turbulento de referencia, distinto umbral [M]

**Hipótesis de régimen:** fase continua de densidad `ρ_c>0`; turbulencia aproximadamente homogénea/isótropa; la escala `d` está en el rango inercial; una gota diluida no modifica sensiblemente el campo turbulento impuesto (comparación *de una vía*); tensión interfacial constante; coeficiente empírico `C_H` mantenido entre preparaciones. Viscosidad relativa, surfactantes y coalescencia pueden sacar el sistema del régimen.

A escala `d` tomamos una diferencia de velocidad característica `δu_d²=(ε d)^{2/3}`; esta es una convención de normalización para el Weber modelo, no una igualdad universal de fluctuaciones locales. Definimos

\[
\boxed{We_0(d)=\frac{\rho_c\varepsilon^{2/3}d^{5/3}}{\sigma}.}\tag{65.3}
\]

Para la escala Hinze con `C_H≈0,725` (constante empírica, **no deducida** de la ontología):

\[
\boxed{d_H=C_H(\sigma/\rho_c)^{3/5}\varepsilon^{-2/5}.}\tag{65.4}
\]

**Teorema algebraico O65-T2 condicionado al modelo:** con `ρ_c,ε,C_H` fijos y dos tensiones `σ_1,σ_2>0`,

\[
\boxed{\frac{d_{H,2}}{d_{H,1}}=\left(\frac{\sigma_2}{\sigma_1}\right)^{3/5},\quad
\frac{We_0(d;\sigma_2)}{We_0(d;\sigma_1)}=\frac{\sigma_1}{\sigma_2}.}\tag{65.5}
\]

Este exponente de escala es exacto **dentro del modelo**, pero el propio criterio de fragmentación es una estimación estadística, **no una regla determinista de supervivencia de cada gota**.

Si se adopta la convención (65.3), `We_{0,crit}=C_H^{5/3}≈0,5851` y

\[
\boxed{\frac{We_0(d)}{We_{0,crit}}=\left(\frac{d}{d_H}\right)^{5/3}.}\tag{65.6}
\]

**Nota de convención:** otros trabajos introducen un factor de segundo orden de estructura en `δu²` (por ejemplo, 2); su `We_crit` cambia conjuntamente. La predicción robusta del ensayo bajo la misma convención es la razón (65.5), no el valor absoluto de `We_crit`.

### Resultados calculados [E]

Supuestos ilustrativos, **no medidos en O53**: `ρ_c=1000 kg/m³`, `μ_c=0,001 Pa·s`, `ε=0,1 m²/s³`, `d=5 mm`, `C_H=0,725`. Elijo `σ=0,036,0,072,0,144 N/m` a propósito para una prueba de sensibilidad; **no son tres mediciones del mismo líquido real**, y `0,144 N/m` no se afirma que corresponda a agua ordinaria.

| σ (N/m) | Hinze d_H (mm) | We_0/We_crit (d=5mm) | Δp esfera (Pa) | Aumento energía de área al dividir en 2 (μJ) |
|---:|---:|---:|---:|---:|
| 0,036 | 3,9275 | 1,4954 | 28,8 | 0,7349 |
| 0,072 | 5,9530 | 0,7477 | 57,6 | 1,4698 |
| 0,144 | 9,0231 | 0,3738 | 115,2 | 2,9396 |

**Lectura limitada:** con el `d=5 mm` fijado, el caso de tensión baja está *sobre* el umbral modelo de fragmentación, mientras los otros están *debajo*. La corriente de referencia no ha cambiado. Una probabilidad real de ruptura exige cálculo bifásico, distribución de esfuerzos/tiempos, condiciones iniciales y mecanismos de coalescencia. Estas tres etiquetas no certifican una ruptura o supervivencia individual.

Los tres casos mantienen exactamente el mismo valor de la escala microscópica de Kolmogorov del **flujo impuesto**: `η=(ν³/ε)^{1/4}=0,05623 mm`. Es importante: cambia el umbral **de interfaz**, no la disipación del portador.

## 4. El costo físico y el límite por la totalidad [T/H]

Una gota esférica de diámetro `d` tiene área `A=πd²`. Si se divide en dos gotas esféricas iguales conservando volumen, `ΔA=πd²(2^{1/3}−1)>0` y

\[
\boxed{\Delta E_\sigma=\sigma\pi d^2(2^{1/3}-1).}\tag{65.7}
\]

La diferencia entre preparaciones es exacta, condicionada a geometrías final e inicial esféricas; no determina la ruta dinámica real.

En un dominio bifásico cerrado sin trabajo externo y bajo supuestos de suavidad, la energía total satisface formalmente

\[
\frac{d}{dt}\Big(K_1+K_2+\sigma A\Big)=-\sum_i\int 2\mu_i|D(u)|^2\,dV.\tag{65.8}
\]

**Esto sí explica físicamente un límite contextual:** si la energía total disponible está acotada, la creación de área tiene un costo y no puede exceder arbitrariamente un presupuesto fijo. **Pero** esto no demuestra que sólo quede `1` celda, que los radios posean múltiplos enteros, ni que la gota posea un tamaño mínimo universal.

## 5. Normalizador del programa: qué ha cambiado y qué no [O/H/F]

### 5.1. El falso cierre

Sean dos gotas con idéntico `d`, misma geometría, mismo `A₀` discreto y, si se escoge, la misma descomposición `a²+b²+1=N²`. Para igual flujo turbulento impuesto, cambiar `σ` altera `d_H`, `We_0/We_{0,crit}`, el salto capilar y el costo de nueva superficie. Por tanto:

\[
\boxed{(d,\,A_0,\,N,\,\varepsilon,\,\rho_c)\ \text{no determina}\ d_H\quad \text{si omite }\sigma.}\tag{65.9}
\]

Éste es un **falsador matemático** de la suficiencia del comparador basado sólo en geometría y conteo para la **pregunta concreta de umbral de fragmentación**. No falsifica la ontología de que la unidad se autorreferencia ni la operación aritmética de O58.

### 5.2. La distinción nueva

Una firma mínima **para calcular exclusivamente la predicción del modelo de Hinze con `C_H` fijado** puede almacenar `\sigma/\rho_c`, `ε`, y `d` o bien la sola combinación adimensional `\Pi_H=d/d_H` si la pregunta es únicamente «¿a qué lado del umbral estimado está?».

**No** se afirma que esa firma cierre la dinámica de una gota: para pronosticar cuándo se rompe y en cuántas hijas habría que conservar además historia de deformación, esfuerzos, flujo, viscosidades, geometría interfacial y estados de ambas fases.

La diferencia que el modelo obliga a reconocer es:

> Una estructura puede estar representada en el mismo múltiplo y seguir habitando la misma geometría, pero cambiar de respuesta al variar una relación que la normalización anterior omitía.

Así, la novedad no es por definición cambiar `N`; puede ser **el reconocimiento de que el contrato de comparación anterior no era suficiente** para distinguir continuaciones físicas.

### 5.3. Dos normalizadores que no debemos fusionar

- `N` de O58: referencia cardinal/aritmética de dos cuadrados y una unidad pendiente; la reconstrucción entre escalas es un resultado bajo ese contrato.
- `d_H` y `\Pi_H`: longitudes y cocientes dimensionales físicos, seleccionados por propiedades de la interfaz y de la corriente turbulenta **bajo un modelo de rango inercial**.

No se ha deducido `N(d_H)` ni `A₀` a partir de un mecanismo capilar. Queda **abierto** si alguna correspondencia física no circular los puede conectar.

## 6. A qué sí responde O65 y qué seguirá abierto

**[T]** Mismo `u=U` y mismo radio `s` pueden ser soluciones bifásicas exactas para diferentes `σ`, con diferentes saltos de presión. Muestran que alterar la referencia física no obliga por sí solo a deshacer la unidad.

**[M/E]** Bajo flujo turbulento impuesto, Hinze distingue tres umbrales y cruza el valor de una gota testigo de `5mm` sin modificar `ρ,ε,μ,d`. El programa necesita representar al menos la información de capilaridad para responder a esa pregunta.

**[F]** Una interfaz basada sólo en `N` y geometría no es suficiente para predecir `d_H` cuando `σ` cambia.

**[A]** No se ha realizado DNS bifásico, ni simulación de ruptura/coalescencia, ni prueba de unicidad de normalizador físico, ni demostración de que `a²+b²+1=N²` gobierne gotas o Navier–Stokes 3D general. Es necesario definir un puente entre la activación de relaciones O61–O63 y el trabajo interfacial real.

**Siguiente pregunta O66:** una vez fijado un mismo historial de esfuerzos (no sólo ε), determinar si la diferencia capilar predice **una trayectoria interfacial** bajo una ley de evolución bien definida, contrastada con su identidad de energía y sin escoger parámetros después de ver los resultados. Idealmente dos fases resueltas; si se comienza con una interfaz reducida, llamarla explícitamente modelo reducido y mantener su falsador.

## 7. Reproducibilidad y procedencia

`python codigo/o65.py` desde el directorio del suplemento escribe `datos/o65_tensiones.csv`, `datos/o65_resumen.json` y dos figuras. El propio script comprueba las razones de escala, los umbrales bajo la convención declarada, el salto de Young–Laplace y la solución trasladada a nivel geométrico. **Los controles numéricos no sustituyen la demostración formal de (65.1)-(65.2).**

O64 se conserva como antecedente independiente y la Imagen Total v3.8.1 no se modifica. Los resultados de O53/O63 corresponden a otra clase de simulación (anillo monofásico en unidades propias) y no se trasladan numéricamente a las gotas de este ensayo.

### Contraste externo, no fuente ontológica

- *Morphology of clean and surfactant-laden droplets in homogeneous isotropic turbulence*, Journal of Fluid Mechanics: https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/morphology-of-clean-and-surfactantladen-droplets-in-homogeneous-isotropic-turbulence/4D73AA84DA6451E44774F5D67F8767F7
- *Droplet–turbulence interactions and quasi-equilibrium dynamics in turbulent emulsions*, Journal of Fluid Mechanics: https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/dropletturbulence-interactions-and-quasiequilibrium-dynamics-in-turbulent-emulsions/02D6429A447BB860DA3615E0D76A062A
- *The interaction of droplet dynamics and turbulence cascade*, Communications Physics: https://www.nature.com/articles/s42005-022-01122-8

La bibliografía acredita parámetros y advertencias de física conocida; no funda ni redefine el programa.
