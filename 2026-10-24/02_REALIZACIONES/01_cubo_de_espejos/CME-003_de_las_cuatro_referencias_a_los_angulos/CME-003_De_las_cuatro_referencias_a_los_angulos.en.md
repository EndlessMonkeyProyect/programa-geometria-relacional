# CME-003 — From four references to the angles π/2 and π/3

**Mirror Cube Laboratory · Relational Geometry Program · Le Matt Ansatz Di Ego · October 24, 2026**

*English translation of `CME-003_De_las_cuatro_referencias_a_los_angulos.md`. The Spanish text is the authoritative version. Terms follow the glossary in `../../../01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.en.md`.*

**Status:**
- [T] known reflection theory, checked here with exact arithmetic;
- [E] reproducible trial;
- [O] reading within the thread;
- [A] what remains open.

## Question

CME-002 shows that what decides whether an enclosure closes is the sum of the fractions, but it takes the first two angles, π/2 and π/3, as input. Do those angles come out of something the program already has, without putting them in by hand?

## What was already there

**From the author.**
- When the one stops being one, two appear; each half splits in two again, and that gives the 4. The solutions emerge together, not one at a time.
- The 2 appears first as a half. The 3 does not appear until the 4 shows itself, and then it emerges as the number of nodes (October 24).
- The four singularities are three and one, but it is impossible to tell which one is "the one" (October).

**T8, of October 14** (`../../../01_HILO/fuentes/06_hilo_del_dos/v2_8/docs/T8_DEL_LENGUAJE_AL_ESPACIO_v2_8.md`):
- two distinctions give four states and three parity comparisons;
- every pair of states is separated by exactly two comparisons;
- in three dimensions, the four states are a regular tetrahedron;
- the identity is symmetric and singles out no privileged reference.

**O19** (`../geometria_O19_O22/O19/`): the central mirrors produce the complementary tetrahedron; together they are the eight vertices of the cube, separated by parity.

**O20 and O22** (`../geometria_O19_O22/O20/`, `O22/`):
- the face mirror creates a fifth reference at 5/3 of the radius;
- reflecting is not filling.

**CME-002, the bit rule** (`../CME-002_pared_que_se_corre/comprobacion_regla_del_bit.py`): a ±1 at each node, together with the exchange of nodes, gives only π/2, π/3 and π/4, with 48 orientations for three nodes.

The rescue note of October 24 (`../../../05_ARCHIVO/notas_recibidas_2026-10-24/`) proposed reading the exchanges of the four references as reflections. This record checks that proposal and completes it.

## Admitted rules

Only two operations on the four references, both already present in the program:
- **exchanging** two references, because none is privileged;
- **changing the sign** of a comparison: the bit ±1 at a node.

Each reference is represented by its three comparisons. No angle is used as input.

## Result [T · E]

1. **The four references are a tetrahedron.** In the coordinates of the comparisons, the references are (1, 1, 1), (1, −1, −1), (−1, 1, −1) and (−1, −1, 1). The axes of the three comparisons are the axes joining opposite edges, and they are perpendicular to each other.
2. **Exchanging is reflecting.** The exchange of two references is the reflection in the plane that leaves the other two fixed.
   - Two exchanges **with no shared reference** commute: order 2, angle π/2.
   - Two exchanges **with one shared reference** run through three references: order 3, angle π/3.
   - The six exchanges generate 24 orientations: this is the (2, 3, 3) enclosure of CME-002.
3. **There are no generators to choose.** The mirrors divide space into 24 chambers, and in every one of them the walls form the same enclosure, with orders 3, 3 and 2. It does not matter where the focus is.
4. **The bit gives the cube.** Changing the sign of a comparison takes the tetrahedron to its complement, and the two together are the eight vertices of the cube: the parity split of O19. With the bit, the product of two mirrors can have order 4 (π/4), and the group reaches 48 orientations, which is the (2, 3, 4) enclosure of the cube.
5. **No other angle appears, before or after.**
   - With two references there is a single mirror and two orientations: the half.
   - With eight references, the product of two exchanges still has order 2 or 3 only.
   - With exchanges and bits, the product of two mirrors has order 2, 3 or 4 only, as the bit rule says.
   - The 5 does not come from here.
6. **If one reference were distinguishable**, only the other three could be exchanged. There would be 6 orientations, and the three mirrors would surround the line of the fixed reference: a flat enclosure, that of the triangle, with two directions instead of three.
7. **Reflecting in a face is something else.** It does not exchange references: it creates a new one outside the tetrahedron, at 5/3 of the radius (O20). The four new ones form the inverted tetrahedron, and that is the reflection that never closes (CME-001).

**A precision.** The orders that fix angles are always those of the product of two mirrors. Composite elements can have other orders: among the 24 there are rotations of order 4, and among the 48, elements of order 6. The two are not mixed.

## Reading within the thread [O]

- **The 2 appears first as a half:** with two references there is a single mirror.
- **The 3 appears with the 4.** With four references, two exchanges can share one, and that gives the order 3. At the same time three nodes appear: there are three comparisons, and each chamber has three mirrors.
- **What shares nothing is perpendicular.** Two exchanges with no shared reference are independent and meet at π/2. It is the same reading as for two numbers with no common divisor.
- **That it is impossible to say which one is "the one"** is what gives the three independent directions. If one were distinguishable, the enclosure would be flat.
- **The tetrahedron, twice.** Reflected in its faces, it creates new references and is the background that never closes. With the exchange of its references, which are its symmetry mirrors, it closes at 24. The same figure gives the open background and the closed island; what changes is whether the reflection brings a new reference or exchanges the ones already there.
- **The cube** is the exchanges plus the bit: the bit rule of CME-002, seen from the four references.

## What it does NOT establish

- It is not new mathematics. That the exchanges of n things form a reflection group is a classical result ‹1›‹2›.
- It does not derive why there are two distinctions (n = 2). T8 leaves that open, and it remains open here.
- It does not derive the metric. The coordinates of the comparisons are one realization.
- It does not prove that the moving wall produces exactly these references and these exchanges.
- It says nothing about the branches.

## What remains [A]

1. **The map from the moving wall.** One must write down which rule of the wall makes its cascade (1 → 2 → 4) give four interchangeable references, none privileged. If that holds, CME-002 has no hand-set input up to the 4.
2. **The two distinctions**, as T8 asks.
3. **The 5.** It comes neither from exchanges nor from bits; it needs the step of the cascade where the one becomes undefined.

## Reproduction

```bash
python3 cme003_cuatro_referencias.py
```

It uses only the standard library and exact arithmetic with integers and fractions. It writes `cme003_resultados.json` and fails if any of the points does not hold, including the separation between the orders of products of two mirrors and those of composite elements. Its printed output is in Spanish.

## Links

- ‹1› E. H. Moore, "Concerning the abstract groups of order k! and ½k! holohedrically and hemihedrically isomorphic with the symmetric and the alternating substitution-groups on k letters", *Proceedings of the London Mathematical Society* 28 (1897).
- ‹2› H. S. M. Coxeter, "Discrete groups generated by reflections", *Annals of Mathematics* 35 (1934).
