# 6. Herencia y composición geométrica de cápsulas

## Lo establecido

La suma directa conserva la capa anterior. Si se construye \(J_{k+1}=J_k\oplus J_N\), con un J_N apropiado, la restricción al sector heredado mantiene su ley. La ecuación de entrelazamiento es

\[
J_{k+1}i_k=i_kJ_k.
\]

No se deriva de aquí la elección de J_N a partir de la información relacional.

Para un cierre general idempotente C, preservar los puntos fijos requiere además \(C_{k+1}i_k=i_kC_k\). Una interacción puede no satisfacer esa compatibilidad y reconfigurar el cierre.

## La propuesta v0.91

La fuente propone:

\[
d_{ij}=x_j-T_{ij}x_i,\qquad q_{ij}=(I-P_k)d_{ij},
\]

y, si q no es cero, una nueva cápsula \(\{q,Jq,-q,-Jq\}\).

Son necesarias definiciones operativas de la interfaz S_k, del transporte T_ij, del espacio de comparación, del subespacio proyectado y del nuevo J. Escribir los nombres de esos mapas no demuestra su existencia con todas las propiedades requeridas.

## Dos obstáculos de integración — revisión editorial

**Residuo nulo por cierre lineal.** Si ambas interfaces están en L_k y el transporte preserva L_k, su resta también está allí; entonces q = 0. Se necesita una representación conjunta más amplia, una operación distinta o una justificación del transporte que introduce información exterior.

**Eje y semilla.** Si R = q/||q|| y se reutiliza \(J_R(v)=v\times R/\|R\|\), q es paralelo al eje, queda fuera del sector transversal y \(q\times R=0\). Para generar la órbita de q debe explicitarse otro operador o un eje distinto. Adoptar un J abstracto es posible como hipótesis; no equivale a derivarlo mediante esa fórmula.

## Qué construcción falta

1. Dar dos cierres y sus interfaces con contrato de suficiencia.
2. Construir la compatibilidad conjunta, aprovechando MF-56 o MF-61B.
3. Identificar novedad por no-factorización.
4. Definir una realización geométrica que conserve esas distinciones.
5. Construir J del nuevo nivel y probar su dominio, compatibilidad métrica y cuadrado.
6. Verificar la estabilidad bajo la dinámica elegida y la recuperación de información heredada.

Es un programa de prueba, no una prueba completada por esta edición.

## Precaución sobre la autosimilitud

Conservar el orden cuatro en sectores existentes no equivale a demostrar que toda composición tenga orden cuatro. La autorrecurrencia puede declararse como principio estructural. Si se pretende derivarla, hace falta una ley sobre relaciones entre generadores, el pendiente explícito de MF-57.

## Fuentes

- [Herencia v0.87](../../fuentes/originales/AUTORRECURRENCIA_CAPAS_HERENCIA_v0_87.md).
- [Composición v0.91](../../fuentes/originales/COMPOSICION_RECURSIVA_CAPSULAS_v0_91.md).
- [Auditoría v0.91](../../fuentes/originales/AUDITORIA_v0_91.md).
- [MF-57, §§9–15](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md).

Siguiente: [dinámica y estabilidad](07_dinamica_estabilidad.md).
