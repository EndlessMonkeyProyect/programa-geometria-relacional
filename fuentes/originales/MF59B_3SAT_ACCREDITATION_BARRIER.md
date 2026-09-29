
# MF-59B — Barrera de acreditación exacta en 3-SAT

**Versión:** v0.67-research  
**Rama:** puente ontología–complejidad.  
**Nota:** se usa MF-59B para no colisionar con un MF-59 histórico del archivo.

## 1. Pregunta correcta

MF-58 mostró que la cantidad semántica de información no mide por sí sola la dificultad.

Para una instancia booleana, la respuesta SAT/UNSAT contiene un solo bit:

\[
b(F)\in\{0,1\}.
\]

La pregunta relevante pasa a ser:

\[
\boxed{\text{¿cuánto cuesta acreditar y actualizar exactamente el cierre?}}
\]

## 2. Tres niveles

Para:

\[
F_t=C_1\land\cdots\land C_t
\]

distinguimos:

- **estado sintáctico:** la lista de cláusulas;
- **estado semántico:** \(M(F)=\{x:F(x)=1\}\);
- **acreditación:** demostrar propiedades semánticas del cierre sin enumerar \(M(F)\).

Añadir una cláusula sintácticamente es barato:

\[
F\mapsto F\land C.
\]

Semánticamente:

\[
M(F\land C)=M(F)\cap M(C).
\]

Pero una representación o actualización compacta no sirve por sí sola si las consultas semánticas siguen siendo difíciles.

## 3. Redundancia exacta

Defina:

\[
\mathrm{Red}(F,C)=1
\iff
F\models C.
\]

Si \(F\models C\), añadir \(C\) no elimina ningún modelo todavía compatible con \(F\).

Así, reconocer redundancia es una forma exacta de acreditar que una diferencia nueva ya estaba contenida por el cierre.

## 4. Teorema MF-59B-A

Sea \(G\) una 3-CNF sobre \(x_1,\ldots,x_n\).

Añada tres variables frescas \(z_1,z_2,z_3\) y la cláusula:

\[
C_z=(z_1\lor z_2\lor z_3).
\]

Entonces:

\[
\boxed{
G\text{ es UNSAT}
\iff
G\models C_z.
}
\]

**Prueba.** Si \(G\) es UNSAT, implica cualquier cláusula. Si es SAT, tome un modelo de \(G\) y extiéndalo con \(z_1=z_2=z_3=0\); la extensión satisface \(G\) y falsifica \(C_z\). QED.

El complemento de \(F\models C\) tiene como certificado una asignación que satisface \(F\) y falsifica \(C\), verificable en tiempo polinómico.

Por tanto:

\[
\boxed{
\text{acreditación exacta de redundancia de cláusula es coNP-completa.}
}
\]

No se está afirmando \(P\neq NP\).

El resultado relevante para el programa es:

\[
\boxed{
\text{reconocer que una diferencia “ya cabe” puede contener un problema global de acreditación.}
}
\]

## 5. Teorema MF-59B-B — barrera incremental

Suponga una representación exacta uniforme \(K(F)\) para toda 3-CNF con:

1. \(|K(F)|\le\mathrm{poly}(|F|)\);
2. actualización \(K(F)\to K(F\land C)\) en tiempo polinómico;
3. consulta \(\mathrm{Empty}(K(F))\) en tiempo polinómico.

Entonces 3-SAT está en \(P\): se parte de \(K(\top)\), se incorporan todas las cláusulas y se consulta si el estado final es vacío.

Por tanto:

\[
\boxed{
\text{cápsula exacta universal + tamaño poly + update poly + Empty poly}
\Rightarrow P=NP.
}
\]

La dificultad puede migrar entre tamaño, actualización y acreditación. Una representación compacta no basta.

## 6. El caso extremo que aclara todo

El cierre terminal de una contradicción puede escribirse simplemente:

\[
\boxed{\bot}.
\]

Y la respuesta SAT/UNSAT es un bit.

Sin embargo, acreditar que todas las alternativas han desaparecido es precisamente la parte global.

Así:

\[
\boxed{
\text{complejidad}\neq\text{cantidad de información en la respuesta}.
}
\]

La complejidad puede residir en el costo necesario para **resolver y acreditar** ese bit.

## 7. Perfil operacional

Proponemos medir:

\[
\boxed{
\mathfrak C(F)=
(L_{\rm desc},T_{\rm acc},T_{\rm upd},T_{\rm empty},T_{\rm dec}).
}
\]

- \(L_{\rm desc}\): longitud de descripción;
- \(T_{\rm acc}\): costo de acreditar equivalencia/redundancia;
- \(T_{\rm upd}\): costo de incorporar una relación;
- \(T_{\rm empty}\): costo de acreditar vacío;
- \(T_{\rm dec}\): costo total de decisión.

\(I_{\rm rel}\) puede registrarse aparte, pero no sustituye estas cantidades.

## 8. Falsador para cualquier propuesta de solución

Una representación candidata debe especificar:

1. cómo construye el estado;
2. cómo incorpora cada cláusula;
3. cuánto crece su memoria;
4. cómo acredita redundancia/equivalencia;
5. cómo detecta \(\bot\);
6. cuál es el costo de peor caso.

Si alguno de esos pasos invoca implícitamente una consulta equivalente a SAT, UNSAT o implicación sin un procedimiento nuevo y acotado, la dificultad fue desplazada.

## 9. Resultado central

La pregunta deja de ser:

\[
\text{“¿puedo comprimir SAT?”}
\]

y pasa a ser:

\[
\boxed{
\text{¿puedo mantener un cierre exacto cuya suficiencia sea localmente acreditable?}
}
\]

## 10. Próximo frente

Buscar un **certificado local composable de suficiencia** \(w_t\) tal que:

\[
(K_t,C_{t+1},w_t)
\longrightarrow
(K_{t+1},w_{t+1})
\]

pueda verificarse con costo polinómico sin reabrir el espacio completo de modelos.

Si esto sólo funciona en familias estructuradas, caracteriza un fragmento tratable.

Si funcionara uniformemente para toda 3-SAT y además permitiera detectar vacío, daría un algoritmo polinómico y resolvería \(P\) vs \(NP\).
