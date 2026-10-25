# O84 — Contabilidad única del eco y actualización sin doble costo

**Programa de Geometría Relacional** · Le Matt Ansatz Di Ego · 22 de octubre de 2026  
**Continuación de** O40, O58, O25, O45, O79–O83.  
**Estado:** [O] interpretación ontológica; [T] teorema matemático dentro del contrato PDE; [E] comprobación reproducible; [A] puente general abierto.

## 0. La corrección que motiva O84

En O83 quedó una condición suficiente de tipo `sum_j (int_{I_j} Q(U_j) +4M_j/nu) < infinity` para una sucesión de intervalos que se acumulan en un instante finito. **Esa condición sobrecuenta el mismo resto**: sumar cotas de cada intervalo contabiliza de nuevo un residual que nunca se perdió. La formulación O84 transporta una sola cuenta de resto mediante un factor integrante global y carga únicamente el *defecto dinámico* y el *costo de cambiar la referencia*.

Narrativa/ontología: la referencia anterior se conserva mientras continúa siendo reconstruible; el múltiplo normalizador aritmético O40/O58 es una estructura diferente de la referencia PDE `U`. No confundir entre ambas sin una identificación física demostrada. El eco no implica invariancia automática del gradiente.

## 1. Definiciones físicas y contrato

En `T³=(R/2πZ)³`, viscosidad `nu>0`, fuerza cero, campo suave solenoidal de media cero:

```
partial_t u + N(u) = nu Delta u,
N(u) := P div(u tensor u),
```

con `P` el proyector de Leray. Para `f` de media cero:

\[
R(f)=\sum_{k\ne0}\frac{|\widehat f_k|}{|k|},\quad
S(f)=\sum_{k\ne0}|\widehat f_k|,\quad
Q(f)=\sum_{k\ne0}|k|\,|\widehat f_k|.
\]

Fijamos una sucesión `0=t_0<t_1<...` (finita o que puede acumularse en `T*`) y referencias suaves solenoidales de media cero `U_j(t)` en `[t_j,t_{j+1})`. Definimos:

\[
F_j=\partial_t U_j+N(U_j)-\nu\Delta U_j,\quad
B_j=R(F_j),\quad g_j=(4/\nu)S(U_j)^2,\quad v_j=u-U_j.
\]

El salto de referencia en `t_j` es
\[
J_j=R(U_{j-1}(t_j)-U_j(t_j)),\quad j\ge1.
\]

Por desigualdad triangular `R(v_j(t_j^+)) <= R(v_{j-1}(t_j^-))+J_j`. **Si la nueva referencia coincide con la anterior en la transición, `J_j=0`.**

## 2. O84-T1: un presupuesto único para toda la secuencia [T]

Sean
\[
G(t)=\int_0^t g_{j(s)}(s)\,ds,
\]
\[
\mathcal C(t)=R(u_0-U_0(0))+
\int_0^t e^{-G(s)}B_{j(s)}(s)\,ds+
\sum_{0<t_j\le t}e^{-G(t_j)}J_j.
\tag{84.1}
\]

Para todo `t<T*` tal que la solución sea suave y `R(v)<nu/2` en cada intervalo:

\[
\boxed{e^{-G(t)}R(v(t))+
\frac\nu4\int_0^t e^{-G(s)}Q(v(s))ds\le\mathcal C(t).}
\tag{84.2}
\]

**Demostración.** En cada intervalo, de O82/O83 y `R(v)<=nu/2`:
\[
D^+R(v)+(\nu/4)Q(v)\le g_jR(v)+B_j.
\]
Multiplicamos por `exp(-G)`; `G' = g_j` en cada interior. Sumamos la desigualdad integrada de todos los intervalos. Cada frontera contribuye `exp(-G(t_j)) [R(v^+)-R(v^-)] <= exp(-G(t_j))J_j`. Los términos de resto anteriores se cancelan telescópicamente; **no se vuelven a sumar**. Para infinitas transiciones con suma de saltos finita, tomar límite y usar convergencia monótona para los términos positivos. QED.

**Corolario O84-C1 (continuación condicional incluso con infinitos cierres).** Fijado un tiempo físico finito `T*`, supongamos referencias explícitas sobre `[0,T*)`, `G_* := lim_{t\uparrow T*}G(t)<infinity`, `C_* := lim_{t\uparrow T*}C(t)<infinity`, y
\[
\boxed{e^{G_*}\mathcal C_*<\nu/2,
\qquad \sum_j\int_{t_j}^{t_{j+1}} Q(U_j(t))dt<\infty.}
\tag{84.3}
\]
Entonces `R(v(t)) <= e^{G_*}C_*<nu/2`, el bootstrap es válido en todo `[0,T*)`, y
\[
\int_0^{T*}Q(v)dt\le\frac4\nu e^{G_*}C_*<\infty.
\]
Por `||\nabla u||_\infty <= Q(U)+Q(v)`, la integral temporal del gradiente es finita. Bajo la hipótesis usual de dato inicial suave y continuación local clásica, el campo no pierde regularidad en `T*` y continúa más allá. **Esto es un criterio suficiente que debe ser comprobado independientemente; no afirma regularidad para todos los datos 3D.**

**Observación:** exigir solo `J_j=0` no impone (84.3). Una secuencia de referencias puede incorporar cada novedad y a la vez acumular `G_*` o `int Q(U)` divergente.

## 3. O84-T2: actualización que hereda la referencia sin pagar salto [T]

Sea `U(t)` una referencia suave conocida para `t` posterior a `a`, con `F_U=partial_t U+N(U)-nu Delta U`. Definimos el incremento inducido **solamente desde el defecto conocido**:

\[
\boxed{C(t)=-\int_a^t e^{\nu(t-s)\Delta}F_U(s)\,ds,\qquad U^+(t)=U(t)+C(t).}
\tag{84.4}
\]

Entonces `C(a)=0`, por lo que `U^+(a)=U(a)` y `J=0`. Puesto que `(partial_t-nu Delta)C=-F_U`, el defecto nuevo satisface exactamente

\[
\boxed{F_{U^+}=N(U+C)-N(U)=N(U,C)+N(C,U)+N(C,C).}
\tag{84.5}
\]

Aquí `N(f,g)=P div(f tensor g)`. Por convolución Fourier y contracción del calor en `S`:

\[
S(C(t))\le\int_a^t S(F_U(s))ds,
\]
\[
\boxed{B_{U^+}(t)\le2S(U(t))S(C(t))+S(C(t))^2.}
\tag{84.6}
\]

Si `S(U)<=L` y `S(F_U)<=F` en `[a,a+delta]`, sigue
\[
\boxed{\int_a^{a+\delta} B_{U^+}(t)dt\le LF\delta^2+\tfrac13 F^2\delta^3,}
\tag{84.7}
\]
frente a un defecto original que habitualmente es de orden `delta`. La mejora local de orden **no** es una garantía de convergencia de infinitas iteraciones cuando L, F o las escalas aumentan.

## 4. Experimento 3D analítico: una primera actualización recupera el certificado [T/E]

Fijamos `nu=1`, `A=4`, `B=C=1`,
\[
\boxed{u_0=(A\sin y,\;B\sin z,\;C\sin x).}
\]

El dato depende de las tres variables y es incompresible; no es la incrustación bidimensional de O83. La referencia viscosa
\[
U^0(t)=e^{-t}u_0
\]
usa seis modos iniciales. Su defecto de Navier–Stokes es
\[
F_0(t)=e^{-2t}W,
\quad W=(AB\sin z\cos y,\;BC\sin x\cos z,\;CA\sin y\cos x).
\tag{84.8}
\]

`W` es solenoidal (cada componente no depende de la coordenada de su dirección vectorial), se soporta en **12 modos nuevos**, y `Delta W = -2W`:
\[
S(U^0)=L e^{-t},\quad L=A+B+C=6;
\qquad S(W)=M=AB+BC+CA=9;
\quad R(W)=M/\sqrt2.
\]

El defecto inicial del calor tiene presupuesto exacto en `[0,delta]`:
\[
G_0(\delta)=2L^2(1-e^{-2\delta}),
\quad\boxed{\mathfrak M_0(\delta)=\frac{M}{4L^2\sqrt2}\left[e^{G_0(\delta)}-1\right].}
\tag{84.9}
\]

La actualización sin salto (84.4) produce
\[
\boxed{U^1(t)=e^{-t}u_0-t e^{-2t}W.}
\tag{84.10}
\]

Para `delta=9/500=0.018`, el presupuesto nuevo queda rigurosamente acotado por
\[
\boxed{\mathfrak M_1(\delta)\le
\exp\{4\delta(L+M\delta)^2\}
\left[LM\delta^2+\frac{M^2}3\delta^3\right].}
\tag{84.11}
\]

Verificación decimal de las *fórmulas analíticas*:
\[
\boxed{\mathfrak M_0\approx0.5194887128>0.5,
\qquad\mathfrak M_1\le0.2717247466<0.5.}
\]

La separación es rigurosa, sin depender de punto flotante: en `codigo/o84_verificar.py` se prueban mediante fracciones racionales las desigualdades `M0>0.5191` y `M1<0.282456`. Se usan `e^{-x}<=1-x+x²/2`, truncaciones inferiores de la serie de `e^x` y una cota superior racional `e^(11/4)<16`.

**Interpretación:** en un campo 3D con transporte no lineal no nulo, el calor inicial falla un criterio suficiente de continuación del intervalo, pero la incorporación de las primeras doce relaciones de interacción lo satisface. No significa que la primera referencia dé lugar a una singularidad, ni que una iteración baste para todos los datos o tiempos.

## 5. Prueba adversarial: el sobreconteo de cierres puede divergir en un flujo suave [T]

Sea la solución exacta de Navier–Stokes sin fuerza
\[
u(x,y,z,t)=(a e^{-\nu t}\sin y,0,0),\quad 0<a<\nu/2.
\]

Tomamos la referencia `U_j=0` para todo `j` y una infinidad de intervalos con `t_j=1-2^{-j}` acumulados en `T*=1`. En cada intervalo, `F_j=0`, `J_j=0`, `G=0`, y el resto `v=u` tiene `R(v(t_j))=a e^{-\nu t_j}\ge a e^{-\nu}`.

El límite suficiente de O83 que contabiliza `\sum_j(4M_j/\nu)` **diverge**, porque `M_j>=a e^{-\nu}`. No obstante, la cuenta global O84 vale **exactamente** `C_*=R(v_0)=a<nu/2`, mientras `int_0^1 Q(u)dt=a(1-e^{-\nu})/nu<infinity`. No existe singularidad y no es necesario cobrar el mismo resto en cada subintervalo.

Esto demuestra que el contador telescópico es estrictamente menos restrictivo que el sobreconteo original **para este ejemplo**. No demuestra el cierre universal de todos los sistemas 3D.

## 6. Lo que sigue pendiente

1. **Construcción universal a priori:** a partir de cada dato suave 3D, generar referencias explícitas, no dependientes de conocer `u(t)` futuro, para cualquier horizonte finito.
2. **Cota uniforme bajo refinamiento:** probar (84.3), no postularla, incluso si aparecen arbitrariamente muchos modos y fases adversas.
3. **Control de amplitud y reloj:** la estela aritmética O58 y el reloj O25/O45 son compatibles con nuestra narración, pero no obligan de por sí a que `G_*`, `int Q(U)` o `C_*` sean finitos. Cualquier ley que lo afirme debe derivarse del balance de NS y de una correspondencia operacional explícita.
4. **Anillo/esfera/ola:** son posibles manifestaciones ontológicas de la regla; O84 es una prueba para campos 3D periódicos, no una clasificación exhaustiva de geometrías singulares ni una demostración del caso `R³` de energía finita.

**Conclusión:** O84 evita doble contabilización, ofrece una actualización con interfaz continua y acredita una mejora estricta en una configuración tridimensional; preserva exactamente el problema general que todavía no queda demostrado.
