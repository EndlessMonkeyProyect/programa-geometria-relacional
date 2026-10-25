# Suplemento O17-F — Escalera de resolución del presupuesto de vorticidad (Navier–Stokes)

Aplica el criterio de O17 a la rama de Navier–Stokes: solo es contenido del plano lo que no cambia al refinar la descripción con la escala física fija. El mismo flujo (corrida A de la rama, Re_λ ≈ 48) se evoluciona desde un estado común en N = 64, 128, 192 y 256 (kmax·η ≈ 1, 2, 3 y 4). Cada diagnóstico se clasifica según si converge.

Entrada: `../START_HERE_3_5_4.es.md`. Documento: `docs/01_O17F_ESCALERA_DE_RESOLUCION_NS.es.md`. Criterios fijados antes de correr: `PRERREGISTRO_O17F.json`.

## Resultado

- **Reproducción independiente.** La auditoría 128↔192 de la rama se reconstruye desde cero en doble precisión y coincide a 3–4 cifras. Las estadísticas de un instante caen dentro de su IC95 en 24 de 26 comparaciones con las tablas publicadas.
- **Las conclusiones de clase se sostienen.** Las medianas y fracciones de primer orden, el papel de la presión y el de la viscosidad, y las probabilidades de bajo giro quedan acreditadas desde kmax·η ≈ 2–3.
- **El término viscoso de segundo orden puntual no está convergido ni en N=192.** 𝒱_c cambia 9 % y 𝒴 6 % entre N=192 y N=256.
- **La pertenencia de estados individuales al canal de bajo giro depende de la descripción.** El índice de Jaccard frente a N=256 es 0.77 en N=192.
- **El signo de la tasa neta d log|b|/dG no se puede afirmar.** Su IC95 en N=256 es [−1.16, +0.52].
- **Nota sobre el prerregistro.** Con el criterio registrado, 11 de 19 estadísticas son contenido del plano. Otras 7 están acreditadas en N=192 pero fallan la monotonía por ruido de muestreo; se informan aparte, sin reclasificarlas.

## Reproducir

```bash
python -B -m unittest discover -s 19_escalera_resolucion_NS_2026_10_19/tests -v
E=19_escalera_resolucion_NS_2026_10_19/experiments/escalera_ns_o17f.py
python -B $E spinup --runs RUNS
for N in 64 128 192 256; do python -B $E nivel --runs RUNS --N $N; done   # ≈ 2 h con 2 núcleos; N=256 usa ≈ 5 GB
python -B $E analizar --runs RUNS --out salida
```
