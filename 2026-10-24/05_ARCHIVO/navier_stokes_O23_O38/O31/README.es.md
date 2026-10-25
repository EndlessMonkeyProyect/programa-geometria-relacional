# O31 — Certificado de persistencia vorticial

Suplemento independiente del Programa de Geometría Relacional (19 octubre 2026).

**Problema:** establecer desde Navier–Stokes 2D un criterio suficiente, prospectivo y no retrospectivo para conservar dos poblaciones de vorticidad distinguibles durante un intervalo finito.

**Resultado:** bajo vorticidad positiva, circulación finita y acotada y segundo momento inicial finito, las desigualdades (O31.1)–(O31.8) demuestran concentración de al menos `1−1/k²` de cada etiqueta en dos discos disjuntos durante `[0,T]`, siempre que se cumpla la condición explícita O31.7.

**No probado:** persistencia de forma exacta, sincronización de fase, fusión, selección intrínseca de etiquetas, estabilidad 3D, regularidad global NS, ni velocidad causal universal.

Archivos:
- `O31_PERSISTENCIA_RELACIONAL_CONCENTRACION_NS.es.md`: teorema con demostraciones, contrato y falsadores.
- `laboratorio_o31.py`: tests algebraicos, ejemplo numérico, controles aleatorios y caso gaussiano exacto aislado.
- `VALIDACION_O31.json`: resultado de las pruebas reproducibles.
- `ANTECEDENTE_O30_2026-10-19.zip`: paquete O30 preservado sin modificaciones.
- `MANIFEST_SHA256.txt`: sumas de comprobación de archivos del paquete.

Ejecutar:

```bash
python laboratorio_o31.py
```

No se necesita conexión a internet. El laboratorio **no es** una DNS ni sustituye las pruebas analíticas.
