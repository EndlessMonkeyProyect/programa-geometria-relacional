# MF-44B — Normalización causal del cierre y separación profundidad–anchura
## Integración de MF-44 con P vs NP, Yang–Mills y la rama dinámica

**Programa de Geometría Relacional**  
**Autor:** Le Matt Ansatz Di Ego  
**Versión:** v1.0 — 4 de octubre de 2026  
**Estatus:** integración formal. No afirma solución de \(P=NP\), Yang–Mills ni Navier–Stokes.

---

# 0. Resultado ejecutivo

La búsqueda en el repositorio muestra que la idea de una tasa límite relacional **ya estaba formalizada** en MF-44 y en la inserción ontológica v0.12.

Para una red relacional con actualización local de radio uno:

\[
\boxed{
d_G(v,S)\le n
}
\]

es condición necesaria para que una diferencia inicialmente localizada en \(S\) pueda afectar \(v\) después de \(n\) actualizaciones.

Por tanto:

\[
\boxed{
c_{\rm rel}^{\max}=1
}
\]

en unidades de **una relación elemental por actualización**.

Esto es una **normalización causal relacional**, no una identificación con la velocidad física de la luz.

La novedad de esta nota no es MF-44A. La novedad es usar ese resultado como eje común para separar:

\[
\boxed{
\text{profundidad de propagación}
\neq
\text{anchura / ramificación / dificultad de cierre}
}
\]

y aplicar esa separación a las ramas P vs NP, Yang–Mills y dinámica continua.

---

# 1. Base exacta: MF-44A

Sea:

\[
G=(V,E)
\]

una red de cápsulas y relaciones.

Sea:

\[
d_G(i,j)
\]

la distancia mínima en número de relaciones elementales.

Considere una actualización local de radio uno:

\[
x_{i,n+1}
=
F_i
\left(
x_{i,n},
x_{i,n-1},
\{x_{j,n}:j\sim i\}
\right).
\]

Sean dos historias que inicialmente difieren sólo en:

\[
S\subseteq V.
\]

## Teorema 1 — Cono causal relacional

Después de \(n\) actualizaciones sólo pueden diferir en:

\[
\boxed{
B_n(S)
=
\{v\in V:d_G(v,S)\le n\}.
}
\]

### Demostración

Por inducción.

Para \(n=0\), la diferencia está contenida en \(S\).

Suponga que en el paso \(n\) la diferencia sólo puede encontrarse dentro de \(B_n(S)\).

En el paso \(n+1\), cada nodo consulta únicamente su propio estado y los estados de sus vecinos. Por tanto, una diferencia sólo puede alcanzar nodos adyacentes a \(B_n(S)\):

\[
B_{n+1}(S).
\]

Así:

\[
\operatorname{supp}\Delta x_n
\subseteq
B_n(S).
\]

\(\square\)

---

# 2. Normalización

Definimos la tasa causal relacional bruta:

\[
c_{\rm rel}^{\rm raw}
=
\sup
\frac{\Delta d_G}{\Delta n}.
\]

Para una regla de radio uno:

\[
\boxed{
c_{\rm rel}^{\rm raw}\le1.
}
\]

Cuando existe una dinámica que satura el frente:

\[
\boxed{
c_{\rm rel}^{\max}=1.
}
\]

Elegir:

\[
\Delta d_G=1,
\qquad
\Delta n=1
\]

como unidades elementales equivale a la normalización:

\[
\boxed{
c_{\rm rel}=1.
}
\]

Esto es análogo formalmente a trabajar con una constante límite fijada a uno, pero no identifica todavía:

\[
c_{\rm rel}
\]

con:

\[
c=299\,792\,458\ {\rm m/s}.
\]

Para eso se requiere un puente dimensional:

\[
x_{\rm phys}=\ell_0 d_G,
\qquad
t_{\rm phys}=\tau_0 n,
\]

y entonces:

\[
v_*=\frac{\ell_0}{\tau_0}.
\]

Sólo una derivación física adicional podría justificar:

\[
v_*=c.
\]

---

# 3. Generalización a radio local \(r\)

Si la regla puede consultar una bola de radio \(r\):

\[
x_{i,n+1}
=
F_i
\bigl(
\{x_{j,n}:d_G(i,j)\le r\},
\ldots
\bigr),
\]

entonces:

\[
\boxed{
d_G(v,S)\le rn.
}
\]

Por tanto:

\[
c_{\rm rel}^{\rm raw}\le r.
\]

Definiendo la unidad causal elemental como \(r\) enlaces:

\[
\tilde d=\frac{d_G}{r},
\]

se recupera:

\[
\boxed{
\tilde c_{\rm rel}=1.
}
\]

Así, \(c_{\rm rel}=1\) es una **normalización de la localidad declarada**, no un número físico absoluto.

---

# 4. Tiempo mínimo de acreditación causal

Sea \(Q_v\) una pregunta en el nodo \(v\) cuya respuesta depende de una diferencia inicialmente localizada en \(S\).

Entonces ningún procedimiento que respete estrictamente la localidad anterior puede acreditar el efecto de esa diferencia en \(v\) antes de:

\[
\boxed{
n_{\min}(v;S)
\ge
d_G(v,S).
}
\]

Para radio \(r\):

\[
\boxed{
n_{\min}(v;S)
\ge
\left\lceil
\frac{d_G(v,S)}{r}
\right\rceil.
}
\]

Este resultado es una cota inferior de profundidad causal.

No es una cota superior del tiempo de resolución.

---

# 5. Cierre global condicionado por propagación

Sea:

\[
\operatorname{ecc}(S)
=
\max_{v\in V}d_G(v,S).
\]

Si un cierre global requiere que una diferencia originada en \(S\) pueda influir causalmente en todos los nodos, entonces:

\[
\boxed{
n_{\rm global}
\ge
\operatorname{ecc}(S).
}
\]

Si la fuente puede estar en cualquier nodo y se requiere coordinación entre extremos:

\[
\boxed{
n_{\rm global}
\ge
\operatorname{diam}(G).
}
\]

## Corolario para grafos de diámetro infinito

Si:

\[
\operatorname{diam}(G)=\infty
\]

y \(S\) es finito, ninguna actualización local de radio finito puede propagar una diferencia desde \(S\) a todo \(G\) en un número finito de pasos.

Formalmente:

\[
\boxed{
\forall n<\infty,\qquad
B_n(S)\neq V.
}
\]

### Advertencia

Esto **no demuestra** que una totalidad infinita “nunca pueda estar cerrada” en cualquier sentido.

Sólo demuestra:

> una novedad localizada no puede producir sincronización causal global finita en una red de diámetro infinito bajo actualización local de radio finito.

Un cierre global impuesto por condiciones iniciales, invariantes globales o reglas no locales queda fuera de este teorema.

---

# 6. Distinción canónica: cierre local y cierre global

El cierre del programa es relativo a un contrato.

Por tanto pueden coexistir:

\[
\boxed{
\text{cierre local completo}
}
\]

y:

\[
\boxed{
\text{frontera global todavía abierta}.
}
\]

Esto no es contradicción.

Una cápsula puede satisfacer:

\[
\forall d\in\mathscr D_{\rm local},
\qquad
d=\bar d\circ\Phi,
\]

mientras una relación nueva entre cápsulas introduce una diferencia que no factoriza por la firma anterior.

Por tanto la cadena correcta es:

\[
\boxed{
\text{cierre local}
\to
\text{interfaz}
\to
\text{nueva relación}
\to
\text{nuevo frente causal}
\to
\text{recierre}.
}
\]

---

# 7. Nueva separación: profundidad frente a anchura

Definimos dos recursos diferentes.

## Profundidad causal

\[
\boxed{
D_{\rm caus}
=
\text{número mínimo de capas de actualización requeridas}
}
\]

para que una dependencia pueda recorrer la red.

## Anchura de cierre

\[
\boxed{
W_{\rm cl}
=
\text{cantidad/tamaño de compatibilidades simultáneas que deben mantenerse}
}
\]

durante la acreditación.

Una tasa causal normalizada puede fijar:

\[
D_{\rm caus}\gtrsim \operatorname{diam}(G),
\]

pero no controla:

\[
W_{\rm cl}.
\]

Por tanto:

\[
\boxed{
c_{\rm rel}=1
\not\Rightarrow
\text{economía global}.
}
\]

Éste es un NO-GO conceptual importante.

---

# 8. Consecuencia para P vs NP

Para una instancia finita 3-CNF de tamaño \(N\), cualquier grafo de incidencia explícito tiene diámetro como máximo lineal en el número de vértices:

\[
\operatorname{diam}(G)=O(N).
\]

Por tanto una limitación causal de una relación por actualización sólo produce una profundidad mínima como mucho polinómica en \(N\).

Así:

\[
\boxed{
\text{la profundidad de propagación por sí sola
no puede explicar una explosión exponencial}
}
\]

en una entrada explícita finita.

La dificultad restante debe residir en alguno de los recursos ya identificados:

\[
\boxed{
\text{anchura}
+
\text{ramificación}
+
\text{tamaño de interfaces}
+
\text{acreditación}
+
\text{selección del siguiente cierre}.
}
\]

Esto refuerza MF-63B.

El Lema de Descenso Acreditado no puede usar como potencial únicamente una distancia causal:

\[
\Delta=d_G.
\]

Aunque esa distancia descienda, no controla cuántas compatibilidades nuevas aparecen transversalmente.

## Discriminante más preciso

El potencial candidato debe separar al menos:

\[
\boxed{
\Delta_{\rm total}
=
(\text{profundidad acreditativa},
\text{anchura de compatibilidad})
}
\]

o una estructura equivalente bien fundada.

---

# 9. Consecuencia para Yang–Mills

La normalización causal proporciona un eje de **localidad/propagación**, pero no un eje espectral.

Por tanto:

\[
\boxed{
c_{\rm rel}=1
\not\Rightarrow
\text{mass gap}.
}
\]

Una teoría puede poseer una velocidad causal máxima y ser gapless.

El problema Yang–Mills sigue requiriendo una propiedad distinta:

\[
\boxed{
\operatorname{Var}(f)
\le
C_{\rm rel}\mathcal D_{\rm rel}[f].
}
\]

Es decir, no basta que las comparaciones puedan propagarse.

Debe demostrarse que ninguna diferencia gauge-invariante no constante puede escapar a todas ellas.

La nueva lectura es:

\[
\boxed{
\text{cono causal}
=
\text{hasta dónde puede llegar una comparación}
}
\]

mientras:

\[
\boxed{
\text{coercividad}
=
\text{si el conjunto de comparaciones alcanza para controlar toda diferencia global}.
}
\]

Son problemas ortogonales.

Esta separación evita confundir localidad relativista con gap espectral.

---

# 10. Consecuencia para Navier–Stokes

Aquí debe hacerse una separación todavía más estricta.

La ecuación de Navier–Stokes incomprensible contiene:

- difusión viscosa, de carácter parabólico;
- una presión obtenida mediante una restricción elíptica global.

Por tanto no es correcto identificar directamente:

\[
c_{\rm rel}=1
\]

con una velocidad física finita de propagación del campo Navier–Stokes continuo.

La normalización sólo puede usarse aquí como:

\[
\boxed{
\text{estructura de actualización/acreditación del modelo relacional}
}
\]

o como propiedad de un discretizado local declarado.

No como consecuencia física del PDE continuo.

## Lo útil para la rama

Los nuevos presupuestos DNS sugieren que un cierre local dinámico puede aparecer por cancelación entre términos grandes.

Por tanto la lectura compatible es:

\[
\boxed{
\text{cierre local}
=
\text{balance acreditado}
}
\]

y no:

\[
\boxed{
\text{cierre local}
=
\text{ausencia de dinámica}.
}
\]

La cuestión global de regularidad permanece separada.

---

# 11. Qué es realmente nuevo en esta integración

## No es nuevo

Ya estaban en el repositorio:

- la distancia relacional \(d_G\);
- el cono causal \(d_G\le n\);
- la cota \(v_{\rm rel}\le1\);
- la saturación del frente en dinámicas específicas;
- la advertencia de que no es todavía \(c\);
- el puente dimensional \(v_*=\ell_0/\tau_0\).

## Sí es una síntesis nueva

La lectura conjunta:

\[
\boxed{
\text{normalización causal}
\quad\perp\quad
\text{economía / coercividad / regularidad}
}
\]

y, en particular:

\[
\boxed{
\text{profundidad}
\neq
\text{anchura}.
}
\]

Esta separación produce un nuevo NO-GO para P vs NP:

> un límite causal lineal no puede, por sí solo, explicar ni resolver la complejidad exponencial; el frente debe buscarse en la multiplicidad de compatibilidades y en su acreditación.

Y produce un nuevo control conceptual para Yang–Mills:

> una velocidad límite relacional no puede sustituir la coercividad espectral.

---

# 12. Estado epistemológico

\[
\boxed{
\text{MF-44A: DERIVADO}
}
\]

\[
\boxed{
c_{\rm rel}=1:
\text{NORMALIZACIÓN bajo localidad de radio uno}
}
\]

\[
\boxed{
c_{\rm rel}\leftrightarrow c:
\text{PUENTE FÍSICO ABIERTO}
}
\]

\[
\boxed{
\text{cierre global infinito imposible en tiempo finito desde novedad localizada}:
\text{CONDICIONAL}
}
\]

\[
\boxed{
\text{profundidad}\neq\text{anchura}:
\text{DERIVADO como separación de recursos}
}
\]

\[
\boxed{
\text{aplicación P vs NP}:
\text{nuevo discriminante programático}
}
\]

\[
\boxed{
\text{aplicación Yang--Mills}:
\text{control conceptual, no prueba de gap}
}
\]

---

# 13. Falsadores

La formulación falla o debe modificarse si:

1. la actualización elemental permite dependencia instantánea fuera del radio declarado;
2. la red cambia de conectividad de forma que la métrica \(d_G\) usada no describe la dependencia real;
3. una regla global/nonlocal se introduce sin registrarla en el contrato;
4. se identifica \(c_{\rm rel}=1\) con \(c\) sin derivar \(\ell_0,\tau_0\);
5. se usa la cota causal para afirmar complejidad, mass gap o regularidad sin un teorema adicional.

---

# 14. Próximo paso útil

Para P vs NP, reemplazar el potencial escalar ingenuo por un objeto de dos ejes:

\[
\boxed{
\Delta_t
=
(D_t,W_t)
}
\]

donde:

\[
D_t
=
\text{profundidad causal/acreditativa pendiente},
\]

\[
W_t
=
\text{anchura de compatibilidad pendiente}.
\]

Buscar un orden bien fundado tal que:

\[
\Delta_{t+1}\prec\Delta_t
\]

con:

\[
D_t=O(N)
\]

ya controlado por localidad, dejando toda la carga difícil en demostrar:

\[
W_t=\operatorname{poly}(N)
\]

y que la política que lo reduce sea computable en tiempo polinómico.

Éste es ahora un blanco más preciso que un potencial escalar indiferenciado.
