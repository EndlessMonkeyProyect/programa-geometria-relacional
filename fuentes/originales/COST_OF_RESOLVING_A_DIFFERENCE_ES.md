
# El costo de resolver una diferencia

Una incertidumbre puede terminar en una respuesta mínima.

SAT o UNSAT requiere un bit.

Eso no significa que sea barato obtener ese bit.

El cierre final de una contradicción puede ser simplemente:

\[
\bot.
\]

Lo difícil puede ser acreditar que ninguna alternativa sobrevivió.

Por ello distinguimos:

\[
\boxed{\text{suficiencia semántica}}
\]

de:

\[
\boxed{\text{suficiencia acreditable}}.
\]

Un estado puede ser semánticamente perfecto y, sin embargo, resultar costoso demostrar localmente que sigue siendo suficiente.

Para la rama NP, una arquitectura útil no sólo debe contener la respuesta correcta: debe poder **certificar económicamente**, después de cada nueva relación, que no perdió ninguna diferencia futura relevante.
