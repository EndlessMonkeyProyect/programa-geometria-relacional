# Genealogía de pruebas y regresión — O48

Las pruebas descritas aquí como anteriores se recuperaron del repositorio/conversaciones y sus archivos. No se presentan como controles nuevos de O48 ni se suman al conteo de O48.

| Antecedente | Hallazgo documentado | Qué prueba O48 ahora |
|---|---|---|
| MF-43 | Reloj como fase por actualización y cociente de ritmos; no tiempo absoluto | Sigue siendo compatible: el reloj `s` de escala es una elección operacional |
| MF-86 / MF-97 | Normalización idempotente y suficiencia relativa al contrato futuro | `G` cierra un contrato preciso, no todos los observables del flujo |
| O25 | Escala `ell_omega²=2E/J` y espejo endógeno | O48 prueba evolución exacta de `ell` como varianza espectral de cizalla |
| O39 | `E'=P-nu J` y control de términos de estiramiento | O48 compara la fuente `T(z)` entre dos tríadas con `P` opuesto |
| O41 | Proyección sobre modos cerrada para cizallas, y fase olvidada produce no-go en NS | O48 introduce la función generadora cerrada y un falsador con espectro radial **completo** |
| O42 | Fase triádica y transferencia instantánea de modos | O48 conecta transferencia directamente con `partial_t M(z)` |
| O43E / O44 | Anillo vorticial, fases, simulaciones cortas; ausencia de vuelta material completa | O48 no reclama vuelta material ni tiempo propio |
| O45 | Marco móvil, tres ritmos, gauge y criterio de suficiencia | O48 diferencia reloj de escala de fase material y temporal |
| O46 | `(E,ell)` puede fijar `E'(0)` bajo `P(0)=0` en familia específica | O48 caracteriza una familia completa con función generadora |
| O47 | Misma energía, E, J, fase inicial y distinto `J'`; simulaciones Galerkin 3D cortas | O48 extiende a *cualquier* orden fijo de momentos, y da un ejemplo con la misma función espectral completa pero diferente `E'(0)` |

No se ejecutó de nuevo el conjunto numérico de O47. Sus archivos, resultados y límites quedan conservados; los verificadores O48 son autónomos. Todas las contribuciones a PDE 3D general que necesitarían una cota de regularidad permanecen abiertas.
