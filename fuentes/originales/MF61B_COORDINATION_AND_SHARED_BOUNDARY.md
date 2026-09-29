# MF-61B — Coordinación entre cierres y frontera compartida

**Versión:** v0.69-research  
**Rama:** complejidad / geometría relacional de restricciones.  
**Nota:** MF-61B evita colisión con numeración histórica.

## 1. Motivación

MF-60B mostró que Horn, XOR y 2-SAT poseen cierres acreditables eficientes dentro de sus propios lenguajes.

El siguiente problema es composicional:

\[
\boxed{
\text{¿qué ocurre cuando cierres localmente simples deben coordinarse?}
}
\]

La primera observación es un no-go muy fuerte para cualquier explicación basada sólo en dificultad local.

Toda 3-CNF:

\[
F=C_1\land\cdots\land C_m
\]

es una conjunción de cláusulas individuales.

Cada cláusula aislada es una relación booleana de aridad tres con sólo siete asignaciones permitidas y su satisfacibilidad es trivial.

Sin embargo decidir la conjunción general es 3-SAT.

Por tanto:

\[
\boxed{
\text{facilidad local de todos los componentes}
\not\Rightarrow
\text{facilidad global de su composición}.
}
\]

La dificultad puede residir enteramente en la coordinación.

## 2. Dos cierres con una frontera común

Escriba:

\[
F_A(X,S)
\]

y:

\[
F_B(S,Y),
\]

donde:

- \(X\) son variables internas de \(A\);
- \(Y\) son variables internas de \(B\);
- \(S\) es la frontera compartida.

Defina el soporte de frontera de \(A\):

\[
\boxed{
B_A
=
\{s\in\{0,1\}^{S}:
\exists x\,F_A(x,s)\}.
}
\]

Y análogamente:

\[
\boxed{
B_B
=
\{s:
\exists y\,F_B(s,y)\}.
}
\]

## 3. Teorema MF-61B-A — criterio exacto de composición

Se cumple:

\[
\boxed{
F_A\land F_B\text{ es SAT}
\iff
B_A\cap B_B\neq\varnothing.
}
\]

### Prueba

Si \(F_A\land F_B\) tiene un modelo global, su restricción a \(S\) pertenece a ambos soportes.

Recíprocamente, si existe \(s\in B_A\cap B_B\), por definición existe una extensión \(x\) que satisface \(F_A\) y una extensión \(y\) que satisface \(F_B\). Como sus únicas variables comunes son \(S\), ambas extensiones pueden unirse en una asignación global.

QED.

La interacción entre los cierres queda reducida exactamente a una pregunta sobre la frontera.

## 4. La frontera como estado suficiente

La función:

\[
\chi_A(s)
=
\mathbf 1[\exists x\,F_A(x,s)]
\]

es un estado suficiente de \(A\) para cualquier futuro que sólo pueda interactuar con \(A\) a través de \(S\).

Ésta es la misma idea de MF-54:

\[
\boxed{
\text{el interior puede olvidarse si la frontera conserva todas las diferencias futuras relevantes}.
}
\]

Pero ahora el objeto aparece directamente en 3-SAT como proyección existencial.

## 5. Dónde reaparece el costo

Si:

\[
|S|=k,
\]

una tabla explícita de frontera posee hasta:

\[
2^k
\]

entradas.

Esto no es una cota inferior universal sobre toda representación posible: algunas fronteras admiten compresión algebraica.

Sí es el costo natural de una representación tabular exacta.

Por tanto:

\[
\boxed{
\text{frontera semánticamente suficiente}
\not\Rightarrow
\text{frontera económicamente representable}.
}
\]

## 6. Eliminación relacional exacta

Cada cláusula se representa como una pequeña relación sobre sus variables.

Para eliminar una variable:

1. se unen las relaciones que la contienen;
2. se proyecta existencialmente la variable eliminada;
3. la relación resultante queda como nueva frontera.

Es exactamente:

\[
\boxed{
\text{join}
\rightarrow
\text{projection}
\rightarrow
\text{new boundary}.
}
\]

No se introduce aproximación.

## 7. Ancho de coordinación

Para un orden de eliminación \(\pi\), defina:

\[
w_\pi
=
\max_t(|S_t|-1),
\]

donde \(S_t\) es el mayor alcance relacional que debe coordinarse en el paso \(t\).

El mejor valor:

\[
w_*(F)=\min_\pi w_\pi
\]

corresponde, salvo convenciones, al ancho inducido/treewidth del grafo primal.

**No se presenta como un invariante nuevo.**

Su importancia para el programa es interpretativa:

\[
\boxed{
w
=
\text{cantidad máxima de referencias que deben permanecer coordinadas simultáneamente
en esta estrategia de eliminación}.
}
\]

Para una representación tabular booleana, el costo es del orden de:

\[
\operatorname{poly}(n,m)\,2^{O(w)}.
\]

Por tanto un ancho acotado da un régimen tratable para esta arquitectura.

## 8. Resultado experimental

Se implementó eliminación relacional exacta por join/projection y se comparó contra fuerza bruta.

Se probaron dos familias con cláusulas locales del mismo tamaño:

- cadenas locales de cláusulas sobre triples consecutivos;
- fórmulas densas aleatorias con triples distribuidos globalmente.

En ambos casos cada cláusula inicial tiene aridad tres.

La diferencia aparece sólo en la coordinación necesaria durante los merges.

Los resultados completos están en:

`results/computation/mf61b_elimination_samples.csv`

y:

`results/computation/mf61b_coordination_summary.json`.

## 9. Lectura fundamental

Esto elimina otra explicación insuficiente:

\[
\text{“3-SAT es difícil porque las cláusulas son complicadas.”}
\]

No.

Cada cláusula es trivialmente manejable.

La dificultad puede surgir de:

\[
\boxed{
\text{muchas relaciones simples}
+
\text{solapamiento global}
+
\text{necesidad de preservar compatibilidad futura}.
}
\]

En el lenguaje del programa:

\[
\boxed{
\text{complejidad}
\sim
\text{costo de mantener una frontera suficiente bajo coordinación}.
}
\]

Esto es una lectura estructural, no una nueva caracterización demostrada de NP.

## 10. Barrera de merge universal

Suponga una representación \(K(F)\) tal que:

1. cada cláusula individual produce una cápsula pequeña;
2. existe:
\[
\mathrm{Merge}(K(A),K(B))=K(A\land B)
\]
exacto y polinómico;
3. el tamaño permanece polinómico bajo una secuencia arbitraria de merges;
4. `Empty` es polinómico.

Entonces cualquier 3-CNF puede construirse uniendo sus cápsulas cláusula por cláusula y decidirse en tiempo polinómico.

Así:

\[
\boxed{
\text{merge exacto universal y económico}
\Rightarrow
P=NP.
}
\]

La composabilidad universal es, por tanto, justamente una de las cosas que no podemos asumir.

## 11. Conexión con MF-56

MF-56 separó:

\[
\text{estado local}
\]

de:

\[
\text{dependencia conjunta}.
\]

MF-61B muestra la versión computacional exacta.

Los cierres \(A\) y \(B\) pueden ser individualmente simples.

La dificultad aparece cuando debemos conservar:

\[
B_A\cap B_B.
\]

Es información que pertenece a la compatibilidad entre ambos, no a uno de ellos por separado.

## 12. Qué queda abierto

Todavía no tenemos una representación universal que supere la tabla \(2^k\).

Tampoco hemos probado que ninguna pueda hacerlo.

Quedan abiertas dos rutas:

1. encontrar una estructura algebraica no tabular que comprima fronteras amplias y siga siendo localmente actualizable;
2. demostrar que cualquier lenguaje candidato vuelve a sufrir explosión de tamaño, normalización o acreditación en alguna familia adversarial.

Ése es el próximo discriminante real.

## 13. Próximo paso

MF-62B debe ensayar una **frontera híbrida** que pueda elegir entre diferentes normalizaciones:

- implicacional;
- afín;
- tabular/residual.

La pregunta no será si cada una funciona en su dominio.

Será si existe una regla económica para cambiar de representación sin resolver implícitamente SAT durante la conversión.

Ese es el próximo punto donde la propuesta puede sobrevivir o colapsar.
