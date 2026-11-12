# Propuesta de incorporación al repositorio

## Destino recomendado

`programa-geometria-relacional/2026-11-11_ampliacion_programa/` — nueva carpeta fechada, sin sobrescribir la Imagen Total 4.0 ni los artículos del 8 y el 10 de noviembre.

## Orden de incorporación

1. **Documentos**: subir esta carpeta como versión de trabajo `v0.1` con referencia a las publicaciones previas y al borrador rector del 11-XI, que conserva su condición de revisión del autor.
2. **Pruebas**: ejecutar `python3 -I -m unittest discover -s laboratorios -p 'test_*.py' -v` desde la carpeta; registrar salida y entorno. Verificar también JSON del laboratorio.
3. **Trazabilidad**: enlazar desde el `README.md` principal a esta entrega, describiendo qué puente formal agrega; mantener títulos de documentos existentes sin reescribir historia o fechas.
4. **Corrección de nomenclatura**: abrir revisión puntual del artículo/solicitud del 8-XI para distinguir `F⊨C` (herencia) de `F⊭C` (novedad). Conservar la formulación original en historial.
5. **Imagen Total futura**: proponer subsección *De la distinción a la economía*, con la matriz de obligaciones y el resultado de suplemento informacional; publicar esa edición solo tras revisión del texto rector.
6. **Verificación externa**: solicitar contraejemplos a los resultados marcados [T] y evaluaciones separadas para las rutas [A].

## Texto breve propuesto para README principal

> **11 de noviembre de 2026 — De la distinción a la economía.** Entrega de integración en revisión: contrato común para referencias y consultas, límite exacto de información adicional al cambiar de referencia, puentes de los laboratorios de espejos, modularidad y tetraedro, controles finitos reproducibles y matriz ROSI de obligaciones. Extiende el hilo ontológico sin atribuir nuevas cotas a 3-SAT general ni conclusiones físicas a las analogías. [Ver carpeta de la ampliación](2026-11-11_ampliacion_programa/README.md).

## Comandos Git (después de descomprimir en la raíz de un clon)

```bash
python3 -I -m unittest discover -s 2026-11-11_ampliacion_programa/laboratorios -p 'test_*.py' -v
git add 2026-11-11_ampliacion_programa/
git commit -m "Integrar continuidad ontologica, economia y laboratorios de referencia"
git push origin main
```

La acción `git push` requiere las credenciales y permiso de escritura correspondientes. **Este paquete todavía no está subido**.

## Borradores y aprobaciones

`De_la_indefinicion_al_cierre_de_la_informacion_v01_2026-11-11.md` fue localizado como documento rector en revisión. Esta carpeta lo cita conceptualmente, pero **no lo incorpora ni declara aprobado**. Una vez revisado, guardar el texto completo con su propia versión y actualizar aquí la referencia.

## Manifiesto de compatibilidad

| Fuente existente | Tratamiento |
|---|---|
| Imagen Total 4.0 | conservar, futura adenda revisada |
| Economía 8-XI v2 | citar teoremas y corregir etiqueta herencia/novedad por PR separado |
| Cálculo que deja de hacerse 10-XI v0.3 | conservar datos; no rehacer benchmark sin ejecutar el comparador |
| Formal anterior de recierre contextual | reconocer prioridad documental de su prueba de suficiencia |
| Laboratorio óptico v5.1 | conservar algoritmos; esta entrega solo prueba un subcaso exacto de pared |
| Suplemento focal del tetraedro | mantener diferencias entre geometría, orientación, rigidez, XOR y contactos |
