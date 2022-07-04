title: Vistas CRUD con CBV: UpdateView | Curso de Django | Hektor Profe

# Vistas CRUD con CBV: UpdateView

Las vistas Update y Delete nos permiten editar y borrar instancias, pero
a diferencia de Create a estas tendremos que pasarles una pk o un slug
para que puedan recuperar la instancia, de forma similar a como hicimos
con DetailView.

Vamos a empezar por UpdateView:

[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/UpdateView/](https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/UpdateView/)\
[https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.UpdateView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.UpdateView) 

![]({{cdn}}/django/images/image674.png)\
![]({{cdn}}/django/images/image873.png)\
![]({{cdn}}/django/images/image136.png)

Ahora sólo tendríamos que añadir un enlace de edición en la lista de
páginas para que nos lleve al formulario:

![]({{cdn}}/django/images/image476.png)\
![]({{cdn}}/django/images/image898.png)

Si probamos a editar una página, como veréis funciona directamente:

![]({{cdn}}/django/images/image810.png)

Esto es porque tanto el formulario de creación como el de edición se
toman del mismo template page\_form.html. El problema es que como
nuestro botón de envío tiene un texto específico “Crear página”. Hay
muchísimas formas de solucionar esto, pero la genérica es simplemente
utilizar otro template con el texto del botón cambiado a “Actualizar
página”.

Para indicarle a nuestra UpdateView que utilice un template alternativa
sólo tenemos que establecer su atributo template\_name\_suffix:

![]({{cdn}}/django/images/image320.png)

Esto irá a buscar automáticamente un template page\_update\_form.html,
así que vamos a clonar el que tenemos con este nombre y le cambiaremos
el texto al botón:

Como en el botón de la parte inferior

![]({{cdn}}/django/images/image687.png)\
![]({{cdn}}/django/images/image808.png)![]({{cdn}}/django/images/image846.png)

Si intentamos editar de nuevo una página ya nos saldrá bien, y si
intentamos actualizarla...\
![]({{cdn}}/django/images/image663.png)

Veremos como nuevamente nos pide configurar una url de redirección:

![]({{cdn}}/django/images/image225.png)

En este caso si quisiéramos redireccionar a la lista de páginas bastaría
con hacer como antes:

![]({{cdn}}/django/images/image904.png)

Pero si queréis redirigir de nuevo al formulario es un poco más
complejo. Necesitaríamos extraer la pk de la instancia. Para lograrlo
esta vez sí debemos redefinir el método get\_success\_url y, ahí obtener
la id de self.object y pasarla como argumento a reverse\_lazy:

![]({{cdn}}/django/images/image398.png)

Como esto no le da ninguna retroalimentación al usuario, os sugiero
añadir un campo GET al final con un ok y capturarlo en el template:

![]({{cdn}}/django/images/image382.png)\
![]({{cdn}}/django/images/image672.png)

![]({{cdn}}/django/images/image780.png)

Y con esto tenemos nuestra UpdateView.

En la próxima lección veremos como trabajar con DeleteView para borrar
instancias.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>