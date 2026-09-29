# Editorial checks

Run with Python 3:

~~~bash
python3 ejemplos/comprobaciones.py
~~~

No external libraries are needed. This is not the sources' original code.

The script checks:

1. full novelty, partial novelty, and redundancy through finite signatures;
2. exact composition of `x = s` and `s = y` when eliminating the shared reference;
3. joint compatibility that cannot be reconstructed from separate marginals;
4. the four-state orbit under the standard rotation;
5. zero residue when the comparison stays in the inherited subspace;
6. cancellation of the seed when it is also used as the axis;
7. the difference between a mixed state and a uniform superposition;
8. the harmonic cycle of a triangle and its disappearance when a face is added;
9. cancellation of exact differences around a cycle.

These checks illustrate specific identities and obstacles. They do not generate a physical theory, solve general SAT, or complete bridge P03.
