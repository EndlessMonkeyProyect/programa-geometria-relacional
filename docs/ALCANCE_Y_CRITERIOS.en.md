# Scope and criteria of this edition

## Corpus

This edition preserves 79 attachments: 72 Markdown files, five JSON files, one CSV, and one ZIP. Three members are extracted from the ZIP; two exactly duplicate documents also provided separately, and the third is the internal v0.91 manifest. Both provenances are retained.

The inventory is limited to this conversation. The texts refer to earlier developments, data, and code that are not included. A reference to them does not mean they are available. The [catalog](../fuentes/CATALOGO.en.md) and [manifest](../fuentes/MANIFIESTO.json) identify the content actually preserved.

## Levels of reading

- **Historical source:** a statement as provided, preserved verbatim.
- **Editorial synthesis:** a reorganized explanation that links the sources.
- **Editorial review:** a mathematical assessment of the integration, expressly identified as such.
- **Editorial example:** a new calculation of limited scope; it does not replace the historical experiments.
- **Open work:** a construction or proof not found in the reviewed corpus.

Authorship of the program remains attributed to Le Matt Ansatz Di Ego, as stated in the sources. Corrections proposed by this edition are not automatically attributed to the author.

## Epistemic labels

| Label | Meaning |
|---|---|
| DEFINITION | Choice of an object and its meaning. |
| POSTULATE | Condition adopted as a starting point. |
| CONDITIONAL DERIVATION | Consequence of stated assumptions; it does not prove those assumptions. |
| REPORTED CONTROL | Numerical result recorded in a source, not fully reproduced here. |
| CHECKED IN THIS EDITION | Example or verification actually run for this delivery. |
| CORRESPONDENCE | Interpretation between branches that requires an additional bridge. |
| OPEN | A procedure, proof, or identification is missing. |
| CORRECTION | Formulation that should be replaced or qualified while retaining the original. |

## Rules of fidelity

1. A later version does not automatically erase all earlier results.
2. An audit that says “closed” is read alongside its assumptions and proofs.
3. The same symbol does not establish identity between objects of different types.
4. A result on a finite model does not automatically transfer to physics or general complexity.
5. “Without loss” describes preservation of the sources; it does not certify that the historical archive is exhaustive or that its claims are universally valid.
6. The originals may contain LaTeX escaping errors or control characters. Their bytes are preserved; the synthesis rewrites necessary expressions legibly.
7. No reuse license is assigned without a decision by the rights holder. Preparing the repository does not change the rights in the sources.

## Verification

Checks cover hashes, the presence of every original, agreement between the package and its extraction, JSON syntax, CSV structure, and local links in the editorial documentation. Exact examples are run without external dependencies. Historical reports of thousands of tests are preserved as reported, not presented as tests rerun here.
