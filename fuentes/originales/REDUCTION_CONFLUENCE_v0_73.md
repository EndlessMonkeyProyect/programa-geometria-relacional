# Regla de reducción, confluencia y retorno a la unidad
## Núcleo formal v0.73

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estatus:** formalización exploratoria. No constituye validación física.

## 1. Qué faltaba después de v0.72

v0.72 fijó:

\[
K_{\mathcal C}=\Omega/\sim_{\mathcal C},
\qquad
x\sim_{\mathcal C}y
\iff
\forall c\in\mathcal C,\ Q_c(x)=Q_c(y).
\]

Y demostró:

\[
K_{\varnothing}\cong\{T\}.
\]

Eso dice qué queda cuando no hay ninguna comparación capaz de distinguir. No dice qué operación elimina una diferencia, por qué ocurre, ni si toda trayectoria física llega a \(T\).

v0.73 separa esas preguntas.

## 2. Normalización no es desdiferenciación

Sea:

\[
q_{\mathcal C}:\Omega\to K_{\mathcal C}.
\]

Una comparación \(b\) es redundante si existe:

\[
\bar Q_b:K_{\mathcal C}\to Y_b
\]

tal que:

\[
Q_b=\bar Q_b\circ q_{\mathcal C}.
\]

Eliminar \(b\) en ese caso no cambia el cierre. Es una normalización descriptiva.

Una **reducción relacional real** requiere que estados antes distinguibles dejen de serlo. Formalmente:

\[
\rho:K\twoheadrightarrow K',
\qquad
|K'|<|K|.
\]

Si:

\[
I(K)=\log_2|K|,
\]

entonces:

\[
I(K')<I(K).
\]

Así:

\[
\boxed{
\text{normalización}
\neq
\text{desdiferenciación}.
}
\]

## 3. Reducción canónica respecto de un futuro

Sea \(\mathcal F\) una familia de futuros u observables que deben preservarse.

Definimos:

\[
x\equiv_{\mathcal F}y
\iff
\forall f\in\mathcal F,\ f(x)=f(y).
\]

El cociente:

\[
N_{\mathcal F}(K)=K/\equiv_{\mathcal F}
\]

es el estado mínimo exacto suficiente para todos los futuros de \(\mathcal F\).

Si una codificación:

\[
s:K\to S
\]

permite reconstruir todos los \(f\in\mathcal F\), entonces:

\[
s(x)=s(y)
\Rightarrow
x\equiv_{\mathcal F}y.
\]

Por tanto el cociente contextual es canónico hasta isomorfismo.

## 4. Retorno a uno

Si:

\[
\mathcal F=\varnothing,
\]

entonces:

\[
x\equiv_{\varnothing}y
\quad
\forall x,y,
\]

y:

\[
\boxed{
N_{\varnothing}(K)\cong\{T\}.
}
\]

Esto formaliza el retorno a una clase única de identidad.

Pero:

\[
\boxed{
\text{no es todavía una ley dinámica}.
}
\]

Dice cuál es el cierre si el contrato relacional llega a vacío. No demuestra que las relaciones físicas deban desaparecer.

## 5. Cadena de pérdida de comparaciones

Sea:

\[
\mathcal F_0
\supseteq
\mathcal F_1
\supseteq
\cdots
\supseteq
\mathcal F_m.
\]

Entonces existe una sobreyección canónica:

\[
K_{\mathcal F_t}
\twoheadrightarrow
K_{\mathcal F_{t+1}},
\]

y:

\[
|K_{\mathcal F_{t+1}}|
\le
|K_{\mathcal F_t}|.
\]

Así:

\[
\boxed{
I_{t+1}\le I_t.
}
\]

El índice \(t\) es sólo un paso de reescritura. No es todavía tiempo físico.

## 6. Confluencia extensional

Si distintas trayectorias eliminan comparaciones en órdenes diferentes pero terminan en la misma familia final:

\[
\mathcal F_*,
\]

el resultado semántico final es siempre:

\[
\boxed{
K_{\mathcal F_*}
=
K/\equiv_{\mathcal F_*}.
}
\]

Por tanto el endpoint extensional no depende del orden de eliminación.

Si todas las trayectorias terminan en:

\[
\mathcal F_*=\varnothing,
\]

todas terminan en:

\[
\boxed{T.}
\]

Ésta es la formulación matemática legítima de:

> independientemente de la trayectoria interior, el cierre final es uno.

## 7. Lo que esto no demuestra

No demuestra:

1. que las relaciones efectivas deban desaparecer;
2. que toda trayectoria admisible termine;
3. que el criterio de reducción sea local;
4. que el criterio sea físicamente correcto;
5. que el criterio sea computacionalmente económico.

Así:

\[
\boxed{
\text{confluencia del cociente}
\neq
\text{convergencia física a }T.
}
\]

## 8. Eliminar redundancias no lleva a \(T\)

Si sólo borramos relaciones reconstruibles desde las demás, entonces:

\[
K_{t+1}\cong K_t.
\]

La información real no disminuye.

Por tanto una teoría física del retorno requiere una operación distinta de la eliminación de redundancias.

## 9. No existe necesariamente una base relacional única

Considere:

\[
\begin{array}{c|cccc}
 & A&B&C&D\\
\hline
x_1&0&0&0&0\\
x_2&0&0&0&1\\
x_3&0&1&1&0\\
x_4&1&0&1&1
\end{array}
\]

El conjunto:

\[
\{C,D\}
\]

distingue las cuatro realizaciones y es minimal.

También:

\[
\{A,B,D\}
\]

distingue las cuatro y es minimal.

Pero sus tamaños son:

\[
2
\quad\text{y}\quad
3.
\]

Así una regla de “eliminar relaciones redundantes hasta quedar irredundante” puede terminar en representaciones mínimas por inclusión de tamaños distintos.

Por tanto:

\[
\boxed{
\text{irredundancia}
\not\Rightarrow
\text{base canónica}.
}
\]

La dependencia relacional general no posee automáticamente la estructura de intercambio de un espacio vectorial o matroide.

## 10. Contrato mínimo de una dinámica futura

Para producir verdadera desdiferenciación se necesita una operación:

\[
D:S\to S'.
\]

Debe especificar al menos:

### D1. Diferencia activa
Un criterio:

\[
\delta_r(S)>0
\]

para una relación activa \(r\).

### D2. Reducción
Una regla que produzca:

\[
\delta_r(S')<\delta_r(S)
\]

sin conocer de antemano el estado final.

### D3. Conservación
Un invariante:

\[
J(S')=J(S)
\]

si la totalidad debe conservar identidad.

### D4. Cierre local
Cuando:

\[
\delta_r=0,
\]

la relación deja de ser discriminante.

### D5. Terminal
Cuando:

\[
\delta_r=0
\quad
\forall r,
\]

debe resultar:

\[
K\cong\{T\}.
\]

Estas condiciones todavía no están derivadas físicamente.

## 11. Función informacional candidata

Una candidata es:

\[
L(S)=\log_2|K(S)|.
\]

Una dinámica de eliminación debería cumplir:

\[
L(S_{t+1})\le L(S_t).
\]

Si cada paso es estricto:

\[
L(S_{t+1})<L(S_t),
\]

hay monotonicidad, pero no necesariamente eficiencia.

Con:

\[
|K_0|=2^n,
\]

una dinámica que sólo elimine una clase por paso puede necesitar hasta:

\[
2^n-1
\]

pasos.

Así:

\[
\boxed{
\text{monotonicidad}
\not\Rightarrow
\text{polinomialidad}.
}
\]

## 12. Condición suficiente para una trayectoria polinómica

Si en cada paso no trivial:

\[
L(S_t)-L(S_{t+1})
\ge
\frac{1}{p(n)}
\]

para algún polinomio \(p\), y:

\[
L(S_0)\le n,
\]

entonces el número de pasos es a lo sumo:

\[
n\,p(n).
\]

En el caso fuerte:

\[
\Delta L\ge1,
\]

se necesitan como máximo \(n\) reducciones.

La dificultad restante es encontrar esos pasos de forma correcta y polinómica.

## 13. Conexión con P vs NP

Para SAT, una regla relacional necesitaría:

1. construir \(S_0(F)\) en tiempo polinómico;
2. aplicar \(D\) en tiempo polinómico;
3. preservar exactamente SAT/UNSAT;
4. disminuir una medida controlada;
5. usar un número polinómico de pasos;
6. terminar en un estado que permita decidir SAT/UNSAT.

Una forma normal única no basta.

\[
\boxed{
\text{forma normal única}
\not\Rightarrow
P=NP.
}
\]

El discriminante correcto es:

\[
\boxed{
\text{normalización exacta y económicamente construible}.
}
\]

## 14. Resultado principal

La frase “todo converge a uno” se separa en:

### A. Cierre lógico
\[
K_{\varnothing}\cong\{T\}.
\]

**DEMOSTRADO por definición.**

### B. Independencia del camino con contrato final fijo
\[
\mathcal F_*\text{ fijo}
\Rightarrow
K_{\mathcal F_*}\text{ único}.
\]

**DEMOSTRADO.**

### C. Toda dinámica física elimina finalmente todas las diferencias
\[
S\to^*\{T\}.
\]

**HIPÓTESIS ABIERTA.**

Confundir A o B con C produciría circularidad.

## 15. Tiempo

El orden de reescritura no debe identificarse con tiempo físico.

La tesis:

\[
\boxed{
\text{sin comparación no hay tiempo relacional interno}
}
\]

permanece coherente si el parámetro de la demostración se entiende como orden lógico/causal y no como duración.

## 16. Siguiente problema exacto

Ya existe un operador canónico de cierre:

\[
N_{\mathcal F}.
\]

Lo que falta es:

\[
\boxed{
\text{una ley que determine }
\mathcal F_t\to\mathcal F_{t+1}
\text{ o }
S_t\to S_{t+1}.
}
\]

La pregunta siguiente es:

> ¿puede esa ley derivarse de conservación de identidad y economía relacional, en vez de ser postulada arbitrariamente?
