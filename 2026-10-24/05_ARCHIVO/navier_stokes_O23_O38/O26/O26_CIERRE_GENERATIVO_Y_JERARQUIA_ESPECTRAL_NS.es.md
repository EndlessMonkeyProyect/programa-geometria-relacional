# O26 — La interfaz del espejo y la jerarquía espectral de Navier–Stokes

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 19 de octubre de 2026  
**Estado:** formalización sectorial nueva y complemento crítico de O25, sin modificación del núcleo ni de la Imagen Total.  
**Etiquetas:** [O] interpretación ontológica; [D] definición/hipótesis formal; [T] resultado matemático demostrado bajo premisas; [E] prueba reproducible; [F] contraejemplo/no-go; [H] hipótesis pendiente; [A] abierto.

## 0. El corte: qué pregunta realmente se investigó

O25 demostró que la escala del espejo `ell_omega=sqrt(A/B)` es un observable del flujo y que su movimiento es calculable desde las ecuaciones de Navier–Stokes para soluciones suaves. O26 invierte la pregunta: **si el radio y las cantidades que lo definen están fijados, ¿queda su movimiento determinado por esa sola interfaz?**

**Resultado [T/F]: no.** Existen dos soluciones suaves y exactas de Navier–Stokes tridimensional, no forzadas, con el mismo instante inicial de energía cinética, enstrofía, palinstrofía y radio `ell_omega`, pero con valores distintos de `dot ell_omega` y `dot n_omega`.

**Resultado [T]:** dentro de la subfamilia de flujos de cizalla, el avance de la profundidad espectral está gobernado exactamente por la varianza del cuadrado del número de onda y es no positivo por efecto de la viscosidad. No se extiende la desigualdad a toda NS 3D.

**Resultado [T/F] general:** ninguna lista fija de momentos espectrales consecutivos hasta orden finito, incluso añadiendo la energía cinética, determina universalmente la derivada del momento más alto sobre la clase completa de flujos de cizalla de espectro finito arbitrario. Se necesita más información o restringir la familia admisible. Esta es una forma clásica de jerarquía de momentos, no un descubrimiento de un teorema físico nuevo.

## 1. Narrativa → ontología → lenguaje → matemática

El **espejo** O25 es una representación por un radio; la **imagen** es la solución expresada en ese marco. Su **foco** no es un punto material: en esta realización es la condición que define el radio espectral. Una **interfaz** `I=(H,A,B)` conserva respuestas concretas: energía, enstrofía y palinstrofía. Dos flujos con la misma interfaz pertenecen a la misma clase de indistinguibilidad para esas preguntas.

**La diferencia pendiente** emerge si una pregunta posterior como `dot n` separa dos realizaciones indistinguibles para `I`. La **relación común** es la igualdad de las respuestas presentes, no la identidad física de los dos campos. El **cierre propio** necesitaría que la interfaz sea suficiente también para todas las continuaciones autorizadas. La **normalización** `ell=sqrt(A/B)` es idempotente como elección de referente, pero esto por sí solo no da un cierre composicional o dinámico universal.

Esta lectura reutiliza Núcleo Generativo Canónico; E9; MF-86 (suficiencia, idempotencia, composicionalidad); CR-5 (una familia de reflexiones no selecciona una sola salida por simetría); MF-43 (orden, ritmo y tiempo distintos); `ritmo_radio_relatividad_relacional_v0_1.md` (producto espectral `R_i omega_i=v_*` condicional); O23 (interfaz suficiente según consultas); O24-R (relojes); O25 (espejo endógeno). No atribuye a esos documentos una derivación del teorema de regularidad NS.

**Precisión de geometría:** el reflejo euclídeo de O19–O23 y la dilatación del marco de O25 son operaciones distintas. Esta rama no afirma que sean un mismo operador físico. **Precisión de velocidad:** el parámetro de propagación `v_*` en el cambio de reloj no es un límite demostrado para la velocidad incompresible `u`, ni se identifica aquí con `c` luz o con `c_DRD` de la memoria elástica.

## 2. Firma observable y balance general [D/T]

En el toro físico fijo `T³=(R/2πZ)³`, sea `u(x,t)` una solución suficientemente suave de Navier–Stokes incompresible, con viscosidad `nu>0`, y `omega=curl u`. Usar integral normalizada por el volumen del toro (las razones no cambian si se usa la integral sin normalizar):

\[
 A=\langle|\omega|^2\rangle,\quad
 B=\langle|\nabla\omega|^2\rangle,\quad
 C=\langle|\Delta\omega|^2\rangle.
\]

Con `A,B>0`, definir `ell_omega²=A/B` y, para una referencia externa **fija** `L>0`, `n_omega=log₂(L/ell_omega)`. La identidad exacta de O25 es

\[
\boxed{\dot n_\omega=\frac{1}{2\ln 2}\left(\frac{\dot B}{B}-\frac{\dot A}{A}\right).}
\]

Para forzamiento `f`, sea `g=curl f`, `S=(omega·nabla)u`. Separar los aportes no viscosos así:

\[
 Z_A=2\langle\omega\cdot S\rangle+2\langle\omega\cdot g\rangle,
\]

\[
\begin{aligned}
 Z_B={}&-2\langle(\partial_i\omega_a)(\partial_i u_b)(\partial_b\omega_a)\rangle
 +2\langle\nabla\omega:\nabla S\rangle\\
 &+2\langle\nabla\omega:\nabla g\rangle.
\end{aligned}
\]

Entonces `dot A=-2 nu B+Z_A`, `dot B=-2 nu C+Z_B`; de donde

\[
\boxed{
\dot n_\omega= -\frac{\nu}{\ln 2}\left(\frac CB-\frac BA\right)
+\frac{1}{2\ln 2}\left(\frac{Z_B}{B}-\frac{Z_A}{A}\right).
}\tag{O26.1}
\]

Por Cauchy–Schwarz `B²≤AC`, de modo que el **aporte explícito de la viscosidad es siempre no positivo** a `dot n`. El resto (estiramiento, advección de gradientes, forzamiento) no tiene signo general fijado por estas identidades. En un flujo de cizalla de la sección siguiente `Z_A=Z_B=0`; la expresión entonces se simplifica. Este balance no controla globalmente `A,B,C` ni descarta blowup en 3D.

Si `L=L(t)`, añadir `dot L/(L ln 2)` a (O26.1). Tal término es un cambio del referente, no una producción viscosa ni una transferencia demostrada del fluido.

## 3. Subfamilia exacta: remolinos modales de cizalla [D/T]

Tomar velocidad tridimensional no forzada y periódica

\[
\boxed{u(x,t)=\left(\sum_{k\in K} a_k e^{-\nu k^2t}\sin(kx_2),0,0\right),}
\]

para cualquier subconjunto finito `K` de enteros positivos y amplitudes reales `a_k`. La divergencia es cero, `(u·nabla)u=u_1 partial_1u=0`, `partial_tu=nu Delta u` y la presión es constante. **Son soluciones exactas de Navier–Stokes 3D**, aunque su dinámica efectiva sea una cizalla lineal (no producen estiramiento de vorticidad).

Sea `w_k(t)=(k a_k)^2 exp(-2 nu k² t)/2>0` para amplitudes no nulas. Con integral por unidad de volumen y ortogonalidad de los cosenos,

\[
M_j(t)=\sum_{k\in K}k^{2j}w_k(t),\qquad
H=M_{-1}=\langle|u|^2\rangle,\ A=M_0,\ B=M_1,\ C=M_2.
\]

La jerarquía se demuestra diferenciando **exactamente** cada modo:

\[
\boxed{\dot M_j=-2\nu M_{j+1}\quad(j=-1,0,1,2,\dots).}\tag{O26.2}
\]

Para `m=B/A`, `ell_omega=m^{-1/2}` y `n_omega=log₂(L sqrt m)`:

\[
\boxed{\dot n_\omega=-\frac\nu{\ln2}\left(\frac CB-\frac BA\right)
=-\frac\nu{\ln2}\frac{\operatorname{Var}_{w}(k^2)}{\mathbb E_w(k^2)}\le0.}\tag{O26.3}
\]

Aquí `E_w` usa los pesos normalizados `w_k/A`. La desigualdad es estricta si hay al menos dos números de onda distintos con peso positivo; es igualdad para un único `k` (aunque la energía siga disipándose).

La identidad `AC-B²=Σ_{i<j} w_iw_j(k_i²-k_j²)²≥0` deja la desigualdad algebraicamente acreditada sin aproximaciones.

## 4. Contraejemplo adversarial con energía y radio iguales [F/T]

Usamos `K={1,2,3,4}`. Los pesos iniciales son:

\[
(w_1,w_2,w_3,w_4)^{(I)}=(1,1,1,1),
\]

\[
(w_1,w_2,w_3,w_4)^{(II)}=\frac1{162}(155,218,81,194).
\]

Cada perfil define amplitudes `a_k=sqrt(2 w_k)/k`; por ello son campos suaves legítimos. En `t=0`:

| Observable normalizado | Flujo I | Flujo II |
|---|---:|---:|
| `H=∫|u|²` | `205/144` | `205/144` |
| `A=∫|ω|²` | `4` | `4` |
| `B=∫|∇ω|²` | `30` | `30` |
| `ell_omega²=A/B` | `2/15` | `2/15` |
| `C=∫|Δω|²` | `354` | `3326/9` |
| `dot n * ln2 /nu` | `-43/10` | `-1301/270` |

**Teorema [F]:** no existe una función determinista universal `F(H,A,B)` que proporcione `dot n_omega` en toda esta familia. Si existiese, daría el mismo resultado para ambos estados, contradiciendo las filas finales.

No se ha demostrado que una física nueva surja de esta diferencia: la predicción de evolución ya está contenida en Navier–Stokes. Lo que sí queda invalidado es inferir la evolución únicamente de tres momentos sin una hipótesis adicional sobre el espectro.

## 5. Teorema general de jerarquía: ninguna firma finita de momentos cierra universalmente [T/F]

Fijado cualquier entero `r≥0`, definir la firma `I_r=(M_{-1}, M_0,..., M_r)`. Elegimos `r+3` números de onda positivos y distintos `k_i`, con `x_i=k_i²`; llamemos `N=r+3`. Construimos el vector

\[
\boxed{h_i=\frac{x_i}{\prod_{j\ne i}(x_i-x_j)}.}\tag{O26.4}
\]

La identidad de interpolación de Lagrange da, para `q=-1,0,...,r`,

\[
\sum_i h_i x_i^q=0,
\]

pero para el siguiente momento:

\[
\sum_i h_i x_i^{r+1}=1.
\]

Comenzar con pesos estrictamente positivos `w_i=1` y tomar `w'_i=1+epsilon h_i`, con `epsilon>0` suficientemente pequeño para preservar positividad. Ambas familias tienen exactamente la misma firma `I_r`, pero

\[
 M_{r+1}(w')-M_{r+1}(w)=\epsilon\ne0.
\]

Como `dot M_r=-2 nu M_{r+1}`, sus derivadas no coinciden. Por tanto:

\[
\boxed{\text{No hay cierre dinámico universal autónomo para }I_r
\text{ en toda la familia de cizallas de espectro arbitrario.}}
\]

**Alcance:** el teorema excluye el cierre por una lista prefijada de estos momentos. No excluye otras representaciones finitas ni algoritmos adaptativos, ni una descripción completa de los coeficientes de Fourier cuando el soporte se restringe a un conjunto fijo finito. De hecho, dentro de un soporte conocido de exactamente dos modos, `A` y `B` pueden recuperar los pesos y sí cerrar la evolución de esa familia específica.

## 6. Traducción al lenguaje ya acreditado [O/D/T]

| Término | Definición operativa para O26 | No implica |
|---|---|---|
| Unidad/cierre propio | una clase de flujos indistinguibles para un conjunto declarado de preguntas y continuaciones | que el grupo sea estable para preguntas futuras arbitrarias |
| Imagen/foco | campo reescalado y condición `B_y/A_y=1` de O25 | centro material privilegiado |
| Referente | escala `ell_omega` y referencia exterior `L` | un espacio absoluto |
| Reflexión | cambio de marco que conserva la solución; una operación geométrica diferente de reflexión especular tetraédrica | que todo reflejo físico o discreto sea esa dilatación |
| Relaciones comunes | respuestas compartidas de `H,A,B` | igualdad de todos los campos o genealogías |
| Diferencia pendiente / residuo | `C` separa los dos futuros a pesar de coincidir `H,A,B` | probabilidad, incertidumbre cuántica o azar |
| Normalización | elegir `ell_omega` hace `B_y/A_y=1` | estabilidad o disipación adicional |
| Profundidad | `n_omega=log₂(L/ell_omega)` | tiempo físico o fase acumulada |
| Ritmo | `v_*/ell_omega` de la familia relacional; `nu/ell²` de viscosidad | igualdad entre propagación causal y flujo incompresible |
| Economía mínima | conservar una firma suficiente **para consultas explícitas** | interfaz finita económica para todos los futuros |

El criterio de E9 (`d` factoriza por la firma si y solo si no separa sus fibras) se aplica aquí sin cambios: el dato `C` no factoriza por `(H,A,B)` en la familia general, pues las dos realizaciones anteriores tienen misma firma y distinto `C`. Para la consulta `dot n`, `C` sí es un discriminante suficiente **dentro del submodelo de cizalla y a un instante**. En el flujo NS general faltan además los términos no viscosos `Z_A,Z_B` de (O26.1). Un dato de la primera derivada no garantiza suficiencia para todas las derivadas futuras.

MF-86 exige composicionalidad: sustituir una estructura por su interfaz debe preservar las respuestas de las continuaciones admitidas. Las dos cizallas anteriores son un testigo de que la interfaz `(H,A,B)` no satisface ese contrato si se permite consultar el siguiente movimiento del radio.

## 7. ROSI: estados, falsadores y próximos cruces [F/A]

- `[RESOLVED | T]` ecuación de balance (O26.1) para soluciones suaves, descomposición viscosa no positiva de `dot n`, jerarquía exacta en cizallas, contraejemplo de dos estados y no-go de firma finita de momentos para espectros arbitrarios.
- `[RESOLVED | F]` mismo estado de observables de bajo orden **no** obliga mismo futuro de espejo. Respuesta negativa acreditada, no afirmación física nueva.
- `[OPEN | H]` derivación de una restricción espectral adicional **desde el núcleo relacional**, que no sea simplemente la reformulación de NS; si se obtiene, exige declaración previa de clase de flujos, fuerza y observables.
- `[OPEN | H]` correspondencia de `v_*` con velocidad luminosa, o relación directa entre reflexión geométrica tetraédrica y movimiento de una escala espectral.
- `[OPEN | NS]` regularidad global 3D. Las identidades implican ninguna cota a priori suficiente de las cantidades de alto orden.
- `[NO-GO]` afirmar `dot n_omega ≤0` para todo NS 3D usando solo la parte viscosa; extrapolar una afirmación válida en flujos de cizalla sin estiramiento al régimen general; reemplazar el tensor de estiramiento por un bit o un radio; identificar el operador de cierre conceptual con solución polinómica universal.

### Falsadores constructivos propuestos para el siguiente módulo

1. Elegir **antes del cálculo** una firma `I` generada por la gramática del programa (no por ver espectros resueltos). Examinar si `dot n` factoriza por `I` en una clase amplia de DNS 3D.
2. Control negativo exacto: las dos cizallas de la sección 4. Toda ley que diga `dot n=F(H,A,B)` debe fallar.
3. Test adversarial: deformación del flujo con igual firma pero distribución espectral distinta, y comparar horizonte de reescala.
4. Si se invoca una relación nueva (ej., restricción sobre espectro permitido desde cierre tetraédrico), precisar la clase que prohíbe y una observación que la falsaría. No ajustar el veto después.
5. Confrontar con O18: una tasa `nu/(v_*ell)` variable por cambio de unidades no es una disipación efectiva `|k|^{5/2}`; derivar un nuevo operador es una hipótesis distinta.

## 8. Reproducción [E]

`laboratorio_o26.py` calcula con `fractions.Fraction` todos los pesos y momentos. `test_o26.py` demuestra los invariantes de los dos perfiles, comprueba aritméticamente el lema general para rangos `r=0,..,6`, verifica la ley de derivadas para momentos negativos y positivos, la desigualdad de varianza y la aproximación numérica del movimiento del espejo. `RESULTADOS_O26.json` registra las salidas; `PRUEBAS_O26.txt` conserva la ejecución; `SHA256SUMS.txt` contiene los hashes. El ZIP original O25 se conserva como antecedente **sin reescribirlo**.

Los tests no sustituyen las pruebas universales de esta nota ni una DNS de turbulencia tridimensional. Las ecuaciones de momentos y la no-clausura de `I_r` son teoremas bajo las hipótesis expuestas, ampliamente relacionados con problemas clásicos de cierre de jerarquías.

**Conclusión:** La evolución exacta del espejo es reconstructible desde el campo Navier–Stokes completo. En cambio, un conjunto fijo de observables reducidos no conserva necesariamente la información suficiente para ese futuro. Esta diferencia entre descripción actual y suficiencia generativa ya estaba en la ontología del programa; O26 aporta un testigo matemático reproducible, no una ley física adicional.
