# 2. Frontera suficiente, identidad y cierre

## Concepto

Una frontera conserva las diferencias que todavía pueden modificar respuestas admitidas. Un cierre organiza interior e interfaz; no equivale a inmovilidad.

Si un resumen \(s:X\to S\) permite reconstruir toda respuesta Q, entonces

\[
s(x)=s(y)\Rightarrow x\sim_C y.
\]

Por eso necesita al menos tantas etiquetas como clases contextuales. El cociente alcanza esa cota: es el resumen determinista exacto mínimo en número de estados para ese contrato.

Esta minimalidad semántica no afirma que el cociente sea barato de calcular ni que minimice todos los formatos de almacenamiento.

## Identidad e interior

El cierre puede operar mediante una interfaz pequeña mientras su contexto permanece en la capa que lo sostiene. La v0.87 representa la herencia por una inclusión con recuperación:

\[
i_k:L_k\hookrightarrow L_{k+1},\qquad p_ki_k=I.
\]

Si \(L_{k+1}=L_k\oplus N_{k+1}\), la proyección al primer sumando recupera la capa previa. Esto conserva información representada; no prueba que toda historia física esté almacenada en una identidad aislada.

## Suficiencia relativa

En el ejemplo de umbral, una pregunta futura es \(Q(p,s)=1[|p|+|s|\le k]\). Si quedan r bits futuros, el resumen mínimo de un prefijo p es

\[
\theta(p)=\operatorname{clip}(k-|p|,-1,r).
\]

Conteos distintos pueden resultar equivalentes porque ningún futuro disponible los discrimina. MF-54 corrigió un contador que era suficiente pero no siempre mínimo.

Si se amplía el contexto, la vieja interfaz puede dejar de bastar. Conservar el interior puede permitir recalcularla; usar solamente el resumen previo no garantiza recuperar distinciones ya omitidas.

## Cierre acreditable

MF-60B añade un testigo de suficiencia: estado y certificado. Deben distinguirse existencia de un certificado, verificación, generación y actualización. Ninguna de estas operaciones se vuelve eficiente por definir un cociente.

## Fuentes

- [MF-54, §§8–14](../../fuentes/originales/MF54_LOCAL_INFORMATION_REFLECTION_AND_BOUNDARY_STATE.md).
- [Cierre acreditable](../../fuentes/originales/ACCREDITABLE_CLOSURE_ES.md).
- [MF-60B](../../fuentes/originales/MF60B_COMPOSABLE_LOCAL_CERTIFICATES.md).
- [Herencia v0.87](../../fuentes/originales/AUTORRECURRENCIA_CAPAS_HERENCIA_v0_87.md).

Siguiente: [novedad y resolución](03_novedad_resolucion.md).
