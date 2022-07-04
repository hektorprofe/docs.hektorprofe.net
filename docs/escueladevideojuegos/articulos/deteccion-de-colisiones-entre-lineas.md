Title: Colisiones entre Líneas | Escuela de Videojuegos | Hektor Profe
Date: 2015-11-04 13:04
Category: Teoría de videojuegos
Tags: colisiones, coordenadas, intersecciones, lineas, pendientes, repaso-teoria-tema-1, sistemas, teoría
Slug: deteccion-de-colisiones-entre-lineas
description: Teoría matemática sobre los sistemas de ecuaciones lineales para calcular colisiones.

# Colisiones entre Líneas

Las líneas en los videojuegos suelen representar los lados de una
estructura, el suelo o también el camino de un objeto en movimiento. Por
tanto si queremos saber si un objeto choca contra el suelo para que no
lo traspase (o contra otro objeto) tendremos que comprobar si la línea
que sigue su camino cruza la línea de suelo (o el camino de otro
objeto). En otras palabras, tendremos que programar una condición basada
en la intersección de dos líneas.

Por ahora ya sabemos como encontrar las ecuaciones de estas líneas, así
que podemos ponerlas juntas y formar un sistema de ecuaciones lineales
para resolverlo matemáticamente.

## Sistemas de ecuaciones lineales

Al resolver un sistema de dos ecuaciones lineales, lo que en realidad
estás buscando es la intersección de dos líneas, es decir, el conjunto
de soluciones con todos los puntos que satisfacen ambas ecuaciones. El
teorema nos indica tres soluciones para dos líneas en el mismo
plano.

**Una única solución cuando las dos líneas tienen distinta pendiente (se
cruzan):**

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-una-solucion-distinta-pendiente.png"/></div>

**Un número infinito de soluciones cuando las dos líneas tienen la misma
pendiente e intercepción-y (pasan por el mismo sitio):**

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-infinitas-soluciones.png"/></div>

**Ninguna solución cuando las líneas tienen la misma pendiente pero
diferente intercepción-y (son paralelas):**

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-ninguna-solucion.png"/></div>

Matemáticamente determinar las soluciones es tan sencillo como comparar las pendientes (m) de las dos ecuaciones lineales:

* Si m1 != m2, una solución (hay colisión):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-soluciones-infinitas.png"/></div>

Cuando sabemos que sólo hay una solución podemos calcular exactamente
el punto de intersección resolviendo los sistemas utilizando el método
de la sustitución para dos incógnitas (o cualquier otro método):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/solucion-sistema-ecuaciones-sustitucion.png"/></div>

* Si m1 == m2, buscar intercepción-y de las dos líneas, b1 y b2:
    
    * Si b1 != b2, cero soluciones (no hay colisión):

    <div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-ninguna-solucion-ejemplo.png"/></div>
        
    * Si b1 == b2, infinitas soluciones (hay colisiones):

    <div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-ecuacion-infinitas-soluciones-ejemplo.png"/></div>

<style>
@media (max-width: 1219.9px){
    .md-nav__item:last-child {
        display: inherit !important;
    }
}

@media (max-width: 667.9px){

    h2 {
        width: 100%;
    }

    .md-typeset h2{
        margin-top: 0;
    }

    .md-main__inner {
        padding-top:0.4em;
    }
}

@media (min-width: 1219.9px){
    .md-nav__link--active {
        padding-left:0 !important;
    }
}
</style>