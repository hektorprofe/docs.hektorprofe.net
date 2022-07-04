title: Mejorando el formulario de perfil | Curso de Django | Hektor Profe

# Mejorando el formulario de perfil

En esta pequeña lección vamos a mejorar algo el aspecto del formulario
de perfil, mezclando nuestro propio formulario con widgets y un poco de
bootstrap.

En primer lugar vamos a implementar un formulario para nuestro modelo
Profile:

![]({{cdn}}/django/images/image376.png)

Fijaros que hemos puesto un ClearableFileInput, eso es para conservar la
opción de borrar la imagen:

![]({{cdn}}/django/images/image524.png)![]({{cdn}}/django/images/image574.png)

Sólo con esto nuestro formulario ya tendrá un mejor aspecto:

![]({{cdn}}/django/images/image183.png)

Pero todavía es muy soso, y esas opciones para la imagen… quedan muy
mal.

La única salida que nos queda es maquetar cada campo manualmente, así
que he preparado un diseño de antemano, os adjunto el enlace en los
recursos:

[https://gist.github.com/hcosta/3302f2cf81b71872c503b405adfb1708](https://gist.github.com/hcosta/3302f2cf81b71872c503b405adfb1708)

Una vez pongamos el nuevo template todo tendrá mejor aspecto:

![]({{cdn}}/django/images/image715.png)

¿Bastante bien no? Pues todavía podemos mejorar una última cosa, y es
que ahora mismo si nuestro usuario no tiene una imagen de perfil no nos
aparece nada. ¿Y si ponemos una imagen de avatar genérica? Os adjunto en
los recursos una imagen llamada no-avatar.jpg, copiadla dentro de los
ficheros estáticos de la app static/registration/img:

![]({{cdn}}/django/images/image312.png)

Ahora vamos a modificar ligeramente el código para mostrar esta imagen
si el usuario no tiene un avatar:

![]({{cdn}}/django/images/image267.png)

Por último recargamos el servidor para cargar en memoria los nuevos
ficheros estáticos y...

![]({{cdn}}/django/images/image269.png)

Muy bien! En la próxima lección añadiremos un enlace al formulario para
que el usuario pueda cambiar su email.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>