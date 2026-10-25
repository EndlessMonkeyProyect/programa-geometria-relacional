---
title: 'O63 — Ritmos materiales y relaciones disponibles en el anillo'
subtitle: 'Del pronóstico de transferencia espectral O62 a una firma angular de referencia propia'
author: 'Le Matt Ansatz Di Ego — Programa de Geometría Relacional'
date: '2026-10-21'
status: 'Suplemento independiente: identidades exactas del sistema Galerkin, ensayos finitos y límites explícitos'
parents: ['O40','O45','O53','O58','O59','O60','O61','O62','Imagen Total v3.8.1']
---

# O63 — Los ritmos de los reflejos no se deducen de la sola energía de cada escala

## 0. Resultado central y alcance

**[O] Narrativa del programa, reconstruida de la conversación.** La totalidad contiene relaciones incluso donde ningún reflejo de una unidad las habita. La unidad se autorreferencia mediante relaciones compatibles que puede reconstruir con su normalizador; las direcciones geométricas son una consecuencia de esa construcción, no su presupuesto ontológico. Al desplazarse el espejo exterior, cambia el comparador sin que ello fuerce transformación física del anillo. El múltiplo que normalizó la configuración anterior porta la continuidad representacional hacia una escala nueva; una ocupación nueva puede alterar la familia de continuaciones.

**[T] Resultado matemático del contrato físico elegido.** Los datos originales de O53 tienen **transferencia inicial de energía entre bandas igual a cero**, como mostró O62. Sin embargo, el desfase entre dos trazadores meridianos tiene en general **derivada inicial no nula**. Su valor se deduce de la velocidad material y de la evolución del centro de enstrofía mediante una identidad exacta de diferenciación.

**[E] Contraste computacional.** Reproducción fiel de estados O53 para `N=40,48`, tres preparaciones, `ν=0.025`, ventana `0≤t≤0.08`, RK4 `dt=0.004` en el mismo modelo Galerkin y partículas por interpolación trilineal. Coincidencia con **24** observables archivados de O53 a `9.96×10^-16` como máximo. Se computaron velocidades iniciales de fase sobre 24 azimutes y se distinguió la señal angular de orden 2 de artefactos de retícula de orden 4.

**[F] Lo que no basta.** Las energías por bandas y las curvaturas energéticas de O62 no especifican el desfase de una **marca material anclada** si se omite su ubicación y orientación relativas. Esto se demuestra girando 90° toda la configuración y manteniendo la marca de consulta: el espectro y las curvaturas de bandas coinciden a redondeo, pero el valor local cambia. Cuando se gira también la marca, **el cambio desaparece**. No afirmar que son dos estados físicamente inequivalentes ni que se haya refutado la suficiencia de *todas* las firmas invariantes posibles.

**[A] Abierto.** No se ha identificado el observable físico equivalente al resto entero `1` de O58–O60; tampoco una asignación física obligatoria del siguiente múltiplo, un reloj universal de singularidad, una predicción de fase a tiempos largos desde pocos escalares ni una prueba de estabilidad/regularidad Navier–Stokes 3D.

## 1. Datos del mismo laboratorio, no nuevo anillo

El estado inicial es el de O53, con radio mayor nominal `R=1`, núcleo `a=0.35`, circulación nominal `Γ=6`, dominio periódico `[-π,π)^3` y Fourier–Galerkin truncado con máscara de desaliasado `2/3` sobre retículas de `40³` y `48³`. Las tres preparaciones son control sin perturbación; perturbación solenoidal `ε=0.14`; la misma perturbación con energía inicial ajustada para coincidir con la del control. No se alteran los datos de O53/O62. Los **archivos originales de O53** y la **fuente de O62** están incluidos como fuentes sin editar.

O62 mide para cada banda Fourier su energía `E_B`, la transferencia no lineal `T_B` y la curvatura inicial `Q_B` respecto de Stokes. La simetría inicial implica `T_B(0)=0` para todas las bandas en este contrato. Es una cancelación energética, no ausencia de velocidad o de evolución material.

## 2. El espejo del anillo: dos referentes diferentes

Sean `u(x,t)` la velocidad y `ω=∇×u` la vorticidad de la aproximación Galerkin. Denotemos `w=|ω|²` y `ρ=√(x²+y²)`. Definimos el centro de *enstrofía* usado en O53:

\[
R_c(t)=\frac{\int \rho\,w\,dx}{\int w\,dx},\qquad
Q(t)=\int w(x,t)e^{iz}\,dx,\qquad Z_c(t)=\arg Q(t),\quad Q(t)\ne0.
\tag{63.1}
\]

Estos son observables definidos de **esa** preparación y del centro elegido; no son el foco ontológico demostrado ni un punto material transportado. La convención angular periódica de `Z_c` requiere una rama desenrollada si atraviesa `±π`.

Como \(\dot w=2\omega\cdot\nabla\times\dot u\), se obtiene al derivar las definiciones:

\[
\boxed{\dot R_c=\frac{\int(\rho-R_c)\dot w\,dx}{\int w\,dx},\quad
\dot Z_c=\operatorname{Im}\frac{\dot Q}{Q},\qquad \dot Q=\int\dot w\,e^{iz}\,dx.}
\tag{63.2}
\]

**[T]** Estas fórmulas son identidades algebraico-diferenciales exactas para el estado finito bajo sus hipótesis. La derivada `dot u` se calcula a partir del operador Galerkin O53. No se ajustan a fases observadas a posteriori.

## 3. Fase material y derivada exacta

Tomamos los trazadores materiales originalmente situados en la semirrecta azimutal `φ`, a profundidades radiales exteriores `d=0.12` y `0.26`. Para cada partícula `x_p(t)`, `dot x_p=u(x_p,t)` y `ρ_p=√(x_p²+y_p²)`. Definimos la fase meridiana que O53 mide respecto del centro:

\[
\theta_p(t)=\operatorname{atan2}(z_p(t)-Z_c(t),\rho_p(t)-R_c(t)).\tag{63.3}
\]

La derivada existe mientras el vector respecto del centro no se anule, y satisface

\[
\boxed{\dot\theta_p=\frac{(\rho_p-R_c)(u_z(x_p)-\dot Z_c)-(z_p-Z_c)(\dot\rho_p-\dot R_c)}{(\rho_p-R_c)^2+(z_p-Z_c)^2},\quad
\dot\rho_p=\frac{x_pu_x(x_p)+y_pu_y(x_p)}{\rho_p}.}
\tag{63.4}
\]

El desfase observable del par exterior, medido en vueltas, es

\[
S_\phi(t)=\frac{[\theta_{0.26,\phi}(t)-\theta_{0.12,\phi}(t)]-[\theta_{0.26,\phi}(0)-\theta_{0.12,\phi}(0)]}{2\pi}.
\tag{63.5}
\]

Por tanto, **la predicción local extraída del estado inicial** es

\[
\boxed{S_\phi(t)=v(\phi)t+O(t^2),\quad
v(\phi)=\frac{\dot\theta_{0.26,\phi}(0)-\dot\theta_{0.12,\phi}(0)}{2\pi}.}
\tag{63.6}
\]

Es una fórmula de Taylor local, no una nueva ecuación universal del programa. Las interacciones presentes en `u` pueden producir `v≠0` aun si `T_B(0)=0` en todas las bandas.

### Espejo que cambia sólo la escala

Si un espejo exterior reemplaza simultáneamente los dos desplazamientos meridianos por `(ρ_p-R_c)/L(t)` y `(z_p-Z_c)/L(t)`, con `L(t)>0`, el ángulo (63.3) no cambia: `atan2(y/L,x/L)=atan2(y,x)`. Al derivar, los términos adicionales de `dot L` también cancelan. **Esto es invariancia de representación**, no una ley de conservación dinámica ni una identificación de `L(t)` con el múltiplo aritmético `N`.

## 4. Resultados medidos

Para la configuración perturbada `ε=0.14`, las pendientes iniciales medidas en vueltas por unidad de tiempo son:

| Malla | Marca φ=0° | Marca φ=90° | Diferencia |
|---|---:|---:|---:|
| 40³ | 0.79187149 | 0.19282169 | 0.59904980 |
| 48³ | 0.88766057 | 0.24980060 | 0.63785998 |

Para el control sin perturbación, ambos azimutes coinciden dentro del error numérico: `0.41634030` (N40) y `0.46524865` (N48). En el perturbado con energía igualada, las pendientes son `0.74710666` frente a `0.18192139` (N40), y `0.83749437` frente a `0.23568310` (N48).

La diferencia de amplitudes entre las mallas es apreciable. **No se certifica convergencia del PDE tridimensional** ni precisión de las pendientes a escala continua; el radio del núcleo sigue subresuelto.

### Firma interna sin orientación privilegiada

Para no introducir la dirección exterior como determinante, muestreamos `v(φ)` en 24 azimutes uniformes y definimos:

\[
\boxed{A_2=\left|\frac1{24}\sum_{j=0}^{23}v(\phi_j)e^{-2i\phi_j}\right|,\quad \phi_j=2\pi j/24.}\tag{63.7}
\]

En el modelo y para giros de 90° que preservan la retícula, `A_2` es invariante. Es una medida de **novedad angular de segundo armónico** para este observable, no la unidad cuadrática `1/N²`, ni un nuevo radio primitivo.

| Malla | Control A₂ | Perturbado A₂ | Perturbado, energía igualada A₂ |
|---|---:|---:|---:|
| 40³ | 4.35×10⁻¹⁶ | 0.16323716 | 0.15400929 |
| 48³ | 1.84×10⁻¹⁶ | 0.15703598 | 0.14816108 |

La dispersión angular sin perturbación **no es exactamente cero** en la retícula cúbica; en N40 es 0.05069 y en N48 es 0.00665. Por eso aquí **no** se utiliza su dispersión total como prueba limpia de novedad: se contrasta el armónico segundo, que es nulo en el control por simetría y robusto en estas mallas perturbadas. Un control adicional con mayores resoluciones sigue pendiente.

## 5. Falsador de suficiencia de bandas para una marca fija

Sea `G_2[u]` la lista de energías por bandas y curvaturas `Q_B` de O62 y sea `C[u,x_p]` la derivada de fase de las marcas ancladas en el laboratorio. Giremos el **campo completo** 90° alrededor del eje del anillo, sin mover la marca de consulta. Las seis energías por bandas y las seis curvaturas iniciales se conservan a precisión de máquina (`E_B` error relativo máximo `≤8.1×10⁻16`; `Q_B` absoluto `≤5.6×10⁻17`), pero la pendiente local difiere:

\[
 v_{\rm original}(0)=0.79187149,\quad v_{\rm girado}(0)=0.19282169\qquad(N=40).\tag{63.8}
\]

**[F, limitado a preguntas ancladas]** De esto se concluye que una firma puramente global sin la relación de la marca respecto del campo no determina `v(0)`. **Pero no son dos sistemas físicos no equivalentes:** al girar *también* las marcas, las trayectorias se corresponden punto por punto. Se comprobó numéricamente esa covariancia durante `0≤t≤0.08`, error máximo `1.31×10⁻15` en vueltas. Por tanto, la orientación absoluta no debe elevarse a ontología; la pregunta exige un anclaje relacional explícito.

## 6. ¿Qué predice y qué no predice la derivada inicial?

El pronóstico lineal (63.6) se compara con la evolución O53. Para `N=48`, perturbación sin igualar energía y marca `φ=0°`:

| Tiempo | Taylor inicial | Valor calculado O53 |
|---|---:|---:|
| 0.02 | 0.0177532 | 0.0150412 |
| 0.04 | 0.0355064 | 0.0248139 |
| 0.08 | 0.0710128 | 0.0333747 |

El signo y el origen dinámico del desfase quedan anticipados, pero **la magnitud diverge rápidamente del cálculo**. Este resultado impide llamar a `v(0)` normalizador dinámico suficiente para un intervalo prolongado. Derivadas de orden superior y evolución del comparador son necesarias; exigir una interfaz finita predictiva es un problema separado.

Los 24 observables temporales de `φ=0°` de la integración corta en `N=40,48` reproducen los 24 valores O53 archivados con discrepancia máxima `9.96×10⁻16`. Son comprobaciones de **consistencia con código original**, no experimentos físicos independientes.

## 7. Ontología → continuidad → puente físico, sin salto injustificado

**Relaciones disponibles:** grados de libertad y acoplamientos de la ecuación, que una familia particular puede dejar sin activación para un observable dado. **Relación habitada:** respuesta concreta de la configuración en el observable registrado. **Autorreferencia de unidad:** equivalencia de sus relaciones de comparación, no ocupación total del espacio. **Novedad:** aquí, contenido angular adicional `A₂`, no un número de reflejos contados físicamente. **Continuidad del normalizador:** obligación pendiente de un operador que transporte relaciones admisibles de una configuración a otra; no se ha derivado de `A₂` ni de O62.

Este trabajo **no deriva** `a²+b²+1=N²`, no decide si el resto correcto del programa es esa identidad o `(N-1)(N+1)+1=N²`, ni demuestra que la PDE obligue a conservar un centro unitario desocupado. Tampoco reconstruye el reloj completo de tres fases O45: `Z_c(t)` es posición axial del centro, **no una fase periódica física propia de la singularidad**. El ensayo compara fases de *dos partículas* con una referencia geométrica móvil declarada. Un tercer ritmo exige definir un observable cíclico propio adicional, sin confundirlo con el desplazamiento axial.

### Una siguiente pregunta honesta (O64)

¿Existe una firma objetiva, que se actualice usando únicamente las relaciones anteriores y tenga costo/escala controlados, capaz de pronosticar no sólo `v(φ,0)`, sino su evolución sin conocer todo el campo de Navier–Stokes? Para contrastarlo, buscar estados de anillo con la misma firma candidata de espectro y armónicos angulares, pero distintas continuaciones. Una diferencia futura certificada refutaría la suficiencia de esa firma; si resiste, habría que probar un teorema dinámico y su control multiescala.

## 8. Reproducción y procedencia

Desde la carpeta O63:

```bash
OPENBLAS_NUM_THREADS=1 python codigo/ejecutar_o63.py
python codigo/graficar_o63.py
python codigo/verificar_o63.py
```

Las fuentes O53/O62 y sus datos previos se copian **sin editar** en `fuentes/`. Los ficheros `resultados/*.csv` y `resultados/resumen.json` son generados por `codigo/ejecutar_o63.py`. `graficos/*.png` usa los CSV reproducidos, sin ilustraciones sintéticas. Un manifiesto SHA-256 verifica los archivos del suplemento. No se modifica el ZIP histórico de Imagen Total v3.8.1.

**Estatutos:** [O] formulación ontológica; [T] identidad bajo hipótesis; [E] integración Galerkin finita; [F] falsador delimitado; [A] problema abierto. **Navier–Stokes 3D sigue abierto.**
