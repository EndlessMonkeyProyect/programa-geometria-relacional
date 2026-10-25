# Auditoría focal de N1-B y T8 — Hilo del Dos v2.7

**Fecha:** 14 de octubre de 2026  
**Método:** lectura de los documentos, inspección del constructor de certificados, y ejecución independiente de `python -m unittest discover -s tests -q`: **85 pruebas correctas**.

## 1. N1-B: alcance exacto

**Proposición defendible.** Para el algoritmo O2c especificado (eliminación de variables ternarias, representación extensional de factores y poda de factores vacíos/redundantes), una corrida que determina insatisfacibilidad puede acompañarse de una refutación por resolución de la codificación CNF de 3-coloración, con longitud limitada por una constante multiplicativa del número de candidatos enumerados. Los certificados construidos en el paquete respetan la cota de 2 veces los candidatos en los casos probados.

**Verificación.** `Prueba.comprobar` comprueba cada resolvente por sus dos antecedentes y pivote. `corrida_trazada` registra nogoods e inserta resoluciones sobre los tres colores usando las cláusulas de al-menos-un-color. Para los casos disponibles, devuelve cláusula vacía; los selectores min-fill y relacional se comparan con la implementación original.

**Límites esenciales.**
1. No hay prueba de una cota inferior para *todo algoritmo* de 3-coloración. El resultado sólo se aplica a algoritmos cuyos pasos admiten esta simulación eficiente.
2. Para pasar de los ensayos a un teorema completamente auditado conviene explicitar el invariante de nogood: toda cláusula etiquetada para una fila es consecuencia de las entradas y queda falsada por esa fila. Demostrar inducción sobre proyección, normalización y detección de tabla vacía.
3. Establecer contablemente `#resoluciones ≤ 2·total_candidates` incluyendo las resoluciones que vacían la interfaz y detenciones anticipadas. La evidencia experimental no reemplaza el argumento para todos los tamaños.
4. El costo de cómputo del selector puede ser arbitrario; el no-go limita el número de candidatos del motor, no afirma eficiencia del selector.
5. La transferencia de la cota exponencial externa requiere confirmar exactamente la distribución de grafos aleatorios, la codificación CNF y el modelo de resolución del resultado citado.

**Estado ROS-1:** OPEN para cierre general formal; ANCHORED para la simulación operacional. No corresponde extrapolarlo a P vs NP.

## 2. T8: geometría combinatoria y geometría física

**Resultados matemáticos internos defendibles.** Para `n` distinciones binarias, representar cada estado por todas las paridades no triviales da un código símplex binario: `2^n` estados, `2^n−1` coordenadas y distancia de Hamming `2^(n−1)` entre palabras distintas. En particular, `n=2` produce cuatro vectores equidistantes en tres coordenadas y la identidad XOR de cuatro estados. La imposibilidad de un quinto punto equidistante vale **en dimensión euclidiana tres**; en dimensión cuatro sí cabe un símplex regular de cinco vértices.

**Distinción obligatoria.** La aplicación de distancias de Hamming ya define una métrica sobre las palabras. Incorporar esos vectores en R³ añade una realización euclidiana concreta. El determinante de Cayley–Menger nulo para cinco puntos es una consecuencia de haber elegido dimensión tres, no una derivación de que el mundo tenga tres dimensiones o de que la distancia física deba existir.

**Enunciado propuesto más preciso.** «Si dos distinciones binarias se representan mediante las tres paridades no triviales, los cuatro estados resultantes admiten una realización como tetraedro regular en dimensión euclidiana tres. La incorporación de un quinto punto en esa misma dimensión obliga a restricciones de compatibilidad entre distancias. Que esta estructura sea el origen de la métrica física permanece como hipótesis».

**Falsadores y puentes necesarios.**
- Justificación relacional interna de por qué *exactamente* dos distinciones son obligatorias; de lo contrario, el mismo proceso permite 1, 3, 4... distinciones y dimensiones 1, 7, 15...
- Un criterio físico que seleccione dimensión espacial 3 frente a 7/15, sin fijar dimensión a priori.
- Una construcción operacional que convierta diferencias de información en distancias con unidades, escalas y observables (sin calibrar el resultado deseado).
- Alguna predicción discriminante, distinta de las identidades de códigos y distancias euclidianas ya conocidas.

**Estado ROS-1:** RESOLVED dentro de la identidad del código y geometría condicional; OPEN para emergencia del espacio físico.

## 3. Ruta mínima siguiente

1. Escribir y probar el invariante inductivo de certificados N1-B y su contabilidad exacta (nivel prueba matemática independiente del test).
2. Introducir explícitamente una familia `T8(n)` y comparar los casos `n=1,2,3`, para que el paso al espacio tridimensional no sea una elección encubierta.
3. Exigir un puente de unidades/observables antes de asociar las razones de radio o las distancias del código a masas o longitudes físicas.

## Dictamen

El avance es real como **restricción de un método de cálculo** y como **representación geométrica consistente**. La frontera que permanece abierta es el paso desde propiedades de representaciones elegidas hasta una necesidad física o una cota de complejidad universal.
