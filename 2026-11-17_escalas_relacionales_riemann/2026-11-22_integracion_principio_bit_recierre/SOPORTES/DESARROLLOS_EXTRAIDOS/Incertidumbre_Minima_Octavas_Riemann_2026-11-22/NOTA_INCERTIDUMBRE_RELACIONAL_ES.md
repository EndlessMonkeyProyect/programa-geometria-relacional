# Diferencia mínima, memoria y desfase entre octavas

**Nota de formalización y contraste cuantitativo** · 22 de noviembre de 2026  
**Ámbito:** realización de Nyman–Beurling–Báez-Duarte; proyección, cierre y escala diádica.  
**Estado:** dos identidades demostradas; datos finitos auditados desde cifras publicadas; interpretación relacional propuesta; condición global abierta.

## Resumen

La diferencia mínima tiene una realización matemática precisa: la distancia cuadrática **óptima** entre la unidad de referencia y el subespacio de reconstrucciones permitido en una escala finita. Su valor es una **cantidad residual**, no un error numérico. Al duplicar la escala, la descomposición ortogonal conserva exactamente la totalidad del presupuesto: una parte se resuelve y otra permanece. Para estudiar el desfase frente al perfil de referencia de orden inverso al número de octavas, se introduce la magnitud normalizada `A_j=(j+1) E_j` y se demuestra una nueva identidad elemental que determina sus incrementos a partir de la ganancia de cada octava. En los diez retornos documentados, el error absoluto siempre disminuye; sin embargo, `A_j` aumenta ligeramente en la última transición, precisamente donde falla la antigua cota rígida. La observación es compatible con una fluctuación relativa a la escala; su extensión a todas las octavas sigue abierta.

## 1. Realización matemática de la diferencia pendiente

En la formulación por proyecciones utilizada en las notas previas, sea `H` un espacio de Hilbert, `χ` la unidad de referencia con `||χ||²=1`, y `V_m⊂V_{2m}` los subespacios de reconstrucciones admitidas hasta las escalas `m` y `2m` (en la realización aritmética se usan funciones de parte fraccionaria y referencias enteras libres de cuadrados). Sea `P_m` la proyección ortogonal sobre `V_m`.

Defínanse:

\[
E(m)=\inf_{v\in V_m}\|\chi-v\|^2=\|\chi-P_m\chi\|^2,\qquad
\Delta(m)=\|(P_{2m}-P_m)\chi\|^2.
\]

**Proposición 1 (presupuesto conservado).** Para todo `m`:

\[
\boxed{E(m)=\Delta(m)+E(2m).}
\]

**Demostración.** Por inclusión de subespacios, `P_{2m}-P_m` es la proyección sobre `V_{2m}∩V_m^⊥`. La identidad

\[
\chi-P_m\chi=(P_{2m}-P_m)\chi+(\chi-P_{2m}\chi)
\]

tiene sumandos ortogonales. El teorema de Pitágoras da la ecuación. En consecuencia `E(2m)≤E(m)` y `0≤Δ(m)≤E(m)`. □

La palabra **mínima** se refiere aquí a la minimización dentro del conjunto de reconstrucciones permitidas: `E(m)` es el mejor resto posible a escala `m`. No identifica por sí misma una constante ontológica ni una cota inferior válida para cualquier modelo de reflexión.

## 2. Identidad exacta del desfase normalizado

Escríbase para `m=2^j`:

\[
E_j=E(2^j),\qquad \theta_j=\frac{E_j-E_{j+1}}{E_j}\quad(E_j>0),\qquad
A_j=(j+1)E_j.
\]

La referencia `E_j=K/(j+1)` corresponde exactamente a `θ_j=1/(j+2)`. Esto permite definir el **desfase de ganancia** en relación con ese perfil:

\[
\varepsilon_j=(j+2)\theta_j-1.
\]

**Proposición 2 (identidad de fase y memoria).**

\[
\boxed{A_{j+1}-A_j=-E_j\varepsilon_j.}
\]

**Demostración.** La Proposición 1 da `E_{j+1}=E_j(1−θ_j)`. Por tanto,

\[
A_{j+1}-A_j=(j+2)E_j(1-\theta_j)-(j+1)E_j
=E_j\{1-(j+2)\theta_j\}=-E_j\varepsilon_j.\quad\square
\]

Si `ε_j>0`, el resto normalizado `A_j` disminuye; si `ε_j=0`, conserva su valor; si `ε_j<0`, aumenta. En todos los casos la magnitud original `E_j` es no creciente. Esta separación evita confundir el retorno de la referencia con una creación de error.

## 3. Ensayo numérico en diez octavas

Se reconstruye `E_1≈0.289965` y se restan las ganancias `Δ_j` de la tabla **Mecanismos del programa frente a la regla de eliminación entre escalas** del 20 de noviembre. Los datos originales están redondeados y la presente nota no reejecuta la matriz de Gram original.

| Octava | `E_j` antes | `θ_j` | `ε_j=(j+2)θ_j−1` | `A_j` antes |
|---:|---:|---:|---:|---:|
| 2→4 | 0.289965 | 67.64 % | +1.029 | 0.579930 |
| 4→8 | 0.093835 | 72.42 % | +1.897 | 0.281505 |
| 8→16 | 0.025882 | 24.92 % | +0.246 | 0.103528 |
| 16→32 | 0.019432 | 21.73 % | +0.304 | 0.097160 |
| 32→64 | 0.015210 | 22.13 % | +0.549 | 0.091261 |
| 64→128 | 0.011844 | 15.78 % | +0.262 | 0.082909 |
| 128→256 | 0.009976 | 15.15 % | +0.364 | 0.079804 |
| 256→512 | 0.008464 | 10.46 % | +0.046 | 0.076174 |
| 512→1024 | 0.007578 | 11.98 % | +0.318 | 0.075783 |
| 1024→2048 | 0.006671 | 6.64 % | **−0.203** | **0.073377** |

En la última transición, la ganancia positiva es `Δ_10≈0.00044319` y el resto baja hasta `E_11≈0.00622744`. En cambio, `A_10≈0.0733769` aumenta a `A_11≈0.0747293` (**+1,84 %**). La identidad de la Proposición 2 predice este cambio sin parámetros adicionales.

Los diez valores impresos satisfacen `θ_j≥0.75/(j+2)` y los diez certificados de semilla publicados satisfacen `certificado_j/E_j≥0.50/(j+2)`. Estas comparaciones permanecen válidas si cada cifra fuente se modifica hasta media unidad de su último decimal publicado. La cota rígida `θ_j≥1/(j+2)` falla en `j=10`.

**Normalización logarítmica.** En las cuatro últimas escalas, `E(2^j) ln(2^j)` vale aproximadamente `0.04693`, `0.04728`, `0.04624` y `0.04748` (para `m=256, 512, 1024, 2048`). Son cifras próximas a `C₀=2+γ−ln(4π)≈0.0461914`. Esta cercanía es **un contraste numérico, no una cota puntual ni una prueba de un límite**. El trabajo clásico de Burnol da una obstrucción asintótica inferior en términos de ceros sobre la línea crítica; la identificación de `C₀` como constante asintótica óptima exige hipótesis adicionales, entre ellas RH y un control de `ζ′` en los ceros en el teorema de Bettin–Conrey–Farmer.

## 4. Certificado de la reducción de cada octava

La separación de lo heredado y lo nuevo aporta un instrumento cuantitativo. Sea `r_m=χ−P_mχ` y sea `g` cualquier vector admisible en `V_{2m}` con `(I−P_m)g ≠ 0`. Por Cauchy–Schwarz en el subespacio nuevo,

\[
\boxed{\Delta(m)\ge\frac{|\langle r_m,g\rangle|^2}{\|(I-P_m)g\|^2}.}
\]

Se verifica la desigualdad en todas las escalas por geometría de Hilbert. Para transformarla en un criterio de cierre se necesita una **cota inferior específica** de su lado derecho en función de `E(m)` y de la escala, obtenida de las propiedades aritméticas de `g`.

**Condición suficiente propuesta:** si existen `c>0` y `j₀` tales que

\[
\boxed{\theta_j\ge\frac{c}{j+2}\quad\text{para todo }j\ge j_0,}
\]

entonces `∑_j θ_j=∞`, el producto `E_J=E_1∏_{j<J}(1−θ_j)` tiende a cero y, **para los espacios precisos del criterio de Báez-Duarte**, se obtiene la hipótesis de Riemann. También basta demostrar una reducción acumulada uniforme por bloques sucesivos del índice `j`. Estas son condiciones suficientes y no resultados acreditados por los diez casos finitos.

## 5. Interpretación y dictamen

**Interpretación relacional:** la incertidumbre mínima por escala se identifica operativamente con `E(m)`, la diferencia que ninguna combinación admitida en esa escala puede reconstruir. Cada retorno conserva el presupuesto original y resuelve parte de la diferencia por una componente perpendicular. El desfase `ε_j` mide cómo se sitúa la ganancia de una octava respecto al perfil armónico de referencia `1/(j+2)`.

**Estado de las afirmaciones:**

- **Demostrado:** identidades de proyección, presupuesto de cierre y variación exacta del resto renormalizado; certificado geométrico de semilla.
- **Contrastado finitamente:** diez octavas de ganancias positivas; caída de la regla rígida en `j=10`; última subida del resto renormalizado; proximidad numérica de `E(m)ln m` a la referencia teórica condicional.
- **Abierto:** demostrar una cota inferior aritmética acumulada uniforme para `θ_j`, o una estimación equivalente, en todas las escalas. La interpretación de `E(m)` como condición ontológica de existencia sigue siendo un puente conceptual, no un teorema aritmético.

**Hallazgo central:** el desfase deja de ser una anomalía: aparece exactamente como cambio de la diferencia pendiente bajo renormalización. La nueva identidad cuantifica el fenómeno, pero una desigualdad aritmética global es todavía necesaria para pasar de la memoria al cierre.

## Procedencia y reproducción

1. *Mecanismos del programa frente a la regla de eliminación entre escalas*, documento interno, 20-XI-2026; tablas de `Δ_j`, certificados de semilla y control hasta 2048.
2. *DICTAMEN_O18_CANALES_POR_OCTAVAS.es.md*, revisión O18 (19-X-2026): producto acumulado y margen logarítmico en un modelo de Navier–Stokes modificado.
3. L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis* (2002): https://arxiv.org/abs/math/0202141
4. J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function* (2002): https://arxiv.org/abs/math/0103058
5. S. Bettin, J. B. Conrey y D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion* (2012/2013): https://arxiv.org/abs/1211.5191

Para reproducir las cuentas de la tabla y el contraste con la precisión publicada:

```bash
python3 certificar_incertidumbre.py
```

El programa genera `tabla_octavas.csv` y `resultado.json` y comprueba las dos identidades y las desigualdades finitas, con controles del redondeo. No constituye una recomputación de la matriz de Gram de 2048 variables.

---

Endless Monkey Project / Relational Geometry Program
