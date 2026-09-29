# Reflexión, escala y almacenamiento de información
## Formalización v0.81

**Programa de Geometría Relacional**  
**Autor de publicación:** Le Matt Ansatz Di Ego  
**Estatus:** formalización matemática exploratoria. No implica validación física.

## 1. Marco normalizado 3–4–5

Sea un cierre normalizado con centro
\[
c=4
\]
y radio relacional
\[
r=1.
\]

Los límites son
\[
b_-=c-r=3,\qquad b_+=c+r=5.
\]

Definimos la reflexión
\[
S_c(x)=2c-x.
\]

Para \(c=4\):
\[
S_4(3)=5,\qquad S_4(5)=3,\qquad S_4(4)=4,
\]
y
\[
S_4^2=I.
\]

Por tanto, el 4 es el punto fijo y 3/5 son imágenes del mismo radio:
\[
|3-4|=|5-4|=1.
\]

La distinción no está en la magnitud sino en la orientación:
\[
x=4+\sigma,\qquad \sigma\in\{-1,+1\}.
\]

## 2. El bit de reflexión

Como hay dos orientaciones posibles,
\[
I_\sigma=\log_2 2=1\text{ bit}.
\]

El bit está en la orientación del mismo radio, no en el radio mismo.

La lectura “3 = apertura” y “5 = cierre” requiere una orientación generativa adicional. La involución sola sólo deriva la simetría \(3\leftrightarrow5\).

## 3. Cierre y cambio de escala

Sea una escala
\[
F_k=(c_k,r_k)
\]
y una coordenada normalizada
\[
\xi_k=\frac{x-c_k}{r_k}.
\]

Cuando una indefinición binaria se resuelve con
\[
\sigma_k\in\{-1,+1\},
\]
la cápsula cerrada puede tratarse como una nueva unidad en el nivel siguiente.

Representamos la información heredada mediante
\[
H_{k+1}=(H_k,\sigma_k).
\]

Después de \(n\) cierres independientes:
\[
H_n=(\sigma_1,\ldots,\sigma_n).
\]

Si los bits son independientes:
\[
|\mathcal H_n|=2^n.
\]

Cerrar no equivale a borrar información: significa convertir información abierta en estructura heredable.

## 4. Firma de diferencia y Mersenne

En una codificación binaria equivalente, si existe un único estado nulo
\[
(0,\ldots,0),
\]
el número de firmas no nulas es
\[
\boxed{M_n=2^n-1}.
\]

Así aparece la escalera
\[
1,3,7,15,31,\ldots
\]
como consecuencia del almacenamiento recursivo de bits, bajo las hipótesis de independencia y estado nulo único.

## 5. Puente candidato 4 → 16 → 15

Si se demuestra que el cierre elemental de orden cuatro produce cuatro discriminantes binarios independientes,
\[
n=4,
\]
entonces
\[
|\mathcal H_4|=2^4=16
\]
y las firmas no nulas son
\[
M_4=2^4-1=15.
\]

Aparece entonces
\[
1+15=16.
\]

Pero este puente sigue siendo condicional:
\[
J^4=I\not\Rightarrow 2^4
\]
sin demostrar que las cuatro imágenes del cierre aportan cuatro bits independientes.

## 6. Prototipo exacto del complemento: sector afín

Sea
\[
C\le V
\]
un subespacio sobre \(\mathbb F_2\), y sea
\[
r\notin C
\]
un residuo nuevo.

Entonces
\[
C'=\operatorname{span}(C,r)
\]
se descompone exactamente como
\[
\boxed{C'=C\;\dot\cup\;(r+C)}.
\]

Además
\[
C'/C\cong\mathbb F_2,
\]
por lo que la extensión añade exactamente un bit.

La nueva referencia nace del propio residuo:
\[
\boxed{\Gamma^*(C,r)=r+C}.
\]

La traslación
\[
\tau_r(x)=x+r
\]
satisface
\[
\tau_r^2=I
\]
y permuta
\[
C\leftrightarrow r+C.
\]

Ésta es una realización exacta de la idea: **la nueva referencia surge como el complemento/reflejo generado por la diferencia que no cabía**.

## 7. Consecuencia para P vs NP

En XOR-SAT o sectores afines, este mecanismo existe y se maneja por álgebra lineal.

Para 3-SAT general, el espacio de soluciones no es normalmente afín. El problema central pasa a ser:

\[
\boxed{
\text{¿existe un análogo no afín de }
C\;\dot\cup\;(r+C)
\text{ que sea exacto y polinómico?}
}
\]

Ésta es ahora la forma más precisa del operador de creación de referencia \(\Gamma^*\).

Si para toda 3-SAT existe una operación recursiva de este tipo con:
- representación polinómica,
- actualización polinómica,
- preservación exacta de SAT,
- una nueva referencia derivada del residuo,
- y fronteras globalmente polinómicas,

entonces habría una vía constructiva hacia \(P=NP\).

Si no puede extenderse fuera de sectores estructurados, esta ruta queda cerrada.

## 8. Síntesis

\[
\boxed{4\pm1\to3,5}
\]

formaliza un centro de cierre con dos imágenes del mismo radio.

El signo \(\pm\) constituye un bit relacional.

Al cerrarse una escala, ese bit puede quedar almacenado en la identidad de la nueva unidad.

Repitiendo el proceso:
\[
\text{un bit por cierre independiente}\Rightarrow 2^n\text{ firmas}.
\]

Excluyendo el estado nulo:
\[
2^n-1
\]
firmas de diferencia.

Esto proporciona un puente formal candidato entre:
- incertidumbre,
- reflexión,
- escala,
- Mersenne,
- y la antigua razón \(1:15\).

La pieza abierta es demostrar que el cierre de orden cuatro genera exactamente cuatro bits independientes y que el complemento afín tiene un análogo no afín útil para 3-SAT.
