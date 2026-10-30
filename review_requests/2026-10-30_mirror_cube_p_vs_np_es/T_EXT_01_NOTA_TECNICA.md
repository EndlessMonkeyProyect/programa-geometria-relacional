# T-EXT-01 — Cota de información contextual

### T-EXT-01: información mínima para continuaciones exteriores [T/E]

**Contrato y alcance.** Fijamos $n\ge2$ vértices etiquetados $V=A\sqcup B$, con $|A|=\lfloor n/2\rfloor$ y $|B|=\lceil n/2\rceil$. Nuestra familia es

$$
\mathcal H_n=\{H_E=(V,E):E\subseteq A\times B\}.
$$

Todos estos grafos son bipartitos y admiten 3-coloraciones. En **esta** prueba, la interfaz exterior contiene **todos los vértices de $V$**: una continuación puede unir dos vértices nuevos a cualquier par $u\in A$, $v\in B$. No se afirma que la misma cota valga para una interfaz propia que solo exponga unos pocos vértices interiores.

Para cada par $u\in A$, $v\in B$, definimos la continuación $D_{uv}$ añadiendo dos vértices nuevos $a,b$ y exactamente las cinco aristas

$$
D_{uv}=\{ab,au,av,bu,bv\}.
$$

La consulta $Q(H_E\cup D_{uv})$ pregunta si el grafo aumentado es 3-coloreable. Una *firma autosuficiente* $\Phi(H_E)$ debe responder esa consulta para **todos** los pares mediante funciones de lectura $d_{uv}$, sin acceso adicional al grafo original que no esté contado en la representación:

$$
Q(H_E\cup D_{uv})=d_{uv}(\Phi(H_E)).
$$

**Teorema T-EXT-01 (cota exacta de estados contextuales).** Bajo este contrato, toda firma autosuficiente distingue al menos

$$
\boxed{2^{|A||B|}=2^{\lfloor n^2/4\rfloor}}
$$

estados. En una codificación binaria de longitud fija esto exige al menos $\lfloor n^2/4\rfloor$ bits. Para esta familia, la cota en bits es ajustada: registrar la matriz de adyacencia de los pares $A\times B$ emplea exactamente esa cantidad, sin que ello garantice lectura eficiente para todas las familias de continuaciones posibles.

**Demostración.** Primero, para todo $E\subseteq A\times B$ y todo par $uv\in A\times B$ se cumple

$$
\boxed{H_E\cup D_{uv}\text{ es 3-coloreable}\iff uv\notin E.}
$$

Si $uv\in E$, los cuatro vértices $a,b,u,v$ inducen un $K_4$ y no admiten tres colores. Si $uv\notin E$, coloreamos $A\setminus\{u\}$ con 0, $B\setminus\{v\}$ con 1, $u$ y $v$ con 2, y los vértices nuevos $a,b$ con 0 y 1, respectivamente. Esta asignación es válida: las aristas originales solo conectan $A$ con $B$, $uv$ está ausente y las cinco aristas nuevas tienen extremos de distinto color.

Si $E\ne E'$, existe un par $uv$ presente exactamente en uno de los dos conjuntos. La continuación $D_{uv}$ da respuestas distintas para $H_E$ y $H_{E'}$. Una firma que permitiera responder todas las consultas no puede identificarlos. Hay $2^{|A||B|}$ subconjuntos de aristas, luego igual número de firmas distinguibles. Una codificación fija con $b$ bits representa a lo sumo $2^b$ estados, de donde $b\ge |A||B|=\lfloor n^2/4\rfloor$. $\square$

**Control independiente [E].** El verificador `verificar_T_EXT_01.py` ensaya exhaustivamente las $16$ instancias sobre cuatro vértices y las $512$ sobre seis. Comprueba la equivalencia anterior para los $4$ o $9$ pares disponibles por instancia: **64 + 4.608 = 4.672 consultas**, sin fallos, y cuenta $16$ y $512$ firmas de respuesta diferentes, respectivamente. Es una comprobación finita de la prueba general, no su fundamento.

**Relación con R5 y R6.** R5 distingue lo que una firma de frontera conserva bajo continuaciones exteriores y pierde ante modificaciones interiores; R6 identifica las distinciones necesarias para inserciones de aristas **sin nuevos vértices** sobre $V$. T-EXT-01 fija otro contrato: **incorporaciones con dos vértices nuevos que pueden contactar todos los vértices de $V$**. Esta familia de consultas recupera individualmente cada arista de $A\times B$. Así cuantifica una barrera informacional de referencia externa, aun cuando la colorabilidad inicial de toda la familia es fácil.

**Límite del resultado.** La cota es cuadrática, no superpolinómica. No demuestra una cota de tiempo para 3-coloración general, ni una barrera de memoria adicional si el algoritmo conserva acceso libre al grafo original, ni la misma cota para una frontera pequeña. La construcción se asemeja a argumentos de familias distinguibles, equivalencia contextual y complejidad de comunicación; su prioridad bibliográfica requiere examen independiente. Es una proposición matemática acotada, no una solución de P frente a NP.

