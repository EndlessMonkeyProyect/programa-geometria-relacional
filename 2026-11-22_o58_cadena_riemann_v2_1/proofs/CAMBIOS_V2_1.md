# Informe de aplicación del dictamen editorial y matemático

**Documento:** De la semilla heredada a la recuperación funcional  
**Versión corregida:** 2.1  
**Fecha:** 22 de noviembre de 2026  
**Estado:** manuscrito de reducción y equivalencia; no prueba incondicional de RH.

## Correcciones aplicadas

| ID | Actuación | Comprobación |
|---|---|---|
| C1 | Se explicita `f_d(x) = {1/(dx)} = 1/(dx)-floor(1/(dx))` y se añade una definición verbal inequívoca de la parte fraccionaria. | Sección 4, ecuación (7). |
| C2 | `M_S := product_{p in S} p`, incluido el caso vacío. | Sección 4, ecuación (8). |
| C3 | `W_infty := closure_{||.||_2}(union_{j>=1} W_j)`. | Corolario 5.2. |
| M1 | Actualización de Pell como igualdad de vectores columna y matriz 2×2; matriz biyectiva módulo p. | Lema 3.2. |
| M2 | Producto `prod_{k=1}^{J-1}(1-eta_k)` y suma sobre el mismo índice k. | Proposición 6.3. |
| M3 | Referencia textual «Lema 6.1», distinguida de «Teorema 6.2». | Sección 9, solicitud de revisión. |
| M4 | Se distingue `d(D)>=C_0/sqrt(log D)` de `Q_j>=C_0^2/log D_j`. | Sección 7.1, ecuación (21). |
| M5 | Factor `mu(M_U)=(-1)^|U|` expreso en la inversión de Möbius. | Lema 4.1. |
| menores | Se explica integrabilidad de `f_d` en L², se explicita el cambio de signo en el espacio lineal, se corrigen referencias y se comprueban encabezados y subtítulos de cuadros. | Secciones 4–9. |

**Aclaración sobre C1, C2, C3 y M1:** el LaTeX de la versión 2.0 ya contenía visualmente la parte fraccionaria, los subíndices, la clausura y la matriz correctos. El diagnóstico de corrupción se originaba, al menos parcialmente, en la extracción automática del PDF. La versión 2.1 refuerza el texto acompañante y la notación para evitar malentendidos de lectura y copia; no convierte una identidad correcta en un teorema nuevo.

## Validación

- Compilación LaTeX por `pdflatex` en dos pasadas: satisfactoria, **9 páginas**.
- Identidades aritméticas y laboratorios finitos: **1.648 controles exactos aprobados**, de acuerdo con `VERIFICAR_CADENA_O58_MOBIUS.py`.
- Contraste bibliográfico: L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Rend. Lincei 14 (2003), Teoremas 1–2, sección 1 y ecuación (1.2), edición académica: https://www.bdim.eu/item?id=RLIN_2003_9_14_1_5_0 .
- Alcance lógico: `RH <=> lim_j U_j=1` es una equivalencia demostrada mediante un teorema clásico y la cadena Pell/Möbius. **No se afirma `lim_j U_j=1` incondicionalmente.**

## Para revisión externa

El núcleo matemático permanece como reducción rigurosa. La condición adicional de recuperación global aritmética aún no está acreditada. La auditoría externa puede concentrarse en la transferencia de escala y en una estimación de ganancias que no introduzca RH como hipótesis.

*Endless Monkey Project / Relational Geometry Program*
