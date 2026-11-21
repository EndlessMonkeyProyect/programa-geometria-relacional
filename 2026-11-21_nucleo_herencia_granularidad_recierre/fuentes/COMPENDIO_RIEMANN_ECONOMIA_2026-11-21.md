# Compendio de actualización — herencia, economía de información y resto de Riemann

**Fecha de corte:** 21 de noviembre de 2026  
**Propósito:** consolidar los materiales del 20–21 de noviembre con el mínimo de afirmaciones independientes, sin perder hipótesis, pruebas ni controles.  
**Estado:** mecanismos finitos y correspondencias exactas **DEMOSTRADOS**; agotamiento funcional global, RH y GRH **ABIERTOS**.  
**Firma:** Endless Monkey Project / Relational Geometry Program

## 1. Dictamen ejecutivo

La formulación común es una **economía de consultas bajo cambios de referencia**. Una representación puede conservar exactamente ciertas respuestas, incorporar distinciones nuevas y, aun así, no cerrar el error global de una aproximación. Hay que distinguir:

- **Conservación:** una pregunta sigue siendo recuperable tras un cambio de referencia.
- **Costo:** la recuperación puede amplificar error o requerir una representación más grande.
- **Cierre:** una familia de operaciones permitidas aproxima al objetivo en la **norma declarada**, con control uniforme sobre las escalas.

En la rama R–RH las identidades aritméticas y los puentes algebraicos están establecidos. La obligación no resuelta es probar una **ganancia acumulada de aproximación** que agote todo el residuo, sin presuponer RH ni usar una conclusión topológica en un espacio distinto.

## 2. Núcleo matemático mínimo

Para un conjunto *finito* de primos `S`, con `M_S=∏_{p∈S}p`, `δ_S=∏_{p∈S}(1−1/p)`, `A_S(x)=#{1≤n≤x:gcd(n,M_S)=1}` y `E_S(x)=A_S(x)−δ_Sx`, se tienen las tres correspondencias:

**A. Mellin y herencia de ceros** — identidad clásica, en `0<Re(s)<1`:

\[
F_S(s):=\int_0^\infty E_S(x)x^{-s-1}\,dx
=\frac{\zeta(s)}s\prod_{p\in S}(1-p^{-s}).
\]

La integral converge absolutamente en esa franja porque `E_S(x)=−δ_Sx` cuando `0<x<1` y `E_S` está acotada para `x≥1`. Como los factores nuevos no se anulan en la franja abierta, preservan **posiciones y multiplicidades** de los ceros de `ζ`; no determinan su localización. La identificación `L_f^S(s,1)=sF_S(s)` solo corresponde a la especialización racional, carácter trivial y factores locales finitos **sin** los gamma arquimedianos de una función L completada.

**B. Diferencias entre escalas** — identidad algebraica exacta:

\[
T_pf(x)=f(x)-f(x/p),\quad P_pf(x)=f(x)-f(px),\quad Jf(x)=f(1/x),\qquad JT_pJ=P_p.
\]

`J` es unitario en `L²((0,∞),dx/x)`, donde `T_p` tiene núcleo cero e imagen **densa, no cerrada**. Esto no transporta automáticamente los cierres funcionales invocados por Masullo: los espacios, las normas y los dominios no coinciden. En el Hilbert relevante para Báez-Duarte, `L²(dx)`, la inversión unitaria requiere un peso adicional.

**C. Criba y funciones fraccionarias** — identidad exacta por inclusión-exclusión:

\[
G_S(t):=-E_S(1/t)=\sum_{d\mid M_S}\mu(d)\left\{\frac1{dt}\right\}.
\]

La inversión por subconjuntos de primos recupera las funciones fraccionarias de índice libre de cuadrados; el espacio generado es el mismo **algebraicamente**. La equivalencia entre el agotamiento de la distancia funcional y RH procede del criterio clásico de Nyman–Beurling/Báez-Duarte. El puente algebraico **no prueba** que dicha distancia se anule.

## 3. Única condición de cierre que debe conservar la actualización

Definir en `H=L²((0,∞),dx)`:

\[
\chi=\mathbf1_{(0,1]},\qquad f_n(x)=\{1/(nx)\},\qquad
W_m=\operatorname{span}\{f_n:n\le m,\ \mu(n)\ne0\},\qquad
e_m=\operatorname{dist}_H(\chi,W_m).
\]

Para `m=2^j` y siempre que `e_{2^j}>0`, sea la fracción recuperada:

\[
\theta_j=\frac{e_{2^j}^2-e_{2^{j+1}}^2}{e_{2^j}^2},\quad
 e_{2^J}^2=e_1^2\prod_{j<J}(1-\theta_j).
\]

El criterio clásico y la identidad de producto dan:

\[
\boxed{\mathrm{RH}\iff e_m\to0\iff\sum_{j\ge0}\theta_j=\infty.}
\]

Esta es una **reformulación exacta**, no un avance demostrativo automático. La antigua propuesta universal `θ_j≥1/(j+2)` **queda descartada como ley**: el registro numérico informa `θ_10≈0.0664` en `1024→2048`, menor que `1/12≈0.0833`. Los datos numéricos requieren certificación de errores de Gram si van a publicarse como desigualdades rigurosas; ya bastan para retirar el carácter de «ley probada». Una condición más débil, aún **por demostrar**, sería `θ_j≥c/(j+2)` para todo `j` suficientemente grande, con `c>0`; también serviría una suma divergente sin cota punto a punto.

La ganancia de una nueva ventana es exactamente el cuadrado de la proyección sobre el complemento ortogonal; una **semilla** `g∈W_{2m}` da la cota computable:

\[
 e_m^2-e_{2m}^2\ge
 \frac{|\langle\chi-P_m\chi,g\rangle|^2}
 {\|(I-P_m)g\|^2},\qquad (I-P_m)g\ne0.
\]

La obligación verdadera es obtener una cota **aritmética, uniforme, no circular** para este cociente, o para su versión de Schur en la matriz de Gram.

## 4. Economía de información, escrita como contrato matemático

Cada aplicación debe declarar `(X,Q,Φ,A,ν,T)`: estados admisibles, preguntas, representación, decodificadores permitidos, norma/costo y regla de herencia. Una firma suficiente para responder `q` no garantiza reconstrucción por **combinaciones lineales**: para `X={0,1,2}`, `Φ(x)=x`, `q(x)=x²`, la pregunta es recuperable, pero la mejor aproximación por `span{1,Φ}` deja error cuadrático `2/9`.

En el lado espectral, `P_S(s)=∏(1−p^{-s})` conserva ceros finitos de referencia, pero dividir por `P_S` puede multiplicar el error por `1/|P_S|`, sin cota uniforme al incorporar todos los primos. **Preservación exacta y recuperación estable son contratos diferentes.** Tampoco debe equipararse el resto geométrico `1/N²` de G–01/O58 al error `e_m²` de R–RH: no comparten observable, espacio ni escala.

**Certificado de tres ventanas**, válido para cualquier aproximante finito `a_m=Σ c_{m,n}f_n`, `B_m=χ−a_m`, `L_m=Σ|c_{m,n}|`, `C_m=Σ c_{m,n}/n`, y `0<δ≤1≤R`:

\[
\boxed{\|B_m\|_2^2\le
\delta(1+L_m)^2+\int_{\delta}^{R}|B_m(x)|^2dx+
\frac{|C_m|^2}{R}.}
\]

La prueba separa las ventanas `(0,δ)`, `[δ,R]` y `(R,∞)`, usando `|f_n|≤1` y la cola exacta `f_n(x)=1/(nx)` cuando `x≥1`. El certificado es **elemental y correcto**, pero demuestra RH solo si se construyen aproximantes y se acota **cada término** hasta cero sin asumirla. El enunciado condicional del anexo que compara un error con `A_k/N_k²+B_k→0` debe conservarse exclusivamente como **obligación de transferencia**, no como teorema nuevo de cierre.

## 5. Resultados experimentales útiles y sus límites

| Ensayo | Dato declarado | Interpretación legítima |
|---|---:|---|
| Ley por octavas, `1024→2048` | `e²_1024≈0.006672`, `e²_2048≈0.006229`, `θ_10≈0.0664` | Refuta numéricamente la cota concreta `1/12` en ese paso; no decide la divergencia de `Σθ_j` |
| `m=2048`, regla por radio `1−log n/log N` | residuo al cuadrado ≈`0.067054`; óptimo ≈`0.006229` | Peso interesante, **no** óptimo en ese tamaño |
| Bloque de primos hasta 17, 128 referencias | criba ≈`0.8385`; óptimo del bloque ≈`0.013135`; óptimo por tamaño ≈`0.008881` | La herencia de criba sin reajuste **no** equivale a mejor proyección |
| Regla de pesos sobre tamaño `N=3000` | residuo de radio ≈`0.0610` | Dato finito; no prueba tasa asintótica |

El estudio de Bettin–Conrey–Farmer sobre pesos logarítmicos y constante `2+γ−log(4π)` es **condicional a RH y a una hipótesis adicional sobre `ζ′` en los ceros**. No debe utilizarse como cota incondicional.

**Corrección al registro `salida_prueba_reglas_de_peso.txt`, sección D:** la integral `S=∫_1^N(ψ(u)−β_Nu)^2/u²du` describe la ventana `x∈[1/N,1]` tras sustituir `u=1/x`. El término `β_N²/log²N` corresponde a `x∈[1,∞)`, **no** a `(0,1)`. La suma impresa **omite** `x∈(0,1/N)`: no es el error `L²` total. Control numérico con el mismo programa: en `N=30`, suma impresa ≈`0.311531` frente a total ≈`0.324490` (omisión ≈`0.012959`); en `N=100`, ≈`0.175087` frente a ≈`0.178475` (omisión ≈`0.003388`). Mantener los números como **error parcial**, corrigiendo las etiquetas, no como evidencia de cierre global.

**Controles adversariales preservados:** (i) una familia abstracta indexada por primos puede reducir estrictamente su error a cada paso y conservar residuo límite `1/2`; (ii) la criba directa satisface recuperación puntual, mientras su error global puede divergir, `\|\chi+G_{S_y}\|_2²≥q_yδ_y²→∞`. Ambas pruebas invalidan inferencias automáticas de «más referencias» a «cierre».

## 6. Depuración documental y reproducibilidad

| Material recibido | Decisión editorial |
|---|---|
| `ANEXO_TECNICO_ES(1).md` y `ANEXO_TECNICO_ES.md` dentro del ZIP del 20-XI | **Duplicado byte a byte** (mismo SHA-256); conservar una sola copia histórica |
| `Mecanismos del programa frente a la regla de eliminación entre escalas.md` y PDF homónimo | Mismo informe en fuente y presentación; conservar **MD editable** como antecedente, PDF opcional |
| `salida_prueba_reglas_de_peso.txt`, `registro_mecanismos..txt`, `registro_bloques_primos..txt` | Registros numéricos de **apoyo**, no tres publicaciones independientes |
| `mecanismos.py`, `bloques_primos.py` | Referencian `prueba_ley_L.py`, **no adjuntado** en este conjunto; no declarar ejecución íntegra reproducible desde los archivos sueltos |
| `prueba_reglas_de_peso.py` | Script independiente con `numpy`; sus valores son exploratorios y requieren control del error de cuadratura/Gram donde corresponda |
| ZIP `ACTUALIZACION_PUENTE_RESOLUCION_RIEMANN_2026-11-20` | Su verificador autónomo produjo **7 PASS**, y sus cinco entradas del manifiesto SHA-256 verificaron `OK`; ello **no** demuestra RH |
| Auditoría original pegada y auditoría corregida del 21-XI | Conservar como historial de revisión; la auditoría original contiene observaciones ya corregidas sobre Mellin, partes fraccionarias y topologías |

**Publicación mínima propuesta:** un solo `COMPENDIO_RIEMANN_ECONOMIA_2026-11-21.md` y un verificador autónomo. No replicar anexos, tablas extensas, PDF ni registros en `main`. Archivar los originales sin sobrescribir su historia; introducir cualquier cambio mediante PR revisable. Verificar por separado la distinción entre **R–03 v0.3 público** y **R–03 v0.4 de trabajo** antes de incorporar el puente como contenido ya publicado.

## 7. Estado para la próxima actualización

**Demostrado / clásico:** identidades A–C, conservación finita, contrato de suficiencia, proyección ortogonal, estimación de tres ventanas, controles adversariales y criterio de equivalencia de cierre clásico.

**Falsado o restringido:** ley universal `θ_j≥1/(j+2)` según los datos hasta `2048`; identidad entre suficiencia general y aproximación lineal; transferencia directa de `1/N²` a `e_m²`; cierre normado inferido de convergencia puntual.

**Abierto y prioritario:** encontrar una familia concreta de semillas/coeficientes que satisfaga una **cota inferior global no circular** de ganancias acumuladas, o una estimación uniforme de las tres ventanas. La búsqueda puede dar un nuevo teorema, una obstrucción o un contraejemplo al criterio propuesto. **RH/GRH no se derivan de los resultados actuales.**

**Masullo:** la conjugación de diferencias ofrece un puente operatorio limitado. El anuncio del 20-XI reconoce reportes de problemas en el borrador; la objeción atribuida a Nielsen figura en las auditorías recibidas, pero su prueba completa **no fue reproducida aquí**. Ninguna correspondencia debe presentarse como validación o reparación de GRH.

## Referencias primarias y de control

- [R–01/R–02: criba y Mellin](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md)
- [R–03: herencia y localización](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md)
- [Báez-Duarte: criterio de aproximación](https://arxiv.org/abs/math/0202141)
- [Burnol: cota inferior](https://arxiv.org/abs/math/0103058)
- [Bettin–Conrey–Farmer: resultado condicional](https://arxiv.org/abs/1211.5191)
- [Vakil: anuncio de Masullo y advertencia posterior](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)

**Criterio editorial:** conservar afirmaciones comprobables, indicar el dominio de cada operación y no convertir la forma algebraica de la clausura en una estimación uniforme inexistente.
