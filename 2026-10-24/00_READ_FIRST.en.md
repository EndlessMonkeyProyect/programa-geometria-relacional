# Relational Geometry Program — read first

**Le Matt Ansatz Di Ego · October 24, 2026**

*English version of `00_LEER_PRIMERO.md`, with a short guide for English readers at the start. The Spanish text is the authoritative version.*

## Start here

The Relational Geometry Program (*Programa de Geometría Relacional*) asks whether a minimal economy of differences, reflections, references and closures can give one common language for mathematical, computational and physical questions. It starts from language and ontology, not from a metric or a clock, and it says at every step what is proved, what is interpretation and what is open.

Most of this package is in Spanish. These files are in English:

| Read | What it is |
|---|---|
| `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.en.md` | **The main text.** The current picture of the whole program: language, the thread in twelve steps, a dictionary, the formal core, the realizations, the three branches, mass, time and gravity, an open-problems matrix and the links to the literature. It starts with the glossary used in all English files |
| `00_PUBLICACION/Programa_Geometria_Relacional_Manuscrito_Publico_2026-10-24.en.md` (and `.pdf`) | A four-page public manuscript, centered on relational time |
| `01_HILO/SUPLEMENTOS/Suplemento_Ritmo_Ciclo_Base_Tiempo_y_Gravedad_2026-10-24.en.md` | The supplement on the base cycle, rhythm, time and a possible bridge to gravity |
| `02_REALIZACIONES/01_cubo_de_espejos/CME-003_de_las_cuatro_referencias_a_los_angulos/CME-003_De_las_cuatro_referencias_a_los_angulos.en.md` | How the angles π/2 and π/3 come out of four references, with an exact verifier |

**How to read the claims.** Every claim carries a status mark: [O] ontology (the author's reading), [D] definition, [T] proved under declared hypotheses, [E] reproducible trial, [F] falsified, [H] physical hypothesis, [A] open. The program does not claim to solve P versus NP, Navier–Stokes regularity or the Yang–Mills mass gap.

**Names.** Folder and file names, code comments and program output are in Spanish. *Hilo* = thread, *ramas* = branches, *realizaciones* = realizations, *laboratorios* = laboratories, *archivo* = archive, *fuentes* = sources, *vigente* = current version.

---

## What this package is

This package gathers in one place the five packages shared on October 24, 2026, sorted into parts and without duplicates:

- `Programa_Geometria_Relacional_O93_NS_Pruebas_Reproducibles_2026-10-22.zip`
- `LAB_CONV_v2_NODOS_CIERRE_PNP_2026-10-22.zip`
- `R02_PUENTE_Y_LABORATORIO_2026-10-23.zip`, plus the `.md` and `.pdf` of R‑02 sent separately
- `Programa_Geometria_Relacional_Rama_NS_Integral_O24_O93_2026-10-24.zip`

The public manuscript and the supplement on rhythm, base cycle, time and gravity, both of October 24, were added that evening.

**Nothing was rewritten.** The original documents and programs are intact; only where they live has changed. What is new in this edition is:
- the two indexes, `00_LEER_PRIMERO.md` and this file;
- `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md`, the reading text of this edition;
- `01_HILO/ESQUEMA_ACORDADO_2026-10-24.md`, the agreed outline;
- the records and programs `CME-001`, `CME-002` and `CME-003`;
- the `revision_2026-10-24/` folder of each branch;
- the English versions (`.en.md`) listed above;
- the READMEs of `00_PUBLICACION/` and of `01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/`;
- `MANIFIESTO_SHA256.txt`, `PROCEDENCIA.csv`, `DUPLICADOS_RETIRADOS.csv` and `verificar_integridad.py`.

## The parts

| Folder | What it contains | Status |
|---|---|---|
| `00_PUBLICACION/` | The public manuscript of October 24 (md and PDF, as received) and its English version | License and DOI not yet assigned |
| `01_HILO/` | The thread: the reading text of this edition and its English version; the agreed outline; Imagen Total 3.9, the previous edition (PDF, general report, index, atlas); `SUPLEMENTOS/`, with the rhythm and gravity supplement; `fuentes/`, the sources: foundations, formal core, language, the synthesis of October 20, the semantic crystal, "The thread of two" and the rhythm and gravity sources | Reading text of this edition; open questions are listed in its Part IX |
| `02_REALIZACIONES/` | Realizations. `01_cubo_de_espejos/`, the mirror cube: minutes, review of the dynamic radius, the cube document, geometry O19–O22, O59, CME‑001, CME‑002 and CME‑003. `02_esferas/`, spheres. `03_circuito_C4/`, the C4 circuit | CME‑001 to CME‑003 done; from CME‑003, the rule of the moving wall that gives the four references remains open |
| `03_RAMAS/` | The branches: Navier–Stokes, P versus NP and Yang–Mills, each with its current version and review notes | See "What is current" |
| `04_LABORATORIOS/` | Laboratories: mirrors E‑MIRROR v1–v8 and sphere radii v10, with programs, data and tests | 151 tests pass |
| `05_ARCHIVO/` | Archive: the full history of Navier–Stokes (v3.7, O23–O38, O39–O53, O54–O92), the integral picture of October 18, earlier audits, the textual corpus of edition 3.9, and the two notes for the compiler received on October 24 | Kept as is |

## What is current in each branch

- **Navier–Stokes:** `03_RAMAS/navier_stokes/VIGENTE_O93/` (October 22), with the Navier–Stokes chapter of Imagen Total 3.9 and the maps of the branch. The route toward a theorem about the program's own equation is in `modelo_propio_O18/`.
- **P versus NP:** `03_RAMAS/p_vs_np/VIGENTE_LAB_CONV_V2/` (October 22).
- **Yang–Mills:** `03_RAMAS/yang_mills/VIGENTE_R02/` (October 23), with R‑01 and the rescue minutes of October 22 in `FUENTES/`.

Each branch has `revision_2026-10-24/`, with what was checked, what should be corrected in the next edition, and the program that verifies it. These notes are in Spanish.

## Decisions taken on October 24

- The aim is a thread of minimal economy for understanding reality. First the thread in its own terms; the links to the literature come afterwards, in a separate layer at the end.
- The order of the thread: the totality, whose property is indeterminacy → reflection → closing or opening according to the angles → the branches.
- The closing angles are given by the structure generated by the multiples that the moving wall leaves behind. CME‑002 writes that rule and proves it in two readings, angles and identities: what decides whether an enclosure closes, repeats or opens is the sum of the fractions compared with the totality.
- The grammar shared by the branches is emergent, not foundational.
- Control criterion: if the thread is on the right path, it closes by itself.

## What was recovered that was not visible before

- "The thread of two" (*El hilo del dos*) in full: 37 documents of October 13 and 14 that lived only as text inside the corpus of edition 3.9. They were recovered byte for byte, each verified against the sha256 recorded in the corpus (`01_HILO/fuentes/06_hilo_del_dos/`). The ±1 reflection at each node, the genealogy 4 → 3 and 5, 8 → 7 and 9, the open bit of the 8, the three as 2² − 1 and the N1 bound of the table engine were already there.
- The programs, results and logs of O44–O48, which were only inside their zips (`05_ARCHIVO/navier_stokes_O39_O53/desarrollos_extraidos/`).
- The full semantic crystal, 12 files that were only compressed (`01_HILO/fuentes/05_sintesis_y_lenguaje_2026-10-20/fuentes_cristal_semantico/`).
- Two sources of the rhythm and gravity supplement, verified by their sha256: GR3, "Unison concordance", of October 18, and the synchrony falsifier of version 5.9, of October 8 (`01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/`). Two other sources cited by the supplement are not in any material available here; its README says so.
- The complete C4 trial: verifier, 16 states and an HTML explorer (`02_REALIZACIONES/03_circuito_C4/C4_v3_8_1/ENSAYO_C4_2026-10-21/`).

## What was withdrawn

85 items were withdrawn. `DUPLICADOS_RETIRADOS.csv` records each one, with its sha256 and where the kept copy is. They are zips whose full content is extracted, exact copies, and one `.pyc` cache. Internal copies of code and data inside each laboratory were kept on purpose, so that each runs and verifies on its own.

## How to verify

```bash
python3 verificar_integridad.py
```

It checks the sha256 of every file against `MANIFIESTO_SHA256.txt`. `PROCEDENCIA.csv` says which package and path each recovered file came from.

From the new structure, these were run again and gave the same results, byte for byte:
- O93 (`verificar_o93.py`), LAB‑CONV v2 and its exhaustive verifier, R‑02, CME‑001, CME‑002, CME‑003, O59, O63, O84 and the C4 trial;
- the tests of the nine mirror and sphere laboratories;
- the three review programs.

The only failure is the known one of `simulacion_galerkin.py` under Python 3.13, when it draws its figure; its numbers come out identical. The fix is in the Navier–Stokes review notes.

## Next editorial steps

1. Review the reading text, especially the table "Language along the thread" (an editorial reading) and the row on the electron and the proton; then the open questions of its Part IX.
2. What remains of CME‑003: the rule of the moving wall that gives four interchangeable references. π/2 and π/3 already come from those references.
3. Address the pending items in each `revision_2026-10-24/`.
4. For publication: choose a license and a DOI, which the manuscript leaves unassigned, and obtain the two missing sources of the supplement (MF‑43 and "Rhythm, radius and relational relativity").
