# Autorrecurencia por capas y herencia sin pérdida
## La reflexión conserva la capa anterior y el cierre puede convertirse en referencia
### Formalización v0.87

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** formalización matemática interna del mecanismo de herencia entre capas.  
**No implica validación física ni selección de partículas.**

---

# 0. Idea que se formaliza

La intuición ontológica es:

> cuando una estructura cierra, no necesita reempacar toda su historia dentro de una nueva variable, porque la información que la produjo sigue formando parte de la capa del sistema en la que el cierre existe.

La reflexión siguiente no borra la capa previa.

La conserva como una de sus referencias y añade una nueva diferencia.

Por tanto:

\[
\boxed{
\text{autorrecurencia}
\neq
\text{reinicio}
}
\]

sino:

\[
\boxed{
\text{autorrecurencia}
=
\text{capa heredada}
+
\text{novedad}.
}
\]

---

# 1. Capas relacionales

Sea

\[
L_k
\]

la capa relacional acreditada en profundidad \(k\).

Una capa contiene las diferencias, referencias y cierres que siguen siendo distinguibles en ese nivel.

El paso a una nueva capa no reemplaza \(L_k\).

La nueva capa se construye como una extensión:

\[
\boxed{
L_{k+1}
=
i_k(L_k)\oplus N_{k+1},
}
\]

cuando la novedad es independiente, donde:

- \(i_k:L_k\hookrightarrow L_{k+1}\) es la inclusión de la capa heredada;
- \(N_{k+1}\) es el módulo de información nueva.

La suma directa expresa independencia informacional en la realización ortogonal.

---

# 2. Recuperabilidad exacta de la capa anterior

Definimos la proyección canónica:

\[
p_k:
L_{k+1}\to L_k,
\qquad
p_k(i_kx+n)=x.
\]

Entonces:

\[
\boxed{
p_k\circ i_k=I_{L_k}.
}
\]

## Teorema 2.1 — Herencia sin pérdida

La inclusión \(i_k\) es inyectiva y toda información representada en \(L_k\) permanece exactamente recuperable desde \(L_{k+1}\).

## Demostración

Si:

\[
i_kx=i_ky,
\]

aplicando \(p_k\):

\[
p_ki_kx=p_ki_ky
\]

y, como \(p_ki_k=I\),

\[
x=y.
\]

Además, para todo \(x\in L_k\),

\[
p_k(i_kx)=x.
\]

Por tanto la capa anterior no necesita reconstruirse ni almacenarse por segunda vez.

\[
\blacksquare
\]

---

# 3. La reflexión como estructura de dos piernas

Una reflexión no se representa sólo por su imagen.

Se representa por la relación entre:

1. aquello que sirve de referencia;
2. aquello que aparece como nueva imagen.

Escribimos una reflexión elemental como:

\[
\boxed{
\mathfrak R_{k+1}(x)
=
\big(i_kx,\nu_{k+1}(x)\big),
}
\]

donde:

\[
i_kx\in i_k(L_k)
\]

es la pierna heredada y:

\[
\nu_{k+1}(x)\in N_{k+1}
\]

es la pierna novedosa.

La información anterior queda literalmente presente en la primera componente de la reflexión.

Así:

\[
\boxed{
\pi_{\rm heredada}\mathfrak R_{k+1}(x)=i_kx.
}
\]

No hace falta añadir una variable de "memoria histórica" externa.

La memoria estructural es la propia permanencia de la capa heredada.

---

# 4. Reflexión de una reflexión

Sea:

\[
\mathfrak R_k
\]

una relación ya construida.

Como su resultado pertenece ahora a la capa acreditada, puede volver a utilizarse como argumento de una nueva reflexión:

\[
\boxed{
\mathfrak R_{k+1}
=
\mathfrak R(\mathfrak R_k).
}
\]

Esto produce profundidad lógica:

\[
\mathfrak R,
\quad
\mathfrak R(\mathfrak R),
\quad
\mathfrak R(\mathfrak R(\mathfrak R)),
\ldots
\]

sin introducir tiempo físico.

La profundidad es orden de autorreferencia.

---

# 5. Cierre estructural

Sea:

\[
\Gamma_k:L_k\to L_k
\]

un operador de cierre con:

\[
\boxed{
\Gamma_k^2=\Gamma_k.
}
\]

Una identidad cerrada es un punto fijo:

\[
\boxed{
\Gamma_kx=x.
}
\]

Para que un cierre estable pueda actuar como referencia en la siguiente capa, se exige compatibilidad de herencia:

\[
\boxed{
\Gamma_{k+1}i_k
=
i_k\Gamma_k.
}
\]

Esta ecuación expresa matemáticamente:

> la ampliación de la capa no cambia retroactivamente aquello que ya estaba cerrado en la capa heredada.

---

# 6. Teorema de persistencia del cierre

## Teorema 6.1

Si:

\[
\Gamma_kx=x
\]

y:

\[
\Gamma_{k+1}i_k=i_k\Gamma_k,
\]

entonces:

\[
\boxed{
\Gamma_{k+1}(i_kx)=i_kx.
}
\]

## Demostración

\[
\Gamma_{k+1}(i_kx)
=
i_k(\Gamma_kx)
=
i_kx.
\]

\[
\blacksquare
\]

Así una identidad cerrada puede sobrevivir como referencia dentro de una capa más rica sin tener que rehacer su cierre.

---

# 7. La realización \(J\)-invariante ya contiene esta herencia

De la formalización anterior:

\[
J_k^2=-I,
\qquad
J_k^4=I.
\]

Sea \(L_k\) un módulo \(J_k\)-invariante.

Si aparece una diferencia \(y\) con residuo:

\[
r=(I-P_{L_k})y\neq0,
\]

la mínima extensión estable es:

\[
\boxed{
L_{k+1}
=
L_k
\oplus
\operatorname{span}\{r,Jr\}.
}
\]

Definimos:

\[
N_{k+1}
=
\operatorname{span}\{r,Jr\}.
\]

Como ambos sumandos son \(J\)-invariantes, el operador extendido tiene forma:

\[
\boxed{
J_{k+1}
=
J_k\oplus J_{N_{k+1}}.
}
\]

Por construcción:

\[
\boxed{
J_{k+1}i_k=i_kJ_k.
}
\]

Esto es exactamente una relación de entrelazamiento/intertwining entre niveles.

---

# 8. Teorema de herencia del cierre de fase

## Teorema 8.1

Si:

\[
J_k^4=I_{L_k}
\]

y:

\[
J_{k+1}i_k=i_kJ_k,
\]

entonces:

\[
\boxed{
J_{k+1}^4i_k=i_k.
}
\]

## Demostración

\[
J_{k+1}^4i_k
=
J_{k+1}^3(i_kJ_k)
=
\cdots
=
i_kJ_k^4
=
i_k.
\]

\[
\blacksquare
\]

Por tanto, en la realización ortogonal ya construida, **el cierre de fase del nivel anterior se hereda automáticamente**.

No hace falta postular de nuevo el cuatro en cada capa.

---

# 9. Dónde queda la información anterior

La información anterior no tiene por qué comprimirse toda dentro del nuevo identificador \(x_{k+1}\).

El estado completo de nivel \(k+1\) es:

\[
\boxed{
\Sigma_{k+1}
=
(L_{k+1},x_{k+1}),
}
\]

no sólo:

\[
x_{k+1}.
\]

Como:

\[
L_k\subset L_{k+1},
\]

la circunstancia anterior sigue perteneciendo al sistema.

La identidad nueva puede ser pequeña porque la capa que la sostiene no fue borrada.

Esto distingue:

\[
\boxed{
\text{identidad}
}
\]

de:

\[
\boxed{
\text{contexto/capa que hace significativa esa identidad}.
}
\]

---

# 10. La identidad no contiene toda la historia

La frase:

> "el cierre guarda toda su historia"

es demasiado fuerte.

La formulación correcta es:

\[
\boxed{
\text{el cierre conserva los invariantes que necesita para ser identidad,
mientras la capa conserva el contexto relacional todavía acreditado}.
}
\]

Así no se exige que un objeto aislado codifique todo el pasado.

Se exige sólo que la evolución de capas sea fiel respecto de la información relevante.

---

# 11. Una reflexión conserva referencia y novedad

El paso generativo mínimo puede escribirse:

\[
\boxed{
L_k
\longrightarrow
\big(i_k(L_k),N_{k+1}\big).
}
\]

La nueva reflexión tiene dos componentes:

\[
\boxed{
\text{herencia}
+
\text{novedad}.
}
\]

Esto realiza exactamente la condición ontológica previa:

\[
\boxed{
\text{cierre}
=
\text{herencia}
+
\text{novedad}.
}
\]

La herencia está en la inclusión \(i_k(L_k)\).

La novedad está en \(N_{k+1}\).

---

# 12. Autorrecurencia sin duplicación

Podría parecer que, al heredar todas las capas, la descripción crece por duplicación:

\[
L_0\subset L_1\subset L_2\subset\cdots.
\]

Pero la inclusión no duplica información.

Cada nueva capa agrega sólo el cociente novedoso:

\[
\boxed{
L_{k+1}/i_k(L_k).
}
\]

En la realización ortogonal:

\[
\boxed{
L_{k+1}/L_k
\simeq
N_{k+1}.
}
\]

Por tanto el costo estructural del nuevo nivel es exactamente la novedad, no toda la historia anterior.

Ésta es la forma matemática de:

> el sistema no vuelve a cargar lo ya resuelto.

---

# 13. Cociente de novedad

Definimos la novedad del paso \(k\to k+1\) como:

\[
\boxed{
Q_{k+1}
:=
L_{k+1}/i_k(L_k).
}
\]

Si:

\[
Q_{k+1}=0,
\]

no apareció dimensión estructural nueva.

Si:

\[
Q_{k+1}\neq0,
\]

la nueva capa contiene información que no cabía en la anterior.

En la realización \(J\)-invariante mínima:

\[
\dim_{\mathbb R}Q_{k+1}=2
\]

por cada residuo independiente, porque:

\[
Q_{k+1}
\simeq
\operatorname{span}\{r,Jr\}.
\]

---

# 14. La nueva unidad como interfaz

Una identidad cerrada:

\[
x_k\in\operatorname{Fix}(\Gamma_k)
\]

puede ser utilizada como interfaz por el nivel siguiente.

Esto no significa que el nivel siguiente sólo vea \(x_k\).

Significa que las operaciones posteriores pueden referirse a \(x_k\) sin tener que reabrir toda la estructura interna que ya cerró.

Es decir:

\[
\boxed{
\text{cierre}
\to
\text{interfaz}
\to
\text{nueva relación}.
}
\]

La capa mantiene la información detallada.

La interfaz permite economía descriptiva.

---

# 15. Condición de suficiencia

Sea \(Q_k:L_k\to Y_k\) una familia de observables relevantes.

Una identidad/interfaz:

\[
s_k:L_k\to S_k
\]

es suficiente si existe:

\[
\bar Q_k:S_k\to Y_k
\]

tal que:

\[
\boxed{
Q_k=\bar Q_k\circ s_k.
}
\]

Esto formaliza:

> una vez cerrado, el nivel superior no necesita volver a consultar cada detalle interno para responder las preguntas que el cierre ya resolvió.

La información no desaparece.

Se vuelve redundante para esas preguntas.

---

# 16. Qué se deriva y qué se adopta

## Derivado dentro de la realización ortogonal

De:

\[
L_{k+1}
=
L_k\oplus\operatorname{span}\{r,Jr\}
\]

se deriva:

- inclusión fiel de \(L_k\);
- proyección de recuperación \(p_ki_k=I\);
- conservación exacta de la información representada en la capa previa;
- herencia de \(J\) mediante suma directa;
- herencia automática de \(J^4=I\);
- novedad localizada en el cociente \(L_{k+1}/L_k\).

## Condición adicional para un cierre estructural general

Para un operador de cierre distinto del cierre de fase se necesita:

\[
\Gamma_{k+1}i_k=i_k\Gamma_k.
\]

Esta condición no se deriva de \(J^4=I\) por sí sola.

Es la definición matemática precisa de "un cierre estable que sigue siendo válido al ampliar la capa".

---

# 17. Qué hueco queda realmente

El hueco de **herencia entre capas** queda cerrado en la realización \(J\)-invariante.

Ya no hace falta preguntar:

> ¿cómo mete la nueva identidad toda la historia anterior dentro de sí?

La respuesta es:

\[
\boxed{
\text{no la mete;}
\quad
\text{la capa anterior permanece incluida en la nueva.}
}
\]

El problema restante es más específico:

\[
\boxed{
\text{¿qué cierres físicos son suficientemente estables
para satisfacer la compatibilidad de herencia cuando interactúan?}
}
\]

Eso requiere dinámica o un criterio de estabilidad física.

No es un problema de almacenamiento de información.

---

# 18. Cadena consolidada

\[
\boxed{
\begin{aligned}
L_k
&\xrightarrow{\text{reflexión}}
(i_kL_k,\;N_{k+1})\\
&\Rightarrow
L_{k+1}=i_kL_k\oplus N_{k+1}\\
&\Rightarrow
p_ki_k=I\\
&\Rightarrow
\text{herencia sin pérdida}\\
&\Rightarrow
J_{k+1}i_k=i_kJ_k\\
&\Rightarrow
J_k^4=I
\Longrightarrow
J_{k+1}^4i_k=i_k\\
&\Rightarrow
\text{el cierre anterior persiste como referencia}\\
&\Rightarrow
\text{la novedad vive sólo en }L_{k+1}/L_k.
\end{aligned}
}
\]

La autorrecurrencia queda así formalizada como **extensión de capa**, no como reinicio ni como copia total de la historia.
