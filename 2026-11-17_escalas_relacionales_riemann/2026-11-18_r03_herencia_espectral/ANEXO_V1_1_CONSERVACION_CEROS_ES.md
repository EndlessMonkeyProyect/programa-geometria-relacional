# Anexo a R–01 / R–02 · Versión 1.1

## Corolario de conservación espectral

**Estado:** consecuencia exacta de la Proposición 1 (§3) de [Las escalas relacionales de la criba (v1.0)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).  
**Fecha:** 18 de noviembre de 2026.  
**Alcance:** conjunto finito de primos `S`; franja abierta `0<Re(s)<1`.

Sea `E_S` la discrepancia definida en R–01/R–02, `F_S=\mathcal M[E_S]` su transformada de Mellin, y `P_S(s)=\prod_{p\in S}(1-p^{-s})`. La identidad publicada es:

\[
F_S(s)=\frac{\zeta(s)}sP_S(s).
\]

**Corolario (R–03, Proposiciones 1 y 2).** En la franja abierta, `F_S` y `ζ` tienen los mismos ceros, con sus multiplicidades, y la normalización `F_S/P_S=ζ/s` es independiente de la referencia finita.

**Justificación:** cada factor `1−p^{-s}` es holomorfo y no nulo en la franja; también lo es `1/s`. La demostración completa y el alcance de la normalización figuran en [R–03 (español)](R03_HERENCIA_Y_LOCALIZACION_ES.md), §§2–3. Este anexo registra el corolario **sin duplicar** las proposiciones del estudio R–03.

**Inserción editorial:** después de la Proposición 1, §3. Añadir en la tabla de resultados: *Conservación de ceros y multiplicidades bajo referencias primas finitas — consecuencia exacta de Mellin; no determina su ubicación.*

**Estado de Riemann:** abierto.

**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**
