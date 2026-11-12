# Tres resultados de integración y pruebas

**Naturaleza:** proposiciones elementales para hacer operativa la continuidad entre referencias. Son resultados matemáticos bajo hipótesis precisas, sin atribución de originalidad universal. La prueba de actualización de firmas ya aparece en la construcción anterior.

## Proposición A — Conservación y novedad por factorización [T]

Sea `X` un conjunto no vacío, `Φ:X→S` una firma y `q:X→Y` una consulta. Son equivalentes:

1. Existe `g:Φ(X)→Y` tal que `q=g∘Φ`.
2. Para cualesquiera `x,y∈X`, si `Φ(x)=Φ(y)` entonces `q(x)=q(y)`.

**Prueba.** 1 ⇒ 2 es inmediata al aplicar `g`. Para 2 ⇒ 1, defina `g(s)=q(x)` para cualquier representante `x` de la fibra `Φ^{-1}(s)`; la condición asegura independencia del representante. □

**Falsador de recuperación.** Un par `x,y` con `Φ(x)=Φ(y)` y `q(x)≠q(y)` prueba que se necesita información adicional para responder la nueva consulta. Este criterio ya figuraba en el borrador rector del 11-XI; aquí queda asociado a una magnitud precisa.

## Proposición B — Cuántos bits faltan al cambiar de referencia [T]

Sean `X` un conjunto **finito, no vacío**, `Φ:X→S` y `q:X→Y`. Para cada firma presente `s∈Φ(X)` defina

\[
k_s=\left|\{q(x):\Phi(x)=s\}\right|,\qquad k=\max_{s\in\Phi(X)}k_s.
\]

Se busca un suplemento fijo `h:X→{0,1}^b` tal que `q` pueda recuperarse exactamente del par `(Φ,h)`. El mínimo posible de bits suplementarios es

\[
\boxed{b_{\min}=\left\lceil\log_2 k\right\rceil}.
\]

**Prueba de necesidad.** En una fibra con `k` valores distintos de consulta, si dos de esos valores recibieran la misma etiqueta `h`, el par `(Φ,h)` sería igual y ninguna lectura podría separarlos. Se necesitan `k` etiquetas y, por tanto, `2^b≥k`.

**Prueba de suficiencia.** En cada fibra `Φ^{-1}(s)`, enumere sus valores distintos de `q` e identifíquelos con códigos de `b` bits. Como el lector conoce `s`, puede reutilizar los mismos códigos en fibras diferentes. Así `(Φ,h)` permite recuperar `q` y alcanza la cota. □

**Alcance.** Es una cota de **longitud fija de etiqueta complementaria**, permitiendo que la codificación dependa de la antigua firma. La tabla de codificación y los algoritmos para construirla **tienen costo propio**; la cota no implica construcción eficiente ni disminución de complejidad de una familia general.

**Caso espejo.** Para `X={1/4,9/4}`, la antigua firma `ρ_1(x)` reúne ambos estados; la consulta nueva `ρ_2(x)` los separa. La fibra antigua contiene dos nuevos valores: `k=2`, `b_min=1` bit.

**Caso modular.** Para `X={0,…,29}`, antigua referencia `Φ(x)=x mod 6` y consulta nueva `q(x)=x mod 10`, cada fibra antigua contiene cinco valores distintos de `q`; `k=5` y `b_min=3` bits. La referencia conjunta equivale a distinguir residuos módulo `mcm(6,10)=30`.

## Proposición C — Refinamiento por nuevas consultas [T]

Si `𝒬⊆𝒬'` son familias de consultas sobre el mismo `X`, entonces

\[
\sim_{\mathcal Q'}\ \subseteq\ \sim_{\mathcal Q},\qquad
|X/\sim_{\mathcal Q'}|\ge |X/\sim_{\mathcal Q}|,
\]

cuando `X` es finito.

**Prueba.** Igualdad de respuesta para toda consulta de `𝒬'` implica igualdad para toda consulta de `𝒬`. La nueva partición refina o conserva la anterior; no puede tener menos clases. □

**Separación importante.** La conclusión se refiere a **añadir preguntas con la referencia fija**. Si cambia además el grupo de simetrías, el dominio o las reglas de continuidad, la inclusión de particiones requiere prueba independiente. En particular, mover una pared cambia la firma y no se trata sin más de añadir una consulta dentro del mismo contrato.

## Condición para actualizar la firma [T: resultado anterior]

Sea `F:X→X`. Existe `f` sobre la imagen de `Φ` con `Φ∘F=f∘Φ` si y solo si

\[
\Phi(x)=\Phi(y)\implies\Phi(F(x))=\Phi(F(y)).
\]

Se prueba definiendo `f(Φ(x))=Φ(F(x))` y comprobando independencia del representante. En `X=Z_4`, la paridad es estable bajo sumar 1; en `X=Z_5`, los estados `0` y `4` tienen paridad igual, pero sus sucesores `1` y `0` tienen distinta paridad. La misma firma deja de ser una interfaz actualizable en el segundo contrato.

## Ejemplo de cierre relativo, no autorreferencia demostrada [F]

Una firma terminal `Φ(x)=Q(x)` siempre factoriza la consulta `Q`; puede construirse computando directamente `Q(x)`. Esa suficiencia de lectura **no demuestra** economía de cálculo ni cierre propio. Funciona como control negativo obligatorio antes de transportar una propiedad semántica a una tesis física u ontológica.
