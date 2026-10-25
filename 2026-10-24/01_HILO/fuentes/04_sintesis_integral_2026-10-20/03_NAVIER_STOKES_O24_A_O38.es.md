# 03. Navier–Stokes: estado integrado, O24–O38

**No-go editorial:** ningún resultado de O24–O38 resuelve la existencia y suavidad global de Navier–Stokes 3D. La mayoría de sus pruebas nuevas viven en vorticidad **bidimensional**, no en 3D. La rama anterior `03_navier_stokes/` conserva por separado identidades y observaciones DNS en 3D, límites numéricos y testigos contrarios.

## 1. Ecuación y diccionario [D]

`∂t u+(u·∇)u=−∇p+νΔu`, `div u=0`. En 2D, `∂tω+u·∇ω=νΔω`, `u=K_BS*ω`, y en 3D hay estiramiento `(ω·∇)u`, ausente en el caso escalar 2D.

Cada remolino es **candidato** a foco relacional local de forma propia; la forma puede describirse por distribución, radio cuadrático, momentos superiores o coherencia de vorticidad. No debe equipararse a singularidad matemática ni a un único contorno material.

## 2. Genealogía de resultados

| Bloque | Objeto y resultado | Alcance explícito |
|---|---|---|
| O24–O25 | espejos/radio dinámico, coordenadas móviles, `ℓ=√(A/B)`, identidad para `dot n` | reparametrización exacta bajo regularidad; no nueva ecuación física ni regularidad global |
| O26 | dos cizallas exactas con H,A,B iguales, C y `dot n` diferentes; jerarquía espectral | **no suficiencia** de la firma truncada elegida |
| O27 | `Sξ=αξ+η`, `η⊥ξ` en 3D | descomposición geométrica exacta; no cuarta dimensión física |
| O28 | retorno racional p:q y bloqueo de fase con K **modelo declarado** | K no proviene aún del flujo |
| O29–O30 | Biot–Savart, centros, cuadrupolos, balance global `Γ₁S₁+Γ₂S₂+Γ₁Γ₂ d²/Γ = M₀+4νΓt` | NS 2D positivo/localizado; no flujo rígido perpetuo |
| O31 | cotas de separación y concentración etiquetadas | horizonte finito suficiente; etiquetas no son vórtices únicos |
| O32 | evolución exacta `dot Q_i = (2/Γ_i)∫(z−C_i)Uω_i`, persistencia de anisotropía | fase indefinida cuando Q=0 |
| O33 | simetrías rotacionales de m componentes y cancelación de momentos bajos | persistencia de simetría **preexistente**, no nacimiento de simetría |
| O34 | forma gaussiana auto-semejante y diferencia física invisible en escala creciente | difusión puede acercar formas sin conservar dos remolinos |
| O35–O36 | reducción inicial **unilateral** de discrepancia de orientación, robustez existencial breve | no atractor bilateral ni sincronización eterna |
| O37 | solapamiento de etiquetas monótono por difusión | no es observable intrínseco de ω total; no prueba identidad común física |
| O38 | transición intrínseca de silla a máximo de ω total en NS 2D para amplitud positiva pequeña | aparece también por **calor lineal**; no prueba mecanismo no lineal universal |

## 3. Contratos de medida [T]

Para `ω_i≥0`, circulación `Γ_i=∫ω_i`, centro `c_i=Γ_i⁻¹∫xω_i`, dispersión `S_i=Γ_i⁻¹∫|x−c_i|²ω_i`. En 2D con suficiente decaimiento y sin forzamiento la circulación es constante. La suma exacta de momentos (O30) relaciona forma y separación, con aporte viscoso creciente.

Para `Q_i=Γ_i⁻¹∫(z−C_i)²ω_i`, el argumento de `Q_i` es una fase de *orientación cuadrupolar*, no la fase de giro de las partículas ni una frecuencia material universal; `Q_i=0` deja esa fase indefinida sin eliminar al vórtice.

## 4. Comparación modular intrínseca [T condicional]

Para momentos no nulos y `r=C_A−C_B≠0`, la combinación:

`Z_{p:q}=(Q_A/|Q_A|)^q (conj Q_B/|Q_B|)^p (conj r/|r|)^{2(q−p)}`

es invariante ante traslación, rotación y homotecia común. `E=1−Re Z` mide una discrepancia **según contrato**. Un valor `dot E(0)<0` garantiza acercamiento inicial, y por continuidad una ventana finita local. No implica `E(t)→0` ni robustez ante todas las perturbaciones.

## 5. Mezcla y nuevo foco no son sincronización [T, N]

O37: `O(t)=∫ω_Aω_B/(ω_A+ω_B)` tiene derivada no negativa `2ν∫ω|∇(ω_A/ω)|²` bajo los datos positivos. Cambia si reetiquetamos una misma ω total: no acredita un foco *intrínseco*.

O38: el perfil lineal de dos gaussianas iguales separadas en `±a` tiene `s²(t)=σ²+2νt`; en el centro, `λ_x=(a²−s²)/s⁴`, `λ_y=−1/s²`. Cruza de silla a máximo si `s²=a²`. Por continuidad parabólica, un flujo NS 2D de circulación suficientemente pequeña presenta también ese cambio en alguna ventana. **Se debe comprobar la pertenencia al sector de simetría**; la prueba no demuestra persistencia de ambos máximos originales durante la transición.

## 6. Significado ontológico y falsadores

**[LECTURA]** Las distinciones propias pueden permanecer dentro de una trama; un foco colectivo nuevo puede aparecer cuando la proyección total cambia de estructura. **[FALSADOR]** Ese cambio sucede asimismo con calor lineal sin acoplamiento no abeliano: crear un máximo no equivale a demostrar sincronización ni gap de Yang–Mills. Una partición que conserva etiquetas tampoco es intrínseca. Mantener ambos controles.

## 7. Obligación pendiente

Una demostración de sincronización estable de dos identidades físicas requiere un observable intrínseco, región dinámica invariante o función de Lyapunov que estabilice una relación, un control de separación/forma y una justificación de que sobreviven las dos identidades. En 3D se necesita además controlar estiramiento, no extrapolar resultados de 2D.
