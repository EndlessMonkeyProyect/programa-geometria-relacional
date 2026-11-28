# T.1.5 — Ley de recuperación direccional y auditoría Arb

28 de noviembre de 2026 · Complemento de T.1 v1.4 · Endless Monkey Project / Relational Geometry Program

## 1. Identidad y cota

En las coordenadas funcionales de §8 de v1.4, sea $T=A^*A$, $0\le T<I$, y $z$ la dirección normalizada del resto. Defínanse $m_j=\langle z,T^jz\rangle$, $R_{p,k}=\sum_{j=0}^k m_j$, $\mu_p=m_0$ y $\eta_p=\sum_{j\ge0}m_j$. La cota testigo funcional es $\gamma_p^G=m_0^2/(m_0-m_1)$ cuando $m_0>0$. En el caso $z=0$, todas las recuperaciones son cero y se toma la cota igual a cero.

**Proposición J1 (cota finita a partir de dos parámetros).** Para $m_0>0$,

$$\alpha_p=\frac{m_1}{m_0}=1-\frac{\mu_p}{\gamma_p^G}\in[0,1),\qquad J_{p,k}:=\mu_p\sum_{j=0}^k\alpha_p^j\le R_{p,k}\le\eta_p.$$

Demostración: la medida espectral de $T$ en la dirección $z$, dividida por $\|z\|^2$, es una probabilidad sobre $[0,1)$. Su momento de orden $j$ es $m_j/m_0$ y su media es $\alpha_p$. La convexidad de $x^j$ para enteros $j\ge1$ y Jensen dan $m_j\ge m_0\alpha_p^j$; para $j=0$ hay igualdad. La suma establece el resultado. Equivalentemente $J_{p,k}=\gamma_p^G(1-\alpha_p^{k+1})$. El caso $\alpha_p=0$ tiene $J_{p,k}=\mu_p$ para todo $k$. La cota utiliza dos escalares y no requiere diagonalizar $T$; el costo de obtenerlos sigue dependiendo del Gram.

## 2. Lectura relacional y condición suficiente

El reconocimiento inicial $\mu_p$ y el solapamiento medio $\alpha_p$ determinan una contribución mínima para cada reflexión sucesiva. La relación corresponde al mecanismo de recierre del laboratorio de espejos; $T$ es un operador de solapamiento, no una reflexión óptica física. Para la cadena natural de primos, la divergencia de $\sum_p J_{p,4}$ implica la divergencia de $\sum_p\eta_p$ y, por T.1 v1.4, RH. Es suficiente probar $pJ_{p,4}\ge c>0$ eventualmente. El umbral 1 es una hipótesis experimental particular; no es necesario. La divergencia de la serie de cotas inferiores no se ha establecido. Tampoco se deduce de la convergencia de los defectos locales del complemento A.

## 3. Resultados de la auditoría

El material Arb recibido reporta ocho etapas (primos 2 a 19), 192 bits de precisión de trabajo, y tres expresiones de la recuperación. En p=19 el resto tras incorporar el primo es aproximadamente 0.0109544729875962, con radio reportado del orden de 4e-46; el condicionamiento estimado de G' es 1.63e8. La etapa final tiene 256 referencias funcionales. Se verificaron los tres hashes originales. Los extremos espectrales calculados con mpmath no se presentan como certificados Arb.

Relectura de centros del JSON original con Decimal (no certificación intervalar de J1):

| p | p gamma (firmas) | p J4 (funcional) |
|---:|---:|---:|
|2|1.324259|1.009130|
|3|2.067533|1.636008|
|5|2.328313|1.505677|
|7|1.094674|1.353835|
|11|1.185931|1.468566|
|13|1.222973|1.092101|
|17|3.924690|3.683862|
|19|2.405177|1.844385|

Las ocho cotas evaluadas en los centros superan 1. No se confunde gamma de firmas con gamma funcional. El contraejemplo intervalar del complemento A ($S=\{11\}$, $p=13$) descarta el umbral universal para configuraciones arbitrarias incluso a profundidad infinita; J1 respeta esa obstrucción. Las etapas de la cadena natural siguen siendo evidencia finita.

## 4. Reproducción y límites

Desde esta carpeta: `python verificar_jensen_centros.py`. Se adjunta la salida reproducida. Para obtener el certificado de J1 con bolas vivas: instalar las dependencias de `../04_auditoria_Arb/requirements.txt` y ejecutar `python verificar_jensen_arb.py 19`. El nuevo script conserva las envolventes decimales de Arb y exige desigualdades estrictas; no reutiliza como intervalos los centros del archivo original. Los extremos espectrales, beta y condicionamientos requieren un certificado espectral separado. La ejecución Arb del nuevo script queda pendiente por falta de python-flint en el entorno de ensamblaje; no se adjunta una salida ficticia. Se solicita al administrador ejecutarlo y conservar el JSON de certificación y versiones antes de fusionar.

## 5. Correspondencias y estatuto

J1 es una consecuencia de Jensen y de la representación espectral de T.1 v1.4; se propone como una formulación económica de la recuperación, sin reclamo de prioridad. Los lemas B1–B4 de transferencia global y A1–A5 de herencia local se conservan como complementos separados. La transferencia analítica usa un insumo externo; la identificación directa de operadores y el cierre autónomo siguen abiertos. La auditoría Arb no certifica los lemas para infinitas etapas ni compila Lean.
