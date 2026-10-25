# O71 — Semilla colectiva, interacción residual y memoria de tercer orden

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego — 21/10/2026**

**Hallazgo principal.** Dos anillos con la misma referencia colectiva, el mismo tensor residual de segundo orden, la misma primera derivada de referencia, radios estadísticos iguales y dos frecuencias de modos comunes idénticas pueden tener **segundas derivadas colectivas distintas**. Es la diferencia en cómo evoluciona la relación omitida, visible en el término cúbico de la ecuación exacta.

Leer primero `O71_FORMALIZACION.es.md`, después `resultados/resumen.json` y `graficos`. Para reproducir desde el directorio principal del ZIP:

```bash
python codigo/experimento_o71.py
python codigo/graficar_o71.py
```

Requisitos: `numpy`, `scipy`, `matplotlib`. Los fuentes necesarios O53→O70 están incluidos. Pruebas: **39/39** en 32³, 40³, 48³. Modo espectral: filtro estricto `|k_j|<N/3` para evitar alias de borde N=48. No hay solución de Navier–Stokes general ni prueba de convergencia al PDE continuo.

**Criterio epistemológico:** [O] ontología; [N] narrativa; [D]/[T] identidades y demostraciones; [E] experimentos discretizados; [A] advertencias y límites; [H] hipótesis futuras.

El paquete es **aditivo**. No reemplaza la Imagen Total ni reescribe O68–O70.
