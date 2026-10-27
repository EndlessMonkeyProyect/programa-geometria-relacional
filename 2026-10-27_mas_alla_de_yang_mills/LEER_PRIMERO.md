# Más allá de Yang–Mills — complemento del 27 de octubre de 2026

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**

Esta carpeta reúne el artículo *Más allá de Yang–Mills: un marco relacional de su emergencia* y todo el material que respalda lo que afirma: siete paquetes reproducibles (PR-01 a PR-07) y una verificación independiente de R-02. Se agrega a la edición del 24 de octubre sin modificar nada de ella.

**Estatus.** No es una solución del problema de la brecha de masa del Clay Mathematics Institute. Es un marco de la **emergencia** de Yang–Mills:
- Los principios del programa generan una familia de acciones de gauge locales, una por cada defecto de cierre admisible. Con una hipótesis adicional, un término cuadrático positivo y no degenerado cerca de la identidad, su límite clásico para campos suaves tiene la forma de Yang–Mills. Wilson es la elección particular natural y estándar, no la única.
- La familia completa de comparaciones ν distingue el centro de u(2) = su(2) ⊕ u(1): tres referencias y una fase común. Una sola comparación no basta.
- Quedan abiertos y declarados: la brecha, el límite cuántico, el mecanismo de masa, la identidad física del fotón, el ángulo de Weinberg y la dirección de escala.

## Contenido

| Ruta | Qué contiene |
|---|---|
| `articulo/` | El artículo en Markdown y PDF, con la solicitud de revisión, y su traducción al inglés (`Beyond_Yang_Mills_2026-10-27_EN`). La versión de referencia es la española |
| `paquetes/PR-01…PR-07/` | Un paquete por paso: README con enunciados y falsadores, `verificar.py`, `resultados.json` y manifiesto SHA-256 |
| `revision_R02/` | Verificación independiente, escrita desde cero, del álgebra de R-02 |
| `referencia_resultados/` | Copia intacta de los `resultados.json` entregados, contra la que se compara |
| `reproducir_todo.sh` | Verifica integridad, corre todos los verificadores y compara con tolerancia |
| `comparar_resultados.py` | La comparación con tolerancia, también usable por separado |
| `entorno.json` | Versiones, semillas y parámetros con que se generaron los resultados |
| `requirements.txt` | Dependencias: `numpy`, `scipy` |
| `MANIFIESTO_SHA256.txt` | Huella de cada archivo distribuido |

## Orden de lectura

1. **El artículo**, `articulo/`.
2. **PR-07**: es el respaldo directo de las secciones 3 a 6 del artículo.
3. **PR-04 → PR-05 → PR-06**: el camino que lleva hacia la brecha, que es el eje de lo que sigue.
4. **PR-01 a PR-03**: los pasos previos, con sus correcciones.

## Qué establece cada paquete

| Paquete | Resultado | Estatus |
|---|---|---|
| PR-01 | El resto de la unidad se conserva si la proyección respeta la duplicación | Teorema elemental; ciego a la brecha, como muestra PR-02 |
| PR-02 | Dónde vive la brecha al duplicar: modos heredados frente a nuevos | Lema exacto; controles sin interacción. Con interacción no decide la brecha (PR-04) |
| PR-03 | Cadena de Ising que crece por volumen: la brecha sobrevive a la interacción | Medición exacta. Su cota se vuelve inútil al iterarla, y su argumento de "pérdida sumable" es vacío; lo corrige PR-04 |
| PR-04 | Criterio correcto: la pérdida logarítmica acumulada entre escalas; Ising 2D con y sin brecha | Identidad exacta; las medidas estructurales no deciden la brecha |
| PR-05 | Brecha uniforme de Ising 2D a alta temperatura: resolución local contra influencia | Teorema conocido, reproducido; β < 0,3322 |
| PR-06 | Masa positiva por cierre de ventanas: el flujo de correlación por el borde | Teorema con un lema citado (Simon–Lieb); β < 0,4067 |
| PR-07 | De los cuatro principios a una familia de acciones; con la condición cuadrática, clase de Yang–Mills; Wilson como elección particular, Manton como otra, y un contraejemplo sin término cuadrático. La familia de comparaciones ν separa u(2) en 3 + 1; controles del tetraedro y de transportes alineados | Clásico, para campos suaves; no determina la acción, no da masas, fotón ni θ_W, ni la brecha |
| revisión R-02 | ν = 2(1 − x² − y² − z² + 2xyz) = 2\|a×b\|², suficiencia de la firma triple (T3) y testigo de bloqueo (T4) | Correcto; es álgebra clásica (Fricke–Vogt) |

## Reproducción

    pip install -r requirements.txt
    bash reproducir_todo.sh              # versión rápida, unos 2 minutos
    bash reproducir_todo.sh --completo   # todos los tamaños, unos 25 minutos

El script hace tres cosas:
1. **Integridad.** Comprueba el manifiesto SHA-256 de los archivos tal como se distribuyeron.
2. **Verificación.** Corre cada verificador. Cada uno tiene sus propias aserciones y falla si un enunciado no se cumple.
3. **Comparación.** Compara los resultados regenerados con `referencia_resultados/`, **con tolerancia y no bit a bit**:
   - números reales con `RTOL = 1e-9` y `ATOL = 1e-12`;
   - tres observables de PR-07, y sólo ellos, tienen una tolerancia específica, con el motivo escrito en `comparar_resultados.py`. Son `sensibilidad_mezcla` (`RTOL = 1e-7`), porque ν ≈ 7·10⁻⁸ se calcula como `1 − ½ tr` cerca de la identidad y la cancelación deja unos 2·10⁻⁹ relativos; `sensibilidad_direccion_central` (`ATOL = 1e-9`), cuyo valor exacto es 0 y lo almacenado es redondeo; y `espectro_ajustado` (`RTOL = 1e-7`), que sale de un ajuste que se detiene con tolerancia de unos 10⁻⁸;
   - enteros, booleanos, textos y estructura, exactos;
   - las parametrizaciones no únicas se comparan por su invariante. Por ejemplo, los pesos ajustados de PR-07, que con otras versiones cambian hasta un 50 %, se comparan por el espectro que producen.

En la plataforma registrada en `entorno.json`, los resultados se regeneran idénticos. En otra plataforma, otra versión de numpy o de la biblioteca de álgebra lineal cambia los últimos dígitos. Por eso la prueba de reproducibilidad es la comparación con tolerancia; el manifiesto certifica la integridad de lo distribuido.

En la versión rápida, PR-04, PR-05 y PR-06 usan tamaños reducidos y no reescriben sus `resultados.json`.

## Correcciones registradas en el camino

- **PR-03 → PR-04.** Que las pérdidas absolutas sumen algo finito no indica nada, porque siempre ocurre. La cantidad correcta es la pérdida logarítmica. La conclusión de PR-03 se sostiene porque coincide con el valor exacto conocido, no por aquel argumento.
- **Revisión de PR-01.** Las excitaciones bajas aparecen en los modos nuevos sólo cuando la duplicación agrega volumen, no cuando subdivide. Corregido en PR-02.
- **Hipótesis "SU(2) se vuelve U(1) al crecer el radio".** Va en dirección contraria a Yang–Mills puro. PR-07 la reformula: lo que cambia con la escala es qué relaciones distingue una referencia, no el grupo.
- **"Los principios seleccionan la acción de Wilson"** (corregido tras una revisión externa). Lo que se sostiene es una familia de acciones cuyo límite clásico es Yang–Mills bajo la condición cuadrática, y la comprobación del continuo es clásica.
- **El principio 4 todavía nombraba el defecto de Wilson** (segunda revisión externa). Ahora pide un defecto general `d(U) ≥ 0`, invariante bajo conjugación y nulo en la identidad. La condición cuadrática es una hipótesis aparte, y Wilson, `1 − ½ Re tr U`, es una elección particular. PR-07 agrega la acción de Manton como otra elección y `[1 − ½ Re tr U]²` como contraejemplo: empieza en orden cuatro y su límite tiende a cero.
- **"Un valor de ν distingue las tres direcciones de su(2)"** (segunda revisión externa). Es demasiado fuerte: dos direcciones no centrales alineadas dan ν = 0. Lo que distingue el centro es la familia completa de comparaciones, por `ν = ε⁴|x×y|²/8 + O(ε⁶)`. PR-07 lo verifica, con el control de transportes alineados y no alineados.
- **Tolerancias de PR-07** (segunda revisión externa). Con otras versiones de numpy y scipy, tres observables de PR-07 diferían en menos de 10⁻⁸ relativos, por encima de la tolerancia general. Tienen ahora una tolerancia específica, documentada; nada más se relajó.

## Validación de esta entrega

| Entorno | Qué se corrió | Resultado |
|---|---|---|
| Python 3.13.17, numpy 2.5.3, scipy 1.18.1 (el registrado en `entorno.json`) | `reproducir_todo.sh`, versión rápida, en una copia limpia | Todas las aserciones pasan; todo coincide con la referencia |
| Python 3.13.17, numpy 2.3.5, scipy 1.17.0 (las bibliotecas del revisor) | Lo mismo | Todas las aserciones pasan; todo coincide dentro de la tolerancia, incluidos los tres campos con tolerancia específica |
| Python 3.13.5, numpy 2.3.5, scipy 1.17.0 (revisor externo, entrega anterior) | Versión rápida | Todas las aserciones pasaron; cuatro diferencias en PR-07, menores que 10⁻⁸ relativas, que la tolerancia específica ahora cubre |

La comparación sigue detectando cambios reales. Un cambio de 10⁻⁶ en un campo con tolerancia específica falla, y uno de 2·10⁻⁹ o 10⁻⁸ en un campo con tolerancia general también. Alterar un entero, como la dimensión del núcleo común, falla.

PR-01 no se ejecutó en estas pruebas: su `verificar.py` es el del autor y su resultado se compara tal como fue entregado.

En PR-07, las secciones A a F dan exactamente los mismos valores que en la primera versión. Las secciones G y H son nuevas.

## Ruta de investigación siguiente

**PR-04** (pérdida acumulada) → **PR-05** (resolución contra influencia) → **PR-06** (flujo por el borde) → **Z₂** → **SU(2)**.

La pregunta concreta es si se puede escribir un flujo por el borde para lazos gauge que cierre, es decir, una desigualdad del tipo Simon–Lieb.
- **Z₂** es el primer caso natural, porque allí valen las desigualdades de Griffiths.
- **SU(2)** es donde no se conoce un análogo.
- Del decaimiento de correlaciones a la brecha espectral, el puente ya existe en la rama (YM-R3B, teorema espectral).

La conclusión del artículo resume qué eslabón es teorema y cuál falta.
