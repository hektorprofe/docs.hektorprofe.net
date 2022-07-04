Title: Distancia entre dos puntos | Escuela de Videojuegos | Hektor Profe
Date: 2015-11-05 15:19
Category: Teoría de videojuegos
Tags: coordenadas, distancia, geometria, lineas, pendientes, pitagoras, punto medio, puntos, repaso-teoria-tema-2, teoría
Slug: distancia-entre-dos-puntos-teoria
description: Teoría matemática para calcular la distancia entre dos puntos y el punto intermedio en 2D y 3D.

# Distancia entre dos puntos (2D y 3D)

Cuando programamos videojuegos una de las cosas que normalmente
necesitamos saber es la distancia entre dos puntos de la pantalla.
Podrían ser dos objetos que van a chocar o la IA (Inteligencia
Artificial) de un enemigo que a cierta distancia de nuestro personaje
nos atacará.

No importa la situación, lo importante es ser capaces de calcular esta
distancia entre dos puntos, y la forma más simple de hacerlo es
utilizando el Teorema de Pitágoras.

## Teorema de Pitágoras

Este teorema nos dice que para cualquier triángulo rectángulo (con un
ángulo de 90º) la suma de sus catetos al cuadrado es igual a la
hipotenusa al cuadrado:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/pitagoras.png"/></div>

Por consiguiente a la inversa se puede deducir que si… a,b y c son las
longitudes de los tres lados de un triángulo y a2 + b2 = c2  entonces el
triángulo es rectángulo con una hipotenusa de longitud
c.

Si aplicamos este conocimiento a una pendiente entre dos puntos P1 y P2
nos daremos cuenta que la propia pendiente es la hipotenusa de un
triángulo rectángulo, siendo el tercer vértice un punto T con las
coordenadas (x2,y1):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/pitagoras-coordenadas.png"/></div>

Traduciendo la figura anterior al teorema de Pitágoras tendríamos
que:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/deduccion-pitagoras.png"/></div>

## Distancia entre dos puntos 2D 

De esta forma podríamos calcular la distancia entre dos puntos como si
fuera la hipotenusa de un triángulo rectángulo, lo que nos da la fórmula
de la distancia en 2D:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/formula-distancia-dos-puntos.png"/></div>

Por ejemplo, si queremos determinar la distancia entre dos objetos en
el plano centrados en las coordenadas (25,80) y (50,45) aplicaremos la
fórmula así:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/ejemplo-ejercicio-pitgaoras-plano.png"/></div>

## Punto intermedio 2D

En nuestros videojuegos, a veces nos vemos en la necesidad de calcular
el punto intermedio entre dos objetos. Para ello podemos utilizar la
siguiente fórmula:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/formula-punto-intermedio.png"/></div>

Por ejemplo para determinar el punto intermedio entre dos objetos
centrados en las coordenadas (40,80) y (50,50) lo calcularemos
así:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/punto-intermedio-ejemplo.png"/></div>

## Distancia entre dos puntos 3D 

Cuando hablamos de tres dimensiones las fórmulas no varían mucho, sólo
hay que tener en cuenta el componente z. La fórmula para la distancia
sería:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/formula-distancia-dos-puntos-3D.png"/></div>

## Punto intermedio 3D 

Mientras que para el punto medio quedaría:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/formula-punto-intermedio-3D.png"/></div>

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