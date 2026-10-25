# Laboratorio del Cubo de Espejos — auditoría de la escala radial ya calculada
**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 23 de octubre de 2026**

## Pregunta precisa
¿El radio es solo reconstruible a partir de distancias internas, o las relaciones del programa permiten determinarlo mediante una regla dinámica?

## Dictamen
**Sí existen derivaciones matemáticas previas que acoplan radio y dinámica**; no corresponde presentar ese vínculo como una tarea nunca abordada. Hay, sin embargo, que distinguir tres niveles de «determinar»: (i) una escala modal según el comparador y un presupuesto declarados, (ii) su ritmo de evolución bajo una ley dinámica declarada y (iii) la selección única de un radio físico absoluto desde el cierre ontológico sin anclajes no justificados. Los documentos acreditan (i) y (ii) en realizaciones concretas; no certifican todavía (iii) para el protón.

## I. Incertidumbre, radio y frecuencia: documentos del 11 de septiembre
En `incertidumbre_radio_pseudoinversa_v0_1.md` se define el comparador `G=C†C≥0` y se maximiza entropía bajo el presupuesto cuadrático fijo `Q=⟨xᵀGx⟩`. En el subespacio distinguible, la distribución gaussiana resultante tiene covarianza:

\[
\Sigma=\beta^{-1}G^+,
\qquad R_i=\frac{1}{\sqrt{\beta\lambda_i}}
\quad (\lambda_i>0).
\]

En `ritmo_radio_relatividad_relacional_v0_1.md`, una dinámica oscilatoria cuadrática del modelo fija `ω_i²=Γλ_i`. Al combinar ambos resultados:

\[
\boxed{R_i\,\omega_i=\sqrt{\Gamma/\beta}.}
\]

**Resultado exacto condicional:** el radio de incertidumbre y la frecuencia no son parámetros desligados dentro de esta realización. La normalización más simple del radio espectral del segundo documento, `R_i=λ_i^{-1/2}`, da `R_iω_i=√Γ`, sin el factor `β`; son dos convenciones distintas y no deben mezclarse silenciosamente.

**Dependencia pendiente:** `G` incluye longitudes de enlaces o pesos; `β` está fijado por el presupuesto de incertidumbre `Q`, pero ese presupuesto debe seleccionarse o derivarse. Conocer la conectividad sin escala métrica no basta para una longitud dimensional única.

## II. Comprobación específica con la unidad tetraédrica K4
Tomemos el tetraedro representado solo por el grafo completo de cuatro referencias, con todos los enlaces de longitud declarada `a`. Si `C_a` es la matriz de incidencia dividida por `a`, entonces:

\[
G_a=C_a^TC_a=a^{-2}L(K_4),\qquad
\operatorname{spec}G_a=\{0,4/a^2,4/a^2,4/a^2\}.
\]

Para cualquiera de los tres modos distinguibles,

\[
R_i=\frac{a}{2\sqrt\beta},\qquad
\omega_i=\frac{2\sqrt\Gamma}{a},\qquad
R_i\omega_i=\sqrt{\Gamma/\beta}.
\]

**Contraejemplo a la selección absoluta a partir de K4 solo:** `a→s a` deja idéntica la arquitectura de cierre y el producto `R_i ω_i`, pero multiplica el radio por `s`. Necesitamos una regla adicional que determine `a`, `β` o un observable con escala dimensional. Esto **no refuta** la derivación radio–ritmo; identifica su frontera lógica.

## III. Radio endógeno y desplazamiento del espejo: O25 (19 de octubre)
`O25_ESPEJO_MOVIL_Y_RELOJ_DEL_FLUJO.es.md` establece para soluciones suaves y periódicas de Navier–Stokes, con `ω=∇×u`:

\[
A=\int|\omega|^2\,dx,\quad B=\int|\nabla\omega|^2\,dx,\quad
\ell_\omega=\sqrt{A/B},\quad
\frac{\dot\ell_\omega}{\ell_\omega}=\tfrac12(\dot A/A-\dot B/B).
\]

`O25` deriva `dot A` y `dot B` de la ecuación física. Por lo tanto **el flujo determina operativamente la escala del espejo y su tasa instantánea**; no es una longitud arbitraria del observador. Pero es una escala espectral colectiva definida usando el campo de NS existente, no una deducción de que el tetraedro ontológico crea su escala ni una nueva fuerza o solución universal.

## IV. Quinta referencia y escala relativa: O20 (19 de octubre)
Reflexionar un tetraedro regular en cada cara, reunir las cuatro continuaciones y repetir la regla da exactamente `R_j=R_0(5/3)^j`. Queda determinado **cómo cambia** el radio entre etapas bajo ese contrato. No se selecciona la longitud dimensional inicial `R_0` ni se demuestra que esa regla describa el radio del protón.

## V. Puente específico al protón: cuidado con las dos asignaciones
`Programa_relacional_integrado_v1_0.md` (25 de septiembre) distingue de forma expresa dos anclajes físicamente incompatibles bajo una misma interpretación de la masa:

- **A — frecuencia total anclada a masa protónica:** `R_V=4 ħ/(m_p c)≈0.841235640 fm` cuando `ε=4`.
- **B — frecuencia de confinamiento anclada a masa protónica:** `R_V=√15 ħ/(m_p c)≈0.814522906 fm` para `ε=4`.

Ambas fórmulas son calculables dentro de sus supuestos; **no son a la vez la misma predicción física**. La identificación de cualquiera de estos radios relacionales con el radio rms electromagnético de carga es una hipótesis de correspondencia adicional. Un cálculo exacto a partir de masa medida y una fracción postulada no equivale todavía a una selección dinámica del radio desde primeros principios.

## VI. Qué cambia en el Laboratorio del Cubo
La tarea **ya resuelta en los modelos** es exhibir un acoplamiento cuantitativo entre geometría, incertidumbre, escala y ritmo. No debemos volver a proponerla como si no existiese.

La nueva prueba precisa es: **¿el cierre propio y el normalizador que transporta continuidad seleccionan `G`, el presupuesto y la correspondencia física de manera única, o pueden dos realizaciones compatibles con el mismo cierre dar radios físicos diferentes?**

Para evitar una circularidad, no introducir el radio experimental para escoger después `G`, `β`, `Γ`, el anclaje A/B o la profundidad `ε`. Exigir una predicción fijada antes del contraste y distinguir radio espectral, radio de proyección, radio geométrico y radio rms de carga.

### Fuentes examinadas
- `incertidumbre_radio_pseudoinversa_v0_1.md` (11 sep 2026)
- `ritmo_radio_relatividad_relacional_v0_1.md` (11 sep 2026)
- `O25_ESPEJO_MOVIL_Y_RELOJ_DEL_FLUJO.es.md` (19 oct 2026)
- `O20_QUINTA_REFERENCIA_Y_ESPEJO_QUE_CRECE.es.md` (19 oct 2026)
- `Programa_relacional_integrado_v1_0.md` (25 sep 2026)
- `Pasted text.txt`, «Economía mínima de la información como incertidumbre» (3 ago 2026)
- `paper_v5_5_revisado.tex` (mayo 2026)

**Estado:** revisión retrospectiva de resultados previos con comprobación algebraica del ejemplo K4; no implica medición física nueva ni prueba de una teoría de partículas.
