
# The Mirror Cube, the Self-Referential Unit, and P versus NP

**Request for independent review · Relational Geometry Program**  
**Le Matt Ansatz Di Ego · October 30, 2026 · expanded edition incorporating T-EXT-01**  
**Repository:** <https://github.com/EndlessMonkeyProyect/programa-geometria-relacional>

## The request in brief

We request an independent review of **the development as a whole**, from its ontological organizing principle to its logical and mathematical realizations and the question of computational cost in 3-coloring. The starting point is a unit understood as a **self-referential space defined by the radius of the relations that sustain it**. Uncertainty expresses the indeterminacy of its nature relative to a reference and a query; it is not an additional object introduced into the unit.

The mirror enclosure provides a setting in which to examine reflection, focus, interior and exterior, normalization, and changes of reference. The sphere and circuit laboratories, R–01 modular arithmetic, and the developments R4, R5, R6, T-EXT-01, and R–04 realize parts of this investigation under different contracts. In the P-versus-NP branch, the question becomes testable: **which distinctions must be preserved, recovered, or certified when an instance's relations change, and what is the total cost of doing so?**

We do not ask reviewers to accept a correspondence because it is intuitively explanatory. We ask them to assess **definitions, assumptions, proofs, reproducible data, correspondences, and barriers** on their own terms. A review that identifies a known equivalent formulation, a missing hypothesis, a better-defined operation, or a counterexample in even one section would be a valuable contribution.

**New result included.** T-EXT-01 establishes a lower bound of $\lfloor n^2/4\rfloor$ bits for self-sufficient signatures answering all exterior continuations $D_{uv}$ on a bipartite family with a full interface. This is a quadratic information lower bound, not a time lower bound or a proof of either side of P versus NP.

**Scope labels.** [O] denotes an ontological formulation; [T], a proposition with proof under stated assumptions; [C], an identified classical result; [E], a reported or supplied finite computation; [I], an interpretive correspondence; and [A], an open question or conjecture. A connection between laboratories is not treated as a mathematical implication until a map preserving the relevant operations and observables has been specified.

## 1. The thread: unit, reference, radius, and relational nature [O]

A unit **does not necessarily arise when images meet**. It is recognized as a self-referential space because an organization of relations defines its own domain of comparison. We call the **relational radius** the reach of that organization: which relations participate in the reference through which the unit is recognized and which sustain its continuity. This radius need not be Euclidean distance, a material surface, or a single numerical value. Each realization must specify how it is determined.

**Contextual uncertainty** is not another entity. It expresses those distinctions concerning the unit's nature that remain undetermined under the chosen frame and query. An exterior perspective may recognize the unit while not determining its interior; an interior perspective may have access to relations absent from the exterior signature.

A **reflection** establishes relations between manifestations and references. Two paths of opposite orientation may reach the same focus; agreement in observed position does not imply agreement in orientation, provenance, or phase. The focus may itself belong to the system. Thus, a meeting is **a query relative to a reference**, not automatic evidence that a unit has come into existence or achieved self-closure.

**Normalization** expresses how distinct references or scales are compared while preserving the relations declared in the model. **Self-closure** (*cierre en sí*) names the continuity of a self-referential organization: testing it requires an internal reference, admissible transformations, and observables that remain compatible. A unit may, in turn, participate in a larger unit without necessarily losing its interior information. This yields a structure of **units of units**.

We propose the following genealogy of concepts for review:

**unit → self-reference → relational radius → relative uncertainty → reflection → normalization → self-closure → composition of units.**

This order is a research thread, not a causal theorem of physics. A singularity, understood here as a unit whose nature is not fully determined from an exterior reference, is not automatically a singularity in general relativity. **The mathematical propositions in the following sections depend on their explicit definitions and assumptions, not on accepting this ontological interpretation.** The ontology shapes the program's questions and genealogy; proofs are assessed within their own models.

### What we ask reviewers to examine in this layer

We ask which existing notions—transition systems with interfaces, quotient theory, observational equivalence, and relational composition—most precisely model this language, **without equating a unit with merely the class of states indistinguishable to an observer**. The program does not need a new name for an already represented entity; it needs an explicit account of the relation between an internal reference and the operations by which the unit is recognized.

## 2. The mirror enclosure: reflection, orbits, and changing references [C/T/I]

In the one-dimensional section of O59, with two ideal mirrors at $0$ and $L>0$, the reflections are

$$
s_0(x)=-x,\qquad s_L(x)=2L-x.
$$

They generate transformations $x\mapsto\pm x+2kL$ for $k\in\mathbb Z$. The signature

$$
\rho_L(x)=\operatorname{dist}(x,2L\mathbb Z)
$$

characterizes exactly the orbits of the declared group: $\rho_L(x)=\rho_L(y)$ if and only if $x$ and $y$ lie in the same orbit. This is an **orbit signature** for a particular geometric question, not a complete account of the unit's interior nature.

**Counterexample to reference updating.** With $L=1$, the positions $x=1/4$ and $y=9/4$ have the same signature $1/4$. Moving the mirror so that $L=2$ yields signatures $1/4$ and $7/4$. Information stored in the earlier signature is insufficient to determine the new one. Two states identified by one reference can require different answers after an admissible change of setting.

The CME laboratories distinguish objects that should not be conflated: the full symmetry group of a regular tetrahedron, $S_4$, has 24 elements (its rotational subgroup is $A_4$, of order 12); the hyperoctahedral group $B_3$ has 48; another contract, the free product of four involutions in CME-001, contains $2\cdot3^\ell-1$ reduced words of length at most $\ell$. For the triangular Coxeter group $(2,3,k)$, the regime is finite when $k=2,3,4,5$, affine when $k=6$, and hyperbolic when $k\ge7$. Initial growth spheres of $(2,3,6)$ and $(2,3,7)$ agree to a finite depth and then separate, even though one pair relation has different orders (6 versus 7).

**Interpretation within the program.** Closure, repetition, and unbounded growth in a group are properties of that group and its generators; analogy alone does not convert them into a complexity bound for a 3-coloring algorithm. The question is which mathematical object, if any, preserves a corresponding distinction between local relations and global behavior.

## 3. Spheres, C₄, and common normalization: other realizations [O/T/I]

In the sphere laboratory, center positions, contacts, and the selected relations determine different structures. Three noncollinear centers determine a plane; four centers of pairwise tangent equal spheres form a regular tetrahedron; four coplanar spheres with only peripheral contacts form a different circuit. Choosing the links is part of the contract, not a consequence of drawing four objects.

In the scalar model of a $C_4$ circuit with constraint $s_i+s_j=0$ on each link, the mode $(a,-a,a,-a)$ exists. If the same constraint is imposed on all six edges of $K_4$, the nonzero mode disappears. This is an exact algebraic distinction between the declared **relational rules**, not a general optical law.

R–01 adds an arithmetic test of continuity. For the reference $\Phi_N(x)=x\bmod N$ and a new query $d_p(x)=x\bmod p$, where $p$ is prime and $\gcd(N,p)=1$, the common reference is

$$
L=\operatorname{lcm}(N,p)=Np.
$$

By the Chinese remainder theorem, under $\gcd(N,p)=1$ there is an isomorphism of residue groups:

$$
\mathbb Z/L\mathbb Z\cong
\mathbb Z/N\mathbb Z\times\mathbb Z/p\mathbb Z.
$$

Each residue class modulo $N$ refines into $p$ classes modulo $L$ while retaining its projection to the previous reference. The **normalized-phase identity**, distinct from the residue projection, is

$$
\frac{j}{N}=\frac{pj}{L}.
$$

This identity compares points on a normalized grid; **it does not turn $j\mapsto pj$ into a section of the natural residue projection**. Compatible affine updates may commute with projections without being injective: multiplication by $0$, for instance, collapses distinctions. **Compatibility between references is not the same as preservation of every distinction.**

These models address a common question about relation, reference, and continuity. Any physical bridge or universal mathematical mechanism would require a definition of which operations are preserved between models.

## 4. Logical and mathematical contract: reference, query, continuation [C/T]

For each realization we declare

$$
\mathfrak R=(X,Q,\mathcal C,\Phi,\mathcal A,\kappa),
$$

where $X$ denotes states; $Q:X\to Y$, the query; $\mathcal C$, the admitted continuations; $\Phi:X\to S$, a signature or observable reference; $\mathcal A$, the effective operations; and $\kappa$, the cost of encoding, construction, updating, storage, querying, and certification. A self-referential unit may additionally require an **internal** reference $\Psi_U$, internal relations $R_U$, and transformations $T_U$: the exterior signature $\Phi$ must not silently replace that information.

**Equivalence under continuations (MF-106).** Given the operators $T_c$ corresponding to continuations, define

$$
x\equiv_{Q,\mathcal C}y
\quad\Longleftrightarrow\quad
Q(T_cx)=Q(T_cy)\quad\forall c\in\mathcal C.
$$

If $\mathcal C$ contains the identity and is closed under composition, both $Q$ and the continuations descend to the quotient $X/\!\equiv_{Q,\mathcal C}$. This is a standard observational-equivalence result related to Myhill–Nerode theory. It characterizes exactly the distinctions that any sufficient representation for this contract must preserve.

**Signature-update criterion (MF-97).** For a transformation $F:X\to X$, an operation $f$ on signatures satisfying $f\circ\Phi=\Phi\circ F$ exists if and only if

$$
\Phi(x)=\Phi(y)\Longrightarrow\Phi(Fx)=\Phi(Fy).
$$

The proof defines $f(\Phi(x))=\Phi(Fx)$; the condition ensures independence from the choice of representative. Reading the answer also requires $Q=d\circ\Phi$. **The existence of $f$ and $d$ does not show that they can be constructed or executed efficiently.**

**Internal reference and self-closure: a candidate contract [A/T under conditions].** To avoid identifying the exterior signature $\Phi$ with the unit, we propose examining an internal reference $\Psi_U:X_U\to S_U$ and a declared set of internal transformations $\mathcal T_U$. For each $T\in\mathcal T_U$, the compatibility to be tested is

$$
\Psi_U(Tx)=t_T(\Psi_U(x)),
\qquad Q=d_Q\circ\Psi_U\quad(Q\in\mathcal Q_U).
$$

If transformations compose, their updates must also compose **on reachable states**: $t_{T_2\circ T_1}=t_{T_2}\circ t_{T_1}$. The internal relations $R_U$ required to be preserved and the queries $\mathcal Q_U$ used to compare internal and exterior recognition must be specified.

These equalities are **testable conditions once their objects have been defined**, not a universal definition of self-closure. They admit trivial realizations (for example, $\Psi_U=\mathrm{id}$); their mere existence therefore does not distinguish a self-referential unit from an encoding of states. The substantial review question is to identify a nontrivial condition of internal stability and continuity that remains meaningful when an exterior reference $\Phi$ changes.

## 5. Interior and exterior: what a reference preserves [T/E]

**R5: composition through a boundary.** For a graph $H$ with a labeled boundary $B$, define

$$
\Gamma_H(B)=\{c|_B:c\text{ is a valid 3-coloring of }H\}.
$$

If two regions share only $B$, their interiors are disjoint, and no additional edges join their interiors, then their union is 3-colorable exactly when their boundary signatures intersect. Adding an edge $ab$ with $a,b\in B$ filters the signature according to $c(a)\ne c(b)$.

**R5-F1 counterexample (original source).** On $V=\{0,1,2,3\}$ with boundary $B=\{0,1\}$, let $H_1$ have edges $01,02,12,03,13$ and let $H_2$ have edges $01,02,12,03$. Both admit six exterior assignments (the pairs of distinct colors on $0,1$). When the same interior edge $23$ is added, $H_1$ becomes $K_4$ and its signature becomes empty; $H_2$ retains six exterior assignments. The exterior signature was sufficient for **exterior continuations** but is insufficient for this **interior** modification. The earlier result has not failed: the family of admissible continuations has changed.

An exact enriched interface for a specified modification $uv$ is $\Sigma_H^{u,v}(B)=\{(c|_B,c(u),c(v)):c\text{ is valid}\}$. Filtering by $c(u)\ne c(v)$ and projecting back to $B$ reconstructs the new signature. This proves semantic sufficiency without establishing universally polynomial size or cost.

**R6: the circumstantial determinant.** Let $\mathcal P_3(G)$ be the family of partitions of $V$, $|V|\ge3$, into three nonempty independent classes without color names. For graphs on the same $V$:

$$
\mathcal P_3(G\cup H)=\mathcal P_3(G)\cap\mathcal P_3(H),\qquad
\Delta_G(e)=\mathcal P_3(G)\setminus\mathcal P_3(G+e).
$$

An edge $e$ is redundant in that circumstance when $\Delta_G(e)=\varnothing$. Cardinality alone does not identify the family: on five vertices, graphs with a single edge $01$ or $12$ each have 19 partitions; adding edge $01$ leaves 19 partitions in the first graph but only 14 in the second.

**Exact separator R6-T3.** If two graphs have different $\mathcal P_3$ families, choose a partition $P$ belonging to one but not the other and construct the complete tripartite graph $K_P$, whose unique admissible partition into three classes is $P$. Adjoining it distinguishes the feasibility of the two instances. Consequently, two graphs have the same feasibility answers under **all** future edge insertions on the fixed vertex set if and only if their $\mathcal P_3$ families agree. This is an exact characterization of contextual equivalence, not a polynomial-time algorithm for computing that equivalence.

The central distinction is more precise than “there is more information”: **the admitted continuations determine which interior differences a reference must preserve**. The next theorem converts this observation into an information lower bound for an explicit family.

### T-EXT-01: minimum information for exterior continuations [T/E]

**Contract and scope.** Fix $n\ge2$ labeled vertices $V=A\sqcup B$, with $|A|=\lfloor n/2\rfloor$ and $|B|=\lceil n/2\rceil$. Consider the family

$$
\mathcal H_n=\{H_E=(V,E):E\subseteq A\times B\}.
$$

Every such graph is bipartite and therefore 3-colorable. **For this proof**, the exterior interface comprises **all vertices of $V$**: a continuation may connect two new vertices to any chosen pair $u\in A$, $v\in B$. We do not claim the same lower bound for a proper interface exposing only a few interior vertices.

For every pair $u\in A$, $v\in B$, define a continuation $D_{uv}$ by adjoining two new vertices $a,b$ and exactly the five edges

$$
D_{uv}=\{ab,au,av,bu,bv\}.
$$

The query $Q(H_E\cup D_{uv})$ asks whether the augmented graph is 3-colorable. A *self-sufficient signature* $\Phi(H_E)$ must answer this query for **every** pair through decoding functions $d_{uv}$, with no additional access to the original graph unless that access is included in the representation:

$$
Q(H_E\cup D_{uv})=d_{uv}(\Phi(H_E)).
$$

**Theorem T-EXT-01 (exact contextual-state lower bound).** Under this contract, any self-sufficient signature must distinguish at least

$$
\boxed{2^{|A||B|}=2^{\lfloor n^2/4\rfloor}}
$$

different states. A fixed-length binary encoding therefore requires at least $\lfloor n^2/4\rfloor$ bits. On this family, the bit bound is tight: the adjacency matrix for pairs in $A\times B$ uses exactly this many bits. This does not establish efficient decoding for arbitrary other continuation families.

**Proof.** First, for every $E\subseteq A\times B$ and each $uv\in A\times B$,

$$
\boxed{H_E\cup D_{uv}\text{ is 3-colorable}\iff uv\notin E.}
$$

If $uv\in E$, the four vertices $a,b,u,v$ induce a $K_4$, which cannot be colored with three colors. If $uv\notin E$, assign color 0 to $A\setminus\{u\}$, color 1 to $B\setminus\{v\}$, color 2 to $u$ and $v$, and colors 0 and 1 to the new vertices $a$ and $b$, respectively. This assignment is valid: original edges run only between $A$ and $B$, the edge $uv$ is absent, and the five new edges have differently colored endpoints.

If $E\ne E'$, some pair $uv$ belongs to exactly one of the two edge sets. The continuation $D_{uv}$ gives different answers on $H_E$ and $H_{E'}$. A signature capable of answering every query cannot identify these two graphs. There are $2^{|A||B|}$ edge subsets and therefore that many distinguishable signatures. A fixed $b$-bit encoding supports at most $2^b$ states, hence $b\ge|A||B|=\lfloor n^2/4\rfloor$. $\square$

**Independent finite check [E].** The verifier `verificar_T_EXT_01.py` exhaustively checks the 16 instances on four vertices and the 512 instances on six. It tests the equivalence above for the 4 or 9 possible pairs per instance: **64 + 4,608 = 4,672 queries**, all successful, and records 16 and 512 distinct response signatures, respectively. This finite computation checks the general proof but is not its foundation.

**Relation to R5 and R6.** R5 distinguishes what a boundary signature preserves under exterior continuations and fails to preserve under interior modifications. R6 characterizes the distinctions needed for edge insertions **without adding vertices** on $V$. T-EXT-01 specifies a different contract: **adjoining two new vertices that can contact every vertex of $V$**. This family of queries recovers each individual edge of $A\times B$. It thus quantifies an exterior-reference information requirement even though recognizing 3-colorability of the original family is easy.

**Limits.** The lower bound is quadratic, not superpolynomial. It is not a time lower bound for general 3-coloring, an extra memory lower bound when the algorithm has unrestricted access to the original graph, or the same bound for a small boundary. The proof resembles distinguishable-family arguments, contextual equivalence, and communication complexity; establishing bibliographic priority requires independent review. It is a theorem with an explicit contract, not a solution to P versus NP.

## 6. Orientation, phase, and global closure: laboratory R4 [T/E]

A 3-coloring $c:V\to\mathbb F_3$ induces on each oriented edge $uv$ a tension $\varepsilon_{uv}=c(v)-c(u)\in\{\pm1\}$. The signed sum of tensions around any cycle vanishes in $\mathbb F_3$. Conversely, nowhere-zero tensions whose periods vanish on a cycle basis integrate to a coloring, unique up to a global constant on each connected component. This is the classical formulation of nowhere-zero modular tensions; the nonzero condition retains the combinatorial character of the problem.

For a closed, connected, orientable triangulated surface with connected face dual, R4 distinguishes face closure from periods on homology: each triangle may close without the tension being a global coboundary. On the periodic triangulated torus $T(n,m)$ in the laboratory, the orientation of the $\mathbb Z^2$ covering is fixed together with the local expression $c(i,j)=i-j\pmod3$. Along an edge from $(i,j)$ to $(i+1,j)$ the increment is $+1$; along one from $(i,j)$ to $(i,j+1)$ it is $-1$. Therefore the fundamental paths oriented in those directions have periods

$$
H_x=n\pmod3,\qquad H_y=-m\pmod3.
$$

When those periods do not vanish, $c(i,j)$ is defined on the covering space but **does not descend** to a well-defined coloring of the periodic torus. Reversing both tension signs reverses both periods without changing their vanishing condition. Under the stated contract, $T(n,m)$ is 3-colorable exactly when $3\mid n$ and $3\mid m$; $T(4,4)$ has locally closing faces but is incompatible, whereas $T(6,6)$ admits six colorings.

This illustrates an important distinction suggested by the cube: **local references may be consistent while a global path retains a residual obstruction**. R4 yields a small signature and an efficient procedure for this family of tori, not a universal algorithm for arbitrary graphs.

## 7. R–04: indeterminate query, determination radius, and certificate [T/E]

Given a fiber $F$ of compatible solutions and a relational query $q$, R–04 distinguishes **indeterminacy** ($F\ne\varnothing$ and $|q(F)|\ge2$), **determination** ($F\ne\varnothing$ and $|q(F)|=1$), and **incompatibility** ($F=\varnothing$). In 3-coloring, the canonical bit is $q_{uv}(c)=[c(u)=c(v)]$. Adding constraints can only shrink the solution set; a determined answer cannot switch to its opposite without the fiber first becoming empty.

In the diamond $K_4-e$, the two nonadjacent tips must share the third color. Identifying them preserves 3-colorability. A closure procedure applying this inference terminates in polynomial time and detects every odd wheel; it does not activate on triangle-free graphs, a class in which 3-coloring remains NP-complete.

The **determination radius** $\rho(G)$ is the minimum number of vertices in a proper induced 3-colorable subgraph in which some nonadjacent pair is determined; if no such subgraph exists, set $\rho(G)=\infty$. It measures the support needed for a query in this laboratory; **by definition it is not the constitutive radius of every unit in the program**.

| Graph family | Vertices | $\rho(G)$ | Incompatibility argument |
|:--|--:|--:|:--|
| Odd wheel $W_r$ ($r\ge5$) | $r+1$ | $4$ [T] | Successive diamonds |
| $M(C_5)$ | $11$ | $9$ [E] | Recoloring the odd cycle |
| $M(C_7)$ | $15$ | $12$ [E] | Recoloring the odd cycle |
| $M(C_9)$ | $19$ | $16$ [E] | Recoloring the odd cycle |
| $M(C_{11})$ | $23$ | $20$ [E] | Recoloring the odd cycle |

The Mycielski values are reported finite checks; the formula $\rho(M(C_r))=2r-2$ for odd $r\ge7$ remains a conjecture. The graphs $M(C_r)$ are triangle-free and not 3-colorable, but deleting any vertex makes them 3-colorable. No fixed-size window inspecting only the colorability of induced subgraphs detects all incompatibilities.

**Certificate contrast.** For $1\le i\le r-2$, the bags

$$
B_i=\{w,v_0,u_0,v_i,u_i,v_{i+1},u_{i+1}\}
$$

form a path decomposition of $M(C_r)$ of width at most 6. With the usual Boolean encoding using three color variables per vertex, resolution elimination compatible with those bags yields refutations of width at most 21 and size polynomial in $r$. Both the construction and its resolution step are explicitly submitted for technical review: **a growing determination radius can coexist with a short certificate** in this family. This does not imply an asymptotic bound for general 3-coloring.

## 8. P versus NP: the cost of preservation and decision [T/A]

To remove a terminological ambiguity, we call an **exact relational procedure** an encodable representation and a collection of uniform operations $\Pi=(\Phi,\operatorname{Init},\operatorname{Update},\operatorname{Read},\operatorname{Certify})$ such that each edge insertion is represented correctly by the update operation and the reading operation correctly decides 3-colorability. `Certify` is optional; when used, its format and verification must be specified. The time, memory, precision, and bit cost of every operation are counted. A **polynomial-time** procedure requires uniform polynomial bounds for the entire chain. The original graph already has a compact representation and can be updated quickly; this does not provide a known polynomial-time procedure for deciding its general 3-colorability.

The existence of an entirely polynomial-time decision procedure for 3-coloring would prove $P=NP$. Instead, the program examines **families of operators and their limitations**, without identifying any particular engine with the class of all algorithms.

N1-A records the cost of explicitly enumerating all three-color assignments of a bag of width $w$: $3^{w+1}$ candidates under that contract. Changing the elimination order does not automatically remove the limitation of this extensional representation.

**N1-B [cited result; review pending].** The historical document `N1_B_CERTIFICADOS_Y_PRIORIDAD_v2_8.md` claims that negative runs of the O2c engine can be converted into resolution refutations, with a size bound of the form $\frac32\,\texttt{total\_candidates}$. **This request does not fully define the counter `total_candidates` or independently revalidate the coefficient $3/2$**. The engine specification, instance encoding, and simulation argument in the technical source are essential. The claim is not presented as a bound for arbitrary methods.

**Transfer by simulation (conditional scheme).** If every negative run of a procedure $\Pi$ of running time $T$ can be uniformly converted into a refutation in a proof system $S$ of size at most $p(T+|G|)$, then a superpolynomial lower bound for $S$ on a particular family transfers to those runs of $\Pi$, under the same encoding. The decisive step is to **prove** the simulation for the proposed procedure; similarity between images is insufficient.

Our proposed testing sequence is **represent → compare → incorporate → refine → join → project → detect emptiness → certify**. Each operation must specify the query and continuations it preserves, the provenance information retained, and the cost of execution and reading. Parity with Gaussian elimination, the diamond rule, R4, and triangle-free adversarial families provide distinct test cases. The absence of a known simulation does not prove that an operator escapes all known proof systems.

## 9. ROSI: critical reflection on language and provenance

ROSI should inspect the relationships among **concept, reference, determinant, formalization, evidence, counterexample, and status**. Its task in this review is not to decide a problem by authority or invent further entities; it is to detect unjustified changes of level. An exterior indistinguishability class is not a complete interior unit; an ontological radius is not automatically $\rho(G)$; a compact signature does not guarantee cheap computation; coincident images do not establish self-closure; and geometric closure does not imply a complexity bound.

Traceability is maintained through MF-97/MF-106 (equivalence and updating), O59/CME (mirrors and groups), R–01 (modular normalization), R4 (tensions and periods), R5 (interior/exterior), R6 (circumstantial novelty), R–04 (indeterminacy, radius, and certificate), E25/E26, N1, and LAB-CONV. The Yang–Mills and Navier–Stokes realizations supply specific analogies concerning insufficient observables (noncommuting products and projections with residual terms). Their physical claims, however, require independent assumptions and proofs and are not premises of the P/NP branch.

## 10. Questions for independent review

We welcome partial, reasoned responses. Each question can be studied without endorsing the entire program.

1. **Ontology and formalization.** Which mathematical structure best expresses a unit with an internal self-reference and a declared relational reach? What nontrivial condition on $\Psi_U$, internal relations, and their transformations distinguishes it from the identity encoding of states or an exterior observational-equivalence class?
2. **Radius and self-closure.** Which testable conditions on internal references, transformations, composition, and observables characterize self-closure in each realization? How can internal continuity be distinguished from the mere determination of an exterior query?
3. **Mirrors.** Are the generators, the orbits of $\rho_L$, the CME-001–003 counts, and the $(2,3,k)$ classification correct? Which observables distinguish oppositely oriented paths arriving at the same focus?
4. **Normalization.** Do the modular projections of R–01 preserve exactly the claimed relations? Under what conditions is injectivity lost even though projection compatibility remains?
5. **R4.** Are the characterization by nowhere-zero $\mathbb F_3$ tensions, the distinction between face closure and homological periods, and the 3-colorability formula for $T(n,m)$ correct? Are the signs of $H_x,H_y$ preserved under the stated orientation, and what are the most direct precedents?
6. **Interfaces and recursion.** Does R5 correctly identify which information is sufficient for exterior continuations and why it fails for interior modifications? Which provenance-aware representation would permit exact, updatable recursive composition?
7. **Circumstantial novelty.** Does the family $\mathcal P_3(G)$ from R6 characterize every admitted future edge insertion? Which symbolic or intensional representations could maintain the same distinctions without enumerating every partition explicitly?
8. **Indeterminacy and radius.** Are the R–04 states, the diamond inference, and the $\rho$ measurements correct? Can $\rho(M(C_r))=2r-2$ be proved or refuted for odd $r\ge7$?
9. **Global certificates.** Are the path decomposition of width $\le6$ and the resolution refutation of width $\le21$ for $M(C_r)$ valid under the stated encoding? Is a stronger prior result known?
10. **Limits of specific engines.** Does N1-B hold under the original definition of `total_candidates`, its invariants, and the O2c encoding? Which proof systems polynomially simulate a proposed updating/closure operator?
11. **Complexity.** What theorem, bound, or separation for a *defined class of procedures* would turn reference, novelty, and closure into a new statement about computational resources, without inferring it from the geometry of reflections?
12. **Bibliographic position and ROSI.** Which parts of the proposed synthesis are already entirely expressed by automata theory, CSP, cohomology, or proof complexity? Which specific statements merit independent examination as potential new contributions?
13. **T-EXT-01 and reference size.** Is the bound of $2^{\lfloor n^2/4\rfloor}$ distinct signatures and $\lfloor n^2/4\rfloor$ bits correct for the bipartite family with a full interface and continuations $D_{uv}$? Which previous theorems in contextual equivalence, communication complexity, or boundaried graphs subsume it? What lower bounds survive when only a proper boundary of size $b<n$ is accessible?

## 11. Materials, reproducibility, and source status

**Main document:** the present revised request. A one-page executive summary provides a reading guide but **does not replace the proofs**. Technical appendices are identified files in the program's history, not results regenerated merely by copying this manuscript. Existing checks belong to their respective programs and inputs: O59 and CME-001–003; the PNP–CME r3 supplement; R4; R–04; R5; R6; N1; and LAB-CONV. Reproducing a result requires its contract, source code, archived output, and source version.

**Publication status as recorded on October 30:** at the time of the Spanish edition, the public repository linked above displayed its October 24 edition and October 27 Yang–Mills supplement; it was not assumed that the October 28–30 supplements had been merged into `main`. The Spanish publication package therefore contained the request and relevant sources. A GitHub publication of this English edition should identify the commit and use links to files that actually exist in the published tree. **This English translation does not itself constitute a GitHub publication.**

**T-EXT-01 check for this edition.** The files `verificar_T_EXT_01.py` and `RESULTADOS_T_EXT_01.json` accompany the Spanish proof package. They record the 4,672 queries and the distinct signatures for $n=4,6$.

**Additional check from the Spanish review.** The orientation of R4 was verified directly with $c(i,j)=i-j$ on the covering. The verifier `verificar_fase_holonomia.py` was rerun and its JSON matched the archived October 29 result byte for byte. Other proofs retain their original historical status and contracts. This translation does not assert that all historical verifiers have been independently rerun again.

**How to respond.** We welcome responses in English or Spanish through a repository issue or in the invitation thread. Identifying an assumption, presenting a counterexample, proving an identity, checking a script, locating relevant literature, or explaining a limitation for a class of algorithms are independent and verifiable contributions. There is no deadline.

## 12. References and provenance

**Program sources.** *The Self-Referential Unit and Its Relational Radius* (October 30, 2026); MF-97/MF-106; R–01 (October 23); O59 and CME-001–003; E25/E26; PNP–CME r3 supplement (October 28); R4 *Orientation, Phase Difference, and the Condition for Global Closure* (October 29); R5 *Same Exterior Reference, Different Interiors* (October 29); R6 *The Circumstantial Determinant* (October 29); T-EXT-01 *Contextual Information Lower Bound with a Full Interface* (October 30, this edition); R–04 *Point of Indeterminacy, Closure, and Counterexamples in 3-Coloring* (October 29); N1-A/N1-B; LAB-CONV; and ROSI.

**Comparative literature.** Coxeter (1934), reflection groups; Świerczkowski (1959), tetrahedral chains; Nerode (1958), continuation equivalence; Mycielski (1955), chromatic graphs; Hell and Nešetřil (1990), $H$-coloring; Maffray and Preissmann (1996), triangle-free 3-coloring; Bulatov (2017) and Zhuk (2020), the CSP dichotomy; Beame, Culberson, Mitchell, and Moore (2005), resolution complexity of random graph coloring; Ben-Sasson and Wigderson (2001), proof length and width; Lauria and Nordström (2017), barriers for algebraic methods.
