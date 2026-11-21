# Compendio de referencia y verificación — 21 XI 2026

El documento principal es **`COMPENDIO_RIEMANN_CME_2026-11-21.md`**. Integra el contrato de transferencia, las identidades aritméticas y funcionales, el cubo de espejos y los focos de determinación, y remite a los anexos históricos sin duplicar su redacción.

## Contenido por estado

- **Demostrado:** las identidades elementales y condicionales del compendio, incluidos los saltos de focos, la fórmula periódica (P), la positividad de $e_m$ y la reformulación $\mathrm{RH}\iff\sum_j\gamma_{2^j}=\infty$.
- **Clásico, con cita:** $\mathrm{RH}\iff e_m\to0$ para la familia de índices libres de cuadrados (Báez-Duarte; Proposición 3.1 de la segunda versión, debida a M. Balazard).
- **Verificado finitamente:** conteos exactos de focos, contraejemplos racionales y errores de Gram de escalas pequeñas.
- **Recalculado en coma flotante doble:** errores óptimos restringidos $e_m^2$ para $m=1,2,4,\dots,2048$, fracciones recuperadas $\gamma_{2^j}$ y comparación de recetas en $N=2048$.
- **Abierto:** correspondencia de los operadores de CME–002 con el sistema funcional, estimación universal de recuperación, RH y GRH.

## Ejecutar

Se requiere **Python 3** con **numpy**. Los controles aritméticos y racionales usan solo la biblioteca estándar; los ensayos de Gram usan numpy.

```bash
python3 scripts/verificar_todo.py
```

La duración depende del equipo y puede superar un minuto; `recalcular_gram.py` ocupa casi todo ese tiempo. Controles individuales:

```bash
python3 scripts/verificar_puentes.py
python3 scripts/verificar_reflexiones.py
python3 scripts/verificar_periodos.py
python3 scripts/verificar_focos.py
python3 scripts/ensayo_angulos.py
python3 scripts/recalcular_gram.py
```

`resultados/VERIFICACION_COMPLETA.txt` conserva una ejecución completa, con versiones de Python y numpy. Los archivos `resultados/*_original.txt` son los registros de trabajo previos; `recalcular_gram.py` reproduce las cifras de `registro_mecanismos_original.txt` que usa el compendio.

## Integridad

En la raíz de esta carpeta:

```bash
sha256sum -c MANIFIESTO_SHA256.txt
```

El manifiesto cubre todos los archivos de la carpeta salvo él mismo. Los controles se ejecutan sin conexión a servicios externos.

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program
