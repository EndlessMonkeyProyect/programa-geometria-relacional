# De la herencia de potencias a la discrepancia de primos nuevos

**Nota de continuidad y verificación finita · 22 de noviembre de 2026**  
**Correspondencia:** RA–01 / S–RA–01 (cierre por proyecciones), HC–02 (herencia de potencias primas), HC–03 (diferencias mínimas y ventanas diádicas).  
**Estado:** identidad y desigualdad de separación demostradas con las cotas de HC–02; evaluación finita reproducible ampliada hasta \(2^{22}-1\); control uniforme de los primos nuevos abierto.  
**Firma:** Endless Monkey Project / Relational Geometry Program.

## 1. Hallazgo concreto

La discrepancia de Chebyshev en cada ventana diádica se descompone **exactamente** en dos contribuciones: una de los primos que entran como nuevos generadores y otra de las potencias de primos ya existentes. La segunda está acotada incondicionalmente por una constante explícita veces \(\sqrt{2^j}\). Por consiguiente, la condición de bloques de HC–03 tiene la misma dificultad matemática si se formula únicamente para los primos nuevos. La descomposición aísla el obstáculo, pero no prueba la estimación crítica.

Esta nota verifica la descomposición y sus amplitudes en ventanas desde \(2\) hasta \(2^{22}-1=4.194.303\), más allá del límite de dos millones registrado en el informe HC–03 consultado. El cálculo ampliado **no** repite ni sustituye el laboratorio funcional S–RA–01.

## 2. Definiciones y proposición

Sean \(L=2^j\), \(j\ge1\), y \(L\le m<2L\). Como en HC–03, \(\Lambda(n)=\log p\) si \(n=p^k\) para algún primo \(p\), y cero en otro caso. Defínanse:

\[
\begin{aligned}
C_j(m)&=\sum_{n=L}^{m}\Lambda(n)-(m-L+1),\\
P_j(m)&=\sum_{L\le p\le m}\log p-(m-L+1),\\
H_j(m)&=\sum_{\substack{L\le p^k\le m\\k\ge2}}\log p.
\end{aligned}
\]

El símbolo \(P_j\) en esta nota es una **discrepancia escalar de primos** y no el operador de proyección ortogonal denominado \(P_j\) en RA–01. Puede escribirse \(D_j^{\mathrm{pr}}\) para evitar esa colisión al fusionar documentos.

**Proposición (separación uniforme de la herencia).** Para todos los enteros \(j\ge1\) y \(L\le m<2L\):

\[
C_j(m)=P_j(m)+H_j(m),\qquad 0\le H_j(m)\le U(2L),
\]

con \(U(x)=\psi(x)-\vartheta(x)=\sum_{k\ge2}\vartheta(x^{1/k})\). Usando la cota probada en HC–02 para \(x\ge4\),

\[
U(x)\le C_0\sqrt{x},\qquad C_0=4\log2+24/e<11.602.
\]

Si \(B_j=\max_{L\le m<2L}|C_j(m)|\) y \(B_j^{\mathrm{pr}}=\max_{L\le m<2L}|P_j(m)|\), se obtiene:

\[
\boxed{|B_j-B_j^{\mathrm{pr}}|\le U(2L)\le C_0\sqrt{2L}.}
\tag{*}
\]

**Prueba.** La identidad \(\psi=\vartheta+U\) separa exactamente los eventos de exponente \(1\) y los de exponente \(k\ge2\). La función \(H_j\) es suma no negativa de eventos heredados dentro de la ventana y por tanto no excede \(U(2L)\). La desigualdad \(|\|f\|_\infty-\|g\|_\infty|\le\|f-g\|_\infty\) aplicada a \(f=C_j\), \(g=P_j\) da (*). La cota final es HC–02. □

**Consecuencia.** La condición de HC–03

\[
B_j=O\bigl(2^{j/2}(j+1)^2\bigr)
\]

se cumple si y solo si \(B_j^{\mathrm{pr}}\) tiene ese mismo orden. Por el criterio clásico citado en HC–03, ambas son formulaciones equivalentes a RH. **La dificultad se concentra en la fluctuación ponderada de los primos ordinarios.** La identidad (*) por sí misma no aporta una nueva cota crítica para esa fluctuación.

## 3. Ensayo computacional ampliado

Método: criba entera para localizar primos, enumeración separada de todas las potencias primas con exponente \(k\ge2\), sumas acumuladas con `numpy` para evaluar los máximos dentro de cada intervalo. Un segundo programa independiente calcula doce puntos por sumación `math.fsum` y repite la identidad de separación con el algoritmo de criba de la biblioteca estándar. El ensayo abarca **4.194.303 enteros positivos**, **295.947 primos** menores que \(2^{22}\) y **399 potencias primas heredadas** menores que ese límite (contadas una vez como eventos).

| Octava \(j\) | Rango de enteros | \(B_j\) completo | \(B_j^{\mathrm{pr}}\) primos nuevos | Aporte total heredado en la octava |
|---:|---|---:|---:|---:|
| 10 | 1.024–2.047 | 30,674 | 38,668 | 14,177 |
| 15 | 32.768–65.535 | 204,267 | 139,742 | 70,050 |
| 20 | 1.048.576–2.097.151 | 875,625 | 904,108 | 441,043 |
| 21 | 2.097.152–4.194.303 | 1.230,454 | 1.718,476 | 637,259 |

Los valores máximos se toman **sobre todas las posiciones** del intervalo, no únicamente en su extremo derecho. En la octava 15, las potencias heredadas pueden reforzar la amplitud de la discrepancia; en la 21, la reducen. Un aporte siempre positivo respecto de la masa aritmética no tiene un efecto uniforme sobre la **magnitud absoluta** del desfase, porque la discrepancia de primos puede tener cualquiera de los dos signos.

En el último intervalo:

\[
\frac{B_{21}}{2^{21/2}(22)^2}\approx0.001756,
\quad
\frac{B_{21}^{\mathrm{pr}}}{2^{21/2}(22)^2}\approx0.002452.
\]

Las dos cifras son observaciones de un intervalo finito. No certifican una constante de acotación aplicable a todos los exponentes \(j\). El máximo error numérico observado al comprobar \(C_j=P_j+H_j\) mediante los acumulados en doble precisión es menor que \(9\cdot10^{-10}\), y los controles por `math.fsum` corroboran las posiciones seleccionadas. Tampoco constituyen aritmética por intervalos.

## 4. Enlace con RA–01 y la obligación restante

RA–01 trabaja con distancias cuadráticas \(Q_j=\|\chi-\Pi_j\chi\|_2^2\) de proyecciones funcionales (aquí \(\Pi_j\) para distinguirlas de la discrepancia escalar anterior). La identidad \(Q_j=Q_{j+1}+\Delta_j\) es exacta. RA–01 demuestra que una suma divergente de **ganancias relativas certificadas** es suficiente para llevar \(Q_j\) a cero. S–RA–01 midió ganancias de una semilla de Möbius hasta 2.048. Ese laboratorio y la condición \(B_j=O(2^{j/2}(j+1)^2)\) de HC–03 son **dos rutas hacia condiciones ya conocidas como equivalentes a RH**, pero no existe en los documentos examinados una desigualdad que transfiera automáticamente la información cuantitativa entre los dos observables.

En particular, una contribución que se hereda exactamente en \(U\) no impone una compensación de signo de los nuevos primos. La corrección aritmética \(<1/8\) de HC–03 pertenece a la fórmula de reconstrucción con diferencias segundas: **es una cota para el defecto de reconstrucción**, no para \(B_j\), ni una cuantificación física de una incertidumbre irreductible.

**Obligación de prueba precisa:** demostrar, sin suponer RH y de forma uniforme en \(j\), una estimación para las sumas parciales centradas

\[
\max_{2^j\le m<2^{j+1}}
\left|\sum_{2^j\le p\le m}\log p-(m-2^j+1)\right|
\le K\,2^{j/2}(j+1)^2.
\]

Alternativamente, demostrar una condición suficiente de RA–01 para la familia aritmética concreta con una semilla explicitada y ganancias acumuladas divergentes. El punto común es establecer una **restricción cuantitativa sobre las aportaciones nuevas**, que no se siga de la identidad de herencia por sí sola.

## 5. Procedencia y reproducción

- **HC–02**, `INFORME_LAB_HC02.md`, 21 de noviembre de 2026: cota de \(U(x)\), separación \(\psi=\vartheta+U\), identidad de transferencia.
- **HC–03**, `INFORME_HC03.md`, 21 de noviembre de 2026: diferencia mínima aritmética, reconstrucción y condición por bloques (HC03.13).
- **RA–01**, `NOTA_AUDITORIA_RA01_v5.md`, 21 de noviembre de 2026: equivalencia para ganancias óptimas y suficiencia para semillas prefijadas.
- **S–RA–01**, `NOTAS_PUBLICACION_3_5.md`, 21 de noviembre de 2026: informe de mediciones y alcance finito.

Se incluyen `verificar_bloques_hc03.py` (requiere Python 3 y numpy), `contraste_fsum.py` (biblioteca estándar), `bloques_hc03_2_22.csv`, `control.json` y `contraste_fsum.json`. Ejecutar los dos scripts desde cualquier carpeta; cada uno escribe resultados junto a su propio archivo.

**Estado final:** separación y desigualdad (*) demostradas; cálculo ampliado verificado; estimación para todas las escalas abierta. No corresponde presentar esta nota como prueba de RH.
