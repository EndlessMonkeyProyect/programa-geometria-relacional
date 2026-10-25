# 04. Yang–Mills: algebra no abeliana, escalas, coercividad y O38

## A. Qué existe [T condicional]

En el modelo finito de `SU(2)`, `Q8` distingue la no conmutatividad al componer. Con `U,V∈SU(2)` se define el observable:

`ν(U,V)=1−(1/2)ReTr(UVU⁻¹V⁻¹)=(1/4)||UV−VU||_F²`.

Es gauge-invariante bajo conjugación común del par. El descriptor reticular `N_a=Σ_{p,q}w_{pq}ν(U_p,U_q)` recoge ciertas incompatibilidades locales; **se anula sobre pares de holonomías conmutativas/Cartan**. El sector abeliano es control adversarial obligatorio.

## B. O17-G: medida y continuo [E; NO TEORÉMA DE CONTINUO]

`20_nu_en_el_continuo_YM_2026_10_19/` presenta un ensayo prerregistrado de tres espaciados y tamaños físicos aproximados. El observable crudo de plaqueta es sensible a la red; observables suavizados a escala fija exhiben estabilidad para varios tamaños, con sistemáticos de interpolación y volumen. Eso **no es una demostración matemática del límite continuo** ni un mass gap. Ver `START_HERE_3_5_5.es.md` y el propio informe O17-G; no sustituir medición por teorema.

## C. Distinción nueva de O38 [N, A]

O38 demuestra una transición topográfica de vorticidad 2D. La **misma transición** ocurre en el semigrupo del calor sobre ℝ², mientras `−νΔ` tiene espectro `[0,∞)` en `L²(ℝ²)` y carece de brecha positiva. Por tanto:

`cambio de foco geométrico ↛ mass gap`.

El experimento Yang–Mills inspirado en O38 puede explorar focos intrínsecos mediante densidad de acción gauge-invariante `s_x(U)=Σ_{p∋x}(1−½ReTr U_p)`, a lo largo de flujo de gradiente/Wilson. **Ese flujo de suavizado no es la evolución cuántica temporal** cuyo espectro fija el mass gap. El paralelo geométrico es **hipótesis de laboratorio**, no identidad física probada.

## D. Problema que realmente falta [A]

Construir una forma relacional sobre funciones físicas gauge-invariantes, `D_rel[f]`, y acreditar que `ker D_rel` consta solo de constantes; después probar una desigualdad uniforme:

`Var_ρ(f)≤C_rel D_rel[f]`.

Luego construir un **puente físico sin circularidad** a la forma de Dirichlet/Hamiltoniano de Yang–Mills y conservar una cota positiva al retirar corte y volumen, junto con existencia axiomática de la teoría continua. Ni el observable ν ni una transición geométrica de O38 entregan por sí solos ese puente.

## E. Control constructivo propuesto

1. Declarar red `SU(2)` pequeña, variables, transformaciones gauge, medida y base de observables (p.ej. trazas de lazos y productos de trazas).
2. Definir comparadores locales independientes del espectro buscado.
3. Hallar explícitamente el núcleo sobre el sector gauge-invariante; **buscar** funciones no constantes invisibles.
4. Verificar sectores Cartan, abeliano `U(1)`, centro trivial y una secuencia de refinamiento de red.
5. Solo si el núcleo se reduce a constantes, estudiar coercividad cuantitativa y **puente** a Hamiltoniano físico.
6. Probar que constantes relevantes sobreviven a `a→0`, `L→∞` sin fijar el gap de antemano.

Esta es la obligación central heredada del hilo consolidado `06_yang_mills/` y la sección YM del V5.9 preservado. No se reclama solución al problema de Clay.
