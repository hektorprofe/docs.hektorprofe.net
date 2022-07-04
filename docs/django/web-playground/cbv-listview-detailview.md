title: DetailView y ListView  | Curso de Django | Hektor Profe

# DetailView y ListView 

Ahora mismo nuestra app Pages tiene dos vistas, una para mostrar un
resumen de las páginas (pages) y otra para cada página individual
(page).

![]({{cdn}}/django/images/image180.png)

Pues os gustará saber que existen dos CBV pensadas para ambas
situaciones, ya sea devolver una instancia o una lista, y son ni más ni
menos que DetailView y ListView, vamos a utilizarlas.

Para implementarlas vamos a inspirarnos en la documentación oficial, a
la cual llegamos fácilmente desde
[https://ccbv.co.uk/](https://ccbv.co.uk/).

Empecemos por la lista de páginas: \
[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.list/ListView/](https://ccbv.co.uk/projects/Django/2.0/django.views.generic.list/ListView/) \
[https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/\#django.views.generic.list.ListView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/\#django.views.generic.list.ListView) 

Sirviéndonos del ejemplo:

![]({{cdn}}/django/images/image104.png)

![]({{cdn}}/django/images/image470.png)\
![]({{cdn}}/django/images/image462.png)

Ahora adaptamos la URL…

![]({{cdn}}/django/images/image147.png)

Ahora vamos a recargar la web y veremos un error:

![]({{cdn}}/django/images/image209.png)

Como véis de forma automática está esperando un template llamado
page\_list.html en lugar de pages.html. Tenemos dos opciones, o
redefinir el atributo template\_name o cambiar el nombre del template
directamente, vamos a hacer la segunda:

![]({{cdn}}/django/images/image825.png)

Si ahora actualizamos la /pages/ veremos que no aparece ninguna página:

![]({{cdn}}/django/images/image405.png)

Tranquilos, esto no significa que no lo hayamos hecho bien, sino que por
defecto nuestra lista de páginas no se envía con el nombre “pages”, sino
con uno genérico de las ListView, y que tal como pone en el ejemplo de
la documentación es:

![]({{cdn}}/django/images/image567.png)

Por tanto sólo debemos ir a nuestro template y cambiar el nombre de esta
variable:

![]({{cdn}}/django/images/image260.png)

Aunque también se acepta por defecto el nombre del modelo seguido de
 \_list:

![]({{cdn}}/django/images/image178.png)

Actualizamos de nuevo:

![]({{cdn}}/django/images/image322.png)

Y ahí tenemos nuestra ListView. ¿Habéis visto cómo utilizando una
ListView nos hemos ahorrado un montón de código? E ahí la gran utilidad
de las CBV.

Vamos a hacer la DetailView para mostrar cada página de forma
individual:

[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.detail/DetailView/](https://ccbv.co.uk/projects/Django/2.0/django.views.generic.detail/DetailView/) \
[https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/\#django.views.generic.detail.DetailView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/\#django.views.generic.detail.DetailView) 

![]({{cdn}}/django/images/image421.png)\
![]({{cdn}}/django/images/image905.png)

Y la URL:

![]({{cdn}}/django/images/image101.png)

Evidentemente ahora tendremos que cambiar algunas cosas para que
funcione. Si visitamos una página y analizamos el error veremos como
solucionarlo:

![]({{cdn}}/django/images/image446.png)

Lo que nos está indicando es que nuestra DetailView está esperando un
campo pj o un campo slug para buscar la página. Nuestro objeto no tiene
un campo slug, sólo lo estamos utilizando de adorno, así que pasaremos
la clave primaria, pk, que no es más que el id. De hecho ya lo estamos
pasando, pero no con el nombre que él espera que es pk:

![]({{cdn}}/django/images/image170.png)

Si todo va bien el siguiente paso será cambiarle el nombre al template
por uno genérico:

![]({{cdn}}/django/images/image203.png)

Así que vamos a cambiarlo:

![]({{cdn}}/django/images/image710.png)

Si actualizamos la página veremos que esta vez ya nos funciona sin
cambiar el nombre de la variable:

![]({{cdn}}/django/images/image137.png)

Esto es porque de forma similar a la ListView, en su template se acepta
tanto la variable {{object}} como el nombre del modelo para hacer
referencia al objeto, y como tenemos {{page}} pues ya funciona:

![]({{cdn}}/django/images/image291.png)

Y de esta forma hemos vuelta a ahorrarnos 3 líneas apenas poniendo dos
palabras: model = Page

¿Supongo que ya empezáis a tener otra visión de las CBV no? Pues esto no
es nada, en la siguiente lección vamos a crear nuestras propias vistas
CRUD (Create-Read-Update-Delete) para gestionar páginas sin necesidad de
utilizar el panel de administrador, ya veréis que útil.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>