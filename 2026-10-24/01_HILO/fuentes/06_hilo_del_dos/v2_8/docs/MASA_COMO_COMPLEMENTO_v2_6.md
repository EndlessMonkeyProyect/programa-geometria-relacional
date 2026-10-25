---
title: "La masa como complemento de la proyección: el modelo fundacional en su texto"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; precisión de la v2"
version: "2.6 — 2026-10-13"
status: "Definición exacta + contraste falsado con una sola escala + regla de escala abierta"
---

# La masa como complemento de la proyección

> **Pedido del autor (13-10-2026).** Remitirse al modelo fundacional, donde la masa es
> la parte complementaria de la proyección y las frecuencias sólo aparecen como
> comparaciones, antes de dar algo por falsado.

La v2 llamó «masa por frecuencias» a lo que falsó. Esta nota lo precisa: lo falsado es
el complemento usado con **una sola escala** para todas las partículas. El complemento
en sí es una definición exacta. Pruebas: `tests/test_masa_complemento_v2_6.py`.

## 1. Los textos

**Capa ontológica, §9 «El espacio que queda»** (reconstrucción v0.29 desde las
posiciones del autor y la exploración fundacional):

> Una fracción nunca está vacía, porque es una escala. La proyección es la parte que se
> refleja respecto de la luz. El complemento es lo que la imagen sostiene frente a las
> demás, y se lee como masa. El modo confinado no es una cara independiente: es la
> diferencia entre la proyección y la totalidad. Como la proyección y el complemento son
> dos referencias irreducibles —una a la luz y otra a las demás proyecciones—, la unidad
> se conserva en el cuadrado: ‖V‖² + ‖m‖² = 1.

**`fotografia_narrativa_y_verificacion.md`, §21.1 y §20.5:**

> con la partición ω_U² = ω_V² + ω_m², y r_V = 2⁻ⁿ, r_m = (2ⁿ−1)/2ⁿ […] m_p corresponde
> por P2 al modo de confinamiento, de modo que λ̄_p = ℏ/(m_p c) es R_m y no R_U.

Regla de anclaje: «Compton entra una sola vez».

**Formalización v1, §30:**

> r_m = ω_m²/ω_U², m_* := ℏω_U/c², m_fis := ℏω_m/c². Entonces algebraicamente:
> m_fis(h) = m_*·√(1−2⁻ʰ).

**«Relational Architecture of Hadrons and Leptons» v4.3:** P2, (m/m*)² = r_m; P4,
r_m(H) = Σ nᵢ r_m,ᵢ, de donde M_H = m*·√(Σ nᵢ r_m,ᵢ); calibración de m* con el protón,
de r_u y r_d con protón y neutrón, y de r_s con la Ω⁻.

## 2. Lo exacto `DERIVADO`

Con E = ħω_U, pc = ħω_V y mc² = ħω_m, la partición es la relación relativista:

```text
ω_U² = ω_V² + ω_m²   ⟺   E² = (pc)² + (mc²)²,     r_V = β²,   r_m = 1/γ²
```

La masa como complemento es la fracción de la energía que no se va en movimiento. La luz
tiene complemento cero. Es una identidad: no se ajusta y no puede falsarse.

## 3. Lo falsado `CONTRASTE`

Con una sola escala m* y profundidad binaria, m = m*·√(1 − 2⁻ʰ): dos masas difieren a
lo sumo √2. El muón pesa 206.77 veces el electrón y el tau 3477.4 (PDG 2025). Falsado.

| Intento | Resultado |
|---|---|
| Radio del protón, ruta A: 4λ̄_p = 0.841236 fm | +0.76σ frente a CODATA 2022; fórmula ya publicada (Haramein 2013; Trinhammer y Bohr 2019): indicio, no predicción |
| Radio del protón, ruta B: √15·λ̄_p = 0.8145 fm | −41σ: falsado |
| Hadrones v4.3 | En otros once bariones no supera a masas constituyentes lineales |
| Leptones con r_m = 2⁻ⁿ | Profundidades no enteras: electrón 23.53, muón 8.14 |

## 4. Lo que falta `ABIERTO`

La razón de masas entre dos singularidades es

```text
m₁ / m₂ = (ω_U₁ / ω_U₂) · √(r_m₁ / r_m₂)
```

El complemento fija el segundo factor. El primero, la escala de cada singularidad, no
sale todavía de la estructura: «R es siempre una escala» marca dónde tiene que salir.
Prueba fijada de antemano: un parámetro fijado con μ/e que prediga τ/e sin tocarlo.

## Matriz

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| ‖V‖² + ‖m‖² = 1 es E² = (pc)² + (mc²)² con r_V = β², r_m = 1/γ² | DERIVADO | `test_particion_es_la_relacion_relativista` |
| Con una sola escala y h ≥ 1, dos masas difieren a lo sumo √2 | DERIVADO | `test_una_sola_escala_acota_la_razon` |
| La razón de masas es (ω_U₁/ω_U₂)·√(r_m₁/r_m₂) | DERIVADO | `test_razon_de_masas_separa_escala_y_complemento` |
| Masa como complemento con una sola escala describe los leptones | FALSADO | §3 |
| Regla de escala por singularidad | ABIERTO | — |
