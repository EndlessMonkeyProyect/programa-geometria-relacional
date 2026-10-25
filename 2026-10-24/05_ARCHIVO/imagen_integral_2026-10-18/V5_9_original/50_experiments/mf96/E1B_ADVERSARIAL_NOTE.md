# E1b — contraejemplo adversarial para la generalización 2-SAT

La revisión externa señaló que la frase “2-SAT nunca supera su número inicial de cláusulas” excedía los datos de E1.

Se reprodujo el caso con las mismas funciones `random_ksat` y `dp_eliminate`:

\[
n=8,\qquad m=32,\qquad \text{seed}=6.
\]

Resultado:

\[
\boxed{
32\to33\to26\to7\to5\to3.
}
\]

Estado final: UNSAT.

Conclusión:

\[
\boxed{
2\text{-SAT}\in P
\not\Rightarrow
\text{monotonicidad del tamaño intermedio de Davis–Putnam}.
}
\]

La lectura de E1 se restringe a las familias y parámetros medidos originalmente.

El contraejemplo se conserva como información nueva del programa.
