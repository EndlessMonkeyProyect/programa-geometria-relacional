# History of this edition

## What computation becomes unnecessary? v0.3 · 2026-11-10

- The paper's thread is written in the program's vocabulary: uncertainty, reflection, closure, inheritance and novelty. Technical terms move to a bridges section with references.
- Added a generic baseline: variable elimination on the formula without recognition, measured with the same protocol as the other routes. The long-connection family is extended to 256 primary variables, and the formulas are exported in DIMACS for dedicated counters.
- Added a contract test of the recognizer on 5,889 formulas. The recognizer explicitly rejects a parity input outside the family; its counts are unchanged.
- The §9 table comes from a single results file, formulas use delimiters that GitHub renders, and the English paper is complete with a PDF.
- The reproduction record lives in `ANEXO_EVIDENCIAS.md` and `EVIDENCE.en.md`. Removed the editorial checklist, the audit log, the earlier laboratory and its before/after control.

## What computation becomes unnecessary? · 2026-11-10

- Added a follow-up paper in Spanish and English, a reading PDF, two laboratories with their original results, and a standalone verifier.
- Checked all 14 files against the supplied manifest. Reran the standalone verifier and the distributed-relations laboratory; the latter required removing the eight-second wall-clock limit from repeated DPLL runs while retaining the node limit. Also reran C7 of the exchange-and-convergence laboratory.
- The package invites independent review and makes no new general 3-SAT complexity claim.

## Pair-swap review · 2026-11-04

- Opened a [dedicated thread](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4) for a human assessment of the rank formulas, their correspondence with the preprints and their precedents.
- Fixed the OpenAI and Anthropic references by commit and the reproducible delivery by the commit of tag `2026-11-03-pair-swap-review`.
- Updated both language guides and their SHA-256 manifest. The archived tag and ZIP retain their original content.

## G–01 review request · 2026-11-02

- Added the English and Spanish G–01 v1.3 review requests, one-page summaries, short invitations, and SHA-256 manifests.
- Q1–Q3 focus on the descent proof for the tree of ordered positive pairs, its precedents, and the finite check through $N=3000$.
- Recorded the weak-field difficulty under the literal identification $r_s/r=1-1/N^2$. The jump from rest to the first tree node is from 0 to $8/9$.

## Gravity thread G–01 — 2026-11-01

- Added document G–01 v1.3 in Spanish and English, as Word, PDF and Markdown, with its figures.
- Added a dependency-free verifier for the exact results and computable controls; the 16 O58 branches from (2,2,3) match the O58 file. SHA-256 manifest for the package.
- Added the v1.2 → v1.3 review spreadsheet and versions 1.0 to 1.2 in `historial/`. Status is OPEN; no derivation of gravity is claimed.

## Mirror Cube and P versus NP review request — 2026-10-30

- Added browsable Spanish and English packages with the full request, summaries, and technical notes.
- Reproduced the 4,672 finite T-EXT-01 queries; the results agree with the archived JSON files.
- Verified SHA-256 manifests for 23 Spanish and 13 English package files. Independent mathematical review is requested; no P versus NP solution is claimed.

## Beyond Yang–Mills complement — 2026-10-27

- Added the Spanish and English article in Markdown and PDF, plus seven PR-01 to PR-07 packages.
- Added an independent R-02 check, reference results, and a SHA-256 manifest: 47 files verified.
- The complement is a draft for review and explicitly leaves the mass gap open.

## Organized edition — 2026-10-24

- Browsable addition of the dated package: 1,047 files checked against its SHA-256 manifest.
- Public manuscript, rhythm and gravity supplement, integrated thread, realizations, research branches, laboratories, and historical archive.
- English guide and principal texts; the 0.1.0 conceptual edition remains available.

## 0.1.0-editorial — 2026-09-29

- Preservation of 79 received files and navigable extraction of three ZIP members.
- Synthesis and ten conceptual chapters.
- Glossary, notation, lineage, and a register of 26 results.
- Separation of historical corrections, nine editorial observations, and eight open issues.
- Complete catalog and integrity manifest.
- New examples and checks identified as editorial work.
- Initial Git repository and portable bundle.
- English translations of the 25 editorial documents; the original sources remain unchanged.
- Publication on GitHub and preservation of original bytes in Windows checkouts.

This numbering describes the editorial work. It does not replace the program's v0.xx versions or MF identifiers.
