# Medición de configuraciones mediante Gram — revisión 1.1

**19 de noviembre de 2026 · Estado: demostraciones clásicas integradas y control finito reproducible.**

**Contrato epistemológico.** El objeto primario es la configuración bajo referencia y granularidad definida; $E_S$ es discrepancia de conteo, y $G_{S,T}$ es un producto interno ponderado. «Dispersión cuadrática» designa una media matemática, no energía física. El peso $x^{-2}$ responde al cambio de variable, no a un radio físico.

## Dictamen

La revisión incorpora tres precisiones: el cotejo del texto R–RH–01 recibido; una proyección obtenida íntegramente desde integrales truncadas; y una separación entre familias de aproximación. Las identidades del puente permanecen correctas. La hipótesis de Riemann sigue abierta.

## 1. Procedencia y enlace pendiente

El antecedente es **R–RH–01 — Primos, reflexión y cierre: una ruta relacional hacia la hipótesis de Riemann**, con fecha declarada **1 de noviembre de 2026**. Se recibió el archivo `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md` el 19-XI-2026: 17.087 bytes, SHA-256 `cba927f6532471cd8aee14f0dbc96ae2b1bfe3137d4910b2813ef72fe42feedf`. Su contenido coincide con la transcripción previa salvo el salto de línea final. Describe el criterio de Nyman–Beurling/Báez-Duarte, una matriz de Gram y la distancia `d_2` con expresiones cerradas.

**No se ha verificado una URL pública permanente de ese manuscrito en GitHub.** El cotejo identifica el contenido del archivo recibido; no aporta metadatos independientes que autentiquen su fecha histórica. El manuscrito se conserva fuera de esta entrega. Para que un tercero pueda repetir el cotejo desde GitHub, habrá que publicarlo o enlazarlo por una ruta estable comprobada. No debe inventarse un enlace.

Bibliografía matemática que fundamenta el criterio de cierre: L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Rend. Lincei Mat. Appl. 14 (2003), 5–11; [arXiv:math/0202141](https://arxiv.org/abs/math/0202141). El cálculo finito de `d_2` no demuestra RH.

## 2. Identidades y realización

Para un conjunto finito de primos `S`, sean `M_S=∏_{p∈S}p`, `δ_S=∏_{p∈S}(1−1/p)` y

$$
 E_S(y)=\sum_{1\leq n\leq y}\mathbf1_{\gcd(n,M_S)=1}-y\delta_S,\qquad
 f_d(t)=\left\{\frac1{dt}\right\}.
$$

De inclusión-exclusión se deduce la identidad exacta:

$$
 h_S(t):=-E_S(1/t)=\sum_{d\mid M_S}\mu(d)f_d(t).
$$

Por el cambio `y=1/t`:

$$
 G_{S,T}=\langle h_S,h_T\rangle
 =\int_0^\infty\frac{E_S(y)E_T(y)}{y^2}\,dy,
 \qquad
 b_S=\langle\chi,h_S\rangle=-\int_1^\infty\frac{E_S(y)}{y^2}\,dy.
$$

Con `χ=1_(0,1]`, la distancia cuadrática a un espacio finito generado por `h_S` es `d²=1−b*G⁺b`. Esta es la fórmula estándar de proyección ortogonal, aplicada a las funciones del programa. **No se reivindica novedad del criterio ni de esta fórmula.**

## 3. Proyección calculada independientemente

Las referencias de control son `S=∅` y `S={2}`. Por tanto, `h_∅=f_1` y `h_{2}=f_1−f_2`. En cada intervalo `[n,n+1)` se integra exactamente una expresión de la forma

$$
 E_j(y)=A_j(n)-\delta_j y,
$$

con `A_∅(n)=n` y `A_{2}(n)=⌈n/2⌉`. El algoritmo construye **ambos** objetos truncados:

$$
 G_{ij}^{(N)}=\int_0^N\frac{E_i(y)E_j(y)}{y^2}\,dy,
 \qquad b_i^{(N)}=-\int_1^N\frac{E_i(y)}{y^2}\,dy.
$$

Obtiene luego `c_N=(G^(N))^{-1}b^(N)` y el mínimo truncado

$$
 d_N^2=1-\frac1N-(b^{(N)})^*c_N.
$$

La diferencia `−1/N` corresponde a la norma exacta de `χ(1/y)` sobre `[0,N]` con medida `dy/y²`; omitirla introduciría un sesgo. No se emplean las constantes `γ`, `log(2π)` ni `log π` durante el cálculo de la proyección truncada; solamente se introducen después, para comprobar contra el valor cerrado.

**Resultados con `N=3000`, `mpmath dps=45`:**

- Distancia obtenida de las integrales truncadas: **0.538346614598845...**
- Valor exacto de control, calculado aparte: **0.538483587254247...**
- Desviación truncada: **0.000136972655402...**

Para `y≥N`, se tiene `|E_∅(y)|≤1` y `|E_{2}(y)|≤1/2`. Como `χ(1/y)=1`, al emplear el candidato `c_N` en todo el dominio resulta la **cota analítica de cola**:

$$
 d_N^2\le d_2^2\le d_N^2+\frac{(1+|c_{N,0}|+\frac12|c_{N,1}|)^2}{N}.
$$

El intervalo resultante es **[0.538346614598845..., 0.541166573542464...]**. La desigualdad de cola es rigurosa en aritmética exacta; los extremos impresos con `mpmath` no son certificados de redondeo dirigido. Para publicación con cotas numéricas certificadas debe añadirse aritmética de intervalos.

## 4. Tres familias de funciones distintas

| Familia | Generadores | Qué mide la distancia | Correspondencia |
|---|---|---|---|
| Dos referencias, este control | `h_∅`, `h_{2}` | Mejor proyección en un espacio de dimensión 2 | Exactamente el espacio generado por `f_1`, `f_2`; comparable con `d_2` de R–RH–01 |
| Subconjuntos de un conjunto finito `P` de primos | `{h_S:S⊆P}` | Proyección sobre `span{f_d:d\mid\prod_{p∈P}p}` | Usa **todos los divisores libres de cuadrados del producto**, con dimensión `2^|P|` |
| Báez-Duarte, truncamiento `m` | `{f_n:1≤n≤m}` | Mejor proyección sobre **todos** los índices enteros hasta `m` | Incluye índices con potencias repetidas, y `m` no equivale al número de primos en `P` |

La igualdad de espacios para la segunda fila se obtiene mediante inversión de Möbius en el retículo de subconjuntos. **Ningún valor numérico de una familia se presenta como si fuera el de otra.** Las aproximaciones con coeficientes especiales de Möbius tampoco deben confundirse con el mejor ajuste por mínimos cuadrados de cada familia.

## 5. Procedencia y alcance del aporte

- **Clásico:** criba por inclusión-exclusión, Nyman–Beurling/Báez-Duarte, proyección de Gram.
- **Derivado exactamente aquí:** reescritura de `h_S` por discrepancia modular y relación integral ponderada.
- **Verificado computacionalmente:** norma y proyección para dos referencias; cola acotada y coincidencia con el control cerrado.
- **Aporte del programa:** contrato explícito que enlaza la dispersión cuadrática de R–01/R–02 con el cierre funcional de R–RH–01, a través de firmas heredadas y medida ponderada. Su carácter **matemáticamente inédito no está demostrado**.
- **Abierto:** probar convergencia global suficiente para RH o una reducción de costo genuinamente nueva; las verificaciones finitas no la prueban.

## 6. Reproducción y circulación

Ejecución en un entorno con `mpmath>=1.3`: `python verificacion_puente_gram_v1_1.py --N 3000 --dps 45`.

El algoritmo es determinista: no necesita semillas. `EJECUCION_LOCAL_2026-11-19.txt` conserva una ejecución previa del paquete; los resultados de esta rama se documentan en el PR. Las sumas `SHA256SUMS.txt` verifican integridad de archivos, no validez de teoremas. El cotejo de R–RH–01 se registra arriba; su enlace público sigue pendiente.

**Endless Monkey Project**<br>
Relational Geometry Program<br>
Le Matt Ansatz Di Ego
