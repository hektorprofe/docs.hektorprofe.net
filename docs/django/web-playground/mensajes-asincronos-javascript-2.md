title: Mensajes asíncronos con JS (2): Desarrollo  | Curso de Django | Hektor Profe

# Mensajes asíncronos con JS (2): Desarrollo 

El textarea que almacenará el mensaje tendrá una estructura típica con
bootstrap, pero en lugar de darle un name, le daremos un id, puesto que
lo recuperaremos utilizando Javascript:

![]({{cdn}}/django/images/image148.png)

Ya que estamos podemos modificar el botón y hacer que se vea mejor:

![]({{cdn}}/django/images/image682.png)

Ahora viene la parte dinámica, pues tenemos que modificar el Script para
recuperar el contenido del textarea al presionar el botón, y no sólo
eso, también hay que codificarlo para que no dé problemas al enviarlo
por GET:

![]({{cdn}}/django/images/image682.png)

Habiendo hecho esto si enviamos algo desde el formulario debería
aparecernos en los parámetros GET de la vista:

![]({{cdn}}/django/images/image915.png)\
![]({{cdn}}/django/images/image309.png)

Esto ya va tomando forma, pero faltan bastantes cosas.

Lo primero una validación que no permita enviar mensajes vacíos, así que
antes de hacer el fetch() comprobaremos que el mensaje tiene por lo
menos un carácter:

![]({{cdn}}/django/images/image327.png)

Esto quedaría aún mejor implementando un Evento con Javascript que
compruebe si el textarea tiene algún valor mientras se escribe. Si lo
tiene activamos el botón de envío, y si no lo desactivamos. Eso sí,
inicialmente tenemos que tener el botón desactivado:

![]({{cdn}}/django/images/image923.png)\
![]({{cdn}}/django/images/image302.png)

Ya sé que no es un curso de JavaScript, pero es que me encanta el
resultado:

![]({{cdn}}/django/images/image769.png)

Ahora vamos a lo importante: procesar este contenido que nos llega a la
vista.

Lo primero será recuperar al usuario, por lo que necesitaremos que esté
identificado. En caso de que no lo esté invocaremos un error 404:

![]({{cdn}}/django/images/image271.png)\
![]({{cdn}}/django/images/image96.png)

Lo curioso en este momento,  es que si intentamos enviar un mensaje nos
va a dar error:

![]({{cdn}}/django/images/image857.png)

¿Cómo es esto posible? Si se supone que estamos identificados…

Bueno, esto ocurre porque una petición fetch() no envía las credenciales
del usuario identificado, para incluirlas en la petición debemos
indicarlo explícitamente:

![]({{cdn}}/django/images/image628.png)

Habiendo hecho esto la sesión actual se enviará también en la petición
asíncrona y ahora sí debería detectar correctamente si el usuario está
identificado para volver a darnos false:

![]({{cdn}}/django/images/image669.png)

Respecto al backend ya sólo nos falta recuperar el Contenido y el Hilo
para poder crear el mensaje si hay algún mensaje. Además una vez lo
creemos modificaremos la clave created y la pondremos a True dando a
entender que todo ha ido bien:

![]({{cdn}}/django/images/image537.png)![]({{cdn}}/django/images/image464.png)

Por fin ha llegado el momento de la verdad, ¿funcionará nuestro código?
Vamos a probarlo:

![]({{cdn}}/django/images/image264.png)

Por lo pronto devuelve True, así que vamos a actualizar la página con F5
a ver si aparece:

![]({{cdn}}/django/images/image40.png)

Y ahí lo tenemos, abajo del todo está el nuevo mensaje:

![]({{cdn}}/django/images/image874.png)

Ya sólo nos falta desarrollar el Javascript para mostrar el mensaje sin
recargar la página directamente y algún que otro detalle, pero en
principio el backend lo tenemos listo.

Así que vamos a tomarnos un descanso y afinamos los detalles en la
tercera parte de esta lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>