title: Práctica: Novena App (Profiles) Perfiles públicos | Curso de Django | Hektor Profe

# Práctica: Novena App [Profiles] Perfiles públicos

Muy bien pues vamos a solucionar la práctica anterior. Como se trata de
una app relativamente sencilla la he preparado de antemano y solo vamos
a repasar los puntos importantes:

![]({{cdn}}/django/images/image365.png)

Vamos a empezar repasando las vistas:

![]({{cdn}}/django/images/image246.png)

No tienen mucha complicación, sólo remarcar que por defecto los
templates se van a buscar a la app registration, donde está creado el
modelo Profile, simplemente debemos cambiar el template\_name.

![]({{cdn}}/django/images/image843.png)

Respecto a las URLS en este caso yo he utilizado la lógica de app:vista,
no era obligatorio hacerlo así, por lo que mientras os funcione está
bien.

En cuanto a los templates simplemente he mostrado una tabla:

![]({{cdn}}/django/images/image193.png)

He ido generando las filas \<tr\> en un bucle para cada profile en
profile\_list y les he añadido una columna con el enlace:

![]({{cdn}}/django/images/image34.png)

Para los perfiles públicos he reutilizado la estructura a dos columnas
del formulario:

![]({{cdn}}/django/images/image616.png)

Como véis utilizando CBV la parte del backend es fácil, lo que más
trabajo da es adaptar los templates.

Por cierto, os pedí crear por lo menos 4 usuarios de prueba, lo he hecho
con la excusa de añadir paginación a nuestra ListView, trataremos el
concepto en la siguiente lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>