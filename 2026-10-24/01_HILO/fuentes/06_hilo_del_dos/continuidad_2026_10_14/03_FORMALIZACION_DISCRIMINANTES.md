# Núcleo matemático de la hipótesis aislada y protocolo falsable

## A. Lo existente, que no debe redemostrarse como novedad

Sea un grafo `G=(V,E)`, colores `C={0,1,2}`, frontera `B`, interior `I=V\B`:

`R_G(c)=∧_{uv∈E}[c_u≠c_v]`

`Γ_G(B)={b∈C^B : ∃i∈C^I, R_G(i,b)}`.

**MF-34/O1d/O2:** para todo contexto exterior que interactúa solo por `B`, `Γ_G(B)` conserva exactamente el contrato de existencia de continuación. El número `|Γ|` no caracteriza su composición.

**MF-63B:** para `F_A(X,S)` y `F_B(S,Y)`:

`B_A(S)=∃X F_A(X,S)`, `B_B(S)=∃Y F_B(S,Y)`, `K_AB(S)=B_A(S)∧B_B(S)`.

La operación Join + Project da nuevo cierre sin reabrir X e Y **si las interfaces exactas previas están realmente disponibles y el contrato de contacto se restringe a S**. Esto es una identidad semántica, no un algoritmo eficiente universal.

**MF-86:** `K ≃_Q N_Q(K)`, `N_Q²=N_Q`, y composicionalidad respecto de relaciones admisibles. La idempotencia por sí sola no garantiza representación corta ni construcción barata.

**MF-98:** separar `Build`, `Update` y `Read`, y considerar costo de creación de una cápsula, tamaño, actualización y certificación.

**O2c/N1-B:** para el motor extensional O2c, con Join/Project/Normalize, cualquier recorrido insatisfacible admite traducción por resolución y la inducción del suplemento v2.8 establece `#pasos de resolución ≤ (3/2)·total_candidates` sin incluir costo del selector. Esto **no restringe todo método posible**.

## B. Enunciado de trabajo de la nueva conjetura

Sea una **clase tipada de cápsulas** `𝒦`, con operaciones públicas `Join`, `Project`, `Normalize`, `Read_Q`, y reglas de ampliación de contexto `Extend`. Para una secuencia de relaciones de entrada `e_1,...,e_m`, la conjetura verbal del autor exige poder formar:

`K_{j+1}=Normalize(Project(Join(K_j, e_{j+1}))) ∈ 𝒦`

sin regresar obligatoriamente a las historias que ya fueron consolidadas, y conservando respuestas para las consultas admitidas.

**Primera pregunta (clausura de tipos):** ¿el resultado pertenece a `𝒦` para todo cierre legítimo y combinación, aunque se agreguen puertos? Esto NO equivale a control del tamaño de la codificación.

**Segunda (suficiencia y estabilidad):** ¿la actualización preserva exactamente todas las consultas de `Q` y todas las continuaciones declaradas, incluidas nuevas interacciones sobre puertos etiquetados? Una interfaz proyectada demasiado pronto puede no contener lo exigido por un contrato ampliado.

**Tercera (economía interna):** si `n` es el tamaño explícito de la entrada y `m` las relaciones, ¿se pueden acotar uniformemente representación, Join, Project, Normalize, Read, certificados y selección por un polinomio en `n+m` para TODOS los grafos? Esta es la obligación adicional que tendría relación con `P=NP`.

**Cuarta (ciclos):** defina primero el ciclo relacional y su costo de paso. Se deben medir tanto número de ciclos como recursos por ciclo. Un número de recierres pequeño puede esconder una proyección costosa.

## C. Controles ya disponibles

- **O1d:** dos cápsulas sobre puertos `A,B,C`, ambas con 18 coloraciones compatibles; un contexto exterior obliga `A=B`. Una combinación da interfaz vacía y la otra 6 filas. Falsador de la idea «mismo conteo = misma cápsula».
- **O2:** una escalera `2×8` con misma interfaz de frontera: `981` candidatos con min-fill y `59 031` con orden inverso. Falsador de «respuesta igual = costo igual» dentro del algoritmo tabular.
- **O2b:** añadir `k` triángulos independientes multiplica soluciones globales por `6^k`, y conserva la respuesta a `Q01` y una frontera pequeña; el costo de eliminación de esta familia crece linealmente. **Control positivo sectorial** de compresión.
- **O2b adversarial:** decidir si hay alguna coloración de `H ⊔ gadget(Q01=sí)` sigue siendo NP-completo, aunque cualquier coloración existente dé una sola respuesta a Q. Falsador de «K_Q=1 implica decidir barato».
- **O2c:** en 35 instancias predefinidas, el selector de densidades empata 33 veces y es peor en 2 contra min-fill; no basta una regla local de densidades.
- **Informe de 81 grafos:** pares con mismas 8 variables, 13 aristas, 12 soluciones globales y 6 en frontera, costos 481 vs 314; núcleos mínimos 11 vs 5 y radios `R*=2` vs `R*=1`. En 22/81 hay relevancia conjunta sin indispensabilidad marginal. Los núcleos se obtuvieron por **búsqueda exhaustiva posterior**, no por ROSI anticipatorio.

## D. Experimento de la nueva hipótesis, SIN cambiar de motor inadvertidamente

1. Escoger un conjunto reproducible de grafos: caminos, franjas, cuadrículas, grafos aleatorios, expanders, gadgets de igualdad/desigualdad, grafos adversariales de ancho creciente y casos triviales/insatisfacibles. Agregar aristas sin cambiar los nombres de puertos.
2. Definir las cápsulas iniciales y la gramática de tipos (no inventar un tipo distinto para cada instancia). Declarar fronteras tipadas y repertorio de futuras preguntas `Q`.
3. Registrar por cierre: operaciones; puertos antes/después; número de ciclos independientes de grafo; radio de consulta; `K_Q`; filas/representación; memoria pico; costo Build, Join, Project, Normalize, Update, Read; testigo de equivalencia de frontera.
4. Ensayar normalización: factores idénticos, tautologías, dependencias derivadas, simetrías demostradas; registrar si el nuevo objeto realmente sustituye a dos cápsulas o si solamente conserva fórmulas pendientes.
5. Ensayar **creación**, no sólo reconocimiento: después de incorporar relación nueva, producir la nueva cápsula con testigo reproducible usando únicamente datos accesibles en esa etapa.
6. Exigir un control independiente de corrección por enumeración en grafos pequeños y verificadores escalables/certificados en grafos mayores.
7. Si se observa crecimiento, clasificar: ¿nuevos puertos? ¿dependencia conjunta? ¿tamaño de instancia? ¿compilación? ¿costo de descubrir equivalencia? ¿cambio de consulta? No atribuir automáticamente la causa a «nuevo tipo ontológico».
8. Separar hipótesis `H_tipo` (clausura algebraica del repertorio), `H_tamaño` (representación económica), `H_costo` (actualización económica), `H_radio` (comportamiento por escalas). Una refutación de `H_costo` en un motor no refuta `H_tipo`.

## E. Lo que se pide al revisor

Intentar, en orden: (i) encontrar la gramática mínima de cápsulas ya contenida en v2.8 y MF; (ii) demostrar clausura bajo recierre como enunciado exacto; (iii) localizar ejemplos donde la normalización conserven/no conserven la economía; (iv) construir testigos de dependencia conjunta o crecimiento de interfaz; (v) evaluar el alcance hacia P versus NP **sin** atribuir a la ontología una cota no demostrada.

Cualquier nueva fórmula de "radio" debe declararse provisional y conservar separados `r_V=2^{-h}`, distancia `d_G`, radio R* desde frontera, ancho intermedio y radio físico. La identidad entre ellos exige un puente demostrado.

## F. Testigo discriminante de nivel inmediato

En `06_TESTIGO_DE_CREACION_DE_RELACION.md` se demuestra con una estrella de tres hojas que **proyectar tres desigualdades binarias puede producir una condición ternaria no factorizable en restricciones binarias sobre los mismos puertos**. Por tanto «mismo tipo de estructura» necesita tiparse: no es cierto si tipo significa «solamente aristas binarias originales»; sí hay clausura abstracta si tipo significa «relaciones finitas con aridad variable». El segundo caso sigue sin controlar crecimiento/costo.
