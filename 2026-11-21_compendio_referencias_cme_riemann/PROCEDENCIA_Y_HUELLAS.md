# Huellas de archivos fuente y estado de consolidación

Este archivo documenta las notas de trabajo usadas para preparar el compendio. Las huellas SHA-256 identifican los archivos de trabajo recibidos para la consolidación; la identidad con versiones remotas de GitHub se comprueba por separado.

| Archivo de trabajo | SHA-256 | Uso |
|---|---|---|
| `ANEXO_TECNICO_ES.md` (anexo técnico del 20 XI) | `964c6d2e0a5358d22a1105481c3dc0474937f32fe8d76e3a0a1d2ffc6e543e83` | Consolidado en el compendio |
| `Mecanismos del programa frente a la regla de eliminación entre escalas.md` | `e25a7d5e94538475be5227b4c2c30900a671ddbe0e60ec6ea2f1eb893bbab5ae` | Consolidado en el compendio |
| `CME_RH_PUENTE_REFLEXIONES_Y_CIERRE_2026-11-21.md` | `131e80fb23e956b884e5ad98fec82a73b3bc274df6ec609c1d0dcb4f8f199f1e` | Consolidado en el compendio |
| `ENSAYO_CME_ARIT_1024_2048_2026-11-21.md` | `248bc8d823bb09c4445f77f127f22089efe24072cc3cf64d25f97daa5469e0f7` | Consolidado en el compendio |
| `FOCOS_DETERMINACION_CME_RH_2026-11-21.md` | `954e1a41af24c3cb49bec864f6420c88fa49b8e14593707ea0b514b01e69dd72` | Consolidado en el compendio |
| Nota de auditoría preliminar sobre el marco de Masullo | `e43fd5a5d4916f84af5217de4476383bfaa769faafe0d6ee0089b537c3193440` | Consolidado en el compendio |
| `resultados/registro_mecanismos_original.txt` | `0ab2748b9a2cc6decbc211d17735ea7c32c15bb8d90fa5047f0c0d5d528cc4eb` | Registro previo de $e_m^2$ y $\gamma_{2^j}$ |
| `resultados/registro_bloques_primos_original.txt` | `8d6db3d949af95a055f3cb438e4db13b14cdf71541f4cee18ecf2eb797ca3086` | Registro previo de bloques de primos |
| `resultados/salida_prueba_reglas_de_peso_original.txt` | `b702a6ebfbacbaab2d2bc1b1bc7406c06aaec856237607d5529cb4f334ec49c9` | Salida previa de `scripts/prueba_reglas_de_peso.py` |

**Duplicado comprobado:** el anexo técnico del 20 XI tiene los mismos bytes que `2026-11-20_resolucion_granularidad_riemann/ANEXO_TECNICO_ES.md` de la entrega del 20 XI. El compendio unificado lo sustituye en esta publicación.

**Registros y recálculo.** Los scripts originales `mecanismos.py` y `bloques_primos.py` dependen de `prueba_ley_L.py`, que no forma parte de esta carpeta; sus registros se conservan como procedencia. Las cifras de `registro_mecanismos_original.txt` que usa el compendio ($e_m^2$ para $m=1,\dots,2048$, $\gamma_{2^j}$ y la comparación de recetas en $N=2048$) se reproducen de forma independiente con `scripts/recalcular_gram.py`, que solo depende de `scripts/prueba_reglas_de_peso.py`.

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program
