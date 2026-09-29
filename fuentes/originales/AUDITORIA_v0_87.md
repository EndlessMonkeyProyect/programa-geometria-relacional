# Auditoría adversarial v0.87

## Resultado principal

La idea "la información anterior queda en la capa del sistema" tiene una realización matemática exacta mediante una cadena de inclusiones:

\[
L_0\hookrightarrow L_1\hookrightarrow L_2\hookrightarrow\cdots.
\]

Si:

\[
L_{k+1}=L_k\oplus N_{k+1},
\]

la proyección al primer sumando recupera exactamente la capa previa.

Por tanto no es necesario que la nueva identidad codifique nuevamente toda la historia.

## Conexión con v0.84

v0.84 ya había dado:

\[
L_{k+1}
=
L_k\oplus\operatorname{span}\{r,Jr\}.
\]

Así la herencia por capas no es una estructura añadida arbitrariamente; ya estaba implícita en la extensión mínima por residuo independiente.

## Herencia de J

Con:

\[
J_{k+1}=J_k\oplus J_N,
\]

se tiene:

\[
J_{k+1}i_k=i_kJ_k.
\]

De ahí:

\[
J_k^4=I
\Rightarrow
J_{k+1}^4i_k=i_k.
\]

El cierre de fase previo persiste exactamente.

## No-go

No se debe afirmar que "la identidad contiene toda la historia".

La capa contiene el contexto aún acreditado; la identidad puede ser sólo una interfaz suficiente.

## Punto abierto

La compatibilidad de un cierre físico general:

\[
\Gamma_{k+1}i_k=i_k\Gamma_k
\]

no se deduce automáticamente de la herencia de fase.

Puede fallar si una interacción nueva destruye o reconfigura una identidad previa.

Por tanto el siguiente problema físico es estabilidad bajo acoplamiento, no almacenamiento de historia.

## Consecuencia para el programa

El antiguo hueco "¿cómo se hereda la información al siguiente nivel?" queda resuelto dentro de la realización ortogonal.

La nueva frontera es:

1. definir la dinámica de acoplamiento entre módulos;
2. determinar cuándo un cierre permanece estable;
3. derivar el selector entre cierres proyectivos y orientados (C2/C4);
4. sólo después conectar estas clases con sectores físicos.
