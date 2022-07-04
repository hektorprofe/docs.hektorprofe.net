title: Grupos y superunidades | Curso Unity desde cero | Hektor Profe

# Grupos y superunidades

En esta última lección vamos a introducir brevemente el uso de los grupos y las superunidades, dos formas de organizar y reutilizar contenido en los scripts gráficos.

Los grupos son una forma de gestionar conjuntos de unidades, se basa en envolver unas cuantas unidades con el ratón mientras presionamos con la tecla `Control`:

![]({{cdn}}/unity/Screenshot_116.png)

Una vez tenemos un grupo podemos manipular en conjunto las unidades que lo forman, también podemos asignarle un nombre, una descripción y un color:

![]({{cdn}}/unity/Screenshot_117.png)

Crear grupos es una forma visual de organizar los scripts y comprobar de un vistazo su funcionamiento.

Por otro lado, con el objetivo de simplificar y reutilizar los gráficos, las superunidades nos permiten agrupar varias unidades en una única maestra identificada con un nombre, vienen a substituir las funciones de código.

Hagamos un ejemplo para ilustrar el funcionamiento.

En el script `Controlador` podemos substituir todo el proceso de alternar la variable en una única `superunidad` llamada `alternarMovimiento`. Para crearla hacemos clic derecho y buscamos `superunit` en el navegador:

![]({{cdn}}/unity/Screenshot_118.png)

Podemos acceder a la superunidad haciendo doble clic en ella y dentro veremos que tiene un `input` y un `output`, ahí definiremos los datos que entran y salen de la superunidad.

La entrada de nuestra superunidad corresponde al flujo que se genera al presionar una tecla, así que vamos a crear un disparador de entrada con el nombre `Flujo`:

![]({{cdn}}/unity/Screenshot_119.png)

Tenemos que llevarnos las unidades de fuera a la superunidad y configurar el flujo de entrada:

![]({{cdn}}/unity/Screenshot_120.png)

Y desde conectar el flujo del evento a la superunidad:

![]({{cdn}}/unity/Screenshot_121.png)

Como en esta superunidad no tenemos un `output` de salida, ya la tenemos lista y si probamos el juego hará lo mismo pero habremos simplicado ligeramente el gráfico.

![]({{cdn}}/unity/Record_19.gif)

A lo largo del curso trabajaremos activamente con los grupos y las superunidades.

Sea como sea con esto acabamos el primer bloque donde hemos repasado los conceptos básicos del desarrollo y a partir de ahora toca crear videojuegos.

___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>