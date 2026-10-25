---
title: "O66 — Presupuesto de novedad multiescala y criterio condicional de continuidad"
subtitle: "Del normalizador y la estela de escalas a una condición de regularidad para Navier–Stokes 3D"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento aditivo independiente: teorema condicional, ejemplo exacto, falsador espectral reproducible y puente físico todavía abierto"
parents: ["O40", "O44N", "O45", "O53", "O54", "O58", "O59", "O60", "O61", "O62", "O63", "O64", "O65", "Imagen Total v3.8.1"]
---

# O66 — La estela de escalas no es aún una cota de regularidad

**Contrato epistemológico.** Las etiquetas son [O] planteamiento ontológico; [D] definición; [T] identidad o teorema demostrado bajo sus hipótesis; [E] cálculo reproducible; [F] contraejemplo a una inferencia; [A] tarea abierta. **No hay una solución del problema del milenio de Navier–Stokes**. Los resultados matemáticos generales usados aquí son conocidos; la contribución de este suplemento es precisar su interfaz con las preguntas del programa y construir controles adversariales.

## I. Narrativa y ontología [O]

La totalidad contiene relaciones disponibles aunque una configuración todavía no las habite. Una unidad se autorreferencia y constituye cierre propio con un conjunto de relaciones efectivas; no está obligada a agotar toda la totalidad. Cuando aparece una nueva relación, la referencia que normalizó las anteriores debe permitir reconstruirlas y discriminar qué cambió. Desde múltiples configuraciones se observa una estela de escalas. La dirección geométrica es consecuencia de esta organización, no un supuesto rector de la ontología.

El peligro es confundir **continuidad reconstruible de las etiquetas** con **control físico de la magnitud que acompaña las relaciones**. La existencia de una familia de normalizadores \(a^2+b^2+1=N^2\) [O58] es una realización aritmética, pero ninguna ecuación de Navier–Stokes impone que los números de la representación se conviertan en amplitudes físicas o acoten gradientes.

La pregunta O66 es: **¿qué presupuesto dinámico debe controlar una cadena de ocupaciones sucesivas para impedir que sus gradientes crezcan sin límite en un tiempo finito?**

## II. Contrato físico y presupuestos exactos [D/T]

Estudiamos Navier–Stokes clásico, viscoso, incompresible, sin fuerza, en el toro tridimensional fijo \(\mathbb T^3=[0,2\pi)^3\):

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\quad \nabla\cdot u=0,\quad\nu>0.
\tag{66.1}
\]

Sean \(\widehat u_k(t)\) los coeficientes Fourier con normalización de promedio volumétrico. Definimos

\[
e_k(t)=\tfrac12|\widehat u_k(t)|^2,\qquad
\mathcal E(t)=\sum_k e_k(t),\qquad
\mathcal W(t)=\sum_k |k|^2e_k(t)=\tfrac12\langle|\omega|^2\rangle.
\tag{66.2}
\]

La última igualdad requiere \(\nabla\cdot u=0\), y \(\omega=\nabla\times u\). \(\mathcal E\) es energía cinética normalizada y \(\mathcal W\) es enstrofía; **no** representan un número de reflejos ni el resto aritmético 1.

Para umbral físico de frecuencia \(K>0\), defina la energía de la cola

\[
\mathcal E_{\ge K}(t)=\sum_{|k|\ge K}e_k(t).
\tag{66.3}
\]

Sean \(\mathcal N_k=-\mathbb P_k\widehat{(u\cdot\nabla)u}_k\) y

\[
\Pi_K(t)=\sum_{|k|\ge K}\Re\bigl(\widehat u_k^*\cdot\mathcal N_k\bigr),\qquad
\mathcal D_K(t)=2\nu\sum_{|k|\ge K}|k|^2 e_k(t).
\tag{66.4}
\]

La identidad de presupuesto de cola es **exacta para soluciones suaves**, con suma absoluta justificada:

\[
\boxed{\frac{d}{dt}\mathcal E_{\ge K}=\Pi_K-\mathcal D_K.}
\tag{66.5}
\]

\(\Pi_K>0\) denota transferencia **neta de energía hacia frecuencias mayores o iguales a** \(K\); no significa necesariamente creación de modos antes vacíos. Sumado sobre todos los modos, el aporte convectivo neto es cero: el flujo reorganiza energía, mientras la viscosidad la disipa.

## III. Identidad de la estela y la cantidad crítica [T]

### Lema O66-T1: representación por colas

Si \(\mathcal W(t)<\infty\), entonces

\[
\boxed{\mathcal W(t)=\int_0^\infty 2K\,\mathcal E_{\ge K}(t)\,dK.}
\tag{66.6}
\]

**Demostración.** Como \(e_k\ge0\), Tonelli permite intercambiar suma e integral:

\[
\int_0^\infty2K\sum_{|k|\ge K}e_k\,dK
=\sum_ke_k\int_0^{|k|}2K\,dK
=\sum_k|k|^2e_k=\mathcal W.
\]

La ponderación \(2K\) no es una elección decorativa: **aparece necesariamente al reconstruir la norma de un gradiente a partir de las colas de energía**. En el lenguaje del programa, no basta saber que una relación a alta escala está disponible o habitada; importa la escala física a la que aporta magnitud.

### Teorema O66-T2: criterio condicional de presupuesto positivo

Sea \(u\) una solución suave en \([0,T_*)\), con dato inicial suave y de energía finita. Fije \(K_0\ge1\). Suponga que para todo \(T<T_*\) el presupuesto acumulado

\[
\boxed{
\mathcal B_T=\int_0^T\!\int_{K_0}^{\infty}
2K\,[\Pi_K(t)-\mathcal D_K(t)]_+\,dK\,dt
\le B_*<\infty,
}
\tag{66.7}
\]

tiene una cota \(B_*\) **independiente de \(T\)**, donde \([z]_+=\max(z,0)\). Entonces \(\sup_{t<T_*}\mathcal W(t)<\infty\). Si \(T_*<\infty\) fuera el tiempo maximal clásico, esta cota permite continuar la solución más allá de \(T_*\), contradicción. En consecuencia, cualquier solución a la que se pueda imponer esa cota en todos los intervalos finitos conserva regularidad en todos ellos.

**Demostración.** Integrando (66.5),

\[
\mathcal E_{\ge K}(t)\le \mathcal E_{\ge K}(0)
+\int_0^t[\Pi_K(s)-\mathcal D_K(s)]_+ds.
\]

Divida (66.6) en \((0,K_0)\) y \((K_0,\infty)\). En la primera parte, la desigualdad global de energía da \(\mathcal E_{\ge K}(t)\le\mathcal E(0)\), luego su contribución es \(\le K_0^2\mathcal E(0)\). Para la segunda parte, use la desigualdad de cola, Tonelli y (66.7):

\[
\boxed{\mathcal W(t)\le K_0^2\mathcal E(0)
+\int_{K_0}^{\infty}2K\mathcal E_{\ge K}(0)\,dK+B_* .}
\tag{66.8}
\]

La expresión derecha es finita por suavidad inicial. La cota de energía y de enstrofía mantiene \(u\) acotado en \(H^1(\mathbb T^3)\); la teoría estándar de continuación local para soluciones fuertes de Navier–Stokes 3D impide que una solución maximal suave termine en tiempo finito con esa norma acotada. \(\square\)

**Advertencia fundamental.** Este es un **criterio condicional de continuación**, no una cota a priori obtenida de la ecuación para todo dato. La novedad pendiente sería derivar \(B_*\) exclusivamente de \(u_0,\nu\) y condiciones admisibles **sin suponer ya el control de la solución futura**. La identidad (66.6) y la equivalencia entre un presupuesto de cola y control de derivadas son herramientas del análisis de Fourier, no una demostración original de regularidad general.

### Corolario O66-T3: dominio de la entrada neta [T]

Es suficiente encontrar, a partir de condiciones comprobables a priori, funciones no negativas \(g_K(t)\) tales que \(\Pi_K-\mathcal D_K\le g_K\) para todo \(K\ge K_0\), y

\[
\int_0^T\!\int_{K_0}^\infty 2K g_K(t)\,dK\,dt\le C(u_0,\nu,T),
\tag{66.9}
\]

con \(C\) finita para cada \(T<\infty\). **Este es el puente que necesita el programa:** la regla de renovación tendría que implicar algo comparable a (66.9), en lugar de limitarse a conservar denominadores.

La condición estricta \(\Pi_K\le\mathcal D_K\) por encima de un umbral fijo es un caso suficiente particularmente restrictivo. No está demostrada para NS general y puede excluir dinámicas físicamente regulares con transferencia transitoria hacia escalas pequeñas.

## IV. Falsador: total constante no significa vorticidad acotada [F/T]

Para cada \(k\in\mathbb N\), considere en \(\mathbb T^3\):

\[
\boxed{u^{(k)}(x,y,z,t)=\bigl(e^{-\nu k^2t}\sin(ky),0,0\bigr).}
\tag{66.10}
\]

Se trata de una **solución exacta, global, suave y no forzada**: \(\nabla\cdot u=0\), \((u\cdot\nabla)u=0\), \(\partial_tu=\nu\Delta u\). Con promedios espaciales,

\[
\mathcal E^{(k)}(0)=\tfrac14,\quad
\mathcal W^{(k)}(0)=\tfrac14 k^2,\quad
\|\omega^{(k)}(0)\|_\infty=k.
\tag{66.11}
\]

Así, energía igual para todos los \(k\) no implica una cota uniforme de vorticidad. Más aún, la **forma de las proporciones de energía entre los modos ocupados** no distingue el número de onda absoluto si el comparador omite sus etiquetas físicas. En esta familia cada campo *sí es globalmente regular* y la viscosidad hace decrecer sus magnitudes; el ejemplo no construye un blow-up.

Si se asigna externamente a todos los campos el mismo normalizador entero del laboratorio \(a^2+b^2+1=N^2\), eso tampoco puede acotar \(k\): la asignación no tiene todavía una ley dinámica que la conecte con las escalas. Es una refutación de la inferencia basada solamente en etiquetas, no de la ontología.

## V. Falsador de fases: mismas magnitudes espectrales, distinto futuro de cola [E/T]

En un campo periódico solenoidal representado por sumas de senos y cosenos de tres dimensiones, mantenemos **exactamente los módulos de todos los coeficientes Fourier** y cambiamos únicamente el signo (fase) de un componente \(0.13\sin(y+z)\) del componente \(u_x\). La distribución energética modal y la enstrofía inicial son idénticas; el presupuesto inicial de transferencia neta hacia la cola \(|k|\ge1.1\) cambia de signo:

| Preparación | Energía \(\mathcal E(0)\) | Enstrofía \(\mathcal W(0)\) | Transferencia \(\Pi_{1.1}(0)\) | Disipación \(\mathcal D_{1.1}(0)\) | \(\dot{\mathcal E}_{\ge1.1}(0)\) |
|:--|--:|--:|--:|--:|--:|
| Fase + | 0.575375 | 0.594250 | -0.05019375 | 0.00188750 | -0.05208125 |
| Fase − | 0.575375 | 0.594250 | +0.00284625 | 0.00188750 | +0.00095875 |

Las identidades de presupuesto son exactas para el campo trigonométrico de baja frecuencia por cálculo de Fourier. Se reprodujeron mediante producto pseudoespectral y proyección solenoidal en una malla de \(24^3\) puntos; ese tamaño basta para evaluar sin alias relevante los productos de los modos aquí empleados. No se hizo evolución prolongada: los números describen **derivadas iniciales** del PDE, sin afirmar diferencias de estabilidad global.

**Consecuencia lógica:** ni el total energético ni todos los valores \(|\widehat u_k|^2\) bastan para reconstruir \(\Pi_K\). Las fases y la composición no lineal de relaciones importan. La configuración con fase negativa incluso presenta **aumento inicial neto de energía en esa cola**, pese a que la energía global disminuye. La existencia de una totalidad finita no prohíbe esas redistribuciones.

Esta es una correspondencia operacional con «relaciones disponibles pero no habitadas» y con la **novedad no factorizable**, sin afirmar que una fase sea una singularidad ontológica.

## VI. Por qué Pitágoras, el resto uno y las dos curvaturas no cierran la prueba [F/A]

1. La identidad bilateral \(N^2-(N-1)(N+1)=1\) de O40/O44N vale para cualquier entero \(N>1\); no acota automáticamente frecuencias ni gradientes.
2. El contrato más fuerte \(a^2+b^2+1=N^2\) de O58 sigue siendo una hipótesis de representación: **todavía no está confirmada por el autor su equivalencia con la formulación bilateral**, ni demostrada su asignación a un fluido.
3. La estela de ocupación de O60 demuestra extensiones combinatorias compatibles, no una ley de selección física ni un límite temporal a infinitos cambios de escala.
4. Las simetrías de O61–O63 permiten distinguir transferencias y fases a tiempo corto; una expansión de Taylor local no suministra una cota uniforme en una posible cascada prolongada.
5. La tensión superficial de O64/O65 pertenece a un **modelo de interfaz bifásica**. No está incluida como término en (66.1) ni puede importarse sin modificar el problema físico.
6. Un cambio de escala del **espejo observador** no introduce ni elimina magnitud física: una transformación de representación debe reconstruir las normas con su jacobiano y unidades correctas.

## VII. Decisión de investigación: objetivo exacto para O67 [A]

La pregunta ya no es «¿puede continuar una figura?». Es **si la regla de normalización de la unidad establece una cota física verificable sobre la entrada neta de energía hacia la estela de frecuencias altas**.

Contrato de aceptación de una futura afirmación fuerte:

- Definir un normalizador endógeno \(\mathsf N[u]\) con unidades, dominio y ley de actualización extraídos de Navier–Stokes, no escogidos a posteriori.
- Probar que conserva la información necesaria de fase y transferencia —o delimitar las preguntas para las cuales basta una interfaz más económica—, porque los dos estados de la sección V comparten las magnitudes espectrales y responden distinto.
- Derivar una estimación uniforme del presupuesto (66.7) o (66.9), **independiente de la solución futura y de la resolución numérica**, para todos los datos de la clase que se pretenda cubrir.
- Demostrar que tal estimación persiste al abrir arbitrariamente nuevas escalas; incluir el control de energía inicial, vorticidad, viscosidad y límites \(K\to\infty\).
- Contrastar con O53/O62/O63 y con familias exactas de cizallas, sin promover una simulación ni una identidad finita a teorema global.

**Veredicto O66:** Se obtiene una condición suficiente expresada como **presupuesto de acumulación positiva por escalas**, y se muestra con ejemplos por qué los normalizadores puramente aritméticos o energéticos no la implican. **No se ha derivado ese presupuesto desde la ontología ni desde una restricción nueva de la ecuación. Navier–Stokes 3D sigue abierto.**

## VIII. Reproducción y genealogía

- Ejecutar: `python codigo/verificar_o66.py` (requiere NumPy).
- Salida: `resultados/controles.json` con verificaciones de cizalla exacta, balance por modo y por cola, identidad de colas y falsador de fase.
- O53 y O62: anillo y transferencia por bandas; O63: ritmos materiales; O40/O44N/O58: normalizador, restas, aritmética; O59–O61: familias de relaciones y ocupación. O64–O65 pertenecen a la rama bifásica, mantenida como comparación y no condición de Navier–Stokes monofásico.
- No se alteran los documentos ni los ZIP originales. El nuevo ensayo es un suplemento independiente y candidato de integración a la Imagen Total después de revisión.
