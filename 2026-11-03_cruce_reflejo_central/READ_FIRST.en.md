# The Cross as Central Reflection · November 3, 2026

**Relational Geometry Program** · Le Matt Ansatz Di Ego · [Español](LEER_PRIMERO.md)

**In one line.** The program had pieces of the terrain (the reclosure through interfaces, the tetrahedron, doubling by reflection and level 8) and had diagnosed the limit of its own engine. After the October announcements, three exact correspondences with Claude's algorithm (2026) were established. They are classical theorems stated in the program's language: this is not an algorithm of its own nor a priority claim, and algorithmic equivalence remains open.

## Contents

| File | What it is |
| --- | --- |
| [`articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.md`](articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.md) ([PDF](articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.pdf)) | The paper. The gain of the cross comes from splitting it across two cuts; the crosses occupy the even tetrahedron; in the doubling, only the 8 makes the cross cheaper, at the cost of associativity |
| [`articulo/El_cruce_como_reflejo_central_2026-11-03.md`](articulo/El_cruce_como_reflejo_central_2026-11-03.md) ([PDF](articulo/El_cruce_como_reflejo_central_2026-11-03.pdf)) | Spanish edition of the paper |
| [`articulo/La_caja_de_espejos_v0.3_2026-11-03_EN.md`](articulo/La_caja_de_espejos_v0.3_2026-11-03_EN.md) ([ES](articulo/La_caja_de_espejos_v0.3_2026-11-03.md)) | The program's path, with its chronology and four levels: what is proved and what remains open |
| [`articulo/Notes_2026-11-03_EN.md`](articulo/Notes_2026-11-03_EN.md) ([ES](articulo/Notas_2026-11-03.md)) | Points discussed (partitions, self-reference, open tasks) and the origin of the tetrahedron |
| `verificacion/` | Five Python 3 verifiers using numpy |
| `referencia_resultados/` | Their reference results |
| `reproducir_todo.sh`, `comparar_resultados.py` | Regenerate everything and compare with the reference |
| `requirements.txt`, `entorno.json`, `MANIFIESTO_SHA256.txt` | Dependencies, reference environment and hashes |

## The five verifiers

| Verifier | Supports |
| --- | --- |
| `experimento_cruce_dos_cortes.py` | The two cuts of the cross (paper, §5) |
| `experimento_tetraedro.py` | The tetrahedron as alphabet and as the geometry of the crosses (paper, §6) |
| `verificar_cadena_duplicacion.py` | The doubling chain: why the 8 (paper, §7) |
| `verificar_particiones.py` | Partitions and self-reference (notes, §1) |
| `verificar_origen_tetraedro.py` | The tetrahedron from the origin in bits, the crystal and E8 (notes, §2) |

## Reproduce

```bash
pip install -r requirements.txt   # numpy
bash reproducir_todo.sh           # about 45 s; exits with code 0 only if all five match the reference
sha256sum -c MANIFIESTO_SHA256.txt
```

The verifiers write their output in UTF-8, so they run the same on Windows.

## Verification

The [request for verification](../review_requests/2026-11-03_cruce_reflejo_central/REQUEST_FOR_VERIFICATION_EN.md) asks for review of reproducibility, the proofs of §7 of the paper and documentary precedence. It also contains the review of §7 carried out by DeepSeek, an AI model.

## Tags

[O] ontological · [T] proposition with proof · [C] classical result · [E] computational verification · [I] interpretative correspondence · [A] open question.

## Use of AI tools

This material was prepared with assistance from two generative AI models, Claude (Anthropic) and DeepSeek. Each document states what each one did. The author reviewed the content and takes responsibility for it.
