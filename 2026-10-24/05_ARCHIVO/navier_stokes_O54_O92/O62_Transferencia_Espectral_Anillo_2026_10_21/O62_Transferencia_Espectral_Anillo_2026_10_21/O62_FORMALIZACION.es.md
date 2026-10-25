---
title: "O62 — Del anillo vorticial O53 al pronóstico de activación de relaciones"
subtitle: "Novedad dinámica de segundo orden, referencia heredada y transferencia entre escalas"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento aditivo; demostración de identidades Galerkin, comparación numérica a corto plazo, puente ontológico condicionado"
parents: ["O40", "O45", "O53", "O54", "O58", "O59", "O60", "O61", "Imagen Total v3.8.1"]
---

# O62 — El anillo contiene relaciones disponibles antes de activarlas

## 0. Resultado principal

**[O — narrativa ontológica del programa]** La totalidad de relaciones existe antes de que cada reflexión la habite. Cada unidad conserva el cierre de su propia referencia. Al avanzar el espejo cambia el ámbito de comparación, no necesariamente la estructura interna. La referencia normalizadora que ya permitió expresar las relaciones debe seguir siendo reconstruible en escalas posteriores; una nueva activación no equivale por sí sola a crear una dimensión. Las direcciones geométricas son expresiones de relaciones ya constituidas, no el antecedente ontológico que se impone para obtenerlas.

**[T — identidad matemática dentro del sistema Galerkin]** En las tres preparaciones **originales** de O53 estudiadas, las transferencias de energía entre bandas son nulas al instante inicial hasta el redondeo, aun cuando la evolución no lineal no lo sea. Esto se explica por la **simetría par bajo inversión espacial** de la velocidad inicial: sus modos Fourier tienen fases reales, mientras la primera contribución convectiva es impar y tiene coeficientes imaginarios. Sin embargo, la segunda derivada espectral distingue preparaciones y permite prever a corto plazo una reorganización de energía entre bandas.

**[E — simulación nueva, con los mismos datos iniciales de O53]** Predicciones de signo basadas **únicamente en el estado inicial** acertaron el signo del desvío respecto de Stokes en 6 bandas, dos tiempos cortos (`0.02`, `0.08`), tres preparaciones y tres mallas (`N=32,40,48`), total `108/108` contrastes. **Esto es una validación local de la expansión de Taylor de la misma PDE discreta, no una ley universal predictiva ni una prueba de regularidad.** La precisión de magnitud disminuye al avanzar el tiempo.

**[A — abierto]** Ninguno de estos cálculos establece una correspondencia obligatoria entre el resto entero `1` de O58–O60 y la distribución continua de energía entre modos. No se ha probado un normalizador relacional finito suficiente para NS 3D ni una condición de conservación de la identidad física de un vórtice.

## 1. Fuente y contrato experimental

Se ha recuperado **el paquete original O53** incorporado en la Imagen Total v3.8.1 a través de la v3.8.0 y v3.7.0. Se almacena sin modificaciones como `fuentes/O53_ORIGINAL_SIN_MODIFICAR.zip`. El código O62 reproduce su perfil inicial y la ecuación Fourier–Galerkin para velocidades, con el fin de analizar presupuestos por banda. No reevalúa aquí los trazadores O53 ni su fase meridiana de largo plazo.

Parámetros originales: dominio periódico `[-π,π)^3`, `ν=0.025`, `R=1`, radio de ducto `a=0.35`, circulación nominal `Γ=6`, operador espectral 2/3 de desaliasado. Perturbación solenoidal de O53 derivada de `curl A`, `A=(0,xg/R,yg/R)`, con perfiles `ε=0`, `ε=0.14`, `ε=0.14` reescalado para igualar energía cinética de la base. O62 integra únicamente `0≤t≤0.08` por RK4 con `dt=0.004`, para `N=32,40,48`.

Se registraron seis bandas **predefinidas** de módulo de índice Fourier: `[0,2)`, `[2,4)`, `[4,6)`, `[6,8)`, `[8,11)` y `[11,∞)`. Se mantienen constantes entre preparaciones. Una banda de índices no es un radio geométrico del toroide: requiere un puente físico específico antes de identificarla con la «estela de escalas» ontológica.

## 2. Relaciones disponibles y relaciones activas: dos definiciones distintas

La velocidad satisface, tras proyectar a campos libres de divergencia, la evolución discreta

\[
\dot{\widehat u}_k=F_k(\widehat u)
=P_k\widehat{(u\times\omega)}_k-\nu |k|^2\widehat u_k,
\quad\omega=\nabla\times u,\quad P_k=I-\frac{kk^\top}{|k|^2}.
\tag{62.1}
\]

La **interacción disponible** está determinada por tríadas `p+q=k` compatibles con el proyector y el recorte espectral. **Transferencia activa** significa que el término proyectado del estado produce una contribución no nula al presupuesto que hemos elegido medir. Se distinguen ocupación de modo (`u_k≠0`) y transferencia de energía (`T_k≠0`).

Para una banda `B`,

\[
E_B(t)=\frac1{2N^6}\sum_{k\in B}|\widehat u_k(t)|^2,
\quad
T_B=\frac1{N^6}\operatorname{Re}\sum_{k\in B}\widehat u_k^*\cdot P_k\widehat{(u\times\omega)}_k,
\quad
D_B=\frac\nu{N^6}\sum_{k\in B}|k|^2|\widehat u_k|^2.
\tag{62.2}
\]

Por diferenciación,

\[
\boxed{\dot E_B=T_B-D_B.}\tag{62.3}
\]

Al sumar las bandas completas, `Σ_B T_B=0` hasta redondeo, que representa redistribución interna sin producción neta de energía por el término convectivo. `Σ_B D_B` es la pérdida viscosa total.

**No interpretar `T_B=0` como ausencia de modos ni de relaciones:** puede haber contribuciones en fase perpendicular a la amplitud que modifican la fase, y pueden cancelarse términos distintos. El criterio de ocupación depende de la pregunta declarada.

## 3. La sorpresa que obliga a cambiar el orden de la prueba

La velocidad original de O53 es par bajo inversión espacial `x→−x` en su instante inicial: la vorticidad generadora es impar y su recuperación solenoidal es par; el potencial vectorial de la perturbación también es impar y su rotacional, par.

Entonces `u(−x,0)=u(x,0)` y `\widehat u_k(0)` son reales. Como `curl u` es impar, `u×curl u` también es impar, y su transformada Fourier es puramente imaginaria. El proyector `P_k` preserva esa paridad. Por consiguiente, para cada índice `k`,

\[
\boxed{\operatorname{Re}\big[\widehat u_k(0)^*\cdot P_k\widehat{(u\times\omega)}_k(0)\big]=0}\tag{62.4}
\]

Y por tanto `T_B(0)=0` para **todas** las bandas, sea con o sin perturbación de O53. Esto es exacto para el modelo de paridad y se confirma en la retícula hasta `≈10^-18` en el total.

**Interpretación importante:** la presencia de las relaciones de transferencia no implica su contribución energética inmediata. La siguiente iteración de la propia dinámica modifica las fases y permite una redistribución que no aparece al mirar sólo el primer instante.

## 4. Segundo orden: pronóstico sin ajustar al resultado

Sea `F=F(uh)` el campo de velocidad temporal Galerkin inicial. Su derivada direccional sobre sí mismo es

\[
F'(u)F=P_\sigma\bigl(F\times\omega+u\times(\nabla\times F)\bigr)+\nu\Delta F.
\tag{62.5}
\]

De `E_B=(1/2)\sum_k|u_k|²/N^6` se deduce exactamente:

\[
\boxed{\ddot E_B(0)=\frac1{N^6}\sum_{k\in B}
\bigl(|\widehat F_k|^2+\operatorname{Re}\widehat u_k^*\cdot\widehat{F'(u)F}_k\bigr).}\tag{62.6}
\]

Tomamos como control **Stokes puro**, que parte del *mismo* estado pero omite el término no lineal:

\[
E^{\mathrm{Stokes}}_B(t)=\frac1{2N^6}\sum_{k\in B}|\widehat u_k(0)|^2e^{-2\nu|k|^2t}.
\tag{62.7}
\]

En cada banda `\dot E_B(0)=\dot E_B^{Stokes}(0)` para los datos O53. Definimos el coeficiente **no lineal** `Q_B=\ddot E_B(0)-\ddot E_B^{Stokes}(0)` y registramos **antes** de integrar:

\[
\boxed{E_B^{NS}(t)-E_B^{\mathrm{Stokes}}(t)
=\tfrac12Q_B t^2+O(t^3).}\tag{62.8}
\]

Si `Q_B>0`, la banda ganará energía *respecto de la difusión sin no linealidad* para tiempos positivos suficientemente pequeños; si `Q_B<0`, perderá. Ninguna de esas proposiciones asegura que su energía absoluta suba ni que aparezca un modo que antes era exactamente nulo.

`Σ_B Q_B≈0` para las tres preparaciones; en O62 el residuo es inferior a `4×10^-16`. Esta compensación exacta al segundo orden significa que el primer efecto neto no lineal es **redistribuir** el total, sin modificarlo al mismo orden en esta clase de datos.

## 5. Comparación ejecutada: predicción anterior frente a evolución

Para `N=48` y la banda `[2,4)`, al tiempo `t=0.08`:

| Estado O53 | `Q_B` inicial | Pronóstico `½Q_B t²` | Diferencia `E_NS−E_Stokes` observada |
|---|---:|---:|---:|
| Sin perturbación | `−0.00388976` | `−1.24472×10^-5` | `−1.31253×10^-5` |
| Perturbación 14 % | `+0.00357643` | `+1.14446×10^-5` | `+6.40140×10^-6` |
| 14 % con energía igualada | `+0.00283393` | `+9.06858×10^-6` | `+5.16096×10^-6` |

El pronóstico **acierta el signo** del cambio en los tres casos; la amplitud cuantitativa deja de ajustarse bien en los perturbados ya a `t=0.08`. A `t=0.02` la aproximación de segundo orden mejora. No se calibró ningún coeficiente al observar el futuro.

Verificación ampliada: 3 mallas `N=32,40,48` × 3 preparaciones × 6 bandas × 2 tiempos = **108** contrastes de signos no triviales, correctos en esta prueba. La coincidencia `N=40/48` del **signo y tendencia** aporta robustez local pero no prueba convergencia a la solución continua ni autoriza extrapolar a `t=2.4`.

La energía inicial `N=40` del control fue `0.0778815660176` frente al registro O53 `0.07788157`, y la del perturbado `0.0874941217582` frente a `0.08749412`. Se comprobó también `N=48`, y la igualación energética del caso de control. Se preserva la genealogía de O53.

## 6. Qué significa para la referencia, el total y la novedad

1. **Total preexistente.** Los índices y las tríadas admisibles existen como estructura matemática antes de que un estado dado transporte energía por ellas. Ésta es una realización limitada de «relaciones disponibles» de O59.
2. **Configuraciones distintas.** Con la misma preparación geométrica del anillo y con energía inicial igualada, cambiar el acoplamiento interno cambia `Q_B`. La diferencia es verificable desde el primer estado completo.
3. **Referencia normalizada.** El presupuesto `Σ_B T_B=0` y las razones `E_B/Σ E_B` proporcionan normalizaciones físicas en este contrato espectral. **No** son el múltiplo entero de O40/O58–O60, ni prueban la igualdad `a²+b²+1=N²`.
4. **Novedad dinámica.** La novedad operacional es un canal de intercambio que pasa de contribución energética nula en el instante inicial a contribución no nula a lo largo de la evolución. No afirmamos que la transferencia deje una cantidad indivisible `1`.
5. **El espejo.** El desplazamiento exterior de O45 no altera por sí mismo `E_B`. Pero las bandas `|k|∈[2,4)` están definidas en el marco periódico físico escogido; una dilatación de coordenadas exige transformar también las etiquetas y sus umbrales, no declarar invariancia de un histograma fijo ante cualquier observador.
6. **La dirección es consecuencia.** El término de acoplamiento posee polarización/direccionalidad porque así expresa Navier–Stokes las relaciones del campo; no lo ponemos como axioma ontológico del programa.

### Contraste crítico con la «unidad pendiente» de O60

En O60 el `1` cuenta una celda de una cuadrícula finita. En O62 una banda almacena amplitudes reales continuas, y las transferencias pueden cambiar de signo. Un mismo presupuesto total admite infinitas distribuciones. El número `1` de O60 **no se obtiene de la conservación de energía**, por lo que no hay derivación legítima de esa identidad discreta desde este cálculo.

## 7. Limitaciones y siguiente pregunta

La ecuación no lineal redistribuye energía, pero controlar el **signo a corto plazo** de una banda no equivale a controlar el estiramiento de vorticidad ni la regularidad de todas las escalas. La prueba usa un anillo periódico moderadamente resuelto y un intervalo pequeño. `O53` observó desfases materiales hasta `2.4`; **no** se ha demostrado una relación predictiva entre `Q_B` y esos desfases. Tampoco se ha identificado un portador físico universal del normalizador aritmético.

**Pregunta O63:** ¿un pronóstico preregistrado de `Q_B` junto con una interfaz de fase y geometría mejora la predicción del *desfase material* de O53 a tiempos largos, sobre datos distintos de los usados para formular la interfaz? De no ser así, acotar el alcance al intercambio espectral local.

## 8. Reproducción

Dependencias: Python 3, `numpy`, `scipy`, `matplotlib` (este último sólo para la gráfica). Ejecutar en la raíz de O62:

```sh
OPENBLAS_NUM_THREADS=1 python codigo/ejecutar_o62.py
python codigo/verificar_o62.py
python codigo/graficar_o62.py
```

Salidas: `resultados/transferencias_y_predicciones.csv`, `resultados/resumen.json`, `graficos/o62_prediccion_banda_2_4.png`, `resultados/ejecucion.log` y `MANIFEST_SHA256.json`.

**Criterios epistemológicos:** `[O]` ontología propuesta; `[T]` identidad exacta en el modelo declarado; `[E]` ensayo numérico; `[A]` puente abierto. No está resuelta la regularidad global de Navier–Stokes 3D. Tampoco se modifica la Imagen Total 3.8.1 ni los paquetes de O53–O61.
