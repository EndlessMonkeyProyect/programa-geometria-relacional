# Relational Geometry Program

[Leer este repositorio en español](README.md).

## The Cross as Central Reflection · November 3, 2026

The [November 3 delivery](2026-11-03_cruce_reflejo_central/READ_FIRST.en.md) contains the paper [*The Cross as Central Reflection*](2026-11-03_cruce_reflejo_central/articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.md) ([PDF](2026-11-03_cruce_reflejo_central/articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.pdf)), the essay ["La caja de espejos" v0.3](2026-11-03_cruce_reflejo_central/articulo/La_caja_de_espejos_v0.3_2026-11-03_EN.md), the [notes of November 3](2026-11-03_cruce_reflejo_central/articulo/Notes_2026-11-03_EN.md) on partitions and the origin of the tetrahedron, and five reproducible verifiers. It measures the piece that Claude's algorithm (2026) decomposes, the cross: the gain comes from splitting it across two cuts, the crosses occupy the program's tetrahedron and, in doubling by reflection, only the 8 makes it cheaper. These are classical theorems stated in the program's language; it is not an algorithm of its own nor a priority claim, and algorithmic equivalence remains open. The [request for verification](review_requests/2026-11-03_cruce_reflejo_central/README.md) asks for review of reproducibility, the proofs and documentary precedence.

[GitHub release 2026-11-03](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/releases/tag/2026-11-03) · [Zenodo DOI: 10.5281/zenodo.23932854](https://doi.org/10.5281/zenodo.23932854)



## G–01 review request · November 2, 2026

We invite review of the tree of positive integer solutions to $N^2-a^2-b^2=1$ for $N>1$, counting different orderings of $a$ and $b$ separately. The first three questions concern the descent proof for each non-root node, precedents for the tree, and reproduction of the count of 754 solutions through $N=3000$. The gravitational interpretation remains open. The request quantifies the gap left by the literal integer reading in the weak-field regime. [One-page summary](review_requests/2026-11-02_G01_gravity/EXECUTIVE_SUMMARY_EN.pdf) · [Full request](review_requests/2026-11-02_G01_gravity/REVIEW_REQUEST_EN.md) · [Edición en español](review_requests/2026-11-02_G01_gravedad_es/LEER_PRIMERO.md)

## Gravity thread G–01: November 1, 2026

The [G–01 · The Mechanism of Gravity package](2026-11-01_G01_mecanismo_de_la_gravedad/READ_FIRST.en.md) contains document v1.3 in [English](2026-11-01_G01_mecanismo_de_la_gravedad/articulo/G01_Mechanism_of_Gravity_v1.3_2026-11-01_EN.md) and in the [Spanish reference text](2026-11-01_G01_mecanismo_de_la_gravedad/articulo/G01_Mecanismo_de_la_Gravedad_v1.3_2026-11-01.md), a dependency-free reproducible verifier, the review that led from v1.2 to v1.3, and the earlier versions. Its central result in this delivery is the identification of the O58 contract with the Minkowski hyperboloid in 2+1 and the proposed tree of its ordered positive integer solutions. The November 2 request specifies the domain, physical assumptions and pending assessment of literature precedence. Its ROSI status is OPEN: it does not derive gravity or Newton’s law.

## Previous review request: October 30, 2026

The [English review request](review_requests/2026-10-30_mirror_cube_p_vs_np/README.md) contains the full text, executive summary, T-EXT-01 materials, and a finite verifier. The [Spanish source package](review_requests/2026-10-30_mirror_cube_p_vs_np_es/LEER_PRIMERO.md) preserves the integral request and historical sources. T-EXT-01 gives a quadratic information bound for a specified family of 3-coloring queries; it does not prove P = NP or P ≠ NP.

## Previous complement: October 27, 2026

The [Beyond Yang–Mills article](2026-10-27_mas_alla_de_yang_mills/articulo/Beyond_Yang_Mills_2026-10-27_EN.md) ([PDF](2026-10-27_mas_alla_de_yang_mills/articulo/Beyond_Yang_Mills_2026-10-27_EN.pdf)) is an English translation of the [Spanish reference text](2026-10-27_mas_alla_de_yang_mills/articulo/Mas_alla_de_Yang_Mills_2026-10-27.md). The [package guide](2026-10-27_mas_alla_de_yang_mills/LEER_PRIMERO.md) introduces seven reproducible packages, PR-01 to PR-07, and an independent R-02 check. The article is a draft for review and does not claim to solve the Yang–Mills mass gap.

## Base organized edition: October 24, 2026

The [English reading guide](2026-10-24/00_READ_FIRST.en.md) introduces the organized edition: its integrated thread, realizations, three research branches, laboratories, and historical archive. The package also includes an [English public manuscript](2026-10-24/00_PUBLICACION/Programa_Geometria_Relacional_Manuscrito_Publico_2026-10-24.en.md) and an [English supplement on rhythm, time, and gravity](2026-10-24/01_HILO/SUPLEMENTOS/Suplemento_Ritmo_Ciclo_Base_Tiempo_y_Gravedad_2026-10-24.en.md).

The [Spanish index](2026-10-24/00_LEER_PRIMERO.md) is authoritative. The edition's manifest verifies 1,047 files; the original ZIP is retained as a distribution archive.

## Earlier conceptual edition: 0.1.0

**Conceptual edition 0.1.0 · September 29, 2026**

**Program author in the source materials:** Le Matt Ansatz Di Ego

**Editorial organization and review:** prepared with AI assistance from the files provided.

The program investigates how a structure of comparisons makes certain differences distinguishable, how a closure preserves a sufficient boundary, and how relations between closures may call for new references. It explores algebraic, dynamical, and computational realizations of this idea.

This repository brings the received development together in a conceptual reading, preserves the originals in full, and indicates which connections are proven, which depend on assumptions, and which remain open. It does not claim a solution to P versus NP or a validated physical theory.

## Start here

1. [Conceptual synthesis](docs/SINTESIS.en.md): the complete argument in connected prose.
2. [Reading map](docs/MAPA_DE_LECTURA.en.md): a question-based path through the chapters and sources.
3. [Results and dependencies](docs/trazabilidad/RESULTADOS.en.md): what can be supported, and under which conditions.
4. [Corrections and open work](docs/trazabilidad/CORRECCIONES_Y_PENDIENTES.en.md): distinguishes historical corrections from new editorial observations.
5. [Source catalog](fuentes/CATALOGO.en.md): access to the 79 preserved attachments.

## Structure

| Directory | Contents |
|---|---|
| docs/conceptos | Ten chapters of conceptual and formal synthesis. |
| docs/trazabilidad | Results, historical changes, open work, and relationships between sources. |
| fuentes/originales | The 79 attachments, unmodified. |
| fuentes/paquetes_extraidos | Browsable contents of the ZIP received. |
| datos | Guide to reported experimental results and their limitations. |
| ejemplos | New, small, reproducible checks, identified as editorial work. |
| herramientas | Integrity, data, and link verification for the edition. |
| verificacion | Verification report for this delivery. |

## What “without losing information” means

The synthesis does not aim to replace every equation or every test in the originals. Preservation is provided through complete copies, a catalog, a SHA-256 manifest, and links from the conceptual exposition. Incompatible or superseded formulations remain in the archive and are identified in the review.

The scope is the attached files available in this conversation. The entire historical repository, its originating conversations, and the experimental scripts mentioned but not included have not been recovered. This delivery contains no v0.71 or v0.88 sources; missing releases are not invented. The v0.91 package is a partial delivery, not a compilation of the full history.

## Two ways to use this delivery

- Open README.en.md in the [public repository](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional) and follow the links with a Markdown viewer.
- Clone the public repository and run the checks:

~~~bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional.git
cd programa-geometria-relacional
python3 herramientas/verificar.py
python3 ejemplos/comprobaciones.py
~~~

The file historial.git.bundle is part of the original ZIP for this delivery, not the published repository. It preserves the initial commit of this edition and does not contain the author's historical Git history. The content can also be read without Git.

## Central status

The contextual definition of information, composition through boundaries, and local algebraic closure have precise conditional results. It remains to be shown that relational composition determines the geometric operator of a new capsule and to verify its stability under the proposed coupling.

The conceptual edition has its own version; it does not rename the program v0.92 or present an editorial review as approval by the author. See [scope and criteria](docs/ALCANCE_Y_CRITERIOS.en.md) and [how to contribute](CONTRIBUTING.en.md).
