Title: 42 formas de mejorar tus videojuegos 2D | Escuela de Videojuegos | Hektor Profe
Date: 2015-09-24 14:28
Category: Artículos
Tags: apuntes, consejos, game maker, juego, jugabilidad, mejorar
Slug: mejorar-la-jugabilidad-en-videojuegos-2d
description: Recopilación de 42 consejos para crear mejores videojuegos independientes.

# 42 formas de mejorar tus videojuegos 2D

Tenía pendiente escribir esta entrada y dejar constancia
de una recopilación de puntos que hice a partir de un par de vídeos de
youtube de esos que salen uno o varios desarrolladores "indies" y dan
una clase magistral compartiendo sus conocimientos.

## Juice it or lose it

El primer vídeo sobre el que he apuntado las ideas es **Juice it or lose
it - a talk by Martin Jonasson & Petri Purhoy** ya lo
retwitee hace un año. Es un ejemplo de como añadiendo algunas mejoras un
juego como breakout (por cierto si buscáis en google images "atari
breakout" veréis qué sale) se puede conseguir algo mucho más divertido. A modo
de recordatorio me apunté los siguientes puntos para mejorar un juego
arcade:

<div class='embed-container' style="margin-top:35px;margin-bottom:60px;"><iframe src='https://www.youtube.com/embed/Fy0aCDmgnxg?showinfo=0' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

1.  Utilizar paletas de colores agradables a la vista.
2.  Utilizar funciones easing/tweening para añadir dinamismo a las
    animaciones.
3.   Utilizar retardos aleatorios en el tweening sobre una serie de
    elementos en conjunto para crear efectos interesantes.
-   Escalado de elementos respecto a la posición de otros para crear
    efectos de suavizado, por ejemplo en un Pong al mover el jugador.
-   Escalado de elementos en colisiones, por ejemplo al rebotar la bola.
-   Rotación de elementos en colisiones respecto al lado de la colisión
    para añadir aún más dinamismo.
-   Estiramiento de elementos durante y/o después colisiones, por
    ejemplo la bota se estira elásticamente unos segundos al colisionar
    contra un elemento.
-   Añadir blends y brillos en las colisiones por unos instantes, es
    importante que el jugador reciba esta información.
-   Utilizar SFX y música adictiva.
-   Utilizar partículas en las colisiones, por ejemplo para generar
    rastros o levantamientos de polvo.
-   Utilizar efectos y tweens al destruir elementos: desaparecer, mover
    hacia arriba, hacia abajo…
-   Dejar rastros temporales de movimiento, por ejemplo la estela de una
    bola.
-   Utilizar sacudidas de pantalla durante las colisiones.
-   Utilizar efectos de brillo sobre el fondo en momentos determinados
    para generar sorpresa o cambios de conducta, por ejemplo cuando cae
    un rayo todo se ilumina por unos instantes y eso capta la atención.

## The art of screenshake

El segundo vídeo **Jan Willem Nijman - Vlambeer - "The art of
screenshake"** lo descubrí
mientras buscaba información sobre como mejorar la presentación de un
juego de plataformas. No tiene absolutamente ningún desperdicio para los
que empezamos con el desarrollo de videojuegos y la mejora del juego que
nos presenta antes y después es impresionante:

<div class='embed-container' style="margin-top:35px;margin-bottom:60px;"><iframe src='https://www.youtube.com/embed/AJdEqssNZ-U?showinfo=0' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

15.   Añadir animaciones básicas y SFX.
16.   Añadir más disparos, por qué limitar los disparos sólo al apretar
    pudiendo disparar ráfagas.
17.   Añadir muchos enemigos.
-   Disparos y ataques más grandes y visibles que llamen la atención.
-   Muzzle flash: animación de disparo (redonda blanca) al disparar.
-   Aumentar la velocidad de los disparos.
-   Disminuir la precisión y hacer que los disparos tomen ligeros
    ángulos diferentes para que no sean totalmente rectos y den una
    impresión de realidad.
-   Efectos de impacto cuando un disparo choca contra una pared o el
    suelo y hay una animación de destrucción.
-   Animación de impacto en el enemigo añadiendo un blend temporal al
    enemigo, éso nos da información de que está ocurriendo un impacto.
-   Retroceso de impacto en el enemigo añadiendo un movimiento ligero
    hacia atrás al ser impactado.
-   Permanencia de enemigos derrotados, tirados en el suelo xD, incluso
    en diferentes zonas al volver atrás.
-   Utilizar un objeto cámara específico para manejar escenas.
-   Suavizado de cámara utilizando linear interpolation, con
    [lerp](http://docs.yoyogames.com/source/dadiospice/002_reference/maths/real%20valued%20functions/lerp.html) es
    posible predecir dónde se movería una instancia en un momento
    determinado del futuro. Al utilizarlo sobre una cámara podemos crear
    un efecto de suavizado, [ver este
    hilo](http://gmc.yoyogames.com/index.php?showtopic=470656&p=3827992).
-   Posicionar la cámara para ver más terreno por un lado que por otro
    (típico en los juegos de disparos).
-   Sacudidas de pantalla al disparar para añadir dinamismo.
-   Implementar retroceso del personaje al disparar.
-   Sleep: una técnica sutil que durante unos milisegundos deja el juego
    parado al realizar un impacto (por ejemplo 20ms al disparar a un
    enemigo) esos milisegundos dejan al cerebro que asimile lo que está
    ocurriendo y lo procese con más intensidad.
-   Añadir un retraso de disparos poniendo un límite a las ráfagas de
    disparos por tiempo.
-   Reculación del arma al disparar (en forma de animación de kick back,
    sólo en el arma).
-   Añadir castigo/penalización al utilizar demasiado rato el disparo,
    desatar por ejemplo un sobrecalentamiento de arma inhabilitándola
    durante unos segundos.
-   Permanencia de los casquillos de las balas, aunque si no queremos
    sobrecargar podemos hacer que desaparezcan al cabo de un rato.
-   Añadir sonidos más graves en los SFX de los disparos.
-   Implementar super armas con mutliráfagas de disparos y cosas así, no
    hay límite en lo que se puede hacer, es un juego!
-   Añadir explosiones aleatorias, es más divertido cuando hay una
    posibilidad que los enemigos exploten al morir y el efecto es
    sencillo.
-   Aumentar la velocidad de los enemigos, estilo slice and dice.
-   Aumentar aún más las sacudidas de cámara al disparar.
-   Aumentar aún más el tamaño y alcance de las explosiones.
-   Incluir incluso más permanencia en forma de humo al haber
    explosiones.
-   Añadir efectos de ralentización bajando el framerate en algún
    momento, por ejemplo durante la animación de derrota del personaje.

14 + 29 = 42 (+1 de propina) formas de mejorar vuestros videojuegos.

¡Espero que os sirva tanto como a mí!

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