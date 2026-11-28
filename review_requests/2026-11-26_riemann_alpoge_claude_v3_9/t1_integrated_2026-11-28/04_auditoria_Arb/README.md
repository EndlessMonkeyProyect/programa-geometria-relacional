# Auditoría Arb recibida
Se conservan intactos los tres archivos recibidos y su manifiesto. El informe suministrado corresponde a `pmax=19`; el valor por defecto del script es 17.

```sh
python -m pip install -r requirements.txt
python -I verificacion_arb_T1.py 19
```

El script original escribe `resultados_arb_T1_p19.json` en el directorio actual. Ejecutar en una copia de trabajo. La salida incluida reporta ocho etapas; no se ha repetido aquí la ejecución de Arb. El script calcula los extremos espectrales con mpmath sobre centros, por lo que beta y los cocientes de condición no tienen certificado espectral. Los JSON originales retienen centros, no radios. La cifra de radio impresa se redondea; no usarla como extremo exacto. Además, `len(E)//2` subcuenta los pares no ordenados al incluir la diagonal: para 256 referencias son 32896 pares únicos, aunque el registro muestra 32768. Esto no altera las fórmulas.

El nuevo verificador de `../05_T1_5/` utiliza los objetos Arb vivos y guarda sus intervalos; se ejecuta separadamente. No cambia los resultados originales. El uso de `python-flint` requiere registrar su versión efectiva y verificar el backend.
