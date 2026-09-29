# Del cierre de cuatro a la duplicación 4→8
## Teorema de órbitas, quinta imagen y nueva referencia — v0.83

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** resultado matemático condicionado a las hipótesis declaradas. No implica validación física ni solución de P vs NP.

---

# 0. Punto de partida

El programa dispone de una realización local con operador \(J\) tal que

\[
J^2=-I.
\]

Por tanto,

\[
J^4=I.
\]

La órbita algebraica de un estado \(x\) es

\[
\mathcal O(x)=\{x,Jx,J^2x,J^3x\}.
\]

Si no existen periodos menores,

\[
Jx\neq x,\qquad J^2x\neq x,\qquad J^3x\neq x,
\]

entonces

\[
|\mathcal O(x)|=4.
\]

---

# 1. Hipótesis de cierre orbital

Sea \(X\) un conjunto de imágenes admisibles y sea

\[
J:X\to X
\]

una biyección que satisface

\[
J^4=I.
\]

Adoptamos la condición de acción libre:

\[
\boxed{
J^k x\neq x
\quad
\forall x\in X,\quad k=1,2,3.
}
\]

Esta condición expresa que ningún estado cierra antes de completar el ciclo de cuatro.

**[HIPÓTESIS H1]** Una identidad local cerrada debe contener la órbita completa generada por \(J\).

---

# 2. Teorema de cardinalidad orbital

## Teorema 1

Bajo las hipótesis anteriores, cada órbita de \(J\) contiene exactamente cuatro elementos y \(X\) se descompone en una unión disjunta de órbitas de tamaño cuatro:

\[
\boxed{
X=\bigsqcup_{\alpha\in X/\langle J\rangle}\mathcal O_\alpha.
}
\]

Por tanto:

\[
\boxed{
|X|=4\,|X/\langle J\rangle|.
}
\]

## Demostración

Como \(J^4=I\), el tamaño de toda órbita divide a \(4\).

Los divisores posibles son:

\[
1,\ 2,\ 4.
\]

La condición de acción libre excluye periodos \(1\) y \(2\). Luego toda órbita tiene tamaño \(4\).

Las órbitas de una acción de grupo forman una partición de \(X\). Por tanto \(X\) es unión disjunta de bloques de cuatro elementos, y su cardinalidad es múltiplo de cuatro.

\[
\blacksquare
\]

---

# 3. Teorema de la quinta imagen

Sea una identidad cerrada inicial

\[
X_1=\mathcal O(x),
\qquad |X_1|=4.
\]

Introduzcamos una nueva imagen

\[
y\notin X_1.
\]

Entonces \(y\) no puede pertenecer a la órbita anterior.

Por H1, conservar \(y\) como identidad cerrada exige conservar también:

\[
Jy,\quad J^2y,\quad J^3y.
\]

Por tanto la extensión cerrada mínima es:

\[
\boxed{
X_2
=
\mathcal O(x)\sqcup\mathcal O(y).
}
\]

Y:

\[
\boxed{
|X_2|=8.
}
\]

## Corolario

La quinta imagen no es el cierre completo nuevo.

Es el **testigo de que existe una segunda órbita**.

Así:

\[
\boxed{
4+1
\quad\text{no cierra como }5;
\qquad
4+1
\quad\Longrightarrow\quad
4+4=8
}
\]

si se exige cierre bajo la misma acción \(J\).

---

# 4. La nueva referencia como índice de órbita

Dentro de una órbita, un estado queda caracterizado por una fase discreta:

\[
k\in\mathbb Z_4.
\]

Con dos órbitas hace falta además saber a cuál pertenece el estado:

\[
\alpha\in\{0,1\}.
\]

La descripción factoriza como:

\[
\boxed{
x\longleftrightarrow(\alpha,k).
}
\]

donde:

\[
k\in\mathbb Z_4,
\qquad
\alpha\in X/\langle J\rangle.
\]

Para dos órbitas:

\[
|\alpha|=2.
\]

Luego la nueva información necesaria para distinguirlas es:

\[
\boxed{
I_{\rm orb}=\log_2 2=1\text{ bit}.
}
\]

Ésta es una realización matemática precisa de:

> la quinta imagen introduce una diferencia que el marco anterior no puede describir; hace falta una referencia adicional.

La referencia adicional no distingue posiciones dentro del ciclo original.

Distingue **qué ciclo** contiene la imagen.

---

# 5. Corrección importante: cuatro estados no son cuatro bits

Una órbita de cuatro estados contiene:

\[
\boxed{
\log_2 4=2\text{ bits}
}
\]

de capacidad de identificación, no cuatro bits independientes.

Por tanto:

\[
\boxed{
J^4=I
\not\Rightarrow
4\text{ bits}
}
\]

y tampoco:

\[
\boxed{
J^4=I
\not\Rightarrow
2^4=16.
}
\]

La antigua cadena

\[
J^4=I\Rightarrow 16\Rightarrow15
\]

no está derivada.

Para obtener \(16\) hace falta una estructura recursiva adicional.

---

# 6. Cómo puede aparecer 16 sin introducirlo a mano

Supongamos que las órbitas de nivel inferior se convierten en nuevas unidades:

\[
\mathcal O_1,\mathcal O_2,\ldots
\]

y que sobre el conjunto de esas unidades actúa un operador de nivel superior \(J_1\) con:

\[
J_1^4=I.
\]

Entonces un cierre completo en el nivel superior requiere cuatro órbitas inferiores:

\[
\boxed{
4\text{ órbitas}
\times
4\text{ estados por órbita}
=
16\text{ estados}.
}
\]

Es decir:

\[
\boxed{
4
\to
8
\to
12
\to
16
}
\]

a medida que se acreditan nuevas órbitas dentro del mismo nivel,

pero el **cierre meta-orbital** se alcanza cuando existen cuatro unidades orbitales:

\[
\boxed{
4\times4=16.
}
\]

Esto proporciona una ruta no circular hacia \(16\), condicionada a demostrar que el operador de cierre se hereda entre escalas.

---

# 7. Recursión de escala

Denotemos por:

\[
X^{(0)}
\]

los estados de nivel básico.

El cociente por las órbitas es:

\[
X^{(1)}
=
X^{(0)}/\langle J_0\rangle.
\]

Cada elemento de \(X^{(1)}\) representa una cápsula cerrada de nivel inferior.

Si existe una acción:

\[
J_1:X^{(1)}\to X^{(1)},
\qquad
J_1^4=I,
\]

podemos volver a cocientar:

\[
X^{(2)}
=
X^{(1)}/\langle J_1\rangle.
\]

En general:

\[
\boxed{
X^{(k+1)}
=
X^{(k)}/\langle J_k\rangle.
}
\]

Esto formaliza la idea:

\[
\boxed{
\text{lo que se cierra en una escala}
\to
\text{unidad en la siguiente}.
}
\]

---

# 8. Dimensión como información de cociente

La nueva referencia no necesita interpretarse inicialmente como eje geométrico.

Matemáticamente es la información necesaria para distinguir clases del cociente:

\[
\boxed{
X/\langle J\rangle.
}
\]

Si existe una sola órbita:

\[
|X/\langle J\rangle|=1,
\]

no hace falta información de órbita.

Cuando aparece la quinta imagen y fuerza una segunda órbita:

\[
|X/\langle J\rangle|=2.
\]

Surge una nueva distinción:

\[
\boxed{
\alpha\in\{0,1\}.
}
\]

**[CORRESPONDENCIA PROGRAMÁTICA]** Si el programa define una dimensión como el espacio necesario para conservar información que no cabía en el marco anterior, entonces el índice de órbita es un candidato matemático a esa nueva dimensión informacional.

No se afirma todavía que sea una dimensión espacial física.

---

# 9. Relación con el radio de resolución

Sea:

\[
\mathfrak M
\]

la familia de cierres todavía compatibles.

Definimos:

\[
U_M=\log_2|\mathfrak M|,
\qquad
R_{\rm res}=2^{-U_M}.
\]

La nueva estructura orbital permite representar la diferencia de dos niveles:

1. fase interna:
   \[
   k\in\mathbb Z_4;
   \]

2. identidad orbital:
   \[
   \alpha\in X/\langle J\rangle.
   \]

Una comparación puede resolver primero \(\alpha\) sin resolver necesariamente \(k\), o viceversa.

Esto separa:

\[
\boxed{
\text{qué módulo}
}
\]

de:

\[
\boxed{
\text{qué estado dentro del módulo}.
}
\]

---

# 10. Puente con las octavas

El resultado:

\[
4\to8
\]

no se introduce por numerología.

Surge de:

1. cierre local de orden cuatro;
2. aparición de una quinta imagen fuera de la órbita;
3. exigencia de cierre de esa nueva imagen bajo la misma acción.

Así, la quinta imagen genera una segunda estructura simétrica de cuatro estados.

Esto coincide estructuralmente con la intuición:

> al aparecer una identidad que no cabe, surgen dos estructuras simétricas y hace falta una referencia para distinguirlas.

La referencia es el índice:

\[
\alpha.
\]

El ocho es entonces:

\[
\boxed{
8=2\times4
}
\]

y no simplemente una potencia elegida externamente.

---

# 11. Implicación computacional

Supongamos que un espacio de estados admite una acción de simetría \(J\) de orden cuatro.

En vez de representar individualmente los estados, puede trabajarse con órbitas:

\[
X
\longrightarrow
X/\langle J\rangle.
\]

Si la acción es libre:

\[
|X/\langle J\rangle|
=
\frac{|X|}{4}.
\]

Esto produce una compresión exacta por un factor cuatro.

## Pero:

Una reducción por un factor constante no convierte por sí misma un problema exponencial en polinómico.

\[
\boxed{
2^n/4
=
2^{n-2}
}
\]

sigue siendo exponencial.

Para afectar P vs NP sería necesaria una **recursión de cocientes** donde estructuras cerradas puedan volver a tratarse como unidades y el número de niveles, el tamaño de las interfaces y el costo de reconocer las órbitas permanezcan polinómicos.

---

# 12. Teorema objetivo recursivo

Buscar condiciones bajo las cuales exista una jerarquía:

\[
X^{(0)}
\to
X^{(1)}
\to
\cdots
\to
X^{(d)}
\]

con:

\[
X^{(k+1)}
=
X^{(k)}/G_k,
\]

donde:

\[
|G_k|=4,
\]

y donde cada cociente pueda calcularse sin enumerar \(X^{(k)}\).

Para una aplicación a complejidad, deben probarse:

\[
d\le\operatorname{poly}(n),
\]

\[
\operatorname{size}(X^{(k)}_{\rm repr})
\le\operatorname{poly}(n),
\]

\[
T_{\rm quotient}(k)
\le\operatorname{poly}(n).
\]

Sólo entonces la recursión orbital tendría relevancia para P vs NP.

---

# 13. Falsadores

La ruta queda falsada en su forma fuerte si ocurre cualquiera de los siguientes:

1. el operador relevante tiene órbitas de tamaño variable no controlado;
2. una quinta imagen puede incorporarse al mismo cierre sin información adicional;
3. reconocer si dos estados pertenecen a la misma órbita es tan difícil como resolver el problema original;
4. las interfaces entre órbitas crecen exponencialmente;
5. el operador de cierre no se hereda de una escala a la siguiente;
6. la acción de orden cuatro aparece sólo por una elección de representación y no por la ontología.

---

# 14. Resultado actual

Lo que sí queda demostrado, bajo \(J^4=I\) y acción libre, es:

\[
\boxed{
\text{una identidad orbital cerrada contiene 4 imágenes}.
}
\]

Y:

\[
\boxed{
\text{una quinta imagen independiente}
\Rightarrow
\text{segunda órbita}
\Rightarrow
\text{mínimo cerrado total }8.
}
\]

Además:

\[
\boxed{
\text{la nueva información es el índice de órbita}.
}
\]

Éste es el puente matemático más limpio obtenido hasta ahora entre:

\[
\text{cuatro}
\to
\text{quinta diferencia}
\to
\text{nueva referencia}
\to
\text{ocho}.
\]

La equivalencia física y la recursión computacional permanecen abiertas.
