# 7. Dinámica, estabilidad y holonomía

## Economía y movimiento

Un cociente de máxima economía conserva las respuestas declaradas y elimina distinciones irrelevantes. Es idempotente. No determina una trayectoria gradual única: varias fusiones pueden conservar exactamente los mismos invariantes.

La v0.74 introduce accesibilidad y demuestra confluencia de contracciones de aristas ya cerrables en un grafo fijo. Queda separado el proceso que hace disminuir una diferencia inicialmente positiva.

## Dinámica variacional

Con comparaciones lineales fijas \(\partial:X\to Y\), patrón b y defecto

\[
D(x)=\tfrac12\|\partial x-b\|^2,
\]

adoptar descenso de gradiente con \(\kappa>0\) da

\[
\dot x=-\kappa\partial^\ast(\partial x-b).
\]

En estados aparece \(\Gamma_X=\kappa\partial^\ast\partial\); en residuos q = ∂x − b, con b constante, \(\Gamma_Y=\kappa\partial\partial^\ast\). Son operadores en espacios distintos.

El principio de descenso, la métrica y la arquitectura son hipótesis de la realización. El nombre «economía» no los determina por sí solo.

## Persistencia

Un módulo M invariante bajo U tiene cierre resonante exacto si \(U^p|_M=I\). En dimensión finita ese retorno implica potencias acotadas sobre M. Una frecuencia de módulo uno por sí sola no basta: un bloque de Jordan puede crecer.

La estabilidad respecto de un U fijo no prueba robustez frente a cambios de U o acoplamientos externos. La v0.76 distingue correctamente esos regímenes.

## Hodge

Para un complejo explícito, con \(B_1B_2=0\),

\[
\Delta_1=B_1^\top B_1+B_2B_2^\top.
\]

Los modos armónicos satisfacen \(B_1h=0\) y \(B_2^\top h=0\). La dinámica combinada de v0.77 es precisa si el giro interno y Hodge actúan en factores distintos:

\[
\dot a=(\omega I\otimes J-\gamma\Delta_1\otimes I)a.
\]

En cada modo de autovalor λ, la norma tiene factor de decaimiento \(e^{-\gamma\lambda s}\). λ = 0 protege el modo en esa arquitectura; no lo identifica con una partícula.

Un triángulo sin cara tiene un ciclo armónico. Añadir la cara puede eliminarlo. Hace falta una regla que determine cuándo se añade esa relación.

## Fase y holonomía — revisión editorial

Si \(\Delta_{ij}=\theta_i-\theta_j\) para fases globalmente asignadas, la suma sobre un ciclo es cero módulo 2π. Una conexión independiente sobre aristas puede tener holonomía no trivial; no basta reetiquetar diferencias exactas.

Asimismo, imponer \(g_{ik}=g_{jk}g_{ij}\) para todos los pares y caminos con identidades e inversos compatibles fuerza transporte independiente del camino. Para estudiar holonomía, se distingue el transporte compuesto por un camino del vínculo directo, sin identificarlos universalmente.

Otro límite: un flujo h sobre un ciclo no se obtiene necesariamente de diferencias de valores nodales. Los gradientes \(B_1^\top x\) son ortogonales a \(\ker B_1\). Cambiar de variables nodales a cochains generales amplía el espacio; debe declararse.

## Fuentes

- [v0.74](../../fuentes/originales/ECONOMY_IDENTITY_LOCAL_REDUCTION_v0_74.md).
- [v0.75](../../fuentes/originales/PHASE_SYNCHRONIZATION_DYNAMICS_v0_75.md).
- [v0.76](../../fuentes/originales/RESONANT_MODULES_STABLE_CLOSURE_v0_76.md).
- [v0.77](../../fuentes/originales/DERIVED_OPERATOR_HODGE_HARMONICS_v0_77.md).
- [v0.89](../../fuentes/originales/GAMMA_DESDE_ARQUITECTURA_v0_89.md).

Siguiente: [bits, pesos y escalas](08_bits_pesos_escalas.md).
