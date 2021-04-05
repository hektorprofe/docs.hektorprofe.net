title: Introducción a las pruebas unitarias | Curso de Django | Hektor Profe

# Introducción a las pruebas unitarias

Vamos a crear una prueba muy simple, ésta creará un usuario de pruebas y
luego comprobará que existe su perfil, si existe pasará el test y si no
fallará.

Para crear un test iremos al fichero tests.py de la app registration.
Ahí veremos que por defecto hay una clase cargada llamada TestCase,
vamos a cargar nuestros modelos User y Profile.

![]({{cdn}}/django/images/image576.png)

Ahora vamos a crear la clase con las pruebas:

![]({{cdn}}/django/images/image184.png)

El método setUp de TestCase es donde haremos la preparación, y luego
tenemos un método propio, test\_profile\_exists, donde definiremos el
test. Puede tener cualquier nombre siempre que empiece por test\_.

La preparación es muy simple, sólo debemos crear un usuario de pruebas:

![]({{cdn}}/django/images/image664.png)

Normalmente los objetos se crean con su método create, pero el caso de
User es especial, ya que contiene un método create\_user encargado de
cifrar la contraseña por nosotros.

Ahora vamos a definir el test. Se supone que en este punto el usuario
creado existirá, así que podemos comprobar que haya un perfil con ese
usuario:

![]({{cdn}}/django/images/image506.png)

La prueba en sí misma es muy sencilla, solo hacemos un assertEqual para
comprobar que exists sea True.

Y ahora ¿como la ejecutamos? Pues desde el manage.py haremos:

![]({{cdn}}/django/images/image471.png)

Como véis se ha creado una base de datos de prueba, casualmente también
llamada test, se ha ejecutado 1 test y ha devuelto OK. Luego se ha
borrado la base de datos de prueba, así que no queda ni rastro del
usuario test.

Con esto lo tenemos perfecto y podemos estar seguros de que nunca
quedará un usuario sin perfil.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>