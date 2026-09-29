# 4. Dependence and composition between closures

## What belongs to the relation

Let \(K_A,K_B\) be interfaces and let \(\Gamma_{AB}\subseteq K_A\times K_B\) be a nonempty joint support. Its projections are \(A_\Gamma,B_\Gamma\). There is support dependence when

\[
\Gamma_{AB}\subsetneq A_\Gamma\times B_\Gamma.
\]

The combinatorial deficit is

\[
D_R=\log_2\frac{|A_\Gamma||B_\Gamma|}{|\Gamma_{AB}|}.
\]

D_R = 0 characterizes the full product. It is not Shannon mutual information, and it does not determine the entire content of the relation: different supports can have the same cardinality.

Binary equality retains both margins {0,1} and admits only {00,11}. Its deficit is one bit. Dependence restricts combinations without necessarily eliminating local states.

## Channel compatibility

Knowing only the sizes of two sets does not determine what can interact. MF-56 includes admissible responses and shared types. MF-57 proposes transformations that intertwine representations:

\[
T\rho_A(g)=\rho_B(g)T.
\]

This criterion restricts channels, but a nontrivial operational channel must be required where appropriate: the zero map satisfies the equality and, by itself, does not establish interaction. The selection of the event does not follow from the existence of the channel.

## Available exact composition

For \(F_A(X,S)\) and \(F_B(S,Y)\), with X and Y disjoint and S their only shared boundary:

\[
B_A=\{s:\exists x\,F_A(x,s)\},\qquad
B_B=\{s:\exists y\,F_B(s,y)\}.
\]

Then

\[
F_A\land F_B\text{ is SAT}\iff B_A\cap B_B\ne\varnothing.
\]

The converse holds because the interior witnesses can be combined without sharing other variables. A new boundary is obtained by joining relations and projecting internal variables. This is exact semantic composition.

Example: x = s and s = y yield x = y when s is projected out. The joint relation preserves a dependence that does not appear in the x and y margins taken separately.

## What does not follow

It does not follow that the support has four elements, that composition produces a perpendicular vector residual, or that its representation is polynomial. A tabulated boundary over k variables can need \(2^k\) entries.

MF-62B shows that difficulty can remain between two tractable sectors even without a general residual: every exact three-literal clause is Horn or dual-Horn. Both sectors can be satisfiable while their conjunction is not.

## Sources

- [MF-56](../../fuentes/originales/MF56_RELATIONAL_DEPENDENCE_AND_CHANNELS.md).
- [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md).
- [MF-62B](../../fuentes/originales/MF62B_HYBRID_FRONTIER_HORN_DUAL_HORN_NO_GO.md).
- [The difficulty between closures](../../fuentes/originales/DIFFICULTY_BETWEEN_CLOSURES_ES.md).

Next: [geometric realization](05_reflexion_geometria.en.md).
