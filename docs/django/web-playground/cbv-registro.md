title: Registro con CBV (1) | Curso de Django | Hektor Profe

# Registro con CBV (1)

La parte del registro no es tan simple como la autenticación, para ello
sí que debemos crear una vista y manejar nosotros la lógica, pero Django
nos ayudará bastante, ya veréis.

Antes de nada vamos a incluir las URLS de registration en el urls.py
 global y así nos olvidamos de ello:

![]({{cdn}}/django/images/image466.png)

Fijaros que las añadiremos justo debajo de las que hicimos para la
autenticación. Esto no es ningún problema, ya que simplemente se
extenderán las que teníamos antes.

Bien, ahora vamos a crear nuestra vista SignUp para manejar el registro.
Fijaros muy bien lo que vamos a hacer:

![]({{cdn}}/django/images/image53.png)

En lugar de crear un formulario desde cero lo que haremos es importar
uno genérico (UserCreationForm) y se lo pasaremos a una vista CreateView
para que lo maneje todo automáticamente, por eso os decía que Django nos
ayudaría bastante.

Vamos a crear el formulario. En este caso no he preparado un diseño de
antemano porque quiero enseñaros cómo modificarlo dinámicamente, así que
vamos a tomar de referencia el de registro y modificarlo:

![]({{cdn}}/django/images/image495.png)

Finalmente configuraremos la URL, vamos a crear un fichero urls.py:

![]({{cdn}}/django/images/image746.png)

Ahora sólo tenemos que acceder a accounts/signup y ver la magia:

![]({{cdn}}/django/images/image65.png)

![]({{cdn}}/django/images/image388.png)

¡Increíble! ¿Funcionará?

![]({{cdn}}/django/images/image845.png)

Pues parece que sí, porque nos ha redireccionado a login.

Os aconsejo redireccionar a otra página o hacer la típica modificación
pasando un parámetro GET, por lo menos así añadimos retroalimentación al
usuario. Por desgracia no podemos concatenar en el success\_url así que
deberemos sobreescribir el método get\_success\_url y devolver nuestra
cadena desde ahí:

![]({{cdn}}/django/images/image658.png)

![]({{cdn}}/django/images/image618.png)

Probamos de nuevo:

![]({{cdn}}/django/images/image593.png)

Bien, vamos a mejorar la apariencia del formulario. Podríamos editar el
HTML pero perderíamos un montón de validaciones automáticas, así que
vamos a aprovecharnos de esta vista que tenemos para modificar los
widgets en tiempo de ejecución. Para hacerlo debemos saber qué nombre
tienen los campos, así vamos a observar el formulario generado y los
atributos name de los inputs:

![]({{cdn}}/django/images/image578.png)

En nuestro caso el formulario tiene tres: username, password1 y
password2.

Sabiendo esto vamos a la vista y haremos lo siguiente para recuperar el
formulario:

![]({{cdn}}/django/images/image690.png)

El método get\_form obtiene el formulario antes de devolverlo, de manera
que podemos modificar sus widgets. Fijaros:

![]({{cdn}}/django/images/image215.png)\
![]({{cdn}}/django/images/image334.png)\
![]({{cdn}}/django/images/image334.png)

![]({{cdn}}/django/images/image255.png)

Ya sólo tenemos que esconder las labels, podríamos hacerlo de forma
similar a como hemos cambiado los widgets… pero es mucho más rápido ir
al template y añadir una tag \<style\> para esconderlas todas de golpe:

![]({{cdn}}/django/images/image696.png)

![]({{cdn}}/django/images/image491.png)

Finalmente para dejarlo perfecto podríamos añadir el enlace al registro
en el menú superior:

![]({{cdn}}/django/images/image751.png)\
![]({{cdn}}/django/images/image115.png)

Con esto tenemos un registro básico para seguir trabajando en las
próximas lecciones.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>