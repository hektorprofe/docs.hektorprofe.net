Title: ¿Cómo funcionan los videojuegos? | Escuela de Videojuegos | Hektor Profe
Date: 2015-10-19 13:27
Category: Artículos
Tags: bucle, ciclos, dibujo, entorno, fases, funcionamiento, inicalizacion, lenguaje, liberación, lógica, renderizado, videojuego
Slug: funciona-videojuego-fases-logicas
description: ¿Algunas vez te has preguntado qué ocurre detrás de un videojuego para que funcionen? Pues te lo voy a explicar.

# ¿Cómo funcionan los videojuegos?

El otro día ya dediqué una entrada a explicar qué es un videojuego,
hoy os traigo una explicación de su funcionamiento, cuáles son las fases
lógicas que todos los videojuegos siguen desde el punto de vista de su
programación.

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/10/video_games_1.jpg" style="width:100%" /></div>

## Fase 1: Inicialización

Sea cual sea el videojuego y el lenguaje o entorno sobre el que se ha
desarrollado, la primera fase siempre es la inicialización en la
memoria. Ésto incluye cargar las librerías, declarar variables, scripts,
 objetos, colecciones dinámicas, asignarles valores iniciales,
etc.

También se suelen precargar recursos para utilizarlos más rápidamente,
como por ejemplo imágenes, modelos, fuentes, sonidos… pero no todos.
Imaginad un videojuego con miles de recursos, si los cargamos todos en
la memoria ram de golpe no daría abasto.

La clave es precargar lo necesario en cada momento, y ésto se puede
hacer gracias a que  los juegos se separan en pantallas o escenarios.
Por tanto no se requerirán los mismos recursos para una crear una
pantalla inicial, que para el momento del juego en sí. Además por no
decir que hay recursos que se pueden utilizar directamente desde el
disco duro, como puede ser la música, así que no hace falta
precargarlos.

Sea como sea, una vez tenemos todo lo necesario en la memoria es
momento de llamar las rutinas que crearán el espacio de juego, por ahora
del escenario inicial. Cómo hacerlo dependerá del entorno o lenguaje,
por lo que no vale la pena profundizar.

Una vez tenemos el espacio, ya sea en 2D o en 3D, tenemos que cargar
los componentes y objetos dentro, normalmente otorgándoles las
posiciones y valores iniciales relativos al espacio y ya estaremos más o
menos listos para comenzar el bucle de
juego.

## Fase 2: Bucle de juego

La fase del bucle de juego es la encargada de crear la ilusión óptica
que percibimos como algo “real” con lo que se puede interactuar. Es la
más importante y controla los procesos fundamentales de la lógica y el
dibujo (o renderizado).

Se conoce como bucle porque se basa en repetir el proceso de dibujo del
espacio con sus componentes y objetos muchas veces por segundo,
normalmente el mismo número de fotogramas con los que estemos
trabajando. Pero claro, si sólo se dibujara el escenario no habría
ningún dinamismo (no veríamos nada moverse ni podríamos interactuar),
por éso siempre antes del proceso de dibujo se ejecuta la lógica del
juego.

Durante la lógica del juego es cuando se controla todo. Se capturan
eventos del teclado, del ratón, se redefinen las propiedades de los
objetos (como su posición en el espacio, o su velocidad), se comprueban
si hay colisiones entre objetos, se cambian sus estados y un largo
etcétera.

Una vez ya hemos analizado el momento e indicamos qué debe hacer cada
componente y objeto del escenario, podemos proceder a su dibujo, que
también depende del entorno o lenguaje que utilicemos. El resultado del
proceso de dibujo será una imagen o fotograma del instante que hemos
programado en el proceso anterior.

Al visualizarse el proceso muchas veces por segundo se crea la ilusión
de movimiento y además como estamos constantemente analizando y
redefiniendo los comportamientos de lo que se dibuja podemos hacer que
sea un proceso interactivo gracias a la retroalimentación que el usuario
nos facilita al presionar el ratón o el
teclado.

## Fase 3: Liberación

Por último pero no por ello menos importante, una vez decidimos que el
juego debe finalizar es fundamental realizar las tareas de limpieza de
la memoria y liberar todos los datos
almacenados.

La mayoría de entornos lo hacen automáticamente, con algunas
excepciones. Si no se utiliza un entorno hay que llamar los métodos y
rutinas necesarias o podríamos acabar saturando la memoria
ram.

## Conclusión

Visto de esta forma no parece muy complejo, pero debido a que todo se
basa en el control del escenario y los objetos que hay dentro, las
matemáticas son fundamentales, concretamente la geometría en el plano
(en 2D) y la geometría en el espacio (en
3D).

Aunque claro está que no es lo mismo utilizar motores o “engines” ya
existentes a tener que programar el tuyo propio. Sería como utilizar la
calculadora o hacerlo a mano, tú decides.

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