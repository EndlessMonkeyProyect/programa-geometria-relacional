# Integracion matematica de Riemann: R-03, HC-02/03 y acarreos

Fecha: 22-11-2026. Estado: manuscrito para revision matematica, con control finito exacto.

## Contenido
- `INTEGRACION_FORMAL_ES.md`: manuscrito fuente con proposiciones y pruebas.
- `INTEGRACION_FORMAL_ES.pdf`: lectura academica paginada.
- `scripts/verificar_integracion.py`: regresiones de coeficientes racionales de log(p), sin bibliotecas externas.
- `RESULTADOS.txt`: salida de la verificacion efectivamente ejecutada.
- `MANIFEST.sha256`: huellas de los archivos distribuidos.
- `scripts/verificar_integridad.py`: comprobacion de integridad del paquete.

## Reproducir

En Linux/macOS: `python3 scripts/verificar_integracion.py --M 400`

En Windows: `py -3 scripts/verificar_integracion.py --M 400`

Comprobar hashes: `python3 scripts/verificar_integridad.py` (o `py -3 scripts/verificar_integridad.py`).

La salida del verificador contiene ASCII para ser compatible con consolas Windows sin configuracion UTF-8.

## Integracion sugerida

Copiar esta carpeta al repositorio bajo:
`2026-11-17_escalas_relacionales_riemann/2026-11-22_integracion_operadores_acarreos/`

Abrir pull request para revision matematica. El paquete no modifica documentos, PR ni commits existentes y no se ha publicado automaticamente.

## Alcance de la verificacion

Los resultados computacionales son comprobaciones finitas sobre identidades algebraicas; las pruebas asintoticas y la equivalencia clasica con RH se presentan por escrito. La correspondencia con la biblioteca Lean de Alpoge y la construccion espectral de Masullo es un estudio comparativo documentado.
