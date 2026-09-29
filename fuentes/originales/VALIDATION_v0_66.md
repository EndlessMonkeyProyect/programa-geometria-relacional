# VALIDATION v0.66 — independencia relacional y rango

**Estado:** PASS para las identidades finitas probadas. Los no-go son resultados internos, no afirmaciones sobre física experimental.

## Controles aleatorios

- Regla de cadena: 4000 pruebas, 0 fallos.
- Redundancia `nu=0 iff factoriza`: 16059 pruebas, 0 fallos.
- Identidad `nu=I(c)-D_R`: 16059 pruebas, 0 fallos.
- Cota binaria `0<=nu<=1`: 16059 pruebas, 0 fallos.
- Axiomas de operador de cierre: 4000 pruebas, 0 fallos.

## No-go de intercambio

Ejemplo:

- `s=0011`
- `x=0101`
- `y=0001=s AND x`

Se verifica `y in Cl(s,x)`, `y not in Cl(s)` y `x not in Cl(s,y)`. El intercambio falla.

Una familia explícita de cuatro comparaciones posee conjuntos generadores mínimos por inclusión de tamaños [2, 3].

## Control SAT

Se generaron 120 familias aleatorias de cláusulas 3-CNF para `n=3..8`. En todos los casos se verificó:

\[
I_{clause}\le n.
\]

Fallos: 0.

Esto es además un teorema inmediato de cardinalidad porque las firmas se evalúan sobre `2^n` asignaciones.

## Ejemplos de novedad

```json
{
  "full_independence_x_given_s": {
    "I_before": 1.0,
    "I_c": 1.0,
    "I_joint": 2.0,
    "novelty": 1.0,
    "dependence_deficit": 0.0,
    "determined": false
  },
  "partial_novelty_y_given_s": {
    "I_before": 1.0,
    "I_c": 1.0,
    "I_joint": 1.584962500721156,
    "novelty": 0.5849625007211561,
    "dependence_deficit": 0.4150374992788439,
    "determined": false
  },
  "redundant_y_given_sx": {
    "I_before": 2.0,
    "I_c": 1.0,
    "I_joint": 2.0,
    "novelty": 0.0,
    "dependence_deficit": 1.0,
    "determined": true
  }
}
```
