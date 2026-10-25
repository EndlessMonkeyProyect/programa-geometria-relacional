# O64 — Gota crítica y normalizador (21 de octubre de 2026)

**Autoría del Programa de Geometría Relacional:** Le Matt Ansatz Di Ego.

Este suplemento es una **continuación aditiva conceptual de O63**; no modifica sus fuentes ni altera la Imagen Total v3.8.1. Introduce explícitamente un problema **bifásico con interfaz** que no estaba en la simulación monofásica O53. No presenta una DNS de gotas ni afirma haber resuelto Navier–Stokes.

**Aporte del puente O58/O60:** Si se POSTULA un área mínima de registro `A₀`, la partición `A_A=a²A₀`, `A_B=b²A₀`, `A_pend=A₀`, `A_total=N²A₀` reproduce exactamente `a²+b²+1=N²` y genera un radio mínimo *del modelo*; no prueba área elemental ni diámetro mínimo físico.

**Hallazgo:** no hay tamaño mínimo positivo de gota impuesto por Young–Laplace dentro del continuo ideal; sí hay una escala condicional de fragmentación turbulenta (`d_H`) y un costo energético positivo al aumentar el área interfacial. La interfaz posee dos radios principales, pero no se identifican con los dos ciclos toroidales ni con los dos enteros del cierre cuadrático de O58.

**Archivos:**
- `O64_FORMALIZACION.es.md`: formalización completa, teoremas, vínculo con O63 y límites.
- `codigo/verificar_o64.py`: 19 pruebas reproducibles sin dependencia externa y generación de tablas CSV.
- `datos/escalas_y_curvaturas.csv`, `datos/toroide_curvaturas.csv`: datos generados.
- `graficos/`: dos gráficos analíticos de referencia, no simulaciones de dos fases.
- `MANIFIESTO_SHA256.txt`: huellas para auditoría.

**Ejecutar:** `python codigo/verificar_o64.py` desde cualquier carpeta.

**Próxima frontera:** O65 compararía condiciones físicas de interfaz a igualdad de datos de flujo para determinar si el comparador relacional necesita explícitamente tensión superficial y curvatura.
