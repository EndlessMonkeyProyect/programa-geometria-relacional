# Programa de Geometría Relacional — G-R3
## Concordancia unísona, foco relacional y condiciones para una hipótesis de masa y gravedad

**Autoría del programa:** Le Matt Ansatz Di Ego  
**Fecha:** 18 de octubre de 2026  
**Carácter:** suplemento independiente y aditivo a N-M1, R-F1 y H-R2. **No sustituye el núcleo canónico.**  
**Orden:** narración → ontología → conceptos → matemática → pruebas y refutadores → puente físico.

### 0. Convención epistemológica

- **[NARRATIVA]** imagen o intuición que orienta una pregunta.
- **[POSTULADO]** premisa ontológica no derivada.
- **[DEFINICIÓN]** convenio formal; no descubrimiento físico.
- **[TEOREMA]** consecuencia demostrada de premisas declaradas.
- **[CONTROL FINITO]** comprobación exhaustiva en un dominio acotado.
- **[CONTRAEJEMPLO]** límite o refutación de una afirmación excesiva.
- **[PUENTE ABIERTO]** correspondencia con la física aún no acreditada.

## 1. Narrativa: los encuentros que encuentran unísono

Una unidad puede proyectar su totalidad desde un foco que solo existe en su propio espacio relacional; el foco no es un observador exterior, una posición previa ni un centro geográfico elegido. Cuando distintas proyecciones convergen, pueden compartir una trama sin ser realizaciones idénticas. En los «nidos de un eclipse», como imagen conceptual, los recorridos se superponen o tienen un encuentro común sin que ese solapamiento visual sea automáticamente un cierre.

Una diferencia pendiente es la incapacidad de las comparaciones disponibles para fijar cómo se relacionan las proyecciones. La nueva intuición es que **el radio podría participar como mecanismo de ajuste de tales diferencias**, mientras una **concordancia unísona** sostiene la referencia propia del módulo. **Masa y gravedad** se proponen como posibles manifestaciones físicas de ese mecanismo único, no como dos cantidades ya derivadas ni como equivalencias establecidas.

No se introducen tiempo, energía, calor, luz o unidades de Planck para «explicar» el inicio. El ritmo relacional será inicialmente solo un **orden de actualizaciones o concordancias**, no una frecuencia temporal física. La frontera material puede desempeñar papel de escala, pero todavía no se le asignan impermeabilidad, absorción, reflexión especular ni propiedades electromagnéticas.

## 2. Núcleo ontológico propuesto — G-R3

**GR3-O1 [POSTULADO, procedente de H-R2].** Una totalidad `U` admite, en ciertos cierres, focos internos desde los que una imagen suficiente puede reconstruir la unidad con respecto a consultas declaradas. Una imagen óptica ordinaria no es necesariamente esta firma reconstruible.

**GR3-O2 [POSTULADO].** Una diferencia entre proyecciones no es necesariamente un objeto físico duplicado, ni equivale a un azar previo. Se define relativa al contrato de comparación disponible.

**GR3-O3 [HIPÓTESIS CENTRAL].** Existe una familia no trivial de módulos donde los ajustes de las diferencias pendientes pueden alcanzar concordancias comunes; tales concordancias hacen posible una referencia propia reutilizable y una profundidad adicional.

**GR3-O4 [PUENTE ABIERTO].** Se investiga si la persistencia del cierre y el ajuste entre cierres son aspectos de una misma dinámica cuya manifestación física produce masa y gravitación. No se atribuyen esas propiedades a un grafo booleano por una semejanza verbal.

**Aclaración:** no se declara que un cierre *obligatoriamente* produzca un módulo nuevo ni que toda singularidad sea un punto geométrico euclidiano. La cardinalidad, la métrica y las escalas requieren condiciones independientes.

## 3. Vocabulario: cinco distinciones que no se pueden colapsar

1. **Foco**: referencia interna posible para reconstruir una unidad. En el ensayo `K₄`, cualquier vértice puede actuar como tal; el modelo *no deriva aún* la génesis de la referencia.
2. **Imagen focal**: información de los vínculos visibles desde el foco *junto con una regla reconstruible declarada*. La imagen no es una copia material independiente.
3. **Común**: subestructura, interfaz o restricciones compartidas entre módulos. Una coincidencia visual sin relaciones determinadas no es suficiente.
4. **Unísono relacional**: las diferencias binarias distribuidas son globalmente compatibles, aunque los estados de los focos no sean todos iguales. **Unísono fuerte** es el caso especial de cero diferencias.
5. **Profundidad**: orden o nivel en que una familia de consultas se vuelve reconstruible (véase H-R2). No equivale todavía a distancia, tiempo o masa.

Distinguir también el **radio geométrico** `r` (medida de longitud bajo una métrica elegida), el **índice discreto de ajuste** `λ` (conteo de diferencias que deben modificarse para obtener un cierre) y el **radio de la totalidad** `R_U` (noción ontológica todavía sin definición métrica acreditada). No se los identifica.

## 4. Laboratorio mínimo: `K₄` con seis relaciones binarias

**[DEFINICIÓN]** Sea `V={0,1,2,3}`. La trama combinatoria es el grafo completo `K₄`, con seis aristas `E`. En cada vértice situamos una variable binaria `s_i∈F₂`. En cada arista registramos una relación `b_ij∈F₂`. Una configuración está **resuelta** si existe `s` tal que:

\[
b_{ij}=s_i\oplus s_j\quad(\forall\,ij\in E).
\]

La transformación `s_i↦s_i⊕1` aplicada simultáneamente a los cuatro focos deja invariantes todos los `b_ij`. No hay un bit absoluto de orientación distinguible desde los vínculos internos.

**[DEFINICIÓN — imagen focal].** En un foco `f`, su imagen local es `Φ_f(b)=(b_fj)_{j≠f}`. Para recuperar todo el grafo, un decodificador usa la regla:

\[
D_f(\Phi_f(b))_{ij}=b_{fi}\oplus b_{fj},\qquad b_{ff}=0.
\]

La regla es parte del contrato matemático; **no se ha demostrado que surja espontáneamente de un lente, un espejo o una singularidad física**.

### 4.1 Teorema GR3-T1 — Reconstrucción de la totalidad desde cualquier foco

**[TEOREMA]** Para `K₄`, son equivalentes:

(a) existe un estado global `s` del que provienen todos los vínculos `b_ij`;  
(b) el XOR alrededor de cada triángulo es cero;  
(c) el decodificador focal recupera los seis vínculos originales desde una estrella de cualquier foco;  
(d) los cuatro focos recuperan los mismos seis vínculos originales.

**Demostración.** Si `b_ij=s_i⊕s_j`, en un ciclo triangular cada estado aparece dos veces, así que la paridad es cero. Fijando cualquier `f`, si todos los triángulos con ese foco tienen paridad cero, necesariamente `b_ij=b_fi⊕b_fj`. Por tanto, `D_f(Φ_f(b))=b`. A la inversa, si la reconstrucción coincide, basta fijar `s_f=0` y `s_i=b_fi` para obtener `b_ij=s_i⊕s_j`. Esto vale para cualquiera de los cuatro focos. □

**Interpretación sobria:** cada imagen local puede reconstruir *todas las relaciones binarias* del módulo al cumplir la regla de cierre. No recupera por sí sola un radio físico, las seis longitudes de un tetraedro geométrico ni observables no incluidos en la interfaz.

### 4.2 Teorema GR3-T2 — Tres pruebas de circuito independientes

`K₄` tiene cuatro triángulos, pero sus cuatro paridades satisfacen una relación de dependencia: cada arista interviene en dos triángulos, de manera que el XOR de las cuatro paridades vale cero. Tres condiciones triangulares independientes bastan para fijar la cuarta.

La dimensión del espacio binario de seis aristas es seis; las relaciones coherentes forman el espacio imagen del operador `s↦δs`, de rango tres. Por tanto el conjunto de asignaciones coherentes tiene `2³=8` elementos. Hay `2⁶=64` etiquetados de aristas posibles y `64−8=56` no coherentes.

Cada uno de los 16 etiquetados de vértices produce el mismo resultado que su inversión global: `16/2=8` clases observables en las aristas. **No** se deduce aquí una secuencia cósmica «8 abierto → 16 cerrado»; de hecho, ocho es un *cociente* de dieciséis dentro de este modelo.

### 4.3 Teorema GR3-T3 — Cierre no equivale a unísono fuerte

Sea `s=(0,1,0,1)`. Sus diferencias de arista no son todas cero, y sin embargo la reconstrucción focal y las paridades triangulares son coherentes. Por tanto, *concordancia* no requiere igualdad de todos los focos.

Esto formaliza la distinción entre *una trama de diferencias compatible* y *cuatro focos idénticos*, evitando borrar diferencias acreditadas para fabricar un cierre.

## 5. Diferencia pendiente y ajuste mínimo (sin imponer radio)

**[DEFINICIÓN]** Si un etiquetado observado `b` no es coherente, establecemos el costo de ajuste combinatorio:

\[
\lambda(b)=\min_{s\in\mathbb F_2^4}\sum_{ij\in E}(b_{ij}\oplus s_i\oplus s_j).
\]

Equivale al número mínimo de **vínculos binarios** cuya etiqueta habría que modificar para que la trama tenga un cierre global. Esta minimización *no afirma* que una estructura física realmente cambie sus vínculos, ni define el mecanismo que selecciona uno de los cierres admisibles. Es un criterio matemático de discordancia con costos unitarios.

**GR3-T4 [TEOREMA para `K₄`].** Los 64 etiquetados se distribuyen exactamente así:

| Costo mínimo `λ` | Cantidad de etiquetados | Número de triángulos discordantes |
|:---:|---:|:---:|
| 0 | 8 | 0 |
| 1 | 48 | 2 |
| 2 | 8 | 4 |

**Prueba.** Cada modificación de una arista invierte la paridad de los dos triángulos que contienen esa arista. La suma de las cuatro paridades es siempre par, de modo que existen 0, 2 o 4 triángulos discordantes. Los 8 etiquetados coherentes tienen cero. Hay seis patrones posibles con exactamente dos triángulos discordantes y uno con los cuatro; para cada patrón hay 8 etiquetados de aristas, pues fijar las tres paridades independientes deja tres bits libres. Un cambio de la arista compartida por la pareja de triángulos corrige el patrón de dos; dos cambios adecuados corrigen el patrón de cuatro. □

**[CONTRAEJEMPLO de unicidad de ajuste].** El etiquetado con todas las aristas iguales a 1 tiene cuatro triángulos discordantes. Su ajuste mínimo es 2, pero hay varias elecciones equivalentes de qué dos vínculos corregir. Un costo mínimo **no determina por sí solo una historia ni un foco único**.

## 6. Teorema de imposibilidad de derivar el radio desde este cierre puro

**GR3-T5 [TEOREMA — límite del modelo].** Supongamos que `λ(b)` depende solo del etiquetado de aristas y el tamaño geométrico `r>0` no modifica la función `b` ni sus reglas de compatibilidad. Entonces para cualquier `r₁,r₂>0`:

\[
\lambda(b;r_1)=\lambda(b;r_2)=\lambda(b).
\]

**Prueba.** `r` no figura en la definición de `λ`, así que no puede alterar el mínimo. □

**Consecuencia:** no podemos afirmar que *el radio surge necesariamente para resolver el pendiente* utilizando solo este laboratorio XOR. El mecanismo radial debe construirse con un puente **independiente**, y la conexión con masa o gravedad está todavía más lejos.

### 6.1 Contrato para una extensión radial no circular

Haría falta una variable relacional medible `r` y una regla **derivada o motivada independientemente** que traduzca cambios radiales a cambios de restricciones o a pesos de concordancia:

\[
\mathcal A(s,r)=\sum_{ij\in E}w_{ij}(r)\,[s_i\oplus s_j\oplus b_{ij}(r)] + C(r).
\]

Aquí `b_ij(r)`, `w_ij(r)` y `C(r)` son *funciones aún desconocidas*. Si se eligen únicamente para producir una respuesta deseada, la derivación sería circular. Si `w` y `b` son constantes y `C=0`, no existe un radio preferido. El primer objetivo es justificar una de esas dependencias con la ontología, un modelo material independiente o una predicción observable.

Una manera de intentar falsar el mecanismo será comparar dos reglas de actualización que difieren en su tratamiento del radio, manteniendo iguales las relaciones iniciales: si ambas predicen las mismas clases de cierre, el radio no aporta una operación relacional distinguible en ese ensayo.

## 7. Módulos comunes y «nidos de eclipse» como intersección de soluciones

Dados dos módulos `M₁,M₂` con interfaz compartida `B`, llamemos `S₁|_B`, `S₂|_B` a las restricciones admitidas por sus proyecciones sobre esa interfaz. La condición de encuentro es:

\[
\mathcal N_B=(S_1|_B)\cap(S_2|_B)\neq\varnothing.
\]

- Si el conjunto común está vacío, no existe resolución compatible bajo las reglas actuales.
- Si contiene varias clases distinguibles, permanece indefinición contextual.
- Si contiene una única clase relevante para las consultas declaradas, hay concordancia contextual, no necesariamente un cierre material.

En geometría, dos tetraedros pueden compartir una cara y fijar una distancia transversal; cuando solo comparten un vértice siguen dejando libertad rotacional. Este contraste ya estaba demostrado en H-R2. No corresponde llamarlo masa/gravedad sin una dinámica.

## 8. Ritmo relacional sin reloj previo

**[DEFINICIÓN PROVISIONAL].** Sea una sucesión de registros o estados relacionales `X₀→X₁→…`. Un «ritmo» inicial es una regla de actualización `T` y el orden de los eventos donde una consulta o circuito se vuelve reconstruible. Una regla `T` que disminuya un costo de discordancia puede definirse matemáticamente, pero esa monotonía sería una **premisa adicional**, no una ley física derivada.

No existe aún una frecuencia `ω` salvo que se asigne una magnitud temporal y una ley de conversión. La expresión **bit unísono** nombra en esta etapa una condición de *consistencia de diferencias*, no un quantum físico de acción, una longitud de Planck ni una unidad de tiempo.

## 9. Masa y gravedad — puente físico deliberadamente abierto

**GR3-F1 [HIPÓTESIS].** Si un mecanismo radial independiente produce cierres estables que persisten ante perturbaciones, podría investigarse un observable asociado a esa persistencia como candidato a *masa efectiva*. No basta un índice abstracto de persistencia: falta explicar inercia, unidades y conservación cuando aplique.

**GR3-F2 [HIPÓTESIS].** Si los mismos cierres determinan cómo se actualizan distancias o geometría entre módulos, podría investigarse un observable de interacción como candidato gravitacional. **Derivar un gradiente de algún costo sin unidades no demuestra fuerza gravitatoria.**

**Condiciones mínimas de éxito externo:**

1. Definir variables de distancia y tiempo con unidades coherentes, y una ley dinámica bien puesta; indicar cómo surge la masa inercial en lugar de insertarla como constante independiente.
2. Mostrar cómo el mismo mecanismo produce una masa gravitacional compatible, incluyendo la universalidad experimental de la caída libre (dentro de sus límites observados).
3. Recuperar en el régimen adecuado el campo `∝1/r²` de una fuente aislada o explicar desviaciones falsables; no introducir esa ley sin derivación.
4. Recuperar aspectos comprobados de la relatividad general, al menos efectos gravitacionales sobre luz y relojes en el régimen pertinente, si se pretende competir como teoría gravitatoria fundamental.
5. Producir un observable independiente y un contraste cuantitativo antes de invocar datos del protón, radios cósmicos, espectro de luz o escala de Planck.

**Límite ontológico:** «masa y gravedad son el mismo mecanismo» es la propuesta del programa, no un resultado científico establecido. Tampoco el modelo XOR deriva la singularidad de un agujero negro ni la singularidad geométrica de relatividad general.

## 10. Relación con el desarrollo anterior y trazabilidad

- **R-F1:** reconstruir la geometría euclidiana desde Gram focal; requiere longitud de referencia y ángulos.
- **N-M1:** novedad de referencia, de tipo y de información relativa al registro.
- **H-R2:** dilatación de una misma imagen no genera profundidad informativa; pegados de tetraedros fijan o dejan libres relaciones transversales.
- **G-R3:** unísono de diferencias binarias y reconstrucción exacta desde cualquiera de cuatro focos; medición combinatoria de un residuo y demostración de que ese residuo solo no selecciona un radio.
- **CR-7:** las relaciones de aridad superior no deben eliminarse si la interfaz pierde información; ejemplos particulares comprimibles no prueban P=NP.

No trasladar el número `2³=8` de `K₄` a los cierres `4–8–16` sin una regla ontológica de correspondencia. No confundir aquí el vértice etiquetado `f` con la derivación física o ontológica del foco interno: **el foco de referencia es un rol formal; su origen sigue abierto**.

## 11. Falsadores y próximos ensayos

**F-GR3-1:** una imagen focal no reconstructiva bajo la regla declarada `D_f` refuta que el módulo correspondiente esté cerrado según este contrato.  
**F-GR3-2:** dos perspectivas cuyos resultados difieren después de normalizar la etiqueta global refutan su concordancia unísona.  
**F-GR3-3:** si modificar solamente el radio no cambia la compatibilidad de ningún vínculo, ese laboratorio no puede derivar una selección radial (teorema T5).  
**F-GR3-4:** una interfaz supuestamente suficiente que falla en una consulta futura admisible obliga a enriquecer la firma y no a llamar «novedad» al error de compresión.  
**F-GR3-5:** si el candidato de masa no tiene las unidades correctas o el campo efectivo no reproduce ensayos gravitacionales conocidos, falla la interpretación física aunque el cierre algebraico sea correcto.

**Protocolo siguiente.** Construir un modelo de proyecciones con radio definido independientemente (geometría de esferas, Gram focal y relaciones observables); establecer una regla de acoplamiento entre radio y vínculos, mantener simetría entre focos, medir cuántos cierres existen sin anclar uno y comparar con una hipótesis nula donde el radio solo reescala. Solo después implementar ritmo dinámico, masa/gravitación y observables de prueba.

## 12. Registro de afirmaciones

| ID | Afirmación | Estado |
|---|---|---|
| GR3-O1 | Foco interno y totalidad reconstructiva | POSTULADO ontológico |
| GR3-O3 | Mecanismo de ajuste concordante que crea referencia nueva | HIPÓTESIS |
| GR3-T1 | Reconstrucción `K₄` desde cualquier estrella si y solo si `b=δs` | TEOREMA |
| GR3-T2 | Tres paridades independientes; 8 etiquetados coherentes | TEOREMA |
| GR3-T3 | Consistencia no exige igualdad de todos los focos | TEOREMA |
| GR3-T4 | Distribución `8/48/8` de costo mínimo | TEOREMA + CONTROL FINITO |
| GR3-T5 | Concordancia solo XOR no fija radio | TEOREMA de límite |
| GR3-F1 | Persistencia de cierre → masa física | PUENTE ABIERTO |
| GR3-F2 | Ajustes entre cierres → gravitación | PUENTE ABIERTO |
| GR3-F3 | El bit unísono define un cuanto fundamental | NO ESTABLECIDO |

### Reproducción

```bash
python3 -m unittest -v test_unisono_gr3.py
python3 laboratorio_unisono_gr3.py
# Ejecución completa (incluye anteriores):
python3 -m unittest -v test_laboratorio.py test_reconstruccion.py test_novedad_modular.py test_profundidad_radial.py test_unisono_gr3.py
```

Todo el código usa solo la biblioteca estándar de Python. Se preservan los archivos históricos como antecedente, no se modifica el núcleo del repositorio del usuario y no se afirma ninguna validación física experimental.
