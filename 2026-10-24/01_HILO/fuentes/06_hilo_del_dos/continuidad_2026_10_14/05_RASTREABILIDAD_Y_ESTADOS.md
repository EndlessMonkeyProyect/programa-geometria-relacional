# Rastreabilidad, alcance y reglas de incorporación posterior

## Archivos del núcleo v2.8 examinados (NO MODIFICADOS)

- `README.md` — orden de lectura y estados consolidados.
- `docs/HILO_DEL_DOS_FORMALIZACION_v2.md` — tesis ontológica y lenguaje como hilo vertebral.
- `docs/CONTINUIDAD_ONTOLOGICA_Y_ESTADOS_v2_8.md` — reglas editoriales y límites entre capas.
- `docs/N1_B_CERTIFICADOS_Y_PRIORIDAD_v2_8.md` — inducción O2c→resolución con cota 1.5 candidatos del motor.
- `docs/PISO_DEL_CAMINO_v2_7.md` — costo en el motor O2 sin poda.
- `docs/T8_DEL_LENGUAJE_AL_ESPACIO_v2_8.md` — geometría y frontera física.
- `docs/GENEALOGIA_Y_CIERRE_v2_5.md` — historia en enteros vs en orden/agrupación algebraica.
- `experiments/o2c_v1_6/` — motores de grafos O2c originales.
- `SHA256_MANIFEST.json` — integridad según v2.8.

## Anexos históricos para cotejo (COPIA, no injerto)
- `FUENTES_COTEJO/MF52_INTERFACE_AS_CAPSULE_COMPILATION_BARRIER.md` — memoria compacta vs aplazamiento.
- `FUENTES_COTEJO/MF63B_recierre_acreditado_compatibilidad_v1.md` — `Join+Project` semántico y barrera de costo.
- `FUENTES_COTEJO/O2_CAPSULAS_GRAFOS_INTERFAZ_RADIO_Y_COSTO_v1_4.md` — algoritmo tabular y cambio de camino.
- `FUENTES_COTEJO/O2B_ORTOGONALIDAD_PREGUNTA_CAMBIO_DEL_MAPA_v1_5.md` — consulta y ortogonalidad, controles y no-go.
- `FUENTES_COTEJO/O2C_SELECTOR_RELACIONAL_MAPA_ADAPTATIVO_v1_6.md` — selector que usa densidad relacional y sus resultados.
- `DATOS_EXPERIMENTALES/INFORME_DENSIDAD_MARCO_2026-10-14.md`, `DATOS_EXPERIMENTALES/INFORME_INDEPENDENCIA_RELACIONAL_2026-10-14.md` y CSV/script — pruebas exploratorias de 81 grafos.

## Estado antes de solicitar integración

| Afirmación | Estado mínimo acreditable |
|---|---|
| Un cierre contextual exacto puede ser nueva referencia para continuaciones declaradas | DERIVADO bajo contrato MF-34/MF-63B/MF-97 |
| Dos estructuras que se juntan «pasan a ser una» semánticamente bajo normalizador suficiente | DERIVADO/DEFINICIÓN tipada; exige especificar puertos y preguntas |
| El resultado de Join/Project/Normalize es del mismo tipo algebraico de relación | DERIVADO cuando la clase admite esos operadores; no implica economía |
| Nunca hacen falta más clases de estructuras a nuevas profundidades | CONJETURA no formalizada universalmente; diferenciar gramática de configuración |
| Toda normalización reduce el número de distinciones necesarias para toda futura pregunta | FALSA si se amplían contextos; hay testigos O1d y O2b |
| Toda normalización reduce el costo computacional | NO DEMOSTRADO; O2/O2c muestran costos dependientes de trayectoria |
| Independencia de restricciones predice radio y costo | OBSERVADO en casos finitos; correlación y causalidad no demostradas |
| P=NP como consecuencia del programa actual | ABIERTO |
| YM mass gap, radiación/tiempo físico o masa como derivación | ABIERTO |

## Política de incorporación del eventual dictamen
1. No borrar ni reescribir fuentes originales, incluso si contienen vocabulario histórico luego precisado.
2. Separar corroboración, corrección y falsación; anotar los ejemplos adversarios en vez de esconderlos.
3. No declarar «teorema» algo sustentado solo por enumeración finita.
4. Identificar para cada propuesta nueva a qué archivo/versión precedente remite y qué exactamente añade.
5. Llevar el juicio de otro LLM a una **propuesta revisable**, no al núcleo automáticamente.
- `FUENTES_COTEJO/MF34_CONTEXTUAL_INVARIANT_AND_TRANSFER_LOAD.md` — invariante contextual exacto, equivalencia bajo contextos.
- `FUENTES_COTEJO/MF44B_normalizacion_causal_cierre_global_v1.md` — tasa de propagación relacional y separación profundidad/anchura.
- `FUENTES_COTEJO/10_MF98_ECONOMIA_Y_RECURSO_DEL_REINGRESO.md` — contrato operacional Build/Update/Read.
- `FUENTES_COTEJO/MF104_PESO_DE_NOVEDAD_Y_TRANSVERSALIDAD.md` — peso de novedad, no-go del salto a la brecha física de Yang–Mills.

**Otra fuente cotejada no incorporada como copia:** `MF86_AUTORREFERENCIA_IDEMPOTENCIA_NORMALIZACION_v0_1.md`, accesible en la biblioteca original; no pudo materializarse en esta sesión. Su suficiencia, idempotencia y composicionalidad están documentadas también en MF-63B y MF-98; el revisor debe consultar la fuente MF-86 si va a atribuirle un lema específico.
