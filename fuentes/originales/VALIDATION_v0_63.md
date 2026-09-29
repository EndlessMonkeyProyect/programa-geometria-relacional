# VALIDATION v0.63 — regla de transición ontológica

**Estado:** PASS para los teoremas finitos ensayados. La selección del siguiente evento permanece OPEN.

## 1. Comparación binaria: cota de un bit

Pruebas: **1000**  
Fallos: **0**

## 2. Fórmula exacta de división binaria

\[
N'=N+s_c.
\]

Pruebas: **1000**  
Fallos: **0**

## 3. Criterio de factorización

\[
\nu_c=0
\iff
c\text{ es constante sobre cada clase previa}.
\]

Pruebas: **1000**  
Fallos: **0**

## 4. Resolución no crea clases

Pruebas: **1000**  
Fallos: **0**

## 5. Identidad novedad–resolución

\[
\nu_X-\nu_{X'}
=
\rho_{\mathcal C'}-\rho_{\mathcal C}.
\]

Pruebas: **1000**  
Fallos: **0**

## 6. Ejemplo de orden

```json
{
  "initial_classes": 2,
  "initial_I": 1.0,
  "after_enrichment_classes": 4,
  "after_enrichment_I": 2.0,
  "final_classes": 2,
  "final_I": 1.0,
  "restrict_first_classes": 2,
  "restrict_first_I": 1.0,
  "novelty_if_enrich_first": 1.0,
  "resolution_after_enrich": 1.0,
  "resolution_if_restrict_first": 0.0,
  "novelty_after_restrict": 0.0,
  "net_change": 0.0
}
```

## 7. Umbral local, n=8, k=4

```json
[
  {
    "t": 0,
    "remaining_future_bits": 8,
    "prefix_realizations": 1,
    "distinguishable_boundary_states": 1,
    "I_rel_bits": 0.0,
    "theta_values": "4"
  },
  {
    "t": 1,
    "remaining_future_bits": 7,
    "prefix_realizations": 2,
    "distinguishable_boundary_states": 2,
    "I_rel_bits": 1.0,
    "theta_values": "3|4"
  },
  {
    "t": 2,
    "remaining_future_bits": 6,
    "prefix_realizations": 4,
    "distinguishable_boundary_states": 3,
    "I_rel_bits": 1.584962500721156,
    "theta_values": "2|3|4"
  },
  {
    "t": 3,
    "remaining_future_bits": 5,
    "prefix_realizations": 8,
    "distinguishable_boundary_states": 4,
    "I_rel_bits": 2.0,
    "theta_values": "1|2|3|4"
  },
  {
    "t": 4,
    "remaining_future_bits": 4,
    "prefix_realizations": 16,
    "distinguishable_boundary_states": 5,
    "I_rel_bits": 2.321928094887362,
    "theta_values": "0|1|2|3|4"
  },
  {
    "t": 5,
    "remaining_future_bits": 3,
    "prefix_realizations": 32,
    "distinguishable_boundary_states": 5,
    "I_rel_bits": 2.321928094887362,
    "theta_values": "-1|0|1|2|3"
  },
  {
    "t": 6,
    "remaining_future_bits": 2,
    "prefix_realizations": 64,
    "distinguishable_boundary_states": 4,
    "I_rel_bits": 2.0,
    "theta_values": "-1|0|1|2"
  },
  {
    "t": 7,
    "remaining_future_bits": 1,
    "prefix_realizations": 128,
    "distinguishable_boundary_states": 3,
    "I_rel_bits": 1.584962500721156,
    "theta_values": "-1|0|1"
  },
  {
    "t": 8,
    "remaining_future_bits": 0,
    "prefix_realizations": 256,
    "distinguishable_boundary_states": 2,
    "I_rel_bits": 1.0,
    "theta_values": "-1|0"
  }
]
```

## 8. No implica

- una ley que determine cuál evento ocurre;
- una dinámica física;
- que una nueva clase matemática sea una nueva dimensión espacial;
- que toda información sea binaria;
- \(P=NP\).
