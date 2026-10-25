# O22 — Teselación tetraédrico-octaédrica y continuidad de interfaces

**Autor del programa:** Le Matt Ansatz Di Ego  
**Fecha:** 19 de octubre de 2026  
**Naturaleza:** suplemento aditivo O22, con formalización condicional, geometría exacta y controles finitos.

Leer primero `O22_CONTINUIDAD_Relleno_Y_FOCO.es.md`. La rama no modifica ninguna Imagen Total ni los suplementos O19–O21.

Archivos:
- `O22_CONTINUIDAD_Relleno_Y_FOCO.es.md` — demostraciones, contratos y límites.
- `laboratorio_o22.py` — pruebas reproducibles con aritmética exacta, Python estándar.
- `RESULTADOS_O22.json` — registros finitos de la construcción.
- `PRUEBAS_EJECUTADAS.txt` — ejecución de las pruebas O22.
- `REGRESION_O21.txt` — ejecución de la suite O21 anterior.
- `ANTECEDENTE_O21_2026-10-19.zip` — archivo integral del suplemento O21 y antecedentes O20/O19.
- `MANIFEST_SHA256.json` — comprobaciones de integridad de los archivos del paquete.

Ejecutar con `python laboratorio_o22.py` desde el directorio del suplemento.

**Resultado principal:** una teselación de tetraedros y octaedros se reconstruye con una sola escala de arista, y el punto reflejado del tetraedro es el centroide de la cara opuesta del octaedro adyacente. El puente físico a masa y espacio-tiempo continúa abierto.
