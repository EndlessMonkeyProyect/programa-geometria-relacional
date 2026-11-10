# Registro de reejecución — 10 de noviembre de 2026

## Comprobación al incorporar el expediente en GitHub

Se verificaron las 14 sumas SHA-256 del paquete recibido. Con Python 3.12.14 y NumPy 2.3.5 pasó el verificador autónomo: reconstrucción del tetraedro, 56 conjuntos de cinco estados, 336 trayectorias de exclusión, 56 ternas locales y 175 conteos aleatorios pequeños comparados con fuerza bruta.

La primera reejecución del laboratorio distribuido reprodujo los 11 conteos principales, pero se detuvo en una repetición de DPLL por su límite fijo de ocho segundos. Se quitó ese límite **solo en las repeticiones de tiempos**, conservando el máximo de 250.000 nodos. Con esa corrección, la corrida completa terminó: coincidieron los 11 conteos principales y los 8 de conexiones largas con los datos suministrados; también pasaron 144 comprobaciones de compuertas, 30 controles aleatorios y dos negativos. Los tiempos de esta máquina no sustituyen las mediciones del archivo original.

Se ejecutó además el control C7 del laboratorio de intercambio y convergencia. Los conteos de inclusión-exclusión y eliminación coincidieron en los casos completados; el caso favorable de 96 variables dio 10.656 y el desfavorable de 32 variables dio 5.220, conforme a los datos publicados. No se ejecutaron C1–C6 ni C8 en esta incorporación.

## Registro suministrado con la entrega

El archivo suministrado `RESULTADOS_RELACIONES_DISTRIBUIDAS.json` se conservó intacto. En un directorio separado se ejecutó completamente el programa de relaciones distribuidas. Coincidieron todos los pares de tamaño, cantidad de cláusulas, número de raíces parciales y conteo exacto de los **11 controles principales** y los **8 controles con conexiones largas**. También pasaron las 144 comprobaciones locales de compuertas, 30 controles aleatorios y dos controles negativos.

Este registro es una **reejecución de la misma implementación**, no una implementación independiente de todo el experimento. Los conteos pequeños se comparan además contra enumeración primaria; en tamaños mayores el programa usa un contador primario de referencia. Las medianas de tiempo dependen del entorno y no deben interpretarse como cotas generales. La suite completa de matrices de intercambio no se volvió a ejecutar en esta revisión.
