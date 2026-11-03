---
title: "Solicitud de verificación independiente"
subtitle: "El cruce como reflejo central · Programa de Geometría Relacional"
author: "Le Matt Ansatz Di Ego"
date: "3 de noviembre de 2026"
lang: es
---

# Solicitud de verificación independiente

**El cruce como reflejo central — Tetraedro, cubo y costo de composición frente a los algoritmos subexponenciales de 3-SAT**

Le Matt Ansatz Di Ego · Programa de Geometría Relacional · 3 de noviembre de 2026

---

## 1. Qué se solicita

Solicitamos verificación independiente de **tres cosas, separadas y con estándares distintos**:

| # | Objeto de verificación | Tipo de estándar | Alcance |
|---|---|---|---|
| V1 | Reproducibilidad computacional (5 verificadores) | Ejecución y comparación de resultados | Totalmente verificable por máquina |
| V2 | Corrección de las Proposiciones 1–3 y el Corolario 4 (§7 del paper) | Prueba matemática | Demostraciones breves, de álgebra clásica |
| V3 | Antecedencia documental (§1 de «La caja de espejos» v0.3) | Evidencia de commits/fechas | Requiere acceso a GitHub, Software Heritage o Zenodo |

**No solicitamos** verificación de los resultados de OpenAI o Anthropic. Esos trabajos se toman como *premisa externa citada* y su auditoría es competencia de sus autores y de la comunidad. Tampoco solicitamos que se reconozca prioridad: este material no la reclama.

---

## 2. V1 — Reproducibilidad computacional

### 2.1 Cómo reproducir

Desde la carpeta `2026-11-03_cruce_reflejo_central` del repositorio:

```bash
pip install -r requirements.txt        # numpy (>=1.24)
bash reproducir_todo.sh                 # ~40 s
```

`reproducir_todo.sh` ejecuta los cinco verificadores, escribe en `resultados/` y compara con `referencia_resultados/`. Termina con código 0 **solo si** los cinco coinciden (enteros exactos; decimales con tolerancia relativa 1e-9).

### 2.2 Los cinco verificadores

| Verificador | Qué comprueba |
|---|---|
| `verificacion/experimento_cruce_dos_cortes.py` | D1 (I − 2P₋) frente a D2 (P₊ − P₋) para t = 1…5; fórmulas cerradas; límite de D1 hasta t = 10 000; control de ocho cuadrados |
| `verificacion/experimento_tetraedro.py` | Los 7 subgrupos de orden 4; signos Q8; estados de Bell, centro y cuatro cruces; costo D1 |
| `verificacion/verificar_cadena_duplicacion.py` | Niveles 2, 4, 8, 16 de Cayley–Dickson: identidad (28), R + C = 2·cruce, dos órdenes, rangos, costo Lema 2, asociatividad |
| `verificacion/verificar_particiones.py` | Particiones: Hardy–Ramanujan, log-concavidad (DeSalvo–Pak), autoconjugadas, relación de Heisenberg, familias de partes |
| `verificacion/verificar_origen_tetraedro.py` | El tetraedro desde el origen en los bits; los cruces en el origen; red cúbica de caras centradas, diamante y E8 |

### 2.3 Integridad

Los hashes SHA256 de todos los archivos están en `MANIFIESTO_SHA256.txt`. Verificar con:

```bash
sha256sum -c MANIFIESTO_SHA256.txt   # Linux/macOS
```

### 2.4 Resultado de referencia

- **Entorno de referencia:** Python 3.13.18, numpy 2.5.3, Linux (`entorno.json`).
- **Reproducción multiplataforma ya realizada por DeepSeek, un modelo de IA (2026-11-03):** Windows, Python 3.12.14, numpy 2.3.5 → los 4 verificadores regeneraron resultados idénticos a la referencia y `comparar_resultados.py` devolvió 0; los 26 archivos coincidieron con sus hashes.

**Criterio de éxito para el revisor:** los 5 JSON coinciden y el hash de cada archivo coincide. No hay ningún número [E] que dependa del sistema operativo.

---

## 3. V2 — Corrección matemática

Se pide revisar las cuatro pruebas de la §7 del paper. Son cortas y usan álgebra clásica.

**Proposición 1.** En los niveles 2, 4 y 8 de la duplicación de Cayley–Dickson, R + C = 2·[x=v][y=u]. *(Prueba: multiplicatividad de la norma — Hurwitz 1898 — e identidad (28).)*

**Proposición 2.** R = (Lᵥᵀ Lₓ)ᵤ,ᵧ y C = (Lₓᵀ Lᵥ)ᵤ,ᵧ, con Lᵥᵀ Lₓ + Lₓᵀ Lᵥ = 2[x=v]·Id (relaciones de Hurwitz–Radon).

**Proposición 3.** Con el conteo del Lema 2, un bloque cuesta 4/4, 8/8 y 11/12 bits en los niveles 2, 4 y 8; en el 16 la identidad (28) falla en 672 casos.

**Corolario 4.** Dentro de la cadena, el único nivel que abarata es el 8, y el 8 no es asociativo (Frobenius 1878).

**Puntos que pedimos revisar con especial atención:**

1. El paso «R² = N·R ⇒ rango por filas de R = N» (Proposición 3): ¿es correcto que ΦΦᵀ = N·Id implica rango N?
2. La afirmación «el rango de R por columnas es el de C por filas» y su valor (N² si N ≠ 2; 2 si N = 2).
3. El conteo de 168 de 210 tríos con signo dependiente del camino en el nivel 8.
4. La afirmación de que todo nivel posterior de la duplicación contiene al 16 como subálgebra con la misma tabla de signos.

**Criterio de éxito:** confirmar o refutar cada proposición con una corrección explícita si la hubiera.

---

## 4. V3 — Antecedencia documental

Lo que el paper afirma sobre fechas es **lo siguiente, y nada más**:

- El recierre (MF-63B) y la composición de interfaces son **públicos antes del 16 de octubre** (commits RGP `c44cfb8` del 3-oct y `6e36993` del 9-oct).
- Los documentos de **conteo** y la **nota de los octoniones** tienen fechas internas del 13–16 de octubre y se hicieron públicos el **24 de octubre**: antes de los anuncios, después del día del descubrimiento.
- El **origen del tetraedro**: la cápsula {A, JA, −A, −JA} y la resolución de una indefinición binaria con σ = ±1 son públicas desde el **29 de septiembre** (PGR `fb27fbf`, fuentes F024 y F056). El tetraedro de referencias aparece explícito en O19 (fechado el 19 de octubre) y en CME-003, públicos desde el 24 de octubre (`0fd5315`).

**Lo que se pide verificar** (no asumir):

1. La **hora de subida** de cada commit según GitHub (la fecha escrita en el documento no basta).
2. La presencia de cada archivo citado en el commit indicado.
3. Una copia en **Software Heritage** o un depósito en **Zenodo con DOI**, si se quiere precedencia definitiva.
4. Las **capturas archivadas** de las dos publicaciones de Reddit (3 y 9 de octubre).

**Criterio de éxito:** confirmar o corregir la tabla de la §1 de «La caja de espejos» v0.3 con evidencia verificable.

---

## 5. Lo que NO se afirma (para que el revisor no pierda tiempo)

1. **No** hay algoritmo propio.
2. **No** se reclama prioridad sobre las técnicas de OpenAI o Claude.
3. **No** se afirma que un laboratorio usara materiales del otro o del programa.
4. **No** se demuestra la validez de los resultados de OpenAI/Anthropic.
5. **No** se afirma que las correspondencias (niveles I–III) reconstruyan los algoritmos ni sus cotas (nivel IV, abierto).

Las correspondencias de los niveles I–III son **teoremas clásicos expresados en el lenguaje del programa** (eliminación de variables; Hurwitz–Radon; octoniones). Su valor no es la novedad, sino la lectura y la medición.

---

## 6. Las cuatro preguntas que esta solicitud responde de antemano

Para que el revisor no tenga que preguntarlas, las respondemos aquí:

1. **¿Este material es el mismo algoritmo que el de OpenAI o Claude?** No. Los tres llegan a conclusiones relacionadas por vías distintas, y este material no presenta ningún algoritmo. OpenAI y Claude dan construcciones algorítmicas con cotas; este documento mide y ubica la pieza (el cruce) que ellos descomponen.

2. **¿El programa «llegó antes»?** En un sentido preciso, sí: el planteamiento público del cierre relacional y las interfaces es del 3 de octubre, anterior a los anuncios. En el sentido que importa, no: el programa no publicó el algoritmo subexponencial, y su propia nota N1 demuestra que su motor es exponencial, de modo que no puede reclamar la salida.

3. **¿Los resultados del programa son equivalentes a los de OpenAI o Claude?** No está demostrado: es el nivel IV, abierto. Además, el recierre es contracción siguiendo un solo árbol, un modelo con cota inferior exponencial incondicional (Austrin, Kaski y Kubjas, 2022), y N1 prueba que el motor de tablas del programa cuesta 2^Ω(n) en grafos aleatorios. Ninguno de los dos, tal como está, puede ser un algoritmo subexponencial.

4. **¿El cierre del programa es polinómico?** Una operación concreta —la clausura por diamantes en 3-coloración (R-04, solicitud de revisión del 30 de octubre, PGR `a1d3f16`)— sí es polinómica. No se activa en grafos sin triángulos, donde la 3-coloración sigue siendo NP-completa. Eso demuestra la eficiencia de una operación, no de una solución general de 3-SAT o 3-coloración.

**En una línea:** el programa tenía piezas del terreno y diagnosticó el límite de su propio motor; tres correspondencias exactas con el algoritmo de Claude se establecieron a posteriori; no llegó a la solución, y no reclama prioridad ni equivalencia.

**Revisión de la §7 por DeepSeek (2026-11-03).** Además de la verificación V2 que se solicita, DeepSeek, un modelo de IA, re-derivó con una implementación propia, sin usar los verificadores del paquete, las Proposiciones 1–3 y el Corolario 4 con enteros exactos y confirmó el conteo «168 de 210»: las pruebas no tienen errores. Al ser la comprobación de un modelo de IA, no reemplaza la revisión humana que se solicita en V2. Informe: `revision_pruebas_sec7_DeepSeek.md`; script: `review_pruebas_sec7.py`, en esta misma carpeta.

---

## 7. Preguntas abiertas (nivel IV) que agradeceríamos que el revisor considere

1. ¿Puede el programa **derivar** 1/√2 (o un ρ < 11/12) desde su propio lenguaje, en lugar de postular la duplicación?
2. ¿Existe una **familia de partes** con operadores que cumplan los Lemas 9 y 10 del paper de Claude y den ρ < 1/√2 (por ejemplo, los cuadrados, α = 1/3, ρ ≈ 0.63)?
3. ¿Hay un **mapa** que lleve la paridad del espejo movido (§3) a un corte (§5) conservando rangos?

---

## 8. Cómo reportar

- **V1:** adjuntar la salida de `bash reproducir_todo.sh`, la salida de `sha256sum -c MANIFIESTO_SHA256.txt`, y la versión exacta de Python y numpy.
- **V2:** señalar cada proposición como *correcta*, *correcta con observación*, o *incorrecta*, con la corrección.
- **V3:** adjuntar capturas o enlaces de los commits/archivos, con sus horas de subida.

El material completo (paper, notas, verificadores y resultados) está en la carpeta `2026-11-03_cruce_reflejo_central` del repositorio.

---

*Estado de este documento: solicitud abierta a revisión independiente. No constituye una declaración de precedencia ni un reclamo de prioridad.*
