title: Buscador de unidades | Curso Unity desde cero | Hektor Profe

# Buscador de unidades

Retomándolo donde lo dejamos en la lección anterior, quiero profundizar un poco en las unidades.

Y es que cuando vamos a añadir un nodo en el gráfico, aparecen muchas categorías, cada una con infinidad de unidades disponibles:

![]({{cdn}}/unity/Screenshot_79.png)

Empecemos centrándonos en las primeras de la lista, pues hacen referencia a los componentes del `GameObject` donde se ha asignado la `Script Machine`. En nuestro caso el cubo tiene un `Transform`, los `Mesh Filter y Render`, un `Box Collider` y el propio `Script Machine`. Si queremos interactuar con cualquiera de ellos tenemos muchas unidades disponibles. Pero encima de todo también tenemos una categoría llamada `Game Object`, cuyas unidades nos permiten acceder y gestionar los `GameObjects` de la escena.

![]({{cdn}}/unity/Screenshot_80.png)

Volviendo al principio encontramos otras categorías generales, colecciones, controles, eventos, lógica, matemáticas, etc.

Existen más de 20.000 unidades y eso es porque deben cubrir cualquier acción programable. Es imposible saberlas todas de memoria y la idea es buscarlas y utilizarlas a medida que surja la necesidad. La gracia del `Visual Scripting`, es que tenemos a nuestra disposición un potente buscador de unidades y eso facilita la tarea a la hora de investigar.

Por ejemplo, vamos a suponer que después de rotar un grado el eje Y en cada `Update`, queremos desplazar el cubo hacia arriba.

Si movemos el cubo hacia arriba en la escena podemos observar que se modifica el eje Y del vector de posición en el componente `Transform`. Si abrimos el buscador de unidades y buscamos `transform translate`, encontraremos todas las unidades relacionadas con la traslación, la transformación que permite cambiar la posición:

![]({{cdn}}/unity/Screenshot_82.png)

Fijaros que aparece la misma unidad repetidas veces, esto se conoce como sobrecarga de un método, y sucede cuando tenemos diferentes formas de realizar una acción. En nuestro caso vamos a centrarnos en `Transform: Translate (X,Y,Z)` que simplemente toma un vector 3D con el valor a incrementar en cada eje:

![]({{cdn}}/unity/Screenshot_83.png)

Notaréis que por defecto esta unidad se muestra transparente, eso es porque no le llega ningún flujo de código y se considera inactiva.

Podemos unir el flujo de salida en la rotación con la entrada de flujo de la traslación y activarla:

![]({{cdn}}/unity/Screenshot_84.png)

Esto se traduciría como: en cada `Update` ejecutar una rotación y luego una traslación. Vamos a indicar un número muy pequeño al eje Y, por ejemplo `0.1` y veamos el resultado:

![]({{cdn}}/unity/Record_13.gif)

Como véis el cubo empieza a flotar hasta que desaparece. En cada fotograma estamos sumando 0.01 unidades del mundo a su posición Y (recordemos que una unidad del mundo equivale a los cuadrados del escenario), eso son 0.60 unidades de altura cada segundo suponiendo que el videojuego funciona a 60 FPS.

En definitiva el flujo es la corriente vital del script gráfico y fluye a través de las unidades activándolas para ejecutar sus acciones. 


___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>