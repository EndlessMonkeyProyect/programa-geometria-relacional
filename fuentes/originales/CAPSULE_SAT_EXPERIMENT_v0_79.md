# Cápsulas exactas y localización de la explosión combinatoria
## Experimento computacional v0.79

**Programa de Geometría Relacional**  
**Autor:** Le Matt Ansatz Di Ego  
**Estatus:** laboratorio matemático/computacional. No constituye una resolución de \(P\) vs \(NP\).

# 1. Pregunta

El núcleo v0.78 propone que una quinta diferencia genuinamente nueva no cabe en un cierre elemental de cuatro y exige una nueva referencia.

La pregunta computacional es:

\[
\boxed{
\text{¿una jerarquía de cierres de capacidad cuatro evita realmente }2^n
\text{ en SAT?}
}
\]

Para responder sin metáfora necesitamos una definición exacta de cápsula en una fórmula booleana.

# 2. Cápsula exacta de un prefijo

Sea:

\[
F(x_1,\ldots,x_n)
\]

una función booleana y sea:

\[
\pi=(v_1,\ldots,v_n)
\]

un orden de referencias.

Después de fijar los primeros \(k\) valores, una asignación parcial \(\alpha\) induce una función residual:

\[
F_\alpha(v_{k+1},\ldots,v_n).
\]

Definimos:

\[
\boxed{
\alpha\sim_k\beta
\iff
F_\alpha=F_\beta
\text{ como funciones sobre todas las continuaciones futuras}.
}
\]

Una cápsula es entonces una clase:

\[
[\alpha]_k.
\]

Esta definición es exacta: dos prefijos se fusionan sólo si ningún futuro posible puede distinguirlos respecto de la decisión final.

Definimos el ancho de cápsulas:

\[
\boxed{
W_\pi(k)
=
|\{F_\alpha:\alpha\in\{0,1\}^k\}|.
}
\]

Y:

\[
W_\pi^{\max}
=
\max_k W_\pi(k).
\]

# 3. Significado informacional

Si:

\[
W_\pi(k)\le4,
\]

una referencia/cápsula cuaternaria puede etiquetar todos los futuros inequivalentes de ese corte.

Cuando:

\[
W_\pi(k)\ge5,
\]

aparece literalmente una quinta función residual inequivalente.

Entonces, bajo el contrato de v0.78, debe abrirse al menos otra referencia o nivel de representación.

Esto convierte la “quinta imagen” en un objeto computacional exacto.

# 4. Teorema de conteo para una jerarquía explícita de aridad cuatro

Suponga que se representan explícitamente \(W\) futuros inequivalentes como hojas de un árbol cuya aridad máxima es cuatro.

Si \(I\) es el número de nodos internos, entonces:

\[
W\le 1+3I.
\]

Por tanto:

\[
\boxed{
I
\ge
\left\lceil\frac{W-1}{3}\right\rceil.
}
\]

Así:

\[
W=2^{\Omega(n)}
\]

implica tamaño explícito exponencial incluso usando cápsulas de cuatro.

La profundidad mínima sólo satisface:

\[
\boxed{
d_4
\ge
\lceil\log_4 W\rceil.
}
\]

Profundidad pequeña no significa representación total pequeña.

# 5. Control positivo: paridad

Para:

\[
x_1\oplus\cdots\oplus x_n=0,
\]

cualquier prefijo sólo necesita recordar la paridad acumulada.

Por tanto existen como máximo dos funciones residuales:

\[
\boxed{
W_\pi(k)\le2.
}
\]

En los controles exactos hasta \(n=12\) el ancho máximo fue siempre 2.

Esto representa una estructura donde la incertidumbre exponencial aparente:

\[
2^n
\]

se comprime exactamente a un solo bit de estado relacional.

Es el tipo de comportamiento que el programa busca.

# 6. Control estructurado: cadena de implicaciones

Para una cadena:

\[
x_1\Rightarrow x_2\Rightarrow\cdots\Rightarrow x_n,
\]

el estado residual también permanece pequeño.

La arquitectura local transporta sólo una cantidad limitada de información hacia el futuro.

# 7. Falsador mínimo de “capacidad cuatro implica compresión”

Considere:

\[
F_m
=
\bigwedge_{i=1}^m
(x_i\leftrightarrow y_i).
\]

Es una fórmula muy fácil: pertenece incluso a 2-SAT.

Use el orden:

\[
x_1,x_2,\ldots,x_m,
y_1,y_2,\ldots,y_m.
\]

Después de fijar todos los \(x_i\), cada una de las:

\[
2^m
\]

asignaciones exige una combinación distinta de valores futuros de los \(y_i\).

Por tanto:

\[
\boxed{
W_\pi(m)=2^m.
}
\]

La quinta función residual aparece ya cuando \(m=3\):

\[
2^3=8>4.
\]

Y el crecimiento continúa exponencialmente.

Pero con el orden intercalado:

\[
x_1,y_1,x_2,y_2,\ldots,
\]

el ancho permanece pequeño.

## Resultado

\[
\boxed{
\text{la explosión puede depender de cómo se eligen las referencias}.
}
\]

Esto es extremadamente importante para el programa.

No basta:

\[
\text{“cada cápsula cierra en cuatro”.}
\]

Hace falta una regla capaz de **descubrir una parametrización/referencia adecuada**.

# 8. Resultados exactos de la familia de igualdad

| \(m\) | variables | \(W\) en corte malo \(x|y\) | ancho máx. malo | ancho máx. intercalado | profundidad cuaternaria mala | nodos internos explícitos mín. |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 | 1 | 1 |
| 2 | 4 | 4 | 4 | 3 | 1 | 1 |
| 3 | 6 | 8 | 8 | 3 | 2 | 3 |
| 4 | 8 | 16 | 16 | 3 | 2 | 5 |
| 5 | 10 | 32 | 32 | 3 | 3 | 11 |
| 6 | 12 | 64 | 64 | 3 | 3 | 21 |
| 7 | 14 | 128 | 128 | 3 | 4 | 43 |
| 8 | 16 | 256 | 256 | 3 | 4 | 85 |

El crecimiento:

\[
W=2^m
\]

está verificado exactamente en esta familia para los tamaños calculados y se demuestra directamente por la forma de las restricciones.

# 9. Estrés con 3-CNF plantadas

También se generaron fórmulas 3-CNF satisfacibles con una solución plantada y aproximadamente:

\[
m=4.2n
\]

cláusulas.

Para cada instancia se midió el ancho exacto de cápsulas en:

- orden natural;
- 12 órdenes aleatorios;
- mejor orden observado entre esos controles.

| \(n\) | cláusulas | mediana natural | mediana mejor de 12 órdenes | mediana de órdenes aleatorios | máximo observado |
|---:|---:|---:|---:|---:|---:|
| 6 | 25 | 3.0 | 3.0 | 3.0 | 5 |
| 8 | 34 | 3.0 | 3.0 | 3.2 | 10 |
| 10 | 42 | 5.0 | 4.0 | 5.0 | 10 |
| 12 | 50 | 5.5 | 5.0 | 5.5 | 10 |

Estos datos son sólo un estrés finito. No establecen una cota asintótica para 3-SAT.

# 10. El punto exacto donde reaparece \(2^n\)

La explosión puede reaparecer en cuatro lugares distintos:

## A. Número de cápsulas

\[
W_\pi(k)
=
2^{\Omega(n)}.
\]

## B. Costo de descubrir el orden/referencia

Puede existir un orden pequeño, pero encontrarlo puede ser difícil.

## C. Frontera entre cápsulas

Aunque cada cápsula sea pequeña, la información conjunta entre ellas puede requerir una interfaz exponencial.

## D. Verificación de equivalencia

Decidir exactamente:

\[
F_\alpha=F_\beta
\]

puede ser tan difícil como una cuestión de implicación/equivalencia booleana.

Por tanto la explosión no desaparece automáticamente.

Puede **migrar**.

# 11. Relación con el núcleo de cuatro

El nuevo núcleo sigue siendo útil.

Nos permite formular la pregunta correcta:

> Cuando aparece la quinta función residual inequivalente, ¿puede el sistema descubrir una nueva referencia que factorice el problema sin enumerar todas las ramas?

Eso es más fuerte que limitar la cardinalidad local a cuatro.

Necesitamos un operador constructivo:

\[
\Gamma(F,S)
\longrightarrow
\text{nueva referencia / descomposición}
\]

tal que:

1. sea exacto;
2. sea polinómico;
3. reduzca la interfaz futura;
4. no requiera conocer una solución;
5. funcione uniformemente para toda 3-SAT.

# 12. Teorema condicional hacia \(P=NP\)

Si existe un algoritmo uniforme que para toda 3-CNF \(F\):

- construye una jerarquía de cápsulas exacta;
- mantiene cada interfaz en tamaño polinómico;
- detecta cada quinta novedad en tiempo polinómico;
- genera una nueva referencia que conserva exactitud;
- usa un número polinómico de actualizaciones;
- decide al final si queda alguna solución,

entonces SAT se decide en tiempo polinómico.

Por tanto:

\[
\boxed{
\text{esa construcción sería suficiente para }P=NP.
}
\]

La existencia de tal algoritmo permanece abierta.

# 13. No-go principal de v0.79

\[
\boxed{
\text{capacidad local 4}
\not\Rightarrow
\text{complejidad global polinómica}.
}
\]

La familia de igualdades demuestra algo aún más instructivo:

\[
\boxed{
\text{una mala referencia puede producir ancho }2^m
\text{ incluso en un problema globalmente fácil}.
}
\]

Así que el objeto decisivo no es sólo la cápsula.

Es:

\[
\boxed{
\text{la regla que descubre qué referencia hace visible la estructura correcta}.
}
\]

# 14. Lectura desde el programa

Esto encaja directamente con la ontología:

\[
\text{incertidumbre}
\to
\text{quinta novedad}
\to
\text{nueva referencia}.
\]

Pero computacionalmente debemos añadir:

\[
\boxed{
\text{nueva referencia correcta debe poder descubrirse económicamente}.
}
\]

La nueva métrica natural del programa no es sólo cuántas soluciones quedan.

Es el costo constructivo de encontrar una representación suficiente.

# 15. Siguiente discriminante

La pregunta sobre NP queda reducida ahora a:

\[
\boxed{
\textbf{¿puede la quinta novedad señalar por sí misma
qué nueva referencia factoriza el futuro?}
}
\]

La familia de igualdad proporciona un control positivo:

- existe una referencia excelente: intercalar \(x_i,y_i\);
- existe una referencia pésima: todos los \(x\) antes de todos los \(y\).

El siguiente paso es intentar derivar la buena referencia **desde la estructura de relaciones**, sin buscar entre órdenes combinatoriamente.

Ahí está ahora el posible aporte diferencial del programa.
