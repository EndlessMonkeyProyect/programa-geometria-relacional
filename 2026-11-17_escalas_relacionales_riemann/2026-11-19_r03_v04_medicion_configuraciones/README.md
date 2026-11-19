# R–03 v0.4 y puente de medición de configuraciones

**19-XI-2026 · Propuesta editorial ES/EN, pendiente de revisión y aprobación del PR**<br>
Le Matt Ansatz Di Ego<br>
Endless Monkey Project<br>
Relational Geometry Program

Esta carpeta integra en una **nueva rama** R–03 v0.4 y la medición de Gram v1.1, conservando el R–03 v0.3 publicado y el historial R–01/R–02. La medición se refiere a discrepancias de configuraciones, no a energía física.

## Documentos

- [R–03 v0.4 — español](R03_HERENCIA_Y_LOCALIZACION_ES.md)
- [R–03 v0.4 — English](R03_SPECTRAL_INHERITANCE_EN.md)
- [Medición funcional mediante Gram — español](PUENTE_GRAM_MEDICION_ES.md)
- [Gram bridge — English](GRAM_BRIDGE_MEASUREMENT_EN.md)
- [Procedencia y alcance](PROCEDENCIA_Y_LIMITES.md)
- [Cambios respecto a la versión histórica](CHANGELOG.md)

## Código y prueba

```bash
python -m pip install mpmath
python verificacion_R03.py --hasta 6
python verificacion_puente_y_control.py
python verificacion_puente_gram_v1_1.py --N 3000 --dps 45
sha256sum -c SHA256SUMS.txt
```

El verificador R–03 completo hasta $10^8$ consume memoria considerable; ejecutar aparte y registrar recursos. Los registros heredados del paquete de auditoría se conservan fuera de esta carpeta y no equivalen a una nueva ejecución.

**Procedencia pendiente:** R–RH–01 del 1-XI-2026 está recuperado como transcripción de lectura, no como archivo original autenticado ni URL pública verificada. Antes de aprobar la integración, se requiere cotejar el original.

**Estado matemático:** identidades finitas verificables y relaciones conocidas; hipótesis de Riemann abierta. No hay prueba de energía física ni ventaja computacional general.
