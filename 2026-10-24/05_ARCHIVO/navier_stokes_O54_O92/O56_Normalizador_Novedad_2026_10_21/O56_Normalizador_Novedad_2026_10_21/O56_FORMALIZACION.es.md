# O56 — La novedad del normalizador y la deformación direccional del toroide

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**21 de octubre de 2026** · Suplemento independiente **sobre** O54–O55 e Imagen Total v3.8.1; no modifica las fuentes históricas.  
**Estado:** [O] ontología original, [D] contrato, [T] teorema exacto bajo hipótesis, [E] simulación reproducible, [F] contraejemplo, [A] abierto.

## 0. Conclusión central, sin perder el hilo

**[O]** La unidad toroidal conserva dos recorridos distinguibles y una referencia común. El espejo móvil permite comparar la unidad con el exterior sin alterar por sí mismo su geometría física. El múltiplo que normalizó una relación transporta su continuidad al siguiente marco, y la novedad debe acreditarse como una diferencia que el comparador anterior no podía expresar. La singularidad ontológica es un cierre propio de identidad, **no** la pérdida de suavidad de una solución PDE.

**[T/F]** Las relaciones de escala de los dos radios y la mera ampliación de un denominador son insuficientes para decidir si la perpendicularidad **material** se conservará. Dos soluciones exactas de Navier–Stokes con iguales radios iniciales, energía, enstrofía y normalizador aritmético pueden dar distinta evolución del ángulo entre dos direcciones materiales marcadas. La diferencia mínima para la **derivada inicial** es el término cruzado `aᵀ S b` de deformación del fluido.

**[E]** La repetición sobre el anillo numérico del laboratorio O55 (malla 32³, t=1.26) reproduce esa distinción: cizallas X e Y de igual amplitud dan ángulos locales finales diferentes, aun conservando prácticamente exactamente los mismos invariantes escalares globales. La relación `r/R` efectiva global se mantiene igual entre ambas preparaciones debido a su simetría rotacional.

**[A]** No se ha derivado una ley intrínseca que asigne el siguiente múltiplo a partir de Navier–Stokes. No se ha construido una interfaz finita que cierre autónomamente la evolución general de 3D. No se demostró estabilidad del anillo ni regularidad global.

## 1. Narrativa → ontología → objetos distinguibles

Hay dos ciclos sobre el toroide geométrico: el toroidal (alrededor del anillo) y el poloidal/meridiano (alrededor del ducto). Una condición local de perpendicularidad distingue sus tangentes, pero **su perpendicularidad no implica coincidencia de fases ni simultaneidad de retornos**. La singularidad relacional no es un punto de la malla ni la curva de vorticidad elevada.

El espejo se define como una comparación desde escala positiva `L(t)`. Para radios físicos `R` y `r`, `Rhat=R/L`, `rhat=r/L`, y por tanto `rhat/Rhat=r/R`. Ésta es una identidad de representación, no una restricción dinámica ni una expansión real. Si `R,r` cambian físicamente, el cociente puede cambiar: no confundir ambas operaciones.

**[D] Dos formas de normalización que no deben mezclarse:**

- **`N_arit`** es un denominador de rejilla de fase para un contrato racional `H_N = {j/N mod 1}`. Si se propone una nueva rejilla `m`, el refinamiento es `L = mcm(N,m)`. La novedad aritmética de representación es `L/N>1`. Por sí sola **no asigna cargas, energía, vorticidad ni movimiento**.
- **`C_Q`**, o interfaz suficiente para preguntas `Q`, preserva relaciones que pueden influir en respuestas futuras. Puede necesitar, además de radios y fases, información de orientación y gradientes. Una novedad relacional se acredita mediante dos estados antes indistinguibles que una pregunta nueva diferencia.

La pregunta de O56 es qué nueva relación necesita el comparador para decidir la **evolución local del ángulo**. No se sustituye la regla ontológica del programa por una rejilla numérica impuesta.

## 2. Teorema exacto: evolución de una perpendicularidad material

**[D/T]** Para un campo `u(x,t)` suave e incompresible, sean `a(t)`, `b(t)` dos desplazamientos materiales infinitesimales transportados por la misma trayectoria `x(t)`:

```
ẋ = u(x,t),      ȧ = (∇u)a,      ḃ = (∇u)b.
S = (∇u + ∇uᵀ)/2.
```

Entonces

\[
\boxed{\frac d{dt}(a\cdot b)=2a^\top S b.}\tag{O56.1}
\]

Para `c=(a·b)/(|a||b|)`:

\[
\boxed{\dot c=\frac{2a^\top S b}{|a||b|}-c\left(\frac{a^\top S a}{|a|^2}+\frac{b^\top S b}{|b|^2}\right).}\tag{O56.2}
\]

**Prueba.** Derivar el producto `a·b` e introducir la parte simétrica `S`, pues la parte antisimétrica se cancela. Derivar los factores `|a|`, `|b|` por regla del producto y sustituir. ∎

Si `c(t₀)=0`, la tasa inicial es **exactamente** `2aᵀ S b/(|a||b|)`. Por tanto la perpendicularidad se sostiene a lo largo del intervalo si se cumple la condición cruzada `aᵀ S b=0` en todos los momentos en que se mantiene perpendicular. No basta imponerla sólo en un instante; ni que `div u=tr S=0` (incompresibilidad) obliga a ella.

**La novedad mínima para esta consulta** es `K = aᵀ S b` junto con la norma actual de los vectores (si hay un ángulo). Para las siguientes derivadas de `K` pueden hacer falta más relaciones del campo, así que aún **no** es una dinámica autónoma de un único escalar.

## 3. Experimento exacto, sin ajustar parámetros al resultado

Tome el dominio periódico de lado `8`, `k=2π/8`, `ν=0.025` y los campos

\[
u^{(j)}(x,y,z,t)=A e^{-\nu k^2t}\sin(kz)\,e_j,\qquad j\in\{x,y\}.
\tag{O56.3}
\]

**[T] Son soluciones clásicas exactas, lisas y sin forzamiento de Navier–Stokes 3D.** `div u=0`, `(u·∇)u=0`, `∂_t u=νΔu`; la presión puede ser constante. En ambas preparaciones, la energía cinética promedio es `E(t)=A²e^(−2νk²t)/4` y la enstrofía `Z(t)=k²E(t)`. Son iguales para `j=x` y `j=y`, y también para `A` y `−A`.

Sitúe sobre la superficie inicial de un toroide de radios `R=1.6`, `r=0.48` un punto con ángulo meridiano `θ=π/4`, en longitud toroidal cero:

\[
z_0=r\sin\theta,\quad a_0=e_y,\quad b_0=(-\sin\theta,0,\cos\theta).
\]

Estas dos direcciones tangentes son inicialmente ortogonales, con normas unidad. Son **marcas sobre una superficie material inicial**: el campo de cizalla exacto no se presenta como un vórtice toroidal aislado exacto.

La aplicación material para el caso `j=y` es

\[
F_t(x,y,z)=(x,y+B(t)\sin(kz),z),\quad
B(t)=\frac{A}{\nu k^2}(1-e^{-\nu k^2t}).
\tag{O56.4}
\]

La matriz de derivadas de `F_t` tiene determinante **uno**: conserva volumen y es invertible para todo tiempo finito. La superficie inicialmente toroidal sigue siendo una superficie embebida, aunque pueda cambiar su métrica y perder perpendicularidad.

Defina `β(t)=B(t) k cos(k z₀)` y `h(t)=β(t)cosθ`. Entonces para cizalla `Y`:

\[
\boxed{\cos\alpha_Y(t)=\frac{h(t)}{\sqrt{1+h(t)^2}},\qquad
\dot{\cos\alpha_Y}(0)=A k\cos(kz_0)\cos\theta.}\tag{O56.5}
\]

Para cizalla `X`, como `a=e_y` y `b` permanece en el plano `xz`:

\[
\boxed{\cos\alpha_X(t)=0\quad\text{para todo }t.}\tag{O56.6}
\]

Con `A=0.22`, `t=1.26`, `ν=0.025`: `α_X=90°`, `α_Y≈81.6332°`, `α_{−Y}≈98.3668°`. Ambos campos `X` e `Y` tienen la **misma energía y enstrofía**, y el mismo espejo prescrito, pero diferente respuesta angular **en la marca material elegida**. La pendiente inicial de `cosα_Y` es `0.117864`, determinada por el dato `K₀=0.058932`, **antes** de calcular el futuro.

**Advertencia de simetría:** los campos X e Y están emparentados por una rotación axial de toda la configuración. La diferencia de ángulo es una pregunta ligada a la **marca material fija**, no un nuevo invariante global sin observador. Si se rota también la marca al comparar, la distinción puede desaparecer. Precisamente por eso orientación y consulta deben declararse.

## 4. El múltiplo y la novedad: qué aporta y qué no

La relación inicial `r/R=3/10` admite codificación racional en denominador mínimo `N=10`. Como ensayo de refinamiento aritmético, **declaramos** una segunda rejilla de resolución `m=4`; entonces `L=mcm(10,4)=20`, `H₁₀⊂H₂₀`, con índice `2`. Es novedad exacta *en el espacio de rejillas de comparación*, no una consecuencia física forzada ni una ley para el vórtice.

Las cizallas X, Y y −Y tienen esa **misma actualización `10→20`** y la misma geometría inicial, pero distinta evolución angular. Así:

\[
\boxed{\text{refinamiento aritmético + proporción interna}\not\Rightarrow\text{evolución de perpendicularidad.}}\tag{O56.F1}
\]

La distinción relevante para esta consulta se acredita con el término nuevo `K=aᵀSb`. El comparador más pequeño para **la derivada inicial desde ángulo recto** requiere registrar la orientación de `a,b`, la contracción cruzada `K` y sus longitudes (unidad aquí). No basta nombrar «novedad» ni elegir un múltiplo después de observar el desvío.

Esta corrección no descarta que exista un **normalizador relacional dinámico más rico**. Lo obliga a transportar la información direccional necesaria, en el contrato de la pregunta. El múltiplo aritmético y esa interfaz direccional son nociones distintas hasta encontrar un puente demostrable entre ellas.

## 5. Contraste numérico sobre el anillo O55 (simulación O56)

Se ejecutó de nuevo el método pseudoespectral y RK2 del ensayo O55 para el anillo de vorticidad inicial, en malla `32³` con `ν=0.025`, `dt=0.014`, `90` pasos, tiempo final `t=1.26`; cizallas divergencia cero X o Y de igual amplitud `0.22`. Se conservaron los mismos trazadores materiales, su marca local, los radios de la superficie y la escala exterior. Ninguna fuerza externa fue añadida al sistema numérico. La **simulación del anillo** no debe identificarse con los campos de cizalla exactos de la sección 3.

| Observación | Sin perturbación | Cizalla X | Cizalla Y |
|---|---:|---:|---:|
| `r/R` inicial | 0.3000 | 0.3000 | 0.3000 |
| Ángulo local inicial | 90° | 90° | 90° |
| Energía inicial | 0.00327671 | 0.01537671 | 0.01537671 |
| Enstrofía inicial | 0.01151066 | 0.01897455 | 0.01897455 |
| `r/R` efectivo final | 0.302181 | 0.303618 | 0.303618 |
| Ángulo local final | 90.955° | **91.106°** | **81.796°** |

La igualdad de los valores globales X/Y en esta familia está relacionada con la simetría axial del anillo inicial; en cambio, la marca material de la consulta está fijada en una posición. **El cambio de orientación respecto de esa marca determina distinta deformación cruzada.** Así se reproduce en un modelo de anillo, con igualdad de energía y enstrofía iniciales, la distinción predicha por la cizalla exacta.

**Límites:** resultados finitos a baja resolución y tiempo corto; además, los vectores locales se estiman con tres trazadores separados por `ε=0.028`, no con una deformación infinitesimal perfecta. El radio efectivo de la superficie es un descriptor, no un radio físico exacto tras cualquier deformación. El campo X es una rotación del campo Y en el modelo simétrico, así que no se reclama una diferencia rotacionalmente invariante. No demuestra selección de multiplicador por NS ni regularidad global.

El contraste del **O55 histórico** también arranca con `q=0.3` y ángulo `90°` en ambos casos; sus resultados a `48³` terminaban aproximadamente a `90.612°` sin perturbación y `80.598°` con cizalla Y. O56 mantiene separadas esas cifras históricas de las nuevas ejecuciones `32³`.

## 6. Un resultado negativo de valor: perder el ángulo no implica perder el anillo

**[F]** Para el flujo exacto (O56.3), la aplicación `F_t` es un difeomorfismo de determinante uno; por tanto una superficie toroidal material inicialmente embebida sigue siendo toroidal topológicamente para todo `t` finito. Sin embargo, las tangentes de la consulta pueden dejar de ser perpendiculares.

Esto refuta la implicación **universal** `perder perpendicularidad local ⇒ deshacerse físicamente el toroide`. Una identidad relacional que exija esa perpendicularidad puede dejar de ser válida *bajo su contrato*, mientras la forma topológica y la solución PDE permanecen regulares. **La ontología del cierre propio y la persistencia de la forma física necesitan observables separados.**

Igualmente, en la cizalla exacta `(ω·∇)u=0`: puede perderse la perpendicularidad **sin** estiramiento de vorticidad. Para acceder a una afirmación de regularidad NS se requeriría una desigualdad adicional que controle el término de estiramiento; la compensación de direcciones no lo hace automáticamente.

## 7. Conexión con el tiempo relacional y Yang–Mills

El tiempo de O45 compara **tres ritmos** (flujo, referencia, partícula) con dos diferencias independientes cuando sus fases están definidas. O56 no añade un reloj ficticio a las cizallas: en estos flujos exactos no se presupone retorno de una partícula. El reloj por fases del anillo O53 permanece como observable distinto y todavía debe acoplarse explícitamente al comparador direccional.

En Yang–Mills, el problema análogo del programa no consiste en transportar el mismo `K` geométrico; consiste en determinar si una diferencia relacional gauge-invariante que el comparador anterior omitía puede producir una **cota dinámica uniforme**. Ni la perpendicularidad de O56 ni el refinamiento `10→20` implican coercividad ni mass gap. Hay un paralelismo metodológico entre suficiencia, novedad y falta de una cota dinámica, no una igualdad de mecanismos.

## 8. Estado, siguiente obligación y falsadores

**Acreditado [T]:** identidad material (O56.1–2); soluciones exactas de cizalla; conservación de volumen; mismo `E,Z,q,N` con respuesta angular diferente para una consulta fija; transporte aritmético `H₁₀⊂H₂₀` bajo el contrato declarado.  
**Acreditado [E]:** simulación `32³` del anillo con cizallas X/Y, reproducción del código de O55 en un caso controlado, y **21 controles** del ensayo analítico/documental.  
**Abierto [A]:** ley física de actualización del normalizador; dinámica autónoma de `K`; condición suficiente de persistencia de identidad física; control de estiramiento de vorticidad; independencia de escala y resolución; vínculo de una firma direccional con el espectro gauge.

**Experimento O57 propuesto:** fijar previamente el comparador `C=(q, fases físicas disponibles, escala, E, Z, K, tasas longitudinales)` y obtener dos campos con igual `C` inicial pero diferente futuro; si eso ocurre, registrar cuál dato nuevo se hace necesario. Antes de esa comparación, medir la evolución en mallas superiores y con marcas distribuidas por distintas posiciones del anillo, para separar invariancia física y dependencia del observador. No introducir una ley restauradora ajustada después de conocer las curvas.

**Lectura síntesis:** el múltiplo conserva una referencia aritmética; para renovar la identidad respecto de una pregunta dinámica debe además incorporar una relación que pueda influir en su futuro. En la perpendicularidad material esa relación mínima inicial es la **deformación cruzada**. Todavía no sabemos si existe una regla universal de renovación que seleccione y sostenga esa relación en Navier–Stokes.

## 9. Reproducción

1. `python codigo/ensayo_o56.py` — genera 127 tiempos por cuatro soluciones exactas, 21 controles, `resultados/serie_exacta.csv`, gráficos y `resultados/resumen.json`.
2. `python codigo/simulacion_toroide_O56.py` — reproduce 3 escenarios del anillo NS en la malla `32³`, guarda la evolución y resumen en `resultados/`. Requiere `numpy`; el primer script admite `matplotlib` para gráficos (sin él, los controles siguen funcionando).
3. `python verificar_paquete.py` — verifica huellas de todos los archivos registrados en `MANIFEST_SHA256.json`.

Se conserva el `O55_simulacion_original.py` y el CSV histórico en `fuentes/` para auditoría, sin modificar sus valores originales. No se ha modificado la Imagen Total v3.8.1 ni ningún repositorio remoto.
