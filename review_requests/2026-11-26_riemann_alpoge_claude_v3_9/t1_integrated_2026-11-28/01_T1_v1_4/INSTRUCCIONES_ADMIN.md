# Instrucciones para administración / Codex

Repositorio de referencia: https://github.com/EndlessMonkeyProyect/programa-geometria-relacional  
Expediente de revisión: https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/16

## Tarea

Incorporar el Anexo T.1 v1.4 como extensión versionada de la Nota técnica 01 v3.9. Mantener la genealogía documental y los archivos publicados de v1.2 y v1.3. La carpeta de destino debe ajustarse a la estructura real del repositorio, previa inspección; si no existe un directorio equivalente, proponer `anexos/T1/v1.4/` sin mover otros archivos.

1. Examinar el estado del repositorio (`git status`, ramas, documentación e índice del expediente). Evitar sobrescribir cambios ajenos. Cotejar la v1.3 publicada con el antecedente del PR.
2. Verificar el manifiesto del ZIP y ejecutar los dos verificadores en una copia de trabajo. Registrar versiones de Python, NumPy y mpmath y la salida completa. La tolerancia del nuevo verificador es numérica, no certificación por intervalos.
3. Revisar §8 y, en particular, las Proposiciones 9–10, el Teorema 3 y la identidad de costo angular. Comprobar que los cambios de precisión en §§1–7 preservan las fórmulas originales. Si hay conflicto de notación, conservar el antecedente y documentar el cambio.
4. Incorporar PDF, fuente TeX, scripts, resultados, README y manifiesto a una carpeta versionada. Actualizar el índice local del expediente con enlace relativo, sin sustituir el manuscrito base ni los históricos. No incorporar archivos auxiliares de compilación ni `__pycache__`.
5. Abrir un PR en borrador con título `T.1 v1.4 — Iterated reflection and directional recovery`, enlazando Issue 16. Adjuntar resultados de verificación y solicitar revisión independiente. No fusionar sin aprobación.

## Texto propuesto para el PR / Issue 16 (English)

### T.1 v1.4 — Iterated reflection and directional recovery

This version preserves the square-free inheritance framework and adds an exact decomposition of each prime-stage recovery into nonnegative reflection moments. It proves a directional lower bound from the first three moments and a closure criterion equivalent to RH through adaptive finite-depth truncations. It also identifies the functional angular cost with the log determinant of the residual operator.

Seven numerical stages reproduce the Schur-complement gain and satisfy the moment, tail and cost identities within floating-point tolerance. The proposed fixed-depth divergence estimate and the arithmetic transfer from automorphic second moments remain open. Independent review is requested for Propositions 9–10, Theorem 3, and the proposed sufficient estimates. This is a local structural extension and an equivalent reformulation, not an unconditional proof of RH.

**Review questions:** Can the admissible automorphic data control the first three moments along the fixed residual direction? Can divergence of the four-step recovery series be established without replacing the square-free residue-zero dictionary? Are there sharper directional estimates with explicit constants?

Endless Monkey Project / Relational Geometry Program
