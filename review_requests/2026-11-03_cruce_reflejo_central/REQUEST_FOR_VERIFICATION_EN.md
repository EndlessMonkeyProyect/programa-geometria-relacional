---
title: "Request for Independent Verification"
subtitle: "The Cross as Central Reflection · Relational Geometry Program"
author: "Le Matt Ansatz Di Ego"
date: "November 3, 2026"
lang: en
---

# Request for Independent Verification

**The Cross as Central Reflection — Tetrahedron, cube, and composition cost against the subexponential 3-SAT algorithms**

Le Matt Ansatz Di Ego · Relational Geometry Program · November 3, 2026

---

## 1. What is requested

We request independent verification of **three things, separated and with different standards**:

| # | Object of verification | Standard | Scope |
|---|---|---|---|
| V1 | Computational reproducibility (5 verifiers) | Execution and result comparison | Fully machine-checkable |
| V2 | Correctness of Propositions 1–3 and Corollary 4 (§7 of the paper) | Mathematical proof | Short proofs, classical algebra |
| V3 | Documentary precedence (§1 of "La caja de espejos" v0.3) | Commit/date evidence | Requires GitHub, Software Heritage or Zenodo access |

**We do not request** verification of the OpenAI or Anthropic results. Those works are taken as a *cited external premise*; auditing them is the responsibility of their authors and the community. Nor do we request recognition of priority: this material claims none.

---

## 2. V1 — Computational reproducibility

### 2.1 How to reproduce

From the `2026-11-03_cruce_reflejo_central` folder of the repository:

```bash
pip install -r requirements.txt        # numpy (>=1.24)
bash reproducir_todo.sh                 # ~40 s
```

`reproducir_todo.sh` runs the five verifiers, writes into `resultados/` and compares against `referencia_resultados/`. It exits with code 0 **only if** all five match (exact integers; decimals with relative tolerance 1e-9).

### 2.2 The five verifiers

| Verifier | What it checks |
|---|---|
| `verificacion/experimento_cruce_dos_cortes.py` | D1 (I − 2P₋) versus D2 (P₊ − P₋) for t = 1…5; closed formulas; D1 limit up to t = 10 000; eight-squares control |
| `verificacion/experimento_tetraedro.py` | The 7 order-4 subgroups; Q8 signs; Bell states, center and four crosses; D1 cost |
| `verificacion/verificar_cadena_duplicacion.py` | Levels 2, 4, 8, 16 of Cayley–Dickson: identity (28), R + C = 2·cross, two orders, ranks, Lemma 2 cost, associativity |
| `verificacion/verificar_particiones.py` | Partitions: Hardy–Ramanujan, log-concavity (DeSalvo–Pak), self-conjugates, Heisenberg relation, part families |
| `verificacion/verificar_origen_tetraedro.py` | The tetrahedron from the origin in bits; the crosses at the origin; face-centered cubic lattice, diamond and E8 |

### 2.3 Integrity

The SHA256 hashes of all files are in `MANIFIESTO_SHA256.txt`. Verify with:

```bash
sha256sum -c MANIFIESTO_SHA256.txt   # Linux/macOS
```

### 2.4 Reference result

- **Reference environment:** Python 3.13.18, numpy 2.5.3, Linux (`entorno.json`).
- **Cross-platform reproduction already performed by DeepSeek, an AI model (2026-11-03):** Windows, Python 3.12.14, numpy 2.3.5 → the 4 verifiers regenerated results identical to the reference and `comparar_resultados.py` returned 0; the 26 files matched their hashes.

**Success criterion for the reviewer:** the 5 JSONs match and every file's hash matches. No [E] number depends on the operating system.

---

## 3. V2 — Mathematical correctness

We ask for review of the four proofs in §7 of the paper. They are short and use classical algebra.

**Proposition 1.** At levels 2, 4 and 8 of the Cayley–Dickson doubling, R + C = 2·[x=v][y=u]. *(Proof: multiplicativity of the norm — Hurwitz 1898 — and identity (28).)*

**Proposition 2.** R = (Lᵥᵀ Lₓ)ᵤ,ᵧ and C = (Lₓᵀ Lᵥ)ᵤ,ᵧ, with Lᵥᵀ Lₓ + Lₓᵀ Lᵥ = 2[x=v]·Id (Hurwitz–Radon relations).

**Proposition 3.** With the Lemma 2 count, one block costs 4/4, 8/8 and 11/12 bits at levels 2, 4 and 8; at the 16, identity (28) fails in 672 cases.

**Corollary 4.** Within the chain, the only level that makes it cheaper is the 8, and the 8 is not associative (Frobenius 1878).

**Points we ask to be reviewed with particular attention:**

1. The step "R² = N·R ⇒ rank of R by rows = N" (Proposition 3): is it correct that ΦΦᵀ = N·Id implies rank N?
2. The claim "the rank of R by columns is that of C by rows" and its value (N² if N ≠ 2; 2 if N = 2).
3. The count of 168 of 210 triples with path-dependent sign at level 8.
4. The claim that every later level of the doubling contains the 16 as a subalgebra with the same sign table.

**Success criterion:** confirm or refute each proposition, with an explicit correction if any.

---

## 4. V3 — Documentary precedence

What the paper asserts about dates is **the following, and nothing more**:

- The reclosure (MF-63B) and interface composition are **public before October 16** (RGP commits `c44cfb8` of Oct 3 and `6e36993` of Oct 9).
- The **counting** documents and the **octonion note** have internal dates of Oct 13–16 and were made public on **October 24**: before the announcements, after the day of discovery.
- The **origin of the tetrahedron**: the capsule {A, JA, −A, −JA} and the resolution of a binary indefiniteness with σ = ±1 are public since **September 29** (PGR `fb27fbf`, sources F024 and F056). The tetrahedron of references appears explicitly in O19 (dated October 19) and in CME-003, public since October 24 (`0fd5315`).

**What we ask to verify** (not to assume):

1. The **upload time** of each commit according to GitHub (the date written in the document is not enough).
2. The presence of each cited file in the indicated commit.
3. A copy in **Software Heritage** or a **Zenodo deposit with DOI**, if definitive precedence is wanted.
4. **Archived captures** of the two Reddit publications (Oct 3 and 9).

**Success criterion:** confirm or correct the table in §1 of "La caja de espejos" v0.3 with verifiable evidence.

---

## 5. What is NOT claimed (so the reviewer wastes no time)

1. **No** algorithm of our own.
2. **No** priority over the techniques of OpenAI or Claude.
3. **No** claim that one laboratory used materials from the other or from the program.
4. **No** proof of the validity of the OpenAI/Anthropic results.
5. **No** claim that the correspondences (levels I–III) reconstruct the algorithms or their bounds (level IV, open).

The level I–III correspondences are **classical theorems expressed in the program's language** (variable elimination; Hurwitz–Radon; octonions). Their value is not novelty, but the reading and the measurement.

---

## 6. The four questions this request answers in advance

So the reviewer does not have to ask them, we answer here:

1. **Is this material the same algorithm as OpenAI's or Claude's?** No. The three reach related conclusions by different routes, and this material presents no algorithm. OpenAI and Claude give algorithmic constructions with bounds; this document measures and locates the piece (the cross) they decompose.

2. **Did the program "get there first"?** In one precise sense, yes: the public statement of relational closure and interfaces is from October 3, before the announcements. In the sense that matters, no: the program did not publish the subexponential algorithm, and its own note N1 proves its engine is exponential, so it cannot claim the exit.

3. **Are the program's results equivalent to OpenAI's or Claude's?** Not proved: it is level IV, open. Moreover, the reclosure is contraction along a single tree, a model with an unconditional exponential lower bound (Austrin, Kaski and Kubjas, 2022), and N1 proves that the program's table engine costs 2^Ω(n) on random graphs. Neither, as it stands, can be a subexponential algorithm.

4. **Is the program's closure polynomial?** One concrete operation — the diamond closure in 3-coloring (R-04, October 30 review request, PGR `a1d3f16`) — is polynomial. It does not fire on triangle-free graphs, where 3-coloring remains NP-complete. That proves the efficiency of one operation, not of a general solution to 3-SAT or 3-coloring.

**In one line:** the program had pieces of the terrain and diagnosed the limit of its own engine; three exact correspondences with Claude's algorithm were established a posteriori; it did not reach the solution, and claims neither priority nor equivalence.

**Review of §7 by DeepSeek (2026-11-03).** In addition to the V2 verification requested here, DeepSeek, an AI model, re-derived with its own implementation, not using the package's verifiers, Propositions 1–3 and Corollary 4 with exact integers and confirmed the "168 of 210" count: the proofs have no errors. Being a check by an AI model, it does not replace the human review requested in V2. Report: `revision_pruebas_sec7_DeepSeek.md` (in Spanish); script: `review_pruebas_sec7.py`, in this same folder.

---

## 7. Open questions (level IV) we would welcome the reviewer to consider

1. Can the program **derive** 1/√2 (or a ρ < 11/12) from its own language, rather than postulating the doubling?
2. Is there a **family of parts** with operators satisfying Lemmas 9 and 10 of Claude's paper that yields ρ < 1/√2 (for example, squares, α = 1/3, ρ ≈ 0.63)?
3. Is there a **map** carrying the parity of the moved mirror (§3) to a cut (§5) that preserves ranks?

---

## 8. How to report

- **V1:** attach the output of `bash reproducir_todo.sh`, the output of `sha256sum -c MANIFIESTO_SHA256.txt`, and the exact Python and numpy versions.
- **V2:** mark each proposition as *correct*, *correct with a note*, or *incorrect*, with the correction.
- **V3:** attach captures or links of the commits/files, with their upload times.

The complete material (paper, notes, verifiers and results) is in the `2026-11-03_cruce_reflejo_central` folder of the repository.

---

*Status of this document: request open to independent review. It constitutes neither a precedence statement nor a priority claim.*
