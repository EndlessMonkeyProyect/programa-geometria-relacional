# Relational Geometry Program

[Leer este repositorio en español](README.md).

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
