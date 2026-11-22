# Del principio de diferencia al recierre aritmético

**Nota de continuidad formal — 22 de noviembre de 2026**  
**Continuidad:** Núcleo Generativo Canónico (P0–P6), RA–01, CR–6, HC–02/03, R–RH–01.  
**Estado:** identidades estructurales demostradas; cálculo exacto en intervalos finitos; relación con la cota crítica **abierta**.

## Resumen

El principio generativo ordena una cadena: diferencia acreditada, comparación, residuo, herencia, novedad y recierre. En la estructura aritmética de divisibilidad, la inversión de Möbius constituye una realización exacta del recierre. Cuando la escala se duplica de `N` a `2N`, la diferencia local de cada nuevo entero `m` en `(N,2N]` es exactamente `-μ(m)` y desaparece al incorporar la nueva referencia.

Este hecho permite separar **cantidad de novedad** —un observable no negativo— de **compensación entre novedades** —una suma firmada—. El primer observable está totalmente determinado por los números libres de cuadrados. El segundo conduce a un criterio clásico equivalente a RH; su cota no se deduce de la sola identidad local. Se recupera así el punto de transferencia entre el núcleo del programa y la distribución de primos, sin introducir la cota deseada como premisa.

## 1. Realización aritmética del principio

La relación de comparación es `d | m` (divisibilidad). La función de Möbius `μ` es la inversa de la función constante `1` respecto de la convolución de Dirichlet:

`sum_{d|m} μ(d) = 1` si `m=1`, y `0` si `m>1`.

La propiedad es una identidad clásica, y aquí se interpreta como regla exacta de cancelación de diferencias en la retícula de divisores.

Para `N≥1` y `m≥1`, defínase el **defecto local truncado**

`F_N(m) = sum_{d|m, d≤N} μ(d)`.

**Proposición 1 (recierre de una octava).** Para cualquier entero `N≥1` y `N<m≤2N`,

`F_N(m) = -μ(m)`, y `F_{2N}(m)=0`.

**Prueba.** Todo divisor propio de `m` es `≤ m/2 ≤ N`. Por tanto, en la suma de todos los divisores de `m`, el único término ausente en `F_N(m)` es `μ(m)`. Como `m>1`, la suma total es cero. Para `2N` ya están todos los divisores. `□`

La estructura especifica una diferencia local con signo y un recierre exacto al incorporar la nueva referencia. Es la identidad ya registrada en los laboratorios previos; se preserva esa procedencia.

## 2. Dos observables distintos

En cada octava `(N,2N]`, la **energía de novedad local** es

`A_N = sum_{N<m≤2N} |F_N(m)|² = sum_{N<m≤2N} μ(m)²`.

**Proposición 2.** `A_N` cuenta exactamente los enteros libres de cuadrados de la octava. En contraste, la **compensación firmada** es

`S_N(t)=sum_{N<m≤t} μ(m)=-sum_{N<m≤t}F_N(m)`, para `N<t≤2N`.

Sea `B_j = max_{2^j<t≤2^{j+1}} |S_{2^j}(t)|`. La identidad exacta

`S_N(2N)² = A_N + 2 sum_{N<m<n≤2N} μ(m)μ(n)`

muestra que la cantidad de novedad está determinada por los términos diagonales, mientras la compensación depende de las correlaciones firmadas entre referencias.

**Precisión de contrato.** `A_N` es una norma cuadrática de una función de defectos sobre **enteros**; no es la energía funcional `Q_j = ||χ−P_jχ||²` de RA–01 en `L²(0,∞)`. Un puente entre ambos contratos exigiría un operador de transferencia con una cota específica.

## 3. Exactitud local y exigencia global

El criterio clásico de la función de Mertens `M(x)=sum_{n≤x} μ(n)` da:

`RH ⇔ M(x)=O_ε(x^{1/2+ε})` para cada `ε>0`.

En consecuencia,

`RH ⇔ para cada ε>0, B_j=O_ε(2^{j(1/2+ε)})` cuando `j→∞`.

**Prueba de equivalencia.** En una dirección, `S_N(t)=M(t)-M(N)` y la cota clásica controla ambos términos. En la otra, cualquier `M(x)` se descompone en una suma de intervalos diádicos completos y un tramo final. La suma de las cotas `2^{j(1/2+ε)}` está dominada por su mayor término gracias a una serie geométrica. `□`

La cota más rígida `|M(x)| ≤ √x` (conjetura clásica de Mertens) fue refutada, de modo que la exigencia correcta para este puente es la familia de cotas con cualquier `ε>0`, no una constante fija igual a uno.

El recierre exacto de `F_N(m)` garantiza la desaparición local del defecto al incorporar `m`, pero el control uniforme de los **prefijos** `S_N(t)` es una propiedad cuantitativa adicional. Los valores en extremos de bloques completos no bastan para garantizar cotas dentro de cada bloque.

## 4. Control adversarial de suficiencia

Sea `H=ℓ²({0,1,2,...})` con base `(e_k)`, `χ=√(2/3)e_0+sum_{k≥1}2^{-k}e_k`, `V_j=span(e_1,...,e_j)`.

La norma de `χ` es exactamente `1` y cada ampliación introduce una dirección nueva que recupera una parte positiva de la diferencia. No obstante, la distancia restante satisface

`Q_j=dist(χ,V_j)²=2/3+4^{-j}/3 → 2/3>0`.

**Prueba.** `sum_{k≥1}4^{-k}=1/3`; toda proyección sobre `V_j` conserva el componente `√(2/3)e_0` fuera del cierre de los subespacios, y la energía de los demás vectores omitidos es `4^{-j}/3`. `□`

Este modelo prueba que herencia, presencia de novedad, positividad de la ganancia y conservación de la unidad no fuerzan por sí solas el agotamiento del residuo. Su función es precisar qué parte del principio necesitaría fuerza cuantitativa adicional. Es compatible con el falsador previamente documentado de granularidad y cierre.

## 5. Nueva obligación de prueba dentro del principio

Se propone examinar la siguiente **obligación de transferencia**, sin adoptarla como postulado verdadero:

> Deducir desde la multiplicatividad, la inversión de Möbius y la estructura de recierre una desigualdad uniforme de compensación de prefijos en todas las octavas, o construir un control de observabilidad que conecte el defecto de divisibilidad con el residuo funcional de RA–01.

La primera vía tiene como observable exacto `B_j`; la segunda exige identificar y acotar el operador que transforma las novedades locales de divisibilidad en una ganancia de proyección. El simple conteo de novedades no establece ninguna de las dos cotas.

La investigación fundacional se localiza, por tanto, en la **necesidad de compensación** que puede emerger del recierre, no en ajustar directamente un exponente al resultado deseado.

## 6. Verificación reproducible

El archivo `verificar_puente.py` realiza **8.188 controles enteros exactos** del recierre local sobre octavas hasta `N=2048` y produce `datos_bloques.csv` con la energía de novedad y los máximos de prefijos firmados para `N=2^j`, `4≤j≤17` (`2N` hasta `262144`). Los cálculos no utilizan coma flotante para las identidades y no prueban cotas asintóticas.

Ejemplos:

| N | Novedades libres de cuadrados | Suma firmada completa | Máximo absoluto de prefijos |
|--:|--:|--:|--:|
| 1.024 | 621 | 11 | 17 |
| 2.048 | 1.246 | -26 | 32 |
| 16.384 | 9.958 | 58 | 105 |
| 131.072 | 79.672 | 44 | 145 |

La cantidad de novedades escala de modo distinto de su desbalance con signo. La reducción observada en esos intervalos es un hecho finito; no es una ley universal demostrada.

## 7. Estado de procedencia

- **Núcleo generativo (septiembre 2026):** P0–P6, diferencia, comparación, residuo, recierre, herencia+novedad.
- **RA–01 / CR–6 (21-XI):** contabilidad ortogonal y condición suficiente de ganancias acumuladas.
- **Granularidad y cierre (21-XI):** contraejemplo que separa herencia de agotamiento funcional.
- **HC–02 / HC–03 (21-XI):** reconstrucción de la fluctuación aritmética, herencia de potencias y criterios de bloques.
- **Teoría clásica:** inversión de Möbius, equivalencia RH–cota de Mertens (Titchmarsh, citado en Hu et al., *On a Mertens-type conjecture for number fields*), y criterio de Nyman–Beurling/Báez-Duarte.

**Estado final:** recierre local **DEMOSTRADO**; separación de observables **DEMOSTRADA**; cálculos **VERIFICADOS FINITAMENTE**; transferencia de principio a compensación crítica **ABIERTA**.

*Endless Monkey Project / Relational Geometry Program*
