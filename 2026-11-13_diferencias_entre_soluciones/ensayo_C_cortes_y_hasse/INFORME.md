# Conservar diferencias bajo cambios de corte y recuperación de Hermite

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Ensayo C · nota de prueba, 13 de noviembre de 2026**

## Objeto y resultado

Se examinaron dos operaciones concretas de construcciones publicadas: (A) la **identidad de ocho cuadrados con signos**, utilizada en la descomposición tensorial de Anthropic, y (B) la **recuperación por valores y derivadas de Hasse**, utilizada en la ruta de interpolación del artículo de OpenAI. Se añadió a ambas una referencia booleana de peso, $`w`$, para transportar cantidad de configuraciones, suma de posiciones y cuadrados de posiciones. Los ensayos utilizan exclusivamente aritmética exacta, con Python estándar, y cuentan con aserciones independientes.

Los resultados locales son: (i) la identidad firmada se verificó en $`8^4=4.096`$ entradas y su transporte de los tres momentos conservó el resultado; (ii) cada pieza tensorial tiene rango 8 en su corte apropiado y 64 en el contrario, por reducción exacta racional; (iii) en el comparador de contracción directa *con filtro de paridad*, la factorización disminuye el cómputo aritmético contado de **12.288** a **960** operaciones escalares, a costa de tablas de grupos y sin incluir búsqueda, signos, accesos y coste binario; (iv) el dato $`H(0)`$ en una deformación de grado a lo sumo cinco se recupera con seis datos de Hermite y ninguno de ellos es descartable dentro de ese sistema de medición para la familia polinómica completa.

**Alcance:** son pruebas sobre operaciones reales de las publicaciones, no reproducciones de las recursiones completas ni mejoras demostradas de sus cotas asintóticas.

## I. Referencia y transporte de momentos

Para cada combinación $`a`$ con posición entera $`w(a)`$, el polinomio truncado es

```math
J_a(t)=(1+t)^{w(a)}\pmod{t^3}
=1+w(a)t+\tbinom{w(a)}2t^2.
```

Si $`J=(N,S,B)`$, el conteo es $`N`$, la suma de posiciones es $`S`$ y la suma de sus cuadrados es $`Q=S+2B`$. Al sumarse o multiplicarse contribuciones, estas tres magnitudes se conservan sin enumerar todas las combinaciones. Los pesos se asignan a factores locales, de manera que $`w(a)=w_1(a_1)+w_2(a_2)`$ en los cortes que se comparan.

## II. Ruta Anthropic: identidad firmada y dos cortes

Para $`x,y,u,v\in\lbrace0,1\rbrace^3`$, la identidad usada por Anthropic es

```math
2[x=v][y=u]
=[x\oplus y\oplus u\oplus v=0]
\bigl(\sigma(x,y)\sigma(v,u)+\sigma(x,u)\sigma(v,y)\bigr),
```

donde $`\sigma`$ es una tabla de signos de los octoniones. Se construyó la tabla de manera determinista por duplicación de Cayley–Dickson y se comprobaron las **4.096** cuádruplas. Las dos piezas $`R`$ y $`C`$ se evaluaron por separado con pesos $`w=\operatorname{popcount}(x)+\operatorname{popcount}(y)+\operatorname{popcount}(u)+\operatorname{popcount}(v)`$.

| Medida | $`2[x=v][y=u]`$ | Pieza $`R`$ | Pieza $`C`$ |
|---|---:|---:|---:|
| Cantidad firmada $`N`$ | 128 | 64 | 64 |
| Suma de posiciones $`S`$ | 768 | 384 | 384 |
| Cuadrados $`Q`$ | 5.376 | 2.688 | 2.688 |

Las piezas tienen sumas firmadas; las 512 entradas no nulas de cada pieza incluyen **224 negativas** y 288 positivas. Su coincidencia final exige conservar los signos. La multiplicidad 2 del lado izquierdo explica $`N=128`$: hay 64 pares compatibles $`(x,y)`$, cada uno contado dos veces.

### Cortes y rango

| Pieza | Corte $`(x,y)\mid(u,v)`$ | Corte $`(x,u)\mid(y,v)`$ |
|---|---:|---:|
| $`R`$ | rango **8** | rango **64** |
| $`C`$ | rango **64** | rango **8** |

El verificador calcula los cuatro rangos por eliminación racional exacta sobre matrices de $`64\times64`$. El rango 8 también se explica constructivamente: para $`R`$ en su orientación favorable, la fila $`(x,y)`$ tiene firma $`s=x\oplus y`$ y signo $`\sigma(x,y)`$, y la columna $`(u,v)`$ aporta $`\sigma(v,u)`$ únicamente si $`u\oplus v=s`$. Esto reúne 64 estados de cada lado en ocho grupos con signos. Para $`C`$ se repite el argumento en el corte opuesto.

### Comparador aritmético explícito

El comparador directo omite por adelantado las cuádruplas que no satisfacen la paridad y evalúa 512 productos ponderados para cada pieza: 1.024 productos de triples en total. La factorización agrega 64 estados a ocho grupos de cada lado y calcula ocho productos finales por pieza.

| Operación escalar (enteros) | Directo con filtro de paridad | Cortes apropiados, factorizados |
|---|---:|---:|
| Sumas | 6.144 | 864 |
| Productos | 6.144 | 96 |
| **Total** | **12.288** | **960** |

Cada suma de triples cuesta tres sumas enteras y cada producto truncado cuesta seis productos y tres sumas enteras; no se aprovecha que algunos coeficientes sean cero. El ahorro local aritmético es un factor de **12,8** frente a este comparador específico. El conteo omite búsquedas y accesos a $`\sigma`$, cálculos XOR, cambios de signo, carga de pesos, administración de memoria y costo a nivel de bits. Además, la factorización y la ventaja de los dos cortes proceden de la identidad conocida; el ensayo no presenta ese factor como un descubrimiento nuevo del programa.

**Lectura ontológica sometida a prueba:** la referencia determina qué se mide; la clase por XOR identifica la relación que se conserva; el signo codifica una diferencia que no puede borrarse; el cierre se acredita por la igualdad exacta de tres momentos. El ahorro global exige integrar reconocimiento y recursión.

## III. Ruta OpenAI: datos de Hasse y límite de reducción

Se consideró la fórmula de cinco variables $`F=(x_1\lor x_2)\land(\neg x_3\lor x_4)`$, con $`x_5`$ libre. Como ensayo de la interfaz de Hermite se usó

```math
H_F(T,t)=\sum_{x\models F}(1+t)^{w(x)}\prod_{i=1}^5(1+Tx_i)\pmod{t^3}.
```

Tiene grado en $`T`$ a lo sumo 5 y $`H_F(0,t)`$ es el polinomio que codifica los tres momentos. Se calcularon **sin enumeración durante el procedimiento principal** los valores y primeras derivadas de Hasse en $`T=1,2,3`$, usando eliminación de variables sobre pares de coeficientes. La enumeración de 32 asignaciones solo auditó el resultado.

La matriz de Hermite tiene $`V_{(a,j),k}=\binom{k}{j}a^{k-j}`$. La fila del funcional que evalúa en cero respecto de los seis datos resulta

```math
\boxed{
H_F(0,t)=
-18H_F(1,t)-9D_TH_F(1,t)+9H_F(2,t)-18D_TH_F(2,t)
+10H_F(3,t)-3D_TH_F(3,t),
}
```

con $`D_T H(a,t)=[z]H(a+z,t)`$. Se obtuvo exactamente

```math
H_F(0,t)=18+51t+57t^2, \qquad (N,S,Q)=(18,51,165).
```

### Certificado de necesidad relativa de seis datos

En el espacio completo de polinomios sobre $`\mathbb Q`$ de grado $`\le5`$, la matriz $`V`$ es invertible. Los seis coeficientes de la fórmula de recuperación son no nulos. Si se suprime el dato número $`i`$, el polinomio cuya lista de observaciones es el vector unitario $`e_i`$ tiene todas las otras cinco observaciones iguales a cero pero valor no nulo en $`T=0`$ (igual a la correspondiente constante de recuperación). Por ello **cada uno de esos seis datos es necesario dentro de ese conjunto fijo de observaciones**, si se exige recuperación para *todos* los polinomios de grado a lo sumo cinco. No se afirma minimalidad entre todas las posibles clases de mediciones ni entre los polinomios producidos por OpenAI.

Como control adicional, una familia *hipotética distinta* $`A+BT^2+CT^4`$ permite reconstruir su término constante a partir de solo tres valores:

```math
H(0)=\tfrac32H(1)-\tfrac35H(2)+\tfrac1{10}H(3).
```

Esto demuestra que la reducción depende de relaciones estructurales explícitas. **No se ha probado que el polinomio auxiliar concreto de OpenAI pertenezca a esa familia.** Asimismo, el experimento no implementa sus sustituciones de bajo rango, su selección de parámetros ni la aritmética modular/precisión completa.

## IV. Conclusión verificable y próximo examen

- **Resuelto localmente:** identidad de signos, orientación óptima de las dos piezas, conservación de $`N,S,Q`$, recuperación Hermite y prueba de necesidad de seis datos en una familia general acotada.
- **Condicional:** agrupar y transportar momentos produce ahorro aritmético local frente a un comparador definido cuando las clases y signos se calculan por la estructura XOR.
- **Abierto:** demostrar que la misma economía atraviesa todos los niveles de recursión de Anthropic o las sustituciones, truncamientos, módulos y cotas de bits de OpenAI; también identificar una subfamilia *real* donde se eliminen datos de recuperación.

La novedad potencial no está en redescubrir la identidad octoniónica ni la interpolación. Está en certificar **qué diferencias respecto de una referencia sobreviven a las transformaciones completas y cuál es el costo neto de conservarlas**. El trabajo *Subexponential Weighted Counting and Exact Optimisation* ya publicó una extensión de OpenAI a pesos en álgebras conmutativas el 29 de octubre de 2026; esa prioridad debe citarse.

## Reproducción

```bash
python3 verificar_transformaciones.py
```

Genera `resultados.json`. Utiliza exclusivamente Python 3 estándar y aserciones estrictas. La evaluación exhaustiva de las 4.096 cuádruplas es una **auditoría** de una identidad local, no un procedimiento de SAT general. Los 32 estados booleanos también se enumeran únicamente para auditoría independiente.

## Fuentes primarias

- Anthropic, *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*, Hexagon, versión 1 del 27 de octubre de 2026; identidad de ocho cuadrados en §2.4, ec. (12); piezas $`R`$ y $`C`$ en §4, ecs. (30)–(31); lema 2. https://hexagonmath.org/2610.00577
- OpenAI, *The Exponential Time Hypothesis is False*, fuente TeX del manuscrito del 25 de octubre de 2026, interpolación de Hermite, https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex
- Deep Bhattacharjee, *Subexponential Weighted Counting and Exact Optimisation*, v1, 29 de octubre de 2026, https://hexagonmath.org/2610.00594v1

---

**Endless Monkey Project**  
*Relational Geometry Program*
