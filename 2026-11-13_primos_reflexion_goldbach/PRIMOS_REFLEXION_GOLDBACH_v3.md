# Primos, reflexión y Goldbach
## Identidades, límites demostrados y frontera espectral

**13 de noviembre de 2026 · revisión v3.0**  
**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program

**Contrato:** nota de formalización, fuentes y verificación independiente de *identidades finitas*. Presenta un vínculo condicionado con el trabajo de Li–Liu; la transferencia a sus operadores espectrales y el control requerido para Goldbach forman la agenda abierta. Las etiquetas de «exacto» indican el dominio de las pruebas bajo las hipótesis declaradas.

## 0. Tabla de resultados y estados

| Resultado | Estado | Hipótesis y dominio | Qué permite y qué permanece abierto |
|---|---|---|---|
| A: inversión modular y multiplicación prima | **EXACTO-REPRESENTACIONAL** | `N≥4` par; `p∤N` | Conmutación de operadores; no cota de correlaciones |
| B: proyección impar y dimensión | **EXACTO-REPRESENTACIONAL** | `H_N=ℓ²(U_N)` | Descomposición en dos sectores de dimensión `φ(N)/2`; no ahorro asintótico acreditado |
| C′: correlación como diferencia de normas | **EXACTO-REPRESENTACIONAL** | Peso real simétrico, `φ≥0` | Igualdad con `G(N)`; no estimación de norma de la parte impar |
| D: sectores CRT y sus dimensiones | **EXACTO-REPRESENTACIONAL, CLÁSICO** | Descomposición `N=∏q_j` en potencias primas coprimas | Reflexión tensorial y sectores ortogonales; el vector `a_N` no tiene por qué factorizar |
| E–F: desplazamientos y funciones `L` | **EXACTO-ANALÍTICO** | `Re(s),Re(t)>1/2`; `Re(\bar s+t)>1` para `-L'/L` | Identidades de Dirichlet en convergencia absoluta; extensión crítica y cotas abiertas |
| G: defecto del peso de von Mangoldt | **EXACTO-ANALÍTICO** | `p∤N`, `Re(s)>1/2` | Soporte y norma cerrados; no cancelación entre caracteres |
| H: estabilidad bajo reconstrucción | **EXACTO-REPRESENTACIONAL** | Aproximante `b_N∈H_N` y error `ε_N` conocido | Desigualdad de error; no construcción uniforme de rango pequeño |
| NG–1: límite de datos modulares | **EXACTO, NO-GO RESTRINGIDO** | Se fija la estructura modular; pesos no negativos libres | La estructura sola no fija `G`; con soporte exacto sí se fija su positividad |
| NG–2: transporte modular `Q_N` | **EXACTO, NO-GO** | Dominio fundamental / truncación `1..K` | Norma `√⌈K/N⌉`, sin extensión acotada al espacio infinito |
| NG–3: defecto frente al autovector | **EXACTO, NO-GO RESTRINGIDO** | `p∤N`, `Re(s)>1/2` | `Ω` no hereda en general la identidad de autovector limpio |
| Control escalón `N=30,42,60,210` y barrido | **CERTIFICADO FINITO** | `φ_step=1_[1/3,2/3]`, discontinuo | Identidades simbólicas y límites racionales; no test del operador de Hardy |
| Serie singular y término diagonal asintótico | **CLÁSICO** | `φ` suave para el asintótico; `N→∞` par | Línea base de densidad y de `D(N)`; no asintótico universal de `G(N)` |
| Transferencia al Hardy `T_N`, cota de norma | **ABIERTO / CONDICIONAL EN LI–LIU** | GRH(N) + hipótesis espectral S o R, como en el artículo | Requiere mapa entre espacios y estimaciones uniformes |
| Goldbach incondicional | **ABIERTO** | Todos los pares suficientemente grandes o todos `N≥4` | Ausencia de prueba incondicional |

**Vocabulario:** en esta nota, «reflexión» significa exclusivamente `J_N f(r)=f(−r)`. El operador de cuatro fases `J²=−I` del repositorio histórico es **otro operador**. «Herencia» exige transportar una relación identificada, y «economía» requiere contabilizar construcción, evaluación y reconstrucción; ninguna reducción de dimensión equivale por definición a una mejora de complejidad.

## 1. Antecedentes y contrato externo

**Procedencia interna (fechas impresas, no certificados públicos de primer depósito):**

- 11-IX-2026: `un_cierre_varios_canales_CRT_v0_1.md`, herencia y novedad por factores coprimos.
- 15-X-2026: `FORMALIZACION_ECO_HERENCIA_RELACIONAL_2026-10-15.pdf`, interfaz, cierre y contexto de consulta.
- 23-X-2026: `R01_PUENTE_NORMALIZACION_AUTORREFERENCIA_YM.es.md`, módulo común al incorporar un primo independiente.
- 1-XI-2026: `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md`, desplazamiento `S_p`, entrelazamiento algebraico, Nyman–Beurling y errores de aproximación.
- 8–12-XI-2026: `economia_del_calculo`, `que_calculo_deja_de_hacerse`, `Imagen_Total_4_0` y `DE_LA_INDEFINICION_AL_CIERRE_DE_LA_INFORMACION_v01.md`.

Repositorios de procedencia:

1. https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
2. https://github.com/EndlessMonkeyProyect/Relational-Geometry-program
3. https://github.com/EndlessMonkeyProyect/relational-geometry-Model

**Artículo externo:** Jiamin Li y Jianya Liu, *A Conditional Proof of the Goldbach Conjecture*, Universidad de Shandong, 13-XI-2026, https://mrc.sdu.edu.cn/info/1018/2193.htm, PDF https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf. Véanse ecuaciones (1.2)–(1.5), (2.1)–(2.4), el espacio Hardy y §6. Su resultado para todos los pares suficientemente grandes es **condicional a GRH(N) más S o R**.

**Línea base clásica:** por los resultados de Montgomery–Vaughan (1975), el número de excepciones a Goldbach hasta `x` cumple `E(x)≪x^(1−δ)` para algún `δ>0`; en particular, casi todos los pares suficientemente grandes son suma de dos primos. Este resultado no elimina todas las posibles excepciones. Fuente reciente de orientación: G. Bhowmik y L. Grimmelt, *The exceptional set of the Goldbach problem*, arXiv:2607.27282, 2026, https://arxiv.org/abs/2607.27282. La forma ponderada fija de Li–Liu tiene hipótesis adicionales; el teorema clásico de «casi todos» no se presenta aquí como idéntico, sin más, a su fórmula para cada `N`.

## 2. Teoremas A, B y C′: inversión y correlación

Para `N≥4` par, sea `U_N=(ℤ/Nℤ)^×`, `H_N=ℓ²(U_N)` con producto escalar usual. Para `p` primo y `p∤N`, defínanse

```math
(J_Nf)(r)=f(-r),\qquad (M_{p,N}f)(r)=f(p^{-1}r),\qquad P_\pm=\frac{I\pm J_N}{2}.
```

**A [EXACTO-REPRESENTACIONAL].** `J_N²=I=J_N*` y `J_N M_{p,N}=M_{p,N} J_N`. La prueba evalúa ambas composiciones en `r`: las dos son `f(−p^{-1}r)`.

**B [EXACTO-REPRESENTACIONAL].** Los caracteres `χ` de `U_N` forman una base ortogonal; `J_Nχ=χ(−1)χ`. El espacio `im P_-` está generado por los caracteres impares, y `dim(im P_-)=φ(N)/2`. No hay puntos fijos de `r↦−r` en `U_N` para `N≥4`, luego las trazas `tr J_N=0` y `tr P_-=φ(N)/2`.

Para `φ∈C_c^∞(ℝ)`, `φ≥0`, `φ(u)=φ(1−u)`, soporte en `[1/3,2/3]`, defínase

```math
a_N(r)=N^{-1/2}\!\sum_{\substack{1\le n<N\\n\equiv r\ (N)}}\!\Lambda(n)\phi(n/N),\qquad
G_\phi(N)=\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}\Lambda(n)\Lambda(m)\phi(n/N)\phi(m/N).
```

**C′ [EXACTO-REPRESENTACIONAL, formulación principal].**

```math
\boxed{G_\phi(N)=\|P_+a_N\|^2-\|P_-a_N\|^2.}
```

*Prueba.* El soporte de `φ` garantiza que `n+m≡0 (mod N)` y la presencia simultánea de ambos términos equivalen aquí a `n+m=N`. Así, `G_φ(N)=⟨a_N,J_N a_N⟩`. Por `J_N=P_+−P_-` y ortogonalidad de ambas proyecciones, se obtiene C′. `□`

**Corolario C.1 (representación).**

```math
\boxed{G_\phi(N)=D_\phi(N)-2\|P_-a_N\|^2,\quad
D_\phi(N)=\|a_N\|^2.}
```

Parseval proporciona `G_φ(N)=D_φ(N)−(2/φ(N))Σ_{χ(-1)=-1}|Σ_ra_N(r)χ(r)|²`, en la normalización declarada. La condición `G_φ(N)>0` es equivalentemente `||P_+a_N||²>||P_-a_N||²`; se **etiqueta equivalencia representacional**, no criterio independiente de prueba.

**Lema de soporte (cerrado).** Para cualquier `a:U_N→[0,∞)` y `S=supp(a)`,

```math
\boxed{\langle a,J_Na\rangle>0\iff S\cap(-S)\ne\varnothing.}
```

*Prueba.* `⟨a,Ja⟩=Σ_r a(r)a(−r)` es suma de términos no negativos y es positiva exactamente cuando existe una pareja de índices reflejados con ambos pesos positivos. `□` El soporte exacto sí determina la **positividad**, aunque no el **valor** de la correlación. Esta precisión corrige la formulación más amplia sugerida para el no-go.

## 3. Teorema D: sectores CRT con dimensiones

Escríbase `N=∏_{j=1}^t q_j`, con `q_j=ℓ_j^{α_j}` coprimos. Por CRT,

```math
H_N\cong\bigotimes_{j=1}^t H_{q_j},\qquad
J_N\cong\bigotimes_{j=1}^t J_{q_j}.
```

Para `σ_j∈{±1}`, sea `P_{σ_j}^{(j)}=(I+σ_jJ_{q_j})/2` y `P_σ=⊗_jP_{σ_j}^{(j)}`.

**D [EXACTO-REPRESENTACIONAL, CLÁSICO].** Los `P_σ` son proyecciones ortogonales entre sí y suman la identidad. Además,

```math
\boxed{\langle a,J_Na\rangle=\sum_{\sigma\in\lbrace\pm1\rbrace^t}
\left(\prod_j\sigma_j\right)\|P_\sigma a\|^2.}
```

*Prueba.* Cada `J_{q_j}` es involución autoadjunta; sus dos proyecciones espectrales son ortogonales y suman `I`. Sus productos tensoriales también lo son. La identidad `⊗_j(P_+^{(j)}−P_-^{(j)})=Σ_σ(∏σ_j)P_σ` da la fórmula. `□`

**Corolario D.1 (paridad y dimensión).**

```math
\boxed{\operatorname{im}P_-\cong
\bigoplus_{\prod_j\sigma_j=-1}\bigotimes_j\operatorname{im}P_{\sigma_j}^{(j)},
\qquad \dim\operatorname{im}P_-={\varphi(N)\over2}.}
```

Para cada potencia prima `q_j≥3`, `dim im P_{±}^{(j)}=φ(q_j)/2`; para `q_j=2`, `dim im P_+^{(j)}=1` y `im P_-^{(j)}={0}`. Se deduce de la traza del operador de inversión local. La identidad separa sectores, **no factoriza automáticamente** el vector de von Mangoldt.

**Matriz CRT explícita, `N=30` y función escalón.** Identificando `U_30≅U_2×U_3×U_5`, ordenando filas `1,2 mod 3` y columnas `1,2,3,4 mod 5`, se obtiene:

```math
A_{30}={1\over\sqrt{30}}
\begin{pmatrix}
0&0&\log13&\log19\\
\log11&\log17&0&0
\end{pmatrix}.
```

El menor de filas 1,2 y columnas 1,3 es `−log(11)log(13)/30≠0`; como sólo hay dos filas, `rank(A_30)=2`. Es un certificado exacto de que el vector no es un tensor puro en esa partición.

## 4. Densidades locales, serie singular y diagonal

Para cada primo `ℓ`, los valores prohibidos por la pareja `r,N−r` son `ν_ℓ(N)=1` si `ℓ|N` y `2` si `ℓ∤N`. Para el producto de los primos `Q_z=∏_{ℓ≤z}ℓ`, el número de clases admisibles es `∏_{ℓ≤z}(ℓ−ν_ℓ(N))`. Al normalizar por la densidad de dos primos independientes aparece la serie singular clásica:

```math
\boxed{\mathfrak S(N)=2C_2\prod_{\substack{\ell\mid N\\\ell>2}}\frac{\ell-1}{\ell-2},\qquad
C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right).}
```

Es una **compatibilidad local**, no una estimación positiva de parejas efectivas.

**Proposición clásica sobre la diagonal.** Para un peso fijo `φ` como el del §2, cuando `N→∞` a través de pares,

```math
\boxed{D_\phi(N)=c_\phi\log N+o(\log N),\qquad
c_\phi=\int_0^1\phi(u)^2\,du.}
```

*Esbozo.* El teorema de los números primos con sumación parcial aplica a `Σ_p (log p)² φ(p/N)²` en el intervalo proporcional `[N/3,2N/3]`, y produce `N c_φ log N+o(N log N)`. Las potencias primas propias dan `O(√N log²N)` antes de dividir por `N`. Un primo que divide `N` dentro del soporte sólo puede ser una excepción de tamaño comparable a `N` (por ejemplo `N=2p`), y su contribución es `O(log²N/N)`. Por tanto, el resultado es **incondicional** y usa el PNT ordinario; **no requiere un PNT uniforme en progresiones con módulo creciente `N`**. Esta diagonal de tamaño `log N` contrasta con el objetivo `G_φ(N)≈c_φ S(N)` de tamaño constante hasta factores aritméticos.

**Línea base «casi todos»:** la cota clásica de excepciones establece existencia para casi todos los pares; la positividad de cada `G_φ(N)` en el soporte fijo, bajo los contratos de Li–Liu, es una afirmación más específica que aquí queda condicional.

## 5. Puente analítico E, F y defecto G

En `ℓ²(ℕ)` se fijan `S_pe_n=e_{pn}`, un carácter de Dirichlet `χ` módulo `N` extendido por cero fuera de las unidades y los vectores

```math
\Psi_{s,\chi}=\sum_{n\ge1}\chi(n)n^{-s}e_n,
\qquad \Omega_{t,\chi}=\sum_{n\ge1}\Lambda(n)\chi(n)n^{-t}e_n,
\quad \Re s,\Re t>\tfrac12.
```

**E [EXACTO-ANALÍTICO].** `S_p^*Ψ_{s,χ}=χ(p)p^{−s}Ψ_{s,χ}` y

```math
\langle\Psi_{s,\chi},\Psi_{t,\psi}\rangle
=L(\bar s+t,\bar\chi\psi),\qquad \Re(\bar s+t)>1.
```

**F [EXACTO-ANALÍTICO EN CONVERGENCIA ABSOLUTA].** Si `χ_0` es el carácter principal,

```math
\boxed{\langle\Psi_{s,\chi_0},\Omega_{t,\chi}\rangle
=-\frac{L'}{L}(\bar s+t,\chi),\qquad\Re(\bar s+t)>1.}
```

*Prueba.* Expansión del producto escalar y serie de Dirichlet de `−L'/L` en su región de convergencia absoluta. `□` La **continuación analítica** y el paso a una estimación en la franja crítica son problemas separados y abiertos en esta construcción.

**G [EXACTO-ANALÍTICO, defecto prima].** Para `p∤N`, `σ=Re(s)>1/2`,

```math
\Delta_{p,s,\chi}:=(S_p^*-\chi(p)p^{-s}I)\Omega_{s,\chi}
=\chi(p)p^{-s}\sum_{n\ge1}\chi(n)n^{-s}
[\Lambda(pn)-\Lambda(n)]e_n.
```

Los únicos coeficientes no nulos están en `n=1` y `n=q^k`, `q≠p`, `q∤N`, `k≥1`, y

```math
\boxed{\|\Delta_{p,s,\chi}\|^2=p^{-2\sigma}
\left[(\log p)^2+\sum_{\substack{q\ne p\ \text{primo}\\q\nmid N}}
\frac{(\log q)^2}{q^{2\sigma}-1}\right]<\infty.}
```

*Prueba.* `Λ(p)-Λ(1)=log p`; si `n=p^k`, la diferencia vale cero; si `n=q^k` con `q≠p`, vale `−log q`; y si `n` tiene dos factores primos distintos ambas `Λ` se anulan. `χ` suprime las potencias que comparten factor con `N`. La suma ortogonal por las bases `e_n` y las series geométricas en `q^{-2σ}` dan la fórmula. Se usa `∑(log n)²n^{-2σ}<∞`. `□`

**Lectura cuantitativa:** la norma individual no depende de la fase `Im(s)` ni de cuál sea `χ` entre caracteres de módulo `N`; cerca de `σ=1/2` la suma diverge. La fórmula delimita la pérdida de la regla de autovector pero no produce cancelación entre caracteres ni cota de `L'/L` en la franja crítica.

## 6. No-go NG–1: qué determinan los datos modulares

Se distinguen dos afirmaciones.

**NG–1a [EXACTO].** La estructura `(U_N,J_N,ν_ℓ(N))`, sin conocer los pesos o el soporte aritmético, no determina el valor ni la positividad de `⟨a,J_Na⟩` para todos los vectores no negativos. En `N=30`,

```math
a=e_{[11]},\quad b=e_{[11]}+e_{[19]},\quad
\langle a,J_{30}a\rangle=0,\quad\langle b,J_{30}b\rangle=2.
```

La estructura modular es la misma, pero **los soportes son distintos**. Es un test de los datos modulares *sin soporte*, no de un contrato que incluya el soporte exacto.

**NG–1b [EXACTO].** Incluso **fijando el mismo soporte** `S={[11],[19]}`, el valor de la correlación no queda determinado por su soporte: para `c=e_[11]+e_[19]` y `d=e_[11]+2e_[19]` se obtiene `⟨c,Jc⟩=2` y `⟨d,Jd⟩=4`. Sin embargo, ambos son positivos, de acuerdo con el lema de soporte del §2.

**Conclusión del límite:** la estructura CRT y sus densidades no proporcionan la distribución de pesos `Λ(n)`; conocer **todo** el soporte ya certifica positividad, pero obtener ese soporte para los pares futuros es precisamente el problema aritmético. No se debe afirmar que soporte idéntico permite cambiar de correlación positiva a nula manteniendo todos los pesos estrictamente positivos sobre las mismas clases.

## 7. No-go NG–2: norma exacta del transporte modular

Defínase en las sucesiones finitas `Q_Ne_n=e_[n]` si `(n,N)=1` y cero en otro caso. Para `p∤N`, `Q_NS_p=M_{p,N}Q_N` en ese dominio.

**NG–2 [EXACTO].** Para `Q_{N,K}` restringido a `ℓ²({1,…,K})`, si `K≥1`,

```math
\boxed{\|Q_{N,K}\|=\sqrt{\left\lceil\frac KN\right\rceil}.}
```

Por tanto, `||Q_{N,N−1}||=1`, mientras que `sup_K||Q_{N,K}||=∞`; no existe extensión acotada `Q_N:ℓ²(ℕ)→H_N`.

*Prueba.* La matriz tiene una fila por cada residuo unitario y una columna por índice. El producto `Q_{N,K}Q_{N,K}^*` es diagonal, con entrada igual al número de representantes de cada clase residual dentro de `1..K`. Su mayor valor es `⌈K/N⌉`: la clase de `1` lo alcanza y ninguna tiene más representantes. La norma es la raíz cuadrada del mayor autovalor. `□`

El crecimiento deriva de **sumar repetidamente índices distintos en el mismo residuo**, no de una propiedad vaga de «no periodicidad». La comparación con un espacio de Hardy necesita un mapa distinto con normalización y cotas demostradas.

## 8. Reconstrucción H: error y costo

Sea `a=a_N∈H_N` y `b∈H_N` una representación aproximada; `ε_N=||a−b||`.

**H [EXACTO-REPRESENTACIONAL].**

```math
\boxed{\left|\langle a,J_Na\rangle-\langle b,J_Nb\rangle\right|
\le (2\|b\|+\varepsilon_N)\varepsilon_N.}
```

*Prueba.* Escribiendo `a=b+h`, el residuo es `2Re⟨h,Jb⟩+⟨h,Jh⟩`. Por Cauchy–Schwarz, su valor absoluto se acota por `2||b||||h||+||h||²`. `□`

Para `b=⊗_j b_j`, se tiene

```math
G_\phi(N)\ge\prod_j\langle b_j,J_{q_j}b_j\rangle
-(2\|b\|+\varepsilon_N)\varepsilon_N.
```

Para `b=Σ_{ν=1}^R⊗_j b_j^{(ν)}`, la correlación de `b` se evalúa como

```math
\langle b,J_Nb\rangle=
\sum_{\mu,\nu=1}^R\prod_j\langle b_j^{(\mu)},J_{q_j}b_j^{(\nu)}\rangle.
```

La expresión necesita `R²t` productos locales **una vez obtenidos los factores**; el costo real suma producirlos, certificar `ε_N`, evaluarlos y reconstruir la respuesta. `dim(im P_-)=φ(N)/2` es un ahorro de dimensión **y sólo permite afirmar eso**: no impide otras estrategias de ahorro ni demuestra alguna en esta construcción.

**Separación de potencias primas.** Sea `G_{pp,φ}` la correlación restringida a dos primos y `R_{N,φ}=G_φ-G_{pp,φ}≥0`. Para `M=||φ||_∞` y `P_*(N)` el número de potencias primas propias `q^k≤N`, `k≥2`,

```math
0\le R_{N,\phi}\le\frac{2M^2(\log N)^2}{N}P_*(N),\quad
P_*(N)\le\sqrt N+(\log_2N)N^{1/3}.
```

Luego `⟨b,Jb⟩>(2||b||+ε_N)ε_N+R_{N,φ}` sería una **condición suficiente** para dos primos. Obtener un aproximante `b_N`, su cota de error y un costo favorable de modo uniforme sigue **ABIERTO**.

## 9. Certificación finita, valor local y frontera de interpretación

**Peso ilustrativo distinto del artículo:** `φ_step=1_[1/3,2/3]`. Se denotan `G_step`, `D_step` y `G_{pp,step}` para evitar identificarlos con los resultados espectrales demostrados para `φ∈C_c^∞`.

El archivo `verificar_puente_goldbach_v3.py` emplea dos métodos de certificación: (i) igualdades simbólicas de polinomios en los símbolos `log p` con coeficientes racionales para los **499 pares `4≤N≤1000`**, y (ii) intervalos de logaritmos obtenidos a partir de la serie racional `log x=2Σ_{j≥0}y^{2j+1}/(2j+1)` con cola explícita `≤2y^{2M+1}/((2M+1)(1−y²))`, después de reducir `x=2^kt` a `1≤t<2`, con `M=24`.

| `N` | `G_step(N)` en intervalo certificado | `D_step(N)` en intervalo certificado | `G_{pp,step}(N)` en intervalo certificado |
|---:|---:|---:|---:|
| 30 | `[0.9551670037049, 0.9551670037050]` | `[0.9675228566874, 0.9675228566875]` | `[0.9551670037049, 0.9551670037050]` |
| 42 | `[0.6567691599176, 0.6567691599177]` | `[0.6932960268351, 0.6932960268352]` | `[0.4396319708729, 0.4396319708730]` |
| 60 | `[0.7628421007726, 0.7628421007727]` | `[0.7666833579532, 0.7666833579533]` | `[0.7628421007726, 0.7628421007727]` |
| 210 | `[1.5290363470560, 1.5290363470561]` | `[1.5561129064321, 1.5561129064322]` | `[1.4265289191294, 1.4265289191295]` |

Para `N=30`, la identidad simbólica es:

```math
G_{step}(30)=\frac{2}{30}(\log11\log19+\log13\log17),
\quad D_{step}(30)=\frac1{30}\sum_{p\in\lbrace11,13,17,19\rbrace}(\log p)^2.
```

`2||P_-a_30||²∈[0.0123558529824,0.0123558529825]` también está certificado.

**Contabilidad numérica de la serie singular:** para `N=30`, `S(30)=16C₂/3`. Dado `c_step=∫φ_step²=1/3`,

```math
\boxed{c_{step}\mathfrak S(30)-G_{step}(30)
=\frac{16}{9}C_2-G_{step}(30)\approx0.218454002245.}
```

Para evitar fingir una certificación de todas las cifras de `C₂`, el verificador da una banda rigurosa a partir del producto sobre primos `p≤200000` y la cola `1−Σ_{k≥B}k^{-2}≤\prod_{p>B}(1−(p−1)^{-2})≤1`:

```math
\boxed{0.21844858028<\frac{16}{9}C_2-G_{step}(30)<0.21845444843.}
```

El valor central aproximado emplea la constante clásica `C₂≈0.6601618158468696`, y **no se vende como certificado de 12 decimales**. La banda del archivo es la certificación efectiva.

**Límite de contrato decisivo:** `φ_step` es discontinuo, y `N=30` está por debajo del umbral `N>e^{10}` utilizado por Li–Liu para construir `T_N` en su contrato. Por ello esta diferencia escalar **no es una medición certificada de `⟨T_Nv_N,v_N⟩`**, ni un test de su hipótesis R; es sólo un diagnóstico aritmético ilustrativo. Para probar una identidad de Hardy hay que trabajar con un peso suave admisible, en el dominio apropiado y bajo las hipótesis de construcción.

## 10. Frontera espectral y obligaciones localizadas

Li–Liu utiliza, bajo sus hipótesis y normalización,

```math
c_\phi\mathfrak S(N)-G_\phi(N)=\langle T_Nv_N,v_N\rangle,
\quad\|v_N\|^2=1,
```

y bajo su hipótesis espectral R una cota del tipo

```math
\boxed{\|T_N\|\le\delta_N,
\qquad\delta_N=\sqrt{\frac{\mathfrak S(N)}N}(\log N)^{3/2}.}
```

**Pendientes diferenciados:**

1. **Mapa de espacios**: definir un operador desde referencias/sectores CRT al espacio Hardy de Li–Liu y acreditar dominio, continuidad y normas. `Q_N` no sirve sin una modificación sustancial.
2. **Estimación aritmética**: demostrar control de correlaciones de `−L'/L` entre caracteres impares en la franja crítica. Las identidades de §5 sólo se usan directamente en convergencia absoluta.
3. **Reconstructor uniforme**: exhibir `b_N`, rango `R(N)`, cota `ε_N` y costo total que hagan positiva la condición de §8, incluso descontando potencias primas.
4. **Control espectral**: demostrar una cota de `||T_N||` dentro de su contrato (o alternativa independiente), sin adoptar como premisa la propia conclusión buscada.
5. **Controles adversariales**: mantener separadas la información de soporte y la de magnitud de pesos; comparar distinto soporte y soporte idéntico; comprobar que la compresión local puede perder correlaciones cruzadas.

**Límite de interpretación:** el programa aporta aquí una representación compatible y pruebas finitas; el artículo externo aporta un operador específico y una implicación condicional. Ninguna identidad presentada es una cota nueva para `T_N` ni una demostración incondicional de Goldbach.

## 11. Lectura ROSI y reproducción

| Bloque | Dictamen | Obligación / alcance |
|---|---|---|
| A–D y C′ | **RESOLVED** | Álgebra modular y proyecciones, contenido representacional clásico |
| E–G | **RESOLVED** dentro de los semiplanos | Identidades analíticas, sin estimación crítica |
| NG–1, NG–2 | **RESOLVED** | Contraejemplos y norma exacta del transporte |
| H | **RESOLVED** | Estabilidad condicional al error `ε_N` disponible |
| Certificación `N≤1000` | **RESOLVED FINITE** | 499 casos simbólicos y cuatro intervalos numéricos |
| Transporte al Hardy y cota espectral | **OPEN** | Definir y controlar mapa, error y operador |
| Prueba de Goldbach | **OPEN** | Se requiere positividad uniforme para pesos de primos efectivos |

**Ejecutar:** `python3 verificar_puente_goldbach_v3.py` (biblioteca estándar; tiempo y plataforma sujetos al equipo). El código prueba identidades simbólicas en `4≤N≤1000`, verifica la forma de la matriz CRT y la multiplicidad de clases en truncaciones, calcula intervalos racionales para `30,42,60,210` y certifica una banda para el diagnóstico `C₂` con una cota elemental de la cola. Los ejemplos finitos no prueban resultados de infinitud.

---

**Endless Monkey Project**  
*Relational Geometry Program*
