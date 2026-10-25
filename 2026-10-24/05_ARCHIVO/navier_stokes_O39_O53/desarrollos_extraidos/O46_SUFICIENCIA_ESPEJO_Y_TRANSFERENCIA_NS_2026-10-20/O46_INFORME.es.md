---
title: "O46 — Suficiencia dinámica contextual, fase y escala del espejo en Navier–Stokes 3D"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Suplemento auditable: teoremas instantáneos para datos 3D suaves, regresión de pruebas preexistentes y falsadores; no es una solución de regularidad global"
parents: ["MF-43", "MF-86", "MF-97", "O25", "O39", "O40", "O41", "O42", "O43R", "O43E", "O44", "O44N", "O45"]
---

# O46 — La información necesaria para continuar: el espejo no es solamente un radio

## 0. Contrato epistemológico

- **[O] Ontología del programa:** la singularidad es cierre propio respecto de una referencia normalizadora. El desplazamiento del espejo cambia el espacio relacional de comparación; el tiempo medido surge de comparar ritmos del flujo, la singularidad/referencia espacial y la partícula. El múltiplo que normalizó una relación la mantiene representable bajo refinamientos; no se identifica con su residuo aislado.
- **[T] Exacto:** las ecuaciones y equivalencias aquí demostradas para campos iniciales suaves, periódicos, libres de divergencia de Navier–Stokes 3D. Las derivadas en `t=0` son derivadas de la solución suave local de las PDE, no de una simulación aproximada.
- **[E] Verificado:** identidades mediante evaluación tridimensional sobre 24³, 32³ y 48³ puntos. Se repitieron verificaciones de O42, O43R, O43E, O44, O45; ver informe de regresión.
- **[F] Falsador:** un comparador que conserve solamente el MCM, la enstrofía y la fase triádica es insuficiente incluso para la derivada inicial de la enstrofía; otro comparador, con una escala espectral endógena, sí determina esa derivada **dentro de esta familia**, pero no la solución futura completa.
- **[A] Abierto:** ley física no arbitraria del foco/ritmo de singularidad, partículas con verdaderos retornos materiales, clausura dinámica no tautológica para NS 3D general y estimación de regularidad global.

**Precaución:** singularidad ontológica ≠ singularidad analítica. Una interfaz suficiente para un observable y una derivada instantánea no lo es automáticamente para todos los tiempos ni para otras preguntas.

## 1. Resultados previos recuperados, no reinventados

- **MF-86 y MF-97:** normalización suficiente/idempotente/composicional y equivalencia contextual estable ante continuaciones. La identidad referenciada puede describir muchas configuraciones internas sin descartar respuestas relevantes para el contrato.
- **O25:** la escala endógena `ell_omega=sqrt(A/B)` con `A=∫|ω|²`, `B=∫|∇ω|²` y el reloj nominal `ds/dt=v*/ell_omega` son exactos para soluciones suaves con denominadores positivos. Una referencia elegida así es reproducible, no una fuerza nueva.
- **O41-T1/T2:** criterio de cociente predictivo y subclase de cizallas en 3D cuyos modos Fourier retenidos tienen una evolución autónoma exacta.
- **O41-T3/T4/T5:** no-go de las interfaces gruesas que omiten fases: hay datos 3D con estiramiento no nulo, misma interfaz/potencias, pero distinta respuesta inicial de un modo. Ya existía la variante con tres amplitudes `A,D,B` y respuesta `dot S_y`.
- **O42:** se evaluó un tubo 3D con fase `2:1`; una firma triádica de fase recuperó una transferencia instantánea en su clase y no una clausura futura.
- **O43E/O44:** anillos 3D finitamente resueltos; diferencias locales de estiramiento por fase y controles adversariales. En O44 los trazadores no completaron ninguna vuelta: no se infiere un resto material de retorno.
- **O45:** el espejo móvil de foco/escala/orientación y las dos diferencias independientes entre tres fases tienen identidades exactas de representación. No existe aún una referencia física universal `φ_s` ni continuidad del reloj material probada.

**Novedad específica O46:** integrar las pruebas anteriores mediante un **doble falsador controlado**: una triada de fase fija con diferentes repartos espectrales de vorticidad que requieren distintos ritmos de disipación, y una **reparación instantánea exacta mediante la escala endógena del espejo**. No se reivindica una novedad en la teoría clásica de PDE; es una discriminación reproducible dentro del programa.

## 2. Campos tridimensionales declarados antes de medir

Dominio `T³=(R/2πZ)³`; `ν=0.03`. Fije `A=1`, `D=0.7`, `B=0.4` y

\[
\psi(x,y)=A\cos x+D\cos y+B\cos(x-y),
\qquad h(z)=\tfrac{K_2}{2}\cos 2z+\tfrac{K_3}{3}\cos3z.
\]

Defina el dato inicial

\[
\boxed{u_0=(\partial_y\psi,\,-\partial_x\psi+h(z),\,0).}\tag{O46.1}
\]

Es liso, periódico, solenoidal y de energía finita en el toro. Su vorticidad es

\[
\boxed{\omega_0=(K_2\sin2z+K_3\sin3z,\ 0,\ A\cos x+D\cos y+2B\cos(x-y)).}\tag{O46.2}
\]

El estiramiento puntual de vorticidad no es nulo:

\[
\boxed{(\omega_0\cdot\nabla)u_0=\omega_{0x}
\left(B\cos(x-y),\,-B\cos(x-y)-D\cos y,\,0\right).}\tag{O46.3}
\]

La teoría local estándar garantiza soluciones NS suaves que parten de ambos datos durante algún intervalo positivo. No se asume que la forma (O46.1) sobreviva como ansatz invariante para `t>0`.

Use dos configuraciones de los modos **ya presentes en ambas**, sin cambiar sus etiquetas ni el MCM `mcm(2,3)=6`:

\[
\begin{array}{c|cc|c}
& K_2 & K_3 & K_2^2+K_3^2 \\\hline
\mathrm{I}&0.6&0.4&0.52\\
\mathrm{II}&0.4&0.6&0.52
\end{array}
\]

Los dos campos comparten exactamente las amplitudes/fases de `ψ`, el triángulo de interacciones en el plano, la norma global inicial de vorticidad y la magnitud cuadrática del estiramiento. Lo que cambia es la asignación de vorticidad a los modos axiales 2 y 3, con gradientes distintos.

## 3. Teorema O46-T1: mismo normalizador, fase y enstrofía, distinta palinstrofía

Use promedios espaciales `⟨·⟩` y defina:

\[
E=\tfrac12\langle|\omega|^2\rangle,
\quad J=\langle|\nabla\omega|^2\rangle,
\quad P=\langle\omega\cdot(\omega\cdot\nabla)u\rangle.
\]

Por ortogonalidad exacta de cosenos/senos,

\[
\boxed{E(0)=\frac{A^2+D^2+4B^2+K_2^2+K_3^2}{4}.}\tag{O46.4}
\]

\[
\boxed{J(0)=\frac{A^2+D^2}{2}+4B^2+\frac{4K_2^2+9K_3^2}{2}.}\tag{O46.5}
\]

Además `P(0)=0` por promedio del factor `cos(x-y)` aunque el estiramiento sea puntual y cuadráticamente no nulo. La identidad exacta de enstrofía de NS da:

\[
\boxed{\dot E(0)=P(0)-\nu J(0)=-\nu J(0).}\tag{O46.6}
\]

| Observable | I | II |
|---|---:|---:|
| `mcm(2,3)` | 6 | 6 |
| `E(0)` | 0.662500 | 0.662500 |
| `P(0)` | 0 | 0 |
| `J(0)` | 2.825000 | 3.325000 |
| `dE/dt(0)` | -0.084750 | -0.099750 |
| `⟨|(ω·∇)u|²⟩` | 0.105300 | 0.105300 |

**Demostración de insuficiencia.** Los campos comparten `E`, `N` y la fase triádica del plano `xy`, pero presentan distintas derivadas de `E`. Por el criterio de O41-T1, **ningún mapa autónomo de `(E,N,fase-tríada)` puede determinar la derivada de `E` para ambos casos**. Esto no exige inferir que el estado físico pierde información: la interfaz la omitió.

## 4. Teorema O46-T2: el espejo espectral devuelve el dato que faltaba

O25 definió sobre el mismo dominio la escala endógena

\[
\boxed{\ell_\omega^2=\frac{\langle|\omega|^2\rangle}{\langle|\nabla\omega|^2\rangle}=\frac{2E}{J}.}\tag{O46.7}
\]

En nuestra familia `P(0)=0`; así,

\[
\boxed{\dot E(0)=-\frac{2\nu E(0)}{\ell_\omega(0)^2}.}\tag{O46.8}
\]

Los dos espejos tienen por tanto distintas escalas **seleccionadas por el flujo**:

| Referencia | I | II |
|---|---:|---:|
| `ell_omega(0)` | 0.6848551297 | 0.6312655864 |
| `ds/dt=v*/ell_omega`, con `v*=1` declarado | 1.46016 aprox. | 1.58412 aprox. |

**Alcance real:** `(E,ell_omega,ν)` es suficiente para el valor de `dot E(0)` **en esta familia**, porque la producción global es cero en el instante inicial. La identidad (O46.7) es un cambio de representación de `J`: la nueva escala no descubrió un mecanismo de disipación ni ofrece una predicción independiente del PDE. Tampoco es suficiente para la evolución completa de los modos o para cualquier `t>0`.

Para un dato NS 3D general, la ley sigue siendo

\[
\boxed{\dot E=P-2\nu E/\ell_\omega^2.}\tag{O46.9}
\]

El estiramiento `P` permanece como dato a controlar. Un espejo normalizado endógenamente no lo determina en general.

**Lectura del tiempo.** Si se utiliza el reloj nominal de escala `ds/dt=v*/ell_omega` de O25, en el instante inicial de esta clase:

\[
\boxed{\frac{dE}{ds}(0)=-\frac{2\nu E(0)}{v_*\ell_\omega(0)}.}\tag{O46.10}
\]

Ésta es una relación exacta entre una tasa de disipación y un reloj **elegido** desde el flujo, no la derivación de un tiempo físico absoluto ni de un ritmo universal propio de una singularidad ontológica. Todavía no incorpora el reloj efectivo de una partícula con retorno material.

## 5. Teorema O46-T3: la fase triádica reconstruye otra pregunta instantánea

Para la `ψ` de (O46.1), considere los coeficientes de Fourier `c_k=hat ψ(k)` con
`k_x=(1,0)`, `k_y=(0,1)`, `k_d=(1,-1)` y `k_x=k_y+k_d`.
Defina el **bispectro real libre de traslación**:

\[
\boxed{\beta=\Re\big(\overline{c_{k_x}}\,c_{k_y}\,c_{k_d}\big)=\frac{ADB}{8}.}\tag{O46.11}
\]

Si `S_y=|hat ω_z(0,1,0)|²` es la potencia de vorticidad del modo bajo, O41-T5 se reescribe exactamente en esta familia:

\[
\boxed{\dot S_y(0)=-\frac{\nu D^2}{2}-2\beta.}\tag{O46.12}
\]

El término extra `h(z)` no contribuye a este modo axial cero en la **primera derivada**. Por eso I y II comparten `dot S_y(0)=-0.07735`, mientras presentan distintas `dot E(0)`.

Bajo cualquier traslación `(x,y)→(x+α,y+β_0)` los coeficientes adquieren fases que se cancelan exactamente en el producto triádico. Así el bispectro conserva una comparación significativa sin depender del origen del espejo.

**Falsador de omisión de fase:** al cambiar `B→−B`, las magnitudes de Fourier iniciales, `E`, `J` y `ell_omega` no cambian, pero `β` invierte su signo y con ello cambia `dot S_y(0)`. Sin este comparador de fase, el espejo endógeno solo no cierra esta pregunta modal.

## 6. Reconciliación con O45: tres ritmos no son tres datos independientes de fase

O45 separa flujo `φ_f`, singularidad/ref. espacial `φ_s` y partícula `φ_p`. Si las fases están definidas sobre una misma referencia y transforman por una misma libertad angular, entonces son independientes sólo dos diferencias `δ_fs,δ_ps`, de las cuales `δ_fp=δ_fs−δ_ps`.

O46 muestra **qué no debe confundirse**: conocer dos diferencias angulares no equivale a conocer la intensidad, la escala de gradiente ni los acoplamientos triádicos de un campo 3D completo. El bispectro `β` pertenece a la fase de modos de un campo; NO se identifica automáticamente con `δ_fs` o `δ_ps` (fases de trayectorias/referencias). La correspondencia física entre ambas exige una función de observación y prueba.

Propuesta de interfaz candidata, **no teorema de suficiencia global**:

\[
\boxed{C_Q[u,\text{referente},\text{partícula}]
=(N_{arit},\,E,\,\ell_\omega,\,\beta_{triadas\ relevantes},\,\delta_{fs},\,\delta_{ps},\,\text{otros observables exigidos por }Q).}
\]

`N_arit` organiza la representación; `ell_omega` organiza el gradiente; `β` recupera una interacción de fase; `δ` compara ritmos referidos. Para probar suficiencia, no basta escribir `C_Q`: se debe exhibir una dinámica inducida sobre la interfaz que respete las fibras de `C_Q`, esto es `C_Q(u)=C_Q(v) ⇒ C_Q(Φ_t u)=C_Q(Φ_t v)` para todo par de estados admisibles y cada `t` del contrato, según O41-T1.

**No-go formal de identidad física:** si `Q` incluye la totalidad del campo de velocidad y vorticidad, ningún listado corto de magnitudes anteriores ha demostrado determinar todas las continuaciones 3D. Elegir `Q` después de ver resultados, o definir su interfaz como la trayectoria futura completa, produciría suficiencia circular.

## 7. Ejecución y límites de verificación

Ejecutar:

```sh
python verificar_O46.py
```

Requiere Python 3 + NumPy. Incluye 66 controles en resolución `24³`, `32³`, `48³` y pruebas de cambio de origen/fase. Comprueba en muestras periódicas las identidades trigonométricas exactas y la derivada instantánea construida desde NS. La coincidencia no constituye un certificado de una PDE general ni una evolución temporal DNS.

**Controles adversariales recomendados para O47:**

1. Elegir un flujo con `P(0)≠0` (por ejemplo el dato de O42) y mostrar que `ell_omega` no determina por sí sola `dot E`.
2. Definir un comparador de fase y escala respecto de un foco espacial **endógeno y reproducible**, no una elección de marco a posteriori.
3. Introducir una partícula material y medir su fase de retorno sólo si completa una vuelta declarada; cuando no retorna, registrar fase de retorno como indefinida.
4. Medir estabilidad de la interfaz en intervalos reales y testar el defecto dinámico `DC_Q(u)F(u)` a pares equivalentes.
5. Exigir convergencia temporal, dimensional y de resolución antes de una ley de control a priori del estiramiento. No atribuir regularidad a un catálogo finito de ejemplos.

## 8. Dictamen

**[DEMOSTRADO en su clase]** Dos flujos NS 3D suaves con estiramiento local no nulo y mismos `(N,E,β)` pueden tener distintas `dot E(0)`; añadir `ell_omega` recupera `dot E(0)` bajo la condición `P(0)=0`; el bispectro recupera otro observable instantáneo que la escala por sí sola no determina.

**[NO DEMOSTRADO]** Que el múltiplo aritmético conserve energía/vorticidad, que el tiempo físico esté definido por el espejo únicamente, que tres ritmos generen por sí solos una clausura exacta de NS 3D general, que `C_Q` sea cerrado para todo tiempo, o que exista una cota general de regularidad.

**Lectura ontológica:** la unidad puede conservar su referencia y su identidad para algunas preguntas aun cuando cambie su reparto interior. Una continuación que exige nueva información obliga a refinar el comparador. El tiempo relacional añade la pregunta *cómo se transforman conjuntamente las referencias*, no una autorización para omitir el gradiente o la fase que determina la dinámica.
