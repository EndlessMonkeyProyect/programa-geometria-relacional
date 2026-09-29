# Composición recursiva de cápsulas cerradas
## La diferencia entre cierres como semilla de la capa siguiente
### Formalización v0.91

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estado:** cierre estructural candidato del mecanismo generativo interno.  
**No implica validación experimental ni derivación completa de las fuerzas físicas.**

---

# 0. Resultado central

Las versiones anteriores dejaron abierto:

\[
\boxed{
\text{¿cómo se componen dos o más cápsulas cerradas
para generar la arquitectura de la capa siguiente?}
}
\]

La respuesta propuesta aquí es mínima:

\[
\boxed{
\text{los cierres no se “multiplican” directamente;}
\quad
\text{se compara su diferencia.}
}
\]

Si esa diferencia ya cabe en la capa existente, no aparece estructura nueva.

Si es irreducible respecto de la capa actual, la diferencia se convierte en un nuevo marcador relacional y la misma regla de reflexión vuelve a actuar sobre ella.

Así:

\[
\boxed{
\text{cierre}
\to
\text{interfaz}
\to
\text{comparación}
\to
\text{residuo irreducible}
\to
\text{reflexión}
\to
\text{nuevo cierre}.
}
\]

---

# 1. La cápsula elemental

Para una referencia no nula \(A\) y un operador normalizado \(J\) con

\[
J^2=-I,
\]

la cápsula elemental es

\[
\mathcal K(A;J)
=
\{A,JA,-A,-JA\}.
\]

La secuencia completa es

\[
\boxed{
\underbrace{A}_{1}
\to
\underbrace{JA}_{2}
\to
\underbrace{-A}_{3}
\to
\underbrace{-JA}_{4}
\to
\underbrace{A}_{5\equiv1}.
}
\]

Por tanto:

- existen cuatro estados distintos;
- la quinta ocurrencia no es un quinto estado;
- la quinta ocurrencia certifica el retorno.

En este sentido preciso:

\[
\boxed{
5=\text{evento de cierre del ciclo de cuatro, no quinta identidad independiente}.
}
\]

---

# 2. El círculo de fase

En el plano real

\[
W_A=\operatorname{span}_{\mathbb R}\{A,JA\},
\]

normalicemos \(\|A\|=1\).

El operador

\[
e^{\theta J}
=
\cos\theta\,I+\sin\theta\,J
\]

genera el círculo de fase.

La cápsula discreta selecciona:

\[
\theta
\in
\left\{
0,\frac{\pi}{2},\pi,\frac{3\pi}{2}
\right\}.
\]

Así la imagen geométrica correcta es:

- un círculo de radio uno en el plano \(A,JA\);
- cuatro posiciones discretas separadas por cuartos de vuelta;
- la siguiente aplicación vuelve a la primera posición.

Una quinta identidad geométricamente distinta en el mismo círculo exige un ángulo adicional \(\theta\) que el generador discreto no contenía.

Ese ángulo es información nueva.

---

# 3. El cierre se convierte en interfaz

Sea

\[
\mathcal K_i^{(k)}
\]

una cápsula cerrada en la capa \(k\).

No borramos su estructura interna.

Definimos una interfaz:

\[
x_i^{(k)}
=
S_k(\mathcal K_i^{(k)}),
\]

donde \(S_k\) conserva exactamente los invariantes que el nivel superior necesita.

La capa anterior permanece como soporte.

Así:

\[
\boxed{
\text{cierre interno}
\neq
\text{pérdida de información}.
}
\]

El nivel superior utiliza \(x_i^{(k)}\) como una nueva referencia sin tener que reabrir cada estado interno.

---

# 4. Comparación de dos cierres

Sean dos interfaces cerradas:

\[
x_i^{(k)},\qquad x_j^{(k)}.
\]

Primero deben expresarse en una referencia común mediante un transporte admisible \(T_{ij}\).

Definimos su diferencia relacional:

\[
\boxed{
d_{ij}^{(k)}
=
x_j^{(k)}
-
T_{ij}x_i^{(k)}.
}
\]

Esta diferencia no se interpreta todavía como distancia física.

Es la información necesaria para distinguir ambas interfaces dentro del marco común.

---

# 5. Novedad versus redundancia

Sea \(P_k\) la proyección sobre la información ya representable por la capa.

Definimos el residuo:

\[
\boxed{
q_{ij}^{(k)}
=
(I-P_k)d_{ij}^{(k)}.
}
\]

Entonces:

### Relación redundante

\[
q_{ij}^{(k)}=0.
\]

La comparación puede reconstruirse desde información que la capa ya posee.

No abre una nueva dirección.

### Relación irreducible

\[
q_{ij}^{(k)}\neq0.
\]

La comparación contiene información que no factoriza por la arquitectura existente.

Ésta es la semilla de la capa siguiente.

---

# 6. Regla de composición

La composición mínima de dos cierres se define por:

\[
\boxed{
\mathcal K_i^{(k)}
\star
\mathcal K_j^{(k)}
:=
q_{ij}^{(k)}.
}
\]

No es un producto algebraico convencional.

Es la extracción de la **diferencia irreducible entre sus interfaces**.

Si:

\[
q_{ij}^{(k)}=0,
\]

la composición no genera novedad.

Si:

\[
q_{ij}^{(k)}\neq0,
\]

se introduce el nuevo marcador:

\[
R_{ij}^{(k+1)}
:=
\frac{q_{ij}^{(k)}}{\|q_{ij}^{(k)}\|}
\]

cuando la normalización está definida.

La magnitud

\[
\rho_{ij}^{(k+1)}
=
\|q_{ij}^{(k)}\|
\]

conserva cuánto residuo había.

---

# 7. Reflexión de la relación

Aquí entra la autorrecurrencia.

La nueva diferencia no requiere una ley distinta.

La misma arquitectura generativa se aplica de nuevo:

\[
\boxed{
U_{ij}^{(k+1)}
=
x_i^{(k)}\times R_{ij}^{(k+1)}.
}
\]

Normalizando:

\[
J_{k+1}^2=-I,
\]

y por tanto:

\[
J_{k+1}^4=I.
\]

La relación entre dos cierres genera entonces su propia cápsula:

\[
\boxed{
\mathcal K_{ij}^{(k+1)}
=
\{
q_{ij},
J_{k+1}q_{ij},
-q_{ij},
-J_{k+1}q_{ij}
\}.
}
\]

Esto formaliza:

\[
\boxed{
\text{una relación puede convertirse en nueva identidad cerrada}.
}
\]

---

# 8. El origen formal de la nueva perpendicular

La documentación temprana del programa afirmaba que la interacción entre límites proyectados de dos partículas generaba información en un vector perpendicular.

La presente formulación recupera esa intuición sin asumir todavía una fuerza física:

\[
q_{ij}
\]

es la diferencia entre cierres.

Su primera reflexión transversal es:

\[
\boxed{
Jq_{ij}.
}
\]

Y:

\[
\langle q_{ij},Jq_{ij}\rangle=0.
\]

Por tanto la nueva perpendicular no se agrega arbitrariamente.

Es la consecuencia de aplicar al residuo relacional la misma estructura \(J\) que gobierna la reflexión elemental.

---

# 9. El papel de \(a\)

El antiguo modo:

\[
a=V\times R
\]

puede ahora leerse como un caso temprano de la regla general:

\[
\boxed{
\text{reflexionar una relación ya generada produce
un nuevo grado de ajuste perpendicular}.
}
\]

No se afirma todavía:

\[
a=F.
\]

La interpretación defendible es:

\[
\boxed{
a=\text{modo generativo de reconfiguración transversal}.
}
\]

Sólo una calibración dinámica posterior podría convertir un modo de este tipo en una aceleración física.

---

# 10. Regla recursiva por capas

La arquitectura completa puede escribirse:

\[
\boxed{
\begin{aligned}
\mathcal K^{(k)}
&\xrightarrow{S_k}
x^{(k)}
\\
(x_i^{(k)},x_j^{(k)})
&\xrightarrow{\text{comparación}}
d_{ij}^{(k)}
\\
d_{ij}^{(k)}
&\xrightarrow{I-P_k}
q_{ij}^{(k)}
\\
q_{ij}^{(k)}\neq0
&\xrightarrow{\text{reflexión}}
\mathcal K_{ij}^{(k+1)}
\\
\mathcal K_{ij}^{(k+1)}
&\xrightarrow{\text{cierre}}
x_{ij}^{(k+1)}.
\end{aligned}
}
\]

Y el proceso puede repetirse.

Esta es la autorrecurrencia generativa.

---

# 11. Dónde se almacena la información

La interfaz superior no sustituye a la estructura inferior.

El estado completo debe entenderse como una torre:

\[
L_0
\hookrightarrow
L_1
\hookrightarrow
L_2
\hookrightarrow\cdots.
\]

La nueva capa contiene:

\[
L_{k+1}
=
L_k\oplus N_{k+1}
\]

en la realización ortogonal.

Así la información nueva se almacena en:

\[
N_{k+1},
\]

mientras:

\[
L_k
\]

permanece como la circunstancia heredada.

Esto realiza exactamente:

\[
\boxed{
\text{la nueva reflexión guarda la novedad;
la capa heredada guarda la circunstancia}.
}
\]

---

# 12. Cuatro cierres en una nueva cápsula

Para que el mismo mecanismo sea auto-semejante a otra escala, se adopta el principio:

> **Una vez que las interfaces de una capa son tomadas como nuevas referencias, la misma ley normalizada de reflexión se aplica entre ellas.**

Entonces una referencia superior \(X\) genera:

\[
X,\quad
J_{k+1}X,\quad
-X,\quad
-J_{k+1}X,
\]

y vuelve a:

\[
X.
\]

Así la regla de cuatro no tiene que postularse por separado en cada escala.

Se reutiliza la misma condición:

\[
\boxed{
J_{k+1}^2=-I.
}
\]

La auto-semejanza de capas es, por tanto, la repetición del mismo tipo de reflexión sobre nuevas referencias.

---

# 13. Qué significa el quinto elemento en la capa superior

Si contamos ocurrencias:

\[
1\to2\to3\to4\to1.
\]

La quinta ocurrencia vuelve a la referencia y certifica cierre.

Si aparece una identidad **realmente distinta** \(B\) después de esos cuatro roles, entonces:

\[
B\notin
\{X,JX,-X,-JX\}.
\]

Por tanto exige información adicional.

Así distinguimos dos sentidos de “cinco”:

\[
\boxed{
5_{\rm ciclo}
=
1_{\rm retorno}
}
\]

y

\[
\boxed{
5_{\rm identidad}
=
\text{novedad externa a la cápsula}.
}
\]

Esta distinción evita una ambigüedad importante del lenguaje informal.

---

# 14. Vínculo entre cápsulas como fase relativa

Si dos cápsulas comparten el mismo tipo de reflexión, una relación entre ellas puede contener una fase relativa:

\[
g_{ij}\in C_4.
\]

Con:

\[
g_{ij}=J^{n_{ij}},
\qquad
n_{ij}\in\mathbb Z_4.
\]

La composición de relaciones sigue la ley del grupo:

\[
\boxed{
g_{ik}
=
g_{jk}g_{ij}.
}
\]

Por tanto las relaciones entre cápsulas no necesitan una regla arbitraria para su orientación.

La fase relativa compone modularmente.

---

# 15. Holonomía: cuándo una red de relaciones cierra

Considérese un ciclo de cápsulas:

\[
i_0\to i_1\to\cdots\to i_m=i_0.
\]

Definimos:

\[
\boxed{
\Omega_\gamma
=
g_{i_{m-1}i_m}
\cdots
g_{i_0i_1}.
}
\]

Si:

\[
\Omega_\gamma=I,
\]

las referencias relativas pueden integrarse sin residuo de fase.

Si:

\[
\Omega_\gamma\neq I,
\]

el ciclo contiene una diferencia relacional que no puede eliminarse mediante cambios locales de referencia.

Así:

\[
\boxed{
\text{holonomía no trivial}
=
\text{información relacional cerrada alrededor de un ciclo}.
}
\]

Esto da un candidato matemático preciso para “información que queda almacenada en la relación”.

No se identifica todavía con una fuerza o carga física.

---

# 16. Relación con el operador dinámico

Una vez definidas las comparaciones activas, el operador de incidencia \(\partial_k\) se construye directamente de ellas.

El defecto de cierre es:

\[
\mathcal D_k
=
\frac12\|\partial_k x\|^2.
\]

Y bajo corrección mínima:

\[
\boxed{
\Gamma_k
=
\kappa\partial_k^\ast\partial_k.
}
\]

Por tanto la cadena queda:

\[
\boxed{
\text{cierres}
\to
\text{diferencias}
\to
\text{incidencia}
\to
\Gamma
\to
\text{reorganización}.
}
\]

La dinámica se apoya en la composición de cierres, no en un operador impuesto desde afuera.

---

# 17. Correspondencia con enlaces

Una interacción estable entre dos identidades puede explorarse como un caso donde la relación entre ellas cierra en una cápsula conjunta.

Formalmente:

\[
q_{AB}\neq0
\]

genera una estructura nueva.

Si esa estructura alcanza cierre:

\[
J^4 q_{AB}=q_{AB},
\]

la relación puede persistir como identidad del compuesto.

Esto ofrece una formulación para:

\[
\boxed{
\text{enlace}
=
\text{relación que adquiere cierre propio}.
}
\]

El enlace covalente es sólo un posible banco de pruebas físico de esta estructura.

No queda derivado por esta matemática.

---

# 18. Materialidad

Con la regla recursiva, la materialidad puede afinarse:

\[
\boxed{
\text{materialidad}
=
\text{persistencia de cierres y de sus relaciones
a través de la torre de capas}.
}
\]

No basta con que una diferencia cierre una vez.

Debe conservar una interfaz suficiente mientras participa en cierres superiores.

Esto distingue:

- identidad local;
- relación cerrada;
- materialidad persistente.

---

# 19. Estatuto del resultado

## Derivado dentro de las hipótesis adoptadas

- cuatro estados distintos bajo un único \(J\);
- quinta ocurrencia = retorno;
- diferencia entre interfaces;
- residuo respecto de una capa;
- perpendicularidad de \(q\) y \(Jq\);
- composición de fases relativas por \(C_4\);
- holonomía de ciclos;
- Laplaciano/incidencia una vez declaradas las relaciones.

## Principio estructural adoptado

- una cápsula cerrada puede actuar como referencia de la siguiente capa;
- la misma ley normalizada \(J^2=-I\) se reutiliza sobre referencias de nivel superior.

Este principio expresa la auto-semejanza que el programa propone.

No se deriva del álgebra de una sola capa por sí sola.

---

# 20. Qué queda abierto

El hueco estructural se ha reducido a:

1. **Accesibilidad física:** qué comparaciones entre cápsulas llegan a activarse físicamente.
2. **Escala:** qué fija \(\kappa\) y la magnitud dimensional de una interacción.
3. **Tiempo:** cómo la profundidad/ritmo de actualización se convierte en una comparación temporal física.
4. **Selección física:** qué cierres corresponden a partículas, enlaces o sectores de fuerza concretos.
5. **Independencia binaria:** por qué los cuatro roles admiten el libro completo \(2^4\) en los sectores donde aparece \(1:15\).

La **composición algebraica de cierres** ya tiene una regla explícita.

---

# 21. Síntesis final

La estructura completa puede resumirse:

\[
\boxed{
\text{unidad}
\to
\text{diferencia}
\to
\text{reflexión}
\to
4\text{ roles}
\to
\text{retorno/cierre}
}
\]

\[
\boxed{
\text{cierre}
\to
\text{interfaz}
\to
\text{comparación con otro cierre}
\to
q
}
\]

\[
\boxed{
q=0
\Rightarrow
\text{sin novedad}
}
\]

\[
\boxed{
q\neq0
\Rightarrow
\text{nueva reflexión}
\to
4\text{ roles}
\to
\text{nuevo cierre}.
}
\]

Por tanto:

\[
\boxed{
\textbf{la relación entre cierres es la semilla de la siguiente capa.}
}
\]

Y la frase conceptual correspondiente es:

> **Una identidad cierra cuando su reflexión vuelve a sí misma. Dos identidades cerradas abren una nueva capa sólo en aquello que su comparación no puede resolver con la información ya heredada. Esa diferencia se refleja de nuevo, y el mismo mecanismo vuelve a cerrar.**

Ésta es la composición recursiva mínima del programa.
