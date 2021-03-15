Title: El eje de coordenadas | Escuela de Videojuegos | Hektor Profe
Date: 2015-10-20 01:24
Category: Artículos
Tags: 2d, 3D, coordenadas, eje, espacio, explicacion, figuras, plano, representación, vectores
Slug: el-eje-de-coordenadas
description: Uno de los más importantes conceptos, por no decir el más importante, dentro del desarrollo de videojuegos es el eje de coordenadas.

Uno de los más importantes conceptos, por no decir el más importante,
dentro del desarrollo de videojuegos es el eje de coordenadas. Es tan
importante debido a que nos permite recrear un plano o un espacio y
posicionar en su interior los diferentes elementos que forman el
videojuego.

Los ejes de coordenadas cartesianas son una parte fundamental de las
matemáticas y la física, ya que nos sirven para representar funciones y
también posiciones. En ellos, cada eje representa una dimensión, por lo
que si hablamos de videojuegos encontraremos dos ejes
básicos.

## Eje de coordenadas en el plano

Representado por dos ejes X e Y que indican las dimensiones ancho y
alto respectivamente. Se utiliza en juegos en dos
dimensiones.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-2d-vacio.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Eje de coordenadas en el plano*</small> 

## Eje de coordenadas en el espacio

Representado por tres ejes, X, Y y Z que indican las dimensiones ancho,
alto y profundidad respectivamente. Se utiliza en juegos en tres
dimensiones, aunque también sirve para juegos  en 2D cuando se utiliza
el eje Z para indicar qué elementos se encuentran por encima de los
otros en el plano, algo que normalmente se indica como una propiedad de
los objetos que determina el orden de renderizado de abajo hacia
arriba.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-3d-vacio.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Eje de coordenadas en el espacio*</small> 

## Origen de coordenadas

El término origen es muy utilizado cuando se habla del eje de
coordenadas. Corresponde al lugar donde se cortan los ejes y tiene el
valor cero. Es muy importante ya que gracias a él podemos tomar una
referencia inicial a partir de la cual posicionar elementos sobre el eje
de coordenadas, utilizando coordenadas, valga la
redundancia.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-2d-origen.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*La O roja es el origen del plano*</small> 

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-3d-origen.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*La O roja es el origen del espacio*</small> 

## Representación de elementos

Tomando un punto sobre el eje de coordenadas (que es la mínima unidad
que se puede representar), cada coordenada nos indica la distancia de
cada dimensión partiendo del origen donde se encuentra el punto. Por
ejemplo un punto A en el plano 2D estará formado por dos coordenadas A =
(X,Y):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-2d.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Punto en el plano*</small> 

Mientras que en el espacio 3D estará formado por tres A = (X,Y,Z):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/eje-3d.png" style="width:200px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Punto en el espacio*</small> 

Otro elemento que se puede representar sobre el eje de coordenadas es
un vector, que no es más que la distancia entre el origen y un punto,
con dirección al punto:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/vector-plano.png" style="width:450px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Vector en el plano*</small> 

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/vector3d.gif" style="width:300px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Vector en el espacio*</small> 

De ahí se entiende que al unir dos puntos con una recta tenemos una
línea en el eje. Si unimos varias líneas entre ellas podemos formar
polígonos, planos e incluso cuerpos 3D bien definidos en base a las
coordenadas de cada punto que las forman.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/poligono.png" style="width:250px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Polígono irregular en el plano*</small> 

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/cubo.png" style="width:250px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Cubo en el espacio*</small> 

Si vamos un poco más allá llegamos al modelado tridimensional en base a
polígonos, que posteriormente se suaviza para recrear objetos mucho más
realistas.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/modelado-3d.jpg" style="width:450px;" /></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Modelado poligonal en 3D y posterior suavizado*</small> 

## Conclusión

A partir de aquí todo es desarrollar la  idea y trasladarla a imágenes
y dibujos en el plano y modelos tridimensionales para el espacio.

Claro está que esto es una simple introducción para que veáis la importancia
del eje de coordenadas en el mundo de los videojuegos. Sólo os digo que
gracias a la geometría y el álgebra es posible hacer muchas cosas, como por ejemplo
rotar formas geométricas en el eje de coordenadas, detectar cuando una
línea se cruza con otra, etc.

Evidentemente estos conocimientos sólo los necesitaremos desarrollar si
queremos programar nuestro propio motor de renderizado (que dudo que sea
el caso), porque por suerte la mayoría de engines ya nos proporcionan
herramientas visuales o funciones para hacerlo de una forma mucho más
cómoda.

Si te interesa el tema, encontrarás mucha más información y ejemplos
sobre el eje de coordenadas [en la
wikipedia](https://es.wikipedia.org/wiki/Coordenadas_cartesianas).

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