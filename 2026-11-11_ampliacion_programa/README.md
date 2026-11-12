# De la distinción a la economía — ampliación verificable

**Endless Monkey Project**  
*Relational Geometry Program*  
**Corte conceptual:** 11 de noviembre de 2026 · **Versión:** 0.1 · **Estado:** propuesta de integración para revisión

## Resultado de esta entrega

El paquete conecta el hilo del programa —indefinición, diferencia, referencia, distinción, comunes, herencia, cierre, información y economía— con un contrato matemático compartido. Contiene tres proposiciones elementales demostradas, un test de límite informacional al cambiar de referencia, un laboratorio finito que contrasta espejos, módulos, orientación y paridad, y un registro de obligaciones para extender el programa.

Su aportación principal es **integrar y operacionalizar**: los teoremas de interfaz contextual y muchos ejemplos ya figuran en las ediciones anteriores. Una identidad entre laboratorios no se presume a partir de la analogía; cada puente indica qué conserva y qué deja pendiente.

## Lectura sugerida

1. [`00_HILO_Y_CONCEPTOS.md`](formalizacion/00_HILO_Y_CONCEPTOS.md) — continuidad ontológica y determinantes.
2. [`01_CONTRATO_UNICO.md`](formalizacion/01_CONTRATO_UNICO.md) — tipos, consultas, actualizaciones y medidas.
3. [`02_RESULTADOS_Y_PRUEBAS.md`](formalizacion/02_RESULTADOS_Y_PRUEBAS.md) — factorizar, reabrir, medir el residuo.
4. [`03_PUENTES_ENTRE_LABORATORIOS.md`](formalizacion/03_PUENTES_ENTRE_LABORATORIOS.md) — espejos, esferas, modularidad, CSP, física.
5. [`04_ECONOMIA_COMPLETA.md`](formalizacion/04_ECONOMIA_COMPLETA.md) — contabilidad y comparadores.
6. [`MATRIZ_ROSI.md`](ROSI/MATRIZ_ROSI.md) — pruebas, falsadores, preguntas abiertas.
7. [`RUTA_DE_INTEGRACION.md`](integracion/RUTA_DE_INTEGRACION.md) — incorporación sin reemplazar el núcleo.
8. [`MAPA_RELACIONES.mmd`](mapa/MAPA_RELACIONES.mmd) — grafo de construcción; [tabla CSV](mapa/RELACIONES.csv) editable.
9. [`AUDITORIA_ECONOMIA_2026-11-11.md`](antecedentes/AUDITORIA_ECONOMIA_2026-11-11.md) — auditoría previa conservada sin modificar.
10. [`REFERENCIAS_Y_VERSIONES.md`](integracion/REFERENCIAS_Y_VERSIONES.md) — procedencia; [`REGISTRO_AUDITORIA.json`](ROSI/REGISTRO_AUDITORIA.json) para reutilización.
11. [`ENGLISH_SUMMARY.md`](integracion/ENGLISH_SUMMARY.md) — English abstract.

## Reproducción local

Python >= 3.9; biblioteca estándar, sin red ni dependencias adicionales:

```bash
python3 -I laboratorios/laboratorio_referencias.py
python3 -I laboratorios/laboratorio_referencias.py --json resultados/reproduccion.json
python3 -I -m unittest discover -s laboratorios -p 'test_*.py' -v
```

El verificador contiene pruebas independientes de: firma de pared, no factorización por cambio de pared; conservación de consultas bajo refinamiento; límite de bits del residuo modular; compatibilidad y ruptura de actualización; seis relaciones XOR del tetraedro binario; dos orientaciones con las mismas distancias geométricas; herencia y novedad en CNF.

## Estructura de estados y alcance

- **[O]** lectura ontológica; **[D]** definición; **[T]** resultado demostrado en hipótesis explícitas; **[E]** control ejecutable finito; **[I]** interpretación entre contratos; **[A]** abierto; **[F]** falsador.
- Los resultados de esta entrega **no** constituyen una cota para 3-SAT general, la resolución de P frente a NP o una deducción física de Yang–Mills, Navier–Stokes o la gravedad.
- Antes de copiar una afirmación al documento central, cotejar la versión de origen, su prueba y el alcance declarado; la incorporación es propuesta, no publicación consumada.

## Fuentes de continuidad

- [Imagen Total 4.0, 10-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_imagen_total_4_0/Imagen_Total_4_0.md)
- [¿Dónde se ahorra el cálculo?, 8-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-08_economia_del_calculo/informe.md)
- [¿Qué cálculo deja de hacerse?, 10-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-10_que_calculo_deja_de_hacerse/PAPER_ES.md)
- [Recierre contextual y costo de una interfaz](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/02_formal_core/contextual_reclosure_and_resource_cost.es.md)
- [Laboratorio óptico v5.1](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/laboratorios/laboratorio_optica_radios_v5_1)

**Nota de edición:** La línea institucional se conserva exclusivamente como *Endless Monkey Project / Relational Geometry Program*.
