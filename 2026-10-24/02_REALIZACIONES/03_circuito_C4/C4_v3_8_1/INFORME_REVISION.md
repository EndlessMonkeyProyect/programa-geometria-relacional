# Auditoría de base e integración — 21 de octubre de 2026

**Base elegida:** Programa de Geometría Relacional v3.8.0-candidata, edición por capas; no es la edición v3.5. Los resultados de esta nota provienen de **nuestra reejecución independiente** sobre los bytes materializados de esa versión. La nueva versión es una capa **aditiva** v3.8.1 sobre la base intacta.

## Identidad y procedencia

- ZIP v3.8.0 preservado byte por byte: `BASE_V3_8_0_INTACTA.zip`, **37,418,017 bytes**.
- SHA-256 de v3.8.0: `0250f182aa81da18dfecbeefe88afb565f13ae10bf9253c0986e2d0940ef1aab`.
- El archivo contiene una copia histórica de **v3.7.0**, cuya huella interna acreditada es `cc3bf8af408600ea1a8beb82740cc52525d60cc73189ab99edc58a19a4c9af91` y cuyos **1.476 archivos** se comprobaron mediante su mapa.
- Estado: versión **candidata**, no depósito publicado ni versión remota de GitHub alterada.

## Qué se ejecutó y qué pasó

| Control independiente | Resultado |
|---|---|
| Lectura completa ZIP v3.8.0, prueba CRC | **PASS** |
| Manifiesto v3.8.0 | **PASS, 36 archivos sin discrepancias** |
| Archivo histórico v3.7.0 y mapa de procedencia | **PASS, 1.476 archivos** |
| Registro de afirmaciones | **PASS, 37 fichas** |
| Enlaces y tablas generadas | **PASS, sin diferencias** |
| 13 controles exactos del editor | **13/13 PASS** |
| 22 suites heredadas, ejecutadas en esta revisión | **22/22 PASS** |
| Pruebas heredadas | **693 PASS, 0 FAIL** |
| Subpruebas | **993 PASS, 0 FAIL** |
| Verificaciones exactas nuevas C4/grafos/XOR | **PASS** |

Entorno: **Python 3.13.5**, Linux-6.18.55-x86_64-with-glibc2.41; dependencias principales `{'pytest': '9.0.2', 'numpy': '2.3.5', 'scipy': '1.17.0', 'pandas': '2.2.3', 'networkx': '3.6.1'}`; duración de `--perfil completo`: **94.065 s**. La salida íntegra, incluyendo las suites, queda en `04_auditoria/resultado_completo.json`. La de perfil rápido en `04_auditoria/resultado_rapido.json`.

## Lectura crítica del programa existente

1. La v3.8.0 ya incorpora, en cinco capas, una narrativa ontológica seguida de contratos y revisiones, y mantiene la distinción entre incertidumbre y azar. Sigue preservando la **pareja valor/referencia normalizadora** como continuidad, el foco **interno**, y los términos **comunes/trama/cierre propio**.
2. La edición es **integral en el sentido documental**, no significa que se hayan demostrado todos los puentes. Sus 37 fichas representan una selección; los 170 registros históricos de procedencia no son 170 teoremas validados.
3. C4 concreta una regla de compensación direccional en un modelo euclidiano fijo. **No** demuestra por sí mismo el nacimiento de la cardinalidad en cuatro desde la reflexión originaria, ni impone cierres en 8, 12 y 16.
4. La propuesta del «cristal directo» se materializa en un laboratorio de vínculos: ruta, ausencia certificable de ruta, independencia y contradicción. El certificado negativo **sí** se establece en grafos explícitos; **no** se transfiere sin más a cualquier instancia NP-completa.
5. No se cambiaron experimentos de física, documentos externos, licencia ni historia. Las referencias bibliográficas son cotejos aportados por los asistentes y no la fuente de las reglas originales del programa.

## Límites honestos de esta auditoría

La reejecución de las suites no reproduce las campañas de alta resolución O53, N=256 ni ensambles pesados. Algunos tests verifican datos guardados o instancias pequeñas. El perfil PASS **certifica esas ejecuciones concretas**, no una prueba formal total de las matemáticas, una corroboración experimental física, ni una resolución de P versus NP, Navier–Stokes o Yang–Mills. No se verificó ninguna eventual versión de repositorio remoto posterior.

## Decisión editorial

Aprobar la **v3.8.0 como base de trabajo trazable y reproducible para las pruebas cubiertas**. Integrar el ensayo C4 y los certificados de vínculos mediante la capa v3.8.1 sin sustituir los originales. Antes de ascender la idea de raíz por confluencia y el puente a P=NP, exigir el discriminante geométrico sin numeración impuesta y un algoritmo uniforme con contabilidad de costo polinómico total para una familia NP-completa.
