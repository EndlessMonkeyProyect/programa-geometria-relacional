# Relational Geometry Program · Version 3.5

**Persistent Core, Inheritance, Granularity, and Reclosure** · November 21, 2026

The [complete English manuscript](documentos/PERSISTENT_CORE_INHERITANCE_GRANULARITY_RECLOSURE_2026-11-21_EN.md) is also available as a [seven-page PDF](documentos/PERSISTENT_CORE_INHERITANCE_GRANULARITY_RECLOSURE_2026-11-21_EN.pdf). Its [Spanish source text](documentos/NUCLEO_HERENCIA_GRANULARIDAD_RECIERRE_2026-11-21.md) and [Spanish PDF](documentos/NUCLEO_HERENCIA_GRANULARIDAD_RECIERRE_2026-11-21.pdf) remain alongside it. The translation preserves the formulas, hypotheses, proof statements, and limits of the source.

The package also contains the [RA–01 appendix](anexos/RA-01_recuperacion_acumulada/README.md), the [A–G–01 harmonics and granularity laboratory](laboratorios/2026-11-21_armonicos_granularidad/README.md), the [S–RA–01 Möbius-seed laboratory](laboratorios/2026-11-21_RA01_semilla_mobius/README.md), source documents, and verification scripts. These supporting materials are in Spanish.

## Scope

The manuscript brings together exact identities for rational transport, algebraic remainder, Möbius-sum reclosure under scale doubling, and orthogonal projection. It gives a three-window reconstruction bound, a finite periodic-energy formula, and a conditional certificate for accumulated recovery by seeds. The numerical laboratory measures the squarefree-reference error through 2048 and finite gains by dyadic block. The global bounds needed to apply the functional criterion to the Riemann hypothesis remain open.

## Reproduction

From this folder, run:

```bash
python3 scripts/verificar_todo.py
sha256sum -c MANIFIESTO_SHA256.txt
(cd laboratorios/2026-11-21_armonicos_granularidad && sha256sum -c MANIFIESTO_SHA256.txt)
```

The numerical S–RA–01 laboratory requires NumPy. The main manifest covers 36 files; the nested harmonics manifest covers five.

## Review provenance

The six documents under `fuentes/` are preserved as historical source material. The reviewed CME–RH compendium is in [draft PR #11](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11), and the R–03 v0.4 edition is in [draft PR #9](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9). The current package is proposed in [draft PR #12](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/12).

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
