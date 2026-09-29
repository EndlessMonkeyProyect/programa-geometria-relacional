# Data and experiments

The result files are kept in `fuentes/originales` to maintain one reference copy of each attachment. The links below point to the bytes received.

| Data | Contents | Limitation |
|---|---|---|
| [mf53_obdd_normalization_summary.json](../fuentes/originales/mf53_obdd_normalization_summary.json) | Threshold, parity, HWB, and equality-order checks. | The original code and MF-53 manuscript are not included. |
| [mf53_equality_order.csv](../fuentes/originales/mf53_equality_order.csv) | Eight rows of OBDD sizes for two orders. | A poor order is not a lower bound for all methods. |
| [mf54_local_information_summary.json](../fuentes/originales/mf54_local_information_summary.json) | Contextual classes, corrected threshold, parity, and reported checks. | The test counts are not regenerated from seeds in this edition. |
| [mf55_transition_rule_summary.json](../fuentes/originales/mf55_transition_rule_summary.json) | Novelty, resolution, and transition in finite examples. | It does not select physical events. |
| [capsule_width_results_v0_79.json](../fuentes/originales/capsule_width_results_v0_79.json) | Residual widths for controls and planted 3-CNF instances. | Small experiments; no asymptotic guarantee. |
| [gamma_reference_results_v0_80.json](../fuentes/originales/gamma_reference_results_v0_80.json) | Seven controls and 24 stress instances. | The laboratory optimum is not the selector's cost. |

## Historical validations

The 14 available VALIDATION files remain in the [catalog](../fuentes/CATALOGO.en.md). They include reported tests of known algorithms, finite identities, counterexamples, and numerical checks. “PASS” is the status declared by the source, not a physical validation or a fresh reproduction of all tests.

## Verification in this edition

The integrity script parses JSON and CSV and compares the common MF-53 rows. It recomputes the 14 successes against the reported optimum in v0.80. It neither reconstructs absent formulas nor independently certifies the stored optima.

The [editorial examples](../ejemplos/README.en.md) are small independent checks that do run in this edition. They are not presented as recovered historical code.

## For future full reproduction

Add the original scripts, dependency versions, seeds, complete instances, parameters, tolerance criteria, and run commands, with provenance. Some sources refer to `results/computation`; those files were not attached and are recorded as missing.
