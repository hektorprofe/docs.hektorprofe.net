title: Optimizando el almacenamiento del avatar  | Curso de Django | Hektor Profe

# Optimizando el almacenamiento del avatar 

El último detalle que os sugiero optimizar es la forma de almacenar el
avatar de usuario. No sé vosotros, pero yo he estado haciendo un montón
de pruebas y se me han guardado un montón de imágenes diferentes:

![]({{cdn}}/django/images/image412.png)

Obviamente no nos interesa almacenar todos los avatares de cada usuario,
sería un despilfarro de espacio, y el espacio vale dinero. Vamos a
almacenar sólo la imagen más reciente. Para lograrlo vamos a crear
nuestro propio update\_to en forma de función. Dentro recuperaremos el
antiguo avatar y lo borraremos haciendo uso de su útil método delete,
que comparten ambos ImageField y FileField. Justo después devolveremos
la ruta al fichero de la forma normal:

![]({{cdn}}/django/images/image75.png)

De esta forma nos aseguraremos de almacenar una y solo una imagen por
usuario, optimizando mucho la memoria. Probadlo, borrad todas las
imágenes del directorio profiles y fijaros como siempre que añadimos una
se borra la anterior:

![]({{cdn}}/django/images/image629.png) 

Con esto damos por finalizado el formulario de perfil. La siguiente
lección es una práctica en la que deberás crear una nueva app para
mostrar los perfiles de forma pública.

Si queréis más información sobre la creación de funciones para
upload\_to os dejo el enlace oficial en los recursos:
[https://docs.djangoproject.com/en/dev/ref/models/fields/\#django.db.models.FileField.upload\_to](https://docs.djangoproject.com/en/dev/ref/models/fields/\#django.db.models.FileField.upload\_to) 

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>