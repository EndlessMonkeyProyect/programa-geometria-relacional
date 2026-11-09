# La economía del cálculo desde las relaciones entre referencias
# The economy of computation from relations between references

Endless Monkey Project  
Relational Geometry Program

8 de noviembre de 2026 · versión 2 / November 8, 2026 · version 2

[Español](#español) · [English](#english)

---

## Español

La pregunta es si la economía del cálculo puede surgir de las relaciones entre referencias (distinciones, herencia, novedad, reunión y reapertura), y qué se puede demostrar con esa ontología. El informe responde con pruebas, contraejemplos, un laboratorio reproducible y el contraste con los trabajos de octubre de 2026 sobre 3-SAT.

### Resultados en breve

- Las distinciones que deben quedar activas para responder con exactitud son el rango de la relación entre lo decidido y lo pendiente. Las fija la frontera.
- La ley de herencia mcm/mcd es el teorema chino del resto. Pide que las referencias permuten (reflexión x − y + z) y que la covarianza entre bloques sea nula; con permutación, la desviación es exactamente k²·Cov(p_J, q_J).
- Una referencia válida para cualquier futuro no puede reunir configuraciones. En grafos expansores, todo orden tiene algún corte con 2^Ω(n) distinciones.
- En una fórmula de Tseitin satisfacible, el rango de corte es 2^λ(A), con λ la función de conectividad del matroide gráfico: el teorema del espacio de estados de Forney en el lenguaje del programa.
- Hay economía exacta con separadores, reflexión y simetría: en el hipercubo, 2^n estados quedan en n + 1 clases; en la rejilla de tres colores de ancho 10, 1536 → 136 → 51: la sucesión de conteos admite una representación lineal mínima de dimensión 51 sobre los racionales, certificada en exacto. Para los anchos 1 a 10 los órdenes mínimos son 1, 1, 2, 3, 5, 7, 13, 19, 35, 51.
- En óptica, la distinción ℓ-ésima se funde a una distancia R ∝ ε^(−1/ℓ). Pendientes medidas: 0,998 · 0,499 · 0,333 · 0,253. La última distinción antes de que todo se reúna en un punto es el dipolo, un ±.
- Los algoritmos de octubre de 2026 coinciden en dónde está la economía (cambio de referencia y teorema chino del resto; reflexión con signo) y difieren en cómo: cambian la referencia o cancelan con signo.

El estado de cada afirmación (resuelta, abierta, superpuesta o cerrada antes de tiempo) está en la sección 10 del informe. La solicitud de revisión está en [`review_requests/2026-11-08_economia_del_calculo`](../review_requests/2026-11-08_economia_del_calculo/LEER_PRIMERO.md).

### Archivos

| Archivo | Contenido |
| --- | --- |
| `informe.md` · `report.md` | El informe completo, en español y en inglés |
| `CAMBIOS.md` | Cambios de la versión 2 y su justificación |
| `encargo.md` · `brief.md` | El encargo de investigación al que responde, en español y en inglés |
| `laboratorio_economia_relacional.py` | Laboratorio reproducible: experimentos E1 a E12, más E5x y E5c |
| `resultados_laboratorio.json` | Resultados de la corrida de referencia |
| `fusion_optica.png` · `optical_fusion.png` | Figura de la ley de fusión óptica (E6), en español y en inglés |
| `requirements.txt` | Dependencias |

### Reproducir

```
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py                # todo, unos 4 minutos
python3 -I laboratorio_economia_relacional.py E5 E5x E5c     # la rejilla y su certificado
```

### Fuentes de la comparación

La lectura de los trabajos de OpenAI y Anthropic se basa en sus resúmenes públicos y en el README de Anthropic. Al 8 de noviembre de 2026 sus pruebas en Lean estaban reproducidas por terceros y la revisión experta seguía pendiente. Si las dos versiones del informe difieren, la referencia es el texto en español.

---

## English

The question is whether the economy of computation can arise from the relations between references (distinctions, inheritance, novelty, gathering and reopening), and what can be proven with that ontology. The report answers with proofs, counterexamples, a reproducible lab and a comparison with the October 2026 work on 3-SAT.

### Results in brief

- The distinctions that must stay active to answer exactly are the rank of the relation between what has been decided and what is pending. They are set by the boundary.
- The lcm/gcd inheritance law is the Chinese remainder theorem. It requires the references to permute (reflection x − y + z) and zero covariance between blocks; under permutation, the deviation is exactly k²·Cov(p_J, q_J).
- A reference valid for every future cannot gather configurations. On expander graphs, every order has some cut with 2^Ω(n) distinctions.
- For a satisfiable Tseitin formula, the cut rank is 2^λ(A), with λ the connectivity function of the graphic matroid: Forney's state space theorem in the program's language.
- There is exact economy with separators, reflection and symmetry: in the hypercube, 2^n states fall into n + 1 classes; in the three-colour grid of width 10, 1536 → 136 → 51: the counting sequence admits a minimal linear representation of dimension 51 over the rationals, certified exactly. For widths 1 to 10 the minimal orders are 1, 1, 2, 3, 5, 7, 13, 19, 35, 51.
- In optics, the ℓ-th distinction merges at a distance R ∝ ε^(−1/ℓ). Measured slopes: 0.998 · 0.499 · 0.333 · 0.253. The last distinction before everything gathers into one point is the dipole, a ±.
- The October 2026 algorithms coincide on where the economy is (change of reference and Chinese remainder theorem; signed reflection) and differ in how: they change the reference or cancel with signs.

The status of each claim (resolved, open, superposed or prematurely closed) is in section 10 of the report. The review request is in [`review_requests/2026-11-08_economia_del_calculo`](../review_requests/2026-11-08_economia_del_calculo/README.md).

### Files

| File | Content |
| --- | --- |
| `informe.md` · `report.md` | The full report, in Spanish and in English |
| `CAMBIOS.md` | Version 2 changes and their reasoning |
| `encargo.md` · `brief.md` | The research brief it answers, in Spanish and in English |
| `laboratorio_economia_relacional.py` | Reproducible lab: experiments E1 to E12, plus E5x and E5c |
| `resultados_laboratorio.json` | Results of the reference run (keys in Spanish) |
| `fusion_optica.png` · `optical_fusion.png` | Figure of the optical fusion law (E6), in Spanish and in English |
| `requirements.txt` | Dependencies |

### Reproduce

```
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py                # everything, about 4 minutes
python3 -I laboratorio_economia_relacional.py E5 E5x E5c     # the grid and its certificate
```

### Sources of the comparison

The reading of the OpenAI and Anthropic works is based on their public summaries and on Anthropic's README. As of November 8, 2026 their Lean proofs had been reproduced by third parties and expert review was still pending. If the two versions of the report differ, the Spanish text is the reference.
