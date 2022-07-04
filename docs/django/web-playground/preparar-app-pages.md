title: Preparando la App (Pages)  | Curso de Django | Hektor Profe

# Preparando la App [Pages] 

Muy bien! Para seguir aprendiendo más sobre las Vistas basadas en Clases
he preparado también una copia de nuestra app Pages para hacerle una
revisión. Descargadla en los recursos y descomprimidla en vuestro
proyecto.

Para utilizarla simplemente la activaremos en settings.py,
configuraremos las urls.py y a migraremos la base de datos sin olvidar
crear un superusuario para poder acceder al panel de administrador
(desde nuestro entorno virtual django2).

![]({{cdn}}/django/images/image315.png)\
![]({{cdn}}/django/images/image781.png)\
![]({{cdn}}/django/images/image122.png)\
![]({{cdn}}/django/images/image457.png)\
![]({{cdn}}/django/images/image30.png)\
![]({{cdn}}/django/images/image632.png)

Ahora para acceder a nuestra app vamos a modificar el enlace a la página
de prueba por el de esta app pages, simplemente podríamos cambiar el
enlace a /páginas/ en el menú, ahí tengo una vista que muestra nuestras
páginas y un pequeño extracto de su contenido (borrar la de ejemplo y
dejar esta):

![]({{cdn}}/django/images/image92.png)\
![]({{cdn}}/django/images/image135.png)

Por cierto, si os preguntáis porque he creado esta vista es para
trabajar un tipo concreto de CBV, luego cuando la adaptemos lo
veréis. En cualquier caso estoy devolviendo un error 404 si no hay
ninguna página, por lo que nos dará error si intentamos acceder:\
![]({{cdn}}/django/images/image522.png)\
![]({{cdn}}/django/images/image307.png)

Vamos a crear algunas páginas de prueba:

![]({{cdn}}/django/images/image624.png)

Fijaros que al intentar crear una página nos da error de ckeditor,
claro, aunque la tengamos instalada en el entorno virtual no la hemos
instalado en settings.py:

![]({{cdn}}/django/images/image436.png)\
![]({{cdn}}/django/images/image858.png)

Ahora sí ya debería funcionar la App:

![]({{cdn}}/django/images/image223.png)\
![]({{cdn}}/django/images/image605.png)

![]({{cdn}}/django/images/image199.png)

![]({{cdn}}/django/images/image70.png)

Con esto tenemos el terreno preparado y en la próxima lección
aprenderemos cómo utilizar dos nuevas CBV.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>