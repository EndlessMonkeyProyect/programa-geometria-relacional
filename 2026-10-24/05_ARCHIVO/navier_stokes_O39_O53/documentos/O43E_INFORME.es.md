# O43E — La vuelta, el resto y la suficiencia del comparador: auditoría temporal

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 20 octubre 2026**

**Estado epistemológico:** [O] ontología reconstruida; [T] teorema algebraico/cinemático; [E] evidencia numérica reproducible de una truncación Galerkin de Navier–Stokes 3D; [A] puente físico abierto; [F] controles adversariales. **No hay resultado de regularidad global, singularidad de Navier–Stokes, reconexión ni fragmentación.** Suplemento independiente de O39–O43R y de Imagen Total v3.6.0.

## 0. Discurso y ontología [O]

La identidad no es un objeto que queda estático dentro del toroide. Las relaciones entre los dos radios, el movimiento local, la referencia compartida y las diferencias que se incorporan pueden redefinirse mientras el flujo avanza. El «uno pendiente» es una fracción referenciada en la normalización; permite continuar la comparación al siguiente ciclo y no equivale por sí mismo a una sustancia, a un material conservado ni a una magnitud física medible. **El cierre en sí exige suficiencia de las relaciones, no identidad de la forma.**

**Discriminante:** distinguir (i) el estado final del resto, (ii) las relaciones recorridas durante el ciclo y (iii) las variables necesarias para predecir el siguiente ciclo. No son automáticamente equivalentes.

## 1. Un teorema exacto sobre insuficiencia del resto final [T]

Sea `rho(t)` un resto de fase continuo, con valores en [0,1], sobre `0 <= t <= T`. Compare dos historias:

\[
\rho_A(t)=0,\qquad \rho_B(t)=\frac12\sin^2\!\left(\frac{\pi t}{T}\right).
\]

Comparten exactamente extremos: `rho_A(0)=rho_A(T)=rho_B(0)=rho_B(T)=0`. Sin embargo, el funcional de historia 

\[
J[\rho]=\int_0^T |\dot\rho(t)|^2\,dt
\]

satisface

\[
\boxed{J[\rho_A]=0,\qquad J[\rho_B]=\frac{\pi^2}{8T}>0.}
\]

**Derivación:** `dot rho_B=(pi/(2T))sin(2pi t/T)` y la media temporal de `sin²` sobre un ciclo es `1/2`.

Este es un **contraejemplo puramente cinemático** a que el resto final determine la historia o su costo acumulado. `J` no es por definición enstrofía ni disipación de Navier–Stokes: exigir tal identificación sin derivación sería circular.

## 2. Ensayo NS 3D: qué se comparó realmente [E]

Domino periódico `T³` de longitud `2pi`, viscosidad `nu=0.03`, campo suave y solenoidal mediante Biot–Savart e integración pseudospectral proyectada con filtrado 2/3 y Runge–Kutta de orden cuatro. Se usa vorticidad inicial concentrada en una vecindad de un **anillo curvado** nominal de radio mayor `R=1.65` y radio transversal `a=0.39`. Ambos casos tienen idénticos `R,a` prescritos.

Se construye una vorticidad azimutal candidata proporcional a un factor gaussiano transversal multiplicado por

\[
1+0.20\cos\varphi+0.12\cos(2\varphi)\;\boldsymbol{\pm}\;0.10\cos(3\varphi).
\]

La proyección de Helmholtz sobre campos solenoidales y la inversión Biot–Savart producen datos `u_+(0)` y `u_-(0)` de Navier–Stokes 3D. El signo de la tercera componente cambia su **fase relativa 3:1**, mientras la fase relativa 2:1 es prácticamente igual. El normalizador de los números de onda espaciales `1,2,3` es idéntico (`mcm=6`). **Son números de onda espaciales, no velocidades poloidales de partículas ni relojes físicos sincronizados.**

Un ajuste de mínimos cuadrados de los modos angulares sobre una corona declarada separa la fase 3:1 de la 2:1 sin contaminarla con la cuadrícula cartesiana. Se mide el estiramiento global `P=<omega · (omega·nabla)u>`; disipación `D=nu<|nabla omega|²>` y enstrofía `E=<|omega|²>/2`, con la identidad exacta `E'=P-D` para el problema periódico continuo. `P_front` es el aporte a `P` en el semiespacio `x>0`, relativo a la orientación fijada de los armónicos.

**Limitación comparativa:** las amplitudes angulares prescritas son iguales en módulo, pero la proyección numérica, el dominio cuadrado periódico y las diferencias de distribución angular producen una pequeña diferencia inicial de enstrofía de aproximadamente `0.026%`. Los radios efectivos obtenidos por momentos de vorticidad tampoco son idénticos, y esos momentos no son exactamente los radios geométricos del tubo. Por ello **no se puede atribuir en exclusiva a la fase todo cambio observado**. La comparación es controlada a nivel de parámetros prescritos y auditada, pero no una pareja de datos idénticos en todos los invariantes.

## 3. Observaciones en t=0.12 [E]

Resolución espacial `64³`, paso `dt=0.005`; parámetros adimensionales del experimento.

| Observable | Fase 3:1 positiva | Fase 3:1 opuesta |
|---|---:|---:|
| Enstrofía inicial `E(0)` | 0.010229325 | 0.010231990 |
| Enstrofía final `E(T)` | 0.009737247 | 0.009739914 |
| Producción global `P(T)` | 0.00000484333 | 0.00000488461 |
| Disipación total `D(T)` | 0.003915766 | 0.003915773 |
| Estiramiento localizado `P_front(T)` | 0.00000209885 | −0.00000005486 |
| Fase 2:1 al final | aproximadamente 0 | aproximadamente 0 |
| Fase 3:1 al final | aproximadamente 0 | aproximadamente ±π |

La producción total difiere poco: alrededor de `0.85%` del valor de referencia. La enstrofía decrece alrededor de `4.8%` en ambos casos. La disipación domina ampliamente el estiramiento global; no se observa crecimiento explosivo ni ruptura. La diferencia localizada es mucho más marcada. **La inferencia defendible es que el comparador fase 2:1 + dos radios prescritos no determina por sí solo la distribución espacial del estiramiento.**

**Controles:** comparar `48³` con `64³` estabiliza `E,P,D` y la distinción espacial; halving `dt=0.005→0.0025` en `48³` no cambia las cifras principales; balance temporal de enstrofía conciliado con error de integración por trapecios menor que `1.6×10^-8`, valor dominado por interpolación temporal en los registros, no un error de PDE certificado. Divergencia solenoidal bajo umbral `10^-12`. Se repite control breve `nu=0` a `32³`: persisten diferencias de estiramiento local. Esto prueba que las diferencias observadas no se deben **exclusivamente** a viscosidad, aunque no establece mecanismos universales.

## 4. Qué NO demuestra la simulación [A]

1. **No hay dos trayectorias materiales seguidas durante una vuelta completa** del toroide ni un verdadero mapa de retorno de Poincaré material. La frase previa «dos campos con el mismo resto final» **no quedó demostrada por este ensayo**; queda corregida explícitamente. Los campos tienen fase 2:1 esencialmente igual y distinta información de un tercer modo, lo cual es una pregunta diferente.
2. No se ha demostrado equivalencia exacta de todos los observables gruesos entre ambos datos; como muestran los valores iniciales, la energía vorticial es próxima pero no idéntica.
3. No hay una secuencia de cierre o ruptura geométrica observada, y por tanto ningún umbral de pérdida de cierre ha sido medido.
4. Una diferencia local en `P` no equivale a una diferencia local en evolución de `E` sin incluir advección y difusión por la frontera de la región.
5. El término angular `delta_{m:1}` es una fase relativa de armónicos espaciales; no constituye automáticamente la **fracción `1/N` heredada entre vueltas materiales** del discurso ontológico.
6. Una dinámica truncada en resolución finita durante `T=0.12` no controla el límite continuo ni los tiempos arbitrariamente largos de NS 3D.

## 5. Decisión sobre el cierre propio [O/E/A]

**Teorema matemático:** el estado final de un resto modular no determina por sí solo el costo de la historia.

**Resultado NS limitado:** un comparador de radios prescritos y fase 2:1 no determina la distribución de estiramiento local en una familia concreta de datos iniciales porque una relación de fase adicional afecta la evolución. La respuesta global, en esta clase, resulta mucho menos sensible.

**Siguiente obligación física no resuelta:** definir un verdadero retorno material sobre una sección transversal del toroide; si las trayectorias poloidales no realizan el retorno requerido, el observable debe declararse indefinido, no fabricarse. Medir el resto material `rho`, separar su historia de `delta_{m:1}`, y demostrar si el conjunto de ambos permite predicción del estiramiento o del intercambio con la escala siguiente. Después buscar un criterio de estabilidad no circular. **No es lícito afirmar que esta familia evita singularidades.**

## 6. Reproducción

`python verificar_O43E.py --N 48 --T .12 --dt .005 --out resultados_N48.json`

`python verificar_O43E.py --N 64 --T .12 --dt .005 --out resultados_N64.json`

`python VERIFICACION_O43E.py`

Requiere Python 3 y NumPy. El archivo `VERIFICACION_O43E.py` realiza las comprobaciones numéricas declaradas; los JSON registran la trayectoria diagnóstica. El modelo no pretende ser DNS de alta resolución y el tratamiento periódico no representa una interfase aire–agua ni tensión superficial.
