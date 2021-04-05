title: PVistas CRUD con CBV: CreateView | Curso de Django | Hektor Profe

# Vistas CRUD con CBV: CreateView

Así que nuestro objetivo es crear nuestras propias vistas CRUD para
manejar Páginas de forma alternativa al admin.

Lo primero que necesitamos es un lugar donde poner estas posibles
acciones así que vamos a crear un submenú superior para darle la opción
al usuario de crear una página en cualquier momento. Obviamente este
menú sólo aparecerá si el usuario es parte del staff y está
identificado.

Como la idea es contar con este submenú en cualquier parte de la app
/pages/ y sería redundante añadirlo en todos los templates os voy a
enseñar cómo utilizar el Tag {%raw%}{% include %} {%endraw%} para incluir porciones de
código.

Es muy fácil, vamos a crear un nuevo template pages\_menu.html dentro de
un subdirectorio includes. No es obligatorio hacerlo así pero es una
buena forma de organizar los includes:

![]({{cdn}}/django/images/image48.png) 

El contenido os lo voy a dar hecho, es básicamente un submenú con varios
enlaces. Os adjunto el código en un enlace en los recursos, podéis
copiarlo como yo:
[https://gist.github.com/hcosta/143950b40dda8cf640076a629cec7f09](https://gist.github.com/hcosta/143950b40dda8cf640076a629cec7f09) 

Ahora sólo tenemos que incluir este menú en las páginas donde queramos
mostrarlo, por ahora pages\_detail y page\_list, justo donde empieza el
bloque content:

![]({{cdn}}/django/images/image613.png)

Si recargamos la página y estemos identificados con un usuario miembro
del staff nos aparecerá este submenú dándonos la opción de crear una
nueva página:

![]({{cdn}}/django/images/image119.png)

Ahora nos toca implementar la funcionalidad, para ello vamos a crear una
nueva CBV de tipo CreateView:

[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/CreateView/](https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/CreateView/)\
[https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.CreateView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.CreateView) 

Como siempre vamos a tomar el ejemplo de la documentación:

![]({{cdn}}/django/images/image909.png)

Y lo vamos a adaptar para manejar páginas. En nuestro caso queremos que
el usuario pueda establecer el título y el contenido así que indicaremos
esos campos:

![]({{cdn}}/django/images/image884.png)![]({{cdn}}/django/images/image232.png)\
![]({{cdn}}/django/images/image668.png)

Ahora vamos a cambiar la URL en el menú y a ver cuál es el siguiente
paso:

![]({{cdn}}/django/images/image550.png)

Como véis en esta ocasión nos devuelve que necesita un template llamado
page\_form:

![]({{cdn}}/django/images/image367.png)

Así que vamos a crearlo:

![]({{cdn}}/django/images/image486.png)

¿Y qué contenido le ponemos? Lo básico sería lo que nos muestran la
documentación. También he maquetado el contenido de antemano, así que
podéis copiar el que os dejo en los recursos, igual que voy a hacer yo:

[https://gist.github.com/hcosta/456df0769f153a2458e711d3f78b75a2](https://gist.github.com/hcosta/456df0769f153a2458e711d3f78b75a2)

Si recargamos la página veremos un formulario sencillo, pero creado
automáticamente:

![]({{cdn}}/django/images/image216.png)

Sé lo que estáis pensando. Mola, ¿pero cómo le añado mis propios
estilos? Tranquilos, lo haremos más adelante. Por ahora vamos a crear
una página a ver si funciona o tenemos que hacer algo más:

![]({{cdn}}/django/images/image705.png)

Al enviar el formulario veréis que da un error:

![]({{cdn}}/django/images/image639.png)

Lo que nos está diciendo es que no hemos definido una url de
redirección, pero curiosamente sí vamos manualmente a la lista de
páginas veremos que se ha creado!

![]({{cdn}}/django/images/image169.png)

Así que básicamente tenemos que volver a la View y añadir un atributo
success\_url con la página que queramos redireccionar. Sabéis que me
gusta hacer las cosas bien así que usaremos reverse para volver a la
lista de páginas:

![]({{cdn}}/django/images/image657.png)\
![]({{cdn}}/django/images/image853.png)

Sin embargo esto no nos va a funcionar:

![]({{cdn}}/django/images/image604.png)

Dentro de un CBV de tipo formulario no podemos usar el reverse, la forma
correcta es redefinir su método get\_success\_url y devolver la url:

![]({{cdn}}/django/images/image409.png)

Que buena gente estos de Django eh, siempre poniéndonos las cosas
fáciles. Por suerte si sois unos vagos y no queréis redefinir el método
get\_success\_url siempre podéis hacer lo de antes sustituyendo reverse
por reverse\_lazy:

![]({{cdn}}/django/images/image381.png)\
![]({{cdn}}/django/images/image217.png)

Si ponemos de nuevo el servidor en marcha y creamos otra página ya
debería funcionarnos:

![]({{cdn}}/django/images/image171.png)

![]({{cdn}}/django/images/image407.png)

Por cierto, si queréis cambiar el orden de las páginas, podéis hacer uso
de los TemplateTags dictsort y reversed para cambiarlo a vuestro gusto:

![]({{cdn}}/django/images/image731.png) 

Y con esto acabamos por ahora. ¿Qué os ha parecido la vista CreateView,
útil verdad? Pues todavía nos faltan dos más: UpdateView y DeleteView,
las veremos en la siguiente lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>