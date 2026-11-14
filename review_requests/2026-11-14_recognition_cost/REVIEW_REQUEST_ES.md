# ¿Cuándo cuesta menos reconocer que calcular?
**Solicitud de revisión independiente — 14 de noviembre de 2026**

**Autor público:** Le Matt Ansatz Di Ego

Se solicita una revisión matemática y computacional de los resultados publicados sobre economía del cálculo, reconocimiento de estructuras, conservación de información y reconstrucción exacta de respuestas.

La pregunta central es:

**¿Bajo qué condiciones reconocer relaciones heredadas reduce el costo total de un algoritmo, incluyendo el propio costo de reconocerlas y verificarlas?**

## 1. Construcción

Una estructura puede contener relaciones que ya están determinadas por otras. Reconocerlas permite conservar sus consecuencias sin volver a calcularlas.

El procedimiento distingue:

- **Referencia:** relaciones disponibles que permiten reconstruir otras.
- **Herencia:** relaciones que ya son consecuencia de la referencia.
- **Novedad:** restricciones que introducen diferencias todavía pendientes.
- **Economía:** reducción verificable del trabajo necesario para producir una misma respuesta exacta.

La comparación se expresa mediante:

$C_{\mathrm{total}}=C_{\mathrm{reconocimiento}}+C_{\mathrm{verificación}}+C_{\mathrm{cálculo}}+C_{\mathrm{reconstrucción}}$.

Existe ahorro neto frente a un algoritmo de referencia B cuando:

$C_{\mathrm{total}}(F)<C_B(F)$.

La comparación exige conservar la respuesta, la instancia y el modelo de costo.

## 2. Resultados disponibles

En el manuscrito *¿Qué cálculo deja de hacerse?*, el conteo exacto mediante relaciones de paridad proporciona una cota:

$O\!\left(\operatorname{poly}(L)(1+2^{\min(t,d)})\right)$,

donde $L$ es la longitud de la entrada, $d$ representa los parámetros libres después del cierre y $t$ las cláusulas nuevas pendientes. Esta cota corresponde al caso en que las ecuaciones de paridad están disponibles.

También se presenta un procedimiento para reconocer relaciones ocultas en familias de fórmulas construidas mediante compuertas.

En una familia con conexiones largas y 96 variables primarias:

| Procedimiento | Tiempo publicado |
|---|---:|
| Reconocimiento y conteo | 12,8 ms |
| Eliminación genérica | 247,0 ms |
| Aceleración observada | 19,3× |

El reconocedor alcanza 256 variables y 4.076 cláusulas en 58 ms. Para ese tamaño se informa una estimación de ancho $2^{58}$ para la eliminación genérica; su medición de tiempo alcanza 96 variables primarias.

También se cuantifican casos en los que el cálculo directo requiere menos tiempo que la representación alternativa.

Los resultados publicados reúnen 23 fórmulas medidas y una prueba adicional de contrato con 5.889 fórmulas; los conteos de las instancias aceptadas coinciden en los controles informados.

Las mediciones corresponden a implementaciones y familias determinadas; se solicita ampliar la comparación con algoritmos especializados.

## 3. Aportes complementarios

La publicación del 14 de noviembre incorpora siete trabajos que permiten extender la comparación hacia:

- La cantidad mínima de información necesaria para conservar respuestas.
- La certificación de costos mínimos dentro de clases de representación definidas.
- La reconstrucción exacta mediante distintas representaciones.
- La medición de diferencias entre soluciones y el costo de recuperarlas.

Estos resultados permiten estudiar por separado el costo de almacenar una estructura, reconocerla, actualizarla y responder consultas.

## 4. Cuestiones para revisión

Se invita a examinar cinco problemas:

1. **Corrección:** verificar las identidades y las condiciones bajo las cuales el reconocimiento conserva exactamente el número de soluciones.

2. **Reproducción:** repetir las mediciones, comprobar sus controles y comparar implementaciones bajo condiciones equivalentes de tiempo y memoria.

3. **Competitividad:** contrastar los resultados con contadores especializados, técnicas XOR, descomposiciones por ancho de árbol y preprocesamiento por definibilidad.

4. **Frontera de economía:** identificar condiciones necesarias, suficientes o contraejemplos que permitan determinar cuándo el reconocimiento compensa su propio costo.

5. **Generalización:** examinar si existen familias más amplias de problemas para las cuales el cambio de referencia pueda demostrarse ventajoso, o establecer límites precisos a esa posibilidad.

## 5. Alcance

La solicitud comprende teoremas bajo hipótesis explícitas, verificaciones finitas y mediciones computacionales.

La extensión a fórmulas generales de tres literales y la existencia de una mejora uniforme permanecen abiertas. Una refutación, una cota inferior o un contraejemplo constituyen resultados relevantes de la revisión.

El objetivo es identificar con precisión qué cálculo se evita, cuánto cuesta identificarlo y cuándo el ahorro se conserva al aumentar la dimensión del problema.

## Documentación

**Manuscrito principal:** [¿Qué cálculo deja de hacerse? — versión 0.3](../../2026-11-10_que_calculo_deja_de_hacerse/PAPER_ES.md)

**Reproducción:** [código, controles y guía](REPRODUCTION.md)

**Actualización:** [Siete trabajos — 12 y 13 de noviembre](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-14-entrega-programa-7-trabajos/README_ENTREGA_2026-11-12_13.md) ([DOI archivado](https://doi.org/10.5281/zenodo.24214053))

Se agradecen revisiones reproducibles, pruebas alternativas, observaciones sobre el modelo de costo y contraejemplos documentados.

**Endless Monkey Project · Relational Geometry Program**
