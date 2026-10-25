# O75 — Del cierre del cuadrado al transporte real de las relaciones

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 22 de octubre de 2026 · **Suplemento aditivo posterior a O74**  
**Ámbito:** proyecciones tetraedro/cuadrado, enlaces de cuatro cápsulas, referencia colectiva y Navier–Stokes.  
**Dictamen:** identidades exactas `[D]`, soluciones exactas de NS `[D–NS]`, falsadores de propuestas universales `[F]`, interpretación ontológica `[O/H]`. **No es una demostración de la regularidad global de NS 3D.**

## 0. Ontología primero [O]

La totalidad precede a la representación, pero no debe identificarse con una magnitud de energía. Cuatro cápsulas con cierre propio, proyectadas como un anillo cuadrangular, dejan dos relaciones diagonales sin participar de la condición activa. Un cierre compartido por los enlaces habilita una libertad de movimiento; no fija la geometría ni el tiempo por sí solo. El múltiplo que normalizó una relación puede continuar como referencia, pero **tener una referencia numérica común no significa que se haya preservado toda la información que determina la configuración siguiente**.

**Pregunta de O75:** ¿podemos construir, usando exclusivamente un campo de velocidad `u(x,t)`, un monitor del cierre de cuatro enlaces y deducir de Navier–Stokes cuándo se sostiene? Sin imponer que las cuatro cápsulas sean engranajes sólidos ni forzar la sincronización. ¿La incompresibilidad garantiza ese cierre?

## 1. Narrativa del experimento de espejo [N]

La caja de espejos ofrece cuatro observaciones de una trama y permite seleccionar una familia cerrada de enlaces. «Apagar la caja» debe significar que la referencia no depende de seguir proyectando **más imágenes**, no que se retiran físicamente paredes que modifican el flujo. Para el laboratorio, escogemos cuatro etiquetas materiales en un flujo ya definido; el campo `u` y su dinámica no dependen de que sigamos observándolas.

Cada etiqueta tiene dos direcciones de relación: la del enlace entrante y la del saliente. Las llevamos con el flujo. Comparamos cuánto se transforman ambas al llegar a la siguiente configuración. El producto de las cuatro comparaciones es una **candidata a referencia de enlace**, no todavía «el» normalizador ontológico único.

## 2. Teorema O75.1 — Transporte material de direcciones [D]

Sea `u` un campo suave en un intervalo `[0,T)` y `X_i(t)` cuatro partículas materiales iniciadas en `x_i`:

\[
\dot X_i(t)=u(X_i(t),t),\qquad X_i(0)=x_i.
\]

La transformación diferencial del flujo `F_i(t)=D\Phi_t(x_i)` satisface

\[
\boxed{\dot F_i=(\nabla u)(X_i,t)F_i,\qquad F_i(0)=I_3.}\tag{75.1}
\]

**Demostración.** Diferenciar la ecuación de trayectoria con respecto a la condición inicial: la regla de la cadena da `∂_t DΦ_t=(Du)(Φ_t,t)DΦ_t`. No se necesita imponer ninguna sincronización. QED.

Para un fluido incompresible:

\[
\boxed{\det F_i(t)=1.}\tag{75.2}
\]

En efecto, Jacobi da `d/dt det F_i=(∇·u)(X_i,t)det F_i=0`. Este es un **cierre volumétrico material real** para soluciones suaves, pero no constituye control sobre la anisotropía, los gradientes o la vida global de la solución. Por ejemplo `diag(e^s,e^{-s},1)` tiene determinante 1 para todo `s`, y su estiramiento máximo crece sin límite al crecer `s`.

## 3. Teorema O75.2 — Referencia de los cuatro enlaces [D]

Fijemos los cuatro vértices iniciales de un cuadrilátero simple `x_1,...,x_4`, en orden cíclico, y las direcciones unitarias materiales

\[
 e_i^-={x_i-x_{i-1}\over |x_i-x_{i-1}|},\qquad
 e_i^+={x_{i+1}-x_i\over |x_{i+1}-x_i|}.
\]

Definamos **brazos de enlace como estiramientos infinitesimales en el punto `i`**:

\[
 a_i(t)=|F_i(t)e_i^-|,\qquad b_i(t)=|F_i(t)e_i^+|,
 \qquad H_F(t)=\prod_{i=1}^4{a_i(t)\over b_i(t)}.\tag{75.3}
\]

Todos valen 1 en `t=0`; por eso `H_F(0)=1`. Obsérvese que estos `a_i,b_i` **no son** los radios de cápsulas ni brazos de contacto realmente rígidos de O74. Son factores materiales medibles por dos direcciones locales. La redefinición es explícita para no suponer la equivalencia física de los modelos.

Sea `S_i=(∇u(X_i)+∇u(X_i)^T)/2`, y

\[
 t_i^\pm(t)={F_i(t)e_i^\pm\over|F_i(t)e_i^\pm|}.
\]

Entonces:

\[
 \boxed{\frac{d}{dt}\log H_F=\mathcal B(t):=\sum_{i=1}^4
 \left[t_i^{-T}S_i t_i^- - t_i^{+T}S_i t_i^+\right].}\tag{75.4}
\]

**Demostración.** Para cualquier `w(t)=F_i(t)e` no nulo, `\dot w=(∇u)w`; por derivación de la norma, `d log|w|/dt=(w/|w|)^T S_i(w/|w|)`. Restar las expresiones entrante y saliente, y sumar en `i`, da (75.4). QED.

Corolario exacto:

\[
 \boxed{H_F(t)=\exp\!\left(\int_0^t\mathcal B(s)\,ds\right).}\tag{75.5}
\]

Por tanto `H_F(t)=1` **para todo `t` en un intervalo** si y sólo si `\mathcal B(t)=0` para todo `t` de ese intervalo. Una cancelación integral puede hacer `H_F(t_*)=1` en un tiempo aislado sin imponer `\mathcal B≡0`.

### Casos en que el producto se cierra sin contenido dinámico propio

Si la matriz `F_i` es idéntica en los cuatro vértices, entonces el factor de estiramiento de cada lado en su extremo final es igual al del mismo lado en su extremo inicial. Los cocientes **se cancelan telescópicamente** y `H_F≡1`, sea o no `det F=1`. Esto explica por qué un producto que siempre cierre por construcción puede ser sólo una identidad de representación y **no una nueva ley del fluido**.

Para `F_i` diferentes, `H_F` registra una forma de heterogeneidad espacial y direccional de deformación material, dependiente de la elección de los cuatro nodos y de sus enlaces. No es un invariante canónico de NS.

## 4. Falsador analítico O75.3: Navier–Stokes exacto, H_F no conservada [D–NS/F]

Tomemos el flujo periódico tridimensional que no depende de `z` (Taylor–Green bidimensional embebido):

\[
 u=A(t)(\sin x\cos y,-\cos x\sin y,0),\quad
 A(t)=Ue^{-2\nu t},\tag{75.6}
\]

\[
 {p\over\rho}=-{A(t)^2\over2}(\sin^2x+\sin^2y),\qquad \nu>0.
\]

Es una solución **exacta de Navier–Stokes 3D periódico**: `div u=0`, `Δu=-2u`, `∂_tu=-2νu`, y la suma advección + gradiente de presión es cero. Es un flujo bidimensional embebido, no un anillo vorticial.

Consideremos los vértices iniciales

\[
 x_1=(0,0,0),\ x_2=(\pi/2,0,0),\ x_3=(\pi/2,\pi/2,0),\ x_4=(0,\pi/2,0).
\]

Al inicio `S(x_1)=diag(U,-U,0)`, mientras las contribuciones de deformación de los otros tres vértices al presupuesto (75.4) se anulan. En `x_1`, la dirección entrante es vertical y la saliente horizontal, por lo cual:

\[
 \boxed{\mathcal B(0)=-2U\ne0,\qquad H_F(0)=1.}\tag{75.7}
\]

Como las trayectorias y `H_F` son suaves, `H_F(t)≠1` para `t>0` suficientemente pequeño. **Concluimos rigurosamente que la incompresibilidad y las ecuaciones completas de NS no imponen `H_F≡1` para todos los cuadriláteros materiales**. No hay singularidad en el campo de velocidades.

## 5. Falsador tridimensional con vorticidad no nula: campo ABC [D–NS/F]

Para no depender sólo del ejemplo bidimensional, usemos el campo ABC de coeficientes iguales:

\[
 u=A(t)(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x),
 \quad A(t)=Ue^{-\nu t}.\tag{75.8}
\]

En el toro periódico `T³`, `div u=0`, `curl u=u`, `Δu=-u`. Por la identidad vectorial `u·∇u=∇|u|²/2-u×(curl u)`, satisface NS exactamente con `p/ρ=-|u|²/2`. Tiene vorticidad tridimensional real (no es un flujo de dos componentes).

Elegimos un cuadrado material inicial de lado `1,2`, situado en `z=0,4`, girado `0,47` radianes respecto del eje `x` y centrado en `(0,3; 0,6; 0,4)` [coordenadas escritas en el código con punto decimal]. Para `U=1`, la identidad (75.4) da:

\[
 \boxed{\mathcal B(0)\approx -0.6718085063988544\ne0.}\tag{75.9}
\]

La expresión es una evaluación numérica de una identidad **analítica exacta** aplicada al campo (75.8). Por continuidad, `H_F` deja de valer 1 también en una solución verdaderamente tridimensional y suave con vorticidad no nula. Un cálculo de trayectorias y matrices materiales verifica toda la evolución a precisión de integración.

### Datos comparativos del laboratorio

**Parámetros ilustrativos** `ν=0,05`, `U=1`, duración `0,9`; unidades adimensionales. Son soluciones de velocidad analíticamente exactas; la integración de las etiquetas materiales y `F_i` es numérica de alta precisión.

| Campo | `d log H_F/dt` en `t=0` | `H_F(0)` | `H_F(0,9)` | Error máximo de `det F_i−1` |
|---|---:|---:|---:|---:|
| Taylor–Green 2D en 3D | −2 | 1 | 0,17881987 | `1,5×10⁻¹¹` |
| ABC 3D Beltrami | −0,67180851 | 1 | 0,42376412 | `4,1×10⁻¹²` |

**Interpretación:** se conserva el volumen material local, pero no la comparación particular de deformaciones entrantes/salientes. `H_F` no pretende ser el único monitor posible de cierre; este resultado invalida *sólo la conjetura de su conservación universal*.

## 6. Una insuficiencia aún más fuerte: mismos datos locales, futuro distinto [D–NS/F]

Consideremos dos soluciones exactas periódicas suaves:

\[
 u^{(0)}(x,y,z,t)=0,
 \quad u^{(1)}(x,y,z,t)=\left[w(y,t),0,0\right],
\]

\[
 w(y,t)={\epsilon\over4}\left(e^{-4\nu t}\cos 2y-e^{-36\nu t}\cos 6y\right).
 \tag{75.10}
\]

Son soluciones de Navier–Stokes: el término advectivo es cero y `w_t=νw_{yy}`. En `t=0`, `w(y,0)=ε sin²(2y) cos(2y)`. En las alturas `y=0` e `y=π/2` que ocupan los vértices del cuadrado (75.7), tenemos exactamente:

\[
 u^{(0)}=u^{(1)}=0,\qquad \nabla u^{(0)}=\nabla u^{(1)}=0.\tag{75.11}
\]

**Pero:**

\[
 \partial_tu^{(1)}|_{t=0,y=0}=8\nu\epsilon e_x,\qquad
 \partial_tu^{(1)}|_{t=0,y=\pi/2}=-8\nu\epsilon e_x,
\]

mientras `∂_t u^{(0)}=0` en todas partes. Las posiciones, las velocidades y todos los gradientes espaciales de **primer orden muestreados en los cuatro nodos** no bastan para reconstruir la evolución de sus velocidades. Es una afirmación sobre **este conjunto finito de datos locales**, no sobre cualquier representación finita imaginable ni sobre todos los espectros de fase posibles.

El campo que falta puede transportarse fuera de los nodos mediante difusión viscosa; una referencia suficiente necesitaría incluir información espacial que el muestreo no conserva. Esto dialoga con O70/O71: coincidencia proyectada no garantiza igualdad del futuro.

## 6 bis. Una semilla física transportada: la vorticidad en la referencia material [D–NS]

Hay una estructura derivada **directamente de la ecuación**, anterior a escoger cuatro enlaces. Para soluciones suaves incomprensibles, sea `ω=∇×u` y `A=∇u`. La vorticidad satisface

\[
 {D\omega\over Dt}=A\omega+\nu\Delta\omega.\tag{75.12}
\]

Por (75.1) y la identidad `d F^{-1}/dt=−F^{-1} A`, obtenemos la **identidad exacta**

\[
 \boxed{ {D\over Dt}\left(F^{-1}\omega(X(t),t)\right)
   =\nu F^{-1}\Delta\omega(X(t),t). }\tag{75.13}
\]

Equivalente a la formulación integral

\[
 \boxed{\omega(X(t),t)=F(t)\left[\omega_0(x)+\nu\int_0^t F(s)^{-1}\Delta\omega(X(s),s)\,ds\right].}\tag{75.14}
\]

**Prueba:** derivar `F^{-1}ω`, sustituir (75.1) y (75.12); se cancelan los términos de estiramiento `Aω`. QED. Es el análogo viscoso de la fórmula de Cauchy para vorticidad. Para `ν=0` la parte `F^{-1}ω` es constante sobre la trayectoria; para `ν>0` recibe la contribución explícita de difusión.

**Interpretación en el vocabulario del programa:** la relación material que llega desde la configuración anterior se distingue de la nueva contribución procedente de las regiones vecinas. Eso formaliza una manera de transportar continuidad entre participantes materiales. **No identifica** todavía esta vorticidad con el «momento de sustentación ontológica», ni garantiza que un toroide conserve su identidad o que sus gradientes sigan acotados.

La viscosidad acopla cada punto con su entorno a través de `Δω`: no es una transferencia determinada por sólo cuatro valores de radio y frecuencia. Los campos TG y ABC fueron verificados con esta identidad; la integral material se comparó numéricamente con el transporte directo.

### Qué información falta para que la semilla compute su propio futuro

Derivando la ecuación de Navier–Stokes espacialmente, su gradiente `A` satisface

\[
 \boxed{ {DA\over Dt}=-A^2-\nabla\nabla(p/\rho)+\nu\Delta A. }\tag{75.15}
\]

La presión no es un dato arbitrario del modelo. Para `div u=0`, en el toro periódico:

\[
 \boxed{\Delta(p/\rho)=-\operatorname{tr}(A^2).}\tag{75.16}
\]

Por tanto, incluso si intentamos hacer evolucionar los cuatro gradientes `A_i` junto con `F_i`, aparecen el Hessiano de la presión y el laplaciano de `A`. Esas cantidades dependen del campo espacial completo. Una condición cerrada exclusivamente con cuatro radios y ritmos exigiría demostrar una cancelación o representación reducida **adicional** que elimine esa dependencia sin imponerla desde afuera. O75 identifica dónde entra esa información, no la ha eliminado.

## 7. Dónde están los giros, radios y múltiplo en la construcción [H]

**Radios:** no se convierten en causas fundamentales; se representan como diferencias de posición en el circuito material y como las direcciones y longitudes de contacto escogidas. **Frecuencias:** las tasas de fase se pueden calcular del campo `u` una vez definido un eje común; no son invariantes independientes de ese eje. **Orientación:** se registra mediante el área vectorial del polígono, y para un elemento material orientado mediante productos cruzados transformados por `F`. **Múltiplo:** la telescopía de `H` en deformación homogénea es un retorno de referencia *real*, no un múltiplo entero de vueltas al estilo O68; la cuantización no se ha obtenido.

**La diferencia normalizada y el múltiplo del sistema siguen siendo objetos diferentes**. Para una normalización aritmética de giros enteros, Bézout puede dejar una unidad y un múltiplo L; el campo NS no obliga a que los estiramientos materiales sean racionales. Por ello no se trasladó arbitrariamente ese resultado a `H_F`.

Si un observador define una «referencia compensada»

\[
 \widehat H(t):=H_F(t)\exp\left(-\int_0^t\mathcal B(s)ds\right),
\]

entonces `Ĥ(t)=1` por (75.5), **pero es tautológico**: exige conocer de antemano toda la historia del término que se buscaba predecir. No constituye una ley de cierre autónomo ni una solución de Navier–Stokes. Un verdadero normalizador predictivo debe cerrar su evolución en información obtenible del estado propuesto sin alimentar el futuro como entrada.

## 8. Consecuencia para la regularidad [F]

Conocer que `det F=1` mientras la solución es suave y/o que alguna relación de cuatro enlaces coincide, no da una cota sobre `||∇u||_∞` ni sobre la enstrofía. Incluso si identificamos un `H` especialmente adaptado a un anillo, una demostración general tendría que:

1. Definirlo de manera objetiva desde el estado `u` sin escoger a mano un circuito favorable;
2. Derivar una ecuación de evolución cerrada o un presupuesto `a priori` utilizable, incluso cuando las simetrías del anillo se rompen;
3. Obtener una restricción cuantitativa de los gradientes para **todos** los datos suaves admitidos, o explícitamente restringir el teorema a una clase determinada;
4. Evitar usar la cota de regularidad buscada como hipótesis encubierta.

El puente matemático O75 es correcto como construcción **transportada desde el campo**. Los ejemplos TG y ABC descartan que su cierre constante sea una ley universal de NS. No se ha encontrado una solución del problema del milenio.

## 9. Qué aporta O75 y siguiente pregunta O76

- **Derivado:** `F_i` transporta las relaciones, y la incompresibilidad normaliza el volumen infinitesimal por `detF=1`.
- **Derivado:** la deriva de las relaciones de enlace está determinada por diferencias locales de deformación `S`.
- **Falsado:** la conservación universal de `H_F=1` en la evolución viscosa tridimensional; existe un falsador ABC exacto.
- **Derivado:** la forma actual de la semilla, que sólo guarda posiciones y gradientes de cuatro puntos, es insuficiente para predecir incluso las velocidades futuras de esos mismos puntos.
- **Abierto:** qué información espacial adicional constituye una referencia dinámica suficiente, de menor complejidad que todo `u(x,t)`, si tal referencia existe para la familia de anillos.

**Propuesta O76:** representar el residual de la caja de espejos y el tensor de deformación transportado en una familia jerárquica de escalas; investigar cuándo esa jerarquía se cierra bajo NS y cuándo su evolución introduce una nueva relación irreductible. Es una pregunta falsable de suficiencia predictiva, no un supuesto de que el cierre existe.

## 10. Reproducción

Desde la raíz del paquete:

```bash
python codigo/verificar_o75.py
```

Dependencias: `numpy`, `scipy`, `matplotlib`. Se generan `datos/resumen.json`, trayectorias CSV y una gráfica comparativa PNG. Las pruebas incluyen verificación punto a punto de la ecuación de NS en los dos campos analíticos, incompresibilidad, identidad de transporte viscoso de vorticidad, derivada de `H_F`, matrices materiales con `detF≈1`, telescopía para deformación homogénea y un caso de muestreo local insuficiente. **No se presenta el número de aserciones como evidencia de regularidad global.**

### Antecedentes del propio programa

O68: normalización entera por Bézout; O69: fases materiales del anillo; O70/O71: referencia común y residuales no visibles; O72: anillo par y relaciones liberadas; O73: impulso vorticial y el régimen axisimétrico sin giro; O74: cierre `H=1` del modelo de contactos y contraste con degeneración geométrica.
