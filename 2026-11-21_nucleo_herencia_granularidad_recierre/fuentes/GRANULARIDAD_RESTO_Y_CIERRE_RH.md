# Granularidad, referencia y agotamiento del resto
## Resultado de búsqueda y prueba de estrés de la vía funcional a Riemann

**Fecha de revisión:** 20 de noviembre de 2026  
**Estado:** dos resultados matemáticos exactos (uno de imposibilidad de cierre finito y otro sobre divergencia del aproximante directo), correspondencia conceptual identificada; **RH no demostrada**.

## 1. Hallazgo documental

La hipótesis de que la *última solución pendiente* equivale a una unidad mínima cuantificable tiene antecedentes precisos:

- **Anexo «Exceso de cierre y novedad relacional» (8 de octubre):** la unidad puede particionarse en `2^n` partes de valor `2^-n`, todas sumando 1. Hay un grano positivo *en cada profundidad* y no existe un grano positivo mínimo *uniforme en todas las profundidades*.
- **O40 (20 de octubre):** una fracción `h/N` se conserva exactamente como `qh/(qN)` al refinar la referencia; conservar su valor no equivale a eliminarla.
- **O58 (21 de octubre):** la fracción restante `1/N²` es exacta para un contrato aritmético particular; no es automáticamente la distancia funcional de Riemann.
- **R–RH–01 (1 de noviembre):** define `χ(t)=1_(0,1](t)` y `f_n(t)={1/(nt)}`; en `L²(0,∞)`, la condición `dist(χ,span(f_1,…,f_m))→0` equivale, por el criterio **clásico** de Báez-Duarte, a RH.
- **R–03 v0.4 (18 de noviembre, copia de biblioteca):** conecta por inversión de Möbius la discrepancia de criba con las `f_n` de índice libre de cuadrados.
- **«Prueba exploratoria: barrera del cierre directo» (20 de noviembre):** demuestra que una recuperación punto por punto mediante criba directa puede presentar, paradójicamente, error cuadrático creciente.

La arquitectura relacional *sí* está construida. El sentido exacto de la «última solución» exige, sin embargo, separar resolución finita, refinamiento de una rejilla y convergencia en norma.

## 2. Teorema A — No hay último cierre finito con estas funciones

Para todo conjunto finito `F ⊂ N`, sea `V_F=span{f_n:n∈F} ⊂ L²(0,∞)` con

\[
f_n(t)=\left\{\frac1{nt}\right\},\qquad
\chi(t)=\mathbf1_{(0,1]}(t).
\]

**Proposición A.** Para todo conjunto finito `F`, `χ ∉ V_F`. En particular, como `V_F` es un subespacio finito-dimensional cerrado,

\[
\boxed{\operatorname{dist}_{L²}(\chi,V_F)>0.}
\]

**Demostración.** Supóngase `χ(t)=Σ_(n∈F) c_n f_n(t)` casi en todas partes. Las funciones sólo tienen un número finito de discontinuidades sobre cada intervalo compacto separado de `t=0`; por igualdad casi en todas partes, las expresiones coinciden en cada tramo continuo y, en particular, sus saltos laterales deben coincidir.

En `t=1` sólo `f_1`, entre los `f_n` de índice entero positivo, tiene un salto, y el salto «límite izquierdo menos límite derecho» de `f_1` es `-1`. El salto de `χ` es `+1`. Por tanto, `1∈F` y necesariamente `c_1=-1`.

Sea `q` un primo mayor que todos los índices de `F`. En `t=1/q` una función `f_n` salta si y sólo si `n|q`, pues `1/(nt)=q/n` debe ser entero. Entre los índices de `F`, únicamente `n=1` divide a `q`. Por tanto, el salto de la combinación en `t=1/q` es `-c_1=+1`. Pero `χ` es constante e igual a 1 en un entorno de `1/q` y su salto allí es 0. Contradicción. `□`

**Alcance:** se descarta la lectura de una **última fracción que cierre exactamente el problema en un número finito de referencias `f_n`**. El teorema no descarta un cierre en el límite de referencias, ni métodos con familias de funciones distintas. Es una consecuencia elemental de la estructura de saltos, no una prueba de RH.

## 3. Teorema B — El resto puntual puede ocultar una masa creciente

Sea `S_y={p primo:p≤y}`, `M_y=∏_(p≤y)p`, `δ_y=∏_(p≤y)(1-1/p)`, y `q_y` el primer primo mayor que `y`. La discrepancia es

\[
A_y(x)=\#\{1\le n\le x: \gcd(n,M_y)=1\},\quad
E_y(x)=A_y(x)-δ_y x,
\]

con su inversión

\[
G_y(t)=-E_y(1/t)=\sum_{d\mid M_y}\mu(d)f_d(t).
\]

**Proposición B.** Para todo `t>1/q_y` se tiene exactamente

\[
\boxed{\chi(t)+G_y(t)=\frac{δ_y}{t}.}
\]

**Prueba.** Para `0<x<q_y`, ningún entero entre `2` y `x` es coprimo con `M_y`; sólo subsiste `1` cuando `x≥1`. Así `A_y(1/t)=χ(t)` cuando `t>1/q_y`. Sustituyendo en `G_y=δ_y/t-A_y(1/t)` resulta la igualdad. `□`

Integrar solamente sobre esa ventana produce

\[
\boxed{\|\chi+G_y\|_{L²}^2\ge q_y δ_y^2.}
\]

Por el producto de Mertens, `δ_y ~ e^(-γ)/log y`, mientras `q_y>y`. Por consiguiente,

\[
\boxed{\|\chi+G_y\|_{L²}^2\longrightarrow\infty.}
\]

No obstante, `G_y(t)→-χ(t)` para cada `t>0` fijo: una concentración de la discrepancia viaja hacia `t=0`. **Cierre puntual y cierre de norma son distintos.** Este teorema figura también en la nota de prueba de estrés recuperada; su derivación usa propiedades clásicas de criba y Mertens.

## 4. Lo que significa matemáticamente «granularidad»

En una partición finita puede haber un grano mínimo `g_N=1/N` o `g_N=1/N²`. Es correcto que `g_N>0` a cada nivel y que `g_N→0` al aumentar la profundidad. Esto no demuestra `d_m→0`, donde `d_m` es la distancia óptima funcional utilizada en R–RH–01.

Para espacios anidados `V_m`, la identidad de proyección escribe el **balance exacto**

\[
\boxed{1=\sum_{m=0}^{M-1}(d_m^2-d_{m+1}^2)+d_M^2,}
\]

con `V_0={0}`. Para demostrar RH hace falta una desigualdad universal que obligue a `d_M²→0`; no basta un refinamiento de grano ni una ganancia positiva en cada etapa.

La ley diádica condicional explorada en un informe anterior

\[
d_{2^j}^2-d_{2^{j+1}}^2\ge\frac{d_{2^j}^2}{j+2}
\]

**sí sería suficiente si se demostrara para todo `j`**: da `d_(2^j)^2≤d_1²/(j+1)→0`. Sus comprobaciones numéricas hasta escalas pequeñas no sustituyen la prueba global; podría ser falsa para algún bloque.

## 5. Pregunta nueva, con contrato verificable

¿Existe una familia de coeficientes `a_(m,n)`, explícita y construible a partir de referencias heredadas y novedades, tal que

\[
\boxed{\left\|\chi-\sum_{n\le m}a_{m,n}f_n\right\|_{L²(0,∞)}^2\le\varepsilon_m,\qquad\varepsilon_m\xrightarrow[m\to\infty]{}0}
\]

**sin suponer previamente RH ni un resultado equivalente**?

El candidato debe controlar las ventanas que se desplazan hacia `t=0`; los coeficientes directos de Möbius y una mera escala de grano no bastan. La desigualdad global sería una contribución decisiva; hasta aquí no fue obtenida.

## 6. Registro de estados

| Enunciado | Estado |
|---|---|
| Granos positivos por nivel y ausencia de mínimo positivo global en rejillas `1/N²` | Identidad elemental |
| Herencia exacta de una fracción `h/N` entre normalizadores | Demostrado bajo el contrato de O40 |
| No existe `χ` en un subespacio generado por un número finito de `f_n` | **Demostrado — Proposición A** |
| Producto de criba directo: cierre puntual pero norma divergente | **Demostrado — Proposición B** |
| Equivalencia `RH ↔ d_m→0` | Criterio clásico, citado |
| Existencia de coeficientes con cota superior global del resto | **Abierto** |
| RH | **No demostrada** |

## 7. Fuentes

- Documentos del corpus: `ANEXO_EXCESO_DE_CIERRE_Y_NOVEDAD_RELACIONAL.md`; `O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md`; `O58_FORMALIZACION.es.md`; `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md`; `R03_v04_BILINGUE.docx`; `PRUEBA_EXPLORATORIA_BARRERA_CIERRE.md`; `INTENTO_DE_PRUEBA_RESTO_RIEMANN.md`.
- [Carpeta pública de Riemann, repositorio](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-17_escalas_relacionales_riemann).
- [L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion*](https://arxiv.org/abs/math/0202141).
- [T. Tao, *Mertens' theorems*](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/).

### Reproducción

`python3 verificar_granularidad.py` verifica con fracciones racionales la identidad de inclusión-exclusión, la ventana exacta y la contradicción de saltos en muestras finitas. Las afirmaciones universales A y B se demuestran en el texto, no mediante el script.

---

Endless Monkey Project / Relational Geometry Program
