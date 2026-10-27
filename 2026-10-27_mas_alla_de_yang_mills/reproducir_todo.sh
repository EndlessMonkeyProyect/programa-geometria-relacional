#!/usr/bin/env bash
# Ejecuta todos los verificadores del complemento "Más allá de Yang–Mills" y compara los resultados.
#   bash reproducir_todo.sh              -> versión rápida (~2 min)
#   bash reproducir_todo.sh --completo   -> todos los tamaños (~25 min)
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODO=""
[[ "${1:-}" == "--completo" ]] || MODO="--rapido"

# 1. Integridad de los archivos distribuidos, antes de regenerar nada
echo "== Integridad (manifiesto SHA-256)"
if command -v sha256sum > /dev/null; then
  ( cd "${RAIZ}" && sha256sum -c --quiet MANIFIESTO_SHA256.txt && echo "   OK" ) || echo "   AVISO: hay huellas distintas. Si ya regeneraste resultados en otra máquina es esperable; la prueba que cuenta es la comparación con tolerancia del paso 3."
elif command -v shasum > /dev/null; then
  ( cd "${RAIZ}" && shasum -a 256 -c --quiet MANIFIESTO_SHA256.txt && echo "   OK" ) || echo "   AVISO: hay huellas distintas; ver el paso 3."
else
  echo "   (no hay sha256sum ni shasum; se omite)"
fi

# 2. Verificadores: cada uno tiene sus propias aserciones
correr () {
  local carpeta="$1"; shift
  echo "== ${carpeta}"
  ( cd "${RAIZ}/${carpeta}" && python3 "$@" > /dev/null && echo "   OK" )
}
correr revision_R02 chequeo_independiente_R02.py
correr paquetes/PR-01_Proyeccion_Recierre_2026-10-26 verificar.py
correr paquetes/PR-02_Modos_Nuevos_2026-10-27 verificar.py
correr paquetes/PR-03_Interaccion_Volumen_2026-10-27 verificar.py
correr paquetes/PR-04_Control_Sin_Brecha_2026-10-27 verificar.py ${MODO}
correr paquetes/PR-05_Brecha_Alta_Temperatura_2026-10-27 verificar.py ${MODO}
correr paquetes/PR-06_Masa_Por_Cierre_2026-10-27 verificar.py ${MODO}
correr paquetes/PR-07_Principios_Accion_2026-10-27 verificar.py

# 3. Comparación con tolerancia (no bit a bit) contra lo entregado
echo
echo "== Comparación de resultados"
python3 "${RAIZ}/comparar_resultados.py"
