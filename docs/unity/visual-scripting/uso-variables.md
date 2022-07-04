title: Uso de variables | Curso Unity desde cero | Hektor Profe

# Uso de variables

Las variables son la quintaesencia de la programación, son algo tan básico e imprescindible que las llevamos utilizando durante todo el curso sin darnos cuenta.

¿Recordáis las propiedades de los componentes? Pues son variables, almacenes de datos de un tipo determinado identificados con un nombre y cuyo valor, como su nombre indica, puede variar:

![]({{cdn}}/unity/Screenshot_88.png)

Solo en los componentes actuales del cubo encontramos docenas y docenas de variables. Desde el propio nombre del objeto cubo, que es una `string`, la casilla de activar o desactivar el objeto, que es la visualización de un dato lógico `boolean`, los vectores de posición, rotación y escalado formados por varios números que hacen referncia a los ejes X, Y, Z y un largo etcétera. 

En definitiva todos los valores que se pueden modificar son variables.

Las variables existen dentro de lo que se conoce como `scopes`, en español ámbitos. Podemos observar esos ámbitos en el inspector del editor de gráficos:

![]({{cdn}}/unity/Screenshot_89.png)

Estos ámbitos pueden ser a nivel de gráfico, objeto, escena, aplicación y de guardado. El ámbito de gráfico es muy restrictivo, pues abarca únicamente el propio gráfico, mientras que las variables de guardado son accesibles desde cualquier lugar y además son persistentes. No vamos a entrar mucho en detalle porque estas cosas se aprenden mejor con la práctica.

Por lo pronto vamos a crear una variable de gráfico para substituir el literal booleano que controla si se mueve o no el cubo. La vamos a llamar `activarMovimiento` y será de tipo `Boolean`:

![]({{cdn}}/unity/Screenshot_90.png)

Los nombres de las variables deben ser autoexplicativos, sino acabaremos con un videojuego repleto de variables que no sabemos qué hacen. 

Algo interesante es que en `Visual Scripting` no hay restricciones respecto al nombre de las variables, pero igualmente os aconsejo utilizar alguna notación común y ceñiros a ella en el proyecto:

![]({{cdn}}/unity/Screenshot_91.png)

En cualquier caso ya tenemos una variable booleana que puede substituir al valor literal, vamos a arrastrarla al gráfico para utilizarla en lugar de éste:

![]({{cdn}}/unity/Screenshot_93.png)

A efectos prácticos es lo mismo, pero debemos considerar que el valor ahora existe en la memoria bajo el nombre `activarMovimiento` y eso nos permitirá interactuar con él desde otras unidades dentro del gráfico.

Vamos a crear un evento para capturar el momento en que el usuario presiona la tecla `espacio` del teclado. Para ello buscaremos una unidad `on keyboard input`. 

Este evento es especial y no requiere un flujo previo, se iniciará al interactuar con la tecla que nosotros le digamos, ya sea al presionarla (Down), dejar de presionarla (Up) o mantenerla (Hold):

![]({{cdn}}/unity/Screenshot_94.png)

Si conectamos a este evento, una unidad que sea capaz de cambiar el valor de la variable `activarMovimiento` deberíamos ser capaces de controlar cuando empieza a moverse le cubo.

La unidad que nos interesa se llama `set graph variable`. Notad que la unidad de la variable arrastrada se llama `Get Variable`, pues `get` permite recuperar el valor, mientras que `set` permite establecerlo. 

**Podemos arrastrar la variable al gráfico manteniendo la tecla ALT** para crear la unidad `SET` en lugar de `GET`, así que básicamente configuraremos el flujo y estableceremos la variable con un valor literal booleano:

![]({{cdn}}/unity/Screenshot_95.png)

Si probamos el juego, al presionar `ESPACIO` la variable cambiará su valor a verdadero y el cubo empezará a moverse.

Pero vamos un paso más allá, en lugar de usar un literal booleano podemos utilizar como fuente la propia variable `activarMovimiento` negando su valor. Negar un valor lógico da como resultado el contrario y es una operación muy simple, podemos hacerlo mediante una unida `negate`:

![]({{cdn}}/unity/Screenshot_96.png)

Lo que acabmos de hacer nos permite alternar los valores `verdadero` y `falso` de la variable booleana cada vez que presionamos la tecla espacio, pudiendo controlar a voluntad el movimiento del cubo.

Me gusta este experimento porque ilustra, aunque de forma sencilla, el funcionamiento de los videojuegos jugando con las variables y los eventos.

___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>