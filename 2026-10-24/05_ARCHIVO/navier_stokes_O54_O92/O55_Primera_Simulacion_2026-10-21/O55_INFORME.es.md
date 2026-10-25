# O55 — Primera simulación dinámica de la hipótesis O54

**Fecha:** 21 de octubre de 2026. **Estado:** experimento exploratorio reproducible, no demostración de regularidad global de Navier–Stokes.

## La pregunta
¿El desplazamiento del espejo cambia la identidad interna del anillo? ¿Se conserva el comparador perpendicular común bajo transporte material? ¿La evolución de los dos radios puede distinguirse de una mera reescala exterior?

## Condiciones de ensayo
Se resolvió numéricamente la ecuación incomprensible y viscosa, sin fuerza externa, en una caja tridimensional periódica:

\[
\partial_tu + (u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad\nabla\cdot u=0.
\]

El flujo inicial se reconstruyó a partir de vorticidad azimutal gaussiana localizada alrededor de un anillo circular, de radio mayor \(R_0=1.6\) y radio del ducto \(r_0=0.48\), en unidades arbitrarias. La caja tiene longitud de lado 8, viscosidad \(\nu=0.025\), paso temporal \(\Delta t=0.014\) y duración \(t=1.26\). Se comparan dos preparaciones: (A) anillo inicialmente axialmente simétrico y (B) el mismo anillo más un campo inicial divergencia-cero \(u_\mathrm{cizalla}=(0,0.22\sin(2\pi z/8),0)\).

El cálculo emplea transformadas de Fourier, proyección de Leray, eliminación de alias 2/3 e integración explícita de punto medio (RK2). Una superficie material del toro se transporta mediante trazadores para estimar sus radios efectivos. Dos desplazamientos infinitesimales aproximados, inicialmente perpendiculares, se transportan para medir el ángulo. Esos radios **son descriptores efectivos de la superficie transportada**; después de una deformación, no equivalen necesariamente a los parámetros de un toro perfecto.

## El espejo móvil se aplicó como comparación, no como fuerza
La referencia exterior se prescribe, a título ilustrativo, como \(L_\mathrm{ref}(t)=\exp(0.23t)\). Se calculan \(\widehat R=R_\mathrm{eff}/L_\mathrm{ref}\), \(\widehat r=r_\mathrm{eff}/L_\mathrm{ref}\). Por simple álgebra:

\[
\frac{\widehat r}{\widehat R}=\frac{r_\mathrm{eff}}{R_\mathrm{eff}}.
\]

Por tanto, ningún cambio del espejo externo, si se limita a cambiar una unidad común, puede modificar por sí solo la relación interna de los radios. El valor de 0.23 no es una constante física derivada del programa.

## Resultados (resolución 48³)

| Magnitud | Sin perturbación | Con cizalla |
|---|---:|---:|
| \(r/R\) inicial | 0.300000 | 0.300000 |
| \(r_\mathrm{eff}/R_\mathrm{eff}\) final | 0.302151 | 0.303593 |
| Ángulo inicial de direcciones materiales | 90° | 90° |
| Ángulo material final | 90.612° | 80.598° |
| Energía cinética final / inicial | 0.825208 | 0.932651 |
| Máxima divergencia final \(\|\nabla\cdot u\|_\infty\) | 6.9 × 10⁻¹⁸ | 8.5 × 10⁻¹⁸ |
| Desacuerdo máximo entre cocientes interno/externo | 5.6 × 10⁻¹⁷ | 5.6 × 10⁻¹⁷ |

La cizalla introduce energía adicional en la condición inicial: **no comparar los cocientes de energía entre casos como si representaran energías iniciales iguales**. La caída energética en cada caso es consistente con disipación viscosa.

## Control de resolución

| Resolución por lado | Ángulo sin perturbación al final | Ángulo con cizalla al final | \(r/R\) efectivo sin perturbación | \(r/R\) efectivo con cizalla |
|---|---:|---:|---:|---:|
| 32 | 90.955° | 81.796° | 0.302181 | 0.303618 |
| 48 | 90.612° | 80.598° | 0.302151 | 0.303593 |
| 64 | 90.471° | 80.841° | 0.302068 | 0.303512 |

Se conserva la **diferencia cualitativa** entre preparaciones en las tres resoluciones. El desvío de la perpendicularidad en la preparación simétrica no es exactamente cero por la representación cartesiana e interpolación de los trazadores. Los resultados numéricos no pueden interpretarse como una prueba de precisión arbitraria.

## Interpretación dentro de O54

1. **Demostrado algebraicamente:** la reescala del espejo cancela en la razón de dos radios medidos respecto de la misma referencia. Es identidad de representación, no propiedad especial de Navier–Stokes.
2. **Observado en este ensayo numérico:** la deformación interna del flujo modifica la perpendicularidad material y puede modificar los radios efectivos; la simetría inicial la conserva aproximadamente, mientras la perturbación rompe esa preservación.
3. **Relación exacta pertinente:** para dos vectores tangentes materiales \(a,b\), \(D(a\cdot b)/Dt=2a^\top S b\), donde \(S=(\nabla u+(\nabla u)^\top)/2\). Es el término dinámico que O54 necesita controlar.
4. **No demostrado:** que exista una ley físicamente determinada para el múltiplo normalizador \(\mathcal N\); que la novedad de un ciclo sea automáticamente admisible; que mantener el comparador asegure la persistencia indefinida del anillo; o que las soluciones generales de Navier–Stokes sean globalmente regulares.

**Próxima tarea bien delimitada:** derivar del programa una regla verificable de actualización \(\mathcal N_{n+1}=F(\mathcal N_n,\mathrm{estado}_n,\mathrm{novedad}_n)\) sin obtenerla a posteriori de una curva que se quiere explicar. Después, predecir cuándo \(a^\top S b\) debería anularse o quedar acotado y verificarlo en ensayos con distintas perturbaciones y viscosidades. El normalizador todavía no está implementado como campo físico; inventarlo como mero ajuste del dato circularizaría la prueba.

## Reproducción

- Código: `O55_simulacion.py` (requiere Python 3 con NumPy y Matplotlib).
- Resultados completos N=48: `O55_resultados.csv`.
- Gráficas: `O55_graficas.png`.
- Resumen legible por máquina: `O55_resumen.json`.
- Repeticiones con N=32 y 64 disponibles en `convergencia/` del ZIP.

Los resultados son específicos a un dominio periódico, al tiempo corto estudiado, a la preparación gaussiana y al método numérico de baja/moderada resolución. La singularidad del programa se trata como objeto relacional conceptual; el campo de velocidad usado en la simulación es regular y no contiene una singularidad matemática puntual.
