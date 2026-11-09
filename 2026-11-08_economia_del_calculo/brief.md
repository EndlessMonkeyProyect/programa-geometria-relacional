# Open research brief

How does the economy of computation emerge from the relations between references?

Endless Monkey Project
Relational Geometry Program

*English version of `encargo.md`. If the two differ, the Spanish text is the reference.*

---

INSTRUCTION FOR THE RESEARCH MODEL

Act as an independent mathematical researcher. Examine the problem presented below from mathematics, physics, logic, information theory and computation.

Your goal is not to confirm a hypothesis or reproduce a known solution. It is to identify relations, build arguments, find mechanisms, formulate proofs and, when appropriate, discover contradictions.

Keep the ontology described, but do not restrict the methodology.

You may use any mathematical, computational or conceptual tool that is relevant. You may also introduce new objects, formalizations and perspectives, as long as you explain their relation to the original structure.

It is not established in advance that the solution must be polynomial, subexponential or belong to any particular complexity class.

The economy, if it exists, must arise as a demonstrable consequence of the mechanism, not as a condition imposed on the research.

## 1. Starting ontology

The Relational Geometry Program investigates how distinctions, references, inheritance, incompatibility, singularity and closure arise from relations between structures.

Its conceptual elements include:

- Reference: a distinction acquires meaning within a relation between structures.
- Relation between radii: the radius of a structure, its distance from another and their relative changes determine which differences are observable from a reference.
- Reflection: a transformation can produce correspondences, equivalences and new relations between elements.
- Inheritance: relations already established can remain contained in later structures.
- Novelty: a relation introduces distinctions that were not determined by the inherited references.
- Closure: certain relations produce configurations whose description can stabilize.
- Relational singularity: different elements or configurations can be gathered under a reference without this implying their physical or mathematical disappearance.
- Reopening: a change of reference can make it possible to distinguish elements previously gathered.

These notions form the initial language of the research. They must not be confused with general theorems already proven.

The central formulation is:

A structure can contain many relations and yet show a small number of distinctions with respect to another structure.

The observed economy could arise from that relation, without an external operation that arbitrarily selects which information to keep.

## 2. Conceptual lab: mirror cube and spheres

The program uses a cube of mirrors with a moving wall as its reference lab.

Successive reflections make it possible to study equivalences, orientation, simultaneity, phase shift and changes in distinctions.

The moving wall represents a change in the relations of the system, not simply an external compression mechanism.

The spheres make it possible to study configurations with no privileged direction and the appearance of differences through links, orientations and shared references.

The tetrahedron, diamond structures and configurations of multiple spheres serve to study closure, incompatibility and new relations.

ROSI and the mirror-box lab are part of the language used to investigate these transformations.

It is not mandatory to use these geometric representations directly in every proof. What is indispensable is to keep and explain their ontological correspondence when an alternative formalization is proposed.

## 3. Available results

The program has several labs and partial results.

### A. Modular inheritance

For an inherited modular reference H and a new observation of period m:

```math
H'=\operatorname{lcm}(H,m)
```

The number of new classes inside each inherited class is:

```math
\frac{H'}{H} = \frac{m}{\operatorname{gcd}(H,m)}
```

For example:

```math
\operatorname{lcm}(15,9)=45
```

Here an additional distinction appears with respect to the inheritance.

On the other hand:

```math
\operatorname{lcm}(315,9)=315
```

The second observation introduces no new modular classes.

This rule is exact under the hypotheses of the model and has known mathematical antecedents. Its general application to other mechanisms remains open.

### B. Economy in combinatorial representations

Earlier experiments observed reductions of states and transitions through structural equivalences.

For a three-colour grid of width ten, a reduction from 1536 states to 136 states under a representation by symmetries was reported.

Results on recurrences and modular Hankel ranks were also obtained.

These checks do not by themselves prove a general construction of minimal representations or a complexity improvement for arbitrary problems.

### C. Optical lab v5.1

A structure of five sources is held fixed and the observation distance is changed.

Under the optical criteria implemented, the distinguishable components follow the sequence:

```math
5\longrightarrow4\longrightarrow3\longrightarrow2\longrightarrow1
```

When the displacement is reversed, the distinctions can reappear.

The experiment includes angular resolution, distance, relative velocity, frequencies, reflection and modular phases.

It was verified that two different internal distributions can show the same simplified observables at a large distance and become different when the reference changes.

This does not mean that all the internal information remains recoverable from the reduced observation.

The equivalence is relative to the observables used.

### D. Known limits of the procedure

The work on 3-colouring shows that certain global incompatibilities are not detected by fixed-size local closures.

The Mycielski families are relevant controls.

Therefore it cannot be assumed that every global structure automatically has a small representation or a sufficient local closure.

These limits must be incorporated into any generalization.

## 4. The main problem

Consider a structure whose size and number of relations grow.

From one reference many distinctions may show. From another, several of them may coincide.

In optics, this happens with an extended structure observed from a great distance: multiple sources can appear as a single spatial component, while some spectral observables remain differentiated.

The original structure does not necessarily change.

What changes is the relation from which it is distinguished.

Main question:

Can computational economy emerge from the equivalences, inheritances and new distinctions produced by a relation between references, so that the cost of solving a problem depends on that structure and not necessarily on enumerating all its configurations?

Do not assume that the answer is affirmative.

Investigate under what conditions it happens, when it fails and how it can be proven.

## 5. Correspondence with computational problems

The aim is to investigate whether the mechanism has consequences for constraint satisfaction problems, solution counting, graphs, recurrences, algebraic systems and other mathematical families.

Recent work by OpenAI and Anthropic on SAT and subexponential algorithms are points of comparison, not solutions to be reproduced.

Independently verify the scope, hypotheses, bounds and validation status of those works.

Distinguish rigorously between:

- Deciding whether a solution exists.
- Counting all solutions exactly.
- Building a representation of the solutions.
- Reducing observable distinctions.
- Reducing effective computational operations.

Do not assume that a reduction in any of these magnitudes automatically implies an equivalent reduction in the others.

Look for structural correspondences where they exist, but do not force equivalences.

## 6. Freedom of research

No specific methodology is requested.

You may investigate through geometry, combinatorics, category theory, group theory, logic, algebra, spectral theory, information, computational complexity, dynamical systems, mathematical optics or any other perspective.

You may also develop entirely new formalisms.

Proposals will be especially valued if they:

1. Identify a general principle derived from relations between references.
2. Distinguish known results from genuinely new consequences.
3. Build mathematical models that can be checked.
4. Find extreme examples where relations are numerous or far apart.
5. Identify counterexamples that delimit the scope of the mechanism.
6. Allow mathematical bounds to be deduced without imposing their form in advance.

A solution that demonstrates a fundamental limitation is also a valid result.

## 7. Open questions

Investigate especially:

First. Under what conditions can two configurations be considered equivalent with respect to a reference without losing the ability to answer an exact query?

Second. Can that equivalence be determined from the inherited relations, without first enumerating all configurations?

Third. What properties determine that a new relation introduces an independent distinction and not simply a redundancy?

Fourth. How does the cost of representing and solving a structure change when its size, the distance between its relations or the number of singularities grows?

Fifth. Are there families where a large number of relations can be expressed through a small number of references without losing exactness?

Sixth. Are there families where that reduction is impossible, and can it be proven why?

Seventh. Can a rigorous mathematical correspondence be established between the optical reduction of distinctions and some exact computational reduction?

Eighth. What complexity consequences arise from the mechanism, if its validity is proven for some family? No target bound is assumed.

## 8. Result requested from the researcher

Carry out an independent investigation.

Begin by reconstructing the ontology through concepts and relations, identifying which elements are mathematically defined and which need formalization.

Then identify different possible routes to a solution.

Do not limit yourself to a single interpretation, and do not prematurely discard incompatible perspectives.

For the routes you consider most promising, try to produce concrete results: definitions, propositions, proofs, counterexamples, constructions or reproducible experiments.

Clearly distinguish between proven results, experimental evidence, hypotheses and open questions.

If you find an equivalent known mechanism, explain the exact correspondence and what the proposed formulation contributes, or does not.

If you discover a contradiction, identify it and determine which part of the construction is affected.

If a new relation appears, explain how it arises from the original elements.

A definitive answer is not required. The aim is to widen the space of solutions without abandoning the starting ontology.

## 9. Evaluation criterion

Use, where relevant, an evaluation inspired by ROSI and ROS-1 Lite.

Distinguish between relations that are:

- Resolved: there is a proof or sufficient check within explicit hypotheses.
- Open: information or a proof is missing.
- Superposed: different interpretations or constructions remain compatible with the evidence.
- Prematurely closed: a conclusion has been asserted without the necessary conditions.

Do not confuse conceptual consistency with mathematical proof.

Do not confuse similarity between mechanisms with equivalence of algorithms.

## 10. Final question

The fundamental question is not how to force a structure to use less information.

It is to understand which distinctions exist, which remain under a reference, which are inherited, which are gathered and which reappear when the relations change.

From that:

What can be proven about the natural economy of representations and its possible consequences for computation?

Investigate freely, keep the ontology, and let the results determine the conclusions.

---

Endless Monkey Project
Relational Geometry Program
