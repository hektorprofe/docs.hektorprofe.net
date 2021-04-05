title: Urls, vistas y templates | Curso de Django | Hektor Profe

# Urls, vistas y templates

No sirve de nada crear unas vistas sin contenido, así que antes vamos a
añadir algunos datos a nuestros modelos. Podemos hacerlo desde la shell
o configurando el admin, yo como soy más de terminal utilizaré la
primera forma.

![]({{cdn}}/django/images/image764.png)

![]({{cdn}}/django/images/image359.png)\
![]({{cdn}}/django/images/image805.png)

![]({{cdn}}/django/images/image722.png)\
![]({{cdn}}/django/images/image615.png)

![]({{cdn}}/django/images/image577.png)

![]({{cdn}}/django/images/image799.png)

![]({{cdn}}/django/images/image817.png)

Ahora sí, vamos con las vistas. Necesitamos por lo menos dos, una para
mostrar los hilos del usuario, y otra para mostrar un hilo en concreto,
por lo que podríamos crear:

-   Una ListView para listar todos los hilos de un usuario en
    /messenger/
-   Una DetailView para listar todos los mensajes de un hilo en
    /messenger/thread/\<int:pk\>/

![]({{cdn}}/django/images/image60.png)

Evidentemente no podemos dejarlas así. En el caso de la ListView no
queremos devolver todos los Thread, sólo los del usuario, así que
debemos filtrarlos. Para conseguirlo sobreescribiremos el método
get\_queryset y filtraremos por el request.user. Esto implica que el
usuario esté identificado, así que necesitamos decorar la CBV con
login\_required:

![]({{cdn}}/django/images/image571.png)

![]({{cdn}}/django/images/image354.png)

La lógica normal sería esta, pero dado que nuestro usuarios tienen una
relación con el modelo Thread a partir del campo Many2Many messages,
podríamos acceder directamente en el template y ahorrarnos toda el
ListView, usando en su lugar una simple TemplateView:

![]({{cdn}}/django/images/image732.png)\
![]({{cdn}}/django/images/image870.png)

Respecto a la DetailView debemos sobreescribir el método get\_object,
ahí comprobaremos si el request.user forma parte del hilo, y si no es
así lanzaremos un error 404:

![]({{cdn}}/django/images/image386.png)\
![]({{cdn}}/django/images/image339.png)

Ahora que tenemos las views vamos a configurar las URL, ponedlas como yo
porque os facilitaré un par de templates ya preparados y utilizarán esta
lógica:

![]({{cdn}}/django/images/image564.png)

![]({{cdn}}/django/images/image752.png)\
![]({{cdn}}/django/images/image118.png)

Nuestras vistas cargarán los templates thread\_list.html y
thread\_detail.html, como os comentaba os los doy hechos para no alargar
demasiado la lección, los podéis descargar en los recursos y copiarlos
en un nuevo directorio templates/messenger en la propia app:

![]({{cdn}}/django/images/image595.png)

![]({{cdn}}/django/images/image517.png)

He añadido comentarios en los Templates para que podáis analizarlos
vosotros mismos, si tenéis alguna duda me lo decís.

Ya sólo nos faltaría añadir la sección message en el menú superior si
estamos identificados:

![]({{cdn}}/django/images/image268.png)

Y probar si todo funciona:

![]({{cdn}}/django/images/image233.png)

En la siguiente lección añadiremos el formulario para enviar mensajes.


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>