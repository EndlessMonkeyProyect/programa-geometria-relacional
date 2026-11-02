#!/usr/bin/env bash
# G–01 v1.3: integridad, verificación y comparación con la referencia.
#   bash reproducir_todo.sh        (unos segundos; sólo biblioteca estándar de Python)
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "== Integridad (manifiesto SHA-256)"
if command -v sha256sum > /dev/null; then
  ( cd "${RAIZ}" && sha256sum -c --quiet MANIFIESTO_SHA256.txt && echo "   OK" ) || echo "   AVISO: hay huellas distintas. Si ya regeneraste resultados en otra máquina es esperable; la prueba que cuenta es la comparación del paso 3."
elif command -v shasum > /dev/null; then
  ( cd "${RAIZ}" && shasum -a 256 -c --quiet MANIFIESTO_SHA256.txt && echo "   OK" ) || echo "   AVISO: hay huellas distintas; ver el paso 3."
else
  echo "   (no hay sha256sum ni shasum; se omite)"
fi

echo "== Verificación (aserciones de verificar.py)"
( cd "${RAIZ}/verificacion" && python3 verificar.py | sed 's/^/   /' )
python3 "${RAIZ}/verificacion/cotejar_O58.py"

echo
echo "== Comparación de resultados"
python3 "${RAIZ}/comparar_resultados.py"
