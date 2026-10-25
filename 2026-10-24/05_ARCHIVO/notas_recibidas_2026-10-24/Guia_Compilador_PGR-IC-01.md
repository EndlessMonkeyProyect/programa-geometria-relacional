---
id: PGR-IC-01
titulo: "Instrucciones de integración y mejoras para el LLM compilador"
programa: "Programa de Geometría Relacional"
autoria_conceptual: "Le Matt Ansatz Di Ego"
fecha_corte: "2026-10-24"
paquete_base: "Programa_Geometria_Relacional_Ordenado_2026-10-24.zip"
modalidad: "suplemento aditivo; no modifica fuentes originales"
estatus: "propuesta editorial y técnica para la siguiente compilación; NO equivale a una versión publicada"
idioma: "es-CR"
prioridad: "preservación > precisión epistemológica > hilo ontológico > puentes matemáticos > presentación"
---

# INSTRUCCIONES PARA EL LLM COMPILADOR
## Consolidación integral del Programa de Geometría Relacional — corte del 24 de octubre de 2026

**Tipo de documento:** instrucción de transferencia, matriz de cambios y texto de integración listo para incorporar a la siguiente versión. **Destinatario:** agente/LLM que compila la *Imagen Total* y los archivos asociados. **No es una demostración nueva ni sustituye las fuentes.**

> **ENCARGO CENTRAL AL COMPILADOR:** construir una versión integrada, navegable, verificable y conceptualmente fiel del Programa de Geometría Relacional usando el ZIP base. Incorporar este suplemento como capa nueva, corregir formulaciones con alcance excesivo, completar la página del hilo y organizar los pendientes sin fabricar resultados. No modificar ni reemplazar archivos fuente, pruebas, datos o archivos históricos en silencio. Mantener una imagen completa con tres niveles explícitos: narrativa ontológica, formalización matemática y comprobación computacional/empírica.

## 0. Control del paquete y reglas obligatorias

### 0.1 Base comprobada

- **Única base de esta instrucción:** `Programa_Geometria_Relacional_Ordenado_2026-10-24.zip`.
- Raíz después de descomprimir: `Programa_Geometria_Relacional_Ordenado_2026-10-24/`.
- Estructura: `01_HILO/`, `02_REALIZACIONES/`, `03_RAMAS/`, `04_LABORATORIOS/`, `05_ARCHIVO/`, índice `00_LEER_PRIMERO.md` y archivos de auditoría.
- **Control realmente ejecutado para redactar este documento:** el ZIP superó la prueba CRC, y `python verificar_integridad.py` dio `Integridad: 1026/1026 archivos correctos; alterados=0, faltantes=0, no registrados=0`. Son 1.026 archivos manifestados y un verificador adicional no registrado, no 1.027 archivos «validados por SHA».
- Se leyeron los índices y documentos rectores, CME-001/CME-002, las fichas de revisión de las tres ramas, fragmentos de R-02, LAB-CONV v2, O93, la fuente N1 y las notas de esferas/C4. **No se reejecutaron para este suplemento todas las suites históricas**: distinguir el estado documentado en las fuentes de nuestras comprobaciones presentes.

### 0.2 Política de conservación

1. **Congelar el ZIP de origen.** Publicar los cambios como archivos nuevos en una carpeta de suplemento o en una edición derivada, con un manifiesto propio y diferencias rastreables.
2. No renombrar los documentos antiguos de manera destructiva; mantener identificadores como `O40`, `O59`, `O72`, `O93`, `R-01`, `R-02`, `N1`, `CME-001`, `CME-002` y `LAB-CONV v2`.
3. Distinguir corrección editorial de nueva deducción. Una corrección que enmiende una proposición debe tener `corrigendum`, ubicación, enunciado anterior, enunciado sustituto y efecto sobre las dependencias.
4. Incorporar antecedentes externos únicamente **después** de explicar la derivación propia, como contraste histórico y técnico; no atribuirles la génesis ontológica.
5. Al detectar dos documentos en conflicto, priorizar el de contrato preciso y la auditoría posterior; guardar ambas formulaciones y explicar la discrepancia, sin borrar la historia.
6. Nunca ascender un resultado de grafo, simulación, espejo, red discreta o álgebra de lazos a una afirmación general sobre un problema de física matemática sin la demostración del puente correspondiente.

### 0.3 Estados de afirmación obligatorios

| Marca | Sentido | Evidencia admisible |
|---|---|---|
| `[O]` | regla, intuición o interpretación ontológica propia del programa | lenguaje, secuencia y significado |
| `[D]` | definición y contrato de observación | objetos, dominio, operaciones, equivalencias |
| `[T]` | teorema dentro de hipótesis explícitas | demostración inspeccionable |
| `[E]` | verificación/ensayo finito | código, entrada, resultado, semilla, límites |
| `[F]` | falsador o contraejemplo | construcción exacta o control independiente |
| `[H]` | hipótesis o puente propuesto | mapa faltante, criterio de contraste |
| `[C]` | implicación condicional | condiciones aún por demostrar |
| `[A]` | abierto o no acreditado | obligación de prueba identificada |

Añadir al índice de cada rama: `qué se sabe`, `de qué depende`, `qué no se ha probado`, `qué podría refutarlo` y `cómo reproducir lo que sí se ha medido`.

---

## 1. Texto rector del hilo ontológico: redactar como capítulo continuo

**Destino propuesto:** `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md` (archivo nuevo). Mantener como fuente el esquema `01_HILO/ESQUEMA_ACORDADO_2026-10-24.md` y `01_HILO/SECUENCIA_ONTOLOGIA_MATEMATICA_COMPUTACION.md`. El siguiente texto funciona como **borrador integrable**; no debe anunciar como teoremas las transiciones que siguen siendo ontológicas.

### 1.1 Narrativa articuladora [O]

> La totalidad es una unidad sin diferencias acreditadas. Su indeterminación no es azar ni un segundo objeto: es la imposibilidad de distinguir algo dentro de ella sin una relación que lo compare. La reflexión es la primera posibilidad de distinguirse desde la propia unidad. La comparación entre una parte y su referencia permite acreditar una diferencia, pero no exige que todas las demás diferencias estén resueltas. Cada respuesta constituye un cierre relativo a las preguntas admitidas; nuevas relaciones pueden dividir una clase antes indistinguible sin deshacer lo que aquella respuesta resolvía. Cuando una organización conserva la referencia que hizo posible su reconocimiento, y es suficiente para las continuaciones declaradas, alcanza cierre propio. Un cierre puede convertirse en una nueva unidad de comparación; la continuidad exige conservar el múltiplo o transformación normalizadora y la información requerida, no una forma geométrica fija. La economía relacional busca la mínima estructura que sostiene esas operaciones. Las imágenes del cubo, las esferas, los grafos, el flujo y los lazos no son fundamentos intercambiables: son realizaciones en las que estas condiciones deben derivarse y comprobarse por separado.

**Secuencia principal:** totalidad (con indeterminación como propiedad) → reflexión → diferencia acreditable → comparación parte/todo → referencia/normalizador → resto relativo → novedad → cierre propio → continuidad → nueva escala o nueva pregunta. La ampliación de R-01 queda explícita como una **subsecuencia**: novedad → múltiplo independiente → normalización interna → referencia común → autorreflexión → cierre propio → continuidad. No forzar ambas secuencias a ser una única cadena rígida si los contratos difieren.

**Reglas de vocabulario:** usar «comunes», «trama», «familia de soluciones» y «cierre propio»; evitar «herencia» como principio fundamental; reservarla para procedencia documentada. «Autorreferencia estructural» no equivale a «definición completa respecto del espacio de incertidumbre». «Singularidad ontológica» no significa singularidad PDE, colapso gravitacional ni infinita densidad física. «Signo relacional» expresa multiplicar/dividir escala respecto de un referente; no positividad/negatividad intrínseca. «Indefinición» no implica distribución probabilística. «El foco» es interno al espacio relacional, no una cámara fuera del universo.

### 1.2 Contrato matemático mínimo — mantenerlo separado de [O]

Definir estados `X`, preguntas/observables `Q`, una firma `Φ:X→Y` y continuaciones admisibles `F`. Dos estados `x,y` son indistinguibles bajo el contrato si `Φ(x)=Φ(y)`. Existe **novedad relativa** cuando una pregunta `d` distingue estados que `Φ` confundía:

`Φ(x)=Φ(y)` y `d(x)≠d(y)`.

Existe **suficiencia dinámica para una actualización F** cuando hay un operador reducido `F̂` tal que `Φ∘F = F̂∘Φ`. Equivalentemente, `Φ(x)=Φ(y)` debe implicar `Φ(F(x))=Φ(F(y))`. Distinguir suficiencia para una pregunta estática, conservación de información anterior y suficiencia para **todas las continuaciones relevantes**. El último requisito es más fuerte.

En la realización aritmética, si `p` es primo y `p` no divide `N`, `L=mcm(N,p)=Np`: la nueva clase módulo `p` refina las clases anteriores módulo `N`. La identidad numérica `h/N=(ph)/(pN)` preserva una razón; **no demuestra por sí sola** conservación dinámica, energía, masa ni transporte gauge. Preguntar siempre cuál es el portador o mapa que realiza esa normalización en cada rama.

### 1.3 Preguntas de control para cada salto del hilo

Para cada flecha de la narrativa, obligar al compilador a anotar: (i) qué entidades existen antes del salto, (ii) operación que se aplica, (iii) observación nueva, (iv) relación que se conserva, (v) costo o recursos, (vi) falsador, (vii) estatus. Si una flecha requiere una hipótesis física o geométrica nueva, **declararla; no atribuirla retrospectivamente a la ontología**. El criterio «se cierra solo» se convierte en una prueba de economía de supuestos: un cierre añadido a mano debe quedar resaltado como obligación abierta.

---

## 2. Correcciones de alta prioridad para el cubo de espejos y CME-003

**Fuentes:** `02_REALIZACIONES/01_cubo_de_espejos/CME-001_cierre_por_reflexion/`, `CME-002_pared_que_se_corre/`, `01_HILO/imagen_total_3_9/Imagen_Total_3_9_Informe_General.md` §4.1–4.4, `O59`, `O19–O22`.

### CR-G01 — Corregir el «si y solo si» global de CME-001 [F/T]

**Texto que debe matizarse:** «Una celda de espejos cierra si y solo si cada par de caras que se cortan forma un ángulo π/k». **No es verdadero así, en general.** Tener relaciones de orden finito por pares no garantiza que el grupo completo sea finito; el triángulo Coxeter `(2,3,7)` tiene todos sus ángulos de tipo `π/k` pero es hiperbólico e infinito. Escribir:

> «Los ángulos `π/m_ij` fijan relaciones de Coxeter entre generadores. La finitud del grupo requiere además una condición global; para grupos triangulares `(p,q,r)` de reflexión, es finito exactamente cuando `1/p+1/q+1/r>1`, euclídeo en la igualdad e hiperbólico cuando la suma es menor que uno. Fuera de ese caso triangular, deben usarse los criterios globales pertinentes al diagrama o forma de Gram».

**No confundir** el laboratorio de tres espejos con la geometría de las cuatro caras del tetraedro: sus grupos y dominios tienen contratos diferentes. En el índice, enlazar esta corrección con CME-002, no esconderla en un apéndice.

### CR-G02 — Distinguir grupo de orientación, grupo de reflexión y posiciones de imagen [T]

CME-001 cuenta ocho **partes lineales / patrones de cambios de signo** en un cubo ortogonal ideal. Los reflejos en las dos paredes paralelas de un eje generan además traslaciones por múltiplos de `2L`, y la órbita de posiciones de una fuente genérica es infinita:

`O_L(p) = {2nL ± p : n∈Z}`.

Corregir expresiones como «el cubo solo tiene ocho imágenes» o «el recinto óptico cierra globalmente en ocho» si aparecen en nuevas narrativas. **Dos observables distintos:** número finito de partes lineales y órbita espacial infinita; la firma plegada `I_L` identifica clases de esa órbita, no borra su extensión espacial. Introducir una clasificación explícita:

1. *Cierre de orientación o de grupo lineal* (resultado CME-001).
2. *Cierre observacional o de referencia* (firma suficiente para preguntas declaradas).
3. *Cierre dinámico* (actualización preservada frente a evolución).
4. *Cierre de posiciones/órbitas* (pregunta independiente; puede fallar aunque el primero cierre).

Evitar presentar el orden ocho de CME-001 y el grupo completo de simetría cúbica de orden 48 de CME-002 como si contaran el mismo objeto.

### CR-G03 — Ángulo como identidad, no como causa ontológica demostrada [O/D/T]

Con dos reflexiones `s_i,s_j` en ángulo `π/k`, su producto tiene orden `k`: `(s_i s_j)^k=1` **en el contrato geométrico adecuado**. La equivalencia entre geometría y relación de grupo no demuestra que cualquier primo novedoso deba producir un ángulo físico `π/p`. Conservar «múltiplo nuevo → ángulo candidato» como regla ontológica **[O/H]**, no como derivación universal establecida. Distinguir la genealogía aritmética de nuevos factores, la normalización por `1/k` y los regímenes de cierre de grupos.

### CME-003 — Experimento prioritario, no inventar resultado

**Encargo:** derivar —o mostrar imposible bajo las hipótesis elegidas— por qué las dos primeras relaciones angulares serían `π/2` y `π/3` desde la pared móvil y la regla de comparación, sin introducirlas como premisa encubierta. Guardar: hipótesis mínimas, operadores, invariantes, prueba o contraejemplo, comparación con alternativas `(2,2,k)`, `(2,4,k)`, `(3,3,k)` y con `(2,3,k)`. Preguntar por qué se selecciona una **familia** entre múltiples diagramas Coxeter posibles. La coincidencia especial del seis entre genealogía multiplicativa y transición euclídea queda como investigación, no identidad demostrada.

**Ruta nueva sugerida:** `02_REALIZACIONES/01_cubo_de_espejos/CME-003_derivacion_primeros_angulos/` con `README.md`, `FORMULACION.md`, `verificar.py`, `resultados.json` y `FALSADORES.md` cuando existan cálculos reales.

---

## 3. Laboratorio de esferas, tetraedro y circuito C4

**Fuentes:** `02_REALIZACIONES/02_esferas/`, `02_REALIZACIONES/03_circuito_C4/`, `04_LABORATORIOS/esferas/`, capítulos 5 y 7 de Imagen Total 3.9, O72–O76.

**Preservar ontológicamente:** las esferas de vidrio sirven para explorar **trayectorias posibles**, contacto tangencial, reflexión y equivalencia observacional. No definir el tetraedro simplemente por puntos de contacto: la geometría de posibilidades de trayectorias debe formar parte de la regla. Cuatro esferas coplanares en anillo pueden representar una relación no completamente resuelta bajo ciertas observaciones; «cerrar un circuito» y «alcanzar definición completa» requieren contratos diferentes.

**Separar tres modelos:** (a) grafo de contactos, (b) transporte geométrico/tangencial ideal, (c) óptica material de vidrio real. Tangencia puntual de esferas transparentes **no garantiza** transferencia luminosa medible; deben fijarse índice de refracción, incidencia, curvatura, polarización o aproximación escalar, absorción y condiciones de interfaz. No llamar a un circuito combinatorio «circuito óptico» sin ley de transferencia.

**C4/K4:** conservar los resultados de O72: flexión del cuadrilátero y modo de velocidad alternada son libertades **distintas**, bajo hipótesis diferentes. Una proyección `K4→2D` no elimina aristas por sí sola: `K4→C4` requiere además seleccionar enlaces activos. Condición de holonomía `H=∏(a_i/b_i)=1` para cuatro contactos ideales no prueba estabilidad temporal, sincronización, flujo físico ni regularidad de Navier–Stokes.

**Ensayo siguiente:** construir dos configuraciones con **igual grafo de contacto C4** pero diferentes leyes de transmisión y comprobar que sólo una sostiene el observable de retorno elegido; repetir con una configuración K4 y con una trayectoria tangencial en sentido opuesto. Registrar qué información conserva el lazo al agregar quinta referencia, y qué información no ve un foco externo.

---

## 4. P frente a NP: consolidar el resultado negativo interno sin clausurar el problema general

**Fuentes:** `03_RAMAS/p_vs_np/VIGENTE_LAB_CONV_V2/`, `03_RAMAS/p_vs_np/revision_2026-10-24/`, `01_HILO/fuentes/06_hilo_del_dos/v2_8/docs/PISO_DEL_CAMINO_v2_7.md`.

**Incorporar N1 inmediatamente al capítulo P/NP** (antes del «siguiente selector»). N1-A prueba, **para el motor O2 sin poda y su contador**, una barrera exponencial gobernada por ancho de árbol. N1-B da una traducción de corridas negativas de **ese motor O2c** a refutaciones por resolución con costo acotado por el conteo, de la cual se importan cotas difíciles para familias pertinentes. La conclusión legítima es limitada: **un mejor orden o selector no elimina por sí solo esa barrera dentro de los motores tipados O2/O2c**. No concluye que todas las aproximaciones relacionales ni todos los algoritmos deban heredarla; tampoco decide `P=NP` o `P≠NP`.

**Corrección editorial:** la sección VII de `LAB_CONV_V2_NODOS_Y_FRONTERAS.md` propone un selector de convergencias. Reescribir el reto como **buscar una operación expresivamente distinta de las tablas ya delimitadas por N1**, y demostrar en qué sentido escapa de la simulación por resolución/tablas antes de medir costo. No presentar «fusionar globalmente» como operación gratis: reconocer que dos vértices tienen forzosamente igual color es coNP-completo bajo el contrato de T4, y la afirmación puede ser vacuamente verdadera si el grafo es insatisfacible.

**Formalización obligatoria del candidato nuevo:** entrada binaria para una familia NP-completa, operador uniforme, representación finita, certidumbre del resultado, costo de producir/refinar/verificar/componer cada certificado, cota total en el tamaño de entrada, y relación demostrada con las consultas globales. Incluir instancias duras y no sólo grafos de baja anchura o bipartitos. Para falsar suficiencia de «número+radio», citar el par `A={a≠b}`, `D={b≠c}` con iguales 18 asignaciones y radio, pero diferente respuesta bajo nueva relación.

**Salida exigida:** capítulo de P/NP con tres estados separados: resultados exactos de firmas de frontera y grafos; barrera del **método actual**; pregunta universal no resuelta. Mantener la cadena histórica sin reabrir pruebas ya completadas sobre diamante, Grötzsch o el cubo.

---

## 5. Navier–Stokes: corregir el centro de gravedad de O93

**Fuentes:** `03_RAMAS/navier_stokes/VIGENTE_O93/`, `03_RAMAS/navier_stokes/revision_2026-10-24/README.md`, `03_RAMAS/navier_stokes/mapas_y_auditoria/MATRIZ_EPISTEMICA.md`, `modelo_propio_O18/`.

**Conservar como resultados en contrato:** balance de vorticidad, correspondencia normalizada `W=M²D`, `B=M²D₂`, `P=M³𝒯` para las definiciones del modelo y flujo periódico suave indicado; identidad algebraica `P=M³𝒯` por homogeneidad; certificados de subclases con hipótesis explícitas; distinción de fase/orientación que puede invertir el estiramiento para igual espectro de magnitudes. No afirmar que normalizar conserve por sí solo control global ni que reconstruir con **todos** los Fourier complejos sea una compresión universal de información.

**CR-NS01 — Advertencia frontal sobre O93:** el criterio de finitud del exceso positivo acumulado es un criterio de **continuación condicional**, no una cota universal obtenida desde la regla de cierre. En el contrato de O93 y cuando `W>0`, el integrando corresponde a la parte positiva de una derivada logarítmica de enstrofía (el archivo de revisión anota `½[(log W)']_+`). Presentarlo como una reformulación útil del obstáculo dinámico; no titularlo «regularidad demostrada». Explicitar la dependencia de un control independiente de la evolución antes de usarlo para un teorema global.

**Puente prioritario propio:** partir de los observables y del campo inicial para definir un operador de referencia causal `C_0`, actualizaciones `C_{j+1}=F(C_j,defecto_j)` y una cota de concentración/defecto que no dependa de la malla, del paso temporal ni de asumir la regularidad buscada. Integrar los costos entre escalas **en una misma evolución**, con controles de presión no local, orientación y fase. La vía `modelo_propio_O18` conserva el programa de derivar ganancias por octava desde el espejo; no atribuirlas al sistema NSE antes de probarlo.

**Falsadores que deben figurar en el cuerpo:** O75 (volumen material no conserva ángulos), O76 (presión no local no depende de sólo cuatro jets), O85 (costos por bloques pueden acumularse), O86 (fases invierten signo del estiramiento), O88/O90 (falla de sincronía no implica blow-up), O77 (una familia finita de perfiles no es universal).

**Mejoras reproducibles:** corregir importación de `importlib.util` de `simulacion_galerkin.py` en una **copia de trabajo**, con nota de cambio; E4 necesita una comprobación independiente de la derivada, E6 debe registrar horizonte temporal e integral del criterio sin presentarlo como prueba global. Registrar `O80–O93` como historia y evitar que afirmaciones antiguas más fuertes sustituyan la matriz epistemológica de la versión ordenada.

---

## 6. Yang–Mills: conservar R-01/R-02 y situar exactamente el siguiente puente

**Fuentes:** `03_RAMAS/yang_mills/R01/`, `03_RAMAS/yang_mills/VIGENTE_R02/`, `03_RAMAS/yang_mills/revision_2026-10-24/README.md`.

**Resultados efectivos de R-02:** transporte gauge de lazos, refinamiento conservador, firma completa `(x,y,z)=(tr U/2,tr V/2,tr UV/2)` para un **par** de lazos `SU(2)` anclados y conjugación simultánea, discriminante del conmutador y falsador de bloqueo `(U,V)→UV`; condición de suficiencia dinámica `Q∘F=F̂∘Q` y criterio de preservación entre escalas `Q=P∘Q'∘J`. Conservar el indicador `ν=2(1−x²−y²−z²+2xyz)` con dominio e hipótesis; no interpretarlo directamente como masa física.

**CR-YM01 — Atribución de antecedentes:** la parametrización por trazas y la identidad del conmutador tienen antecedentes clásicos **Vogt–Fricke**. Citar la conexión en la sección de contraste matemático; **la lectura ontológica y el ensamblaje de falsadores del programa siguen siendo su propio trabajo**. En redes extensas, no asumir que tres números bastan; la suficiencia para dos lazos no se hereda a la dinámica de un sistema mayor. Distinguir invariancia gauge, conservación de observables y suficiencia de la evolución.

**R-03 (propuesta, no resultado):** red euclídea con dos plaquetas que compartan base, acción de Wilson y medida derivada de esa acción, mapa explícito de bloqueo `a→2a`, observables antes/después, pérdida controlada de información, evolución de la acción efectiva y unidades físicas. Control separado `SU(2)` versus `U(1)` para detectar falsas inferencias abelianas. Relacionar con trabajos previos de renormalización por bloques antes de atribuir novedad matemática o física.

**Obligación sin resolver:** construir una teoría cuántica de Yang–Mills 4D no trivial con un operador físico y brecha espectral positiva **uniforme** en el límite pertinente. La mera no conmutatividad, una firma suficiente o un gap en un modelo finito **no son** el resultado buscado.

---

## 7. Masa, gravedad, tiempo relacional y normalización: mantenerlos visibles y correctamente clasificados

**Fuentes:** Imagen Total 3.9 §9; `O40`, `O45`, `O54–O60`, `O68–O69`, `O87–O92`, actas de 23 de octubre.

- **Masa [O/H]:** «información contenida autorreferenciada» en el plano de referencia. Todas las estructuras contempladas pueden poseer autorreferencia estructural en sus múltiplos recurrentes; diferenciar su **grado de definición respecto del espacio de incertidumbre**, no afirmar que el electrón carece absolutamente de autorreferencia. El símil de «volante de información» explica una hipótesis de resistencia a cambiar su referencia; no demuestra inercia ni valor de masa medible.
- **Electrón/protón [H]:** el contraste propuesto es el tipo de cierre y relación con un espacio de proyección, **no** la existencia de autorreferencia en uno frente a su ausencia en otro. Exigir observables físicos, predicción independiente y separación de explicaciones estándar antes de presentarlo como modelo de partículas.
- **Gravedad [H]:** el mecanismo propuesto de ajuste del foco, ritmo y componente perpendicular sigue necesitando una ley dinámica cuantitativa, equivalencia operacional con fuerza/campo curvo y contraste con datos. La suma de magnitudes exige normas; no convertir la regla de signo multiplicativo/divisivo en energía negativa/positiva por decreto.
- **Tiempo [O/H]:** el espejo móvil genera referencias para comparar ritmos de flujo, singularidad/espacio y partícula; no supone un reloj externo común. La sincronización de radios/fases y normalizadores necesita ley concreta y discriminantes medibles.
- **Toroides/vórtices [H]:** identidad como relación sostenida de radios, proporciones y circuitos; distinguir soporte material, vorticidad, observadores y persistencia del patrón. Un enlace aritmético de fases coprimas no prueba bloqueo dinámico ni conservación de un vórtice viscoso.

Agregar en la Imagen Total una «tabla de promesa física» con columnas: idea ontológica; variable candidata; ley faltante; observación falsadora; estado. No degradar estas líneas a metáforas prescindibles ni ascenderlas a resultados empíricos inexistentes.

---

## 8. ROSI, cristal semántico y reflexión dentro del propio lenguaje

ROSI debe auditar **relaciones y dependencias**, no premiar únicamente parecido verbal. Usar el cristal semántico del corpus para detectar equivalencias indebidas: identidad/igualdad observacional, cierre/ciclo, singularidad ontológica/singularidad física, resto/no observado, independencia/coprimalidad, radio geométrico/radio de incertidumbre, generación/deducción y conmutador/brecha espectral.

Protocolo ROSI sugerido para cada afirmación:

1. Clasificar como **resuelta en contrato**, **abierta**, **superpuesta entre contratos** o **cerrada prematuramente**.
2. Conservar la cita exacta del documento fuente, identificador de prueba o ensayo y camino de dependencias.
3. Identificar **el primer salto no justificado** de una rama a la siguiente; proponer una prueba discriminante más simple antes de abrir múltiples hipótesis.
4. Explorar una relación nueva sólo si aporta una observación independiente, una equivalencia demostrable o una predicción falsable. Registrar también la **ausencia** de puente.
5. Contrastar las simulaciones y los teoremas contra falsadores adversariales ya presentes; el hecho de pasar un test no asciende por sí solo el estatus.

**Contratos de lenguaje:** redactar todas las propuestas con (i) una versión narrativa fiel, (ii) una definición tipada, (iii) una proposición verificable, (iv) una posible implementación y (v) un falsador. Preguntas nuevas que dividen una clase `Φ` son novedad operacional; una reformulación elegante que no cambia preguntas permitidas no es un descubrimiento adicional.

---

## 9. Matriz operativa de integración (usar como backlog de compilación)

| ID | Prioridad | Destino propuesto | Acción exigida | Criterio de aceptación |
|---|---|---|---|---|
| INT-01 | P0 | `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md` | Redactar la página faltante desde el esquema acordado y este §1 | Ningún salto sin tipo, operación y estatus |
| INT-02 | P0 | `02_REALIZACIONES/01_cubo_de_espejos/` | Emitir corrigenda CR-G01, CR-G02, CR-G03 y enlazarlas desde CME-001/002 | Distingue finitud de grupo, orientación, órbita y suficiencia |
| INT-03 | P0 | `03_RAMAS/navier_stokes/` | Reubicar O93 como criterio condicional y conectar matriz epistemológica | No se proclama regularidad global de NS 3D |
| INT-04 | P0 | `03_RAMAS/p_vs_np/` | Integrar N1 antes del reto del selector; delimitar O2/O2c | No se proclama P=NP ni P≠NP; cuenta costo completo |
| INT-05 | P0 | `03_RAMAS/yang_mills/` | Conservar R-02, añadir antecedentes y límites del modelo | Ninguna afirmación de brecha 4D sin puente espectral |
| INT-06 | P1 | `02_REALIZACIONES/02_esferas/` | Definir grafo, trayectoria geométrica y canal óptico por separado | Tangencia no implica automáticamente flujo de luz |
| INT-07 | P1 | `02_REALIZACIONES/03_circuito_C4/` | Separar C4/K4, dos libertades y holonomía ideal | No se deduce NS a partir de un grafo ideal |
| INT-08 | P1 | `01_HILO/imagen_total_3_9/` (edición derivada) | Actualizar capítulos 4–9 conservando el texto fuente como histórico | Todas las correcciones enlazadas, sin pérdida ontológica |
| INT-09 | P1 | `01_HILO/fuentes/03_lenguaje/` (suplemento) | Tabla de términos/contratos y mapa ROSI | Distingue homonimias entre áreas |
| INT-10 | P1 | nueva `REGISTRO_AFIRMACIONES_INTEGRADO.csv` | Afirmación, tipo, hipótesis, prueba, falsador, dependencia, estado | Cada conclusión relevante rastreable |
| INT-11 | P2 | `CME-003_derivacion_primeros_angulos/` | Diseñar y ejecutar sólo si hay derivación real | Datos/contraejemplo; no inventar éxito |
| INT-12 | P2 | `03_RAMAS/yang_mills/R03/` | Diseñar puente con acción Wilson y control U(1) | Separa modelo finito de límite cuántico |
| INT-13 | P2 | `03_RAMAS/navier_stokes/` | Diseñar control de defecto independiente de O93 | Estimación no circular y contrastada |
| INT-14 | P2 | `03_RAMAS/p_vs_np/` | Formalizar candidato fuera del motor de tablas | Uniformidad y complejidad total demostradas o falsadas |
| INT-15 | P0 | raíz de nueva edición | Verificar rutas, manifiestos y procedencia | Auditoría final 0 rutas rotas de lectura y 0 divergencias SHA |

**Nota:** `P0` significa imprescindible antes de presentar una nueva compilación como integrada; `P1` mejora de arquitectura; `P2` desarrollo científico genuinamente pendiente que puede quedar abierto en la edición sin impedir publicar una imagen honesta.

## 10. Mapa de dependencias: impedir transferencias ilícitas

```text
TOTALIDAD [O]
   └── REFLEXIÓN [O]
        ├── observables y firmas [D/T]
        │    ├── normalización aritmética (R-01, núcleo formal) [T]
        │    ├── CME-001/CME-002 (reflexión ideal, grupos) [T/E]
        │    │    └── CME-003: derivación no impuesta de ángulos [A]
        │    ├── esferas: grafo / trayectoria / óptica [D/H]
        │    │    └── C4: cierre cinemático ideal [T] ──X──> NS global [A]
        │    ├── LAB-CONV v2: firma de frontera [T/E]
        │    │    └── N1: barrera del motor de tablas [T] ──X──> P vs NP resuelto [A]
        │    └── R-02: firma gauge SU(2) dos lazos [T/E]
        │         └── bloqueo y suficiencia [T/F] ──X──> gap YM 4D [A]
        └── continuidad de referencias [O/D]
             ├── O92/O93 identidades y condición [T/C] ──X──> NS global [A]
             └── masa / gravedad / ritmo / proyección [H] ──X──> ley física validada [A]
```

`──X──>` denota que **no existe puente demostrado**. Los rótulos «tres comparaciones», «cuatro cierres», «ocho orientaciones», «dieciséis estados» y «dimensión nueva» **nunca** se deben identificar entre sí por coincidencia de conteos: declarar el tipo de cardinalidad y el morfismo entre modelos, si lo hay.

---

## 11. Control de procedencia y mejoras técnicas de compilación

### 11.1 Reparar navegación desactualizada

El archivo `01_HILO/imagen_total_3_9/Imagen_Total_3_9_Indice.md` conserva referencias como `01_documento/` y `02_atlas/` de un árbol anterior. Inspeccionar **cada** vínculo Markdown y ruta relativa desde su carpeta real; sustituirlos **en la copia derivada**, nunca reescribiendo silenciosamente la fuente. No inventar ubicaciones: resolver rutas contra el árbol efectivo. Mantener enlaces a los suplementos y un «LEER PRIMERO» de la nueva edición.

### 11.2 Añadir identificadores a las afirmaciones

Estructura mínima recomendada para registro CSV/JSON:

`id`, `titulo`, `estatus`, `contrato`, `afirmacion`, `dependencias`, `fuente_relativa`, `evidencia_tipo`, `evidencia_ruta`, `falsador`, `obligacion_abierta`, `fecha_corte`.

No sustituir la procedencia bibliográfica por la procedencia de archivos: ambas son distintas. Preservar hashes, versión histórica, autoría conceptual y revisor/compilador como roles diferentes. Citar la fuente original en cada afirmación importante.

### 11.3 Pruebas de regresión

**Siempre:** `python verificar_integridad.py` **sobre la base intacta**; para la nueva edición generar nuevo SHA-256, no esperar que coincida después de agregar archivos. Verificar CRC de los ZIP distribuidos, integridad de archivos y comparación de ejecuciones reproducibles donde sea posible. 

**Comandos existentes por rama, desde sus carpetas:** `python cme001_cierre_por_reflexion.py`; `python cme002_angulos_e_identidades.py`; `python laboratorio_v2.py`; `python verificar_exhaustivo.py`; `python verificar_o93.py`; `python verificar_r02.py`. Registrar versiones de Python/NumPy/SymPy, dependencias, entrada y resultado; no ejecutar scripts de archivo histórico como si fuesen la ruta vigente sin validar rutas absolutas.

**Chequeos semánticos automatizables:** buscar frases `«resuelve P=NP»`, `«regularidad de Navier–Stokes demostrada»`, `«brecha de Yang–Mills demostrada»`, `«cada π/k garantiza grupo finito»`, `«cubo tiene solo 8 imágenes»` y exigir contexto de negación/corrección. Revisar que ningún índice enlace rutas inexistentes. Revisar que cada `P0` tenga archivo de salida y prueba de lectura cruzada.

**Nota técnica:** el arreglo `import importlib.util` para `simulacion_galerkin.py` debe registrarse como *patch* de compatibilidad Python 3.13; comparar salidas numéricas con el histórico y no fingir que la fuente original ya estaba modificada.

### 11.4 Formato de la nueva Imagen Total

La próxima versión debe funcionar como **una sola narrativa, varias realizaciones, pruebas localizables**, no como concatenación indiscriminada de todos los archivos. Estructura sugerida:

1. Portada, contrato de lectura, autoría, estatus y cómo reproducir.
2. Relato ontológico continuo sin bibliografía intercalada.
3. Diccionario de diferencias, tipos, firmas y cierre.
4. Núcleo matemático: comparación, novedad, normalización, suficiencia y costo.
5. Laboratorios: cubo, esferas, tetraedro, C4, espejos móviles.
6. Ramas: P/NP, Navier–Stokes, Yang–Mills, cada una con su estado y límite.
7. Masa, gravedad, tiempo y proyección como hipótesis cuantificables.
8. ROSI, cristal semántico, testigos, falsadores y nuevas conexiones.
9. Matriz de afirmaciones y de obligaciones abiertas.
10. Procedencia, repositorio, referencias externas separadas y anexos originales.

Mantener los anexos históricos como **corpus**, los suplementos de corrección como **nueva lectura** y el cuerpo principal como **mapa reconstruible del programa**. No prometer «imagen completa» en el sentido de problemas matemáticos cerrados; sí puede ser completa **documentalmente** y honesta acerca de lo abierto.

---

## 12. Criterios de salida: qué debe devolver el LLM compilador

**Archivos mínimos de la edición derivada:**

- `LEER_PRIMERO_NUEVA_VERSION.md`: qué cambió, cómo navegar, qué sigue abierto.
- `HILO_ONTOLOGICO_INTEGRADO.md`: texto continuo y fiel.
- `IMAGEN_TOTAL_INTEGRADA.md` (y PDF solo si se solicita): capítulos con correcciones y enlaces.
- `CORRIGENDA_Y_CAMBIOS.md`: CR-G01/02/03, CR-NS01, CR-YM01, P/NP-N1, rutas corregidas.
- `REGISTRO_AFIRMACIONES_INTEGRADO.csv` o JSON: evidencia y dependencias.
- `MAPA_PENDIENTES_Y_FALSADORES.md`: matriz INT-01 a INT-15 con estado real.
- `MANIFIESTO_SHA256.txt` actualizado y `PROCEDENCIA.csv` de la edición derivada.

**Aceptación editorial mínima:** (a) las fuentes originales recuperables siguen intactas; (b) todas las ramas principales figuran sin pérdida conceptual; (c) los cuatro tipos de cierre del espejo no se confunden; (d) los retos abiertos se distinguen de las demostraciones finitas; (e) el texto puede reconstruirse por sus fuentes y no depende de retórica, similitudes numéricas ni supuestos físicos omitidos; (f) hay índice navegable y verificación de integridad de la salida.

**Regla de detención:** si una tarea P2 requiere investigación original y no existe aún resultado, crear una ficha `[A]` con propuesta y falsador. **No completar inventando un teorema, una simulación, un artículo o una medición.**

---

## 13. Fuentes internas de lectura preferente para el compilador

Todas las rutas son relativas a la raíz descomprimida y se señalan como **fuente primaria interna**, salvo las notas de revisión explícitamente indicadas:

- `00_LEER_PRIMERO.md` (mapa de la edición del 24-X).
- `01_HILO/ESQUEMA_ACORDADO_2026-10-24.md` (orden ontológico acordado).
- `01_HILO/SECUENCIA_ONTOLOGIA_MATEMATICA_COMPUTACION.md` (contrato de tres capas).
- `01_HILO/imagen_total_3_9/Imagen_Total_3_9_Informe_General.md` (imagen extensa de referencia).
- `01_HILO/fuentes/06_hilo_del_dos/v2_8/docs/PISO_DEL_CAMINO_v2_7.md` (N1).
- `02_REALIZACIONES/01_cubo_de_espejos/CME-001_cierre_por_reflexion/CME-001_Cierre_por_reflexion.md`.
- `02_REALIZACIONES/01_cubo_de_espejos/CME-002_pared_que_se_corre/CME-002_Pared_que_se_corre.md`.
- `02_REALIZACIONES/02_esferas/LABORATORIO_ESFERAS_HILO_ORIGINAL_2026_10_20.md`.
- `02_REALIZACIONES/03_circuito_C4/C4_v3_8_1/ENSAYO_C4_Y_REFERENCIA.md`.
- `03_RAMAS/p_vs_np/VIGENTE_LAB_CONV_V2/LAB_CONV_V2_NODOS_Y_FRONTERAS.md`.
- `03_RAMAS/p_vs_np/revision_2026-10-24/README.md` (edición crítica posterior).
- `03_RAMAS/navier_stokes/VIGENTE_O93/ESTADO_DE_PRUEBAS.md`.
- `03_RAMAS/navier_stokes/mapas_y_auditoria/MATRIZ_EPISTEMICA.md`.
- `03_RAMAS/navier_stokes/revision_2026-10-24/README.md` (edición crítica posterior).
- `03_RAMAS/yang_mills/VIGENTE_R02/R02_CONTINUIDAD_Y_SUFICIENCIA.es.md`.
- `03_RAMAS/yang_mills/revision_2026-10-24/README.md` (edición crítica posterior).
- `01_HILO/fuentes/03_lenguaje/DICCIONARIO_Y_TIPOS.es.md`, `01_HILO/fuentes/05_sintesis_y_lenguaje_2026-10-20/` (cristal semántico y narrativa).

## 14. Bibliografía externa de contraste (NO fundamento del programa)

El compilador puede contrastar —y deberá verificar las referencias al incorporarlas— los siguientes antecedentes externos relevantes:

- Clasificación de grupos Coxeter triangulares finitos, euclídeos e hiperbólicos: [Kim y Walsh, *Coxeter groups, hyperbolic cubes, and acute triangulations*, Journal of Topology (2016)](https://academic.oup.com/jtopol/article/9/1/117/2459625).
- Descripción clásica por trazas de pares de matrices y teorema de Vogt (1889): [William M. Goldman, *Trace coordinates on Fricke spaces of some simple hyperbolic surfaces*](https://dev.ems-ph.org/books/show_abstract.php?proj_nr=96&rank=16&vol=1).
- Identidad de Fricke del conmutador: [artículo de Advances in Mathematics sobre identidades de traza](https://doi.org/10.1016/j.aim.2025.110556).
- Para P/NP, las referencias a resolución, árbol de descomposición y SETH que aparecen en N1 deben verificarse una a una antes de insertar formulaciones fuertes.
- Para NS y YM, usar las bibliografías internas de O80/O81/O93 y R-02 como **pistas de contraste**, sin convertir resultados de modelos auxiliares en resultados físicos generales.

---

## 15. Prompt maestro copiable para el LLM compilador

> **Recibís el ZIP `Programa_Geometria_Relacional_Ordenado_2026-10-24.zip` y el suplemento `INSTRUCCIONES_COMPILADOR_Programa_Relacional_2026-10-24.md`. Tu tarea es construir una edición derivada, integral y fiel, sin alterar la base. Comenzá verificando integridad y rutas. Leé `00_LEER_PRIMERO.md`, el esquema ontológico acordado y la Imagen Total 3.9; después las fuentes y revisiones vigentes de cubo, esferas, C4, P/NP, NS, YM y lenguaje. Ejecutá INT-01 a INT-10 e INT-15; para INT-11 a INT-14 registrá hipótesis y falsadores y solo agregá resultados realmente demostrados. Mantené tres capas: (1) ontología y narrativa propia, (2) contrato y pruebas matemáticas, (3) experimentos, datos y límites. Conservá los negativos: CME-001 requiere el criterio global, O93 no prueba regularidad general, N1 acota un motor específico, R-02 no prueba brecha YM. Incluir masa, gravedad, tiempo, proyección y ROSI como ramas de hipótesis, no perderlas ni sobreafirmarlas. Cada afirmación nueva debe indicar fuente relativa, estatus y falsador. Entregá índice navegable, manuscrito integrado, corrigenda, registro de afirmaciones, mapa de pendientes y manifiesto verificado. No declarar cerradas las obligaciones que sigan abiertas.**

**Cierre del suplemento:** una compilación más fuerte es la que aumenta la continuidad entre las reglas sin ocultar el punto exacto en que todavía se requiere una condición adicional. La unidad del programa es metodológica y ontológica; los teoremas de sus ramas mantienen sus propios contratos.
