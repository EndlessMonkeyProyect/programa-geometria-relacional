# Navier–Stokes — memoria conjunta y migración del residuo

**Estado:** analogía de lenguaje; las identidades locales del programa permanecen, regularidad 3D global **OPEN**.

MF104 muestra en un laboratorio probabilístico que una distinción persistente puede perder intensidad uniforme. MF107 muestra que una interfaz que conoce solamente comparaciones por parejas puede omitir un dato conjunto relevante. En fluidos esto sugiere una **pregunta de diseño de observables**: ¿una interfaz a escala fija preserva el dato conjunto que controla la migración del máximo euleriano y la reentrada del residuo crítico?

Nada en las trazas SU2 suministra una cota para Navier–Stokes. La dinámica de estiramiento, transporte, presión y disipación debe derivarse del PDE; la salida de una partícula material del conjunto de alta vorticidad no controla el supremo sobre **todas** las posiciones.

**Protocolo falsable de un candidato:** escoger interfaz euleriana `I_t` y función de control `F(I_t)` antes de simular; buscar dos campos permitidos con interfaces iguales pero distinta evolución del máximo, o una secuencia de picos en la que la cota uniforme falle por migración. Si existe, la interfaz es insuficiente para el objetivo global.

Referencias de programa: `10_branches/navier_stokes/01_NAVIER_STOKES_CANALES_GEOMETRICOS_v3.tex` y `70_reviews/R59_PROBLEMAS_EN_LENGUAJE_RELACIONAL_ACTUAL.md`.
