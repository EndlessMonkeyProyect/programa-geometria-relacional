# Del cierre de fase al cierre binario
## Cociente proyectivo, libro relacional booleano y origen estructural de 1:3 y 1:15
### Formalización v0.85

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** formalización matemática + puente informacional explícito.  
**No implica validación física ni identifica por sí sola los dos sectores con electrón/protón.**

---

# 0. Punto de partida acreditado

De la formalización v0.84:

\[
J^2=-I,
\qquad
J^4=I.
\]

Para \(A\neq0\),

\[
\mathcal O_4(A)
=
\{A,JA,-A,-JA\}
\]

es una órbita libre de cuatro fases.

Estas cuatro imágenes viven geométricamente en el plano real

\[
W_A=\operatorname{span}_{\mathbb R}\{A,JA\},
\qquad
\dim_{\mathbb R}W_A=2.
\]

Por tanto:

\[
\boxed{
4\text{ fases}
\neq
4\text{ dimensiones lineales}.
}
\]

---

# 1. Dos niveles que antes estaban mezclados

Debemos separar:

## 1.1 Espacio geométrico de estados

\[
W_A=\operatorname{span}\{A,JA\}.
\]

Tiene dimensión real 2.

## 1.2 Espacio formal de roles de fase

Sea

\[
\mathcal P_4
=
\{p_0,p_1,p_2,p_3\}
\]

el conjunto de etiquetas:

\[
p_k\leftrightarrow J^k.
\]

Definimos el espacio libre sobre esas etiquetas:

\[
F_4:=\mathbb R[\mathcal P_4].
\]

Entonces:

\[
\boxed{
\dim_{\mathbb R}F_4=4.
}
\]

Existe una aplicación natural:

\[
\pi_A:F_4\to W_A,
\qquad
p_k\mapsto J^kA.
\]

No es inyectiva:

\[
\pi_A(p_2)=-\pi_A(p_0),
\qquad
\pi_A(p_3)=-\pi_A(p_1).
\]

Así, \(F_4\) no es un espacio físico adicional. Es un **libro de roles relacionales**.

---

# 2. El cociente proyectivo produce orden dos

Supongamos que una descripción no distingue un vector de su inverso:

\[
A\sim -A.
\]

En el espacio proyectivo real:

\[
[A]=[-A].
\]

La órbita de cuatro se reduce a:

\[
\boxed{
\mathcal O_2([A])
=
\{[A],[JA]\}.
}
\]

Porque:

\[
J^2[A]=[-A]=[A].
\]

Luego el operador inducido \(\bar J\) satisface:

\[
\boxed{
\bar J^2=I.
}
\]

Algebraicamente:

\[
\boxed{
C_4/\langle J^2\rangle
\simeq C_2.
}
\]

Por tanto existen dos cierres canónicos asociados a la misma gramática:

\[
\boxed{
\text{cierre orientado}: C_4,
}
\]

\[
\boxed{
\text{cierre proyectivo/no orientado}: C_2.
}
\]

---

# 3. Principio de libro relacional completo

## [PUENTE B — completitud booleana]

Sea \(\mathcal P\) el conjunto de roles relacionales distinguibles de un cierre.

Si la arquitectura debe poder representar **qué subconjunto de esos roles participa simultáneamente** sin confundir relaciones de distinto orden, el objeto mínimo exacto es:

\[
\boxed{
\mathfrak B(\mathcal P)
=
\mathcal P(\mathcal P)
\simeq
\{0,1\}^{|\mathcal P|}.
}
\]

Su cardinalidad es:

\[
\boxed{
|\mathfrak B(\mathcal P)|
=
2^{|\mathcal P|}.
}
\]

Este resultado es combinatorio.

Lo que se adopta como puente es que este libro booleano sea el objeto informacional relevante para la regla histórica de cierre binario.

---

# 4. Realización algebraica mediante álgebra exterior

Sea

\[
F=\mathbb R[\mathcal P],
\qquad
\dim F=n:=|\mathcal P|.
\]

La exterior algebra:

\[
\Lambda^\bullet F
=
\bigoplus_{k=0}^n\Lambda^kF
\]

tiene:

\[
\dim\Lambda^kF=\binom nk.
\]

Luego:

\[
\boxed{
\dim\Lambda^\bullet F
=
\sum_{k=0}^n\binom nk
=
2^n.
}
\]

Cada monomio exterior:

\[
p_{i_1}\wedge\cdots\wedge p_{i_k}
\]

codifica un subconjunto orientado de \(k\) roles.

Así, el álgebra exterior ofrece una realización lineal del mismo libro de subconjuntos.

## Ventaja

Conserva explícitamente relaciones:

- unitarias: \(\Lambda^1F\);
- binarias: \(\Lambda^2F\);
- ternarias: \(\Lambda^3F\);
- de orden superior.

Por tanto es una candidata concreta para representar información conjunta que no debe reducirse a pares.

No se afirma que toda relación física sea antisimétrica; ésta es una realización mínima para relaciones orientadas.

---

# 5. La descomposición 1 + (2^n - 1)

El grado cero tiene dimensión:

\[
\boxed{
\dim\Lambda^0F=1.
}
\]

Representa el escalar:

\[
1,
\]

es decir, la configuración vacía/no diferenciada del libro relacional.

El resto tiene dimensión:

\[
\sum_{k=1}^n\binom nk
=
2^n-1.
\]

Por tanto:

\[
\boxed{
2^n
=
1+(2^n-1).
}
\]

Ésta no es una identidad introducida desde la física.

Es la descomposición natural entre:

\[
\boxed{
\text{sector escalar/no diferenciado}
}
\]

y

\[
\boxed{
\text{todos los sectores relacionales no vacíos}.
}
\]

---

# 6. Caso proyectivo: 1:3

Para el cierre proyectivo:

\[
|\mathcal P_2|=2.
\]

Entonces:

\[
\dim F_2=2,
\]

y:

\[
\dim\Lambda^\bullet F_2
=
2^2
=
4.
\]

Por grados:

\[
\dim\Lambda^0F_2=1,
\]

\[
\dim\Lambda^1F_2=2,
\]

\[
\dim\Lambda^2F_2=1.
\]

Luego:

\[
\boxed{
4=1+3.
}
\]

La razón escalar : relacional es:

\[
\boxed{
1:3.
}
\]

---

# 7. Caso orientado: 1:15

Para el cierre orientado:

\[
|\mathcal P_4|=4.
\]

Entonces:

\[
\dim F_4=4,
\]

y:

\[
\dim\Lambda^\bullet F_4
=
2^4
=
16.
\]

Por grados:

\[
\boxed{
16
=
1+4+6+4+1.
}
\]

El grado cero aporta:

\[
1.
\]

Los grados positivos aportan:

\[
4+6+4+1=15.
\]

Por tanto:

\[
\boxed{
16=1+15,
}
\]

y la razón escalar : relacional es:

\[
\boxed{
1:15.
}
\]

---

# 8. Qué significa ahora la profundidad binaria

Proponemos una definición operacional que reemplaza la antigua motivación ambigua.

## [DEFINICIÓN — profundidad booleana de cierre]

Sea \(\mathcal P\) el conjunto mínimo de roles de fase distinguibles cuya participación conjunta debe poder representarse.

Definimos:

\[
\boxed{
n_B:=|\mathcal P|.
}
\]

Entonces el libro exacto tiene:

\[
\boxed{
N_{\rm conf}=2^{n_B}.
}
\]

Así:

\[
n_B=2
\quad\Longrightarrow\quad
N_{\rm conf}=4,
\]

y:

\[
n_B=4
\quad\Longrightarrow\quad
N_{\rm conf}=16.
\]

Esto evita la afirmación incorrecta:

> cuatro estados son cuatro bits.

La afirmación correcta es:

> cuatro **roles distinguibles** producen cuatro decisiones de pertenencia cuando la arquitectura debe representar subconjuntos arbitrarios de roles.

---

# 9. Del conteo a las fracciones cuadráticas

Hasta aquí sólo tenemos cardinalidades.

Para recuperar la regla histórica:

\[
r_V=2^{-n},
\qquad
r_m=1-2^{-n},
\]

se necesita un puente de medida.

## [PUENTE W — peso relacional normalizado]

Postulamos que, en ausencia de una estructura adicional que privilegie combinaciones particulares, el peso cuadrático de un sector es proporcional al número de canales elementales del libro relacional que contiene:

\[
w(S)
=
\frac{\dim S}{\dim\Lambda^\bullet F}.
\]

Entonces el sector escalar tiene:

\[
\boxed{
r_V
=
\frac{1}{2^n}
=
2^{-n},
}
\]

y el sector relacional complementario:

\[
\boxed{
r_m
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

El Puente W es la única identificación necesaria para convertir el conteo de canales en la partición cuadrática histórica.

No se deriva de P3–P6.

Debe declararse y después justificarse o falsarse.

---

# 10. Los dos casos históricos

## Cierre proyectivo

\[
n_B=2
\]

da:

\[
\boxed{
r_V=\frac14,
\qquad
r_m=\frac34,
}
\]

es decir:

\[
\boxed{
1:3.
}
\]

## Cierre orientado

\[
n_B=4
\]

da:

\[
\boxed{
r_V=\frac1{16},
\qquad
r_m=\frac{15}{16},
}
\]

es decir:

\[
\boxed{
1:15.
}
\]

Estas dos particiones ya no se introducen como números independientes.

Provienen de:

\[
C_2
\quad\text{vs.}\quad
C_4
\]

más el mismo principio de completitud booleana.

---

# 11. Correspondencia física: todavía separada

Es tentador identificar:

\[
C_2
\leftrightarrow
\text{sector leptónico},
\]

\[
C_4
\leftrightarrow
\text{sector bariónico}.
\]

Pero esa identificación no se deriva de la matemática anterior.

Para volverla física deben definirse observables capaces de determinar si un sistema:

1. identifica \(A\sim-A\), o
2. conserva la orientación completa.

Por tanto:

\[
\boxed{
1:3\text{ y }1:15
\text{ están derivados como arquitecturas matemáticas;}
}
\]

\[
\boxed{
\text{su asignación a electrón/protón sigue siendo correspondencia tentativa.}
}
\]

---

# 12. Relación con la incertidumbre como bit

En \(\mathfrak B(\mathcal P)\), cada rol \(p_i\) aporta una coordenada:

\[
b_i\in\{0,1\},
\]

que significa:

\[
b_i=
\begin{cases}
0,&p_i\text{ no participa en la relación representada},\\
1,&p_i\text{ participa}.
\end{cases}
\]

Así:

\[
\boxed{
(b_1,\dots,b_n)\in\{0,1\}^n.
}
\]

La unidad binaria aparece como la distinción mínima necesaria para registrar si un rol relacional participa.

Esto es un bit estructural de representación.

No se identifica automáticamente con un bit cuántico físico ni con probabilidad de medición.

---

# 13. Relación con la quinta imagen

El cierre orientado posee cuatro roles:

\[
p_0,p_1,p_2,p_3.
\]

El libro completo de relaciones entre ellos ya contiene:

\[
16
\]

configuraciones.

Por tanto, una quinta **fase del mismo ciclo** no añade un nuevo rol:

\[
p_4=p_0.
\]

En cambio, una nueva diferencia independiente \(r\neq0\) genera un nuevo módulo \(J\)-invariante.

Ese módulo trae su propio libro de roles.

Así se distinguen:

\[
\boxed{
\text{repetición de fase}
}
\]

de:

\[
\boxed{
\text{nueva identidad/módulo}.
}
\]

---

# 14. Qué se ha cerrado realmente

Bajo P3–P6:

\[
J^2=-I,
\qquad
J^4=I.
\]

De ahí se derivan dos cierres naturales:

\[
C_4
\]

y el cociente:

\[
C_4/\{\pm I\}\simeq C_2.
\]

Bajo el Puente B:

\[
C_2
\Rightarrow
2^2=4
=
1+3,
\]

\[
C_4
\Rightarrow
2^4=16
=
1+15.
\]

Bajo el Puente W:

\[
\boxed{
C_2
\Rightarrow
r_V:r_m=1:3,
}
\]

\[
\boxed{
C_4
\Rightarrow
r_V:r_m=1:15.
}
\]

Por tanto existe ahora una ruta no circular desde el álgebra local hasta las dos particiones históricas.

---

# 15. Lo que aún no debe afirmarse

No se ha demostrado:

1. que la naturaleza use necesariamente el libro booleano completo;
2. que el peso físico sea necesariamente proporcional a dimensión/cardinalidad;
3. que \(C_2\) corresponda al electrón;
4. que \(C_4\) corresponda al protón;
5. que la razón de frecuencias medida de una partícula esté dada por esos pesos;
6. que esto resuelva P vs NP.

---

# 16. Falsadores matemáticos y programáticos

La construcción falla como puente físico si:

1. los observables requieren información conjunta que la exterior algebra no conserva;
2. la participación de roles no puede representarse por inclusión/exclusión binaria;
3. aparecen pesos no uniformes que no pueden derivarse de información adicional;
4. la orientación \(A\sim-A\) no distingue las dos clases de sistemas postuladas;
5. una representación más económica conserva toda la información relevante sin producir \(2^n\) configuraciones.

---

# 17. Cadena consolidada

\[
\boxed{
\begin{aligned}
P3\text{--}P6
&\Rightarrow
J^2=-I\\
&\Rightarrow
J^4=I\\
&\Rightarrow
C_4\\
&\Rightarrow
\begin{cases}
C_4,&\text{orientación conservada},\\
C_2=C_4/\{\pm I\},&\text{orientación proyectivizada}
\end{cases}\\
&\xRightarrow{\text{Puente B}}
\begin{cases}
2^4=16=1+15,\\
2^2=4=1+3
\end{cases}\\
&\xRightarrow{\text{Puente W}}
\begin{cases}
r_V:r_m=1:15,\\
r_V:r_m=1:3.
\end{cases}
\end{aligned}
}
\]

Éste es el puente matemático más corto encontrado hasta ahora entre:

\[
\boxed{
\text{cierre de fase}
\to
\text{profundidad binaria}
\to
\text{partición armónica}.
}
\]
