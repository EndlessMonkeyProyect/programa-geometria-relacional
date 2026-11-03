#!/usr/bin/env bash
# Regenera los resultados de los cinco verificadores y los compara con la referencia.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p resultados
python3 verificacion/experimento_cruce_dos_cortes.py resultados/resultados_cruce_dos_cortes.json > /dev/null
python3 verificacion/experimento_tetraedro.py resultados/resultados_tetraedro.json > /dev/null
python3 verificacion/verificar_cadena_duplicacion.py resultados/resultados_cadena_duplicacion.json > /dev/null
python3 verificacion/verificar_particiones.py resultados/resultados_particiones.json > /dev/null
python3 verificacion/verificar_origen_tetraedro.py resultados/resultados_origen_tetraedro.json > /dev/null
python3 comparar_resultados.py referencia_resultados resultados
