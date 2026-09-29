# How to continue the repository

## Preserve the history

Do not edit `fuentes/originales` or replace a source with a corrected version. Add a new version under a different name, record its provenance, and update the manifest. Retain earlier audits.

## Add a result

Each new result should state:

1. the question;
2. the objects, domains, and assumptions;
3. the claim;
4. the proof or procedure;
5. a relevant example and counterexample;
6. its scope and dependencies;
7. the sources or files it changes conceptually.

Label a numerical check as a check, not as a general proof. Do not describe a new definition as a derivation of its physical necessity.

## Update the synthesis

Identify the result in the register that is affected. Explain whether the update corrects, restricts, generalizes, or replaces a formulation. Check that it does not inadvertently change the meaning of capsule, reference, residue, dimension, or closure.

## Run the checks

~~~bash
python3 herramientas/verificar.py
python3 ejemplos/comprobaciones.py
~~~

These commands use the Python standard library. They print reports to standard output; save the results only when recording a new review.

## Publication

This edition is published at [EndlessMonkeyProyect/programa-geometria-relacional](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional). This edition does not assign an open license by default. The first commit documents editorial organization; it does not establish the original discovery date of the results.
