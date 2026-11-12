# ¿Qué diferencias deben sobrevivir?

**El cubo de espejos, el reconocimiento de herencia y el costo de mantener una respuesta exacta**

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · Propuesta de actualización conceptual y solicitud de verificación independiente

> **Estado de investigación: ABIERTO.** Este texto no demuestra `P = NP` ni `P ≠ NP`. Examina cuándo una reducción exacta de diferencias se traduce, o no, en una reducción del trabajo total.

## 1. Reflexión central

El número de configuraciones de un sistema no equivale al número de distinciones que una consulta necesita conservar. El cubo de espejos propone imaginar una referencia que reúne manifestaciones sin destruir las relaciones de origen. La pared móvil modifica qué diferencias se observan. Las esferas y los radios dan una lectura de resolución, simultaneidad y desfase. En computación, esta imagen se somete a una prueba más exigente: **¿podemos descubrir, verificar, actualizar y usar esa referencia con un costo neto inferior al de resolver directamente el problema?**

Las relaciones heredadas no necesitan recalcularse si existe una representación que las conserva y permite reconstruir la respuesta. Pero una igualdad observada desde una referencia puede romperse al recibir una restricción futura: **cierre observable no implica cierre operativo**. Por eso el residuo y el costo de reapertura no son adornos; son parte del mecanismo.

La pregunta sobre P frente a NP aparece precisamente cuando intentamos extender una economía demostrada en familias estructuradas a instancias arbitrarias, sin suponer que la referencia óptima venga dada.

## 2. Correspondencia explícita entre imagen y objeto matemático

| Imagen conceptual | Traducción contrastable | Riesgo que debe controlarse |
|---|---|---|
| Espejo y reflejo | Transformación de estados, equivalencia o involución que preserva una consulta declarada | Que dos imágenes parecidas no sean computacionalmente equivalentes |
| Pared móvil | Cambio de la referencia/partición, no de las soluciones subyacentes | Que la reducción pierda distinciones necesarias ante continuaciones |
| Esferas y radios | Familia de observaciones con diferente resolución y particiones inducidas | Que la pérdida de resolución se confunda con recuperación gratuita |
| Tetraedro | En `K4`, seis vínculos `b_ij=s_i XOR s_j` representados por tres bits independientes | Confundir este contrato con vínculos arbitrarios |
| Herencia | Restricción ya implicada por la referencia | Omitir el trabajo de reconocer la implicación |
| Singularidad observable | Muchas configuraciones reunidas en una misma clase para la consulta | Confundir equivalencia observacional con identidad interna |
| Cierre y recierre | Una referencia que admite composición correcta con restricciones futuras | Suponer cierre antes de comprobar el residuo |
| Reapertura | Refinamiento necesario cuando una nueva restricción diferencia estados antes reunidos | Tener que reconstruir información que fue descartada |
| Economía | Menor costo **total** para la misma respuesta y el mismo modelo de comparación | Confundir compresión con tiempo de ejecución |

## 3. Resultados que sostienen la pregunta

### 3.1 Seis vínculos, tres bits

En el tetraedro `K4`, con estados de vértice sobre `F_2`, los vínculos de paridad cumplen `b_ij = b_fi XOR b_fj` al fijar un foco `f`. Los 16 estados de vértices inducen 8 patrones de vínculos, que se codifican exactamente con 3 bits. Es una economía de representación y reconstrucción **para esa clase de vínculos**, no para cualquier grafo o fórmula.

### 3.2 Cinco estados: raíz y residuo

En `F_2^3`, si tres cláusulas sobre las mismas tres variables distintas excluyen tres asignaciones diferentes, las cinco permitidas se descomponen de manera exacta en **un plano afín de cuatro puntos y un punto residual**. Una cuarta exclusión puede cerrar el plano (si elimina el residuo) o retraer la referencia anticipada (si elimina un punto del plano). Al recorrer las 336 exclusiones iniciales ordenadas y sus 5 continuaciones posibles, hay 336 cierres y 1344 retracciones. La unicidad de la raíz no autoriza a borrar el residuo.

### 3.3 El límite de la clausura local

La regla del diamante en 3-coloración identifica vértices que necesariamente tienen el mismo color y permite detectar ruedas impares. Las familias de Mycielski muestran que incompatibilidades globales pueden existir sin esos diamantes. Por ello, una clausura local fija no puede asumirse algoritmo universal para 3-coloración. Otros laboratorios, como las tensiones modulares sobre toros, separan igualmente el cierre de caras de los periodos globales.

### 3.4 La economía no es una sola magnitud

La rejilla `10 × m` de 3-coloración aporta un ejemplo medible: 1536 columnas compatibles, 136 órbitas bajo simetrías y una recurrencia escalar mínima reportada de orden 51 con certificado exacto. Son objetos diferentes: estados de columna, órbitas y dimensión necesaria para la sucesión de conteos. La relación no demuestra que 3-coloración general sea fácil.

### 3.5 Conteo paramétrico

Para un sistema explícito de paridad `Ax=b` sobre `F_2` y `t` cláusulas OR que no estén implicadas por la referencia, si `d` es la dimensión de libertad afín, hay un procedimiento exacto de conteo con costo

`O(poly(L) * [1 + 2^min(t,d)])`.

Se elige entre inclusión-exclusión sobre las cláusulas y enumeración de las variables libres. Esta cota es polinómica cuando `min(t,d)=O(log L)`; no lo es en general cuando ambos parámetros crecen mucho. Si la paridad está oculta en una fórmula OR arbitraria, falta contabilizar el costo de encontrarla y certificar la transformación.

## 4. El contrato de economía que debe figurar en la imagen

Para una fórmula `F`, un extractor `E` intenta producir una referencia `R`, un residuo `Δ` y un certificado `π`. Un verificador `V` examina que la reducción conserve la respuesta consultada, y un calculador responde sobre `(R,Δ)`.

La comparación honesta exige, para una línea base `B`:

`C_rec(F) + C_ver(F) + C_calc(R, Δ) + C_recon(F) < C_B(F)`.

Todos los términos deben medirse bajo la misma tarea (decidir, contar o reconstruir), el mismo modelo de costo, y la misma familia de instancias. **Una referencia comprimida que cuesta más reconocer no ofrece por ello economía total.**

## 5. La pregunta P frente a NP formulada sin anticipar su respuesta

**Proposición condicional.** Si existe un procedimiento determinista que para *toda* 3-CNF `F` de longitud `L`:

1. construye y verifica en tiempo polinómico una transformación exacta a una instancia `XOR+OR` de tamaño polinómico,
2. preserva el resultado de satisfacibilidad,
3. deja `min(t,d)=O(log L)`, y
4. permite decidir la instancia transformada mediante el algoritmo del apartado 3.5,

entonces `3-SAT ∈ P` y, por NP-completitud de 3-SAT, **`P = NP`**.

Esta es una implicación lógica, **no** la afirmación de que dicho procedimiento exista. Si además la transformación es parsimoniosa y conserva el número de modelos de cada fórmula, la consecuencia es todavía más fuerte: el conteo de `#3SAT` quedaría en tiempo polinómico. Ese grado de reducción está sin demostrar.

La alternativa que también debe buscarse es una familia explícita de instancias en la cual reconocer y certificar la referencia requiera un costo que borre el ahorro de representación. Encontrar esas barreras puede producir un resultado valioso aunque no resuelva P frente a NP.

## 6. Estado para la auditoría ROSI

| Afirmación | Estado recomendado |
|---|---|
| Tetraedro, 8 patrones y tres bits | Demostración local bajo hipótesis explícitas |
| Cinco estados = plano afín + residuo | Demostración local, control finito independiente |
| Cierres y retracciones `336 / 1344` | Control exhaustivo pequeño reproducible |
| Orden 51 en la rejilla de ancho 10 | Certificado comunicado por el expediente del 8-XI; reproducir la prueba exacta original al auditar |
| Conteo paramétrico `XOR+OR` | Argumento matemático con paridad explícita; comparar con técnicas clásicas |
| Reconocimiento de paridades ocultas por compuertas | Condicionado a la familia de codificaciones verificables; ensayos no universales |
| Mejor economía que todas las alternativas | No demostrado; hay controles favorables y contrarios |
| Algoritmo general para 3-SAT | Abierto |
| `P = NP` o `P ≠ NP` | No resuelto |

**Resultado global sugerido: OPEN.** La evidencia local no autoriza una conclusión universal. La reproducción de verificadores propios y la revisión matemática externa deben registrarse por separado.

## 7. Actualización recomendada de la imagen

**Imagen del programa:** `imagen_cubo_economia_2026-11-10.png`.

Leer de izquierda a derecha: estados y distinciones; plano más residuo; cubo como referencia y reflejo; tetraedro que ejemplifica herencia; las dos continuaciones posibles (cierre o reapertura); y el costo de mantener la respuesta exacta. El desenlace gráfico es **`P ? NP — pregunta abierta`**, no una igualdad asumida.

**Precisión indispensable para el pie de imagen:** “Menos clases observables” no significa pérdida nula de información para toda pregunta: significa preservar la respuesta **para una consulta y una familia de continuaciones declaradas**. Otra consulta puede exigir distinguir de nuevo estados que la referencia actual reúne.

## 8. Próxima verificación independiente

La pregunta más productiva ya no es solamente si existe compresión. Es:

**¿Qué certificados permiten reconocer, con costo controlado, una referencia exacta que soporte todas las continuaciones relevantes, y qué instancias obligan a conservar un residuo grande o a pagar un reconocimiento costoso?**

Los ensayos siguientes deberían enfrentar instancias con paridades manifiestas, paridades escondidas tras compuertas, fórmulas aleatorias, casos de alta anchura y familias difíciles conocidas; comparar conteo y decisión contra solvers especializados, incluyendo el reconocimiento y la reconstrucción; y separar coincidencias algebraicas locales de equivalencias de algoritmos completos.

## 9. Trazabilidad

- [El cubo de espejos y P frente a NP (30-X-2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/review_requests/2026-10-30_mirror_cube_p_vs_np_es)
- [El cruce como reflejo central (3-XI-2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-03_cruce_reflejo_central)
- [La economía del cálculo (8-XI-2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-08_economia_del_calculo)
- [¿Qué cálculo deja de hacerse? (10-XI-2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_que_calculo_deja_de_hacerse/PAPER_ES.md)
- [Registro de auditoría del 10-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_que_calculo_deja_de_hacerse/ANEXO_AUDITORIA.md)

### Control local añadido con esta nota

Ejecutar `python3 verificar_referencia_local.py`. Verifica de manera independiente, por enumeración, la geometría afín de 3 bits, la relación `336/1344`, la reconstrucción de `K4` y 50 instancias pequeñas `XOR+OR` contra fuerza bruta. **No reproduce por sí solo el laboratorio completo del repositorio, ni establece una nueva cota de complejidad.**
