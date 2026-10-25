# O44-N — El múltiplo normalizador, la indefinición del uno y su alcance en Navier–Stokes

**Programa de Geometría Relacional**  
**Autoría del programa:** Le Matt Ansatz Di Ego  
**20 de octubre de 2026**  
**Carácter:** suplemento exacto e independiente del laboratorio numérico O44 toroidal previamente ejecutado.  
**Estatus:** reconstrucción ontológica [O], álgebra exacta [T], soluciones exactas particulares de NS 3D [T], no-go de suficiencia [F], puente físico abierto [A]. No modifica el núcleo ni demuestra regularidad global.

## 0. Ontología original preservada [O]

La unidad es la totalidad sin diferencia acreditada; la reflexión distingue relaciones; el **múltiplo que normalizó la relación** permite expresar sus partes y su resto en una referencia común. El resto no constituye por sí solo la identidad de la unidad. La singularidad **ontológica** es cierre propio de la referencia que sostiene relaciones y diferencias pendientes; no es por definición una singularidad de Navier–Stokes (pérdida de suavidad de la solución).

La identidad cuadrática del documento canónico del 13-X-2026 es, para enteros N>d>0,

\[
N^2-(N-d)(N+d)=d^2.
\]

Para d=1, la normalización da

\[
\boxed{1=\frac{N^2-1}{N^2}+\frac1{N^2}.}
\]

Esta identidad vale para cualquier entero N>1; la interpretación ontológica no se sigue únicamente del álgebra. La referencia `N` tampoco tiene aún una ley de asignación universal en los fluidos.

## 1. El teorema O40 que permanece [T]

Para el círculo de fases `T=R/Z` y las subfamilias `H_N={j/N mod 1}`, el refinamiento común de las referencias de denominadores N,m es `H_lcm(N,m)`. Una fracción `h/N` se transporta exactamente a `h(L/N)/L` cuando `L` es múltiplo de N. El numerador del resto puede cambiar. Ésta es **herencia de representación**; no es por sí una ley de movimiento.

## 2. Dos normalizaciones distintas en NS [D]

En el toro tridimensional `T³=[0,2π)³`, el campo de velocidad suave y solenoidal `u` satisface

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad \nabla\cdot u=0,\quad\nu>0.
\]

Defina `ω=curl u`, `E=1/2 <|ω|²>` y `E_k=1/2|ωhat(k)|²`, usando promedio espacial. Parseval:

\[
E=\sum_{k\in\mathbb Z^3}E_k,\qquad w_k=E_k/E,\quad \sum_kw_k=1\quad (E>0).
\]

Esto realiza una **unidad cuadrática normalizada física**: todo `w_k` es una fracción de enstrofía. Su denominador **es E(t), no N²**. La identidad anterior `1=(N²-1)/N²+1/N²` solo corresponde a un reparto particular si las condiciones iniciales se eligen así. No se deriva de la ecuación que `w_resto=1/N²`.

Distinga `N= mcm` de **etiquetas de armónicos espaciales** (un refinamiento aritmético) de la magnitud continua `E(t)` (el normalizador de fracciones de enstrofía). Identificarlos sería un error dimensional y lógico.

## 3. Prueba exacta: referencia N=6 estable, proporciones móviles [T]

Sean `a₂,a₃>0` y el campo

\[
\boxed{u(y,t)=\left(\frac{a_2}{2}e^{-4\nu t}\sin2y+\frac{a_3}{3}e^{-9\nu t}\sin3y,\,0,\,0\right).}
\]

**Demostración de NS exacta:** `∇·u=∂_x u_x=0`, el término `(u·∇)u=u_x∂_x u=0`, `Δ sin(ky)=-k²sin(ky)` y `∂_t u=νΔu`; tome presión constante. El campo es suave para todo tiempo y constituye una solución tridimensional (aunque espacialmente degenerada) sin estiramiento de vorticidad.

La vorticidad es

\[
\omega=(0,0,-a_2e^{-4\nu t}\cos 2y-a_3e^{-9\nu t}\cos3y),
\]

con

\[
\boxed{E(t)=\frac14(a_2^2e^{-8\nu t}+a_3^2e^{-18\nu t}).}
\]

Los modos 2 y 3 permanecen distintos de cero para todos los tiempos finitos, por lo que su mínimo común múltiplo queda `N=mcm(2,3)=6`.

**Experimento de la identidad cuadrática:** imponga al inicio

\[
a_2^2=35/36,\qquad a_3^2=1/36.
\]

Entonces `E(0)=1/4` y `w₂(0)=35/36`, `w₃(0)=1/36` corresponden exactamente a la identidad `6²−(6−1)(6+1)=1` normalizada. Esta elección es intencional, no seleccionada por NS.

La evolución del resto modal satisface

\[
\boxed{w_3(t)=\frac{1}{1+35e^{10\nu t}}.}
\]

Para ν>0, la fracción `w₃(t)` decae estrictamente, aunque `w₂(t)+w₃(t)=1` y `N=6` durante todo tiempo finito. **Resultado:** la totalidad y su referencia aritmética persisten; el resto *físico* no conserva el valor `1/N²`. Esta observación no refuta el principio ontológico, sino una identificación física no demostrada.

## 4. No-go de suficiencia dinámica [F]

Construya las configuraciones A y B intercambiando los pesos:

- `A: (a₂²,a₃²)=(35/36,1/36)`;
- `B: (a₂²,a₃²)=(1/36,35/36)`.

Tienen **el mismo** normalizador armónico `N=6`, los mismos modos activos `2,3`, la misma enstrofía inicial `E(0)=1/4`, la misma viscosidad y la misma identidad `w₂+w₃=1`. Sin embargo,

\[
E_A(t)=\frac14\left(\frac{35}{36}e^{-8\nu t}+\frac1{36}e^{-18\nu t}\right),
\]
\[
E_B(t)=\frac14\left(\frac1{36}e^{-8\nu t}+\frac{35}{36}e^{-18\nu t}\right).
\]

Para cualquier t>0, ν>0, `E_A(t)>E_B(t)`. Por consiguiente, `(N,E(0))` **no constituye una interfaz suficiente para predecir E(t)** en esta clase exacta de soluciones NS. La fracción modal inicial adicional `w₂(0)` sí basta para esta clase lineal especial, pero no para NS tridimensional general con acoplamiento no lineal.

## 5. El múltiplo y la combinación de modos: dos estructuras [T/A]

En O40, `mcm(n,m)` refina denominadores de **fracciones**. En Fourier, la no linealidad `u·∇u` contiene convoluciones `p+q=k`; por tanto, la menor subred de números de onda que contiene las etiquetas iniciales y está cerrada bajo suma y resta es el grupo aditivo `Λ=span_Z(S)`.

**Teorema condicionado:** durante toda la existencia suave y única, si `uhat₀(k)=0` fuera de una subred aditiva `Λ⊂Z³`, entonces `uhat_t(k)=0` fuera de `Λ`. La prueba se basa en la equivarianza por traslaciones y unicidad (o en el cierre del sistema Fourier): el laplaciano y el proyector de presión no cambian las etiquetas, y las convoluciones de etiquetas de `Λ` permanecen en `Λ`.

En una coordenada, `span_Z(2,3)=Z` (relacionado con `mcd(2,3)=1`), mientras `mcm(2,3)=6` refina las fracciones `1/2` y `1/3`. No son dos leyes rivales: normalizan **objetos diferentes**. Que una subred permita un modo no significa que su amplitud sea necesariamente distinta de cero; en el flujo de cizalla anterior no se generan modos nuevos porque el término convectivo se anula.

**Consecuencia:** usar `mcm` de todos los modos que aparezcan durante una solución 3D como invariante físico requiere hipótesis adicionales; pueden aparecer nuevos números de onda. La subred aditiva es una propiedad estructural más robusta, pero tampoco impone un control de amplitud ni de estiramiento.

## 6. Ecuación exacta del reparto modal [T]

Para cada `k`, defina la contribución no lineal real `T_k` por `dE_k/dt=T_k-2ν|k|²E_k` y sea `P=ΣT_k` el estiramiento neto global. La disipación es `D=Σ2ν|k|²E_k`. Para E>0,

\[
\boxed{\dot w_k=\frac{T_k-2\nu|k|^2E_k}{E}-w_k\frac{P-D}{E}.}
\]

Es una identidad exacta. Los pesos continúan sumando uno porque `Σ dot w_k=0`. Pero `T_k` depende de interacciones entre fases y amplitudes del campo, no sólo del múltiplo normalizador. Esta es la puerta matemática hacia O42 y O43-E. No es una cota de regularidad.

## 7. Contraste con O44 toroidal ya ejecutado [E/A]

Se encontró en el espacio de trabajo un laboratorio O44 anterior que prolongó el O43-E mediante ocho fases iniciales, 32 trazadores pasivos por corrida y un solucionador Galerkin de NS 3D en dominio periódico, con controles `N=32/48/64` para `T=0.12`, `ν=0.03`. Se volvió a ejecutar `VERIFICACION_O44.py` y se obtuvieron **114 controles PASS**. El mayor avance toroidal de los trazadores en las ocho fases fue menor que `0.00043` radianes, por lo que **ningún trazador completó una vuelta toroidal y no hay un resto material de retorno definido**. Esto es una ausencia de observable en el ensayo, no una ausencia universal de retorno en anillos vorticiales.

En ese barrido, el estimador descriptivo de `P_front` basado en fase (`1+cosφ+sinφ`) presentó RMSE LOOCV `1.8171×10⁻⁸` frente a `8.8157×10⁻⁷` para una media ciega a fase. **Pero** un predictor alternativo basado en la enstrofía inicial obtuvo `1.5839×10⁻⁸` (mejor que el predictor de fase): el barrido contiene covariación y **no acredita una ventaja causal independiente de la fase**. Se mantiene el resultado de O43-E: falta una comparación realmente suficiente y una vuelta material seguida.

El presente suplemento O44-N es complementario, no un reemplazo de ese O44 numérico: ofrece una pareja de **soluciones PDE exactas** donde `(N,E(0))` es insuficiente, incluso sin estiramiento y sin error de discretización. Los dos experimentos delimitan qué habría que medir en un anillo con verdadera dinámica material.

## 8. Decisión y próximo ensayo [A]

1. **Aceptado como principio ontológico del programa:** el uno y su referencia normalizadora preceden a la elección de una figura; las diferencias pueden reorganizarse sin destruir la totalidad referenciada.
2. **Demostrado para NS en este laboratorio:** existen soluciones exactas que conservan el mismo múltiplo de referencia `N=6` y la totalidad normalizada, pero redistribuyen sus pesos; N y E inicial no son dinámicamente suficientes.
3. **Demostrado para campos suaves periódicos:** la subred aditiva Fourier inicial es estructuralmente heredable mientras haya solución suave única; no equivale al mcm de denominadores.
4. **Pendiente:** construir una interfaz físicamente medible que incluya fase, estiramiento y flujo entre escalas en un anillo tridimensional genuino; demostrar que permite predecir y limitar el balance `E'=P−D` de O39 sin suponer la regularidad.
5. **Criterio de refutación:** dos datos con igual interfaz propuesta pero distinto `E'(0)` o evoluciones posteriores demuestran insuficiencia. Para regularidad general se exige una cota independiente que controle el estiramiento; este laboratorio no la ofrece.

**Límite epistemológico:** la persistencia de una normalización no impide por sí misma una singularidad analítica. La construcción es un avance en la especificación de qué puede y qué no puede representar el normalizador, no una solución del problema Clay de Navier–Stokes.

### Antecedentes

- `FORMALIZACION_CANONICA_REFLEXION_CARDINALIDAD_CAPSULAS_MASA_v1.md`, teorema T1, 13-X-2026.
- `O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md`, refinamiento de H_N, 20-X-2026.
- `O39_BALANCE_GEOMETRICO_MATERIAL_Y_FLUJO_ENTRE_ESCALAS.es.md`, enstrofía y escalas móviles.
- `O41_COMPARADOR_Y_NO_GO_DE_HERENCIA_DINAMICA.es.md`, insuficiencia de amplitudes frente a fases.
- `O42_FASE_MODULAR_TRANSFERENCIA_Y_ESTIRAMIENTO_3D.es.md`, prueba local 3D de fase.
- `O43E_INFORME.es.md`, simulación numérica 3D en anillo curvado; sin retorno material ni singularidades.

**Reproducción del suplemento:** `python3 O44_normalizador_y_dinamica_NS.py` (biblioteca estándar). El script verifica en malla la solución exacta y el balance mediante comparación numérica con las expresiones analíticas. **Verificación histórica del O44 toroidal:** en `O44_NS_Toroide_Semilla_2026-10-20/`, ejecutar `python3 VERIFICACION_O44.py` (requiere NumPy). Ninguno constituye un certificado de regularidad PDE.
