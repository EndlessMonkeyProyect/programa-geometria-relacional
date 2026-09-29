# MF-58 — Independencia relacional, rango de distinguibilidad y límite del rango semántico

**Versión:** v0.66-research  
**Estado:** resultados exactos para sistemas finitos + no-go estructural + consecuencia explícita para la rama P vs NP.  
**Alcance:** define cuándo una comparación es redundante, parcialmente novedosa o independiente respecto de un cierre. No identifica todavía estas cantidades con dimensiones espaciales físicas.

---

## 1. Problema

MF-57 corrigió la idea de que repetir una misma referencia genera nuevas dimensiones. Una referencia fija produce un ciclo local. Por tanto, si una nueva dimensión ha de emerger, debe corresponder a una diferencia que el cierre anterior no pueda expresar.

MF-58 pregunta:

> ¿qué significa exactamente que una diferencia sea nueva o independiente respecto de las referencias existentes?

---

## 2. Firma contextual

Sea un conjunto finito de realizaciones `X` y una familia de comparaciones `S`.

Cada comparación `c` tiene una respuesta

\[
q_c:X\to A_c.
\]

La firma conjunta es

\[
\Phi_S(x)=(q_c(x))_{c\in S}.
\]

Dos realizaciones son indistinguibles respecto de `S` si tienen la misma firma.

El número de clases es

\[
N(S)=|\operatorname{im}\Phi_S|,
\]

y la distinguibilidad relacional es

\[
\boxed{I(S)=\log_2N(S).}
\]

---

## 3. Novedad condicional

Para una nueva comparación `c`, definimos

\[
\boxed{\nu(c\mid S)=I(S\cup\{c\})-I(S).}
\]

Siempre:

\[
\nu(c\mid S)\ge0.
\]

Si `c` es binaria:

\[
\boxed{0\le\nu(c\mid S)\le1.}
\]

Esto extiende MF-55: una comparación binaria puede abrir como máximo un bit, pero su aporte puede ser parcial.

---

## 4. Redundancia exacta

La nueva comparación no aporta ninguna distinción si y sólo si su respuesta puede reconstruirse desde la firma anterior:

\[
\boxed{
\nu(c\mid S)=0
\iff
q_c=\bar q_c\circ\Phi_S
}
\]

para alguna función `\bar q_c`.

Por tanto:

\[
\boxed{
\text{nueva observación}\neq\text{nueva referencia}.
}
\]

Sólo hay apertura cuando la comparación no factoriza por el cierre existente.

---

## 5. Independencia de soporte

Sea

\[
I(c)=\log_2|\operatorname{im}q_c|.
\]

Definimos el déficit de independencia entre la firma previa y la comparación nueva:

\[
\boxed{
D_R(S:c)=I(S)+I(c)-I(S\cup\{c\}).
}
\]

Entonces, exactamente:

\[
\boxed{
\nu(c\mid S)=I(c)-D_R(S:c).
}
\]

Esta identidad une MF-56 y MF-58.

### Tres regímenes

**Redundante**

\[
\nu=0.
\]

La comparación ya estaba contenida en el cierre.

**Parcialmente nueva**

\[
0<\nu<I(c).
\]

La comparación abre diferencias, pero parte de su contenido depende de lo que el cierre ya distinguía.

**Independiente en soporte**

\[
\boxed{D_R=0\iff\nu=I(c).}
\]

La firma conjunta realiza el producto completo:

\[
\operatorname{im}\Phi_{S\cup\{c\}}
=
\operatorname{im}\Phi_S\times\operatorname{im}q_c.
\]

Para una comparación binaria no constante:

\[
\boxed{D_R=0\Rightarrow\nu=1\text{ bit}.}
\]

Éste es el candidato más fuerte a una **nueva referencia independiente**.

---

## 6. Regla de cadena

Para cualquier orden `c_1,...,c_m`:

\[
\boxed{
I(\{c_1,\ldots,c_m\})
=
\sum_{j=1}^{m}
\nu(c_j\mid c_1,\ldots,c_{j-1}).
}
\]

Los aportes individuales dependen del orden, pero la suma final no.

Así, la cantidad total de distinguibilidad no depende de la narrativa usada para introducir las comparaciones.

---

## 7. Capacidad binaria mínima

Si se permite una codificación binaria arbitraria de las clases del cierre, el número mínimo de bits para etiquetarlas es

\[
\boxed{d_2(S)=\lceil I(S)\rceil.}
\]

Debe distinguirse:

- `I(S)`: contenido de distinguibilidad exacto en bits logarítmicos;
- `d_2(S)`: número mínimo de coordenadas binarias sin estructura adicional.

Una comparación binaria plenamente independiente aumenta ambos en exactamente un bit/coordenada.

Una comparación parcialmente nueva puede aumentar `I` sin aumentar todavía `d_2` si existe capacidad de codificación libre en el marco anterior.

Por tanto:

\[
\boxed{
\text{novedad}>0
\not\Rightarrow
\text{una nueva dimensión binaria completa}.
}
\]

---

## 8. Cierre por dependencia funcional

Dentro de un universo declarado de comparaciones `\mathcal O`, definimos

\[
\operatorname{Cl}(S)
=
\{c\in\mathcal O:q_c\text{ factoriza por }\Phi_S\}.
\]

Esta operación satisface:

1. extensividad: `S\subseteq Cl(S)`;
2. monotonía: `S\subseteq T\Rightarrow Cl(S)\subseteq Cl(T)`;
3. idempotencia: `Cl(Cl(S))=Cl(S)`.

Es por tanto un operador de cierre exacto.

---

## 9. No-go MF-58A — este cierre no es, en general, un espacio vectorial ni un matroide

La intuición de “base” y “dimensión” no puede importarse automáticamente del álgebra lineal.

Considere cuatro realizaciones y las comparaciones binarias

\[
s=0011,\qquad x=0101,\qquad y=0001.
\]

Se cumple:

\[
y=s\land x.
\]

Por tanto:

\[
y\in Cl(\{s,x\}),
\qquad
y\notin Cl(\{s\}).
\]

Pero:

\[
x\notin Cl(\{s,y\}).
\]

Esto viola el axioma de intercambio que caracterizaría una estructura tipo matroide.

Existe incluso una familia binaria finita con conjuntos generadores mínimos por inclusión de tamaños distintos: 2 y 3.

Por tanto:

\[
\boxed{
\text{dependencia relacional general}
\not\Rightarrow
\text{rango lineal/matroide canónico}.
}
\]

Si una dimensión física ha de emerger, se necesita una estructura adicional que justifique una ley de intercambio, ortogonalidad u otra noción geométrica fuerte.

---

## 10. Ejemplo mínimo

Tome:

\[
s=0011.
\]

### Nueva referencia completamente independiente

Para

\[
x=0101,
\]

las cuatro firmas `(s,x)` aparecen:

\[
00,01,10,11.
\]

Luego:

\[
D_R(s:x)=0,
\qquad
\nu(x\mid s)=1.
\]

### Novedad parcial

Para

\[
y=0001,
\]

sólo aparecen tres firmas:

\[
00,10,11.
\]

Entonces:

\[
I(s,y)=\log_2 3,
\]

\[
\boxed{
\nu(y\mid s)=\log_2 3-1\approx0.585
}
\]

y

\[
\boxed{
D_R(s:y)=2-\log_2 3\approx0.415.
}
\]

La diferencia es nueva, pero no independiente.

### Redundancia posterior

Una vez conocidas `s` y `x`, `y=s\land x`:

\[
\boxed{\nu(y\mid s,x)=0.}
\]

Lo que parecía una nueva diferencia desde un marco pobre se vuelve derivable desde un marco más rico.

---

## 11. Lectura ontológica prudente

MF-58 permite reemplazar una frase demasiado fuerte:

> “si aparece información nueva, nace una dimensión”.

por tres niveles:

\[
\boxed{
\begin{array}{ll}
\nu=0 &: \text{la diferencia ya cabe};\\
0<\nu<I(c) &: \text{hay refinamiento parcialmente dependiente};\\
\nu=I(c) &: \text{aparece una referencia plenamente independiente en soporte}.
\end{array}
}
\]

La última es el candidato más limpio a “nueva dimensión relacional”.

Identificarla con una dimensión espacial física permanece abierto.

---

## 12. Consecuencia decisiva para P vs NP

Sea una instancia booleana sobre `n` variables. Su espacio de asignaciones tiene

\[
|X|=2^n.
\]

Para **cualquier** familia de comparaciones/cláusulas sobre esas asignaciones:

\[
N(S)\le|X|=2^n.
\]

Por tanto:

\[
\boxed{I(S)\le n.}
\]

y

\[
\boxed{d_2(S)\le n.}
\]

Éste es un no-go importante:

\[
\boxed{
\text{el rango semántico de distinguibilidad, por sí solo,
no puede explicar la dificultad NP.}
}
\]

En efecto, el número mínimo de bits para **nombrar** una clase semántica es siempre lineal en `n`.

La dificultad puede residir en otra parte:

- construir/acreditar la clase correcta;
- representar económicamente la función de transición entre clases;
- actualizarla tras eliminación/proyección;
- decidir equivalencia sin reabrir un interior exponencial.

Esto refuerza la separación ya obtenida por el programa:

\[
\boxed{
\text{representar}
\neq
\text{acreditar}
\neq
\text{actualizar}
\neq
\text{decidir}.
}
\]

---

## 13. Perfil de complejidad en lugar de un solo rango

Para la rama computacional, MF-58 recomienda no colapsar todo a una única “dimensión”.

El objeto relevante debe ser al menos un perfil:

\[
\boxed{
\mathfrak C
=
(I_{rel},L_{desc},T_{acc},T_{upd},T_{dec}).
}
\]

Donde:

- `I_rel`: bits semánticos mínimos de distinguibilidad;
- `L_desc`: longitud de una representación exacta operativa;
- `T_acc`: costo de acreditar equivalencias/cierres;
- `T_upd`: costo de actualizar después de una relación/proyección;
- `T_dec`: costo de extraer la decisión requerida.

No se propone todavía una combinación escalar de estas cantidades.

Para una ruta hacia `P`, todas las componentes operativas relevantes tendrían que permanecer polinómicas de manera uniforme.

---

## 14. Qué quedó resuelto y qué no

### Resuelto dentro del formalismo finito

- criterio exacto de redundancia;
- medida de novedad condicional;
- identidad entre novedad y déficit de dependencia;
- criterio de independencia plena de soporte;
- regla de cadena;
- cota binaria;
- operador de cierre funcional;
- no-go de estructura matroide general;
- cota `I\le n` para comparaciones booleanas sobre `n` variables.

### Abierto

- qué estructura adicional convierte algunas referencias en direcciones geométricas físicas;
- cómo se deriva esa estructura desde reflexión/cierre;
- qué gramática operacional es físicamente/computacionalmente admisible;
- cómo medir `L_desc,T_acc,T_upd,T_dec` sin introducir un oráculo;
- `P` vs `NP`.

---

## 15. Próximo paso

MF-59 debe trasladar el resultado a SAT sin volver a cometer el error de medir sólo cantidad de información.

La pregunta correcta ya no es:

\[
\text{“¿cuántos bits independientes tiene SAT?”}
\]

porque la respuesta semántica está acotada trivialmente por `n`.

La pregunta correcta es:

\[
\boxed{
\text{¿cuánto cuesta acreditar y actualizar exactamente esos bits relacionales
sin reabrir el espacio }2^n\text{?}
}
\]

Ésta es ahora la frontera precisa de la rama NP.
