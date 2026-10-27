# Revisión independiente de R-02 · 27 de octubre de 2026

`chequeo_independiente_R02.py` está escrito desde cero: no importa ni ejecuta el código de R-02. Sobre 5000 pares aleatorios de SU(2) comprueba lo siguiente:

| Afirmación de R-02 | Error máximo |
|---|---|
| `ν = 2(1 − x² − y² − z² + 2xyz)` | 1,1·10⁻¹⁵ |
| `D = 1 − x² − y² − z² + 2xyz = \|a×b\|²` | 6,7·10⁻¹⁶ |
| Región de firmas `\|z − xy\| ≤ √((1−x²)(1−y²))` | 0 |
| T3, dirección recíproca: se reconstruye explícitamente la conjugación que une dos pares con la misma firma | 8,8·10⁻¹² |
| T1: covariancia de caminos | 1,3·10⁻¹⁵ |
| T4: el testigo de bloqueo da el mismo `UV` con `ν = 2` y `ν = 0` | exacto |

**Lectura.** T1 a T7 son correctos: T1, T3 y T4 se comprueban numéricamente aquí; los demás, por lectura de sus pruebas. El bloque algebraico es clásico: la firma por trazas es el teorema de Fricke–Vogt, su extensión a k lazos es de Procesi, y la reconstrucción por lazos de Wilson es de Giles (1981). La nota de revisión del 24 de octubre ya lo señala.

Ejecutar: `python chequeo_independiente_R02.py` (requiere `numpy`). El script tiene aserciones: falla si alguna afirmación no se cumple. La salida está en `resultados.txt`.
