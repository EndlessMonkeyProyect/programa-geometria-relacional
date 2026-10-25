# Vínculo directo, indeterminación y certificado negativo: nueva lectura de P
**Propuesta ontológica del programa [O/A]; teorema restringido para grafos explícitos [T].**

## La propuesta nueva del diálogo

La expresión **«P puede ser de un cristal directo»** se conserva literalmente, sin atribuirle un significado único no acreditado. Una interpretación operacional que ponemos a prueba es: un estado relacional deja disponible una **firma de sus vínculos suficientes** para contestar una consulta sin enumerar todas sus posibles realizaciones internas. Una indeterminación puede significar múltiples continuaciones compatibles, no azar ni fracaso del procedimiento. Queremos que P también pueda responder que **no existe un vínculo pertinente**, incluso si no ofrece una ruta a la solución.

Esta intuición exige separar tres mensajes de un comparador: `VINCULO_ACREDITADO` (existe ruta o relación compatible), `SIN_VINCULO_EN_ESTE_CONTRATO` (no está conectado por las operaciones declaradas) y `CONTRADICCION/IMPOSIBILIDAD` (ninguna continuación satisface las restricciones). **No equivalen entre sí.** Una pregunta incompleta o una representación que perdió correlaciones no autoriza afirmar imposibilidad.

## Caso demostrado: grafo dirigido explícito

Sea G=(V,E) finito, presentado **explícitamente** por sus vértices y aristas, s origen y t destino. Un recorrido BFS o DFS computa R, los vértices alcanzables desde s, en tiempo O(|V|+|E|). Si t∈R, una lista de aristas de s a t es un testigo positivo verificable. Si t∉R, el par `(R; s∈R, t∉R, para cada (u,v) con u∈R: v∈R)` es un certificado negativo: cualquier recorrido que parta de s se queda en R, por lo que no puede llegar a t.

La certificación negativa también se comprueba en O(|V|+|E|), porque R es un conjunto explícito y se inspeccionan las aristas. **El algoritmo determina el resultado incluso cuando no existe ruta.** Esto implementa la intuición en un dominio ya conocido en P, sin resolver P versus NP.

## Comparaciones más expresivas: paridad y restricciones

En XOR binario, Union-Find con paridad conserva diferencias de valor a un representante. Entre dos componentes independientes no hay relación de paridad **forzada**, aunque sí existen asignaciones globales. Agregar una arista entre componentes puede imponer una relación; cerrar un ciclo puede ser redundante o generar contradicción. La distinción entre independencia y contradicción es observable, no retórica.

En un problema de satisfacibilidad general, no hallar vínculos locales no significa que la instancia sea imposible. Un grafo de variables puede ser conectado y aun así no admitir ninguna asignación, o contener componentes independientes y muchas soluciones. Por ejemplo, K4 no admite tres colores, aunque es completamente conectado. Incluso cuando existe un **grafo explícito de estados** cuyo camino codifica la solución, ese grafo puede tener **exponencialmente muchos estados respecto del tamaño de la entrada original**. No se puede medir P con el tamaño de un objeto exponencial ya regalado.

El programa ha estudiado interfaces suficientes `Γ_H(b)=∃i H(i,b)` y firmas de frontera. El cuello de botella no es solo consultar la firma ya calculada: hay que acotar uniformemente construcción, composición, normalización, almacenamiento y consulta. El mismo soporte exterior puede ocultar correlaciones ternarias, tiempos de generación muy distintos o memoria creciente.

## Qué hay que demostrar para tocar P versus NP

Elegir una clase NP-completa en su representación usual —por ejemplo, la 3-coloración de grafos— y proporcionar un algoritmo determinista, uniforme y correcto en **todas** las entradas de n bits que produzca positivo o negativo en costo `n^k` para alguna constante k independiente de la entrada. Se deben contabilizar búsqueda y validación de firmas, incorporación de nuevos vínculos, memoria, los casos adversariales y la salida negativa. Para P=NP bastaría resolver una clase NP-completa así. El procedimiento de alcanzabilidad no basta, porque resuelve una clase especial ya conocida en P.

## Experimento siguiente — protocolo anti-autoengaño

1. Mantener grafos como ruta principal, SAT solo como contraste de límites. Definir claramente qué es el «cristal» (una firma reconstruible y consultas habilitadas) y cómo se construye.
2. Comparar en la misma ejecución un caso con ruta, otro sin ruta y otro con vínculos ausentes pero soluciones existentes; obtener pruebas verificables de cada estado.
3. Extender de paridad XOR a restricciones de tres o más referencias sin proyectar fuera correlaciones conjuntas. Agregar instancias adversariales sin testigos locales simples.
4. Medir la complejidad contra el tamaño **original** de la entrada, incluyendo el fracaso. No confundir un certificado del no-vínculo con una prueba universal de inexistencia de solución.

**Dictamen:** el avance conceptual válido es un **sistema de decisión con negativo certificable en un contrato explícito**. La generalización uniforme a NP-completos sigue abierta. La afirmación P=NP no está establecida por estas pruebas.
