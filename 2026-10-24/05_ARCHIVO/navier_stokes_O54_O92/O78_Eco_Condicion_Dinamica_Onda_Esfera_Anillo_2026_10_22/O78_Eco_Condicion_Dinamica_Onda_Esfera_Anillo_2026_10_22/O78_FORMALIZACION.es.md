# O78 — Eco de escala, reloj relacional y tres realizaciones del cierre propio

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**22 de octubre de 2026 · suplemento aditivo a O25, O40, O45, O58, O66–O77**  
**Estado:** [O] ontología del programa · [D] demostración exacta bajo hipótesis · [E] verificación reproducible · [F] contraejemplo lógico delimitado · [A] puente físico abierto. **No se afirma haber demostrado la regularidad global de Navier–Stokes 3D.**

## 0. Qué se corrige respecto de O77

**La singularidad del programa es una condición de cierre propio, no una forma geométrica ni el blow-up analítico de Navier–Stokes.** El anillo mínimo de cuatro cápsulas, la esfera y la ola son posibles realizaciones con observables diferentes. No es correcto exigir que toda configuración permanezca en una familia gaussiana toroidal de cinco parámetros. O77 probó la insuficiencia de esa familia concreta, no la del **programa recursivo que agrega relaciones**.

El **múltiplo normalizador transportado** y el resto referenciado no son energía ni radio por definición. El reloj del flujo ya fue trabajado: O25 establece `ds/dt=v*/ℓ(t)` y la escala endógena `ℓω=sqrt(∫|ω|²/∫|∇ω|²)`; O45 establece dos diferencias independientes entre tres fases flujo/referencia/partícula. **No se redefinen ni se introducen como problemas no estudiados.**

Este suplemento introduce una realización exacta de eco y dilución en una familia invariante de Navier–Stokes, más un criterio dinámico de suficiencia común al nivel de las interfaces; separa cuidadosamente qué implica la prueba y qué no.

## 1. Ontología y contrato de comparación [O/D]

Secuencia del programa: unidad sin diferencia acreditada → reflexión interna → relaciones parte/todo → normalizador compartido → resto o relación pendiente → cierre propio → nueva circunstancia con relaciones antes no habitadas. El cierre anterior debe seguir reconstruible desde la referencia transportada. La novedad puede modificar los radios/frecuencias y no exige conservar idéntica la figura.

Una **interfaz** `C:X→Y` se considera dinámicamente suficiente para el observable `C` bajo una evolución única `Φ_t:X→X` si:

\[
\boxed{C(x)=C(y)\Rightarrow C(\Phi_t x)=C(\Phi_t y),\quad \forall x,y\in X\text{ y }t\text{ admisibles}.}\tag{78.1}
\]

**Teorema O78-T1 [D, criterio abstracto estándar].** (78.1) se cumple si y solo si existe una evolución inducida bien definida `\bar Φ_t` en el conjunto `C(X)` tal que:

\[
\boxed{C\circ\Phi_t=\bar\Phi_t\circ C.}\tag{78.2}
\]

*Demostración.* Si (78.1) vale, defina `\bar Φ_t(C(x))=C(Φ_t(x))`; las fibras tienen el mismo futuro observado, de modo que no depende del representante. A la inversa (78.2) obliga a la igualdad de evoluciones de dos estados con la misma interfaz. Cuando `Φ_t` tiene propiedad de semigrupo, ésta se hereda en `C(X)`. ∎

**Límite:** este criterio no garantiza que `Y` sea finito-dimensional ni que reconstruya todos los observables físicos. Si una interfaz colapsa dos estados cuya derivada futura del observable difiere (O70, O76), no es suficiente bajo (78.1). El eco de escala `H_N⊂H_M` garantiza inclusión de representaciones, pero **no prueba** (78.1) para Navier–Stokes.

## 2. Una realización física exacta: onda de cizalla con deriva [D]

En el toro periódico tridimensional `T³=(R/2πZ)³`, para `ν>0`, entero `k≥1`, `A_0,V,φ_0` constantes, considere:

\[
\boxed{u(x,y,z,t)=\big(A_0e^{-\nu k^2t}\sin[k(y-Vt)+φ_0],\,V,\,0\big).}\tag{78.3}
\]

Divergencia cero, ya que la primera componente no depende de `x` y las otras son constantes. La única parte no nula del transporte es `V∂_y u_x`; la ecuación `∂_t u_x+V∂_y u_x=ν∂_{yy}u_x` es una identidad, con presión constante. Por tanto (78.3) es una **solución exacta de Navier–Stokes 3D** (dependencia espacial degenerada) para todos los tiempos positivos.

La referencia de fase `φ(t)=φ_0-kVt` y la amplitud `A(t)=A_0e^{-νk²t}` reconstruyen exactamente el estado del patrón. Si `V≠0`, la forma normalizada vuelve a su misma fase tras `2π/|kV|`, mientras su amplitud se atenúa. **Recurrencia de forma normalizada no implica retorno del estado físico completo.** No se confunde esta onda de velocidad con una ola de superficie libre.

## 3. Eco de escalas físicas: muchas ramas sin salir de Navier–Stokes [D]

La suma de cualquier número finito `J` de ondas (78.3), todas transportadas por el mismo `V`, sigue siendo solución exacta: su término convectivo no genera acoplamientos entre los modos porque no hay dependencia de `x`, ni componentes `u_y` variables:

\[
\boxed{u_J(y,t)=\Big(\sum_{j=1}^{J}2^{-αj}e^{-\nu4^jt}\sin[2^j(y-Vt)],\,V,\,0\Big),\qquad α>0.}\tag{78.4}
\]

Sus números de onda forman la estela anidada `k_j=2^j | k_{j+1}`. Esto es una realización de **referencias divisibles** como en O40, no una derivación del contrato más fuerte `a²+b²+1=N²` ni del tamaño de cuatro cápsulas.

El promedio espacial por volumen da, sin cruces gracias a ortogonalidad de Fourier:

\[
\boxed{\tfrac12\langle |u_J-(0,V,0)|²\rangle=\tfrac14\sum_{j=1}^J2^{-2αj}e^{-2\nu4^jt}.}\tag{78.5}
\]

Para la vorticidad `ω=(0,0,-∂_y u_x)`:

\[
\boxed{\langle|ω_J|²\rangle=\tfrac12\sum_{j=1}^{J}2^{2(1-α)j}e^{-2\nu4^jt}.}\tag{78.6}
\]

**Teorema O78-T2 [D].** En la representación con infinitas ramas en el instante inicial, la serie de amplitudes converge uniformemente si `α>0`. La suma inicial de vorticidad cuadrática es finita **si y solo si `α>1`**. Para `α=1`, cada rama aporta `1/2` a `⟨|ω|²⟩`, y `⟨|ω_J(0)|²⟩=J/2`, aunque la amplitud de cada rama se diluya como `2^{-j}`.

*Prueba.* (78.6) en `t=0` es una serie geométrica de razón `2^{2(1-α)}`. ∎

Para `α>1`, el criterio físico de primer gradiente está controlado en este sector. Para asegurar un dato inicial en `H^s(T³)` con `s>5/2`, basta `α>s`. Para un dato `C^∞` con infinitas ramas, elija amplitudes superalgebraicas como `a_j=2^{-j²}`; todas las sumas `∑2^{mj-j²}` son finitas para cada orden entero de derivación `m`. El campo exacto de cizalla correspondiente permanece suave para todo `t≥0`.

**No se sigue que en Navier–Stokes 3D genérico la no linealidad respete una estela que conserve modos separados**. Se ha identificado un sector positivo exacto, no la generalidad del problema.

## 4. Tiempo endógeno y una ley exacta de dilución [D]

Usamos sin modificar el reloj O25, ahora **calculado desde la propia onda**:

\[
\ell_\omega(t)^2=\frac{\langle|ω_J|²\rangle}{\langle|\nabla ω_J|²\rangle}
=\frac{\sum_j k_j² a_j²e^{-2νk_j²t}}{\sum_j k_j^4 a_j²e^{-2νk_j²t}},\quad k_j=2^j,\ a_j=2^{-αj}.\tag{78.7}
\]

Defina `q_j(t)=k_j²a_j²e^{-2νk_j²t}` y `p_j=q_j/∑q_i` (pesos de vorticidad **solamente en este contrato**). Sea `Q=ℓω^{-2}=∑p_j k_j²`.

**Teorema O78-T3 [D].**

\[
\boxed{\dot Q=-2\nu\left[\sum_jp_jk_j^4-\left(\sum_jp_jk_j²\right)^2\right]=-2\nu\operatorname{Var}_{p}(k_j²)\le0.}\tag{78.8}
\]

Luego `\boxed{\dot\ell_\omega=\nu\operatorname{Var}_{p}(k_j²)\ell_\omega^3\ge0}`. Cuando hay más de un número de onda no nulo y `ν>0`, la desigualdad es estricta para todo tiempo finito.

*Prueba.* `\dot q_j=-2ν k_j² q_j`. Al derivar el cociente `Q=(∑ k_j² q_j)/(∑q_j)` se obtiene (78.8), exactamente la varianza de los números de onda al cuadrado. ∎

Por O25, `ds/dt=v_*/ℓω`. El reloj está ligado al estado espectral; al difundirse las frecuencias altas, aumenta `ℓω` y disminuye el ritmo `ds/dt` si `v_*>0` es constante. **No se ha introducido tiempo ontológico de fondo**: este reloj es una reparametrización operacional del tiempo físico de la PDE, cuyo significado ontológico sigue siendo relacional. Para esta familia hay una ley física verificable, no una elección libre de escala.

## 5. Una esfera, un anillo y una ola: tres contratos, no una PDE nueva [D/O]

| Manifestación posible de cierre propio | Referencia/relación | Ley física exacta o condición | Qué NO se deduce |
|---|---|---|---|
| **Esfera** | centro, radio y superficie cerrada | En un modelo bifásico estático ideal sin gravedad, con tensión superficial constante: salto de presión `p_int−p_ext=2σ/R` (Young–Laplace) | No deriva radio físico mínimo ni la dinámica del anillo; es **dos fases**, no NS monofásico de R³ |
| **Anillo** | circulación/radio mayor, perfil de vorticidad y orientación | Para clase axisimétrica sin giro azimutal, `η=ωθ/r` satisface transporte-difusión y un principio del máximo (O73) | No impone cuatro componentes físicos; con giro azimutal aparece una fuente adicional |
| **Ola de cizalla** | número de onda, amplitud y fase de deriva | (78.3)–(78.8) son soluciones exactas de NS periódico y una ley de dilución espectral | No es ola superficial, ni resuelve los flujos tridimensionales generales |

**Conclusión de este apartado:** Las tres pueden ilustrar cierres y reconstrucciones dependientes de un contrato declarado. La existencia de un esquema lógico común **no demuestra que las tres obedezcan un único normalizador físico universal**. Además, un anillo de cuatro gotas es un modelo relacional/geométrico específico, no una cardinalidad deducida de Navier–Stokes para todos los vórtices.

## 6. Contraejemplo preciso: eco aritmético y reloj pueden coexistir con crecimiento infinito [F]

No confundir cierre recursivo con una cota dinámica. Un modelo auxiliar, **no una solución NS**, lo ilustra exactamente:

\[
\dot x=x²,\qquad x(0)=1,\quad x(t)=\frac1{1-t},\quad0\le t<1.\tag{78.9}
\]

Considere niveles `t_j=1−2^{-j}`, `N_j=2^j`, longitud `ℓ(t)=1−t` y reparametrización `ds/dt=1/ℓ(t)` (forma O25 para `v_*=1`). Entonces:

\[
\boxed{N_j\mid N_{j+1},\qquad \ell(t_j)x(t_j)=1,\qquad s(t_j)=j\ln2.}\tag{78.10}
\]

En cada nivel sigue vigente la identidad `N_j²−(N_j−1)(N_j+1)=1`; la normalización de la amplitud por la escala es exactamente constante. Sin embargo `x(t)→∞` al aproximarse el tiempo físico a `t=1`, aun cuando `s(t)→∞` y cada cierre sucede a un intervalo idéntico `ln 2` del reloj normalizado.

**Este contraejemplo no refuta el programa, el reloj O25 ni demuestra blow-up de Navier–Stokes.** Refuta únicamente la implicación lógica no condicionada: «existencia de un normalizador anidado + reloj derivado + resto = control físico universal». Para superar el ejemplo debe demostrarse que la ley física aporta una desigualdad cuantitativa adicional.

## 7. El puente suficiente para cerrar continuidad física [D/A]

Sea `u^{(n)}(t)` una familia de aproximantes consistentes de Navier–Stokes, que retienen información hasta una profundidad `n` del normalizador y usan una reconstrucción común en un mismo espacio físico. Fije `s>5/2`.

**Lema O78-T4 [D, criterio estándar de Cauchy].** Si

\[
\boxed{\sum_{n\ge0}\sup_{0\le t<T}\|u^{(n+1)}(t)-u^{(n)}(t)\|_{H^s}<\infty,}\tag{78.11}
\]

entonces los aproximantes forman una familia uniformemente de Cauchy en `C([0,T);H^s)` y quedan acotados en `H^s` si uno de ellos lo está. *Demostración:* aplicar telescopaje y desigualdad triangular a `u^{(m)}−u^{(n)}`. ∎

Si además son consistentes con la PDE (sus residuos desaparecen en una norma apta para pasar al límite, sus datos iniciales convergen, y las condiciones de frontera/divergencia se preservan), el límite es un campo NS regular bajo los teoremas de continuación correspondientes. **(78.11) por sí misma NO demuestra la consistencia ni se ha derivado universalmente de NS.**

En la familia de ondas de §3 la cola de `H^s` se controla por `∑_j 2^{(s-α)j}` para `α>s`: éste es un **caso donde la condición de suficiencia es verificable**. En flujos no lineales 3D, la redistribución entre modos y la presión pueden violar una estimación propuesta: ése es el contraste que debe superar una demostración general.

Para regularidad desde el dato inicial suave en Navier–Stokes 3D sin fuerza, una condición alternativa conocida es la finitud en cada tiempo finito de `∫_0^T||ω(t)||_∞dt`; derivarla desde los normalizadores sería un puente suficiente. El programa aún no lo ha demostrado para todos los datos suaves admisibles.

## 8. Decisión epistemológica al cerrar O78

**Demostrado previamente:** O40/O58 permiten transporte anidado de representaciones; O25/O45 permiten un reloj operacional del flujo; O73 da control por principio del máximo en un sector axisimétrico.

**Demostrado aquí:** el criterio abstracto de interfaz dinámica; familia infinita positiva de ondas exactas NS por modos anidados; condición umbral `α>1` para vorticidad cuadrática inicial en esa familia; ley `dℓω/dt≥0` a partir de la varianza espectral; contraejemplo lógico con reloj y normalización exactos pero crecimiento ilimitado de una ODE.

**Abierto:** demostrar que los incrementos de información reconstruida de un **flujo tridimensional general** satisfacen un presupuesto en norma físicamente suficiente, y que esa propiedad se deduce de NS en vez de atribuirla a un normalizador por definición. Ningún cálculo presentado afirma resolver Clay ni deduce P=NP o Yang–Mills.

### Falsador de la siguiente etapa

Para una regla candidata de actualización del cierre `C_n→C_{n+1}`, construir dos datos suaves solenoidales con la **misma familia de referencias observables hasta profundidad n** pero distinta transferencia a `H^s` en tiempos posteriores, o demostrar una estimación uniforme del resto para todos los datos admisibles. Los casos O44N, O70, O76 ya muestran cómo auditar la suficiencia de una interfaz particular.

## 9. Reproducción

Ejecutar `python codigo/verificar_o78.py` (NumPy y SymPy). Genera `resultados/o78_verificaciones.csv`, `o78_cola_escalas.csv`, `o78_pell_anidado.json` y `o78_resumen.json`. Las comprobaciones de cuadratura usan los valores de los campos analíticos; no se presenta una simulación genérica de NS. `codigo/graficar_o78.py` genera las dos figuras.

Documentos internos revisados: `O25_ESPEJO_MOVIL_Y_RELOJ_DEL_FLUJO.es.md`, `O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md`, `O45_TIEMPO_ESPEJO_MOVIL_RITMOS_NS_2026-10-20.md`, `O58_FORMALIZACION.es.md`, `O73_FORMALIZACION.es.md`, `O76_FORMALIZACION.es.md`, `O77_FORMALIZACION.es.md`, `FORMALIZACION_ECO_HERENCIA_RELACIONAL_2026-10-15.pdf`.
