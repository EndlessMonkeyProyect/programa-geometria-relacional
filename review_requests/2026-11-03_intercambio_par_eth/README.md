# Request for independent review · The pair swap in both ETH refutations · November 3, 2026

[Español](LEER_PRIMERO.md)

## Priority review · editorial update of November 4, 2026

We first request a focused human assessment: **are Propositions 1, 2, 4 and 5 and Corollary 3 of the proof note correct, and do they faithfully represent the cited constructions?** A second question concerns precedents for the exact formulas or this comparison. Corrections and references are welcome, even for a single claim.

Replies can be collected in the [dedicated review thread](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4). Documentary chronology remains a separate question. A consequence for either bound remains open; a response on that point should identify a concrete inequality or reduction.

### Reproduce the archived delivery

```bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
cd programa-geometria-relacional
git checkout --detach 46e47274e9e573b9c91da1516d067c4f49c289f9
python -m pip install -r 2026-11-03_cruce_reflejo_central/requirements.txt
python review_requests/2026-11-03_intercambio_par_eth/verificar_pieza_compartida.py
```

The commit corresponds to tag `2026-11-03-pair-swap-review`. These commands use `python` on Windows; use `python3` on systems that require it. They fix the reviewed content; dependencies retain the range declared in `requirements.txt`. Previously used environments are recorded in the request and archived output. Section 6 of the full request describes the other verifiers.

**Fixed sources:** [OpenAI, commit `42907c9`](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) · [Anthropic, commit `16a5ce4`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf).

## Wider scope of the request

We request independent review of three things, with different standards:

1. **Documentary precedence.** What the program had made public before October 16, using independently dated records of the relevant content.
2. **The shared piece.** Whether the pair swap is the same local operator in OpenAI's and Anthropic's algorithms, and whether the related binomial counts for Anthropic's one-bit ranks and OpenAI's explicit measurement rows matter for either bound.
3. **Explanatory power.** Whether the framework derives any of this or only describes it.

We claim no priority and no algorithm of our own, and we do not assess the validity of the two refutations. The chronology rests on commit metadata and still needs independent timestamps.

| File | What it is |
| --- | --- |
| [`REVIEW_REQUEST_EN.md`](REVIEW_REQUEST_EN.md) | The full request |
| [`SOLICITUD_REVISION.md`](SOLICITUD_REVISION.md) | Spanish edition |
| [`PROOF_NOTE_3_3_EN.md`](PROOF_NOTE_3_3_EN.md) | Proof of the formulas of Section 3.3 for every t |
| [`NOTA_PRUEBA_3_3.md`](NOTA_PRUEBA_3_3.md) | Spanish edition of the proof note |
| [`verificar_pieza_compartida.py`](verificar_pieza_compartida.py) | Numerical checks for Section 3.3; numpy only, under a second |
| [`salida_verificador_2026-11-03.txt`](salida_verificador_2026-11-03.txt) | Its output, with versions and the script's hash |
| [`MANIFIESTO_SHA256.txt`](MANIFIESTO_SHA256.txt) | SHA-256 hashes of these files |

Run the checks with `python verificar_pieza_compartida.py`. Replies are welcome as [issues](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4).
