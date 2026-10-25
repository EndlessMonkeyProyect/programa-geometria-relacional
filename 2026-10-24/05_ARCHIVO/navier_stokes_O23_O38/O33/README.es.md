# O33 — Simetría modular y relación común de formas vorticiales

**Le Matt Ansatz Di Ego · Programa de Geometría Relacional · 20 de octubre de 2026**

## Qué se logró

1. Teorema de equivarianza: Navier–Stokes 2D preserva la relación exacta entre dos vorticidades etiquetadas que son imágenes bajo media vuelta cuando el estado total posee esa simetría.
2. Identidad de forma: `Q_B=Q_A`, sin imponer coeficiente de acoplamiento ni confundir fase cuadrupolar con circulación material.
3. Certificado condicional O31–O32: dos concentraciones simétricas anisótropas permanecen distinguibles durante un intervalo a priori computable.
4. Extensión a `m` formas: las fases cuadrupolares guardan diferencias modulares fijas y los momentos globales de orden `k` se anulan cuando `m` no divide `k`; para `m=3`, el cuadrupolo del conjunto puede ser cero mientras cada forma local conserva anisotropía y el tercer momento global no es cero.
5. Refutador: la coincidencia de circulación, centroides relativos, radios y segundo momento de forma no impone simetría ni igualdad futura de ritmos de orientación.

## Reproducción

```bash
python verificar_o33.py
```

El informe `VALIDACION_O33.json` contiene resultados de controles analíticos y de cuadratura. No hay simulación DNS temporal. El ZIP conserva íntegro el suplemento O32 como antecedente, sin editarlo.

## Alcance epistemológico

Todos los teoremas dependen de Navier–Stokes 2D, suavidad, unicidad, positividad para los certificados de concentración y simetría **inicial impuesta**. No hay demostración de creación de simetría, convergencia atractora, fusión, cierre físico espontáneo, regularidad NS 3D, ni equivalencia con `c`.

**Política:** no se modifica la Imagen Total ni el núcleo canónico.
