# La economía del cálculo desde las relaciones entre referencias
# The economy of computation from relations between references

Endless Monkey Project · Relational Geometry Program · 8 de noviembre de 2026 / November 8, 2026 · Le Matt Ansatz Di Ego

[Español](#español) · [English](#english)

---

## Español

La pregunta es si la economía del cálculo puede surgir de las relaciones entre referencias (distinciones, herencia, novedad, reunión y reapertura), y qué se puede demostrar con esa ontología. El informe responde con pruebas, contraejemplos, un laboratorio reproducible y el contraste con los trabajos de octubre de 2026 sobre 3-SAT.

### Resultados en breve

- Las distinciones que deben quedar activas para responder con exactitud son el rango de la relación entre lo decidido y lo pendiente. Las fija la frontera, no el tamaño.
- La ley de herencia mcm/mcd es el teorema chino del resto. Es exacta cuando las referencias permutan, es decir, cuando hay reflexión x − y + z.
- Una referencia válida para cualquier futuro no puede reunir configuraciones. En grafos expansores, ningún orden baja de 2^Ω(n) distinciones.
- Hay economía exacta con separadores, reflexión y simetría: en el hipercubo, 2^n estados quedan en n + 1 clases; en la rejilla de tres colores de ancho 10, 1536 → 136 → 51.
- En óptica, la distinción ℓ-ésima se funde a una distancia R ∝ ε^(−1/ℓ). Pendientes medidas: 0,998 · 0,499 · 0,333 · 0,253. La última distinción antes de que todo se reúna en un punto es el dipolo, un ±.
- Los algoritmos de octubre de 2026 coinciden en dónde está la economía (cambio de referencia y teorema chino del resto; reflexión con signo) y difieren en que no reúnen configuraciones.

No se obtiene una cota nueva de complejidad. El estado de cada afirmación (resuelta, abierta, superpuesta o cerrada antes de tiempo) está en la sección 10 del informe.

### Archivos

| Archivo | Contenido |
| --- | --- |
| `informe.md` · `report.md` | El informe completo, en español y en inglés |
| `encargo.md` · `brief.md` | El encargo de investigación al que responde, en español y en inglés |
| `laboratorio_economia_relacional.py` | Laboratorio reproducible, experimentos E1 a E12 |
| `resultados_laboratorio.json` | Resultados de la corrida de referencia |
| `fusion_optica.png` · `optical_fusion.png` | Figura de la ley de fusión óptica (E6), en español y en inglés |
| `requirements.txt` | Dependencias |

### Reproducir

```
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py        # todo, unos 4 minutos
python3 -I laboratorio_economia_relacional.py E5     # un experimento
```

### Alcance

La lectura de los trabajos de OpenAI y Anthropic se basa en sus resúmenes públicos y en el README de Anthropic; los artículos completos y el código Lean no se revisaron. Al 8 de noviembre de 2026 sus pruebas en Lean estaban reproducidas por terceros y la revisión experta seguía pendiente. Si las dos versiones del informe difieren, la referencia es el texto en español.

---

## English

The question is whether the economy of computation can arise from the relations between references (distinctions, inheritance, novelty, gathering and reopening), and what can be proven with that ontology. The report answers with proofs, counterexamples, a reproducible lab and a comparison with the October 2026 work on 3-SAT.

### Results in brief

- The distinctions that must stay active to answer exactly are the rank of the relation between what has been decided and what is pending. They are set by the boundary, not by the size.
- The lcm/gcd inheritance law is the Chinese remainder theorem. It is exact when the references permute, that is, when there is reflection x − y + z.
- A reference valid for every future cannot gather configurations. On expander graphs, no order goes below 2^Ω(n) distinctions.
- There is exact economy with separators, reflection and symmetry: in the hypercube, 2^n states fall into n + 1 classes; in the three-colour grid of width 10, 1536 → 136 → 51.
- In optics, the ℓ-th distinction merges at a distance R ∝ ε^(−1/ℓ). Measured slopes: 0.998 · 0.499 · 0.333 · 0.253. The last distinction before everything gathers into one point is the dipole, a ±.
- The October 2026 algorithms coincide on where the economy is (change of reference and Chinese remainder theorem; signed reflection) and differ in that they do not gather configurations.

No new complexity bound is obtained. The status of each claim (resolved, open, superposed or prematurely closed) is in section 10 of the report.

### Files

| File | Content |
| --- | --- |
| `informe.md` · `report.md` | The full report, in Spanish and in English |
| `encargo.md` · `brief.md` | The research brief it answers, in Spanish and in English |
| `laboratorio_economia_relacional.py` | Reproducible lab, experiments E1 to E12 |
| `resultados_laboratorio.json` | Results of the reference run (keys in Spanish) |
| `fusion_optica.png` · `optical_fusion.png` | Figure of the optical fusion law (E6), in Spanish and in English |
| `requirements.txt` | Dependencies |

### Reproduce

```
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py        # everything, about 4 minutes
python3 -I laboratorio_economia_relacional.py E5     # one experiment
```

### Scope

The reading of the OpenAI and Anthropic works is based on their public summaries and on Anthropic's README; the full papers and the Lean code were not reviewed. As of November 8, 2026 their Lean proofs had been reproduced by third parties and expert review was still pending. If the two versions of the report differ, the Spanish text is the reference.
