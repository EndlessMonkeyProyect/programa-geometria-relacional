# Auditoría adversarial v0.86

## 1. Qué se derivó

Dado un libro cuadrático de dimensión \(D=2^n\) y un principio de homogeneidad pre-referencia, el estado positivo normalizado invariante bajo permutaciones signadas de canales es único:

\[
\rho_0=I/D.
\]

Por tanto un canal unidimensional tiene peso:

\[
1/D=2^{-n}.
\]

El complemento tiene peso:

\[
(D-1)/D.
\]

Esto cierra el antiguo puente de peso sin postular equiponderación canal por canal.

## 2. Qué sigue siendo supuesto

La homogeneidad pre-referencia no se deriva de P3–P6.

Debe justificarse ontológicamente como "ausencia de diferencia acreditada" o mantenerse como principio independiente.

También se supone que el libro relevante es la completitud cuadrática/Clifford de los roles.

## 3. No-go importante

La mera permutación de generadores no basta.

Bajo \(S_n\), los subconjuntos de distinto tamaño no son equivalentes. Puede haber pesos distintos por capa de Hamming.

Para obtener uniformidad sobre los \(2^n\) canales se necesita invariancia bajo traducciones XOR/cambio de origen o una simetría equivalente que actúe transitivamente sobre los canales completos.

## 4. Corrección histórica de sigma

Después de v0.84:

\[
\sigma=-1.
\]

Por tanto no debe seguir interpretándose \(\sigma\) como bit pendiente.

La orientación binaria correcta es:

\[
J\leftrightarrow -J.
\]

## 5. Máxima entropía

La distribución uniforme es también la única de entropía máxima:

\[
H_{\max}=\log_2 2^n=n.
\]

Esto es coherente con la ontología de incertidumbre, pero no convierte automáticamente una entropía matemática en entropía física.

## 6. Relación con 1:3 y 1:15

La matemática produce:

- \(n=2\): \(1:3\);
- \(n=4\): \(1:15\).

La asignación física a leptones/bariones permanece abierta.

## 7. Riesgo de reetiquetado

Si "homogeneidad" se define simplemente como "todos los canales tienen igual peso", no se ha avanzado.

La formulación válida es invariancia bajo un grupo transitivo de recodificaciones de canal, de la cual la uniformidad se demuestra.

## 8. Próximo discriminante

El siguiente problema legítimo no es volver a calcular \(1:15\).

Es demostrar por qué el sistema físico relevante conserva orientación completa \(C_4\) o sólo su clase proyectiva \(C_2\).

Ese selector debe producir un observable distinto y falsable.
