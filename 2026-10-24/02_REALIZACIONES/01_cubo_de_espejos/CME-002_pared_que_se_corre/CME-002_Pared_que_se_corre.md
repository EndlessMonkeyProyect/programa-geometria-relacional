# CME-002 — La pared que se corre: ángulos e identidades

**Laboratorio del Cubo de Espejos · Programa de Geometría Relacional · 24 de octubre de 2026**
**Estado:** [O] regla de Diego · [T] teoremas conocidos verificados · [E] ensayo reproducible · [F] correcciones a lo dicho en la conversación

## Regla [O]

Desde adentro, la celda mide siempre uno. Desde afuera, al correrse la pared, los cubículos se van reduciendo y la celda queda normalizada a la totalidad como 1/k. Cuando aparece un múltiplo nuevo, una relación modular que antes no tenía con qué compararse, ese entero k fija el ángulo π/k entre dos espejos. Sobre esa relación se construye lo demás.

## Dos lecturas de lo mismo

- **Ángulos:** dos espejos que se cortan en π/k.
- **Identidades:** aplicar esos dos espejos k veces seguidas es no hacer nada, (sᵢsⱼ)ᵏ = 1. El ángulo es una identidad, y k es el múltiplo que cierra.

El ensayo calcula cada lectura por separado:
- los ángulos, con las matrices de reflexión;
- las identidades, solo con las igualdades y sin ninguna geometría: la enumeración de Todd–Coxeter decide si el recinto cierra, y la serie de Steinberg da cuántas orientaciones nuevas aparecen en cada paso cuando no cierra.

## Recinto y observable

Tres espejos que forman un triángulo con ángulos π/2, π/3 y π/k. Como control, π/2, π/2 y π/k. Se cuentan las orientaciones distintas que se alcanzan con a lo sumo L reflexiones, hasta L = 16.

## Resultado [T/E]

**Familia (2, 3, k)**

| k | Factores | 1/2 + 1/3 + 1/k | Qué pasa | Orientaciones |
|---|---|---|---|---|
| 2 | 2 | 4/3 | **cierra** | 12 |
| 3 | 3 | 7/6 | **cierra** | 24 |
| 4 | 2² | 13/12 | **cierra** | 48 |
| 5 | 5 | 31/30 | **cierra** | 120 |
| 6 | 2·3 | 1 | **se repite** | las nuevas por paso crecen en línea recta (+12 cada 5 pasos) |
| 7 | 7 | 41/42 | **se abre** | cada paso multiplica por 1,176281 |
| 8 | 2³ | 23/24 | se abre | × 1,230391 |
| 9 | 3² | 17/18 | se abre | × 1,261231 |
| 10 | 2·5 | 14/15 | se abre | × 1,280638 |
| 11 | 11 | 61/66 | se abre | × 1,293486 |
| 12 | 2²·3 | 11/12 | se abre | × 1,302269 |

**Control (2, 2, k):** cierra para todo k, en 4k orientaciones. Es un prisma.

En los 22 casos las dos lecturas dan lo mismo, paso por paso: lo que cuentan las matrices es exactamente lo que predicen las identidades solas.

**La apertura más lenta de la familia es k = 7**, y su tasa es el número de Lehmer, 1,176280818260…, con coincidencia en doce cifras. Es la raíz de x¹⁰ + x⁹ − x⁷ − x⁶ − x⁵ − x⁴ − x³ + x + 1; desde 1933 se pregunta si existe un número de su tipo más pequeño.

## Lo que decide [T]

No decide el primo por sí solo. Decide la suma de las tres fracciones frente a la totalidad:

- **sobra** (1/p + 1/q + 1/k > 1): el recinto **cierra**, como una esfera;
- **llena justo** (= 1): el recinto **se repite**, como un panal que tesela el plano;
- **no alcanza** (< 1): el recinto **se abre**, y cada paso multiplica lo anterior.

Es la suma de los ángulos de un triángulo comparada con π: literalmente un teorema de triángulos.

## Lectura en el hilo [O/H]

- **La normalización a la totalidad es la que decide.** Las celdas son fracciones de la totalidad; si sobran, cierran; si la llenan justo, se repiten; si no alcanzan, abren.
- **El primo nuevo encaja, con matices.** 2, 3 y 5 cierran; 7 y 11 abren. El 4 = 2², que solo profundiza el 2, todavía cierra. El 6 = 2·3 no trae ningún primo nuevo, y es justo donde aparece la repetición.
- **La escala sale sola.** Al cerrar, la totalidad es un número finito (12, 24, 48, 120). Al repetirse, crece siempre al mismo ritmo. Al abrirse, cada paso multiplica.
- **Observación:** en los tres únicos triángulos que teselan el plano, (2,3,6), (2,4,4) y (3,3,3), el tercer entero es el mínimo común múltiplo de los otros dos. Lo inverso no vale: (2,5,10) tiene 10 = mcm(2,5) y se abre.

## Correcciones a lo dicho en la conversación [F]

1. **«Desde el 7 no cierra nada finito»** no es exacto. Con dos ángulos rectos, cualquier k cierra (el control). Lo que vale es la suma de las fracciones.
2. **«El cubo usa el 2 y el 4»:** el recinto del cubo de CME-001 usa solo ángulos rectos. Es su grupo de simetrías completo, de 48 orientaciones, el que corresponde a (2, 3, 4).
3. **«Cierra solo hasta el 5»** es cierto para la familia (2, 3, k). En general, cuando tres o más espejos no se separan en grupos independientes, los únicos enteros que aparecen en un recinto que cierra son 2, 3, 4 y 5.

## Lo que NO establece

- La regla «primo nuevo → ángulo π/primo» no decide el régimen por sí sola; lo decide la suma.
- El ensayo fija a mano los dos primeros ángulos, π/2 y π/3; no los deriva de la pared que se corre.
- Es teoría conocida de grupos de triángulos y de espejos; lo nuevo es la lectura en el hilo.
- No prueba nada sobre Navier–Stokes, P frente a NP ni la brecha de Yang–Mills.

## Siguiente operación

**CME-003** (`../CME-003_de_las_cuatro_referencias_a_los_angulos/`): π/2 y π/3 salen de intercambiar las cuatro referencias de T8, y con el bit sale π/4. Queda escribir la regla de la pared que da esas cuatro referencias intercambiables. Con ella, lo demás sale solo: cierre hasta el 5, repetición en el 6 y apertura desde el 7.

## Reproducción

```bash
python3 cme002_angulos_e_identidades.py
```

Requiere NumPy y SymPy; tarda unos 25 segundos. Escribe `cme002_resultados.json` y falla si las dos lecturas no coinciden, si el régimen no es el esperado o si la tasa de (2,3,7) no coincide con el número de Lehmer.

## Referencias de enlace

- H. S. M. Coxeter, «Discrete groups generated by reflections», *Annals of Mathematics* 35 (1934).
- R. Steinberg, *Endomorphisms of linear algebraic groups*, Memoirs of the AMS 80 (1968): serie de crecimiento a partir de los subgrupos finitos.
- D. H. Lehmer, «Factorization of certain cyclotomic functions», *Annals of Mathematics* 34 (1933).
