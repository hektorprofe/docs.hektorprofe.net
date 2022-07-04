title: Vistas CRUD con CBV: DeleteView | Curso de Django | Hektor Profe

# Vistas CRUD con CBV: DeleteView

Bien, antes de ponernos con la DeleteView vamos a añadir un enlace para
borrar páginas en nuestra lista, justo al lado de editar:

![]({{cdn}}/django/images/image725.png)

Ahora vamos a crear la vista:

[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/DeleteView/](https://ccbv.co.uk/projects/Django/2.0/django.views.generic.edit/DeleteView/)\
[https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.DeleteView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/\#django.views.generic.edit.DeleteView) 

Esta es muy sencilla. Al igual que UpdateView está esperando un campo pk
o slug en el Path para recuperar la instancia. Luego mostrará un
formulario para confirmar el borrado y redireccionará a una
success\_url.

![]({{cdn}}/django/images/image328.png)\
![]({{cdn}}/django/images/image761.png)\
![]({{cdn}}/django/images/image465.png)

Ahora si probamos a borrar una página debería indicarnos el template a
crear:

![]({{cdn}}/django/images/image503.png)

Como véis este deberá llamarse page\_confirm\_delete, así que vamos a
crearlo:

![]({{cdn}}/django/images/image611.png)

Como siempre os voy a facilitar el contenido ya creado tomando como
referencia el de la documentación, lo podéis copiar del enlace de
recursos tal y como hago yo:
[https://gist.github.com/hcosta/586f1354e662a25d43a1b2e66403eda9](https://gist.github.com/hcosta/586f1354e662a25d43a1b2e66403eda9) 

Con esto ya podríamos borrar páginas:

![]({{cdn}}/django/images/image208.png)

Como véis en no muchas lecciones hemos aprendido lo esencial sobre las
CBV, hemos creado vistas CRUD para manejar modelos y tenemos todo lo
necesario para gestionar páginas sin necesidad de acceder al panel de
administración.

Por cierto, os comenté que os enseñaría a personalizar el formulario de
las CBV, os lo enseño en la próxima lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>