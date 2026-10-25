# Rama Navier–Stokes — estado para revisión

## Estructura exacta ya disponible

Para:

\[
\omega=q\xi,
\]

\[
\boxed{
\frac{D_t\omega}{q}=a\xi+b,
\quad
a=D_t\log q,
\quad
b=D_t\xi\perp\xi.
}
\]

Con:

\[
\mathcal S=\frac{D_t^2\omega}{q},
\]

\[
\boxed{
P_\xi^\perp\frac{db}{dG}
=
\frac{\mathcal S_\perp}{a}-2b.
}
\]

La rama actual no identifica bajo giro con regularidad.

## Actualización MF-95

Se deriva:

\[
\boxed{
D_ta
=
\mathcal S_\parallel-a^2+|b|^2.
}
\]

Para:

\[
\beta=\frac{|b|}{a},
\]

\[
\boxed{
\frac{d\beta}{dG}
=
\Gamma
=
\frac{\widehat b\cdot\mathcal S_\perp}{a^2}
-
\beta
\left(
1+\beta^2+\frac{\mathcal S_\parallel}{a^2}
\right).
}
\]

Si \(\Gamma\ge\delta>0\) dentro de un canal \(\beta<\beta_\eta\), una trayectoria no puede permanecer allí durante crecimiento \(G\) arbitrariamente grande.

## Frontera real

El supremo euleriano puede migrar entre trayectorias y escalas.

Por tanto falta controlar:

\[
\boxed{
\text{migración/reentrada del residuo crítico}.
}
\]

La revisión debe decidir si el sector de estancamiento introducido en MF-95 reduce el problema o sólo lo renombra.


## Lectura relacional actual — revisión interna 5.9

**Actualización de alcance:** la dificultad pendiente es el **control euleriano global de migración y reentrada**; identidades lagrangianas locales no prueban regularidad.

Ver `../../70_reviews/R59_PROBLEMAS_EN_LENGUAJE_RELACIONAL_ACTUAL.md` para el contrato, NO-GO y falsadores.
