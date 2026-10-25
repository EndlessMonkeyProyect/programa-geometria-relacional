# O36 — Comparación modular y acercamiento unilateral (NS 2D)

**Suplemento autónomo exploratorio.** No modifica la Imagen Total ni el núcleo.

Contenido:
- `O36_FORMALIZACION_CIERRE_MODULAR_Y_NO_GO_BILATERAL.es.md`: teoremas, hipótesis, pruebas, contraejemplos, interpretación ontológica.
- `verificar_o36.py`: controles de invariancia de marco, resultados gaussianos O35, paridad, orden cuadrático cerca de la alineación, y cota geométrica O31.
- `VALIDACION_O36.json`: salida de los controles.
- `ANTECEDENTE_O35_2026-10-20.zip`: antecedente reproducible íntegro, copiado sin modificar.
- `MANIFIESTO_SHA256.txt`: integridad de archivos del suplemento.

**Precisión:** las integrales gaussianas computadas son valores de la derivada temporal inicial del PDE, no integración temporal de Navier–Stokes. El signo analítico demostrado se aplica para separación suficientemente grande; los números a distancia `d=6` son comprobaciones por cuadraturas, no aritmética de intervalos.

**Principal resultado nuevo interno:** la paridad exacta del defecto de fase en la familia espejo y su anulación cuadrática cerca de la alineación impiden declarar atracción exponencial uniforme para ambas orientaciones. Hay acercamiento unilateral finito robusto, no sincronización global demostrada.
