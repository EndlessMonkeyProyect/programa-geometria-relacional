# Traducción histórica y contratos de tipos

**Le Matt Ansatz Di Ego · Integración 3.1**

Una misma letra cambia de función entre versiones. Esta tabla permite recuperar
una idea histórica sin cambiar el significado de la notación vigente.
Complementa el [lenguaje canónico](canonical_relational_language.es.md).

| Fuente o realización | Notación de esta edición | Tipo y condición |
|---|---|---|
| Razón de frecuencia UnHz | $a_V=\omega_V/\omega_U$ | Amplitud adimensional, con frecuencias positivas |
| Peso modal cuadrático | $r_V^{\rm freq}=a_V^2$ | Peso, bajo partición ortogonal declarada |
| Razón complementaria | $\mu=\omega_m/\omega_V$ | Cociente adimensional; requiere $\omega_V>0$ |
| Proyección de probabilidades | $r_{\rm ref}=1/(NC_2(p))$ | Peso geométrico con métrica euclídea |
| Radio de frecuencia | $\ell_V=c/\omega_V$ | Longitud si $c$ es una velocidad y $\omega_V$ una frecuencia angular |
| Radio de carga | $r_{\rm rms}=\sqrt{\langle r^2\rangle}$ | Observable con distribución y procedimiento de medida |
| Descriptor de bloque d | $d_{\rm balance}=1-\lvert N_d-5\rvert/5$ | Coordenada de ocupación suministrada, sin unidad |
| Novedad aritmética | $\operatorname{ord}_p(2)=h$ | Primer exponente de aparición del primo |
| Novedad de una ruta | Primo ausente del registro visitado | Propiedad del recorrido, no del nivel |

Si se adopta $\omega_U^2=\omega_V^2+\omega_m^2$, entonces

$$
\mu^2=\frac{1-a_V^2}{a_V^2}
=\frac{1-r_V^{\rm freq}}{r_V^{\rm freq}}.
$$

Si además $r_V^{\rm freq}=2^{-q}$, se obtiene $\mu^2=2^q-1$.
Esto es una consecuencia de dos postulados, no evidencia independiente de
una selección física. Para $a_V=1/4$, el peso es $1/16$ y $\mu^2=15$.
Usar $1/4$ como peso cambiaría el resultado.

## Momento, radio y energía

El momento lineal, el momento angular y la acción son tipos distintos. Si $L$ es momento angular y $R$ longitud, $L/R$ tiene unidades de momento lineal. La [traducción a energía](../publication/momentum_radius_and_energy.es.md) declara los puentes que permiten $E_0=cL/R$. Cuantificar un radio respecto de una referencia no implica por sí solo seleccionar valores discretos; tampoco identifica un radio espectral, uno de frecuencia y uno de carga.

## Generación y partición

Los operadores de generación pueden actuar en un espacio distinto del de la
partición modal. En esta última $U=V+m$ y $V\perp m$ son compatibles con
$\|U\|^2=\|V\|^2+\|m\|^2$. Añadir $U\perp V$ en el mismo producto interno
positivo forzaría $V=0$. La separación de tipos de MF108, ya recogida por la
v3, evita trasladar relaciones de un espacio al otro sin un mapa.

Las denominaciones históricas «Forma A» y «calibración A» tampoco se identifican
por su letra. Cada correspondencia debe escribir qué frecuencia se vincula
con qué masa. Las alternativas y el estado experimental permanecen en
[puentes físicos](../publication/physical_bridges.es.md) y
[radio protónico](../publication/proton_radius_hypothesis.es.md).

## Estado probabilístico y estado cuántico

El vector uniforme de amplitudes es un estado puro; la densidad $I/N$ es de
máxima mezcla. La coincidencia de probabilidades de una medición concreta no
los identifica. Asimismo $2uu^{\mathsf T}-I$ es una reflexión ortogonal del
espacio de comparación, pero puede sacar un vector del simplex:

$$
(1,0,0,0)\longmapsto(-1/2,1/2,1/2,1/2).
$$

La propiedad de preservar estados exige un contrato adicional. La
[nota de resolución](../02_formal_core/resolution_and_modal_weights.es.md)
declara por separado probabilidades, amplitudes y operadores densidad.

## Protocolo de fase recuperado, pendiente de datos

El informe histórico de UE sugiere comparar una diferencia de fase mediante
la longitud candidata $R_\phi=(c/\omega)\lvert\Delta\phi\rvert$.
Antes de usarla se debe declarar si la fase está envuelta o desenvuelta,
la referencia, el muestreo y el observable que se pretende representar.
No se identifica automáticamente con un radio de carga.

Para dos preparaciones con iguales $c,\omega$ y fases centradas, definir
$\beta=\operatorname{Var}(\Delta\phi)_2/
\operatorname{Var}(\Delta\phi)_1$ da
$R_{\phi,\mathrm{rms},2}/R_{\phi,\mathrm{rms},1}=\sqrt{\beta}$,
si el denominador es positivo. Sin centrado deben usarse los segundos
momentos, que incluyen el cuadrado de la media. La coherencia temporal es
otra cantidad y necesita su propia función de correlación.

Esta edición conserva el protocolo como propuesta sin un dataset validado.
Las referencias opacas del informe antiguo no se convierten en citas
experimentales: hacen falta fuentes primarias recuperables y predicciones
fijadas antes de evaluar los datos.

## Cómo incorporar un pasaje antiguo

Identificar primero estado, espacio, métrica, unidades, operación y observable.
Luego traducir los símbolos y conservar la condición que hace válida cada
igualdad. Si no hay correspondencia suficiente, registrar la propuesta como
pregunta abierta. El [mapa de integración](../publication/UPDATE_3_1.md) y las
[huellas de fuentes](../references/INTEGRATION_3_1_SOURCES.json) permiten volver
al documento concreto sin importar toda la conversación al árbol público.
