Title: Funciones, sistemas y puntos | Escuela de Videojuegos | Hektor Profe
Date: 2015-11-02 13:03
Category: Teoría de videojuegos
Tags: cartesianas, coordenadas, funciones, pantalla, puntos, repaso-teoria-tema-1, representación, sistemas, teoría
Slug: funciones-sistemas-puntos-teoria-matematicas
description: Teoría matemática sobre las funciones, sistemas y puntos en 2D y 3D

# Funciones, sistemas y puntos

## ¿Qué es una Función?

En el mundo de la programación es normal encontrar funciones. Por lo
general una función es una pauta o serie de instrucciones que toma una
información inicial (entrada / input) y devuelve nueva información
(salida / output). Esta función puede tomar variables, números, texto y
devolver todo tipo de información o simplemente realizar una
acción.

Sin embargo en las matemáticas una función sólo implica números. Toma
unos números, se aplican unas reglas y se devuelve un nuevo número. Una
de las formas para definir una función en las matemáticas es por ejemplo
una tabla de paridad ordenada con las entradas y salidas de la función
para sus valores. Por ejemplo supongamos que la función toma un número
(x) y devuelve el doble de éste (y):

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/tabla-de-pares.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Tabla de paridad ordenada*</small> 

Las tablas de paridad ordenadas son útiles, pero tienen muchas
limitaciones debido a que para determinar una salida antes hay que
describir todas las posibilidades
anteriores.

La otra forma de definir una función es utilizar una fórmula o ecuación
que relacione los dos números. Por ejemplo la tabla anterior se podría
definir utilizando la ecuación y = 2x, donde x es la entrada e y es la
salida. Esta es la manera cómoda y rápida, pues nos permite tomar
cualquier entrada y determinar su salida sin describir todas las
posibilidades, sólo sustituyendo el valor de x en la ecuación y
resolviéndola.

Quizá ahora te estás preguntando qué tienen que ver las funciones con
los videojuegos, pues mucho, porque precisamente se utilizan para poder
“poner” cosas en la pantalla del ordenador. Siendo más específicos,
cuando hablamos de poner, en realidad nos referimos a posicionar en la
pantalla, pero para posicionar debemos seguir algunas reglas y aquí es
dónde aparecen los sistemas de coordenadas.

## El sistema de coordenadas

Este sistema de representación consiste en una rejilla formada por un
eje-x horizontal y otro eje-y vertical. El primero representa la anchura
y el segundo la altura. Gracias a este sistema los programadores de
videojuegos pueden posicionar cualquier objeto sobre el plano 2D formado
por el sistema simulando la pantalla del
ordenador:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-2D.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Eje de coordenadas cartesianas*</small> 

Para hacerlo se utilizan los puntos.

## ¿Qué es un Punto?

Un punto es un objeto que indica un lugar particular en el sistema de
coordenadas. La notación de un punto es P(x,y), donde P es el nombre del
punto, x representa la coordenada horizontal e y su coordenada
vertical.

El lugar donde se cruzan los ejes se conoce como el punto de origen y
se corresponde con las coordenadas (0,0). A partir del origen el valor
de las x es positivo a la derecha y negativo a la izquierda. Así como el
valor de las y es positivo hacia arriba y negativo hacia
abajo.

Representar los puntos es bastante fácil, sólo hay que ir contando las
distancias y marcar el lugar donde se cruzan la proyecciones  de los
ejes:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/coordenadas-2D.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Representación de algunas coordenadas en el sistema cartesiano*</small> 

Gracias a este sistema se pueden utilizar funciones para mover los
objetos alrededor de la pantalla a partir de sus coordenadas x e y. Sin
embargo hay que diferenciar un punto importante antes de dar el tema por
zanjado, y es que las pantallas no utilizan el sistema cartesiano para
visualizar la información.

## Coordenadas en la pantalla

La diferencia entre el sistema cartesiano y de la pantalla varía en el
eje-y debido a que las pantallas están creadas para visualizar de arriba
hacia abajo. Eso se traduce en que el eje de las y es positivo hacia
abajo y negativo hacia arriba, o también que el origen se encuentra en
la esquina superior izquierda, mientras que para el sistema cartesiano
está en la esquina inferior izquierda, tal como muestra la siguiente
figura:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistemas-pantalla-cartesiano.png"/></div>

¿En qué nos afecta ésto? Pues que si quieres crear tu motor de
renderizado el último paso es convertir las coordenadas cartesianas en
coordenadas de pantalla, pero ésto suele ser un proceso automático en
muchas librerías y frameworks. Incluso hay entornos completos como
GameMaker que utilizan directamente coordenadas de pantalla para
ahorrarse este paso.

## Representación de objetos 3D

Hemos estado hablando de cómo representar objetos en el plano pero...
¿qué hay de los objetos en tres dimensiones? ¿Cómo se
representan?

En el caso de los videojuegos en 3D la cosa se complica un poco más,
pero las bases son fundamentalmente las mismas. Lo que se hace es añadir
un tercer eje-z al sistema de coordenadas para simular la
profundidad:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/sistema-3d.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Sistema cartesiano tridimensional*</small> 

Por tanto se añade la nueva coordenada z y un punto en el espacio
tridimensional se definirá P(x,y,z), siendo el origen el punto (0,0,0).
Normalmente cuanto más cerca del usuario esté el punto la profundidad
será más positiva (estará por encima) y cuanto más lejos será más
negativa (estará por debajo).

Esta interpretación es ámpliamente utilizada en las matemáticas y
también la utilizan la mayoría de programadores, además de ser un
estándar OpenGL, pero no es la única. En la siguiente imagen vemos un
ejemplo de representación de un punto:

<div style="text-align:center;margin-top:25px"><img src="{{cdn}}/wp-content/uploads/2015/11/espacio-tridimensional.png"/></div>
<small style="display:block;text-align:center;padding: 0 15px;">*Representación de un punto en el espacio 3D*</small> 

Cómo veis es algo más complicado de intuir pero en esencia es lo mismo
que las dos dimensiones, así que tiempo al tiempo.

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