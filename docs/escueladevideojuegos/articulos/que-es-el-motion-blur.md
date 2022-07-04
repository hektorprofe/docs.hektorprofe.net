Title: ¿Qué es el Motion blur? | Escuela de Videojuegos | Hektor Profe
Date: 2015-10-27 11:44
Category: Artículos
Tags: motion blur, movimiento, rastro, realidad, recrear, videojuegos
Slug: que-es-el-motion-blur
description: En esta entrada te explico acerca de lo que es el Motion Blur.

Sin duda el mundo de los videojuegos es el mundo de los gráficos en
movimiento, pero el movimiento en un videojuego no es real sino que es una recreación o
ilusión que nuestro cerebro interpreta. Al ser una simulación, está
sujeta a limitaciones que los desarrolladores tienen que perfeccionar
para simular al máximo la realidad.

## El movimiento en la realidad

En la vida real, cuando cualquier cosa se mueve de un lugar a otro, está
claro que recorre la distancia entre su lugar inicial y su lugar final,
independientemente de su velocidad. Sin embargo cuando una cámara toma
una fotografía de una situación en la que hay elementos en movimiento se
nos presenta como un efecto extraño en el que parece que estos elementos
están en varios sitios a la vez. Este efecto se conoce como **Motion blur**
o rastro de movimiento.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/motion-blur-rastro-movimiento.jpg" style="width:500px;" /></div>

Este rastro de movimiento es la prueba de que por muy rápido que se
mueva algo, en la realidad tiene que recorrer todo el trayecto, si no
sucediera entonces no sería movimiento, sino que sería
teletransportación, algo que "todavía" no es posible.

¿Pero qué sucede en los videojuegos?

## El movimiento en los videojuegos

Si habéis creado alguna vez un videojuego, entonces sabéis que para
mover un elemento lo que hacemos es modificar sus posiciones en el eje
de coordenadas en cada fotograma:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/incremento1.png" style="width:600px;" /></div>

Por tanto, cuanta 
más incrementamos la posición entre dos fotogramas, más distancia
parecerá que se mueve:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/incremento2.png" style="width:600px;" /></div>

Sin embargo esto
tiene un pequeño inconveniente... y es que cuando movemos un elemento en
un videojuego éste no recorre todo el trayecto entre las posiciones de
cada fotograma, sino que podríamos decir que va saltando, o
teletransportándose, y por tanto no existe rastro alguno de movimiento
más allá que el de las posiciones múltiples del incremento de posición.

Cuando este movimiento es en base a pequeñas distancias no hay problema
porque simula bien la realidad (menos velocidad, más fotogramas), pero
si movemos un elemento mucha distancia en cada fotograma entonces sí que
notaremos los saltos por la pantalla (más velocidad, menos fotogramas),
y no debemos olvidar que para una recreación fluida se aconsejan como
mínimo 24 fotogramas por segundo.

## Motion blur en los videojuegos

De todas formas, como ya dije al principio, que no exista este fenómeno
como algo natural no significa que no se pueda recrear en los
videojuegos para suavizar el movimiento de sus elementos. De hecho es
todo lo contrario y se suele utilizar bastante.

Recrear el rastro de movimiento en los videojuegos se puede implementar
de muchas formas pero una que es sencilla es "clonar" varias veces el
gráfico en movimiento en dirección opuesta al que se mueve y restarle
opacidad hasta que desaparece.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/recrear-motion-blur.png" style="width:200px;" /></div>

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