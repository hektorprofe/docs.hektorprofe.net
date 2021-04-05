title: Restaurar contraseña | Curso de Django | Hektor Profe

# Restaurar contraseña

Los usuarios son despistados por naturaleza, se registran en muchos
sitios y luego no recuerdan sus credenciales, así que es necesario
proveerles de una forma para recuperar su cuenta en caso de que olviden
su contraseña. Sin embargo para que puedan hacerlo es necesario que
cuenten con su correo electrónico enlazado al usuario, y esa es la razón
por la que nos hemos pasado las últimas dos lecciones configurando el
email en el registro.

Así que lo primero será configurar una cuenta de correo en Django como
hicimos durante la web empresarial para enviar correos de prueba,
podríamos volver a utilizar vuestra bandeja de Mailtrap, pero en esta
ocasión os voy a mostrar una alternativa por si algún día no contáis con
Internet, se trata de configurar un servidor SMTP para pruebas, éste
hará ver que envía los correos pero en realidad los guardará en forma de
ficheros dentro de un directorio, vamos a configurarlo:

![]({{cdn}}/django/images/image161.png)

De esta forma nuestros emails se crearán en un nuevo directorio llamado
sent\_emails, obviamente podéis poner cualquier otro nombre. Por cierto,
si en lugar de crear ficheros queréis mostrar los correos por la
terminal también podéis, sólo tenéis que cambiar filebased por console.
Os adjunto documentación por si queréis aprender otras opciones de
configuración:
[https://docs.djangoproject.com/en/dev/topics/email/\#console-backend](https://docs.djangoproject.com/en/dev/topics/email/\#console-backend) 
[https://docs.djangoproject.com/en/dev/topics/email/\#smtp-backend](https://docs.djangoproject.com/en/dev/topics/email/\#smtp-backend) 

Ahora antes de ponernos manos a la obra, dejadme deciros que este
proceso de restauración ya nos funciona, lo está gestionando el panel de
administrador automáticamente. Probad a acceder la URL de restauración
/accounts/password\_reset/:

![]({{cdn}}/django/images/image637.png)

Si ya os está bien que aparezca el admin podríais dejarlo así, pero creo
que es más interesante utilizar nuestros propios templates. Así que
tendremos que empezar diciéndole a Django que dé prioridad a los
templates de la app Registration antes que los del panel de admin.
Simplemente debemos poner nuestra app por delante en settings.py:

![]({{cdn}}/django/images/image248.png)

Si no hacéis este cambio nunca os aparecerán vuestros propios templates.

Bien, vamos a por esta primera página password\_reset. Lo único que
debemos hacer es crear nuestra propia versión del template bajo el
nombre password\_reset\_form.html. Como tendremos que crear varios os
los voy a adjuntar todos en un descargable descargar este y todos los
demás en los recursos.

![]({{cdn}}/django/images/image531.png)

Una vez tengáis los nuevos templates en el
directorio /templates/registration/ si accedemos de nuevo….

![]({{cdn}}/django/images/image860.png)

Ahora si introducimos un correo, esté o no enlazado a un usuario, se
redireccionará a una página de confirmación en la url
[password\_reset/done/](password\_reset/done/),
probad con uno de mentira:

![]({{cdn}}/django/images/image844.png)

![]({{cdn}}/django/images/image736.png)

Ahora repetid el proceso pero utilizando un email real que hayáis
utilizado para registraros anteriormente, se os debería crear el
directorio sent\_mails en la raíz del proyecto:

![]({{cdn}}/django/images/image737.png)

Lo que tendremos dentro es un fichero con el email que “en teoría” se ha
enviado al usuario. Si lo abrimos podremos seguir las instrucciones:

![]({{cdn}}/django/images/image336.png)

Como véis se envía un enlace con un token para recuperar la contraseña,
así como un recordatorio del nombre del usuario. Vamos a abrir ese
enlace a ver qué nos aparece:

![]({{cdn}}/django/images/image789.png)

Como véis aquí tenemos el formulario de restauración que se toma del
template password\_reset\_confirm.html, en él debemos introducir la
contraseña nueva dos veces. Probad a poner una contraseña numérica o
equivocaros aposta, os deberían aparecer los errores de validación, y si
ponéis una correcta nos llevará a la última pantalla que nos falta por
ver, password\_reset\_complete:

![]({{cdn}}/django/images/image349.png)

Si tenéis curiosidad sobre cómo son los templates originales os voy a
dejar un enlace al repositorio oficial:
[https://github.com/django/django/tree/master/django/contrib/admin/templates/registration](https://github.com/django/django/tree/master/django/contrib/admin/templates/registration) 

Por cierto, existen un par de vistas más para cambiar la contraseña del
usuario autenticado, pero esas las veremos cuando creemos los perfiles.

Lo único que nos falta es añadir el enlace de restauración en el
formulario de autenticación:

![]({{cdn}}/django/images/image812.png)

![]({{cdn}}/django/images/image279.png)

Con esto acabamos la parte de la autenticación y el registro.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>