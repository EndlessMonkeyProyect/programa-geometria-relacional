# Nota técnica: referencia, composición, residuo y control de escala

Entrega fechada el **22 de noviembre de 2026**, organizada para revisión matemática y eventual incorporación al repositorio público. Contiene una nota formal en español, un verificador estándar de Python, un reporte de la ejecución y un manifiesto SHA-256.

**Documento:** `MARCO_COMUN_ES.md`. Contiene siete proposiciones con demostraciones, una tabla de procedencia y la condición equivalente de RH expresada en acarreos ponderados. **Estado de la hipótesis de Riemann:** abierto. **Estados de P frente a NP y Yang–Mills:** abiertos.

**Control:** ejecutar `python3 verificar_marco.py` para obtener el reporte de pruebas acotadas. Se emplean exclusivamente módulos de la biblioteca estándar. El script no sustituye demostraciones para cuantificadores infinitos.

**Ruta de integración sugerida** (carpeta nueva, sin modificar archivos anteriores):

`2026-11-22_referencia_composicion_residuo/`

**Texto sugerido para PR:** «Se incorpora una comparación formal entre contratos de continuación, acarreos modulares y defectos de conmutación en SU(2). Se presentan siete proposiciones demostradas, con una identidad aritmética exacta y un criterio de RH como reformulación de una cota abierta. La nota distingue las hipótesis específicas de cada dominio y añade verificaciones finitas reproducibles».

**Control de integridad:** desde la carpeta, `sha256sum -c MANIFEST.sha256` en Linux/macOS; en Windows puede ejecutarse `python3 verificar_integridad.py`. Ninguna ruta escrita en la nota implica que esta entrega esté publicada: el paquete se entrega localmente.

Endless Monkey Project / Relational Geometry Program
