title: Mensajes asíncronos con JS (1): Primer concepto | Curso de Django | Hektor Profe

# Mensajes asíncronos con JS (1): Primer concepto

El formulario de mensajes tiene la estructura más simple del mundo, un
único campo con un texto. ¿Vale la pena diseñar un form para eso? Pues
no. Además es una ocasión excelente para enseñaros a trabajar con
peticiones asíncronas.

¿Qué es una petición asíncrona? Para entenderlo podemos simplemente
tomar un ejemplo real. Imaginaros un usuario navegando por una página
web. En un momento dado decide cambiar de sección y hace clic en un
enlace. Al hacerlo, se hace una petición al servidor para que éste
devuelva la nueva página.

-   Si este proceso es síncrono, al hacer la petición el cliente queda
    en un limbo esperando la respuesta, digamos que se sincroniza con el
    servidor. Si el servidor tarda 5 segundos en devolver la nueva
    página, serán 5 segundos que el cliente estará bloqueado esperando
    la respuesta.
-   En cambio, si este proceso es asíncrono, el cliente pide la página
    pero puede seguir funcionando. En otras palabras, la petición ocurre
    en segundo plano sin que el cliente se percate de ello, y únicamente
    será consciente al recibirse la respuesta.

Este tipo de peticiones son muy útiles porque no requieren recargar toda
la página, sino que se puede modificar sólo una sección determinada en
función de la respuesta, haciendo la experiencia mucho más fluida. Sin
duda la forma ideal para enviar mensajes sin que el usuario deba
recargar toda la página.

¿Pero cómo se logra este comportamiento? Pues gracias al lenguaje
Javascript, que es capaz de crear un objeto en memoria donde manejar la
petición, capturar la respuesta y modificar el DOM, la interfaz que
permite modificar el contenido del HTML en tiempo real.

Pero basta de introducciones y vamos a entrar en materia, empezando por
identificar qué datos necesitamos para crear un mensaje y cómo podemos
enviarlos a una vista clásica:

-   El hilo: lo pasaremos en el PATH de la petición con una variable pk
-   El usuario: ya lo tenemos en la propia petición request
-   El contenido: lo enviaremos en una petición GET

Podríamos enviarlo en una petición POST, pero como requiere el token
csrf es más fácil hacerlo por GET.

Así que vamos a crear la vista:

![]({{cdn}}/django/images/image68.png)

El respectivo PATH quedaría así:

![]({{cdn}}/django/images/image580.png)\
![]({{cdn}}/django/images/image906.png)

Si accedemos a nuestra nueva vista nos dará error porque no estamos
devolviendo nada:

![]({{cdn}}/django/images/image18.png)

¿Qué tenemos que devolver en una petición asíncrona? Pues lo que
queramos, puede ser texto plano, un snippet HTML para inyectarlo
directamente en la página, o una estructura bien organizada en formato
XML o JSON que podemos analizar para actuar en consecuencia.

Mi recomendación es responder siempre con estructuras JSON, unos objetos
muy parecidos a un diccionario de Python pero escritos con la sintaxis
de Javascript, algo muy útil, porque como la propia petición se realiza
en Javascript, la respuesta se puede manejar al vuelo sin hacer
conversiones.

Para poder devolver una respuesta JSON necesitamos importar el módulo
JsonResponse:

 ![]({{cdn}}/django/images/image869.png)

Ahora crearemos la respuesta como si fuera un diccionario Python
indicando que inicialmente no se ha creado el mensaje y la
transformaremos a JSON para devolverla:

![]({{cdn}}/django/images/image130.png)

Si actualizamos la página funcionará mostrando nuestro diccionario:

![]({{cdn}}/django/images/image227.png)

Sin embargo fijaros bien en el resultado, pues se trata de un objeto
JSON y no un diccionario de Python. Es prácticamente igual pero cambia
el booleano False con la f en minúscula porque en Javascript se escribe
de esa forma.

Lo bueno es que este objeto ya es reconocible por Javascript, por lo que
podemos empezar a desarrollar la parte del formulario. Luego ya
volveremos a nuestra vista.

Vamos a empezar haciendo un experimento, a ver si somos capaces de hacer
una petición asíncrona a la vista add\_message presionando un botón y
mostrando el resultado en pantalla.

Dado que prácticamente todos los navegadores implementan las funciones
de ECMA Script 6, para hacer una petición asíncrona ya no es necesario
hacer malabarismos ni utilizar librerías como jQuery.  Sólo debemos
utilizar la función fetch, la cual toma una url para hacer la petición y
también es capaz de manejar la respuesta:

Explicar línea a línea el experimento, separar fetch de .then, .then:

![]({{cdn}}/django/images/image791.png)

![]({{cdn}}/django/images/image442.png)\
![]({{cdn}}/django/images/image669.png)

¡Perfecto! Como véis obtenemos el valor de created en una alerta.

Ahora viene lo bueno, necesitemos capturar el contenido del mensaje y
enviarlo a la vista al presionar el botón.

Todo eso lo haremos en la siguiente lección que es una continuación de
esta, pero para que os hagáis una idea vamos a hacer una simulación. En
nuestra vista mostraremos un print de los parámetros GET:

![]({{cdn}}/django/images/image882.png)

Y crearemos un contenido de prueba que concatenaremos como parámetro GET
a la url:

![]({{cdn}}/django/images/image38.png)

Al presionar el botón nos aparecerá en el debug:

![]({{cdn}}/django/images/image479.png)

Bueno, pues como os decía, en la siguiente lección crearemos un textarea
y tomaremos este contenido de ahí.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>