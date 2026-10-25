# Suplemento editorial — Ciclo base, recurrencia, tiempo relacional y posible puente de gravedad

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 24 de octubre de 2026**  
**Carácter:** integración para la edición de publicación, aditiva, sin modificar los documentos originales de MF-43, O45, GR3 y MF-44B.

## 1. Premisa narrativa recuperada [O]

> El ritmo al que suceden los procesos es lo que entendemos como tiempo. El ciclo base es la referencia; los demás ciclos aparecen como múltiplos o relaciones respecto de ella.

En el programa, esta premisa continúa el reloj como comparación de recurrencias y la metáfora del espejo móvil. **No significa que una velocidad dimensional sea literalmente una frecuencia.** La identificación eventual de la constante límite con la velocidad de la luz es un puente físico adicional.

La progresión ontológica se conserva: unidad no comparada → primera diferencia → reflexión → recurrencia de un cierre propio → ciclo elegido como referencia → comparación de ritmos → tiempo medido. La gravedad se investiga después, no como definición de la distancia ni como sinónimo de sincronización.

## 2. MF-43: construcción discreta exacta [T bajo hipótesis]

Para modos de una cadena homogénea con una regla reversible local, el modelo fija

$$
x_{j,n+1}-2x_{j,n}+x_{j,n-1}=-\eta(L_a x_n)_j.
$$

En un auto-modo $L_a u=\lambda u$ se busca $z_n=\exp(i\Omega n)$, obteniendo

$$
2\cos\Omega-2=-\eta\lambda,
\qquad
\boxed{\Omega=2\arcsin(\sqrt{\eta\lambda}/2)}.
$$

Requiere $0\le \eta\lambda\le4$. Con $\lambda(k)=4\sin^2(k/2)$, el requisito adicional de velocidad de grupo constante en la rama orientada impone $\eta=1$ y se obtiene $\Omega(k)=k$ para $0\le k\le\pi$. En las unidades del modelo, equivale a una relación elemental propagada por actualización. El período lógico $P_i=2\pi/\Omega_i$ permite comparar $P_i/P_j=\Omega_j/\Omega_i$. Un paso $n$ no es un segundo y $\Omega$ no es una frecuencia física medida.

## 3. Comparación invariante del espejo móvil [T bajo hipótesis]

O45 representa el espejo mediante un foco $X(t)$, una escala $\ell(t)>0$ y una orientación $A(t)\in SO(3)$:

$$
x=X(t)+\ell(t)A(t)y.
$$

Esta es una transformación de coordenadas; no constituye por sí sola una fuerza. Para tres fases desenrolladas $\phi_f,\phi_s,\phi_p$, sus diferencias $\delta_{fs},\delta_{ps}$ determinan $\delta_{fp}=\delta_{fs}-\delta_{ps}$, una relación de rango dos. Si el cero angular depende del parámetro $\lambda$, hace falta fijar el marco o usar una conexión $b$ con $\kappa_i=\phi_i'-b$ y $b\mapsto b+\chi'$. Entonces:

$$
\boxed{\Gamma_{i\mid0}=\frac{\kappa_i}{\kappa_0}}
$$

es una razón invariante mientras $\kappa_0\ne0$. Si $\Theta_0$ es fase covariante acumulada y monótona, el reloj relativo es $\tau_0=[\Theta_0(\lambda)-\Theta_0(\lambda_*)]/(2\pi)$. Esto no postula un tiempo absoluto. Si falla la recurrencia de referencia, el reloj deja de estar definido bajo ese contrato.

## 4. Dos modelos de ritmo que no deben confundirse

**MF-43:** $\Omega$ = *fase discreta por actualización*, con una fórmula arcseno y condición no dispersiva.  
**Comparador espectral continuo:** $R_i=1/\sqrt{\lambda_i}$, $\omega_i=\sqrt{\Gamma\lambda_i}$; su producto $R_i\omega_i=\sqrt{\Gamma}$ es una identidad exacta del modelo diferencial. Son realizaciones diferentes. No se debe reemplazar $\omega$ por $\Omega$ ni definir a partir de su coincidencia una ley relativista sin prueba.

Si $T_i=2\pi/\omega_i$ y $n_i=R_i/R_0$ en el comparador continuo, entonces $T_i=n_iT_0$. No se concluye que cualquier recurrencia física sea un múltiplo entero, ni que sus ritmos sean idénticos. Para identificar $v_*=\sqrt\Gamma$ con $c$ se requieren unidades, propagación causal universal y contraste físico; el valor $c_{\rm rel}=1$ de MF-44B es una normalización discreta de localidad, no una medición de $c$.

## 5. Concordancia unísona no es uniformidad de identidades

GR3 define vínculos binarios $b_{ij}=s_i\oplus s_j$ sobre K4. Sus paridades triangulares nulas equivalen a la posibilidad de reconstruir las seis aristas desde la estrella de cualquier foco. Hay 8 estados de vínculo coherentes entre 64 posibles; uno coherente puede tener diferencias no nulas. Por eso **concordancia** significa compatibilidad y reconstrucción, no identidad fuerte ni fase cero universal.

La distinción entre identidad y distancia debe ser respetada. La comparación de dos cierres construye una distancia o relación; no genera automáticamente una fuerza.

## 6. Consecuencia para la rama de gravedad [O/H; no nuevo teorema gravitatorio]

La gravedad se investiga como cambio físico de relaciones entre cierres que mantienen sus identidades y ritmos relacionales. El modelo energético $V(r,\delta)=K(r)(1-\cos\delta)$ solo penaliza el desfase. En $\delta=0$, $V=0$ para todo $r$ y $\partial V/\partial r=0$ a fase fija; por tanto ese **único término** no da atracción persistente si las fases coinciden. La relación de identidad, el cambio de foco y el ritmo deben formar parte de un contrato dinámico más amplio si se quiere explicar gravedad.

En la fase actual se conocen modelos y puentes condicionados, pero no una derivación inequívoca de la constante $G$, del potencial exterior, de la universalidad de caída libre ni de efectos relativistas a partir únicamente del cierre propio. Introducir $1/r$ o calibrar parámetros usando $G$ medido no constituye una predicción independiente. La prueba futura debe escoger variables de escala y actualización *sin ajustar retrospectivamente la respuesta*.

## 7. Estados y obligaciones para ROSI

| Elemento | Estatus | Obligación o falsador |
|---|---|---|
| Ciclo base como referencia | [O/D] | Identificar el contrato del ciclo elegido; no postular segundos primordiales |
| Recurrencia de MF-43 | [T] condicional | Controlar hipótesis locales, estabilidad y ramas espectrales |
| Comparador O45 | [T] condicional | Evitar fases puramente convencionales; mantener covariancia |
| Producto $R\omega$ | [T] en modelo continuo | No transferir sin prueba a la recurrencia discreta |
| Límite relacional MF-44B | [T] combinatorio | No identificar $c_{\rm rel}=1$ con $c$ físico sin hipótesis |
| Reconstrucción focal GR3 | [T] en K4 | La coherencia no impone tamaño, masa ni gravedad |
| Gravedad como ajuste de relación | [H] | Dinámica, medidas, acoplamiento, predicción independiente |

## 8. Fuentes primarias preservadas

- `01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/MF43_INTRINSIC_RELATIONAL_CLOCK.md` — fuente incorporada byte a byte.
- `01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/ritmo_radio_relatividad_relacional_v0_1.md` — fuente incorporada byte a byte.
- `01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/SUPLEMENTO_GR3_AJUSTE_UNISONO.es.md` — fuente incorporada byte a byte.
- `05_ARCHIVO/navier_stokes_O39_O53/documentos/O45_TIEMPO_ESPEJO_MOVIL_RITMOS_NS_2026-10-20.md` — copia que ya tenía el paquete.
- `01_HILO/fuentes/06_hilo_del_dos/continuidad_2026_10_14/FUENTES_COTEJO/MF44B_normalizacion_causal_cierre_global_v1.md` — fuente anterior ya preservada.

**Nota editorial:** las fórmulas se encuentran también en el manuscrito público. Este suplemento distingue los modelos por sus objetos y sus hipótesis; no intenta sustituir las fuentes ni adjudicar originalidad a teoremas conocidos.
