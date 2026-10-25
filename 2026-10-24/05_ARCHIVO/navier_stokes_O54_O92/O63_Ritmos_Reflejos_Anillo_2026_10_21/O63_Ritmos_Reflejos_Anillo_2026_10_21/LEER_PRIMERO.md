# Programa de Geometría Relacional — O63, suplemento aditivo (21 octubre 2026)

**Autoría del programa:** Le Matt Ansatz Di Ego

O63 continúa O62 sobre la **fuente O53 original**, preservando la distinción ontológica: relaciones disponibles, reflejos que las habitan, referencia normalizadora que conserva continuidad y novedad en la configuración. El suplemento evita hacer de la dirección absoluta o de una orientación del observador una premisa del programa.

**Hallazgo:** transferencias de energía iniciales por bandas nulas no implican desfases materiales nulos. La derivada inicial de fase relativa al centro del anillo se calcula exactamente a partir del estado inicial de Galerkin. Una firma angular de segundo orden, independiente del azimut absoluto, aparece en el anillo perturbado (incluso con energía inicial igualada) y permanece nula en el control O53 dentro de las retículas probadas.

**Límites:** el pronóstico lineal pierde precisión más allá de tiempos muy cortos; la retícula cúbica introduce anisotropía; la normalización cuadrática con resto uno no está derivada de Navier–Stokes; las tres fases de O45 no quedan todas realizadas; no hay prueba de regularidad global 3D.

**Archivos:** `O63_FORMALIZACION.es.md` (narrativa→identidades→pruebas→límites), `codigo/` (ejecutar, graficar y verificar), `resultados/` (CSV y JSON), `graficos/` (datos calculados), `fuentes/` (O53 y O62 históricos sin modificar). Ejecución `OPENBLAS_NUM_THREADS=1 python codigo/ejecutar_o63.py` y `python codigo/verificar_o63.py`.

Suplemento independiente. No altera Imagen Total v3.8.1 ni los archivos históricos.
