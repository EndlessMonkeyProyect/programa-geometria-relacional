# Laboratorio A–G–01 — Armónicos, granularidad heredada y cierre observacional

**Anexo técnico | 21 de noviembre de 2026**  
**Continuidad documental:** MF-69 (factores armónicos primitivos), O40 (normalizador y herencia), O58/G–01 (resto algebraico), ROSI (contratos de consulta), MF-86/CR-6 (suficiencia bajo contrato), CME-002 (cambio de referencia), R–03 y R–RH–01 (representación funcional).  
**Firma:** Endless Monkey Project / Relational Geometry Program.

## 1. Resultado ejecutivo

Una familia armónica de frecuencias `ω_n=nω₀`, observada mediante la **escala inversa** `R_n=R₀/n`, tiene separación entre vecinos `Δ_n=R₀/[n(n+1)]`. Bajo una consulta con granularidad fija `g_K=R₀/K²`, todas las escalas `R_n` con `n>K²` pertenecen a **una misma celda de resolución anclada en cero**. El resultado es un teorema exacto del contrato observacional elegido. Para una granularidad que también varía, la competencia entre índices `n` y `K` está dada por la razón `K²/[n(n+1)]`.

Este laboratorio construye una **correspondencia de escala** entre las fórmulas de MF-69 y la forma algebraica del grano de O58. El paso desde el cierre observacional hasta una norma funcional se formula con un contrato de transferencia independiente.

## 2. Definiciones y procedencia

**Referencia armónica (MF-69):** sea `ω₀>0`, `v_*>0` y `R₀=v_*/ω₀`. Las repeticiones armónicas se parametrizan por enteros `n≥1`:

$$
\omega_n=n\omega_0,\qquad R_n=\frac{v_*}{\omega_n}=\frac{R_0}{n}.
\tag{A1}
$$

La frecuencia `ω_n` crece con `n`; **la escala inversa** `R_n` decrece. La etiqueta armónica expresa conmensurabilidad con `ω₀`; la clasificación de factores nuevos de MF-69 se lleva en otra firma (monoide heredado).

**Normalizador (O58):** las ternas enteras admisibles `(a,b,K)` satisfacen

$$
a^2+b^2+1=K^2,\qquad \frac{a^2+b^2}{K^2}+\frac1{K^2}=1.\tag{A2}
$$

Por ejemplo `(2,2,3)`, `(4,8,9)`, `(12,12,17)` y `(70,70,99)`.

**Contrato de comparación A–G–01:** a cada normalizador admisible `K≥3` se le asigna, **como hipótesis de laboratorio explícita**, una resolución dimensional `g_K=R₀/K²`. Esta definición usa la *forma* del resto de O58. Su interpretación física como resolución de un instrumento o del espacio requiere justificar la operación que vincula ambas magnitudes.

Se especifican dos consultas:

1. **Tolerancia de pares:** dos escalas consecutivas están por debajo del umbral `θg_K` si su distancia es menor o igual a ese umbral (`0<θ≤1`). Esta consulta no se define como relación de equivalencia.
2. **Celda de resolución:** `Q_K(R)=floor(R/g_K)` para `R≥0`. Dos escalas son indistinguibles para **esta consulta concreta** cuando `Q_K` devuelve el mismo entero. Esta igualdad sí define una relación de equivalencia.

## 3. Teorema A — Separación armónica exacta

Para todo `n≥1`:

$$
\boxed{\Delta_n:=R_n-R_{n+1}=\frac{R_0}{n(n+1)}.}\tag{A3}
$$

**Demostración.** Se resta `R₀/n−R₀/(n+1)`, con numerador `R₀`. Por tanto `Δ_n>0` y `Δ_n→0`. $\square$

## 4. Teorema B — Cociente de granularidad y criterio de tolerancia

Para enteros `n≥1` y `K≥3`:

$$
\boxed{\eta(n,K)=\frac{\Delta_n}{g_K}=\frac{K^2}{n(n+1)}.}\tag{A4}
$$

La condición exacta `Δ_n≤θg_K` equivale a

$$
\boxed{n(n+1)\ge \frac{K^2}{\theta}}
\quad\Longleftrightarrow\quad
\boxed{n\ge\left\lceil\frac{\sqrt{1+4K^2/\theta}-1}{2}\right\rceil}.\tag{A5}
$$

**Demostración.** Sustitución de (A3) y `g_K`, seguida de resolución de la desigualdad cuadrática en `n≥0`. $\square$

Para una sucesión de normalizadores `K_j→∞` y una regla de correspondencia **declarada** `n_j=n(K_j)` se distinguen tres regímenes:

- Si `n_j/K_j→∞`, entonces `η(n_j,K_j)→0`: los vecinos convergen a una resolución **relativamente** cada vez más fina.
- Si `n_j/K_j→c∈(0,∞)`, entonces `η(n_j,K_j)→1/c²`.
- Si `n_j/K_j→0`, entonces `η(n_j,K_j)→∞`.

Es una tricotomía matemática completa para esta razón. En particular, la identificación `n=K` da `η=K/(K+1)→1`: la separación queda debajo de `g_K`, pero el margen **relativo** no crece.

## 5. Teorema C — Cierre exacto de celda para una resolución fija

La consulta de celda se evalúa mediante

$$
\boxed{Q_K(R_n)=\left\lfloor\frac{K^2}{n}\right\rfloor.}\tag{A6}
$$

Por tanto, para cada `K≥3` y todos los enteros `n,m>K²`:

$$
\boxed{Q_K(R_n)=Q_K(R_m)=0.}\tag{A7}
$$

**Demostración.** De `n>K²` se sigue `0<K²/n<1`; su parte entera es cero. Lo mismo vale para `m`. $\square$

El umbral de entrada en esta celda es **exactamente** `n=K²+1`. El límite (A7) es el cierre de una **consulta** finita: las escalas permanecen matemáticamente distintas como números reales y constituyen una sola clase observacional `Q_K`.

**Ensayo de frontera.** Para `n=K²`, `Δ_n/g_K=1/(K²+1)`, muy pequeño, pero `Q_K(R_{K²})=1` y `Q_K(R_{K²+1})=0`. Así se separan formalmente la consulta de **tolerancia** y la de **celda**. Una diferencia subgranular puede cruzar la frontera de una celda.

## 6. Realizaciones admisibles y comparaciones

En cada fila `K` se utiliza una solución explícita de (A2) y se prueban tres parejas de armónicos: `n=K`, `n=K²`, `n=K²+1`.

| Normalizador `K` | `n` | `η(n,K)` exacto | `Q_K(R_n)` | `Q_K(R_{n+1})` | Misma celda |
|---:|---:|---:|---:|---:|:---:|
| 3 | 3 | `3/4` | 3 | 2 | No |
| 3 | 9 | `1/10` | 1 | 0 | No |
| 3 | 10 | `9/110` | 0 | 0 | Sí |
| 9 | 9 | `9/10` | 9 | 8 | No |
| 9 | 81 | `1/82` | 1 | 0 | No |
| 9 | 82 | `81/6806` | 0 | 0 | Sí |
| 17 | 17 | `17/18` | 17 | 16 | No |
| 17 | 289 | `1/290` | 1 | 0 | No |
| 17 | 290 | `289/84390` | 0 | 0 | Sí |
| 99 | 99 | `99/100` | 99 | 98 | No |
| 99 | 9801 | `1/9802` | 1 | 0 | No |
| 99 | 9802 | `9801/96089006` | 0 | 0 | Sí |

Los números de la tabla son fracciones racionales exactas (el verificador registra y comprueba todas las igualdades). La misma estructura se cumple para todo normalizador admisible `K`.

## 7. Correspondencia con herencia, recierre y evaluación ROSI

- **Herencia armónica:** `ω_n=nω₀` y la firma de MF-69 permiten reconocer repeticiones y nuevas factorizaciones según el vocabulario multiplicativo acreditado.
- **Granularidad:** la ecuación (A2) entrega una fracción positiva `1/K²`; el contrato `g_K=R₀/K²` traduce esa fracción en una escala de observación declarada.
- **Recierre bajo consulta:** (A7) demuestra que una cola infinita de armónicos comparte una respuesta `Q_K=0` para cada `K` fijo. La consulta conserva el núcleo de referencia `R₀` sin exigir desplazamiento del núcleo.
- **Cambio de referencia:** al actualizar `K` se recalculan las celdas; O40 aporta la regla exacta de conservación de fracciones entre normalizadores compatibles.
- **Laboratorios:** CME-002 representa el desplazamiento de la frontera de consulta; el laboratorio de esferas representa la incorporación de referencias. La fórmula (A7) es una realización numérica con contrato propio, cuya correspondencia geométrica se investiga mediante un mapeo explícito.

La validación ROSI contiene: objetos (`R_n`, `g_K`), pregunta (`Q_K`), discriminante (`n>K²`), testigo (A6), prueba (A7), control de frontera (`n=K²`) y reproducción exacta.

## 8. Proposición D — Transferencia funcional bajo certificado de norma

En `H=L²((0,∞),dx)` sean `χ=1_(0,1]`, `f_d(x)={1/(dx)}` y `W_m=span{f_d:1≤d≤m, μ(d)≠0}`. Sea `e_m=dist(χ,W_m)`.

**Proposición condicional.** Si una continuación aritmética construye, para índices `m(K)→∞`, aproximantes `a_K∈W_{m(K)}` y cotas certificadas `\varepsilon_K→0` tales que

$$
\boxed{\|\chi-a_K\|_2^2\le\varepsilon_K,}\tag{D1}
$$

entonces `e_m→0` y se cumple RH por la dirección suficiente del criterio clásico de Nyman–Beurling/Báez-Duarte.

**Demostración.** `0≤e_{m(K)}²≤||χ-a_K||²≤ε_K→0`. La distancia `e_m` es monótona por inclusión de espacios, y `m(K)→∞` permite extender el límite a toda la familia. El criterio clásico se aplica a la familia completa porque los espacios restringidos están incluidos en los completos. $\square$

**Contrato específico de transferencia:** documentar un operador que convierta `(K,n(K),Q_K)` en coeficientes admisibles `a_K` **y** una cota global (D1). En los anexos de tres ventanas, esta cota se descompone en el sector próximo a cero, el intermedio y la cola. La diferencia subgranular de (A4) y la coincidencia de celda (A7) ya poseen pruebas; la cota (D1) exige controlar la integral de error y la economía de esos coeficientes.

**Compatibilidad de índices:** las cotas inferiores clásicas `e_m²≳1/log m` exigen que cualquier supuesta cota `e_{m(K)}²=O(K^{-2})` vaya acompañada por `log m(K)≳K²`. Este control evita identificar libremente el índice armónico `n`, el normalizador `K` y el número de funciones `m`.

## 9. Resultado de incorporación

El laboratorio establece **dos resultados universales**: la razón exacta entre separación armónica y granularidad (A4) y la indistinguibilidad por celda de todos los modos inversos con `n>K²` (A7). Asimismo entrega una condición tipada para relacionarlos con el contrato funcional de Riemann (D1). Cada afirmación se puede verificar separadamente con aritmética exacta.

### Fuentes internas y trazabilidad

1. `MF69_factores_armonicos_primitivos_regla_engranaje_v1.md`, §12 (repetición armónica) y §§2–4 (monoide, herencia y novedad).
2. `O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md` (transporte racional bajo cambio de referencia).
3. `O58_FORMALIZACION.es.md` y `G01_Mecanismo_de_la_Gravedad_Programa_Relacional_v1.3_2026-11-01.docx`, normalizador con `a²+b²+1=K²`.
4. `ANEXO_TECNICO_ES.md` (20-XI, tres ventanas, cambio entre escalas, límite funcional).
5. `COMPENDIO_RIEMANN_CME_2026-11-21.md` (21-XI, focos de Möbius, Gram y recuperación por proyecciones).
6. `PUENTE_GRANULARIDAD_TRES_VENTANAS_2026-11-21.md` (21-XI, energía periódica y masa de discrepancia).

**Le Matt Ansatz Di Ego**  
**Endless Monkey Project / Relational Geometry Program**
