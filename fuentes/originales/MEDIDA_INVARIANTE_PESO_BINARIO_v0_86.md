# De la incertidumbre máxima al peso \(2^{-n}\)
## Medida invariante, completitud cuadrática y cierre del puente de peso
### Formalización v0.86

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** formalización matemática interna con un principio explícito de homogeneidad pre-referencia.  
**No implica validación física ni selección experimental de un sector.**

---

# 0. Objetivo

La formulación anterior obtuvo:

\[
J^2=-I,\qquad J^4=I,
\]

y distinguió dos cierres canónicos:

\[
C_4
\]

y

\[
C_4/\{\pm I\}\simeq C_2.
\]

También mostró que un libro completo de \(n\) roles relacionales tiene \(2^n\) canales, de modo que:

\[
n=2\Rightarrow4=1+3,
\qquad
n=4\Rightarrow16=1+15.
\]

Quedaba abierto el puente de peso:

\[
\boxed{
\text{conteo de canales}
\stackrel{?}{\longrightarrow}
\text{peso cuadrático}.
}
\]

Aquí se prueba que el peso uniforme no necesita postularse canal por canal. Se sigue de una simetría más primitiva:

\[
\boxed{
\text{antes de seleccionar una referencia,
ningún canal relacional está privilegiado}.
}
\]

---

# 1. Espacio de roles

Sea

\[
F_n=\operatorname{span}_{\mathbb R}\{e_1,\dots,e_n\}
\]

un espacio formal de \(n\) roles relacionales distinguibles.

Estos roles no son necesariamente dimensiones espaciales físicas.

Son generadores de información relacional.

---

# 2. Completitud cuadrática: álgebra de Clifford

El modelo posee una estructura métrica/cuadrática.

La completitud algebraica natural de un espacio cuadrático \((F_n,Q)\) es su álgebra de Clifford:

\[
\boxed{
\mathrm{Cl}(F_n,Q).
}
\]

Por la propiedad universal de Clifford:

\[
v^2=Q(v)\,1
\]

para todo \(v\in F_n\).

Como espacio vectorial:

\[
\mathrm{Cl}(F_n,Q)
\simeq
\Lambda^\bullet F_n.
\]

Por tanto:

\[
\boxed{
D_n:=\dim\mathrm{Cl}(F_n,Q)=2^n.
}
\]

Una base está dada por las hojas:

\[
e_I=e_{i_1}\cdots e_{i_k},
\qquad
I\subseteq\{1,\dots,n\}.
\]

Así cada subconjunto \(I\) indexa un canal de la completitud cuadrática.

---

# 3. Sector escalar y sector relacional

La componente de grado cero es:

\[
\mathrm{Cl}^0_{\rm scalar}
=
\operatorname{span}\{1\}.
\]

Tiene dimensión:

\[
\boxed{1}.
\]

Su complemento vectorial formado por todos los grados positivos tiene dimensión:

\[
\boxed{
2^n-1.
}
\]

Luego:

\[
\boxed{
2^n=1+(2^n-1).
}
\]

Esta descomposición es puramente algebraica.

---

# 4. Estado pre-referencia

Sea

\[
\mathcal H_n
\]

el espacio euclidiano de coeficientes de la base de hojas \(\{e_I\}\), de dimensión \(D_n=2^n\).

La incertidumbre pre-referencia no se representa como desconocimiento subjetivo, sino como ausencia estructural de un discriminante que privilegie un canal.

Introducimos:

## Principio H — Homogeneidad pre-referencia

Antes de que una comparación seleccione una referencia, la descripción no puede asignar pesos diferentes a dos canales que la arquitectura todavía no distingue.

Formalmente, el estado de peso \(\rho\) debe ser invariante bajo todas las permutaciones y cambios de signo de la base de canales:

\[
U\rho U^\ast=\rho
\]

para todo \(U\) del grupo de permutaciones signadas de la base.

Este principio no dice que todos los estados físicos sean uniformes.

Se aplica exclusivamente al estado **anterior a la introducción de información discriminante adicional**.

---

# 5. Teorema de unicidad de la medida pre-referencia

## Teorema 5.1

Sea \(\rho\) un operador positivo sobre \(\mathcal H_n\) con:

\[
\operatorname{Tr}\rho=1.
\]

Si:

\[
U\rho U^\ast=\rho
\]

para toda permutación signada de la base de canales, entonces:

\[
\boxed{
\rho_0=\frac{1}{D_n}I
=
2^{-n}I.
}
\]

## Demostración

Las reflexiones de signo independientes:

\[
e_I\mapsto -e_I
\]

obligan a anular toda entrada fuera de la diagonal de \(\rho\).

Las permutaciones arbitrarias de los canales obligan a que todas las entradas diagonales sean iguales.

Por tanto:

\[
\rho=cI.
\]

Como:

\[
\operatorname{Tr}\rho=cD_n=1,
\]

se obtiene:

\[
c=\frac1{D_n}=2^{-n}.
\]

\[
\blacksquare
\]

---

# 6. Interpretación como medida uniforme

Equivalente y más elementalmente, los canales pueden identificarse con:

\[
G_n=(\mathbb Z_2)^n.
\]

La operación es XOR/suma módulo 2.

Si una medida normalizada \(\mu\) satisface:

\[
\mu(A\oplus g)=\mu(A)
\]

para todo desplazamiento \(g\in G_n\), la acción de \(G_n\) es transitiva y:

\[
\boxed{
\mu(\{x\})=2^{-n}
}
\]

para todo canal \(x\).

Ésta es la medida de Haar normalizada del grupo finito \(G_n\).

No hace falta postular pesos iguales individualmente: la homogeneidad los fuerza.

---

# 7. El rol de la proyección

Antes de la proyección:

\[
\rho_0=\frac{I}{2^n}.
\]

La arquitectura no ha seleccionado un canal como referencia.

La proyección introduce una referencia.

Sea:

\[
P_0
\]

el proyector sobre el único canal escalar/no diferenciado:

\[
\operatorname{span}\{1\}.
\]

Entonces:

\[
\operatorname{rank}P_0=1.
\]

El complemento:

\[
P_{\rm rel}=I-P_0
\]

tiene rango:

\[
2^n-1.
\]

---

# 8. Teorema del peso cuadrático

Definimos el peso de un sector \(S\) mediante:

\[
w(S)
=
\operatorname{Tr}(\rho_0P_S).
\]

Entonces:

\[
w(S)
=
\frac{\operatorname{rank}P_S}{2^n}.
\]

En particular:

\[
\boxed{
r_V
:=
w(P_0)
=
\frac1{2^n}
=
2^{-n},
}
\]

y:

\[
\boxed{
r_m
:=
w(P_{\rm rel})
=
\frac{2^n-1}{2^n}
=
1-2^{-n}.
}
\]

Por tanto:

\[
\boxed{
r_V:r_m
=
1:(2^n-1).
}
\]

## Resultado

El antiguo "Puente W" queda derivado **dado el Principio H y la completitud cuadrática**.

No se necesita un postulado independiente de equiponderación.

---

# 9. Forma de norma

Una realización equivalente usa un vector purificado de amplitudes iguales:

\[
|\Omega_n\rangle
=
2^{-n/2}
\sum_{I}|I\rangle.
\]

Entonces:

\[
\|\Omega_n\|=1.
\]

Para cualquier canal unitario \(|I_0\rangle\):

\[
\boxed{
\|P_{I_0}\Omega_n\|^2
=
2^{-n}.
}
\]

Y para su complemento:

\[
\boxed{
\|(I-P_{I_0})\Omega_n\|^2
=
1-2^{-n}.
}
\]

Así la aparición de \(2^{-n}\) como **peso cuadrático** es exactamente una consecuencia de amplitudes iguales impuestas por la homogeneidad pre-referencia.

---

# 10. Incertidumbre como bit

El estado uniforme tiene entropía:

\[
S(\rho_0)
=
-\operatorname{Tr}\rho_0\log_2\rho_0.
\]

Como hay \(2^n\) autovalores iguales a \(2^{-n}\):

\[
\boxed{
S(\rho_0)=n\text{ bits}.
}
\]

Por tanto:

\[
\boxed{
n
=
\text{cantidad de incertidumbre binaria
de la completitud relacional pre-referencia}.
}
\]

Esto da un significado informacional preciso a la profundidad \(n\).

No significa que una órbita de cuatro fases contenga cuatro bits.

Significa que la completitud cuadrática generada por \(n\) roles independientes tiene \(2^n\) canales y, cuando ninguno está distinguido, su incertidumbre máxima es \(n\) bits.

---

# 11. Conexión con el radio de resolución

En una formalización anterior se definió:

\[
R_{\rm res}=2^{-U}
\]

para una incertidumbre \(U\) medida en bits.

Aquí:

\[
U=n.
\]

Luego:

\[
\boxed{
R_{\rm res}
=
2^{-n}.
}
\]

Pero también acabamos de derivar:

\[
r_V=2^{-n}.
\]

Por tanto existe una identificación interna natural:

\[
\boxed{
r_V
=
R_{\rm res}
}
\]

si ambos objetos se interpretan como el peso normalizado del único canal de referencia frente al libro completo de incertidumbre.

Ésta es una identificación interna del programa.

No convierte automáticamente a \(R_{\rm res}\) en una longitud física.

---

# 12. Frecuencias y radios

Si el peso cuadrático se representa mediante:

\[
r_V
=
\frac{\omega_V^2}{\omega^2},
\]

entonces:

\[
\frac{\omega_V}{\omega}
=
2^{-n/2}.
\]

Por tanto:

\[
\boxed{
\omega_V
=
2^{-n/2}\omega.
}
\]

Y si se introduce la escala operacional:

\[
R_V=\frac{c}{\omega_V},
\qquad
R_U=\frac{c}{\omega},
\]

entonces:

\[
\boxed{
\frac{R_V}{R_U}
=
2^{n/2}.
}
\]

Así la cadena histórica:

\[
r_V=2^{-n}
\Rightarrow
R_V=2^{n/2}R_U
\]

queda recuperada.

La identificación de \(R_U\) con una longitud física concreta permanece como puente operacional.

---

# 13. Casos \(C_2\) y \(C_4\)

## Cierre proyectivizado \(C_2\)

\[
n=2.
\]

Entonces:

\[
D=2^2=4,
\]

\[
r_V=\frac14,
\qquad
r_m=\frac34,
\]

y:

\[
\boxed{
r_V:r_m=1:3.
}
\]

Además:

\[
S=2\text{ bits}.
\]

## Cierre orientado \(C_4\)

\[
n=4.
\]

Entonces:

\[
D=2^4=16,
\]

\[
r_V=\frac1{16},
\qquad
r_m=\frac{15}{16},
\]

y:

\[
\boxed{
r_V:r_m=1:15.
}
\]

Además:

\[
S=4\text{ bits}.
\]

---

# 14. Corrección del signo de orientación

La formalización v0.84 fijó:

\[
(A\times R)\times R
=
-\|R\|^2A.
\]

Por tanto el antiguo signo:

\[
\sigma\in\{\pm1\}
\]

de la doble proyección ya no es un bit libre en la realización métrica positiva.

La ambigüedad binaria restante es:

\[
\boxed{
J
\quad\leftrightarrow\quad
-J,
}
\]

es decir, el sentido del ciclo de fase.

Ambos satisfacen:

\[
(\pm J)^2=-I.
\]

Por tanto debe distinguirse:

- **signo de la doble proyección:** fijado en \(-1\);
- **orientación del generador:** \(s=\pm1\), todavía binaria.

---

# 15. Por qué sólo la simetría de permutación no basta

Un punto adversarial importante:

Si sólo exigimos invariancia bajo permutaciones de los \(n\) generadores originales, las configuraciones se agrupan por peso de Hamming:

\[
0,1,\dots,n.
\]

Nada obliga a asignar el mismo peso a capas de Hamming diferentes.

Por tanto:

\[
\boxed{
S_n\text{-simetría sola}
\not\Rightarrow
r_V=2^{-n}.
}
\]

La derivación necesita una homogeneidad más fuerte del libro pre-referencia: invariancia bajo cambios de origen/XOR o, equivalentemente, ausencia de cualquier discriminante entre canales completos.

Ésta es una condición falsable y debe mantenerse explícita.

---

# 16. Lectura por máxima entropía

La misma conclusión se obtiene mediante economía informacional.

Entre todas las distribuciones sobre \(2^n\) canales, la que no introduce ninguna distinción no acreditada es:

\[
p_I=2^{-n}.
\]

Es la única que maximiza:

\[
H(p)
=
-\sum_Ip_I\log_2p_I,
\]

con:

\[
H_{\max}=n.
\]

Cualquier distribución no uniforme satisface:

\[
H(p)<n
\]

y codifica una preferencia adicional.

Dentro del programa, esa preferencia tendría que ser acreditada por nueva información relacional.

Así, "máxima incertidumbre" no significa ausencia de estructura.

Significa:

\[
\boxed{
\text{ninguna diferencia adicional ha sido acreditada
entre los canales disponibles}.
}
\]

---

# 17. Cadena consolidada

La ruta queda:

\[
\boxed{
\begin{aligned}
J^2=-I,\ J^4=I
&\Rightarrow
\text{roles de cierre}\\
&\Rightarrow
F_n\\
&\Rightarrow
\mathrm{Cl}(F_n,Q)\\
&\Rightarrow
D=2^n\\
&\Rightarrow
\text{homogeneidad pre-referencia}\\
&\Rightarrow
\rho_0=\frac{I}{2^n}\\
&\Rightarrow
r_V=2^{-n}\\
&\Rightarrow
r_m=1-2^{-n}\\
&\Rightarrow
r_V:r_m=1:(2^n-1).
\end{aligned}
}
\]

El paso que antes era un postulado numérico ha sido sustituido por una condición estructural más profunda:

\[
\boxed{
\text{no hay canal preferido antes de que exista
información que lo distinga}.
}
\]

---

# 18. Qué queda abierto

La matemática del peso está cerrada **condicionada al Principio H**.

Permanecen abiertos:

1. justificar desde la ontología, o adoptar explícitamente, que la homogeneidad pre-referencia actúa sobre el libro completo de canales;
2. demostrar qué sistemas físicos realizan \(C_2\) y cuáles realizan \(C_4\);
3. justificar la identificación física del sector escalar con el modo \(V\);
4. conectar el radio operacional con observables sin calibración circular;
5. extender o refutar la identificación del entero \(n\) a cierres colectivos de otros niveles;
6. estudiar si la misma arquitectura produce una regla computacional relevante para P vs NP.

---

# 19. Falsadores directos

La derivación deja de aplicar si:

- antes de la proyección existe una diferencia acreditada entre canales;
- el libro relevante no es la completitud cuadrática \(\mathrm{Cl}(F_n,Q)\);
- algunos canales están prohibidos estructuralmente antes de seleccionar referencia;
- el observable relevante no usa la norma cuadrática;
- el sector "visible" no es un canal unidimensional sino un subespacio de rango mayor.

En el último caso:

\[
r_V=\frac{k}{2^n}
\]

si el sector visible tiene rango \(k\).

Así, la predicción \(2^{-n}\) es falsable incluso dentro del formalismo.
