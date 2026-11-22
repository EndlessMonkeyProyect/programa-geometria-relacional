# Nota de continuidad — aparición y herencia

Material suplementario para R–01/R–02 y HC–03. No constituye un laboratorio nuevo ni una publicación de una prueba de RH.

- `NOTA_CONTINUIDAD.md`: enunciados y demostraciones.
- `verificar_transicion.py`: verificador exacto con biblioteca estándar de Python.
- `muestras.csv`: cortes numéricos para inspección.
- `verificacion.json`: recuento de controles exactos.
- `SHA256SUMS.txt`: manifiesto para comprobar integridad.

Desde este directorio, ejecutar `python verificar_transicion.py`, luego `sha256sum -c SHA256SUMS.txt` (o una herramienta compatible). La ejecución vuelve a generar los CSV/JSON deterministas; la precisión global de la condición RH no se demuestra por ejecutar un rango finito.
