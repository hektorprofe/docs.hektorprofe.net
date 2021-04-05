title: Personalizando el administrador (4) | Curso de Django | Hektor Profe 

# Personalizando el administrador (4)

Nuestra web está acabada, pero debemos tener en cuenta un detalle
importante,y es que nuestros clientes no deberían tener permisos para
gestionar algunas partes del panel de administrador. Puede sonar cruel,
pero hay que pensar en el cliente como alguien… vamos a decir
despistado, al que si le decimos que no haga algo seguro que lo acaba
haciendo, os lo digo con total seguridad.

Por tanto como dice el dicho, ojos que no ven corazón que no siente, y
por tanto más que advertirle lo que haremos es esconder las partes
peligrosas. Para lograrlo vamos a introducir el uso de los grupos y
permisos de usuario.

Vamos a ir a nuestro panel de administrador con nuestro superusuario y
vamos a ir al apartado grupos. Crearemos un nuevo grupo llamado
“personal”. Supondremos que es para el personal de la empresa.

Los permisos se gestionan de la siguiente forma. Para cada modelo hay
tres permisos: añadir, editar y borrar. Es tan sencillo como seleccionar
los permisos que queremos dar a los miembros del grupo y ponerlos en el
lado derecho, podemos hacer doble clic o seleccionar varios con Shift o
Control y presionar el botón de la flecha hacia la derecha.

Para los miembros del grupo Personal vamos a añadir los siguientes
permisos:

-   App Blog: Todos los permisos para los modelos Categoría y Entrada
-   App Pages: Todos los permisos para el modelo Página
-   App Services:Todos los permisos para el modelo Servicio
-   App Social: Permiso de edición para el modelo Enlace

En resumen, dejaremos que el usuario maneje completamente el blog y las
páginas secundarias, pero los servicios y los enlaces sociales los
restringimos para que no pueda añadir de nuevos ni borrar los actuales:

![]({{cdn}}/django/images/image665.png)

Ahora tenemos que crear un usuario y añadirlo a este grupo. Podemos
llamarlo test:

![]({{cdn}}/django/images/image891.png)

Deberemos marcarlo como STAFF para que tenga acceso al admin, y añadirlo
al grupo de Personal:

![]({{cdn}}/django/images/image141.png)

Como podéis observar se pueden configurar varios campos y permisos
específicos para el usuario, yo os recomiendo gestionar un grupo porque
es más cómodo.

Vamos a entrar con este usuario test a ver qué nos aparece:\
![]({{cdn}}/django/images/image324.png)

Todo lo tenemos perfecto excepto por una cosa.

En la App Social, estamos permitiendo que el usuario pueda cambiar la
CLAVE y el NOMBRE de la red. Dentro de lo que cabe el nombre no importa
mucho, pero la CLAVE la utilizamos directamente en el template, así que
no podemos dejarle editarla.

Los permisos nos pueden ayudar a nivel de Modelo, pero no de campos, así
que tendremos que encontrar una forma de por lo menos hacer el campo
“sólo de lectura” a los miembros del grupo “Personal”.

¿Recordáis cómo hicimos que un campo fuera sólo de lectura? Teníamos que
editar crear una tupla o lista llamada readonly\_fields en el admin del
modelo. Claro, esto no podemos hacerlo porque es común para todos los
usuarios, pero hay una forma de extenderlo: crear un método
get\_readonly\_fields capaz de detectar el usuario identificado durante
la petición y sobreescribir su valor:

![]({{cdn}}/django/images/image814.png)

De esta manera, si detectamos que el usuario actual forma parte del
grupo Personal, le cambiamos dinámicamente los campos key y name como
sólo lectura. Y si no devolvemos una tupla vacía indicando que puede
editarlos todos (demo).

La mayoría de campos del ModelAdmin se pueden sobrescribir en tiempo de
ejecución con sus respectivos métodos, yo suelo utilizar mucho el
get\_exclude, que permite esconder campos en lugar de ponerlos sólo de
lectura. Os dejaré un enlace a la documentación por si queréis
investigar.

[https://docs.djangoproject.com/en/dev/ref/contrib/admin/\#modeladmin-methods](https://docs.djangoproject.com/en/dev/ref/contrib/admin/\#modeladmin-methods) 

Y ya está, sólo quiero daros la enhorabuena por haber completado el
segundo proyecto del curso. Deseo de corazón que hayáis aprendido mucho
y podáis ponerlo todo en práctica en vuestros proyectos.

Nos vemos en el próximo.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>