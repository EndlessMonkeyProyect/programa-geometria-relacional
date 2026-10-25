# O79 — Eco de escala, relación de fase y generación de novedad en Navier–Stokes

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**22 de octubre de 2026** · suplemento posterior a O78  
**Estatus:** [O] ontología, [N] narrativa, [D] identidad y proposición demostradas, [E] comprobación Fourier, [F] falsador de suficiencia, [A] conexión física abierta. **No demuestra regularidad global de NS tridimensional.**

## 0. Prioridad del programa [O/N]

La singularidad ontológica se entiende como cierre propio de una relación y **no** como una geometría obligatoria ni como una singularidad analítica (blow-up). Anillo, esfera y ola son posibles manifestaciones con interfaces físicas distintas. Lo ya acreditado por O40/O58 es la **transportabilidad aritmética** de una referencia normalizada y la posibilidad de un eco anidado de múltiplos; O25/O45 ya construyeron un reloj a partir de las escalas y ritmos del flujo. No debemos redefinir estas piezas ni confundir la energía con la fuente ontológica de la unidad.

O78 mostró que, en una clase exacta de ondas de cizalla sin acoplamiento entre ondas, amplitudes dyádicas `2^{-αj}` producen suma inicial de vorticidad cuadrática finita si y solo si `α>1`. **Pregunta O79:** ¿qué determina la evolución cuando dos relaciones sí interactúan y generan una tercera? ¿Un eco de múltiplos y las magnitudes normalizadas contienen toda la información pertinente?

## 1. Navier–Stokes en Fourier, sin imponer enlaces [D]

En el toro periódico `T³=(R/2πZ)³`, con `ν>0`, para un campo real, suave e incompresible `u`,

\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\qquad\nabla\cdot u=0.\tag{79.1}
\]

La proyección de Leray `P_m=I-mmᵀ/|m|²`, para `m≠0`, da exactamente

\[
\boxed{\partial_t\widehat u_m=-\nu|m|^2\widehat u_m - iP_m\sum_{k+l=m}(\widehat u_k\cdot l)\widehat u_l.}\tag{79.2}
\]

La *información de la siguiente transformación* incluye productos de coeficientes complejos: magnitud y fase de las relaciones que satisfacen `k+l=m`. La existencia de una subred aditiva de etiquetas no asigna esas amplitudes ni sus fases.

## 2. Proposición O79-T1: mismos módulos, diferente transferencia [D]

Sean los vectores enteros y polarizaciones:

\[
 k=n(1,0,0),\quad l=n(0,1,1),\quad m=k+l=n(1,1,1),
 \quad A=(0,1,0),\ B=(1,0,0),\ C=(1,1,-2),\quad n\in\mathbb N.
\]

Se verifican `k·A=l·B=m·C=0`. Definamos los datos iniciales suaves

\[
\boxed{u_0(x)=aA\cos(k\cdot x)+bB\cos(l\cdot x)+cC\sin(m\cdot x),}\tag{79.3}
\]

con `a,b>0`, `c` real. Por ser un polinomio trigonométrico solenoidal, constituye dato periódico suave para Navier–Stokes y posee solución suave local. Esta triada depende de dos combinaciones espaciales independientes, aunque vive en `T³`. En §5 agregamos un cuarto modo que la convierte en un campo genuinamente dependiente de tres coordenadas.

La energía media del modo `±m` es

\[
 E_m=\frac12\sum_{s=\pm m}|\widehat u_s|^2=\frac32 c^2.
\]

Al calcular `-(u·∇)u` y eliminar su parte de presión se obtiene la contribución exacta en ese modo:

\[
\left.\partial_tu\right|_{\mathrm{no\ lineal},m}
=\frac{nab}{6} C\sin(m\cdot x),\tag{79.4}
\]

pues `P_m(A+B)=C/3` y `A·l=B·k=n`. Por tanto, el **balance inicial exacto** satisface

\[
\boxed{\frac{dE_m}{dt}(0)=\underbrace{\frac{nabc}{2}}_{T_m}\;\underbrace{-9\nu n^2c^2}_{\mathrm{disipaci\acute on}}.}\tag{79.5}
\]

Las otras dos transferencias no lineales iniciales son `T_k=T_l=−nabc/4`, de modo que `T_k+T_l+T_m=0`, como exige la conservación instantánea de energía por el término convectivo. Cambiar `c→−c` **no cambia ningún espectro modal de magnitud** ni la energía global inicial, pero invierte las tres transferencias no lineales. Por consiguiente, las magnitudes por modo y su subred común **no constituyen un normalizador dinámico suficiente para predecir `E_m'(0)`**.

Para `n=a=b=1`, `c=±1/4`, `ν=0.01`:

| Variable | c=+1/4 | c=−1/4 |
|---|---:|---:|
| Energía media total `E(0)` | 0.593750 | 0.593750 |
| `E_m(0)` | 0.093750 | 0.093750 |
| `T_m(0)` | +0.125000 | −0.125000 |
| Pérdida viscosa `-9ν c²` | −0.005625 | −0.005625 |
| `E_m'(0)` | **+0.119375** | **−0.130625** |

**Advertencia:** esto es un teorema de insuficiencia de un comparador (magnitudes + múltiplos), no una refutación del programa si su referencia incluye las relaciones de fase pertinentes, y no un contraejemplo a la suavidad de NS.

## 3. Proposición O79-T2: una relación nueva a escala igual [D]

El modo de diferencia `d=k−l=n(1,−1,−1)` está inicialmente desocupado: `û_d(0)=0`. La derivada inicial sí lo ocupa:

\[
\boxed{\left.\partial_tu\right|_{d,t=0}
=\frac{nab}{6}(-1,1,-2)\sin[(k-l)\cdot x].}\tag{79.6}
\]

El término viscoso no aporta nada inicialmente a ese modo nulo. Se demuestra expandiendo los productos `cos(k·x) sin(l·x)` y `sin(k·x) cos(l·x)` y aplicando la proyección sobre `d`.

**Diferencia crucial:** `|d|=|m|=\sqrt3 n`. La nueva relación tiene **la misma magnitud de frecuencia** que otra previamente habitada, pero distinta dirección del vector de onda y diferente fase. La novedad dinámica no siempre equivale a reducir un radio o aumentar una profundidad. La familia original de tres modos no es invariante porque la evolución crea otros modos; esto no prohíbe una jerarquía que incorpore esa novedad.

## 4. El reloj endógeno del flujo distingue futuros [D]

Usamos exactamente la escala O25:

\[
 A_\omega=\langle|\omega|^2\rangle,\quad
 B_\omega=\langle|\nabla\omega|^2\rangle,\quad
 \ell_\omega=(A_\omega/B_\omega)^{1/2}.
\]

Para (79.3), a tiempo inicial:

\[
\begin{aligned}
 A_\omega&=n^2(a^2/2+b^2+9c^2),\\
 B_\omega&=n^4(a^2/2+2b^2+27c^2),\\
 C_\omega&=n^6(a^2/2+4b^2+81c^2).
\end{aligned}\tag{79.7}
\]

`C_ω=⟨|Δω|²⟩` aquí. Al derivar los balances exactos con (79.2),

\[
 \boxed{A'_\omega=\tfrac32n^3abc-2\nu B_\omega,\quad
 B'_\omega=\tfrac{13}{2}n^5abc-2\nu C_\omega,\quad
 \ell'_\omega=\frac{\ell_\omega}{2}\left(\frac{A'_\omega}{A_\omega}-\frac{B'_\omega}{B_\omega}\right).}\tag{79.8}
\]

Con `n=a=b=1,c=±1/4,ν=0.01` ambos estados poseen `ℓ_ω(0)=√(33/67)≈0.7018100266` y, sin embargo,

\[
\boxed{\ell'_{\omega,+}(0)\approx-0.0705936454,\qquad
\ell'_{\omega,-}(0)\approx+0.0741487210.}\tag{79.9}
\]

El reloj `ds/dt=v_*/ℓ_ω(t)` de O25 **ya estaba definido**. Si se toma `v_*=1`, los dos sistemas tienen igual primera tasa `s'(0)` y distinta segunda tasa `s''(0)=−ℓ'_ω/ℓ_ω²` (aprox. `+0.14332649` frente a `−0.15054437`). La regla que reconstruye el reloj físico precisa la dinámica de fase, no únicamente la magnitud espectral instantánea.

## 5. Prueba adicional con dependencia espacial genuinamente tridimensional [D/E]

Para impedir que el resultado dependa exclusivamente de datos de rango espacial dos, se añade la onda

\[
 d\,(1,0,0)\cos(nz),\qquad d=0.3.
\]

La base de los tres vectores `k,l,(0,0,n)` tiene rango tres. El modo añadido es solenoidal y no genera ninguna pareja adicional que sume `m`, `k` o `l` entre los modos iniciales. Por tanto la transferencia exacta `T_m=nabc/2` y su inversión de signo permanecen. Los datos ahora dependen realmente de `x,y,z`. En (79.7), las expresiones `A_ω,B_ω,C_ω` ganan respectivamente `n²d²/2, n⁴d²/2, n⁶d²/2`; las contribuciones no lineales de (79.8) permanecen, y la viscosidad incluye esos términos adicionales. Se comprueba con Fourier para `n=1` y `n=2`.

La construcción no demuestra que esos datos provoquen pérdida de regularidad; ambas condiciones iniciales son suaves y el enunciado se limita a las tasas instantáneas, que pueden calcularse exactamente.

## 6. Escalado entre ramas — resultado condicional, no cierre general [D/A]

Escalando la triada como `n=2^j` y `a=b=|c|=n^{-α}`, la transferencia no lineal *al modo `m`* tiene magnitud

\[
 \boxed{|T_m|=\tfrac12 n^{1-3α},\quad
 |\partial_t W_m|_{\mathrm{no\ lineal}}=|m|^2|T_m|=\tfrac32 n^{3-3α},}\tag{79.10}
\]

si `W_m=|m|²E_m` es la enstrofía del modo. La suma de **estas contribuciones triádicas aisladas** sobre `n=2^j` es geométrica y finita si y solo si `α>1`; para `α=1` cada contribución es constante. Su comparación con O78 es matemática y útil, pero no hay una ley física que imponga `α` ni un desacoplamiento automático entre triadas de escalas distintas.

**Límite:** en un campo con varias triadas presentes, los términos cruzados entre ramas generan interacciones adicionales. Sumar estimaciones de triadas separadas no controla por sí solo la transferencia completa de NS 3D. Para una solución inicialmente suave con infinitas frecuencias hace falta elegir además amplitudes que satisfagan las condiciones Sobolev requeridas; `α>1` en esta construcción es umbral de un balance específico, **no una demostración general de regularidad**.

## 7. Herencia de un común sin clausurar artificialmente los perfiles [D]

Para cada `n`, los modos iniciales anteriores pertenecen a la subred `n\mathbb Z³`. Mientras la solución periódica siga siendo suave y única, la evolución preserva la periodicidad espacial `2π/n` en cada coordenada y por ello no genera frecuencias fuera de `n\mathbb Z³`. Ésta es **herencia física exacta de una estructura de etiquetas**, pues Navier–Stokes es equivariante por traslación. Sin embargo, en esa subred hay infinitas frecuencias disponibles y el producto cuadrático genera algunas que inicialmente no estaban presentes, como (79.6).

La propiedad heredable demostrada es la **subred**, no la congruencia cuadrática `a²+b²+1=N²` de O58 ni una cota universal de amplitudes.

## 8. Contrato para una semilla realmente suficiente [O/D/A]

La condición abstracta de O78 es `C∘Φ_t=\bar Φ_t∘C`. Para los datos O79, el comparador formado por (i) magnitudes espectrales, (ii) subred heredada y (iii) escala/reloj O25 **no satisface** ese contrato para predecir la derivada modal ni la derivada del reloj, porque `c` y `−c` comparten todos esos datos y producen tasas diferentes.

Una interfaz que retenga, al menos, el producto de fase/resonancia `abc` junto con las etiquetas triádicas resuelve esta diferencia **instantánea**. A medida que se habitan nuevas relaciones como `k−l`, también se requieren sus interacciones para predecir pasos posteriores. No queda demostrado que una interfaz universal pequeña o finita pueda llevar todas las continuaciones sin reconstruir progresivamente información adicional.

El siguiente problema, O80, sería investigar una jerarquía de **restos de interacción** con norma y tasa controlables uniformemente entre ramas, y probar si el normalizador heredado predice o acota los términos cruzados. Se debe evitar fijar de antemano que cada rama permanece aislada o que basta su contador entero.

## 9. Reproducción [E]

Ejecutar `python3 codigo/verificar_o79.py` (NumPy) en este directorio. El código evalúa `u_0`, sus derivadas espectrales, la proyección de Leray y sus balances en mallas `16³–48³`, escalas `n=1,2,4`, ambos signos de `c` y campos genuinamente tridimensionales por inclusión del cuarto modo. Compara todos los observables con las fórmulas analíticas y verifica errores al nivel de redondeo. **268 aserciones ejecutadas correctamente.** Los resultados se guardan en `resultados/`.

`python3 codigo/graficar_o79.py` (matplotlib) regenera los gráficos. Este experimento certifica identidades instantáneas en una familia explícita de datos, **no integra en el tiempo** una solución PDE ni verifica regularidad global de NS 3D.

## Referencias internas del programa

- O25: escala y reloj endógenos del flujo.
- O40 y O58: normalizador transportado, resto y eco de múltiplos.
- O66 y O67: presupuestos de transferencia y límites para regularidad.
- O70 y O76: parte común obtenida por reflejos y dependencias omitidas.
- O77: una subfamilia gaussiana fija no captura toda la evolución del anillo.
- O78: onda de cizalla multiescala exacta, sin interacciones no lineales entre las ramas.
