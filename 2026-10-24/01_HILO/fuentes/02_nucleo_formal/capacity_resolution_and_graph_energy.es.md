# Capacidad, resolución y forma cuadrática de comparación

**Le Matt Ansatz Di Ego · Integración 3.1 · Resultado finito bajo contrato**

Dos redes pueden admitir las mismas diferencias y representar el mismo estado,
pero asignar costos distintos a sus comparaciones. Esta nota conecta dos
resultados ya disponibles: [resolución y proyección](resolution_and_modal_weights.es.md)
y [comparadores locales](local_comparators_and_relational_laplacian.es.md).
La conexión usa el cociente de Rayleigh clásico; no reclama un nuevo teorema
espectral general.

## Contrato

Sean $N\ge2$, $p_i\ge0$, $\sum_i p_i=1$, producto interno euclídeo,
$u=(1,\ldots,1)/\sqrt N$ y $\bar p=(1/N,\ldots,1/N)$. Sea $G$ un grafo
simple, conexo, no ponderado, con incidencia orientada $B$ de tamaño
$N\times\lvert E\rvert$. Defina

$$
L=BB^{\mathsf T},\qquad
\mathcal E_G(p)=p^{\mathsf T}Lp=\sum_{\{i,j\}\in E}(p_i-p_j)^2,
\qquad
\mathcal R(p)=\log_2\!\left(N\sum_i p_i^2\right).
$$

“Energía de comparación” es el nombre matemático de esta forma cuadrática
adimensional. No se le asigna una unidad física, temperatura ni escala de masa.
La notación y la interfaz de cálculo se conservan por compatibilidad. Aquí
$p$ designa probabilidades y $L$ un Laplaciano: no son los momentos de la
[traducción física de momento y radio](../publication/momentum_radius_and_energy.es.md).

## Tres cantidades diferentes

| Cantidad | Definición | De qué depende |
|---|---|---|
| Capacidad de diferencia | $\operatorname{rank}B=N-1$ | Espacio y conectividad |
| Resolución del estado | $\mathcal R(p)$ | Distribución y referencia |
| Forma cuadrática de comparación | $\mathcal E_G(p)$ | Distribución y aristas |

La identidad de la v3 da

$$
\tan^2\theta=N\sum_i p_i^2-1
=N\|p-\bar p\|^2=2^{\mathcal R}-1,\qquad
r_{\rm ref}=2^{-\mathcal R}.
$$

Por tanto $0\le\tan^2\theta\le N-1$. La igualdad con el rango ocurre
precisamente para distribuciones concentradas en una alternativa. Para probar
el caso de igualdad, $\sum_i p_i^2=1$ y $\sum_i p_i=1$ implican
$\sum_{i<j}p_ip_j=0$; la no negatividad permite sólo una coordenada positiva.
En la referencia uniforme el ángulo es cero y el rango sigue siendo $N-1$.

## Cota que incorpora la organización

Sean $0=\lambda_1<\lambda_2\le\cdots\le\lambda_N$ los autovalores de $L$.
Entonces

$$
\boxed{\lambda_2(2^{\mathcal R}-1)
\ \le\ N\mathcal E_G(p)\
\le\lambda_N(2^{\mathcal R}-1).}
$$

**Prueba.** Escriba $m=p-\bar p$. Como $L\bar p=0$ y $m\perp u$,
$p^{\mathsf T}Lp=m^{\mathsf T}Lm$. La descomposición en una base ortonormal
de autovectores de $L$ da
$\lambda_2\|m\|^2\le m^{\mathsf T}Lm\le\lambda_N\|m\|^2$.
Multiplicar por $N$ y sustituir la identidad anterior prueba el resultado.
La igualdad inferior o superior exige que $m$ pertenezca al correspondiente
autoespacio, o que $m=0$. $\square$

La conectividad es esencial para $\lambda_2>0$. Este resultado no identifica
un gap de un Hamiltoniano físico ni proporciona una cota uniforme para una
familia de redes con tamaño creciente.

## Ejemplo que distingue las tres cantidades

Para $p=(1,0,0,0)$ compare el camino de cuatro vértices y el grafo completo:

| Red | Rango | Resolución | $\lambda_2$ | $\lambda_N$ | $\mathcal E_G$ |
|---|---:|---:|---:|---:|---:|
| Camino, estado en un extremo | 3 | 2 bits | $2-\sqrt2$ | $2+\sqrt2$ | 1 |
| Completa | 3 | 2 bits | 4 | 4 | 3 |

El rango y la resolución coinciden; la energía cambia. En el grafo completo,
$L=N(I-uu^{\mathsf T})$ y la cota se satura para todo $p$.

Para estados independientes $p\otimes q$, la resolución se suma. Si
$t_p=\tan^2\theta_p$, también

$$
t_{p\otimes q}=t_p+t_q+t_pt_q.
$$

Esta identidad se obtiene de $1+t=N\sum p_i^2$. No define por sí misma qué
grafo o dinámica usar en la composición.

## Reproducción y procedencia

El [demostrador](../07_emergence_laboratory/graph_resolution.py) valida estados,
conectividad y aristas; los [controles](../tests/test_ue_integration.py) prueban
la cota, la independencia de orientación y la composición.

~~~bash
python 07_emergence_laboratory/graph_resolution.py
~~~

La revisión de UE motivó esta conexión. El resumen LV2 histórico ya estaba
integrado con alcance corregido en la v3: no se atribuye a esta edición la
corrección previa de rango frente a ángulo. La ampliación concreta es enlazar
esa resolución con la forma de comparación y hacer ejecutable la distinción.
