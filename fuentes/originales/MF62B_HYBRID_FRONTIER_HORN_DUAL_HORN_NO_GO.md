# MF-62B — Frontera híbrida: no-go de residuo cero y coordinación Horn/dual-Horn

**Versión:** v0.70-research

## 1. Falsador de la frontera híbrida

MF-61B sugirió absorber sectores tratables y dejar sólo un residuo general. MF-62B pregunta si una instancia difícil puede tener residuo cero.

La respuesta es sí.

## 2. Toda cláusula exacta de tres literales es Horn o dual-Horn

Sea \(p\) el número de literales positivos de una cláusula de tres literales.

\[
p\in\{0,1,2,3\}.
\]

Si \(p\le1\), la cláusula es Horn. Si \(p\ge2\), contiene a lo sumo un literal negativo y es dual-Horn.

Por tanto cualquier E3-CNF se particiona exactamente:

\[
\boxed{F=H\land D}
\]

con \(H\) Horn y \(D\) dual-Horn.

No queda residuo general:

\[
\boxed{K_{\rm res}=0.}
\]

## 3. Ambos sectores son individualmente satisfacibles

Cada cláusula Horn de ancho tres tiene al menos dos literales negativos, así que:

\[
\boxed{H(0^n)=1.}
\]

Cada cláusula dual-Horn tiene al menos dos literales positivos, así que:

\[
\boxed{D(1^n)=1.}
\]

Luego ambos sectores tienen siempre un testigo trivial.

## 4. Teorema MF-62B-A — contradicción puramente intersectorial

Si \(F=H\land D\) es UNSAT, la contradicción no está en \(H\) ni en \(D\) por separado.

Está únicamente en:

\[
\boxed{
\mathrm{Models}(H)\cap \mathrm{Models}(D)=\varnothing.
}
\]

Por tanto:

\[
\boxed{
\text{existencia local}\not\Rightarrow\text{coexistencia global}.
}
\]

## 5. Teorema MF-62B-B — barrera de compatibilidad

Suponga un procedimiento polinómico universal que, dados un Horn-CNF \(H\) y un dual-Horn-CNF \(D\), decida si:

\[
H\land D
\]

es satisfacible.

Como toda E3-CNF se separa linealmente en \(H\) y \(D\), dicho procedimiento decidiría E3-SAT en tiempo polinómico.

Por tanto:

\[
\boxed{
\text{compatibilidad exacta Horn+dual-Horn en P}
\Rightarrow P=NP.
}
\]

Esto no prueba \(P\neq NP\). Identifica dónde puede residir toda la dificultad.

## 6. No-go principal

La hipótesis:

\[
\text{“todo lo difícil quedará en el residuo no tratable”}
\]

es falsa en general.

Aquí:

\[
\boxed{K_{\rm res}=0}
\]

pero la coordinación global sigue conteniendo E3-SAT.

Así:

\[
\boxed{
\text{residuo cero}\not\Rightarrow\text{tractabilidad}.
}
\]

La dificultad puede vivir en el acoplamiento entre dos módulos individualmente tratables.

## 7. Nueva cantidad necesaria

El perfil híbrido debe incluir un costo de acoplamiento:

\[
\boxed{
C_{\rm coup}
=
\text{costo de acreditar compatibilidad entre módulos}.
}
\]

Ya no basta medir:

\[
(L_1,L_2,L_{\rm res}).
\]

Necesitamos:

\[
\boxed{
\mathfrak H(F)=
(L_1,L_2,L_{\rm res},C_{\rm coup},T_{\rm empty}).
}
\]

## 8. Lectura relacional

El estado decisivo no pertenece a \(H\) o a \(D\) por separado.

Pertenece a:

\[
\boxed{H:D}.
\]

Computacionalmente:

\[
\boxed{
B_H\cap B_D\neq\varnothing?
}
\]

Ésta es exactamente la coordinación de fronteras de MF-61B.

## 9. Control computacional

Se generaron 640 E3-CNF aleatorias con \(n=5,\ldots,12\).

Se verificó:

- partición exacta Horn/dual-Horn;
- \(0^n\) como testigo Horn;
- \(1^n\) como testigo dual-Horn;
- equivalencia \(F=H\land D\).

Fallos: 0 en todos los controles.

De las fórmulas muestreadas, 143 fueron UNSAT y las 143 tenían ambos sectores individualmente SAT.

Esto ilustra el teorema; no es evidencia sobre \(P\) vs \(NP\).

## 10. Resultado conceptual

La forma correcta ya no es:

\[
\text{fácil}+\text{difícil}.
\]

Puede ser:

\[
\boxed{
\text{fácil}+\text{fácil}+\text{coordinación difícil}.
}
\]

## 11. Próximo paso

MF-63B debe tratar la compatibilidad como un objeto de primer nivel:

\[
\boxed{
K_H,\ K_D,\ K_{HD}
}
\]

donde \(K_{HD}\) conserve sólo las dependencias necesarias entre ambos cierres.

El falsador será:

- tamaño de \(K_{HD}\);
- costo de actualizarlo;
- costo de acreditar vacío;
- posible equivalencia implícita con SAT/UNSAT.

La cuestión pasa a ser:

\[
\boxed{
\text{¿puede comprimirse económicamente la relación de compatibilidad misma?}
}
\]
