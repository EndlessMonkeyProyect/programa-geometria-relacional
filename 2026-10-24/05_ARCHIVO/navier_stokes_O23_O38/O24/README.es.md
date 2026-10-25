# O24-R — Relojes relacionales y flujo incompresible

Suplemento autónomo y exploratorio del Programa de Geometría Relacional, 2026-10-19.

## Qué documenta

- Recupera explícitamente las derivaciones históricas `R_i omega_i = v_*`, con distintas normalizaciones de radio espectral.
- Calcula `n=log2(L/ell)` y las razones de tres tasas (propagativa, advectiva y viscosa).
- Distingue tasa de actualización, frecuencia nominal, fase acumulada y tiempo físico.
- Prueba que `n(t)->infinito` no implica un número infinito de ciclos nominales en el escenario `ell(t)=a sqrt(nu(T-t))`.
- Declara como **abierto** el vínculo con c física, la dinámica de la escala local, regularidad de Navier–Stokes y la rama hiperviscosa O18.

## Cómo reproducir

Python 3 estándar, sin dependencias externas:

```bash
python -B -m unittest discover -v
python -B laboratorio_o24_r.py
```

Las pruebas auditan álgebra, escalamiento y contraejemplos, **no** una DNS ni una demostración de regularidad global.

## Antecedentes

`ritmo_radio_relatividad_relacional_v0_1.md`; `incertidumbre_radio_pseudoinversa_v0_1.md`; `unidad_minima_incertidumbre_por_direccion_v0_1.md`; `MF44B_normalizacion_causal_cierre_global_v1.md`; `navier_stokes__redistribution_v2.pdf`.

La documentación no inventa una versión histórica nueva, no modifica los archivos originales y no declara que la igualdad `v_*=c` haya sido demostrada.
