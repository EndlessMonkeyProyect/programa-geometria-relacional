# O92 — Normalización compuesta: armónicos, sistema, nodos y transporte entre escalas

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**22 de octubre de 2026 · suplemento aditivo después de O91.**  
**Fuentes internas auditadas:** O40, O41, O61, O68, O74, O79, O88, O91.  
**Etiquetas:** [O] ontología propia del programa; [T] demostración matemática bajo contrato; [E] chequeo computacional; [F] refutación de una *interfaz especificada*, no del programa completo; [A] abierto.

## 0. Veredicto de la revisión

**Corrección de O91.** El contraste de O91 utilizaba dos vectores diferentes de pesos de los cuatro armónicos, aunque tenían el mismo mínimo común múltiplo `N=12` y los mismos tres momentos agregados. Una interfaz que guarda las **relaciones entre cada armónico y el sistema** distingue inmediatamente ambos estados. Su cuarto momento `C=⟨|Δω|²⟩` se reconstruye de esos pesos. **No es información independiente si todos los pesos individuales ya se conservaron.**

**Demostración positiva de O92.** Separar la magnitud global del campo de los coeficientes armónicos *complejos y vectoriales* normalizados produce una descripción exactamente reconstructible y una ley de evolución derivada de Navier–Stokes. La ley revela explícitamente qué parte de la redistribución entre armónicos se debe a disipación y cuál a transferencia no lineal, dependiente de fases y orientaciones. No hace falta crear un nuevo normalizador ontológico.

**Límite preciso.** Esta normalización completa guarda, en general, infinitos coeficientes. La equivalencia exacta con Navier–Stokes por cambio de variables **no aporta por sí sola una estimación a priori de regularidad**. Falta probar que existe una compresión relacional físicamente suficiente que conserve el presupuesto de transferencia y obtenga un control uniforme de concentración para todo dato suave 3D sin fuerza.

## 1. Ontología y capas ya desarrolladas [O/T]

No cambiamos el orden del programa: unidad → comparación parte/todo → referencia que normalizó → resto referenciado → cierre propio → nueva circunstancia. La identidad no reside en el resto aislado ni en una geometría fija. Las normalizaciones tienen funciones **diferentes**, que no se reemplazan unas por otras:

1. **Entre armónicos**: relaciones de amplitudes, fases y orientaciones de los canales realmente activos, junto a enlaces triádicos potenciales o efectivos. No identificar un armónico con una partícula ontológica.
2. **Del sistema**: magnitud física global y relación entre la totalidad y las contribuciones normalizadas de cada canal.
3. **Del nodo/circuito**: cierre de cuatro enlaces, `H=∏(a_i/b_i)=1` bajo la hipótesis de contacto ideal O74. No convierte el circuito en ley NS.
4. **De ritmos**: dos giros `k_1,k_2` con clase primitiva `(q,p)`, múltiplo `L=gcd(k_1,k_2)` y transformación unimodular de Bézout O68, cuando los números de vueltas existen.
5. **De escala/ramificación**: refinamientos `H_N↪H_M` si `N|M`, mapas de proyección compatibles y, para cubiertas no invertibles, etiqueta `h` que identifica la preimagen O40/O88.

El conjunto formal es un **diagrama de interfaces compatibles**. No hay una identificación canónica demostrada entre el entero de vueltas `L`, el mcm de etiquetas Fourier `N`, los brazos de contacto `a_i,b_i` y la intensidad o el radio de un fluido. Una composición física exige mapas que especifiquen qué estado se observa en cada interfaz.

### T92.1 — Lo que sí se compone de manera exacta [T, recuperado]

- Para `N|M|K`, el refinamiento O40 cumple `i_M^K ∘ i_N^M=i_N^K`.
- Para la pareja primitiva `(q,p)`, Bézout permite `aq+bp=1`. La matriz `[[a,b],[p,-q]]` tiene determinante `−1` y reconstruye íntegramente las dos fases. Si un mapa posterior multiplica las dos fases por `n>1`, necesita además la etiqueta de rama: tiene `n²` preimágenes.
- Para cuatro enlaces idealizados con `a_i=r_i,b_i=r_{i+1}`, el producto de holonomía se telescopa a `1`; si los brazos de ida/vuelta de un mismo nodo difieren, el cierre no está garantizado.

**Prueba:** O40 (inclusiones), O68 (matriz inversa entera), O74 (producto telescópico), O88 (grado de cubierta). Las 86 comprobaciones que ejecuta el verificador O92 comprueban instancias, pero no reemplazan esas pruebas.

La **proposición no demostrada** es que los cuatro tipos de coordenadas tengan una realización común canónica en **cada** solución tridimensional. La composición algebraica no crea esos mapas físicos.

## 2. Volver a O91 sin perder los armónicos [T/F]

O91 tenía cuatro frecuencias `k=1,2,3,4` y amplitudes cuadráticas `w_k>0`, con

\[
 m_j=\sum_{k=1}^{4} k^{2j} w_k,\quad j\in\{-1,0,1,2,\dots\}.
\]

Los estados racionales del contraste eran

\[
\begin{aligned}
 w^{(C)}&=(7/12,\ 539/150,\ 1/20,\ 817/300),\\
 w^{(D)}&=(203/300,\ 427/150,\ 113/100,\ 689/300).
\end{aligned}
\]

Ambos tienen `N=12` y `m_{-1}=23867/14400`, `m_0=139/20`, `m_1=2949/50`; **pero no tienen iguales los pesos individuales**.

Introducimos, conforme a la normalización ya trabajada, la distribución armónica dentro del sistema:

\[
\boxed{W=m_0=\sum_{k=1}^4w_k,\qquad \rho_k=w_k/W,\qquad \sum_k\rho_k=1.}\tag{92.1}
\]

El mapa `(W,(ρ_k))↦(w_k)` es exactamente invertible: `w_k=Wρ_k`. En particular,

\[
\boxed{m_j=W\sum_{k=1}^{4}k^{2j}\rho_k.}\tag{92.2}
\]

En O91 `m_2^{(C)}=7593/10` y `m_2^{(D)}=7257/10`. No se necesita medir un nuevo cuarto momento si `ρ_k` y `W` ya son conocidos: (92.2) lo computa. Ésta es una corrección **sustantiva** de la interpretación de O91, no una invalidación del cálculo de sus momentos.

Para esta clase de cizallas, `w_k(t)=w_k(0)e^{-2νk²t}` y, definiendo `D=Σ k²ρ_k`, resulta:

\[
\boxed{W'=-2νDW,\qquad\rho_k'=-2ν(k²-D)\rho_k.}\tag{92.3}
\]

La ecuación conserva `Σρ_k=1` y reproduce **exactamente toda la evolución** para cualquier conjunto inicial de pesos de los cuatro armónicos. No aparece un quinto observable. Esto sí confirma suficiencia dinámica dentro de esa clase lineal exacta.

## 3. Normalización armónico ↔ sistema para NS 3D completo [T, identidades PDE]

Sea `u` suave, real, solenoidal, de media cero, periódica en `T³`, viscosidad `ν>0`, **sin fuerza**. Con coeficientes de Fourier vectoriales complejos `û_k`, ponemos

\[
\boxed{A(t)=\left(\sum_{k\ne0}|\hat u_k|²\right)^{1/2}>0,
\qquad z_k(t)=\hat u_k/A(t),\qquad \sum_{k\ne0}|z_k|²=1.}\tag{92.4}
\]

`A` es la magnitud del **sistema**; `z_k` contiene magnitud *relativa*, fase y polarización del **armónico**. Si conservamos todos los `z_k` y `A`, se reconstruye el campo: `û_k=A z_k`. Esto formaliza la normalización doble; no debe confundirse con un teorema de compresión finita.

La ecuación proyectada a Fourier es

\[
\dot{\hat u}_k=-ν|k|²\hat u_k-i\,\mathbb P_k
\sum_{p+q=k}(q\cdot\hat u_p)\hat u_q,
\quad \mathbb P_k=I-kk^\top/|k|².
\]

Definimos, **sin introducir un nuevo normalizador**, el operador de interacción escrito en las coordenadas normalizadas:

\[
\mathcal B_k(z,z)=-i\,\mathbb P_k\sum_{p+q=k}(q\cdot z_p)z_q,
\qquad D=\sum_{k\ne0}|k|²|z_k|².
\]

### T92.2 — Sistema cerrado exacto en todas las coordenadas [T]

\[
\boxed{\dot A=-νDA,\qquad
\dot z_k=-ν(|k|²-D)z_k+A\mathcal B_k(z,z).}\tag{92.5}
\]

**Demostración.** El balance de energía de NS sin fuerza en la caja periódica da
`(A²)'=−2νΣ|k|²|û_k|²=−2ν A²D`, luego `A'=−νAD`. Derivar `z_k=û_k/A`, sustituir el generador Fourier y la expresión de `A'` produce (92.5). La parte no lineal conserva la norma cuadrática por la propiedad antisimétrica del transporte: `Σ Re(conj(z_k)·B_k)=0`. Por tanto `Σ|z_k|²=1` sigue siendo cierto. ∎

Esta identidad formaliza **dos niveles simultáneos**: uno controla la intensidad total, otro la redistribución entre armónicos. No presupone que el campo sea un anillo o un circuito de engranes.

### T92.3 — Balance de concentración entre armónicos y sistema [T]

Sea `D_2=Σ|k|⁴|z_k|²`. Derivando `D` con (92.5) obtenemos:

\[
\boxed{\dot D=-2ν(D_2-D²)
+2A\sum_{k\ne0}|k|²\Re\big[\overline{z_k}\cdot\mathcal B_k(z,z)\big].}\tag{92.6}
\]

El primer término es `−2ν Var_ρ(|k|²)≤0`: **selección viscosa relativa**. El segundo es **transferencia triádica**, con fases, direcciones y acoplamientos del propio estado. Puede ser positivo o negativo. En un campo general, el término no queda determinado por el mcm de frecuencias, el tamaño total ni las magnitudes espectrales aisladas.

**No confundamos:** `D` es el promedio normalizado de `|k|²`; no es el entero ontológico `N`, ni la tasa angular del resorte, ni un límite sobre la vorticidad. La enstrofía se obtiene por `||ω||²=A²D`. La identidad (92.6) es una reescritura exacta del balance existente de estiramiento/disipación, no una cota nueva de regularidad.

## 4. La fase y la polarización faltantes: dos ensayos exactos [T/F]

### Ensayo A — Misma normalización escalar, transferencia distinta (O61)

Los datos de O61

\[
 u_θ(0)=(0,A\sin θ\cos x,A\cos θ\cos x+B\cos y),
\quad θ=0\text{ o }π/2
\]

poseen iguales índices activos, magnitudes de cada armónico, energía y enstrofía. Sin embargo, la interacción que puede poblar `k=(1,1,0)` cumple

\[
\boxed{|\mathcal T|=AB|\sin θ|.}\tag{92.7}
\]

Con `θ=0`, el modo queda vacío; con `θ=π/2`, la derivada inicial de su componente vertical contiene `AB/2 sin(x+y)`. La diferencia está en la **orientación vectorial del armónico**, no en el normalizador escalar. La clase O61 tiene soluciones suaves globales exactas; no hay singularidad en este ejemplo.

### Ensayo B — Misma magnitud y escala, transferencia de signo contrario (O79 extendido)

Tomamos `p=(1,0,0)`, `q=(0,1,1)`, `m=p+q=(1,1,1)` y polarizaciones solenoidales `a=(0,1,0)`, `b=(1,0,0)`, `c=(1,1,-2)`; añadimos la onda transversal `0.3(1,0,0) cos z` para dependencia espacial genuinamente 3D. Se consideran los datos

\[
 u_±(0)= a\cos(p\cdot x)+b\cos(q\cdot x)
 \pm0.4c\sin(m\cdot x)+0.3(1,0,0)\cos z.
\]

Para `ν=0.03`, los dos estados poseen el mismo sistema total `A=1.2349089035`, los mismos pesos `|z_k|²`, el mismo `D=1.9573770492` y `D_2=4.5016393443`. Calculando el generador (92.5) sin integrar en el tiempo:

| Término de `D'` | Fase + | Fase − |
|---|---:|---:|
| Difusión entre armónicos `−2ν(D₂−D²)` | −0.040218866 | −0.040218866 |
| Transferencia no lineal | +0.393442623 | −0.393442623 |
| **`D'(0)`** | **+0.353223757** | **−0.433661489** |

Es una prueba de **derivadas instantáneas exactas bajo la PDE**, comprobada con álgebra Fourier independiente en código (errores numéricos en identidades menores que `1e−12`); no se afirma que el régimen de fases se sostenga indefinidamente. El observable que discrimina es `z_k` **complejo vectorial** y su transferencia triádica, no un momento nuevo.

## 5. Composición relacional y criterio O41 [T/A]

Un candidato a interfaz jerárquica que **respeta** las definiciones ya desarrolladas puede representarse como

\[
\mathfrak C(u,\mathcal G)=
\big(A,\{z_k\}_{k\ne0},\text{refinamientos }i_N^M,\text{clase }(q,p),\text{etiquetas }h,\ H(\mathcal G)\big),
\tag{92.8}
\]

**sólo cuando** la geometría `G` ofrece realmente giros, nodos y brazos de contacto que se puedan medir. Los últimos campos no son funciones canónicas conocidas de `u` en la clase general; no declaramos que toda solución posea exactamente cuatro nodos ni que todos sus armónicos compartan un ciclo físico.

- **Representabilidad:** para todas las coordenadas normalizadas `A,z`, la evolución (92.5) es reconstructible mientras exista la solución suave. Refinamientos de fase y etiquetas de rama respetan O40/O88.
- **Suficiencia predictiva:** el criterio de O41 exige `C(u)=C(v)⇒ C(Φ_t u)=C(Φ_t v)`. Como `(A,z)` es **inyectivo**, cumple el criterio tautológicamente; no es compresión útil. Si omitimos direcciones o fases, O61/O79 violan ese criterio incluso en `t=0` (al observar la transferencia).
- **Control físico:** ninguna de las identidades (92.5)-(92.6) acota **a priori** el término de transferencia `2A Σ |k|² Re(\bar z_k·B_k)` en todos los datos, ni demuestra que el normalizador ontológico o la holonomía H lo reduzcan.

De ello se desprende el criterio fuerte, no circular: hallar una interfaz físicamente construida `C_*` que sea suficientemente comprimida para ser genuinamente informativa, y probar una estimación **uniforme** de los defectos/transferencias *antes de conocer la trayectoria futura*, para toda condición inicial admisible, con fases y orientaciones incluidas cuando alteren el signo de los acoplamientos.

**Límite explícito de refutación:** el ensayo O91 no ataca esta interfaz completa, porque los estados difieren en `ρ_k`. Los ensayos O61/O79 atacan la versión que elimina polarizaciones/fases, **no** una interfaz que ya conserva sus interacciones. Repetir estos ensayos como si refutaran cualquier normalizador del programa sería incorrecto.

## 6. Dictamen de integración en la Imagen Total

1. **[T] Reafirmado:** normalización primitiva por Bézout O68; múltiplo del conjunto; cierre H del circuito ideal O74; inclusión exacta de referencias O40 y reconstrucción con etiqueta de rama O88.
2. **[T] Corregido en O91:** el cuarto momento no añade información si se dispone de la distribución de pesos normalizados armónico-por-armónico y su total; O91 sigue siendo un buen resultado para el comparador agregado de tres momentos.
3. **[T] Nueva integración explícita (identidad PDE clásica):** (92.5)-(92.6) conectan normalización armónica y total, exhibiendo la parte de fase/orientación y la viscosidad sin introducir otro normalizador.
4. **[F] Falsadas únicamente interfaces especificadas:** sólo magnitudes armónicas o sólo promedios globales no predicen transferencias triádicas; los comparadores que conservan dirección y fase distinguen los casos.
5. **[A] Pendiente exacto:** el paso `normalización completa reconstructible → cota universal no tautológica de transferencia` en NS tridimensional. Tampoco hay morfismo universal demostrado desde los cuatro contactos de O74 hasta el sistema Fourier.

**No se modifican O40, O68, O74, O88 u O91, salvo registrar esta corrección de interpretación de O91 como suplemento.** No se declara resuelta regularidad global de Navier–Stokes 3D ni se confunde una reescritura con una nueva ley física.

## 7. Reproducción

```bash
python codigo/verificar_o92.py
```

El verificador ejecuta **86 controles** de inclusiones compuestas, Bézout, cierre C4 ideal, reconstrucción de momentos O91, proyecciones solenoidales O61 y ecuaciones normalizadas de Fourier/transferencia O79 con cuatro direcciones de onda independientes. Produce `resultados/o92_verificacion.json` y `resultados/ejecucion.txt`. La comprobación numérica valida los valores reportados; las demostraciones generales son las identidades escritas aquí.
