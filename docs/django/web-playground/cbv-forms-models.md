title: Formularios para Modelos en CBV | Curso de Django | Hektor Profe

# Formularios para Modelos en CBV

Personalizar el formulario enlazado a un modelo es muy fácil. Sólo
tenemos que crear un formulario como hicimos con el de contacto, dentro
del fichero forms.py:

![]({{cdn}}/django/images/image394.png)

Sin embargo en esta ocasión en lugar de definir cada campo a mano, vamos
a hacer que Django los genere automáticamente. Para ello indicaremos el
modelo dentro de una clase Meta, así como la lista campos que queremos
generar y que abstraeremos de la vista:

![]({{cdn}}/django/images/image768.png)

Ahora de vuelta a las vistas que manejan formularios, simplemente
indicaremos el atributo form\_class y le pasaremos este formulario.
Además ahora podemos borrar el campo fields porque ya viene incluido en
el formulario:

![]({{cdn}}/django/images/image461.png)\
![]({{cdn}}/django/images/image475.png)

Si accedemos a la página para crear páginas, valga la redundancia, no
habrá cambiado nada y continuará funcionando sin problemas:

![]({{cdn}}/django/images/image735.png)

Ahora viene la parte interesante,pues al estar trabajando en un
formulario extendido podemos añadir nuestros queridos campos Widget con
configuraciones extendidas:

![]({{cdn}}/django/images/image415.png)\
          ‘content’: ![]({{cdn}}/django/images/image585.png)\
![]({{cdn}}/django/images/image156.png)

También podemos esconder las labels sobreescribiendo el diccionario
labels y poniendo sus valores vacíos:

![]({{cdn}}/django/images/image912.png)

¿Y sabéis lo mejor de todo? Hasta podemos establecer el widget de
CKeditor:

![]({{cdn}}/django/images/image586.png)\
![]({{cdn}}/django/images/image718.png)

Sin embargo no basta sólo con añadirlo en el form, para que aparezca
debemos cargar los ficheros estáticos tal como indican en la
documentación:
[https://github.com/django-ckeditor/django-ckeditor\#outside-of-django-admin](https://github.com/django-ckeditor/django-ckeditor\#outside-of-django-admin) 

Podríamos hacerlo en el pages\_menu.html, a fin de cuentas es sólo
cargar scripts y así lo tendremos centralizado:

![]({{cdn}}/django/images/image540.png)

Con esto tenemos un formulario genial funcionando sin problemas:

![]({{cdn}}/django/images/image313.png)

Sólo nos faltaría corregir pequeños detalles, como poner la disposición
en parágrafos y cambiar el botón de envío por uno más elegante:

![]({{cdn}}/django/images/image337.png)\
![]({{cdn}}/django/images/image177.png)

Ahora un truco de veterano. ¿Os habéis fijado que el widget de CKeditor
no es adaptativo en el ancho? ¿Ni en nuestro editor de páginas, ni
tampoco en el panel de administrador? Para arreglarlo necesitaremos
redefinir el código CSS del widget, pero no os preocupéis porque os voy
a enseñar una forma muy fácil de hacerlo. Os adjunto un Gist con el
código que vamos a modificar, no es mucho.

[https://gist.github.com/hcosta/15ae0835e5824685d46e75f49efc1bcb](https://gist.github.com/hcosta/15ae0835e5824685d46e75f49efc1bcb) 

Lo primero es crear el CSS que sustituirá el del widget original.
Simplemente vamos a crear dentro de la app pages un
directorio static/pages/css con un  fichero llamado por
ejemplo custom\_ckeditor.css. Dentro pondremos lo siguiente:

![]({{cdn}}/django/images/image174.png)

A continuación tendremos que cargar este CSS siempre que mostremos el
editor. Podemos cargarlo de la forma tradicional justo debajo de los
scripts de ckeditor en el page\_menu.html:

![]({{cdn}}/django/images/image263.png)

Si reiniciamos el servidor y recargamos veremos que el textarea ya es
adaptativo:

![]({{cdn}}/django/images/image262.png)

Ahora tenemos que solucionar el del administrador. ¿Habrá alguna forma
fácil o tendremos que modificar los templates? Pues tranquilos, existe
una forma extremadamente sencilla que podemos definir en el propio
admin.py de la app pages:

![]({{cdn}}/django/images/image123.png)

Ahora si volvemos al admin, veréis que también es adaptativo:

![]({{cdn}}/django/images/image238.png)

Ya sólo nos falta adaptar el formulario de UpdateView para que muestre
todo igual que esta:

![]({{cdn}}/django/images/image64.png)

Así como el template (podemos copiar todo el form y sólo cambiar el
texto del botón):

![]({{cdn}}/django/images/image43.png)

Y de igual forma podríamos copiar los estilos del botón para ponerlos en
el formulario de borrado:

![]({{cdn}}/django/images/image745.png)

![]({{cdn}}/django/images/image36.png)

Con esto tenemos todas las vistas CRUD bien bonitas y acabamos esta
interesante lección. En los recursos os dejo los enlaces a la
documentación sobre Formularios y django-ckeditor por si queréis seguir
aprendiendo.

[https://docs.djangoproject.com/en/dev/topics/forms/](https://docs.djangoproject.com/en/dev/topics/forms/)\
[https://github.com/django-ckeditor/django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) 

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>