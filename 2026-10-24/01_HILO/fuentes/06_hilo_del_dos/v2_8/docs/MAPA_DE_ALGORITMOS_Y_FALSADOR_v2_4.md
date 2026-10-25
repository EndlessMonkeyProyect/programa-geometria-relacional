---
title: "Dónde están los algoritmos: mapa de la rama de cómputo y falsador de MF-46 §14"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; suplemento de la v2.3"
version: "2.4 — 2026-10-13"
status: "Mapa de lo ya planteado + reglas compartidas del 8 (exacto) + falsador corrido en tamaños chicos; NO demuestra P=NP ni P≠NP"
---

# Dónde están los algoritmos

> **Pedido del autor (13-10-2026).** Reflexionar sobre la conceptualización, los chats
> y los documentos para ubicar los algoritmos ya planteados; después, continuar.

Esta nota ubica cada algoritmo de la rama de cómputo (MF-1 a MF-23, MF-44B, MF-46,
MF-63B, MF-96, MF-98, MF-115, v3.1, la auditoría del 12-10 y la v2) y corre, por primera
vez, el falsador central de MF-46 §14. Código: `experiments/falsador_v2_4.py`.
Pruebas: `tests/test_falsador_v2_4.py`.

---

## 1. El principio que ordena el mapa

Un algoritmo del programa es económico por una de dos razones:

1. **Cociente chico.** La pregunta tiene pocas clases (Myhill–Nerode, T1): el contador
   truncado tiene k+2, la paridad tiene 2.
2. **Regla compartida.** Las soluciones admiten una operación que combina tres
   soluciones en otra solución (un polimorfismo). Es lo que el programa llamó «regla
   compartida» o «múltiplo común»: x ⊕ y ⊕ z para lo afín, la mayoría para 2-SAT, el
   «y» para Horn.

Cuando ninguna de las dos alcanza, el costo es exponencial en **el residuo que la regla
no cierra**, y cada algoritmo mide ese residuo con su propio parámetro.

**El 8 como ejemplo mínimo** `DERIVADO`. En el lenguaje de la v2.3:

| Relación sobre tres distinciones | Tamaño | Reglas ternarias que la conservan | Clase de Schaefer |
|---|---:|---|---|
| Destino: k = i ⊕ j (L_D) | 64 de 512 | 8, entre ellas x ⊕ y ⊕ z | Afín: tratable |
| Bit abierto: det(i, j, k) = 1 | 168 de 512 | **Sólo las tres proyecciones** | Ninguna: NP-completa como restricción |
| Las ocho 3-cláusulas con signo, juntas (MF-15) | — | Sólo las tres proyecciones | Ninguna: 3-SAT |

El bit abierto del 8, solo, no tiene ninguna regla compartida, igual que 3-SAT. El
destino sí. En la ontología: **el lenguaje de destinos cierra con una regla; el bit es
lo que ninguna regla cierra** (P5, regla R). Pruebas: `test_bit_abierto_solo_admite_proyecciones`,
`test_destino_conserva_la_regla_afin`, `test_ocho_clausulas_con_signo_solo_proyecciones`.

**Escritura del bit en el lenguaje del programa** `DERIVADO`. Tres distinciones son
independientes si y sólo si sus siete combinaciones no nulas, los siete puntos del
plano de Fano que generan, son distintas de cero. Por tanto el bit abierto se escribe
como **una capa de destinos** (cuatro combinaciones definidas por XOR) **más siete
«no es cero»**, cada uno una 3-cláusula: la relación de 7 de 8 casos que MF-46 llamó
bloque A. Prueba: `test_bit_abierto_cnf_es_independencia`.

## 2. Las cuatro zonas

### Zona 1 · Lo que cierra el lenguaje de destinos — exacto y polinómico

| Algoritmo (dónde) | Nombre conocido | Por qué es barato |
|---|---|---|
| Cápsula afín GF(2) (v1; laboratorio 12-10; v2 §19); control E1 de MF-96 | Eliminación gaussiana | Regla x ⊕ y ⊕ z |
| Contador truncado q = mín(k+1, Σ) (v3.1, MF-63B) | Contador secuencial (Sinz, 2005) | k+2 clases |
| Paridad y último bit (v3.1, economía de memoria) | Autómata finito | 2 → 4 clases |
| Controles 2-SAT y Horn (MF-15, MF-16) | Clases de Schaefer | Mayoría; «y» |
| Todas las agrupaciones de una historia del 8 (v2.3) | Programación dinámica por intervalos, O(n³); lenguajes libres de contexto | A lo sumo dos valores por tramo |
| Superelementos (propuesta del 5-10) | Complemento de Schur | Consultas lineales: k² números |

### Zona 2 · Lo que paga por el residuo, con un parámetro — exacto, costo 2^parámetro

| Algoritmo | Parámetro | Costo |
|---|---|---|
| MF-15 | Ancho de interfaz w | 2^w |
| MF-48; v3.1 §4; MF-115 C | Anchura inducida w* ≥ anchura de árbol | 2^w*; incondicional para tablas |
| MF-19, MF-53 | Ancho de OBDD = clases residuales por nivel | Número de nodos |
| MF-16 | Defecto k respecto de un núcleo tratable (*backdoor*) | 2^(ak) |
| MF-13 | Rango residual r_res fuera del núcleo afín | 2^r_res |
| MF-46 | Ventana local K | 2^O(K) |

MF-13 es la versión de fórmula de la división de T7: núcleo afín (destino) más residuo.

### Zona 3 · Búsqueda con aprendizaje — hereda las cotas del sistema de prueba

| Algoritmo | Equivale a | Cota conocida |
|---|---|---|
| Ciclo K_{t+1} = N(K_t ⋈ C) con cláusulas | Davis–Putnam / resolución | Palomar, Tseitin en expansores, 3-CNF aleatoria |
| Bifurcación con Z compartido (rama P vs NP §15) | DPLL / CDCL | Las mismas |
| Anchura de cierre (MF-44B) | Ancho de resolución | Ancho lineal ⇒ tamaño exponencial (Ben-Sasson–Wigderson) |
| Política CAG (MF-46) | Resolución + razonamiento XOR | Rango afín cero en 3-CNF aleatoria (MF-46B) |
| Lema de descenso acreditado (v3.1) | Automatizar un sistema de prueba | NP-difícil para resolución (Atserias–Müller) |

### Zona 4 · El blanco universal — equivale a P vs NP o colapsa algo mayor

- Equivalen a P = NP (v3.1 §3; MF-115 A y B): el Teorema de Acreditación Económica
  Universal, MCR-3SAT, GRN-3SAT, la O5, la cápsula canónica parametrizada por el radio
  (conjetura del 12-10) y el objetivo de v3.1.
- Sólo la existencia de un estado suficiente polinómico colapsaría la jerarquía
  polinómica (Karp–Lipton); certificados cortos para toda insatisfacible darían
  NP = coNP (Cook–Reckhow).
- Señales descartadas por el propio programa: el radio cardinal 1/|C| ({00,11} y
  {01,10}); ε_L como señal única (MF-46A); el residuo acreditativo para SAT, sin
  gradiente; representación compacta no es normalización (MF-14); la Suficiencia
  Relacional, que son las razones suficientes ya NP-difíciles.

## 3. El falsador de MF-46 §14: diseño

MF-46 §14 declara falsada la ruta como candidata general si existe una familia explícita
para la cual toda política del repertorio sufre al menos una explosión en K (ancho
inspeccionado), M (arquitectura), B (bifurcaciones) o T (trabajo).

**Repertorio declarado.**

| Método | Representa | Mide |
|---|---|---|
| DPLL con propagación unitaria | Zona 3, búsqueda | B = decisiones |
| CAG afín (aproximación) | MF-46: acredita las ecuaciones afines de bloques locales de ≤ 9 variables y hace eliminación gaussiana en cada nodo | B y rango afín acreditado |
| Davis–Putnam sin subsunción | Ciclo con cláusulas | M = máximo de cláusulas vivas (tope 20 000 o 2·10⁶ pares) |
| Tablas de frontera | Zona 2 | K = w* del orden min-fill; M = 2^w* |

**Familias.** Palomar PHP(n); Tseitin sobre 3-regulares aleatorios con carga impar;
3-CNF aleatoria con m/n = 4.26; y **restricciones del 8**: n distinciones de 3 bits,
n/5 tríos obligados a cerrar (c = a ⊕ b) y 2n tríos obligados a quedar independientes
(el bit abierto, escrito como en §1). Tres semillas por tamaño, salvo palomar.

## 4. Resultados `CONTRASTE` en tamaños chicos

B se reporta como mediana sobre las instancias insatisfacibles (costo de refutar). «≥»
marca un método detenido por su tope: el valor es una cota inferior.

**Tseitin** (n = vértices)

| n | 6 | 8 | 10 | 12 | 14 | 16 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|
| B DPLL | 15 | 31 | 63 | 127 | 255 | 511 | 1023 |
| B CAG | **0** | **0** | **0** | **0** | **0** | **0** | **0** |
| Rango afín | 6 | 8 | 10 | 12 | 14 | 16 | 18 |
| w* | 4 | 4 | 4 | 5 | 5 | 6 | 6 |

**Palomar** (n = agujeros)

| n | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|
| B DPLL = B CAG | 8 | 51 | 374 | 3245 | 32 780 |
| Rango afín | 0 | 0 | 0 | 0 | 0 |
| M Davis–Putnam | 22 | 113 | 2402 | ≥ 16 295 | ≥ 16 083 |
| w* | 7 | 12 | 19 | 27 | 35 |

**3-CNF aleatoria** (n = variables)

| n | 20 | 40 | 60 | 80 | 100 |
|---|---:|---:|---:|---:|---:|
| B DPLL = B CAG | 13 | 39 | 63 | 253 | 1409 |
| Rango afín | 0 | 0 | 0 | 0 | 0 |
| M Davis–Putnam | 1341 | ≥ 20 001 | ≥ 20 001 | ≥ 20 001 | ≥ 20 001 |
| w* | 14 | 28 | 40 | 55 | 69 |

**Restricciones del 8** (n = distinciones)

| n | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| B DPLL | 450 | 1330 | 4389 | 11 299 | 41 075 | 31 867 |
| B CAG | 83 | 324 | 808 | 1605 | 3230 | 2450 |
| Rango afín acreditado | 123 | 147 | 171 | 195 | 219 | 246 |
| M Davis–Putnam | 1178 | 9954 | 10 799 | 13 969 | 13 833 | ≥ 20 001 |
| w* | 12 | 17 | 17 | 17 | 20 | 21 |

**Pendientes** de log₂ B por unidad de n (mínimos cuadrados): Tseitin, DPLL 0.50 y
CAG 0; palomar 2.96; 3-CNF aleatoria 0.08; restricciones del 8, DPLL 1.34 y CAG 1.01.

## 5. Lectura

- **Tseitin cae en la zona 1 para CAG.** La política acredita todas las paridades y
  refuta sin bifurcar; DPLL se duplica cada dos vértices. Reproduce MF-46 §8. A estos
  tamaños w* y Davis–Putnam todavía no muestran la cota exponencial que la teoría da
  para expansores (Urquhart; anchura de árbol lineal); hace falta n mayor para verla.
- **Palomar y 3-CNF aleatoria quedan fuera de la zona 1.** CAG no extrae ninguna
  ecuación y coincide con DPLL, lo que reproduce MF-46B hasta n = 100. Davis–Putnam
  revienta su tope y w* crece linealmente (≈ 0.63 por variable en palomar, ≈ 0.69 en
  aleatoria).
- **Restricciones del 8: los destinos se absorben, el bit no.** CAG acredita la capa de
  destinos entera (el rango crece linealmente) y baja las bifurcaciones entre 4 y 13
  veces. Pero B sigue duplicándose por cada distinción nueva. Es la versión
  computacional de T7: refinar del lenguaje de destinos al de historias tiene costo, y
  absorber lo afín no lo paga.
- **El falsador dispara para el repertorio declarado.** En palomar y en 3-CNF aleatoria
  los cuatro métodos explotan en B, M o K, en concordancia con las cotas conocidas
  para resolución y para tablas. Por el criterio de MF-46 §14, la ruta {DPLL, CAG afín,
  Davis–Putnam, tablas} queda falsada **como candidata general**. No queda falsada una
  CAG multilenguaje ni otro lenguaje de cápsulas, y nada de esto prueba P ≠ NP.

## 6. Lo que no se afirma

- Las pendientes son de tamaños chicos: son contraste, no cotas. Las cotas
  asintóticas vienen de los teoremas citados.
- CAG es una aproximación de la política lexicográfica de MF-46: acredita todos los
  bloques locales de una vez y no elige el orden de crecimiento.
- Davis–Putnam corre sin subsunción; w* es una cota superior de la anchura de árbol.
- La dificultad de la familia del 8 es empírica. Como problema de restricciones es
  NP-completa en el peor caso (Schaefer); su distribución aleatoria no está estudiada.
- La familia del 8 usa cláusulas de ancho 3 y 4; no es 3-CNF estricta.

## 7. Adiciones a la matriz epistémica

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| El bit abierto sólo admite proyecciones | DERIVADO | `test_bit_abierto_solo_admite_proyecciones` |
| El bit abierto está fuera de las seis clases de Schaefer | DERIVADO | `test_bit_abierto_fuera_de_las_seis_clases` |
| El destino conserva x ⊕ y ⊕ z | DERIVADO | `test_destino_conserva_la_regla_afin` |
| Las ocho 3-cláusulas juntas sólo admiten proyecciones (MF-15) | DERIVADO | `test_ocho_clausulas_con_signo_solo_proyecciones` |
| Bit abierto = capa de destinos + siete «no es cero» | DERIVADO | `test_bit_abierto_cnf_es_independencia` |
| Los resolutores coinciden con fuerza bruta; la acreditación afín es sonora | DERIVADO | `test_coinciden_con_fuerza_bruta`, `test_restricciones_del_ocho_contra_distinciones`, `test_acreditacion_afin_es_sonora` |
| El falsador de MF-46 §14 dispara para el repertorio declarado | CONTRASTE, tamaños chicos | `results/falsador_v2_4.json` |
| En la familia del 8, absorber destinos no cierra el bit | CONTRASTE | ídem |
| Una CAG multilenguaje escapa al falsador | ABIERTO | — |

## Reproducir

```bash
python -m unittest discover -s tests -p "test_falsador_v2_4.py" -v
python experiments/falsador_v2_4.py            # unos 10 minutos
python experiments/falsador_v2_4.py --rapido   # versión breve, no escribe resultados
```

## Fuentes

- T. J. Schaefer, «The complexity of satisfiability problems», STOC 1978.
- C. Lautemann, P. McKenzie, T. Schwentick y H. Vollmer, «The Descriptive Complexity Approach to LOGCFL»,
  https://arxiv.org/abs/cs/9809114 (cita a Bédard, Lemieux y McKenzie, 1993: palabras sobre grupoides finitos y lenguajes libres de contexto).
- H. Albuquerque y S. Majid, «Quasialgebra structure of the octonions», https://arxiv.org/abs/math/9802116.
- R. Williams, C. Gomes y B. Selman, «Backdoors to typical case complexity», IJCAI 2003.
- E. Ben-Sasson y A. Wigderson, «Short proofs are narrow — resolution made simple», J. ACM 48 (2001).
- A. Haken (1985); A. Urquhart (1987); V. Chvátal y E. Szemerédi (1988): cotas exponenciales para resolución.
- A. Atserias y M. Müller, «Automating resolution is NP-hard», FOCS 2019.
- C. Sinz, «Towards an optimal CNF encoding of Boolean cardinality constraints», CP 2005.
- A. Darwiche y P. Marquis, «A Knowledge Compilation Map», JAIR 17 (2002).
