# O23 — La misma quinta referencia, dos cierres: interfaz suficiente y concordancia entre escalas

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Estado:** suplemento de investigación. [O] ontología, [D] definición/contrato, [T] teorema geométrico bajo las condiciones declaradas, [E] prueba finita, [F] contraejemplo, [A] abierto.  
**Continuidad:** O5 (comparaciones suficientes), O14 (composición por fronteras), O17 (contención relativa a preguntas), O19–O22 (espejos, quinta referencia, tetraedro, octaedro y teselación). Los antecedentes históricos se conservan sin alteración.

## 1. Narrativa de la diferencia pendiente [O]

Una cara triangular puede mantener sus tres referencias y producir un reflejo reconstruible. Ese reflejo conserva relaciones, pero su existencia como punto no determina todo lo que ocupa la región siguiente. La misma posición puede actuar como vértice de una celda o como centro de una cara de otra celda. **La diferencia pendiente es una distinción estructural que una consulta futura puede requerir**, no una ausencia de coordenadas ni una incertidumbre necesariamente aleatoria.

Este resultado refina «la estructura se repite hasta contener la indefinición»: la repetición puede estabilizar relaciones de interfaz y todavía necesitar una pregunta nueva para distinguir completaciones compatibles.

## 2. Construcción exacta desde una cara [D/T]

Tomar en unidades de longitud arbitrarias los cuatro vértices

\[
  P=(0,0,0),\quad A=(1,1,0),\quad B=(1,0,1),\quad C=(0,1,1).
\]

Son un tetraedro regular de arista \(\sqrt2\). La cara \(F=(A,B,C)\) está en \(x+y+z=2\), con centroide \(c=(2/3,2/3,2/3)\). Reflejar \(P\) por esa cara produce

\[
\boxed{q=(4/3,4/3,4/3)}.
\]

**Continuación T:** la envolvente \(\operatorname{conv}(A,B,C,q)\) es un tetraedro regular, en el que \(q\) es el cuarto vértice. Volumen \(V_T=1/3\).

**Continuación O:** definir el punto

\[
\boxed{w=\frac{c+q}{2}=(1,1,1)}
\]

y la segunda cara \(F'=\{2w-A,2w-B,2w-C\}\). Los seis puntos de \(F\cup F'\) forman un octaedro regular, de lado \(\sqrt2\). Su volumen es \(V_O=4/3\). Su cara opuesta tiene centroide \(q\), mientras \(q\) no es un vértice del octaedro.

**Teorema O23-T1 — indistinguibilidad del puerto geométrico:** las dos completaciones comparten exactamente la misma cara \(F\) y el mismo reflejo puntual \(q\). Si la interfaz solo admite consultas sobre \((F,q)\), ambas completaciones pertenecen a la misma clase de equivalencia. La cantidad de información estructural distinguible entre estos *dos modelos* por esas consultas es cero.

**Teorema O23-T2 — discriminante mínimo:** la pregunta *«¿q es un vértice estructural de la siguiente celda?»* separa las dos completaciones: verdadera para T y falsa para O. Si las dos completaciones son las únicas posibilidades del contrato, una distinción binaria es suficiente para clasificarlas y al menos dos respuestas distintas son necesarias. Se trata de un bit lógico **relativo a esa familia de preguntas y modelos**, no de una unidad física de masa, energía ni entropía.

**Teorema O23-T3 — reconstrucción:** dados la cara regular \(F\), el lado de ocupación que determina la celda anterior y la especie declarada \(s\in\{T,O\}\), la celda exterior es reconstruible de forma única **dentro de esta familia de poliedros euclídeos regulares**. Si \(s=T\), la quinta referencia es el vértice exterior. Si \(s=O\), el centro octaédrico es \(w=(c+q)/2\) y su cara opuesta es la imagen de F por inversión central respecto de w. Este teorema exige que la cara pertenezca a un tetraedro regular conocido o que se suministre la coorientación y escala; una cara sin interior declarado admite dos lados.

**Falsador [F]:** la igualdad de coordenadas de la quinta referencia no determina qué volumen debe contarse: \(V_O/V_T=4\). Una contabilidad de «información contenida» que igualase las dos celdas solo por compartir \((F,q)\) perdería una distinción requerida por preguntas sobre ocupación.

## 3. Contrato de la interfaz [D]

Para reconstruir una continuación local se separan cuatro piezas:

1. **Referencias comunes:** tres vértices de la cara y sus tres distancias, que acreditan la métrica local y las correspondencias de borde.
2. **Coorientación:** qué semiespacio de la cara está ya ocupado por la celda conocida. Cuando se conoce esa celda, la orientación exterior se reconstruye y no demanda una etiqueta adicional.
3. **Tipo de continuación:** T u O cuando ambas están permitidas. Es la nueva pregunta mínima de ocupación.
4. **Concordancia global:** cómo se relacionan los tipos en otras caras y cómo se evitan solapamientos, recorridos contradictorios y huecos. No se deduce del puerto aislado.

En particular, el número de bits de una representación de interfaz depende de las preguntas futuras. La cara etiquetada por coordenadas puede exigir más información numérica que el simple tipo lógico, y una descripción global ya conocida puede hacer innecesario retransmitir la etiqueta T/O en cada cara.

## 4. Transmisión de la estructura en la trama tetra–octa [T/E]

En la teselación **específica** de O22, cada cara conecta un tetraedro con un octaedro. Sea \(G^*\) el grafo dual: vértices = celdas, aristas = caras compartidas. Sea \(\chi(v)\in\{0,1\}\) el tipo, con contrato \(\chi(v)\oplus\chi(w)=1\) sobre cada arista del dual.

**Teorema O23-T4:** en un grafo dual conectado, la transmisión consistente de un tipo inicial por todas las caras existe si y solo si todos los ciclos tienen longitud par (el grafo es bipartito). Si existe, la asignación queda determinada por una sola clase inicial, salvo la inversión global de clases. *Conocer el número de caras de cada celda puede eliminar incluso esa ambigüedad: las celdas T tienen cuatro caras y las O ocho.*

Esto es un resultado combinatorio condicionado a una regla de alternancia ya elegida. No demuestra que la cara triangular, por sí sola, obligue a alternar T y O, ni que todo grafo bipartito tenga una realización geométrica sin cruces. En O22, además se verificaron posiciones y empalmes de la red periódica: para período \(N=4\), 64 tetraedros, 32 octaedros y 256 caras dobles; para \(N=6\), 216, 108 y 864, respectivamente. O23 repite estos controles mediante un laboratorio independiente.

**Falsador:** un circuito impar no admite ese contrato de tipos: volver al nodo inicial pediría un tipo diferente del que salió. Una estructura global de «comunes» no puede deducirse sin verificar las relaciones de recorrido.

## 5. Cambio uniforme de escala y papel del signo [T]

Si transformamos cada referencia mediante una similitud euclídea \(x\mapsto sQx+b\), con \(s>0\) y \(Q\) ortogonal, entonces la reflexión, los centroides, la clasificación de vértices, las incidencias y la operación de reconstrucción conmutan con el cambio de escala:

\[
\boxed{\mathrm{Continuar}(sQF+b,sQp+b;\mathrm{tipo})
      =sQ\,\mathrm{Continuar}(F,p;\mathrm{tipo})+b}.
\]

Las longitudes pasan a \(s\) veces las iniciales; los volúmenes pasan a \(s^3\) veces. La relación \(V_O/V_T=4\) y el bit lógico de especie permanecen invariantes.

El papel relacional del signo de escala/referente se expresa mediante las operaciones de multiplicación y división al pasar de una representación a otra, sin equipararlo a los signos de las coordenadas de una figura.

**Dos regímenes distintos de radio:** O20 genera capas concéntricas mediante el factor geométrico \(5/3\), preservando un centro global; O22 mantiene un lado local constante al desplazar las celdas en una teselación. La similitud de O23 transporta una descripción completa entre escalas, pero **no selecciona por sí sola la ley de crecimiento físico ni equivale a la operación generativa O20**.

Un ejemplo preciso: los seis puntos medios del tetraedro original forman el octaedro interno de O21, con lado \(a/2\). Multiplicar sus distancias respecto de su centro por dos produce un octaedro de lado \(a\). Para empalmarlo además hay que escoger posición y orientación compatibles con la cara. Igualar escalas no resuelve automáticamente la ocupación.

## 6. Consecuencia para la contención de información [O/D/A]

El programa interpreta que la masa es **la contención de información en este plano**. O23 proporciona una forma de plantear preguntas acerca de qué información transmite una interfaz:

\[
\text{continuaciones }X=\{T,O\},\quad
\pi_{F,q}(T)=\pi_{F,q}(O),\quad
Q_{\mathrm{vértice}}(T)\ne Q_{\mathrm{vértice}}(O).
\]

Así, una descripción puede conservar todas sus lecturas existentes y necesitar refinamiento para distinguir una relación exterior nueva. El volumen físico y el número de vértices son observables geométricos del modelo; todavía no constituyen una definición física de masa ni una fórmula de energía. No se atribuye una magnitud de masa a la etiqueta de especie por el solo hecho de añadir un bit de comparación.

## 7. Pruebas y procedencia [E]

`laboratorio_o23.py` usa fracciones racionales exactas, sin paquetes externos, y prueba: reconstrucción para las cuatro caras, todas las permutaciones de etiquetas de F, transformaciones con escala racional y transformaciones ortogonales con reflexión, relación volumétrica, el criterio discriminante, incompatibilidad de ciclos impares, propagación de clases y red periódica en N=4 y N=6. Se conserva íntegro el ZIP O22 y se vuelve a ejecutar su suite de pruebas.

La comprobación numérica de ejemplos finitos respalda la implementación de los teoremas anteriores, pero no reemplaza sus demostraciones generales.

## 8. Alcance, novedad y ruta O24 [A]

- **Logro específico O23:** la misma cara y quinta referencia permiten dos roles estructurales diferentes; una pregunta futura diferencia las completaciones. La alternancia de tipos admite una regla exacta de transporte sobre el dual de O22.
- **Antecedentes matemáticos:** reflexiones euclídeas, tetraedros, octaedros, grafos bipartitos y equivariancia bajo similitudes son resultados y técnicas conocidas. La contribución es su integración como contrato falsable del programa; no se presenta como descubrimiento original universal.
- **Obligación O24:** determinar si una regla de continuación seleccionada por el cierre propio, sin programar explícitamente «alternar tetra/octa», puede reproducir simultáneamente ausencia de huecos, consistencia de recorridos y transmisión mínima de información. Evaluar también interfaces donde se permitan más de dos tipos y comportamientos de escala no uniformes.
- **Abierto en física:** ningún resultado en O23 selecciona masa en kg, radio del protón, gravedad, flujo de Navier–Stokes o Yang–Mills. Todos requieren dinámica y observables calibrados adicionales.

## Glosario mínimo

**Cara:** tres referencias y sus comparaciones de distancia. **Reflejo:** nueva posición obtenida de la reflexión de una referencia anterior. **Tipo de continuación:** familia de relaciones de la celda exterior. **Cierre de interfaz:** capacidad de reconstruir respuestas de una familia de consultas; no ausencia absoluta de alternativas. **Comunes:** relaciones simultáneas sostenidas por varias unidades. **Signo de escala:** papel multiplicativo/divisivo al comparar escala y referente. **Foco local:** referencia reconstruible por cada celda; una red translacional infinita no selecciona por sí sola un foco global privilegiado.
