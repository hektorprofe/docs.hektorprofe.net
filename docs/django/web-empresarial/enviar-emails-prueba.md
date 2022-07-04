title: Enviando emails | Curso de Django | Hektor Profe 

# Enviando emails

Django incluye un módulo dedicado expresamente a manipular y enviar
emails. Dentro encontramos funciones como send\_message para usos
simples o la clase EmailMessage, más sofisticada. Nosotros utilizaremos
la segunda forma, ya que nos permite establecer fácilmente un
reply\_email, o email de respuesta, ya lo veréis.

Antes de nada para enviar emails necesitamos configurar una cuenta de
correo.

Podríamos estar horas y horas hablando sobre como configurar diferentes
correos con sus diferentes protocolos pero eso sería un lío.

Lo que os recomiendo es registrarnos en un proveedor como mailtrap, ya
que nos permite crear cuentas de correo gratuitas para realizar pruebas,
y además funciona en Django sin problemas. Luego en la práctica cada uno
deberá configurar su cuenta, os dejaré la documentación:

[https://docs.djangoproject.com/en/dev/topics/email/](https://docs.djangoproject.com/en/dev/topics/email/)


Una vez establecida la configuración de una forma segura estamos listos
para ir a la vista y enviar un nuestro correo de contacto utilizando la
función send\_mail.

Primero importaremos la función y el EMAIL que utilizaremos para enviar
el correo, tomado del propio settings.py:

![]({{cdn}}/django/images/image79.png)

Luego creamos la estructura del correo utilizando la clase EmailMessage
(os adjunto la documentación relacionada):\
[https://docs.djangoproject.com/en/dev/topics/email/\#emailmessage-objects](https://docs.djangoproject.com/en/dev/topics/email/\#emailmessage-objects) 

DONDE EMAIL\_HOST\_USER -\> EMAIL DEL QUE ENVIA

![]({{cdn}}/django/images/image288.png)

Cuando la tenemos, utilizamos el método send() para enviarlo. Podemos
detectar algún fallo con un bloque try except y redireccionar tanto si
funciona bien como si falla:

![]({{cdn}}/django/images/image159.png)

Sólo deberíamos modificar el template y detectar si en request.GET está
el parámetro FAIL para mostrar un mensaje clásico de  “Error enviando el
formulario, prueba más tarde”, pero eso os lo dejo a vosotros.

Vamos a probar si se envía el correo:

![]({{cdn}}/django/images/image39.png)

![]({{cdn}}/django/images/image432.png)

![]({{cdn}}/django/images/image438.png)

Y bien, por lo menos a mi me ha funcionado sin problemas.

Evidentemente en la vida real no se recomienda utilizar un email de
Google, sobretodo si vamos a enviar muchos correos, pero para una web
sencilla puede servir perfectamente.

Con esto tenemos el proyecto prácticamente terminado, sólo faltan
algunos ajustes en el admin para prevenir ciertas acciones por parte de
nuestros clientes, os lo cuento en detalle en la próxima lección.

Así que, suponiendo que ya tenéis una cuenta de Gmail, aunque sea de
prueba, vamos a empezar generando una clave de aplicación. Esto es
necesario porque por seguridad Gmail no nos deja identificarnos con
nuestra en aplicaciones externas, necesitamos un token. El primer paso
es ir a nuestra cuenta de Google desde cualquier web de Google:

![]({{cdn}}/django/images/image724.png)

Vamos al apartado Inicio de sesión y seguridad \> Contraseñas de
aplicación

![]({{cdn}}/django/images/image787.png)

Aquí generaremos una contraseña para Correo, podemos darle el nombre
Django Test Email:\
        ![]({{cdn}}/django/images/image305.png)

![]({{cdn}}/django/images/image4.png)

Una vez la tengamos la dejáis reservada, luego la utilizaremos.

![]({{cdn}}/django/images/image360.png)

El siguiente paso es configurar el email en el fichero  settings.py.
Debéis poner exactamente esto:

![]({{cdn}}/django/images/image748.png) 

Ahora viene cuando la matan, tenemos que configurar los campos.

El problema que tiene esto, es que no es el tipo de información que
podemos poner en cualquier sitio.

Algunos desarrolladores cuando tienen que utilizar información
confidencial optan por crear lo que se conoce como variables de entorno.
Es una práctica válida y recomendada, pero no vamos a utilizarla en este
curso. En su lugar os voy a enseñar a crear un fichero de configuración
externo y a cargarlo en Django para hacer uso de sus datos.

Vamos a crear un fichero de configuración JSON, un formato de
serialización de datos bastante común hoy en día. Nosotros lo vamos a
crear en el directorio raíz del proyecto, pero si lo váis a utilizar en
producción os sugiero ponerlo en otro directorio del equipo, y
sobretodo, no publicarlo nunca en un repositorio público.

A este fichero lo llamaremos email\_settings.json:

![]({{cdn}}/django/images/image224.png)

Dentro escribiremos la siguiente estructura, muy similar a un
diccionario de Python (atención a true y no True):

![]({{cdn}}/django/images/image298.png)

Una vez lo tengamos vamos a settings.py y lo cargaremos utilizando el
módulo json de python de la siguiente forma:

![]({{cdn}}/django/images/image251.png)\
![]({{cdn}}/django/images/image739.png)


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>