# When Is Recognition Cheaper Than Computation?

**Request for Independent Mathematical and Computational Review**

November 14, 2026

**Public author:** Le Matt Ansatz Di Ego

## Abstract

A structure may contain relations already determined by other relations. Recognizing what is inherited can eliminate repeated computation, but recognition itself has a cost.

Recent results examine this trade-off through exact counting, parity constraints, structural recognition, information preservation, and reconstruction.

The central question is:

**Under what conditions does recognizing inherited structure reduce the total computational cost of producing an exact answer?**

Independent examination is invited to establish the conditions under which these savings occur, identify their limitations, and determine whether they extend beyond the currently tested families.

## 1. Definitions and Cost Model

The construction distinguishes four elements:

- **Reference:** a collection of relations from which other relations can be reconstructed.
- **Inheritance:** relations already implied by the reference.
- **Novelty:** constraints that introduce distinctions not yet resolved.
- **Economy:** a measurable reduction in computational work while preserving the exact answer.

For an algorithm that recognizes and uses a reference, total cost is:

$$
C_{\mathrm{total}} =
C_{\mathrm{recognition}}+
C_{\mathrm{verification}}+
C_{\mathrm{computation}}+
C_{\mathrm{reconstruction}}.
$$

Against a baseline algorithm $B$, net savings occur when:

$$
C_{\mathrm{total}}(F)<C_B(F),
$$

for the same input, output requirement, and cost model.

Representation size, execution time, memory consumption, and reconstruction cost are examined separately.

## 2. Established and Measured Results

The November 10 manuscript, *What Computation Becomes Unnecessary?*, establishes an exact counting procedure for systems containing explicitly given parity equations and remaining disjunctive clauses.

Under the stated hypotheses, its running-time bound is

$$
O\left(\operatorname{poly}(L)
\left(1+2^{\min(t,d)}\right)\right),
$$

where $L$ is the input length, $d$ is the number of free parameters after closure, and $t$ is the number of remaining clauses not implied by that closure.

A separate recognizer identifies parity relations hidden inside specific families of Boolean gate constructions.

For a tested family with 96 primary variables and long-range connections:

| Method | Measured time |
|---|---:|
| Recognition and exact counting | 12.8 ms |
| Generic variable elimination | 247.0 ms |
| Observed speedup | 19.3× |

The recognizer also processes an instance with 256 primary variables and 4,076 clauses in 58 ms. At that size, the reported width estimate for generic elimination is $2^{58}$; the measured baseline extends through 96 primary variables.

The published experiments include 23 measured formulas and an additional contract test over 5,889 formulas, with exact-count agreement on all accepted instances in the reported controls.

Other experiments quantify cases where direct computation is faster than an alternative representation.

These measurements concern specified algorithms, implementations, and instance families.

## 3. Recent Extensions

The November 12–13 contributions extend the investigation toward:

- Quantifying distinctions required to preserve exact answers.
- Certifying representation costs within explicitly defined classes.
- Comparing alternative algebraic representations.
- Measuring differences between solutions and the cost of recovering them.
- Identifying how changes of reference alter observable distinctions while preserving the underlying structure.

Together, these contributions support a distinction between **minimal information** and **minimal computational work**.

## 4. Questions for Independent Review

**A. Mathematical correctness**

Verify the stated counting bounds, closure identities, and count-preservation conditions. Identify missing hypotheses or counterexamples.

**B. Computational reproducibility**

Reproduce the experiments, verify the counting results, and report runtime and peak memory under controlled conditions.

**C. Algorithmic comparison**

Compare the recognizer with established exact model counters, XOR-aware solvers, tree-decomposition methods, and definability-based preprocessing.

**D. Recognition overhead**

Determine conditions under which discovering and verifying a reference costs less than directly solving the original instance.

**E. Generalization and lower bounds**

Identify structural parameters that determine the savings, construct unfavorable families, and examine the possibility of lower bounds on recognition cost.

The broader question is whether exact, verifiable changes of reference can provide savings for nontrivial families of three-literal formulas without readily recognizable local templates.

## 5. Scope and Status

The available work contains four distinct categories:

- **Exact:** algebraic identities and theorems under stated hypotheses.
- **Conditional:** recognition and counting propositions restricted to specified families.
- **Experimental:** finite checks and comparative measurements.
- **Open:** generalized recognition, uniform savings, competitive lower bounds, and implications for unrestricted computational complexity.

Independent verification may establish broader results, tighter restrictions, or explicit counterexamples.

Each outcome helps identify where computation can be avoided and where its cost must remain.

## 6. Documentation

- [Main manuscript, version 0.3 — November 10](../../2026-11-10_que_calculo_deja_de_hacerse/PAPER_EN.md)
- [Code, recorded controls, and reproduction guide](REPRODUCTION.md)
- [Seven works — English summary, November 12–13](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-14-entrega-programa-7-trabajos/README_ENTREGA_2026-11-12_13.en.md) ([archived DOI](https://doi.org/10.5281/zenodo.24214053))

Independent mathematical examination, reproducible benchmarks, alternative proofs, and documented counterexamples are welcome.

**Endless Monkey Project · Relational Geometry Program**
