# Laboratorio A–G–01 — Armónicos y granularidad

Anexo incremental para la consolidación del 21-XI-2026. Presenta los resultados matemáticos en positivo, con una consulta declarada y una condición de transferencia funcional separada.

## Archivos

- `documentos/LAB_ARMONICOS_GRANULARIDAD_Y_RECIERRE_2026-11-21.md` — definiciones, teoremas A–C, prueba, contrato D y fuentes.
- `scripts/verificar_armonicos_y_granularidad.py` — verificación con fracciones exactas.
- `RESULTADOS_VERIFICACION.txt` — salida del verificador.
- `integracion/INSTRUCCIONES_ADMIN.md` — incorporación no destructiva a la nueva versión.
- `MANIFIESTO_SHA256.txt` — control de integridad.

## Reproducción

Desde esta carpeta:

```bash
python3 scripts/verificar_armonicos_y_granularidad.py
```

**Resultado central:** bajo la consulta de celdas `Q_K(R)=floor(R/(R0/K²))` y los modos `R_n=R0/n`, todas las referencias `n>K²` pertenecen a una misma clase observacional. La razón de separaciones es `K²/[n(n+1)]`. La aplicación al error funcional se presenta como proposición condicional con su propio contrato de norma.

Endless Monkey Project / Relational Geometry Program
