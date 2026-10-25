# Programa de Geometría Relacional — Laboratorio v10

**Radios, ritmos, silencios angulares, esferas y orientación del cierre**  
18 de octubre de 2026. Rama aditiva independiente, continuación de v9. Sin modificaciones a los ZIP 3.4.1, v8 o v9.

## 1. Narrativa

En una partitura, un silencio tiene una posición y una duración, aunque no emita una nota. En el laboratorio v9 ese hecho se modeló con dos pulsos discretos. Aquí las notas se proyectan sobre **radios** y **direcciones**. Un espacio sin proyección puede estar ubicado en la retícula sin que por ello podamos afirmar que contiene una esfera oculta. Además, tres esferas de referencia pueden determinar la distancia del centro de una cuarta y conservar una ambigüedad: la nueva esfera puede aparecer de uno u otro lado del plano, con exactamente las mismas medidas. El modelo distingue una métrica completa de una orientación que todavía no ha sido seleccionada.

## 2. Ontología y lenguaje [PROPUESTA]

- **Medida repetida:** unidad de longitud con la que se expresan distancias y radios.
- **Proyección:** posición admitida por una regla en la métrica previamente definida.
- **Silencio geométrico:** celda que no ocupa ninguna regla de proyección seleccionada; no equivale a inexistencia física.
- **Indeterminación de orientación:** más de una realización espacial es compatible con el mismo conjunto de distancias.
- **Nueva relación independiente:** una observación o anclaje que distingue realizaciones antes equivalentes, aunque use la unidad de longitud ya existente.
- **Cierre propio y reflexión:** interpretación ontológica abierta; la coincidencia de distancias es una realización matemática de una equivalencia bajo reflexión, no una demostración de origen ontológico.

**Precaución principal:** la reflexión isométrica preserva todas las distancias. Reconocer una orientación absoluta requiere un marco orientado o una relación que rompa esa simetría. Repetir relaciones internas no determina por sí solo si el tetraedro se colocó encima o debajo de un plano.

## 3. Experimento A: ritmos sobre radios [DERIVADO DEL MODELO]

La métrica base del ensayo es una retícula de 12 anillos `r = 2u, 4u, ..., 24u` y 12 direcciones `theta = 0°, 30°, ..., 330°`. El paso radial `2u` también es generado por los períodos `4u` y `6u` mediante combinaciones enteras (`gcd(4,6)=2`). El paso angular `30°` es el común divisor de las separaciones `60°` y `90°`. La existencia de celdas intermedias NO obliga a ninguna familia a ocuparlas.

- A: proyección en `r ≡ 0 (mod 4u)` y `theta ≡ 0 (mod 60°)`.
- B: proyección en `r ≡ 0 (mod 6u)` y `theta ≡ 0 (mod 90°)`.
- C: *intervención nueva*, mismos radios que A, direcciones `theta ≡ 30° (mod 60°)`.

Resultados del barrido exhaustivo de 144 celdas:

| Magnitud | Celdas |
|---|---:|
| Familia A | 36 |
| Familia B | 16 |
| A ∩ B | 4 |
| A ∪ B | 48 |
| Silencios conjuntos de A ∪ B | 96 |
| Familia C | 36 |
| Celdas nuevas aportadas por C | 32 |
| A ∪ B ∪ C | 80 |
| Silencios conjuntos luego de C | 64 |

La familia C **no introduce otro radio**, pero sí requiere **elegir una relación angular nueva**, que no se deduce de la mera presencia de silencios. La retícula resultante describe los vacíos con la medida anterior, sin demostrar que todos sean completables físicamente ni que deban ocuparse.

## 4. Experimento B: tres y cuatro esferas [DERIVADO EN GEOMETRÍA EUCLÍDEA]

Representamos esferas por sus **centros y distancias** entre centros, con una unidad arbitraria `u`. La forma de las esferas no interviene en la prueba; si sus radios físicos son `u`, las tres primeras podrían tocarse al estar separadas `2u`.

Fijamos `a = 2u` y tres centros en el plano z=0:

- `P0 = (0, 0, 0)`;
- `P1 = (a, 0, 0)`;
- `P2 = (a/2, √3 a/2, 0)`.

Buscamos un centro `Q` cuya distancia a cada `Pi` sea `a`. Existen dos respuestas exactas:

`Q± = (a/2, √3 a/6, ±√(2/3) a)`.

Se trata de dos tetraedros regulares especulares. Tienen **las mismas longitudes** de todas sus aristas, pero sus volúmenes orientados, respecto del plano etiquetado, son opuestos:

`V± = ± a³/(6√2) = ±0.94280904158 u³`, para `a=2u`.

Se incorpora luego un cuarto centro de referencia en el mismo plano:

`P3 = (a/2, −√3 a/2, 0)`.

La distancia a Q+ y Q− resulta idéntica: `√2 a`. Toda referencia que permanezca en ese plano conserva esa ambigüedad de reflexión.

Finalmente se mueve el cuarto anclaje fuera del plano, a:

`P3' = (0, 0, a)`.

Las distancias nuevas pasan a ser distintas:

- `|Q+−P3'| = 1.21162178611 u`;
- `|Q−−P3'| = 3.81208245549 u`.

Si el marco conoce la posición orientada de P3', esa cuarta relación permite reconstruir Q+ sin ambigüedad. No requirió una **unidad primitiva nueva** de longitud: sí requirió un **dato relacional independiente** (la distancia al anclaje fuera del plano) y una referencia orientada que el sistema coplanar no poseía.

### Prueba de rango

Restando las ecuaciones de distancias al cuadrado:

`2(Pi−P0)·Q = ||Pi||²−||P0||² − (di²−d0²)`.

- Tres referencias coplanares no alineadas: rango 2 y, bajo consistencia, dos soluciones Q±.
- Cuatro referencias **también coplanares**: rango 2 y las dos soluciones persisten.
- Cuatro referencias **no coplanares**: rango 3 y una solución dentro del marco calibrado.

La diferencia entre rango 2 y 3 no significa aparición de una dimensión física universal a partir de una longitud. Significa que las observaciones adquirieron una dirección lineal independiente.

## 5. Resultado condicional y alcance [DERIVADO]

**Proposición:** En R³, si todas las referencias que definen distancias a un punto desconocido están en un mismo plano, reflejar el punto respecto a ese plano no cambia las distancias. Si el punto está fuera de ese plano, su signo de altura no se identifica con esas distancias. En cambio, cuatro referencias afínmente independientes con distancias exactas y consistentes identifican un único punto respecto al sistema de coordenadas de las referencias.

Esto no afirma unicidad absoluta de una figura sin una referencia externa: **cualquier configuración entera trasladada, rotada o reflejada conserva las distancias internas**. La distinción de orientación siempre es relativa al marco orientado.

## 6. Comprobaciones y falsadores

1. Enumeración exhaustiva de los 144 pares (radio, ángulo); los silencios no requieren inventar otro paso radial.
2. Cálculo analítico de los dos tetraedros regulares especulares a igual distancia de los tres anclajes.
3. Prueba de que el cuarto anclaje coplanar no permite decidir el signo de la altura.
4. Prueba de que el cuarto anclaje fuera del plano aporta rango 3 y separa las distancias de ambas realizaciones.
5. Ensayos aleatorios: reflexión de 50 puntos respecto a un plano preserva todas sus distancias a siete referencias coplanares.
6. Ensayos aleatorios: reconstrucción de puntos a partir de cuatro referencias no coplanares por resta de cuadrados.
7. Verificación del volumen orientado, cuya magnitud permanece y cuyo signo se invierte.

**Contraejemplo a «todo silencio completa una estructura»:** la retícula admite celdas vacías en las que ninguna regla proyecta una esfera; nada obliga al sistema físico a llenarlas.  
**Contraejemplo a «repetir longitudes basta para resolver la orientación»:** los tetraedros Q+ y Q− satisfacen todas las distancias internas, pero no permiten decidir el lado del plano.

## 7. Relación con otras ramas [ABIERTA]

Se observa una analogía metodológica, no una equivalencia probada: en v8, una razón trigonométrica puede conservar cierta relación y perder un signo de fase; en v9, un muestreo puede conservar ritmos sin permitir identificar su composición; en v10, las distancias conservan la métrica y pueden perder orientación relativa. Son **tres mecanismos diferentes** de no identificabilidad.

Para vincular los resultados con ondas electromagnéticas harían falta dinámica de campo, condiciones de contorno, polarización y un modelo de medición. No se deduce aquí una partícula, una ley física de emergencia dimensional, P=NP ni un resultado sobre Yang–Mills.

## 8. Próxima prueba

Mover de forma continua un cuarto anclaje desde z=0 hacia z≠0, con ruido y precisión finita, y medir el umbral práctico a partir del cual Q+ y Q− son distinguibles. La transición de rango exacto al abandonar el plano no implica discriminación robusta bajo ruido cerca del plano. Se podría superponer una familia de radios 4u/6u y buscar si las coincidencias cambian la identificabilidad sin introducir nuevas unidades de longitud.

## 9. Ejecución

Requiere Python 3, NumPy y Matplotlib, sin conexión a internet:

```bash
python radios_esferas_v10.py
python -m unittest -v test_radios_esferas_v10.py
```

Entregables: `radios_esferas_v10.py`, `test_radios_esferas_v10.py`, dos CSV, `resultados_v10.json`, cuatro figuras PNG, registro de pruebas, nota de hallazgo, manifiesto SHA-256, `README.es.md` y archivo ZIP.
