# Cierre transversal, radio de resolución y recursión de escala
## Formalización v0.82

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** formalización exploratoria. No implica validación física ni solución de P vs NP.

---

# 0. Separación epistemológica

- **[POSTULADO]** regla constitutiva del programa.
- **[DEFINICIÓN]** objeto matemático elegido para hacer precisa la idea.
- **[DERIVADO]** consecuencia matemática de las definiciones e hipótesis declaradas.
- **[CORRESPONDENCIA]** traducción tentativa entre el formalismo y una lectura física.
- **[ABIERTO]** teorema, cota o puente todavía no demostrado.
- **[NO-GO]** identificación que no debe hacerse sin hipótesis adicionales.

---

# 1. Arquitectura acreditada y comparación

Sea \(\mathcal A\) la arquitectura relacional actualmente acreditada.

Una comparación entre dos expresiones \(a,b\) produce:

\[
\boxed{
\mathcal C(a,b)=(q,r)
}
\]

donde:

- \(q\) es la parte resuelta o acreditada;
- \(r\) es el residuo: la diferencia que todavía no puede absorberse en el marco actual.

Sea \(\operatorname{Cl}(\mathcal A)\) el cierre de lo que la arquitectura puede representar sin añadir una referencia independiente.

Entonces:

\[
r=0
\quad\Longrightarrow\quad
\text{la comparación puede cerrar dentro de }\mathcal A,
\]

mientras:

\[
r\neq0,\qquad r\notin\operatorname{Cl}(\mathcal A)
\]

significa que existe novedad relacional.

**[POSTULADO P1 — Conservación de la novedad]**  
Una diferencia relevante que no cabe en el marco vigente no se elimina. Debe conservarse como complemento de representación.

---

# 2. Complemento antes que perpendicularidad

Ontológicamente, la descomposición mínima es:

\[
\boxed{
x=x_{\parallel}+x_{\mathrm{comp}}
}
\]

donde \(x_{\parallel}\) es lo representable en \(\mathcal A\) y \(x_{\mathrm{comp}}\) es el complemento que todavía no cabe.

No se presupone todavía una geometría euclidiana.

Si posteriormente la realización dispone de un producto interno, definimos el proyector:

\[
P_{\mathcal A}:\mathcal H\to\mathcal H_{\mathcal A}
\]

y su complemento:

\[
P_{\mathcal A}^{\perp}=I-P_{\mathcal A}.
\]

Entonces:

\[
\boxed{
x=P_{\mathcal A}x+P_{\mathcal A}^{\perp}x
}
\]

y, bajo ortogonalidad,

\[
\boxed{
\|x\|^2
=
\|P_{\mathcal A}x\|^2
+
\|P_{\mathcal A}^{\perp}x\|^2.
}
\]

**[NO-GO]** “información nueva” no implica por sí sola ortogonalidad.  
La ortogonalidad es una realización geométrica del complemento, no su definición ontológica.

---

# 3. El residuo como información transversal

Definimos:

\[
\boxed{
r_{\perp}:=P_{\mathcal A}^{\perp}x.
}
\]

En esta realización, el residuo es información que no puede representarse en el subespacio vigente.

La extensión mínima del marco es:

\[
\boxed{
\mathcal H_{\mathcal A'}
=
\mathcal H_{\mathcal A}
\oplus
\operatorname{span}\{r_{\perp}\}.
}
\]

Lo que era “perpendicular” o exterior respecto del nivel \(k\) queda contenido en el nivel \(k+1\).

Por tanto:

\[
\boxed{
\text{exterior al marco }k
\;\not\equiv\;
\text{exterior a la totalidad}.
}
\]

La recursión es:

\[
\mathcal A_k
\;\to\;
\mathcal A_{k+1}
=
\operatorname{Cl}
\left(
\mathcal A_k\cup\{r_k\}
\right).
\]

---

# 4. Módulos cerrados compatibles

Sea:

\[
\boxed{
\mathfrak M(\mathcal A)
}
\]

la familia de módulos/cierres internamente consistentes todavía compatibles con la información acreditada por \(\mathcal A\).

Una comparación discriminante \(d\) induce:

\[
\boxed{
\mathfrak M'
=
\{M\in\mathfrak M(\mathcal A):
M\text{ es compatible con }d\}.
}
\]

Por construcción:

\[
\mathfrak M'\subseteq\mathfrak M.
\]

Si la comparación aporta información real:

\[
\boxed{
\mathfrak M'\subsetneq\mathfrak M.
}
\]

Ésta es la formalización de la frase:

> comparar reduce los módulos en que la diferencia todavía puede organizarse.

El cierre identitario ocurre cuando:

\[
\boxed{
|\mathfrak M|=1.
}
\]

Puede quedar todavía residuo representacional interno; por eso distinguimos:

\[
\boxed{
\text{identidad determinada}
\neq
\text{residuo completamente eliminado}.
}
\]

La cristalización exacta exige además:

\[
\boxed{
\rho=0.
}
\]

---

# 5. Incertidumbre y radio normalizado

Definimos la incertidumbre modular:

\[
\boxed{
U_M(\mathcal A)
=
\log_2|\mathfrak M(\mathcal A)|.
}
\]

Entonces:

\[
U_M=0
\quad\Longleftrightarrow\quad
|\mathfrak M|=1.
\]

Para representar la intuición de que el “radio” asciende hacia una unidad definida, introducimos el radio normalizado de resolución:

\[
\boxed{
R_{\mathrm{res}}
=
2^{-U_M}
=
\frac{1}{|\mathfrak M|}.
}
\]

Así:

\[
0<R_{\mathrm{res}}\le1,
\]

y:

\[
\boxed{
R_{\mathrm{res}}=1
\quad\Longleftrightarrow\quad
|\mathfrak M|=1.
}
\]

Una comparación discriminante satisface:

\[
|\mathfrak M'|<|\mathfrak M|
\]

y por tanto:

\[
\boxed{
R_{\mathrm{res}}'>R_{\mathrm{res}}.
}
\]

El radio aumenta no porque transcurra tiempo, sino porque disminuye la multiplicidad de cierres todavía compatibles.

---

# 6. Radio de resolución y radio físico

Conviene mantener dos objetos separados.

## 6.1 Radio informacional normalizado

\[
R_{\mathrm{res}}=\frac{1}{|\mathfrak M|}.
\]

Mide cuánto se ha determinado la identidad relativa a los módulos compatibles.

## 6.2 Radio mínimo de discriminación

Para una familia admisible de discriminantes \(\mathcal D\):

\[
r_{\min}(\mathcal C;\mathcal D)
=
\min
\left\{
|\mathcal B|:
\mathcal B\subseteq\mathcal D,\;
\Phi_{\mathcal B}|_{\mathcal C}
\text{ es inyectiva}
\right\}.
\]

Este segundo objeto cuenta cuántas comparaciones adicionales son necesarias para separar todos los estados de una cápsula.

**[NO-GO]** ninguno de estos radios es automáticamente una longitud física.

Una correspondencia física requiere un puente independiente.

---

# 7. No hay tiempo primitivo en la recursión

La secuencia:

\[
\mathcal A_0\to\mathcal A_1\to\cdots
\]

no representa necesariamente tiempo físico.

El índice \(k\) cuenta:

\[
\boxed{
\text{profundidad lógica}
=
\text{orden de autorreferencias/cierres}.
}
\]

El tiempo aparece sólo cuando un ciclo es adoptado como referencia y se compara con otro ciclo.

Por tanto:

\[
\boxed{
\text{profundidad}
\neq
\text{tiempo}.
}
\]

---

# 8. Un ciclo de cierre como operador idempotente

Podemos formalizar la idea de “la totalidad se resuelve en un solo ciclo” mediante un operador de cierre conceptual:

\[
\boxed{
\Gamma:\mathcal A\mapsto\overline{\mathcal A}
}
\]

con:

\[
\boxed{
\Gamma^2=\Gamma.
}
\]

Una vez cerrado:

\[
\Gamma(\overline{\mathcal A})
=
\overline{\mathcal A}.
\]

Esto captura un único acto lógico de cierre.

**Importante:** que el cierre sea conceptualmente un solo operador no implica que su evaluación computacional tenga costo constante.

Separamos:

\[
\boxed{
\text{profundidad ontológica}
\neq
\text{costo computacional}.
}
\]

---

# 9. Información almacenada en el cierre

Sea \(H_k\) la firma heredada por una identidad cerrada.

Si la comparación que produce el cierre contiene una orientación binaria:

\[
\sigma_k\in\{-1,+1\},
\]

entonces:

\[
\boxed{
H_{k+1}=(H_k,\sigma_k).
}
\]

El cierre no destruye el bit; lo incorpora en la identidad de la nueva unidad.

La unidad cerrada puede actuar como referencia:

\[
\boxed{
\overline{\mathcal A}_k
\longrightarrow
\text{referencia de }\mathcal A_{k+1}.
}
\]

Así:

\[
\boxed{
\text{residuo}
\to
\text{complemento}
\to
\text{cierre}
\to
\text{identidad}
\to
\text{nueva referencia}.
}
\]

---

# 10. Relación con el cierre de orden cuatro

Sea \(J\) un operador local que satisface:

\[
\boxed{
J^2=-I.
}
\]

Entonces:

\[
\boxed{
J^4=I.
}
\]

La órbita:

\[
x,\;Jx,\;J^2x,\;J^3x
\]

cierra al cuarto paso algebraico.

Esto ofrece un candidato para un módulo local cerrado de orden cuatro.

Pero debe distinguirse:

\[
\boxed{
J^4=I
}
\]

de:

\[
\boxed{
\text{“cuatro es la capacidad universal máxima de información”.}
}
\]

La segunda afirmación todavía requiere un teorema adicional.

## Teorema objetivo 4→5

Probar que, bajo las reglas mínimas del programa, una quinta diferencia independiente no puede representarse dentro del cierre de orden cuatro sin:

1. introducir una nueva referencia;
2. o ampliar el espacio de representación.

Formalmente, buscar condiciones bajo las cuales:

\[
r_5\notin\operatorname{Cl}(\mathcal A_4)
\]

implique:

\[
\boxed{
\mathcal A_5
=
\operatorname{Cl}
(\mathcal A_4\oplus\langle r_5\rangle).
}
\]

---

# 11. Forma abstracta de la operación central

El núcleo puede resumirse mediante:

\[
\boxed{
\mathscr R:
(\mathcal A,\mathfrak M,x)
\mapsto
(\mathcal A',\mathfrak M',r)
}
\]

con:

\[
x=q+r,
\]

\[
q\in\operatorname{Cl}(\mathcal A),
\]

\[
r\notin\operatorname{Cl}(\mathcal A)
\quad\text{si existe novedad},
\]

\[
\mathfrak M'\subseteq\mathfrak M,
\]

y:

\[
\mathcal A'
=
\operatorname{Cl}(\mathcal A\cup\{r\})
\quad\text{si }r\neq0.
\]

Queremos que:

\[
\boxed{
|\mathfrak M'|<|\mathfrak M|
}
\]

para toda comparación verdaderamente discriminante.

El cierre es el punto fijo:

\[
\boxed{
\mathscr R(\overline{\mathcal A})
=
\overline{\mathcal A}.
}
\]

---

# 12. Puente computacional hacia P vs NP

La formalización no demuestra \(P=NP\).

Sí identifica una pregunta más precisa.

Para una instancia computacional \(F\), sea:

\[
\mathfrak M(F)
\]

la familia de módulos/cierres compatibles con la información local disponible.

El objetivo no es enumerar sus miembros.

Se busca un operador:

\[
\boxed{
\mathscr R_F
}
\]

que, usando sólo una representación compacta, produzca:

\[
\mathfrak M_{k+1}
\subsetneq
\mathfrak M_k
\]

cuando exista información discriminante.

La pregunta de complejidad es:

\[
\boxed{
\text{¿puede calcularse cada cociente/reducción sin enumerar }
\mathfrak M_k\text{?}
}
\]

Una vía a \(P=NP\) requeriría demostrar simultáneamente:

\[
\operatorname{size}(R_k)\le\operatorname{poly}(|F|),
\]

\[
T_{\mathrm{update}}(R_k)\le\operatorname{poly}(|F|),
\]

\[
T_{\mathrm{closure}}(R_k)\le\operatorname{poly}(|F|),
\]

y preservación exacta de satisfacibilidad.

## Falsador computacional directo

La vía queda descartada si existe una familia de instancias para la que cualquiera de estas operaciones exige:

- enumerar exponencialmente módulos;
- mantener una representación superpolinómica;
- resolver implícitamente el problema original para decidir qué residuo conservar.

---

# 13. Síntesis canónica

\[
\boxed{
\text{unidad}
\to
\text{reflexión}
\to
\text{diferencia}
\to
\text{comparación}
\to
(q,r)
}
\]

\[
\boxed{
r=0
\Rightarrow
\text{cierre interno}
}
\]

\[
\boxed{
r\neq0
\Rightarrow
\text{complemento}
\Rightarrow
\text{realización transversal}
\Rightarrow
\text{marco ampliado}
}
\]

y simultáneamente:

\[
\boxed{
\mathfrak M_0
\supset
\mathfrak M_1
\supset
\cdots
\supset
\mathfrak M_\star,
\qquad
|\mathfrak M_\star|=1.
}
\]

La medida dual puede escribirse como:

\[
\boxed{
U_M=\log_2|\mathfrak M|,
\qquad
R_{\mathrm{res}}=2^{-U_M}.
}
\]

De modo que:

\[
\boxed{
U_M\downarrow0
\quad\Longleftrightarrow\quad
R_{\mathrm{res}}\uparrow1.
}
\]

No es evolución temporal.

Es resolución estructural.

La información que no cabe en un nivel no desaparece: se conserva como complemento y puede volverse parte constitutiva de la identidad cerrada del nivel siguiente.
