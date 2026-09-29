# Γ: selección endógena de referencia desde la frontera relacional
## Experimento v0.80

**Programa de Geometría Relacional**  
**Autor:** Le Matt Ansatz Di Ego  
**Estatus:** heurística estructural + controles exactos. No resuelve \(P\) vs \(NP\).

# 1. Pregunta

v0.79 localizó el problema:

\[
\boxed{
\text{cuando aparece una quinta función residual inequivalente,
¿puede esa novedad indicar qué referencia abrir?}
}
\]

El objetivo de v0.80 es construir el primer operador candidato:

\[
\Gamma
\]

sin consultar soluciones y sin probar órdenes completos.

# 2. Representación exacta de cápsulas

Para un orden de variables \(\pi\), dos prefijos están en la misma cápsula si inducen la misma función residual futura:

\[
\alpha\sim_k\beta
\iff
F_\alpha=F_\beta.
\]

El ancho exacto en el corte \(k\) es:

\[
W_\pi(k).
\]

El mejor orden posible para una fórmula pequeña se obtiene por programación dinámica exacta sobre subconjuntos:

\[
\operatorname{OPT}(F)
=
\min_\pi\max_k W_\pi(k).
\]

Este óptimo se usa únicamente como oráculo de laboratorio para evaluar \(\Gamma\). No forma parte del algoritmo propuesto.

# 3. Qué información usa Γ

\(\Gamma\) ve sólo la arquitectura de restricciones:

- qué variables participan en cada relación/cláusula;
- qué relaciones ya están totalmente dentro del marco elegido;
- cuáles cruzan la frontera;
- qué variables externas mantienen abiertas esas relaciones.

No mira:

- asignaciones satisfactorias;
- la tabla de verdad;
- el ancho residual exacto;
- el orden óptimo.

# 4. Regla Γ₀

Sea \(S\) el conjunto de referencias ya incorporadas.

Una relación \(e\) está abierta si:

\[
e\cap S\neq\varnothing
\quad\text{y}\quad
e\setminus S\neq\varnothing.
\]

La frontera exterior es:

\[
\partial^+S
=
\bigcup_{e\text{ abierta}}(e\setminus S).
\]

## Semilla

Si \(S=\varnothing\), se toma una variable de participación máxima.

## Actualización

Si existe frontera, cada candidato \(v\in\partial^+S\) se evalúa por:

1. tamaño de la nueva frontera exterior;
2. número de relaciones que seguirán cruzadas;
3. balance relaciones abiertas menos relaciones cerradas;
4. número de relaciones cerradas por \(v\);
5. número de relaciones activas a las que \(v\) pertenece.

\(\Gamma_0\) selecciona lexicográficamente la opción de menor carga futura.

La interpretación es:

\[
\boxed{
\text{seguir la novedad que cierra más estructura
sin abrir una frontera mayor de la necesaria}.
}
\]

# 5. Complejidad de Γ₀

La regla puede evaluarse directamente desde las incidencias de la fórmula.

Una implementación ingenua cuesta a lo sumo un número polinómico de operaciones en:

\[
n
\quad\text{y}\quad
m.
\]

Por sí sola, por tanto, \(\Gamma_0\) no esconde una búsqueda sobre \(n!\) órdenes.

Esto no garantiza que encuentre un buen orden.

# 6. Control decisivo: igualdades permutadas

La familia:

\[
F_m=\bigwedge_i(x_i\leftrightarrow y_i)
\]

tenía un orden malo con ancho:

\[
2^m
\]

y un orden intercalado pequeño.

Ahora se permutaron las etiquetas para impedir que el algoritmo conozca de antemano las parejas.

\(\Gamma_0\) sólo ve la red de relaciones.

| control | óptimo exacto | \(\Gamma_0\) | grado estático | orden natural |
|---|---:|---:|---:|---:|
| permuted_equality n=4 | 3 | 3 | 4 | 4 |
| permuted_equality n=6 | 3 | 3 | 8 | 8 |
| permuted_equality n=8 | 3 | 3 | 5 | 5 |
| permuted_equality n=10 | 3 | 3 | 32 | 32 |
| permuted_implication_chain n=6 | 3 | 3 | 4 | 4 |
| permuted_implication_chain n=8 | 3 | 4 | 5 | 5 |
| permuted_implication_chain n=10 | 3 | 3 | 5 | 6 |

En esta familia, \(\Gamma_0\) recupera la estructura local de las parejas desde las relaciones mismas. El punto no es que resuelva un problema difícil —la familia es fácil— sino que satisface el control conceptual:

\[
\boxed{
\text{una diferencia abierta puede señalar la referencia que la cierra}.
}
\]

# 7. Estrés exacto en 3-CNF pequeñas

Se generaron 24 fórmulas 3-CNF satisfacibles plantadas, con tamaños \(n=6,\ldots,9\). Para cada una:

- se calculó \(\operatorname{OPT}(F)\) exactamente;
- se aplicó \(\Gamma_0\);
- se comparó con grado estático;
- orden natural;
- 24 órdenes aleatorios.

| \(n\) | instancias | mediana OPT | mediana \(\Gamma_0\) | grado | natural | aleatoria | razón mediana \(\Gamma_0/\mathrm{OPT}\) | \(\Gamma_0\) óptimo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 6 | 2.0 | 2.5 | 2.5 | 2.5 | 2.5 | 1.00 | 5/6 |
| 7 | 6 | 3.0 | 4.0 | 4.0 | 3.5 | 4.0 | 1.17 | 3/6 |
| 8 | 6 | 3.5 | 3.5 | 4.0 | 4.0 | 4.0 | 1.00 | 5/6 |
| 9 | 6 | 3.0 | 4.0 | 4.0 | 4.0 | 4.0 | 1.33 | 1/6 |

Estos tamaños son demasiado pequeños para inferir complejidad asintótica.

# 8. Qué aprendimos

## Resultado positivo

Existe al menos un operador puramente relacional, polinómico y sin acceso a soluciones que recupera automáticamente la buena referencia en controles donde la estructura correcta está localmente expuesta.

Esto convierte la idea de “quinta novedad \(\to\) nueva referencia” en un algoritmo definido.

## Resultado negativo

En 3-CNF generales pequeñas, \(\Gamma_0\) no coincide siempre con el orden óptimo.

Por tanto:

\[
\boxed{
\text{frontera local}
\not\Rightarrow
\text{referencia global óptima}.
}
\]

La información necesaria puede estar distribuida más allá del vecindario inmediato.

# 9. Interpretación desde el programa

La quinta novedad sí contiene información:

- revela qué relaciones permanecen abiertas;
- identifica qué referencias podrían cerrarlas;
- permite una decisión local no arbitraria.

Pero no hemos demostrado que esa información sea suficiente para decidir la mejor ampliación global.

Así debemos distinguir:

\[
\boxed{
\text{novedad local}
\neq
\text{suficiencia predictiva global}.
}
\]

# 10. Nuevo objeto: horizonte de referencia

Esto sugiere ampliar \(\Gamma_0\).

Sea:

\[
H_r(S)
\]

el subgrafo/subhipergrafo relacional visible a distancia \(r\) de la frontera.

Definimos una familia:

\[
\Gamma_r
\]

que elige la siguiente referencia usando sólo \(H_r(S)\).

Entonces la pregunta se vuelve cuantitativa:

\[
\boxed{
\text{¿existe un }r=\operatorname{polylog}(n)
\text{ o constante que mantenga pequeño el ancho para toda 3-SAT?}
}
\]

Si requiere:

\[
r=\Theta(n)
\]

y explorar combinaciones exponenciales dentro de ese horizonte, la economía se pierde.

# 11. Teorema condicional actualizado

Si existe una familia uniforme \(\Gamma_r\) tal que para toda 3-CNF de tamaño \(N\):

1. \(r\le\operatorname{polylog}N\) o el costo total de consulta es polinómico;
2. cada elección se computa en tiempo polinómico;
3. el ancho de cápsulas inducido satisface:
   \[
   W_{\Gamma_r}^{\max}(F)\le\operatorname{poly}(N);
   \]
4. la representación de cada cápsula y su frontera es polinómica;
5. las equivalencias/fusiones se acreditan en tiempo polinómico;
6. el número de actualizaciones es polinómico;

entonces:

\[
\boxed{3\text{-SAT}\in P}
\]

y por tanto:

\[
\boxed{P=NP}.
\]

La existencia de tal familia continúa abierta.

# 12. Falsador directo para la ruta

La vía “quinta novedad elige referencia” falla como estrategia general si existe una familia explícita \(F_n\) tal que, para toda regla de horizonte acotado de la clase declarada:

\[
W_{\Gamma_r}^{\max}(F_n)
=
2^{\Omega(n)}
\]

o la regla debe explorar exponencialmente muchas alternativas para evitar ese ancho.

Ese es ahora un falsador mucho más nítido que simplemente encontrar una instancia difícil.

# 13. Próximo paso

Hay dos direcciones.

## A. Fortalecer Γ sin oráculo

Construir:

\[
\Gamma_1,\Gamma_2,\ldots
\]

con horizonte relacional creciente y medir cuánto conocimiento hace falta para aproximar el orden óptimo.

## B. Buscar una familia adversarial

Diseñar fórmulas donde todos los vecindarios locales parezcan equivalentes, pero sólo una organización global evita ancho exponencial.

Si tal familia existe para cualquier horizonte pequeño, tendremos localizado exactamente dónde la incertidumbre local deja de contener información suficiente sobre el futuro.

# 14. Posición actual

La investigación ha avanzado de:

\[
\text{“quizá el cierre evita }2^n\text{”}
\]

a:

\[
\boxed{
\text{“¿cuánta información relacional debe observarse para elegir
una referencia que mantenga polinómica la representación futura?”}
}
\]

Ésta es una pregunta matemática concreta y falsable.

No es todavía una resolución de \(P\) vs \(NP\).
