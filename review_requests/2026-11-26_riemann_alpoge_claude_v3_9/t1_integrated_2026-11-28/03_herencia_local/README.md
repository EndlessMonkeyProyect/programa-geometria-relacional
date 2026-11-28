# T.1 — Complemento de herencia local

Complemento de investigación, no reemplazo de T.1 v1.4. Leer `Anexo_T1_Herencia_local.md`.

## Reproducción

Python 3, NumPy y mpmath. Desde este directorio:

```sh
python verificar_herencia_local.py
python certificar_contraejemplo.py
```

El primero reutiliza el Gram de Vasyunin de v1.4 en doble precisión; el segundo usa aritmética de intervalos y entradas enteras. Los JSON y salidas se adjuntan. Los JSON pueden regenerarse con pequeñas diferencias de redondeo entre plataformas. El manifiesto autentica los archivos distribuidos, no los JSON regenerados. Verificar primero con `sha256sum -c SHA256SUMS` (Linux/macOS con GNU coreutils) o herramientas SHA-256 equivalentes.

## Incorporación propuesta (administrador/Codex)

1. Identificar el directorio vigente del expediente Riemann / Nota técnica 01 v3.9 / T.1 y conservar los paquetes anteriores intactos.
2. Incorporar este paquete en un subdirectorio nuevo, por ejemplo `T1/complemento_herencia_local_2026-11-28/` (ajustar a la organización real del repositorio).
3. Verificar el manifiesto y ejecutar los dos scripts; conservar sus salidas en el PR y registrar versiones de Python, NumPy y mpmath. Si hay diferencias de redondeo, cotejar las aserciones y la cota intervalar, sin sustituir silenciosamente archivos históricos.
4. Actualizar el índice con: A1–A5 demostrados como resultados internos; equivalencia con RH mediante Báez-Duarte; contraejemplo intervalar al criterio universal; anulación asintótica de defectos abierta; transferencia directa de operadores abierta.
5. Proponer revisión independiente de los lemas y del teorema A3 antes de fusionar. Evitar presentar el complemento como demostración autónoma de RH o como formalización Lean.

Título de PR sugerido: `T.1: local hereditary defects, coefficient variation and interval counterexample`.
