---
title: "Del cuatro a la distancia, y el tiempo como resolución"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida de la conversación del 14-10-2026"
version: "2.7 — 2026-10-14"
status: "T8 derivado; decisión del autor sobre el tres y uno; lecturas del tiempo tipadas; tres abiertos"
---

# Del cuatro a la distancia, y el tiempo como resolución

Esta nota amarra la conversación del 14 de octubre. La primera parte formaliza cómo
nace la distancia en el paso del cuatro al cinco (T8). La segunda tipa las lecturas
del tiempo que se discutieron, separando lo exacto de lo que es lectura del autor.
Pruebas: `tests/test_del_cuatro_a_la_distancia_v2_7.py`. Experimento:
`experiments/del_cuatro_a_la_distancia_v2_7.py`.

---

# I. Del cuatro a la distancia

## 1. El enunciado del autor `POSTULADO`

> En la emergencia de los radios, cuando el radio no alcanzó para la cardinalidad que
> podía mantener la estructura, quedan cuatro con el mismo radio. Surge una nueva
> diferencia para la quinta singularidad, y en ese momento surge un espacio de
> comparación: lo que nosotros podemos medir como distancia. Las referencias, las
> demás, ya estaban.

> X, Y, Z sólo son referencias: un marco. Con tres esferas podríamos referir cualquier
> punto en un plano; la cuarta da la posibilidad de configurar diferente, de generar un
> espacio, una descripción adicional.

> **Decisión (14-10-2026).** Son tres y uno, pero no se puede distinguir cuál.

## 2. Lo que decía la base

| Fuente | Qué dice | Estado antes de esta nota |
|---|---|---|
| Formalización canónica v1, §16 | La distancia del árbol no es una métrica: «la distancia espacial sólo puede definirse después de derivar comparaciones geométricas adicionales» | ABIERTO |
| MF-67 | Un cierre de cuatro no fija el radio | DERIVADO (no-go) |
| Fotografía narrativa, §17 (agosto) | Con fracciones que se tocan, sin métrica: tres del mismo tipo más uno de otra especie (la recta que toca a todos), y no hay quinto | DERIVADO en el plano |
| Nota de octubre, teorema 5 | n distinciones binarias tienen 2ⁿ − 1 comparaciones no triviales; el 15 son las de cuatro distinciones | DERIVADO |
| §21.1 de la fotografía narrativa | «El cuatro hace tres trabajos»: 2 × 2, cuatro estados y exponente | ABIERTO |

## 3. T8 — Del cuatro a la distancia `DERIVADO`

Sea n el número de distinciones binarias. Cada estado se escribe por sus 2ⁿ − 1
comparaciones no triviales, que son las paridades sobre subconjuntos no vacíos de
distinciones. Los cinco enunciados siguientes están verificados en el experimento.

**(a) Referencias al mismo radio.** Dos estados distintos difieren en exactamente
2ⁿ⁻¹ comparaciones. Los 2ⁿ estados están todos a la misma distancia entre sí: forman un
símplex regular que ocupa 2ⁿ − 1 ejes (rango afín completo). Es el código símplex.

| Distinciones | Estados | Ejes de comparación | Distancia entre todos |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 3 | 2 |
| 3 | 8 | 7 | 4 |
| 4 | 16 | 15 | 8 |

*Prueba.* Para una diferencia δ ≠ 0, exactamente la mitad de los 2ⁿ caracteres
detectan δ, y todos ellos son no triviales: 2ⁿ⁻¹. ∎

Con dos distinciones, las cuatro referencias son 000, 011, 101 y 110: todas a distancia
2, en tres ejes. **El tres no se supone: es el número de comparaciones no triviales de
dos distinciones, 2² − 1.** La misma tabla da los 7 ejes del 8 (los puntos de Fano) y
el 15 del programa.

**(b) Tres y uno sin distinguir cuál.** Las cuatro referencias cumplen una sola relación,
y es simétrica:

```text
a ⊕ b ⊕ c ⊕ d = 0          (con signos ±1, centradas: v₁ + v₂ + v₃ + v₄ = 0)
```

Tres cualesquiera fijan la cuarta. Las simetrías del cubo de comparaciones que respetan
las cuatro realizan las 24 permutaciones. Trasladar por cualquiera de ellas la lleva al
origen. Hay tres libres y una cerrada, y la relación no dice cuál es la cerrada.

**(c) La quinta.** En los tres ejes de dos distinciones no caben cinco referencias
iguales; el máximo, por búsqueda exhaustiva, es 4. Cualquier quinta palabra queda a
distancias 1, 1, 1 y 3, y **señala exactamente a una de las cuatro**, su antípoda. Las
cuatro quintas posibles señalan a las cuatro referencias, una cada una. La distinta la
pone el de afuera.

En esferas el resultado es el mismo. Cuatro esferas iguales de radio 1 se tocan todas.
Una quinta que toque a las cuatro **tiene que tener otro radio**:

```text
interior    r₅ = (√6 − 2)/2 = 0.224745…
envolvente  r₅ = (√6 + 2)/2 = 2.224745…   (el continente)
Soddy–Gosset en tres dimensiones: (Σk)² = 3·Σk²   (k = 1/r; exacto en ℚ(√6))
```

Es la primera razón de radios que la estructura impone sin calibrar.

**(d) La distancia nace con la quinta.** Hasta cuatro singularidades, todas sus
comparaciones son independientes. Con cinco aparece la primera relación obligada entre
ellas: el determinante de Cayley–Menger se anula.

| Singularidades | Comparaciones | Libres | Relaciones obligadas | Cayley–Menger |
|---:|---:|---:|---:|---|
| 2 | 1 | 1 | 0 | ≠ 0 |
| 3 | 3 | 3 | 0 | ≠ 0 |
| 4 | 6 | 6 | 0 | ≠ 0 |
| 5 | 10 | 9 | **1** | **= 0** |
| 6 | 15 | 12 | 3 | = 0 |

Hasta cuatro, las comparaciones son etiquetas. Con la quinta empiezan a deberse algo
unas a otras, y eso es lo que hace que un conjunto de comparaciones sea un espacio
(Menger). **El espacio es la solución de esas relaciones.**

Las referencias ya estaban, y eso también es exacto. Con las cuatro, la quinta queda
determinada por sus comparaciones. Con sólo tres, queda en dos lugares espejo: un ±
que tres referencias no resuelven y la cuarta sí. Ejemplo verificado: con referencias en
(0,0,0), (4,0,0), (0,4,0) quedan (1,2,3) y (1,2,−3); con (0,0,4), sólo (1,2,3).

**(e) En el 8.** Las cuatro unidades cuaterniónicas (índices cerrados, 1 ⊕ 2 = 3)
cierran todos sus tríos: 0 abiertos. Una quinta unidad, cualquiera de las cuatro de
afuera, trae 18 tríos abiertos ordenados, que son el bit abierto de T7. Lo que genera ya
es el 8 entero.

## 4. Qué cuatro es este cuatro

| Aparición | Objeto | Con T8 |
|---|---|---|
| 2 × 2 | estados de dos distinciones | **las cuatro referencias** |
| Cuatro al mismo radio | símplex regular | **las mismas cuatro**, en sus 2² − 1 = 3 ejes |
| 1 ⊕ 3 de los cuaterniones | unidad y tres imaginarias | las cuatro referencias con un origen elegido (T8b); lo distinto por sí mismo es la comparación trivial (§5) |
| ε = 4 en R_p = 4λ̄_p | profundidad | sin cambio: sigue siendo otro trabajo del cuatro |

Dos de los tres trabajos del cuatro quedan unificados: los estados de dos distinciones
**son** las cuatro referencias al mismo radio, y sus comparaciones dan los tres ejes. La
pregunta «por qué cuatro» pasa a ser «por qué dos distinciones». El programa responde
con un postulado: el 4 es la actualidad. Ahí vive ahora el «por qué cuatro», y queda
declarado como postulado.

## 5. Lo que sí es distinto `POSTULADO` (lectura)

Entre las cuatro singularidades ninguna es distinta (T8b). Entre las cuatro
**comparaciones** de dos distinciones sí hay una distinta de forma intrínseca: la
trivial, comparar cada cosa consigo misma, que no separa nada. Las cuatro comparaciones
son una trivial más tres ejes.

**Lectura.** El «uno de otra especie» de agosto, la recta que toca a todos, sería esa
comparación común y no una singularidad. Por eso el autor puede decir «son tres y uno»
y a la vez «no se sabe cuál»: el uno es la referencia compartida, y ninguna de las
cuatro lo es por sí misma. Es una lectura que concilia agosto con hoy; no está derivada.

## 6. Lo que T8 no hace

- **No identifica los tres ejes con el espacio físico.** Es el puente que falta
  (ABIERTO).
- **No deriva por qué dos distinciones** (POSTULADO: el 4 es la actualidad).
- **No convierte 0.2247 en una masa.** Antes de compararla con cualquier razón física hay
  que declarar cuál sería; si no, se repite lo del protón (CONTRASTE pendiente, sin
  candidato declarado).

---

# II. El tiempo como resolución

Lecturas de la conversación de voz del 14-10-2026, tipadas.

## 7. El tiempo es comparación de ritmos `POSTULADO` · identidades `DERIVADO`

> El tiempo es la comparación del ritmo de sistemas: un compás donde cada instrumento
> tiene su métrica y entre todos saturan el compás.

Antecedente propio: «el tiempo no transcurre: se organiza como ritmo» (16-04-2025).
Externos: Mach y Barbour.

**Precisión.** La rejilla de la que todos son múltiplos es el MCD. El compás donde todos
vuelven a coincidir es el **mínimo** común múltiplo; un «máximo común múltiplo» no
existe, porque los múltiplos comunes crecen sin fin. Ejemplo verificado: los periodos 1,
1/2, 1/3 y 3/4 tienen rejilla 1/12 y compás 3. Si los ritmos son conmensurables, el
compás cierra y es un ciclo. Si no lo son, no cierra nunca y es el hilo abierto.

## 8. El 8 cierra en el infinito `DERIVADO`

La recta proyectiva octoniónica es una esfera: OP¹ ≅ S⁸. Es el espacio de ocho
dimensiones más un solo punto en el infinito (Baez 2002). «Vemos el otro lado» es estar
en la carta plana; el cierre es el punto opuesto. **Una esfera es simétrica: cerrar da
la totalidad, no una dirección.**

## 9. La comparación no tiene dirección `POSTULADO` · enlace `DERIVADO`

> Si comparás algo no podés decir que lo comparaste para un lado o para el otro. Lo que
> queda es una diferencia de incertidumbre, que no es una magnitud. Es la base de la
> indefinición.

Una diferencia sin signo es un solo bit, que hay diferencia, sin orientación. Es el ± que
ninguna convención fija (T7a).

## 10. La flecha está en resolver `POSTULADO` · `ABIERTO`

> Las soluciones de la coherencia, en la medida en que se van resolviendo, van hacia el
> uno: las distancias se quieren reducir, la frecuencia sintonizar, la materia acelerar.

La comparación no tiene dirección, pero **resolverla sí**: lo resuelto no se des-resuelve.
Hay dos tendencias, y el autor las pone perpendiculares:

> En esas dos variables se construye el cristal de la realidad.

La novedad trae material al frente; la resolución lo congela.

| Lugar | Qué es |
|---|---|
| Atrás | el cristal congelado: el pasado |
| Adelante | la diferencia abierta, sin dirección: el futuro |
| El filo | el presente, donde se cristaliza |

> Debería crecer hasta que se resuelva todo, y hay mecanismos de resolución. El tiempo no
> importa, sino la resolución de las cosas.

**ABIERTO.** Un cristal se forma sólo en una banda angosta de ritmos. Si la resolución
corre demasiado, queda ruido congelado; si corre demasiado la novedad, no cuaja. Falta
decir por qué la realidad está en la banda que cristaliza.

## 11. El límite `DERIVADO` · lectura `POSTULADO`

> Leído en función del radio propio frente al exterior, superando el mínimo común, no
> presentaría diferencia: ahí sería el límite. Para nosotros aparecería como una cinta,
> porque estamos dentro del sistema.

> La distancia se resolvió porque ya no tiene sentido comparativo. En tu física:
> alcanzaría la velocidad de la luz y quedaría congelado en el tiempo.

Lo exacto, con la partición de la v2.6 (r_V = β², r_m = 1/γ²):

```text
reloj propio   dτ/dt = √r_m          longitud   L = L₀·√r_m
en la luz      r_m = 0: sin reloj y sin distancia
```

**El reloj que late es el complemento de masa**: la proyección pura no late. La materia
con masa se acerca a ese límite sin tocarlo (r_m > 0). **Lectura:** el cristal es
asintótico, y lo que nunca cierra, 1/γ² > 0, es la masa en reposo: el residuo que el
cierre no borra.

## 12. La masa sólo como razón `DERIVADO` · `POSTULADO`

> La masa ya no importaría, porque no habría con qué compararla. Lo único que podría
> cambiar es el radio, pero eso es una variable.

**Exacto.** Un radio solo, sin otro al lado, es una convención (gauge): agrandar todo al
doble sin nada afuera no cambia ninguna comparación. Sólo hay razones. μ/e es una razón
entre dos singularidades, y por eso la regla de escala tiene que nacer de comparar dos,
nunca de una sola.

**Lectura del autor.** La masa es el mecanismo de almacenamiento de la información, y el
espacio es lo resuelto. Es la partición r_V + r_m = 1 leída como ontología:

| Parte | Lectura |
|---|---|
| Proyección | lo solucionado, tendido como espacio |
| Complemento | lo guardado, sostenido como masa |

## 13. ¿El espacio es solución de qué?

«El espacio de la incertidumbre lo obliga» define espacio con espacio. Para no dar
vueltas, la incertidumbre tiene que ser una cuenta y no una extensión. Hay dos respuestas
en cuenta:

1. **Cayley–Menger** `DERIVADO` (T8d). El espacio es el conjunto de comparaciones que
   cumplen las relaciones obligadas que aparecen desde la quinta singularidad.
2. **Forma en bits** `CONTRASTE` sin candidato. La cota de Bekenstein (1981) limita la
   información de un sistema de radio R y energía E = mc²:

   ```text
   I ≤ 2π·R·E/(ħ c ln 2) = (2π/ln 2)·(R/λ̄),    con λ̄ = ħ/(mc)
   ```

   Con un presupuesto fijo de información, masa y radio se intercambian (m ∝ 1/R). Es una
   cota, no una igualdad: que una partícula la sature no está establecido.

## 14. «Hacia el uno» y la expansión `CONTRASTE`

**Versión universal.** Si todo fuera siempre hacia el uno, las distancias se reducirían
a gran escala. El universo se expande: **choca con el dato**. También choca con la
lectura vieja del propio programa, donde la expansión es desincronización.

**Versión «en sistemas ligados».** Sigue ABIERTA.

---

# III. Decisiones y abiertos de esta versión

| Cuestión | Estado |
|---|---|
| ¿Cuatro iguales, o tres y uno? | **DECIDIDO** por el autor: tres y uno sin distinguir cuál. Contenido exacto en T8b |
| ¿Por qué dos distinciones? | POSTULADO: el 4 es la actualidad |
| ¿Los tres ejes de comparación son el espacio físico? | ABIERTO: puente |
| Regla de escala por singularidad | ABIERTO. Prueba fijada (v2.6): un parámetro fijado con μ/e que prediga τ/e = 3477.4 sin tocarlo |
| «Hacia el uno»: ¿siempre o en sistemas ligados? | La versión universal choca con la expansión; la de sistemas ligados está ABIERTA |
| La flecha como frente del cristal | POSTULADO. La banda que cristaliza está ABIERTA |

## Matriz

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| n distinciones: 2ⁿ estados a igual distancia en 2ⁿ − 1 ejes | DERIVADO | `test_n_distinciones_dan_un_simplex_regular` |
| a⊕b⊕c⊕d = 0; tres fijan la cuarta; 24 permutaciones; cualquiera hace de uno | DERIVADO | `test_cierre_simetrico_y_ninguna_distinguida` |
| No cabe una quinta igual; la de afuera señala a una | DERIVADO | `test_no_cabe_una_quinta_igual_y_la_de_afuera_senala_a_una` |
| La esfera que toca a cuatro iguales tiene otro radio (Soddy–Gosset) | DERIVADO | `test_la_esfera_que_toca_a_cuatro_iguales_tiene_otro_radio` |
| Primera relación obligada con cinco (Cayley–Menger) | DERIVADO | `test_la_primera_relacion_obligada_aparece_con_cinco` |
| Tres referencias dejan un ±; cuatro lo resuelven | DERIVADO | `test_tres_referencias_dejan_un_signo_y_cuatro_lo_resuelven` |
| Cuatro unidades cierran; la quinta trae el bit abierto y genera el 8 | DERIVADO | `test_cuatro_cierran_y_la_quinta_trae_el_bit_abierto` |
| Compás = MCM, rejilla = MCD | DERIVADO | `test_compas_es_mcm_y_rejilla_es_mcd` |
| Reloj propio = √r_m | DERIVADO | `test_el_reloj_propio_late_como_la_raiz_del_complemento` |
| OP¹ ≅ S⁸ | DERIVADO (clásico) | Baez 2002 |
| Tiempo = comparación de ritmos; flecha = resolución; cristal | POSTULADO | — |
| Masa = almacenamiento; espacio = lo resuelto | POSTULADO | — |

## Fuentes

- J. C. Baez, «The Octonions», *Bull. AMS* 39 (2002) 145–205.
- F. Soddy, «The Kiss Precise», *Nature* 137 (1936) 1021; T. Gosset, *Nature* 139 (1937) 62.
- K. Menger, «Untersuchungen über allgemeine Metrik», *Math. Ann.* 100 (1928);
  L. M. Blumenthal, *Theory and Applications of Distance Geometry* (1953).
- F. J. MacWilliams y N. J. A. Sloane, *The Theory of Error-Correcting Codes* (1977), código símplex.
- J. D. Bekenstein, «Universal upper bound on the entropy-to-energy ratio for bounded
  systems», *Phys. Rev. D* 23 (1981) 287.
- J. Barbour, *The End of Time* (1999).
