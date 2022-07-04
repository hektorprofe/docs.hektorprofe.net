title: Procesado y validación | Curso de Django | Hektor Profe 

# Procesado y validación

Ya tenemos el formulario pero todavía le faltan algunos campos para
poder funcionar, vamos a ello.

Lo primero es configurarlo correctamente, así que vamos a envolver un
tag \<form\> y a configurar su acción y método:

![]({{cdn}}/django/images/image371.png)

Hay dos métodos para enviar un formulario: POST y GET. El método GET es
visible a simple vista, se añade a la URL de la petición con un
interrogante al final. A nosotros no nos interesa que las peticiones se
vean en la barra de direcciones, por eso vamos a utilizar el método POST
que se envía oculto:

En cuanto al atributo action sería la página donde enviamos el
formulario,  al no establecer ningún valor, se interpretará que la
petición POST debe realizarse contra la página actual, que en nuestro
caso será /contact/ de la web.

Si intentamos enviar el formulario, como hemos indicado que los campos
son obligatorios (con el atributo required=True) algunos navegadores nos
maneja una prevalidación automática:

![]({{cdn}}/django/images/image908.png)

Cuando consigamos enviar el formulario nos aparecerá un error:

![]({{cdn}}/django/images/image504.png)

Nos devuelve un error de verificación CSRF fallida (el token CSRF se ha
perdido o es incorrecto). ¿Qué es esto del token CSRF? Pues ni más ni
menos que un sistema de seguridad. CSRF son las siglas de Cross-site
request forgery , en español: Falsificación de petición en sitios
cruzados.

¿Para qué sirve? Pues para prevenir que una página web pueda enviar
información a nuestros formularios desde un dominio externo. Os
adjuntaré en los recursos el enlace a la Wikipedia por si queréis una
explicación más
detallada. [https://es.wikipedia.org/wiki/Cross-site\_request\_forgery](https://es.wikipedia.org/wiki/Cross-site\_request\_forgery)

Para solucionar el error debemos generar un token CSRF dentro del
formulario de la siguiente forma:

 ![]({{cdn}}/django/images/image20.png)

Si recargamos la página a simple vista no habrá cambiado nada, pero si
observamos el código veremos un campo hidden (oculto) con el token:

![]({{cdn}}/django/images/image44.png)

Ahora si volvemos a enviar el formulario, como podréis observar no
ocurre nada, pero eso no significa que no se esté enviando, sólo que no
lo vemos porque el método es POST. Si cambiamos un momento a GET veréis
como se envíanen la barra de direcciones:

![]({{cdn}}/django/images/image416.png)

Vamos a dejarlo como estaba:

![]({{cdn}}/django/images/image129.png)

Para que veais que no os miento, haced lo siguiente:

![]({{cdn}}/django/images/image84.png)

Así debugearemos los datos POST de la petición:

![]({{cdn}}/django/images/image647.png)

Queda demostrado entonces que estamos enviando datos a la vista a través
de la petición, ahora sólo nos falta manipularlos en nuestra vista para
procesarlos y enviar el email.

¿Recordáis que en todas las vistas siempre estamos tomando un parámetro
request en la primera posición? Pues, de la misma forma que hemos hecho
en el template también podemos acceder a los datos POST.

Sin embargo, antes de lanzarnos a manipular estos datos  debemos estar
seguros de que ha ocurrido una petición POST. Poned esto en la vista:

![]({{cdn}}/django/images/image680.png)

Ahora si cargamos nuestra página y observamos la terminal, veremos el
tipo de petición que se realiza. Si es la página normal recibimos una
petición GET:

![]({{cdn}}/django/images/image754.png)

En cambio si enviamos el formulario:

![]({{cdn}}/django/images/image649.png)

Por tanto la respuesta a la pregunta, ¿cuándo procesaremos el
formulario? está clara “Sólo cuando detectemos una petición POST”:

![]({{cdn}}/django/images/image721.png)

Una vez estamos seguros de que se ha enviado el formulario, lo que
haremos es rellenarlo con los datos que se envían. Es fácil, sólo
debemos hacer lo siguiente:

![]({{cdn}}/django/images/image237.png)

Únicamente habiendo hecho este cambio, si enviamos el formulario, veréis
que éste queda rellenado con los campos que se le envían:

![]({{cdn}}/django/images/image86.png)

Una utilidad relacionada con ésto es que si algún campo no valida bien,
por lo menos el usuario no deberá introducir de nuevo todo desde el
principio, pero esa no es su razón de ser.

Haber rellenado el formulario nos permite comprobar si todos los campos
son válidos:

![]({{cdn}}/django/images/image741.png)

Si todos los campos son válidos procederemos a recuperarlos. Como
request.POST no deja de ser un diccionario, una forma segura de hacerlo
es utilizar su método get que permite devolver un valor por defecto:

![]({{cdn}}/django/images/image459.png)

En este punto ya tenemos la información recuperada en la vista, así que
procederemos a enviar el email, pero esto lo dejo para más adelante.

Por ahora vamos a suponer que todo ha ido bien y debemos informar al
usuario de que su mensaje se ha enviado correctamente. Esto lo podemos
hacer fácilmente. En lugar de renderizar el template de contacto podemos
hacer un redireccionamiento enviando una variable OK por GET a la propia
página /contact/.

Para redireccionar tenemos a nuestra disposición la función redirect:

![]({{cdn}}/django/images/image675.png)

Y podríamos simplemente hacer lo siguiente:

![]({{cdn}}/django/images/image610.png)

Esto está bien, pero ya sabéis que no me gusta poner cadenas en crudo,
es una mala práctica. Por ello voy a introducirs brevemente la función
reverse(), que es igual que {%raw%}`{% url %}`{%endraw%} en los templates:

![]({{cdn}}/django/images/image758.png)\
![]({{cdn}}/django/images/image390.png)

Hacedme caso, parece tedioso pero es una muy buena práctica dejar que
Django resuelva él mismo las URL que tenemos definidas en los Paths.

Ahora que tenemos la redirección, vamos a enviar el formulario y como
véis nos recarga la página pasando este OK en la parte superior.

![]({{cdn}}/django/images/image573.png)

Ahora en el template podemos comprobar si existe esta variable GET ‘ok’
en el diccionario request.GET, y si es así mostrar un mensaje que diga
“Su mensaje se ha enviado correctamente etc.”:

![]({{cdn}}/django/images/image109.png)\
![]({{cdn}}/django/images/image744.png)

El formulario está casi listo, pero visualmente no tiene nada que ver
con el que teníamos maquetado. En la siguiente lección os enseñaré como
adaptar un diseño en lugar de utilizar el que genera Django
automáticamente.


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>