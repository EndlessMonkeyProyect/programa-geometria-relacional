# O45 — Tiempo relacional, espejo móvil y Navier–Stokes

Suplemento autónomo al Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 20 de octubre de 2026.

## Contenido

- `O45_TIEMPO_ESPEJO_MOVIL_RITMOS_NS_2026-10-20.md`: narrativa ontológica, definiciones, 6 proposiciones cinemáticas/matemáticas, transferencia a NS, límites y falsadores.
- `verificar_O45_espejo_ritmos_NS.py`: diez pruebas ejecutables de transformaciones, fases, transporte, NS transformado y contraejemplos sectoriales.
- `O45_VERIFICACION.json`: resultados de la ejecución.
- `SHA256_MANIFEST.json`: huellas digitales de los tres archivos anteriores.

## Reproducción

`python verificar_O45_espejo_ritmos_NS.py`

Dependencia: NumPy. Los controles numéricos usan un flujo de cizalla suave especial y no demuestran un teorema de regularidad 3D general.

## Fuentes del programa

MF-43; MF-86; MF-97; `Dinámica relacional y emergencia del tiempo`; O24-R; O25; O39; O40; O41; O43-R; O44-N. Este suplemento no sobreescribe el núcleo canónico ni los antecedentes.

## Etiquetado

`[O]` ontología; `[D]` definición; `[T]` consecuencia o teorema dentro de hipótesis declaradas; `[H]` hipótesis; `[A]` abierto; `[F]` falsador.
