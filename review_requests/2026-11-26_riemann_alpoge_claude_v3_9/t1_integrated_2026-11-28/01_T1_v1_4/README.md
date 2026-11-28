# Anexo T.1 — versión 1.4

**Endless Monkey Project / Relational Geometry Program**  
28 de noviembre de 2026 · extensión propuesta para Nota técnica 01 v3.9 / Issue 16.

## Alcance

Conserva las secciones 1–7 de v1.3 con precisiones editoriales y matemáticas, y añade §8, «Reflexión iterada: recuperación por momentos». La nueva formulación establece:

- Proposición 9: ηₚ = Σⱼ≥₀ ⟨z,Tʲz⟩, con m₀=μₚ y cola relativa acotada por q^(k+1).
- Proposición 10: cota direccional mejorada Lₚ = m₀ + m₁²/(m₁−m₂) ≥ γₚ^G, con convención 0/0=0.
- Teorema 3: RH equivale a la divergencia de las recuperaciones truncadas Rₚ,ₖₚ con profundidad adaptada por q^(kₚ+1) ≤ 1/2.
- Identidad de economía: Kₚ^H = −½ log det(I−T). Se obtiene un límite de profundidad suficiente, no una complejidad uniforme.
- Siete etapas verificadas (2 a 17): la cota Rₚ,₄, reescalada por p, resulta entre 1.00913 y 3.74593; Lₚ conserva entre aproximadamente 68.5% y 100% de la ganancia exacta. Son resultados numéricos, no certificados por intervalos.

La divergencia global, la transferencia automorfa y RH incondicional permanecen abiertas. La equivalencia de §7 se cotejó contra los artículos de Báez-Duarte [2002, primera versión](https://arxiv.org/abs/math/0202141) y [segunda versión](https://arxiv.org/abs/math/0205003). La extensión usa herramientas clásicas de proyecciones ortogonales, complemento de Schur y series de Neumann; su aplicación en esta cadena se ofrece a corroboración, sin reclamo de prioridad.

## Cambios de precisión

- μₚ es la fracción reconocida; pμₚ es el reconocimiento reescalado.
- La condición (12) es suficiente y da una mejor cota de velocidad que la cota publicada citada; no se demuestra que sea estrictamente más fuerte que RH.
- Los cálculos lineales de 40 dígitos utilizan entradas de doble precisión.
- Se especifican casos de acoplamiento cero, y se distingue el dilatador unitario de las reflexiones involutivas.
- Los controles Lean y los scripts externos v3.9 se conservan como antecedentes declarados por v1.3; no se vuelven a ejecutar ni se incluyen en este paquete.

## Reproducción

Requisitos: Python 3, NumPy >= 1.24; mpmath opcional para el control lineal de 40 dígitos. LaTeX opcional para recompilar. Desde el directorio de este paquete, verificar primero el manifiesto:

```bash
sha256sum -c SHA256SUMS
python -m pip install -r requirements.txt
python verificacion_independiente_T1.py
python verificar_reflexion_iterada.py
```

Los scripts generan JSON; pueden producir diferencias de representación o redondeo por plataforma y bibliotecas. Para mantener la integridad archivada, ejecutar en una copia del directorio. El segundo script incluye aserciones de consistencia entre Schur, momentos, cotas, colas y costo angular. Reutiliza la fórmula de Vasyunin del primer script; no es una integración independiente adicional.

Para compilar el PDF:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Anexo_T1_Herencia_y_transferencia_v1_4.tex
pdflatex -interaction=nonstopmode -halt-on-error Anexo_T1_Herencia_y_transferencia_v1_4.tex
```

## Incorporación al repositorio

Véase `INSTRUCCIONES_ADMIN.md`. Se propone un PR en borrador para revisión técnica; no sustituir el histórico v1.2/v1.3 ni la Nota técnica 01 v3.9. No se ha modificado el repositorio remoto.
