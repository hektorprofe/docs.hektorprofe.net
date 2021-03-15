Title: Círculos y Esferas (Ecuaciones) | Escuela de Videojuegos | Hektor Profe
Date: 2015-11-09 11:36
Category: Teoría de videojuegos
Tags: centro, circulo, coordenadas, ecuacion, esfera, geometria, radio, repaso-teoria-tema-2, representación, teoría
Slug: circulos-y-esferas-teoria
description: Ecucaciones del círculo y la esfera.

# Círculos y Esferas (Ecuaciones)

Otro de esos conceptos importantes en el mundo de los videojuegos es la
ecuación de un círculo. Por ejemplo se utiliza cuando quieres mover un
objeto formando un camino circular o también para crear una área de
colisión circular alrededor de otro objeto.

## Ecuación del círculo

Debes recordar que en un plano, como la pantalla, un círculo es una
serie de puntos a una determinada distancia, el radio, de un punto fijo
llamado el centro. Sólo con estos dos elementos, el centro y el radio,
es posible determinar la ecuación de un círculo, que tiene mucho que ver
con el teorema de Pitágoras.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/ecuacion-circulo1.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Ecuación de un círculo*</small> 

En la siguiente figura podemos observar un círculo con centro en(1,2) y un radio de 2:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/circulo-en-el-plano.png"/></div>

¿Reconoces al teorema de Pitágoras? Quizá es más fácil si tomamos un círculo centrado en el origen (0,0):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/circulo-en-el-origen.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Ecuación de un círculo en el origen*</small> 

Ya hemos visto la ecuación del círculo, pero ¿qué pasa si lo trasladamos al espacio tridimensional?

## Ecuación de la esfera

Una esfera es el resultado de un círculo en el espacio girando alrededor
de su punto central. Las esferas se utilizan para representar bolas,
pero también pueden ser utilizadas como límite geométrico de objetos
complejos tales como automóviles o naves espaciales. A menudo en el el
desarrollo 3D se utilizan esferas delimitadoras para simplificar la
detección de colisiones entre dos objetos que no requieren colisión
precisa. Al igual que un círculo, la esfera está definida por un centro
y un radio. La única diferencia es que el punto central tiene tres
coordenadas en lugar de dos:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/ecuacion-esfera.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Ecuación de una esfera*</small> 

De la misma forma que antes cuando el centro está en el origen la
ecuación se simplifica:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/ecuacion-esfera-origen.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Ecuación de una esfera en el origen*</small> 

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