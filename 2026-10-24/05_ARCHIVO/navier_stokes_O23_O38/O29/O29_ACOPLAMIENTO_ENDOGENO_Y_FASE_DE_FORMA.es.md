# O29 — Acoplamiento endógeno y fase de la forma en Navier–Stokes

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego** · 19 de octubre de 2026  
**Estatuto:** suplemento independiente para contraste. [O] interpretación; [D] contrato; [T] teorema condicionado; [E] cálculo control; [F] falsador; [A] pregunta abierta.  
**Edición:** NO modificar la Imagen Total, el núcleo ni los suplementos previos.

## 0. Problema y respuesta precisa

O28 definió el residuo de fases `ψ=qφ_A-pφ_B` e introdujo como **modelo de trabajo** `ψdot=δ-K sinψ`. Eso NO identifica el acoplamiento real entre remolinos. O29 deriva de la ecuación 2D NS un **funcional de acoplamiento no local** que depende de las formas íntegras y ofrece una fase geométrica de la forma, cuando está definida. **No se deduce un coeficiente escalar universal K, ni se demuestra bloqueo, fusión o regularidad 3D.**

La secuencia ontológica sigue siendo `diferencia -> comparación -> módulo/residuo -> posible cierre propio`, sin reconocer, elegir o perseguir sincronía. La *forma* es información relacional de un remolino dentro del flujo; una representación matemática la realiza por los momentos de la distribución de vorticidad.

## 1. Contrato geométrico [D]

Trabajamos en `R²` con NS no forzado, viscosidad `ν>0`, vorticidad escalar `ω=∂₁u₂-∂₂u₁` y Biot–Savart:

```
∂t ω + u·∇ω = ν Δω ,       u = K_BS * ω,
K_BS(z) = Jz / (2π|z|²),     J(x,y)=(-y,x).
```

Se suponen regularidad y decaimiento suficientes para integrar por partes, finitud de los primeros y segundos momentos, y dos componentes iniciales etiquetadas `ω_A^0,ω_B^0` con circulación `Γ_i=∫ω_i ≠0`. Dado el campo total `u`, cada etiqueta evoluciona por la **misma** advección-difusión lineal: `∂tω_i+u·∇ω_i=νΔω_i`. Por unicidad, su suma vuelve a ser `ω`. Este marcado es un **contrato de representación**, no una separación única exigida por la física. La difusión puede solapar los componentes.

Si cada `ω_i` tiene signo fijo, `c_i=Γ_i⁻¹∫x ω_i` es centro de vorticidad usual; para distribuciones firmadas es un centro algebraico, no necesariamente un punto dentro de la estructura.

## 2. T1 — Interacción exacta entre centros [T]

Sea `u_i=K_BS*ω_i`, `r=c_A-c_B` y

```
I_AB = ∬ K_BS(x-y) ω_A(x) ω_B(y) dxdy.
```

**Teorema.** La circulación de cada población es constante y

```
ċ_A = I_AB / Γ_A,
ċ_B = -I_AB / Γ_B,
ṙ = (1/Γ_A + 1/Γ_B) I_AB.
```

**Prueba.** Integrando `∂tω_i` se anulan transporte y difusión. Multiplicando por `x`, `d/dt ∫ xω_i = ∫u ω_i` (el segundo momento del laplaciano de x es cero). El término propio `∫(K*ω_i)ω_i` se anula por la antisimetría `K(z)=-K(-z)`. Los cruzados son `I_AB` y `-I_AB`, respectivamente. Dividir por `Γ_i` demuestra las tres identidades. ∎

Si `r ≠ 0`, el ángulo orbital `φ_orb=arg(r)` y la distancia `d=|r|` satisfacen:

```
φdot_orb = cross(r,ṙ)/|r|²,
ddot      = (r·ṙ)/|r|.
```

Estas expresiones son **exactas para el NS 2D etiquetado**, pero no definen aún dos fases internas independientes. `I_AB` **no es un K escalar**. Requiere conocer la distribución de la vorticidad: su forma es parte del acoplamiento.

**Caso límite puntual.** Para vórtices concentrados de intensidades `Γ_A,Γ_B` en centros separados `d>0`, formalmente (o en el sistema clásico de vórtices puntuales)

```
I_AB = Γ_A Γ_B K_BS(r),
ṙ = (Γ_A + Γ_B) K_BS(r),
φdot_orb = (Γ_A + Γ_B)/(2πd²),     ddot = 0.
```

Las ecuaciones puntuales son un **límite/modelo Euler**, no soluciones suaves con `ν>0` a tiempos positivos. Si `Γ_A+Γ_B=0`, el par puede trasladarse manteniendo el vector separación; no equivale a ausencia de interacción.

## 3. T2 — Radios y circulación no agotan el acoplamiento [T/F]

Considérese la interacción instantánea de una distribución A concentrada en el origen con B compuesta por dos masas de mitad de circulación colocadas simétricamente respecto del centro `(2,0)` a distancia `1`:

- **Forma longitudinal:** B en `(1,0)` y `(3,0)`.
- **Forma transversal:** B en `(2,1)` y `(2,-1)`.

Las dos tienen idéntica circulación total, centro y **segundo momento radial** de B igual a `1`, pero `I_AB/(Γ_AΓ_B)` vale, respectivamente:

```
I_long/(Γ_AΓ_B) = (0,-1/(3π)),
I_trans/(Γ_AΓ_B)= (0,-1/(5π)).
```

A iguales `Γ_A=Γ_B=1` y `|r|=2`, la velocidad angular orbital del sistema puntual es `1/(3π)` frente a `1/(5π)`. La diferencia procede exclusivamente de la **orientación de la forma**.

No es necesario recurrir a distribuciones singulares: reemplazar cada masa puntual por una gaussiana suave estrecha con la misma varianza isotrópica produce, para ambas configuraciones, **exactamente los mismos centros, circulaciones y segundos momentos radiales**. Al hacer tender la anchura a cero, las integrales de interacción tienden a los valores anteriores y siguen siendo distintas para anchura positiva suficientemente pequeña. Tales gaussianas son **datos iniciales suaves admisibles** para NS 2D; no se afirma que mantengan esa forma exacta durante la evolución.

**Falsador:** cualquier cierre `I_AB=F(Γ_A,Γ_B,c_A,c_B,m_A,m_B)` independiente de orientación/forma falla en esta familia. No todo remolino admite una fase orientacional observable, pero cuando la admite esa información no es prescindible.

## 4. T3 — Fase de forma extraída de NS [T]

Introduzcamos la coordenada compleja `z=x₁+i x₂`, `C_i=c_{i,1}+ic_{i,2}` y la velocidad compleja `U=u₁+i u₂`. Definamos la firma cuadrupolar de la forma:

```
Q_i = (1/Γ_i) ∫(z-C_i)² ω_i(x) dx ∈ C.
```

La parte real distingue alargamiento entre ejes y la parte imaginaria correlaciones transversales. Cuando `Q_i ≠ 0`, `φ_i=arg Q_i (mod 2π)` define una fase de **orientación de la forma** (el eje geométrico tiene orientación `φ_i/2 mod π`). Una estructura circular ideal puede satisfacer `Q_i=0`: entonces **la fase no existe**, sin que desaparezca la estructura física.

**Teorema.** Para datos etiquetados suaves y momentos finitos:

```
Qdot_i = (2/Γ_i) ∫ (z-C_i) U(z) ω_i(x) dx.
φdot_i = 2 Im{ [∫(z-C_i)U(z)ω_i(x)dx]/(Γ_i Q_i) },  Q_i ≠0.
```

**Prueba.** Derivar el momento bajo la ecuación de advección-difusión. La dependencia de `C_i(t)` no aporta términos porque `∫(z-C_i)ω_i=0`. El término difusivo instantáneo es cero, ya que el polinomio `(z-C_i)²` es armónico en las dos coordenadas reales: `Δ(z-C_i)²=0`. La contribución de transporte es `2∫(z-C_i)Uω_i`. La fase se deriva mediante `d/dt arg Q = Im(Qdot/Q)`. ∎

**No confundir:** la anulación del término difusivo directo en `Qdot` no significa que viscosidad no afecte la forma o la fase, porque la evolución de `ω_i` y de `U` depende de `ν`.

La integral se descompone exactamente:

```
U=U_A+U_B,
Ω_i^{self}=2 Im [∫(z-C_i)U_i ω_i/(Γ_i Q_i)],
Ω_i^{cross}=2 Im [∫(z-C_i)U_j ω_i/(Γ_i Q_i)].
φdot_i= Ω_i^{self}+Ω_i^{cross}.
```

Para un módulo entero `p:q`, la fase relativa de formas satisface **exactamente**

```
ψ=qφ_A-pφ_B,
ψdot=qΩ_A^{self}-pΩ_B^{self}
     + qΩ_A^{cross}-pΩ_B^{cross}.
```

El segundo renglón constituye el **acoplamiento endógeno** de Navier–Stokes para esta firma. No es, en general, función exclusiva de `ψ`, ni igual a `-K sinψ`; podría cambiar de signo o depender del resto de la estructura. La fase es de FORMA (momentos), no automáticamente la frecuencia angular del material, la frecuencia espectral `v_*/R` ni el ángulo orbital del par.

## 5. T4 — Anchura viscosa y frecuencia orbital en formas gaussianas [T/D]

Si, en **un instante dado**, las distribuciones `ω_i` son gaussianas isótropas de centros `c_i`, circulaciones `Γ_i` y covarianzas `σ_i² I₂`, la integral exacta del Teorema 1 se evalúa como

```
I_AB = Γ_AΓ_B K_BS(r) [1-exp(-d²/(2(σ_A²+σ_B²)))],
φdot_orb = (Γ_A+Γ_B)/(2π d²)
           ·[1-exp(-d²/(2(σ_A²+σ_B²)))].
```

Prueba: la diferencia de posiciones ponderadas por ambas gaussianas es gaussiana de centro `r` y covarianza `(σ_A²+σ_B²)I`. El campo inducido por una gaussiana radial de circulación unitaria encierra fracción `1-exp(-d²/(2s²))` a distancia `d` por Stokes/Biot–Savart. ∎

Se trata de una **identidad instantánea** y NO afirma que la suma de dos gaussianas siga siendo solución gaussiana exacta durante su interacción: los núcleos se deforman y se difunden. El parámetro de sincronización **no es** `σ`, `d` o `Γ` por sí solo.

## 6. Precisión respecto de O28 y del núcleo [O]

- **Forma propia:** la distribución de vorticidad y sus momentos representan una relación independiente dentro del marco del flujo, no una sustancia aparte.
- **Módulo:** relación entera entre dos fases *declaradas*, cuando ambas tienen fase; la aritmética no implica atracción.
- **Comparación:** `ψ=qφ_A-pφ_B`, sin observador agente; su tasa depende del campo completo de NS.
- **Comunes/trama:** mismo campo total `u` advecta ambas poblaciones etiquetadas; su interacción usa Biot–Savart.
- **Resto:** el par de fases y radios no determina el funcional cruzado; orientación, distribución de vorticidad y entorno permanecen relevantes.
- **Cierre propio:** identidad de una estructura persistente para una consulta definida; `ψdot=0` instantáneo NO demuestra estabilidad, persistencia ni fusión física.
- **Singularidad:** foco de referencia en lenguaje ontológico, no explosión de una norma PDE.

El resultado concuerda con el principio de conservar diferencia sin inventar nueva dimensión: pueden existir diferencias transversales de forma dentro del mismo plano. **El núcleo ontológico no implica matemáticamente la ley de Biot–Savart; la ley entra aquí como dinámica física conocida y comprobada.**

## 7. Límite de dimensiones y pruebas pendientes [A/F]

En 3D, `ω` es un campo vectorial y satisface `∂tω+u·∇ω=(ω·∇)u+νΔω`: estiramiento y cambio de orientación. No se obtiene por sustitución la ecuación 2D de centros y fases cuadrupolares. Una extensión 3D requiere una firma de forma e identidad de vórtice independiente de un plano privilegiado y control de estiramiento, viscosidad, transporte y deformación.

**Obligaciones:** (1) declarar una segmentación de vórtices reproducible y estable; (2) evaluar `Ω_i^{cross}` antes de observar supuesta sincronización; (3) probar que un canal modular produce un atractor o una coherencia objetiva en una clase concreta de NS; (4) comparar contra cierres rivales sin el término cruzado y contra casos sin fase definida; (5) analizar en 3D un tensor de forma, no atribuir una perpendicular física al mero residuo informacional.

**No se ha demostrado** sincronización universal, fusión, regularidad global 3D ni `v_*=c`. La descomposición `Ω_i=Ω_i^{self}+Ω_i^{cross}` es exacta, pero no reduce la dinámica a un `K` escalar.

## 8. Fuentes y genealogía

Internas: Núcleo generativo canónico; MF-43; O25–O28, en particular O28 §7 que exige derivar el acoplamiento sin ajuste retrospectivo.

Externas: Thierry Gallay (2012), *Stability and interaction of vortices in two-dimensional viscous flows*, DCDS-S 5(6), 1091–1131, DOI 10.3934/dcdss.2012.5.1091.  
Gallay et al., *On the dynamics of vortices in viscous 2D flows*, Mathematische Annalen, DOI 10.1007/s00208-023-02568-z.  
Estos trabajos contextualizan el campo y el límite de vórtices puntuales; las identidades T1–T4 se demuestran dentro del contrato aquí declarado, no se atribuyen como nuevas leyes físicas descubiertas.
