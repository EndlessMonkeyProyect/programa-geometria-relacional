# Instrucciones para integrar la actualización del 22 de noviembre de 2026

**Rama recomendada:** `main`, mediante una rama de revisión y pull request.  
**Repositorio de destino:** `EndlessMonkeyProyect/programa-geometria-relacional`.  
**Acción solicitada:** incorporar como **carpeta nueva** bajo `2026-11-17_escalas_relacionales_riemann/`; conservar los originales existentes sin sobrescribirlos.

## Pieza principal

`ACTUALIZACION_CONSOLIDADA_ES.md` es la **única exposición editorial** del avance. Las carpetas `SOPORTES/` contienen documentación y ejecuciones anteriores, preservadas con procedencia y SHA-256; **no representan 16 teoremas adicionales** ni 16 publicaciones nuevas.

## Contenido y fidelidad

- `SOPORTES/FUENTES_CONCEPTUALES/`: textos fundacionales, notas de octubre, fuentes LaTeX de Mersenne y documentos Biblioteca recuperados. Se excluyó de la copia pública una fuente TeX con metadatos de identidad personal; la edición pública equivalente conserva el desarrollo matemático. En dos fuentes TeX se unificó únicamente la grafía del seudónimo. Los demás `.md`/`.tex` conservan sus bytes; los `.txt` son materializaciones de lectura identificadas como tales.
- `SOPORTES/PAQUETES_HISTORICOS/`: **16 ZIP históricos inalterados**, incluidos los laboratorios HC-01/02/03, aparición, acarreos, análisis de octavas, RA–01/HC–03, principio de Möbius, coherencia y frontera.
- `SOPORTES/DESARROLLOS_EXTRAIDOS/`: archivos originales de los ZIP accesibles directamente: documentos, PDF existentes, scripts, tablas, figuras y manifiestos anteriores. Archivos `.pyc` se mantienen solamente en los ZIP.
- `SOPORTES/COMPARACIONES_EXTERNAS/`: comparaciones técnicas a terceros preservadas **como contexto**, no como fuente de prueba.
- `INDICE_ARCHIVOS.csv`, `MATRIZ_RESULTADOS.csv` y `MANIFIESTO_SHA256.txt`: auditoría integral de procedencia y alcance.

## Verificación sin instalaciones adicionales

Desde la carpeta que contiene el documento maestro:

```bash
python3 verificar_paquete.py
```

El verificador usa sólo Python estándar y aplica: integridad SHA-256 de todos los archivos del paquete, control de ZIP históricos, pruebas aritméticas exactas del recierre local, identidad de frontera, inversión binaria y transporte del bit.

El script imprime sólo caracteres ASCII, para evitar fallos por codificación en Windows. La prueba no depende de NumPy. Los laboratorios históricos que usan NumPy se ejecutan desde sus propias carpetas si se decide auditarlos de nuevo, sin reemplazar sus registros anteriores.

## Criterio editorial para el PR

**Título sugerido:** `Riemann: integración y trazabilidad desde reflexión y bit hasta el recierre (22-XI-2026)`.

**Descripción sugerida:**

> Se consolida el orden conceptual original y se enlazan RA–01, HC–01/02/03, CME–002, acarreos, octavas de Mersenne, recierre de Möbius y coherencia de frontera. Se acredita la Proposición F del 21-XI como antecedente; se adjuntan fuentes y laboratorios sin atribuir prioridad retrospectiva. Las identidades demostradas, las equivalencias clásicas, los ensayos finitos y la obligación aritmética global quedan separados.

## Antes de fusionar

1. Revisar `MATRIZ_RESULTADOS.csv` frente a los manuscritos originales y conservar seudonimos y fechas documentadas.
2. Revisar el estado de paquetes ya publicados: si existe una fuente canónica idéntica en el repositorio, preferir **enlace y hash** en lugar de otra copia en `main` cuando el tamaño total sea relevante. El presente ZIP conserva ambos para permitir una integración autónoma.
3. Ejecutar `python3 verificar_paquete.py` y comprobar que no se modificaron los históricos.
4. Confirmar la ubicación relativa de los enlaces antes de fusionar.
5. Declarar el alcance como **integración documental y laboratorio**, no prueba de RH/GRH.

**Estado de esta copia:** material preparado para revisión en un pull request; el ZIP original permanece fuera de la publicación porque contiene la fuente excluida.

Endless Monkey Project / Relational Geometry Program
