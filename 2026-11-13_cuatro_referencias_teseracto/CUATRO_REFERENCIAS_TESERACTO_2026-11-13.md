# Cuatro referencias, paridad y reconstrucción de un teseracto

**Correspondencia entre configuraciones binarias, reflexiones y observación**  
**Publicación técnica · Versión 1.1 · 13 de noviembre de 2026**

**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program

## Resumen

Cuatro distinciones binarias independientes generan un espacio de 16 configuraciones cuyo grafo de cambios individuales es el hipercubo $`Q_4`$. La separación por paridad determina dos conjuntos de ocho vértices cuyas envolventes convexas son 16-celdas (hexadecacorones), cada una delimitada por 16 celdas tetraédricas. Las seis comparaciones binarias por pares determinan exactamente ocho firmas: cada firma reúne una configuración y su complemento global, conserva la paridad y deja una elección binaria sin resolver. Se caracteriza la imagen de estas comparaciones y se establece una reconstrucción explícita.

El contraste con la caja de espejos distingue esta construcción del arreglo de los cuatro planos de las caras de un tetraedro regular, que produce 15 regiones abiertas. Se prueban dos obstrucciones: las reflexiones físicas de las caras no conmutan y toda órbita estable no vacía bajo ellas es infinita. Se formula una condición necesaria y suficiente para etiquetar una órbita con los 16 estados mediante un cociente compatible con las reflexiones, y se verifica para los cuatro espejos: la órbita del centroide nunca regresa a una configuración anterior y se reparte en 16 clases que se transforman exactamente como $`Q_4`$. La etiqueta de cada configuración es la paridad de sus reflexiones en cada espejo. La secuencia distingue cierre, herencia, superposición y dimensión de comparación de una dimensión espacial adicional.

**Palabras clave:** tetraedro; teseracto; hipercubo; 16-celda; paridad; firma de observación; reflexión; producto libre; cociente; información suplementaria.

## Estado de los enunciados

| Enunciado | Estado | Condición o alcance |
|---|---|---|
| Cuatro cambios binarios producen $`Q_4`$ | **Exacto** | Operaciones $`T_i(x)=x\oplus e_i`$ |
| Cada familia de paridad forma una 16-celda | **Exacto** | Representación en los vértices $`(\pm1)^4`$ |
| La firma por pares tiene ocho fibras de tamaño dos | **Exacto** | Observación XOR de los seis pares |
| La paridad es observable por pares si y solo si $`n`$ es par | **Exacto** | $`n\geq2`$ referencias y comparación completa |
| Los cuatro planos de las caras determinan 15 regiones | **Exacto** | Tetraedro regular y planos completos fijos en $`\mathbb R^3`$ |
| Una órbita estable bajo esas cuatro reflexiones es infinita | **Exacto** | Órbita no vacía; reflexiones euclidianas literales |
| Las cuatro reflexiones generan un producto libre | **Exacto** | Lema 1; resultado clásico [2–5] |
| La órbita del centroide se etiqueta con los 16 estados | **Exacto** | Teorema 6; vale para casi todo punto inicial y falla sobre los planos de los espejos |
| Identificar esos 16 estados con una cuarta dirección física | **Abierto** | Requiere hipótesis geométricas adicionales |

## 1. Punto de partida: referencia, distinción y observación

Una **distinción** separa estados según una respuesta posible; una **relación** permite comparar respuestas; una **firma** reúne las respuestas que una observación conserva. El **cierre** designa una organización capaz de mantener las relaciones declaradas bajo las operaciones admitidas. La **herencia** consiste en recuperar relaciones anteriores desde una representación posterior, mientras que la **información suplementaria** distingue estados que una firma había reunido.

Esta secuencia procede de los documentos rectores del programa; las definiciones generales de economía, actualizaciones y suficiencia de firmas conservan allí sus propios contratos. El presente artículo examina una realización concreta dentro de esas definiciones.

En el nivel geométrico, cuatro puntos no coplanares forman el primer *simplex* de volumen tridimensional positivo: el tetraedro. En el nivel de configuraciones, cuatro distinciones binarias permiten 16 asignaciones. Son afirmaciones diferentes: la primera depende de independencia afín en $`\mathbb R^3`$; la segunda, de cuatro coordenadas binarias independientes. La conexión se establece mediante operaciones y observaciones explícitas.

## 2. Cuatro distinciones y el grafo del teseracto

Sea $`R=\lbrace r_1,r_2,r_3,r_4\rbrace`$ el conjunto de referencias y

```math
X=\mathbb F_2^4,\qquad T_i(x)=x\oplus e_i,\quad 1\leq i\leq4,
```

donde $`e_i`$ contiene un $`1`$ en la posición $`i`$ y ceros en las otras. Los cambios satisfacen

```math
T_i^2=I,\qquad T_iT_j=T_jT_i,
```

```math
T_1^{a_1}T_2^{a_2}T_3^{a_3}T_4^{a_4}=I
\quad\Longleftrightarrow\quad a_1=a_2=a_3=a_4=0.
```

**Teorema 1 (órbita y grafo de Cayley).** El grupo $`G=\langle T_1,T_2,T_3,T_4\rangle\cong(\mathbb Z/2\mathbb Z)^4`$ actúa libre y transitivamente sobre $`X`$. Su grafo de Cayley para los generadores $`T_i`$ es $`Q_4`$, con 16 vértices y 32 aristas.

**Demostración.** Para cada $`a=(a_1,a_2,a_3,a_4)`$, el producto $`T_1^{a_1}\cdots T_4^{a_4}`$ envía $`0000`$ a $`a`$, con unicidad. La acción es transitiva y ningún elemento no trivial fija un estado. Cada vértice tiene cuatro vecinos; el número de aristas es $`16\cdot4/2=32`$. $`\square`$

La representación $`x\mapsto((-1)^{x_1},\ldots,(-1)^{x_4})`$ realiza sus 16 vértices como los del teseracto en $`\mathbb R^4`$. Los $`T_i`$ son cambios binarios; su relación con las reflexiones de las caras de un tetraedro físico se establece en las secciones 6 y 7.

## 3. Paridad: dos 16-celdas

Defínase

```math
p(x)=x_1\oplus x_2\oplus x_3\oplus x_4,
\qquad X_\varepsilon=\lbrace x\in X:p(x)=\varepsilon\rbrace.
```

Cada $`X_\varepsilon`$ posee ocho vértices. Un único $`T_i`$ cambia la paridad; una composición de un número par de cambios la conserva.

**Proposición 1 (16-celdas).** La envolvente convexa de la representación geométrica de cada $`X_\varepsilon`$ es una 16-celda o *hexadecacoron*: ocho vértices, 24 aristas y 16 celdas tetraédricas. Su grafo es $`K_8`$ menos un emparejamiento perfecto.

**Demostración.** Los ocho vértices de paridad par son $`\lbrace\pm u_1,\ldots,\pm u_4\rbrace`$, donde

```math
\begin{aligned}
u_1&=(1,1,1,1),&u_2&=(1,1,-1,-1),\\
u_3&=(1,-1,1,-1),&u_4&=(1,-1,-1,1).
\end{aligned}
```

Estos cuatro vectores son ortogonales entre sí y tienen la misma norma. Su envolvente es, por una transformación ortogonal y de escala, el politopo cruzado de dimensión cuatro. El conjunto impar se obtiene por una reflexión en una coordenada y produce una copia congruente. En cada familia, los únicos pares de vértices no unidos por arista son los cuatro pares antipodales (distancia de Hamming cuatro); todos los demás están a distancia dos. Por tanto hay $`(8\cdot6)/2=24`$ aristas y, como en el politopo cruzado de dimensión cuatro, 16 facetas tetraédricas. $`\square`$

**Distinción de figuras.** $`Q_4`$ es el grafo de los 16 estados con aristas de distancia uno, siempre entre par e impar. Cada 16-celda es la envolvente de una sola familia de ocho vértices, con aristas de distancia dos. La cifra 16 de su nombre cuenta sus celdas tetraédricas; sus vértices son ocho.

La operación de tomar vértices alternos del teseracto aparece en el apéndice H de *A New Era of Thought* (1888), bajo el nombre *tetra-tessaract*. El prefacio atribuye expresamente ese apéndice a **Alicia Boole y H. John Falk**, editores del libro de **Charles Howard Hinton** [1].

## 4. Comparaciones por pares y elección global

Defínase la firma completa de seis comparaciones:

```math
\Phi:X\longrightarrow\mathbb F_2^6,
\qquad \Phi(x)=(q_{12},q_{13},q_{14},q_{23},q_{24},q_{34}),
\qquad q_{ij}=x_i\oplus x_j.
```

**Teorema 2 (fibras de la firma).** Se cumple

```math
\Phi(x)=\Phi(y)\quad\Longleftrightarrow\quad
 y=x\ \text{o}\ y=x\oplus1111.
```

**Demostración.** De la igualdad de firmas se sigue $`x_i\oplus y_i=x_j\oplus y_j`$ para cualesquiera $`i,j`$. Los cuatro términos son, pues, un mismo bit $`c`$, de donde $`y=x\oplus(c,c,c,c)`$. Las dos posibilidades $`c=0`$ y $`c=1`$ producen efectivamente la misma firma. $`\square`$

Existen, por consiguiente, ocho firmas, cada una con dos preimágenes. La imagen se caracteriza sin enumeración completa:

**Proposición 2 (imagen y reconstrucción).** Una sextupla $`q\in\mathbb F_2^6`$ pertenece a $`\operatorname{im}\Phi`$ si y solo si satisface las ecuaciones triangulares

```math
q_{ij}\oplus q_{jk}\oplus q_{ik}=0
\quad\text{para toda terna }\lbrace i,j,k\rbrace\subseteq\lbrace 1,2,3,4\rbrace.
```

Tres de esas cuatro ecuaciones son independientes. Equivalentemente, se requieren

```math
q_{23}=q_{12}\oplus q_{13},\qquad
q_{24}=q_{12}\oplus q_{14},\qquad
q_{34}=q_{13}\oplus q_{14}.
```

**Demostración y algoritmo.** Las identidades se siguen sustituyendo $`q_{ij}=x_i\oplus x_j`$. En sentido inverso, fijar $`x_1=0`$ y definir

```math
x_2=q_{12},\qquad x_3=q_{13},\qquad x_4=q_{14}
```

reproduce las otras tres comparaciones por las ecuaciones indicadas. El único otro estado compatible es el complemento global. $`\square`$

La paridad se obtiene directamente de la firma:

```math
p(x)=q_{12}\oplus q_{34}
     =q_{13}\oplus q_{24}
     =q_{14}\oplus q_{23}.
```

Por ejemplo, $`0000`$ y $`1111`$ producen la misma firma $`000000`$, y ambos tienen paridad par. **La indefinición es la elección global** entre los dos estados complementarios que la observación por pares reúne en una misma firma; la paridad es otra partición, y la firma la conserva.

### 4.1. Qué cambia al incorporar una quinta referencia

Para $`n\geq2`$, sean $`X_n=\mathbb F_2^n`$, $`\Phi_n(x)=(x_i\oplus x_j)_{i<j}`$ y $`p_n(x)=\bigoplus_{i=1}^n x_i`$.

**Teorema 3 (paridad y número de referencias).** Cada fibra de $`\Phi_n`$ tiene exactamente dos estados, $`x`$ y $`x\oplus1^n`$. La paridad $`p_n`$ puede recuperarse de la firma si y solo si $`n`$ es par.

**Demostración.** El argumento del teorema 2 da $`\ker\Phi_n=\lbrace 0,1^n\rbrace`$ y, en consecuencia, $`2^{n-1}`$ firmas. Además,

```math
p_n(x\oplus1^n)=p_n(x)\oplus(n\bmod2).
```

Si $`n`$ es par, los dos estados de una fibra tienen igual paridad y esta queda determinada por la firma; si $`n`$ es impar, poseen paridades opuestas y ninguna función de la firma puede determinarlas. $`\square`$

En cuatro referencias hay 16 estados, ocho firmas y paridad observable. En cinco hay 32 estados, 16 firmas y una paridad global que las diferencias por pares dejan sin determinar. Este cambio exacto pertenece a las firmas de comparación y permite formular una consulta sobre la quinta referencia; su lectura como esfera física o como dirección espacial adicional es una hipótesis aparte.

## 5. Los cuatro planos de las caras: 15 regiones

Considérese el tetraedro regular con vértices

```math
\begin{aligned}
v_1&=(1,1,1),&v_2&=(1,-1,-1),\\
v_3&=(-1,1,-1),&v_4&=(-1,-1,1).
\end{aligned}
```

La cara opuesta a $`v_i`$ pertenece al plano $`H_i=\lbrace z\in\mathbb R^3:v_i\cdot z=-1\rbrace`$. Los cuatro planos completos forman un arreglo de hiperplanos. El centroide del tetraedro es el origen.

**Teorema 4 (conteo de regiones).** El complemento $`\mathbb R^3\setminus\bigcup_iH_i`$ tiene exactamente **15 regiones abiertas**.

**Demostración.** Se cumple $`\sum_i v_i=0`$. Un punto exterior a todas las caras satisfaría $`v_i\cdot z<-1`$ para los cuatro índices, lo que al sumar daría $`0<-4`$, imposible.

Recíprocamente, para cualquier subconjunto propio $`S`$ de índices de tamaño $`k\in\lbrace 1,2,3\rbrace`$, considérese

```math
a_i=\begin{cases}
-2,&i\in S,\\[2pt]
\displaystyle\frac{2k}{4-k},&i\notin S.
\end{cases}
```

Se tiene $`\sum_i a_i=0`$. Los vectores $`v_i`$ abarcan $`\mathbb R^3`$ y satisfacen una sola relación lineal, $`\sum_i v_i=0`$; por tanto, el mapa $`z\mapsto(v_i\cdot z)_i`$ tiene como imagen el hiperplano de cuádruplos de suma cero. Existe así un $`z`$ con $`v_i\cdot z=a_i`$, exterior exactamente para $`i\in S`$. Para $`S=\varnothing`$ sirve $`z=0`$. Se realizan 15 patrones de signos y falta solo el patrón exterior a las cuatro caras. Cada patrón realizable define una intersección de semiespacios abiertos, que es convexa y conexa; corresponde por tanto a una sola región. $`\square`$

El número 15 cuenta **regiones de los planos fijos**. Las configuraciones de una órbita de reflexiones repetidas son otro objeto, estudiado en las secciones 6 y 7.

## 6. Reflexiones físicas y obstrucciones exactas

Sea $`S_i`$ la reflexión euclidiana respecto de $`H_i`$. En estas coordenadas,

```math
S_i(z)=z-\frac{2}{3}(v_i\cdot z+1)v_i.
```

Como $`v_i\cdot v_j=-1`$ para $`i\ne j`$, las normales de las caras ni son paralelas ni ortogonales; las reflexiones $`S_i`$ y $`S_j`$ no conmutan.

**Proposición 3 (obstrucción de conmutatividad).** Sea $`D`$ un dominio estable bajo $`S_i,S_j`$ y $`F:D\to\mathbb F_2^4`$ una función inyectiva. Si

```math
F(S_i z)=T_i(F(z))\quad\text{y}\quad F(S_j z)=T_j(F(z))
\qquad(z\in D),
```

entonces $`S_iS_j=S_jS_i`$ sobre $`D`$.

**Demostración.** Para cada $`z\in D`$,

```math
F(S_iS_jz)=T_iT_jF(z)=T_jT_iF(z)=F(S_jS_iz).
```

La inyectividad de $`F`$ obliga a la igualdad de las dos configuraciones físicas. $`\square`$

Las dos composiciones coinciden solo sobre la recta de la arista común. Sea $`\alpha`$ el ángulo entre $`v_i`$ y $`v_j`$, con $`\cos\alpha=-1/3`$. La composición $`S_iS_j`$ es una rotación alrededor de la recta $`H_i\cap H_j`$ de ángulo $`\pm2\alpha`$, y $`S_jS_i`$ es su inversa; por tanto $`S_iS_jz=S_jS_iz`$ equivale a que la rotación de ángulo $`4\alpha`$ fije $`z`$. Como $`\cos\alpha\notin\lbrace 0,\pm1\rbrace`$, ese ángulo no es múltiplo de $`2\pi`$, y sus puntos fijos son exactamente los de la recta $`H_i\cap H_j`$.

**Corolario 1.** Ningún dominio no vacío $`D`$ estable bajo dos reflexiones $`S_i,S_j`$, con $`i\neq j`$, admite una función inyectiva $`F`$ que cumpla las ecuaciones de la proposición 3.

**Demostración.** Por la proposición 3, todo $`z\in D`$ cumple $`S_iS_jz=S_jS_iz`$; luego $`z\in H_i\cap H_j`$ y $`S_iz=z`$. La ecuación $`F(S_iz)=F(z)\oplus e_i`$ da entonces $`F(z)=F(z)\oplus e_i`$, imposible. $`\square`$

**Proposición 4 (obstrucción de finitud).** Todo subconjunto no vacío $`D\subseteq\mathbb R^3`$ estable bajo las cuatro reflexiones de las caras del tetraedro anterior es infinito. En particular, toda órbita de un punto es infinita.

**Demostración.** Si $`D`$ fuera finito, su centroide $`c=|D|^{-1}\sum_{z\in D}z`$ sería fijo por cada reflexión, dado que cada $`S_i`$ permuta $`D`$. Por tanto $`c\in\bigcap_iH_i`$. Esto exigiría $`v_i\cdot c=-1`$ para cada $`i`$; al sumar se obtiene $`0=-4`$, contradicción. $`\square`$

El corolario 1 descarta, ya con dos espejos, una identificación inyectiva de los operadores físicos de caras con las cuatro involuciones conmutativas. La proposición 4 descarta una órbita física finita estable, en particular una de 16 puntos. La realización disponible es entonces **no inyectiva**: cada uno de los 16 estados reúne una clase de configuraciones físicas. La sección 7 la construye.

### 6.1. Dimensión euclidiana mínima de cuatro cambios fieles

**Proposición 5.** Una acción fiel de $`(\mathbb Z/2\mathbb Z)^4`$ mediante isometrías de $`\mathbb R^d`$ exige $`d\geq4`$. En $`\mathbb R^4`$ la cota se alcanza mediante cambios independientes de signo.

**Demostración.** Una acción finita por isometrías tiene un punto fijo común: el promedio de la órbita de cualquier punto. Tras trasladarlo al origen, la acción se vuelve ortogonal. Sus elementos son involuciones ortogonales, por tanto matrices simétricas; como además conmutan, pueden diagonalizarse simultáneamente. La imagen queda contenida en el grupo de matrices diagonales con entradas $`\pm1`$, de orden $`2^d`$. La fidelidad exige $`2^4\leq2^d`$. Para $`d=4`$, los cambios individuales de signo realizan el grupo. $`\square`$

Esta proposición se refiere a **acciones isométricas fieles**. Un espacio físico tridimensional sostiene los 16 estados como etiquetas de clases de configuraciones (sección 7); la cuarta dirección euclidiana es la condición de una acción fiel por isometrías.

## 7. Criterio exacto para un cociente de la órbita

Descartada la realización inyectiva, la pregunta precisa es: ¿pueden las configuraciones de una órbita física organizarse en 16 clases que se transformen como $`Q_4`$?

Sean $`W=\langle s_1,s_2,s_3,s_4\mid s_i^2=1\rangle`$, producto libre de cuatro grupos de orden dos, y $`\pi:W\to\operatorname{Isom}(\mathbb R^3)`$ la acción definida por $`\pi(s_i)=S_i`$. Sea $`z_0\in\mathbb R^3`$ y $`\mathcal O=W\cdot z_0`$ su órbita. Se define el homomorfismo de paridad por generadores

```math
\psi:W\longrightarrow\mathbb F_2^4,
\qquad \psi(s_i)=e_i.
```

**Teorema 5 (criterio necesario y suficiente).** Existe una aplicación $`F:\mathcal O\to\mathbb F_2^4`$ que cumple $`F(z_0)=0`$ y

```math
F(S_i z)=F(z)\oplus e_i\qquad(z\in\mathcal O,\quad 1\leq i\leq4)
```

si y solo si

```math
\operatorname{Stab}_W(z_0)\subseteq\ker\psi.
```

Cuando existe, $`F`$ es **sobreyectiva**: se realizan los 16 estados como etiquetas, aunque la órbita física sea infinita.

**Demostración.** La ecuación de compatibilidad obliga a $`F(\pi(w)z_0)=\psi(w)`$ para cualquier palabra $`w`$. Si una palabra $`h`$ fija $`z_0`$, debe cumplirse $`0=F(z_0)=F(\pi(h)z_0)=\psi(h)`$: necesidad. Inversamente, si todo estabilizador tiene paridad nula, la regla

```math
F(\pi(w)z_0):=\psi(w)
```

está bien definida: si $`\pi(w)z_0=\pi(w')z_0`$, entonces $`w'^{-1}w`$ pertenece al estabilizador y $`\psi(w)=\psi(w')`$. La regla satisface las cuatro ecuaciones de compatibilidad. Como $`\psi`$ es sobreyectiva y cada palabra actúa sobre $`z_0`$, la imagen de $`F`$ es toda $`\mathbb F_2^4`$. $`\square`$

El criterio convierte la realización en un examen de relaciones entre palabras de reflexión: una palabra que fije la configuración inicial con $`\psi(w)\ne0`$ la impide; si todas las palabras estabilizadoras tienen paridad nula, el teorema la construye. Una función no inyectiva conserva los 16 estados binarios y reúne infinitas configuraciones físicas en cada clase. La exactitud se mide por las consultas que la representación conserva.

### 7.1. Los cuatro espejos del tetraedro

Las reflexiones de la sección 5 se escriben con matrices enteras:

```math
N_i=3I-2\,v_iv_i^{\mathsf T},\qquad S_i(z)=\frac{N_iz-2v_i}{3}.
```

Módulo 3 se cumple $`N_i\equiv v_iv_i^{\mathsf T}`$. Una palabra $`w=s_{i_1}s_{i_2}\cdots s_{i_n}`$ es **reducida** cuando dos letras consecutivas son siempre distintas; cada elemento de $`W`$ distinto de la identidad se escribe de manera única como palabra reducida no vacía. Su acción es $`\pi(w)=S_{i_1}\circ\cdots\circ S_{i_n}`$, y $`c`$ denota el centroide del tetraedro, que es el origen.

**Lema 1 (huella módulo 3).** Sea $`w=s_{i_1}\cdots s_{i_n}`$ reducida, con $`n\geq1`$, y sea $`L(w)`$ la parte lineal de $`\pi(w)`$. Entonces $`3^nL(w)`$ y $`3^n\pi(w)(c)`$ tienen coordenadas enteras y

```math
3^nL(w)\equiv(-1)^{n-1}\,v_{i_1}v_{i_n}^{\mathsf T},
\qquad
3^n\pi(w)(c)\equiv\pm\,v_{i_1}\pmod 3 .
```

Ambos lados derechos tienen todas sus entradas iguales a $`\pm1`$; en particular, son distintos de cero módulo 3.

**Demostración.** La parte lineal es $`L(w)=3^{-n}N_{i_1}\cdots N_{i_n}`$ y, como dos letras consecutivas son distintas y $`v_i\cdot v_j=-1`$ para $`i\neq j`$,

```math
N_{i_1}\cdots N_{i_n}\equiv v_{i_1}\,(v_{i_1}\cdot v_{i_2})\cdots(v_{i_{n-1}}\cdot v_{i_n})\,v_{i_n}^{\mathsf T}=(-1)^{n-1}\,v_{i_1}v_{i_n}^{\mathsf T}\pmod 3 .
```

Para la traslación, sea $`\tau(w)=3^n\pi(w)(c)`$. Se tiene $`\tau(s_i)=-2v_i\equiv v_i`$ y, si $`s_jw`$ es reducida,

```math
\tau(s_jw)=N_j\,\tau(w)-2\cdot3^{n}v_j\equiv v_j\,\bigl(v_j\cdot\tau(w)\bigr)\pmod 3 .
```

Si $`\tau(w)\equiv\varepsilon v_{i_1}`$ con $`\varepsilon=\pm1`$ y $`j\neq i_1`$, resulta $`\tau(s_jw)\equiv-\varepsilon v_j`$. La inducción sobre $`n`$ completa la prueba. $`\square`$

**Teorema 6 (las 16 clases de la caja de espejos).**

1. La acción $`\pi`$ es fiel: las cuatro reflexiones generan un grupo isomorfo a $`W`$, producto libre de cuatro grupos de orden dos.
2. El estabilizador del centroide es trivial. Las palabras reducidas están en biyección con los puntos de su órbita; a longitud $`n`$ corresponden $`4\cdot3^{n-1}`$ puntos.
3. La regla $`F(\pi(w)(c))=\psi(w)`$ define una aplicación sobreyectiva sobre $`\mathbb F_2^4`$ que cumple $`F(S_iz)=F(z)\oplus e_i`$. Cada una de las 16 clases contiene infinitos puntos.
4. Lo mismo vale para todo punto inicial $`z_0`$ fuera de la unión de los conjuntos fijos $`\operatorname{Fix}\pi(w)`$ con $`\psi(w)\ne0`$. Esa unión es numerable, está formada por planos, rectas y puntos, y tiene medida nula. Sobre cada plano $`H_i`$ la etiqueta no existe: $`S_i`$ fija el punto y $`\psi(s_i)=e_i\ne0`$.

**Demostración.** (1) Si $`\pi(w)`$ fuera la identidad para una palabra reducida no vacía, se tendría $`3^nL(w)=3^nI\equiv0\pmod 3`$, contra el lema 1. (2) Si $`\pi(w)(c)=c=0`$, entonces $`3^n\pi(w)(c)=0`$, contra el lema. Si dos palabras $`w,w'`$ llevan $`c`$ al mismo punto, la forma reducida de $`w'^{-1}w`$ fija $`c`$ y es, por tanto, vacía. Hay $`4\cdot3^{n-1}`$ palabras reducidas de longitud $`n`$. (3) Es el teorema 5 con $`\operatorname{Stab}_W(c)=\lbrace 1\rbrace`$. Si $`a\neq b`$ y $`a`$ difiere de la última letra de $`w`$, las palabras $`w(s_as_b)^{2k}`$, $`k\geq0`$, son reducidas, distintas y de igual paridad que $`w`$; por (2) dan infinitos puntos de la clase de $`w`$. (4) Por (1), para cada $`w\ne1`$ la isometría $`\pi(w)`$ es distinta de la identidad y su conjunto fijo es un subespacio afín propio; $`W`$ es numerable. Fuera de la unión indicada, $`\operatorname{Stab}_W(z_0)\subseteq\ker\psi`$ y se aplica el teorema 5. $`\square`$

Para puntos iniciales enteros, la misma huella da un criterio explícito: si $`z_0\in\mathbb Z^3`$ cumple $`v_i\cdot z_0\not\equiv-1\pmod 3`$ para los cuatro índices, entonces $`3^n\pi(w)(z_0)\not\equiv0\pmod 3`$ para toda palabra reducida no vacía, y el estabilizador de $`z_0`$ es trivial.

**Lectura.** La órbita física se abre sin regresar: ninguna secuencia de reflexiones devuelve el centroide a una configuración anterior, y su grafo es el árbol en que cada configuración tiene cuatro vecinas. La etiqueta $`F`$ registra cuántas veces, módulo dos, la configuración atravesó cada espejo; el orden de las reflexiones queda guardado en la posición física. En términos algebraicos, $`\psi`$ es la abelianización de $`W`$ y $`Q_4`$ es el cociente del árbol por ella: las 16 clases son lo que la órbita conserva cuando las reflexiones se comparan sin orden.

**Condición sobre los ángulos.** La etiqueta depende de las relaciones entre espejos. En un punto genérico existe si y solo si toda relación $`\pi(w)=I`$ tiene paridad nula en cada espejo. Dos espejos a $`90^\circ`$ cumplen $`(s_is_j)^2=1`$, de paridad nula, y la permiten; dos espejos a $`60^\circ`$ cumplen $`(s_is_j)^3=1`$, con $`\psi=e_i\oplus e_j`$, y la impiden en todo punto. Los cuatro espejos del tetraedro regular no tienen relaciones, y la condición se cumple.

**Enlace con la literatura.** El punto 1 del teorema 6 es el resultado con que Świerczkowski respondió a Steinhaus: una cadena de tetraedros regulares unidos cara con cara nunca se cierra [2, 3]. Dekker estudió reflexiones euclidianas que generan productos libres [4], y Stewart obtuvo el mismo producto libre con matrices sobre $`\mathbb Z/3\mathbb Z`$ [5]; el lema 1 es una forma directa de ese argumento. Aquí ese resultado se lee como cociente: las cadenas que no se cierran se reparten en 16 clases que se transforman como $`Q_4`$.

## 8. Interpretación dentro del programa

La secuencia examinada es

```math
\text{distinción}\ \longrightarrow\ \text{comparación}\ \longrightarrow\
\text{firma}\ \longrightarrow\ \text{clases}\ \longrightarrow\
\text{nueva consulta}.
```

El tetraedro marca, bajo independencia afín, un cierre volumétrico mínimo. El teseracto aparece, bajo independencia de cuatro cambios binarios, como el espacio de configuraciones. La 16-celda expresa la separación de ese espacio por paridad. Las comparaciones por pares producen una superposición observacional: los complementos globales son diferentes estados con una misma firma. Las reflexiones físicas producen una órbita abierta, sin retornos, cuyo cociente por la paridad de cada espejo recupera los 16 estados.

La palabra *dimensión* conserva aquí dos usos delimitados. Una **dimensión geométrica** requiere independencia espacial de coordenadas. Una **dimensión de comparación** es una distinción adicional que las observaciones anteriores dejan sin recuperar. Los teoremas indican cuándo aparece información suplementaria; atribuir esa información a una dirección física es la cuestión abierta de la tabla de estado.

La relación con la regla de herencia del programa se encuentra en las clases observacionales: una representación posterior debe conservar las consultas que sus operaciones necesitan resolver. El conteo de firmas cuantifica las diferencias posibles de esta realización; su uso en problemas generales de cálculo corresponde a la rama computacional del programa.

## 9. Conclusiones y obligación reproducible

Los resultados establecen, con hipótesis explícitas, la correspondencia entre cuatro referencias binarias, $`Q_4`$, dos 16-celdas y ocho firmas de comparaciones. Distinguen además la pérdida de una elección global de complemento de la partición par/impar. La extensión a $`n`$ referencias identifica una diferencia exacta entre $`n`$ par e impar, relevante para examinar el paso de cuatro a cinco.

El laboratorio de cuatro espejos aporta dos obstrucciones y una construcción. Sus planos fijos generan 15 regiones abiertas; sus reflexiones no conmutan y toda órbita estable es infinita, de modo que una identificación inyectiva literal con los 16 estados queda descartada. El teorema 6 construye la identificación por cociente: la órbita del centroide, infinita y sin retornos, se reparte en 16 clases etiquetadas por la paridad de reflexiones en cada espejo, con las cuatro transiciones binarias de $`Q_4`$. La cuestión abierta es geométrica: si esas 16 clases sostienen una cuarta dirección física.

El archivo `verificar.py` acompaña esta publicación y comprueba con aritmética exacta las cuentas binarias, la imagen de las firmas, las dos 16-celdas con sus 16 celdas, los 15 patrones de regiones, la coincidencia de $`S_iS_j`$ y $`S_jS_i`$ solo sobre la arista común, y el lema 1 en todas las palabras reducidas hasta longitud 10, junto con la ecuación $`F(S_iz)=F(z)\oplus e_i`$ en esa porción de la órbita del centroide. Las proposiciones 4 y 5 y los teoremas 5 y 6 se demuestran en el texto.

## Referencias y procedencia

1. **Hinton, Charles Howard.** *A New Era of Thought*. Londres: Swan Sonnenschein & Co., 1888. En particular, parte II y apéndice H, *Sections of Cube and Tessaract*. **Nota de autoría:** el prefacio identifica a Alicia Boole y H. John Falk como redactores del apéndice H. Texto íntegro: https://www.gutenberg.org/files/60607/60607-h/60607-h.htm
2. **Świerczkowski, Stanisław.** «On a free group of rotations of the Euclidean space». *Indagationes Mathematicae* 20 (1958), 376–378.
3. **Świerczkowski, Stanisław.** «On chains of regular tetrahedra». *Colloquium Mathematicum* 7 (1959), 9–10.
4. **Dekker, T. J.** «On reflections in Euclidean spaces generating free products». *Nieuw Archief voor Wiskunde* (3) 7 (1959), 57–60.
5. **Stewart, Ian.** «Tetrahedral chains and a curious semigroup». *Extracta Mathematicae* 34 (1) (2019), 99–122. https://doi.org/10.17398/2605-5686.34.1.99
6. **Endless Monkey Project.** *De la indefinición al cierre de la información*, manuscrito integrado, 12 de noviembre de 2026. Antecedente interno: definiciones, firmas, cierre, información suplementaria y herencia.
7. **Endless Monkey Project.** *Auditoría de la regla de reflexión y del orden de aparición*, 21 de octubre de 2026. Antecedente interno: distinción entre reflexión local, sincronizada y aritmética.
8. **Endless Monkey Project.** [*Imagen Total 4.0*](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_imagen_total_4_0/Imagen_Total_4_0.md), 10 de noviembre de 2026. Contexto y trazabilidad de las construcciones.
9. **Endless Monkey Project.** [*La economía del cálculo desde las relaciones entre referencias*](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-08_economia_del_calculo/informe.md), 8 de noviembre de 2026. Herencia y conteos por clases observacionales.
10. **Endless Monkey Project.** [*¿Qué cálculo deja de hacerse? La caja de espejos: incertidumbre, reconocimiento y cierre*](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_que_calculo_deja_de_hacerse/PAPER_ES.md), 10 de noviembre de 2026. Laboratorio de reconocimiento y economía.

---

**Endless Monkey Project**  
*Relational Geometry Program*

**Versión:** 1.1 · 13 de noviembre de 2026  
**Estado editorial:** publicación técnica para verificación independiente. Resultados exactos, condiciones de realización y cuestión abierta identificados por separado.
