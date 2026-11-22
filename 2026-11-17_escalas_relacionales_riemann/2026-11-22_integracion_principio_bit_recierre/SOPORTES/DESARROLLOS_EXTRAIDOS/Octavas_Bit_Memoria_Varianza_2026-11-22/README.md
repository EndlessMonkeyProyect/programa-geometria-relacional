# Memoria del bit y trayectoria diagonal — 22/11/2026

**Objeto:** una nota técnica para revisión que conecta el transporte exacto de bits entre octavas, la varianza finita de los ciclos de acarreos y la trayectoria auto-referenciada de la frontera móvil. Continúa resultados anteriores sin modificar sus fuentes.

**Contenido:**

- `MEMORIA_BINARIA_Y_TRAYECTORIA_DIAGONAL_ES.md`: proposiciones con demostraciones y estados.
- `verificar_memoria.py`: verificador de biblioteca estándar de Python; utiliza `fractions.Fraction` para covarianzas exactas.
- `RESULTADOS.txt`: resultados de la ejecución.
- `MANIFEST.sha256`: integridad de los otros tres archivos.

**Ejecución:** `python3 verificar_memoria.py` (también `py -3 verificar_memoria.py` en Windows). Se usa salida ASCII para compatibilidad. Ejecutar `sha256sum -c MANIFEST.sha256` para comprobar integridad en Linux/macOS.

**Alcance:** las identidades aritméticas y la cota de segundo momento son demostradas bajo sus definiciones; el agotamiento normalizado usa el teorema de los números primos; la cota cuantitativa equivalente a RH sigue siendo el objetivo de investigación.

Endless Monkey Project / Relational Geometry Program
