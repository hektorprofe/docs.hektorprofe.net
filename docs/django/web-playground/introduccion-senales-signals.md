title: Introducción a las señales | Curso de Django | Hektor Profe

# Introducción a las señales

El primer detalle que vamos a solucionar es la prevención de un
potencial error que podría hacer tambalear toda nuestra página, y ese es
el momento de crear un perfil.

Tal y como lo tenemos ahora, siempre que un usuario se registre y se
identifique será redireccionado directamente a su perfil, de manera que
se creará la instancia enlazada. Pero, ¿qué ocurriría si por alguna
razón el usuario se registra y no accede nunca? Pues que nos quedará un
usuario sin perfil, una situación tendiente a errores en el futuro.

Así que vamos a solucionar esta situación introduciendo algo muy
interesante conocido como Signals o Señales.

Una señal es un disparador que se llama automáticamente después de un
evento que ocurre en nuestro ORM. En nuestro caso lo que haremos es
crear automáticamente un perfil justo después de que se cree un usuario,
y así estaremos 100% seguros de que todos los usuarios cuentan con un
perfil desde el primer momento.

Crear una señal es relativamente fácil, lo haremos en el fichero
registration/models.py:

Dentro vamos a crear una función que enlazaremos a través de una señal
al modelo User justo después de crear un usuario, tiene que recibir un
sender, una instance y los kwargs. Instance hace referencia al objeto
que envía la señal, y que en nuestro caso será el usuario recién creado,
así que simplemente creamos el perfil y nos quedamos tan anchos:

![]({{cdn}}/django/images/image648.png)

Ahora debemos debemos transformar la función en una señal. Lo haremos
con el decorador @receiver, al cual le pasaremos un tipo de señal, en
nuestro caso post\_save (después del guardado),  y un sender, que
corresponderá al modelo encargado de enviar la señal, en nuestro caso
User:

![]({{cdn}}/django/images/image894.png)\
![]({{cdn}}/django/images/image499.png)

Con esto ya lo tenemos, pero hay que tener en cuenta que esta señal se
ejecutará siempre que se guarde la instancia, ¿habrá alguna forma de
ejecutar la consulta sólo cuando se crea por primera vez? Pues sí. Si
comprobamos del diccionario kwargs la clave created, esta debería
devolver True si justo después de crearse la instancia se ha llamada a
la señal. Si no existe devolveremos False por defecto:

![]({{cdn}}/django/images/image507.png)

Vamos a registrar un nuevo usuario a ver si funciona ha creado su
perfil...

![]({{cdn}}/django/images/image802.png)

![]({{cdn}}/django/images/image612.png)

Pues parece que sí, pero para estar seguros vamos a meternos un momento
en la shell y a consultarlo manualmente. La shell es un entorno python y
django dentro de nuestro proyecto, de manera que podemos interactuar en
tiempo real a través de instrucciones:

![]({{cdn}}/django/images/image483.png)

Como véis el objeto existe, por lo que podemos afirmar que efectivamente
se ha creado el perfil.

Sin embargo utilizar la shell para hacer estas comprobaciones muy
tedioso, en la siguiente lección vamos a ver cómo realizar una prueba
unitaria que cree un usuario y después compruebe que se ha creado el
perfil.

Por cierto, también existen las señales pre\_save, pre\_delete y
post\_delete, pero como nosotros necesitamos que el usuario ya exista,
hemos utilizado post\_save. Para más información podéis consultar la
documentación sobre señales, os la dejo en los recursos:
[https://docs.djangoproject.com/en/dev/topics/signals/](https://docs.djangoproject.com/en/dev/topics/signals/) 


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>