title: Desplegando un proyecto de prueba | Curso de Django | Hektor Profe

# Desplegando un proyecto de prueba

Os aviso de antemano de que esta lección será muy larga, realizar un
despliegue no es cualquier cosa y requiere configurar un montón de
opciones, pero el resultado es muy grato y estoy seguro de que será una
buena experiencia.

Existen muchas empresas que nos permiten desplegar nuestros proyectos en
la nube, como Heroku o AWS (Amazon Web Services), incluso se puede
desplegar en un servidor privado, pero en cualquier caso se requieren
conocimientos de administración de sistemas. Os compartiré tutoriales y
manuales para algunos de estos servicios en la siguiente lección. Y por
mi parte me centraré en enseñaros cómo hacerlo en PythonAnywhere, un
Hosting especializado en proyectos Python, que nos da la posibilidad de
desplegar un proyecto gratuito de una forma bastante fácil, así por lo
menos os sirve de experiencia práctica.

Lo primero será ir a la web
[http://www.pythonanywhere.com](http://www.pythonanywhere.com) y
crear una cuenta de principiante. El nombre de la cuenta será la
dirección donde se publicará nuestro proyecto, así que elegid un buen
nombre.

![]({{cdn}}/django/images/image318.png)

![]({{cdn}}/django/images/image623.png)

Al registrarnos contaremos con nuestro propio subdominio, en mi caso:
[http://webpersonal.pythonanywhere.com/](http://webpersonal.pythonanywhere.com/) ,
con hasta 512 MB de espacio.

Bien, ahora deberíamos iniciar una terminal y clonar nuestro
repositorio, configurarlo para producción y poner el servidor en marcha.
Suena fácil, pero en realidad no lo es, básicamente porque cada hosting
tiene sus normas y pautas a la hora de desplegar Django o cualquier otro
servicio, obviamente en el caso de PythonAnywhere no iba a ser
diferente.

En el enlace de la documentación DeployExistingDjangoProject
([https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/](https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/) +
[https://help.pythonanywhere.com/pages/DjangoStaticFiles](https://help.pythonanywhere.com/pages/DjangoStaticFiles))
se detalla punto a punto como desplegar correctamente Django, os lo
dejaré en los recursos porque es básicamente lo que vamos a hacer.

Vamos a ir al apartado consoles y vamos a iniciar Bash para trabajar
como si estuviéramos en la terminal del servidor.

El siguiente paso es crear un entorno virtual para ejecutar nuestro
proyecto, pero en lugar de utilizar Anaconda aquí tenemos que crearlo
con la herramienta VirtualEnv, es la forma más clásica:

![]({{cdn}}/django/images/image340.png)

De forma similar a Anaconda podemos desactivar el entorno con:

![]({{cdn}}/django/images/image35.png)

Sin embargo para activarlo aquí deberemos ejecutar el script activate
desde su propio directorio con un source:

![]({{cdn}}/django/images/image80.png)

Podemos hacer un pip list para ver qué paquetes nos vienen instalados:

![]({{cdn}}/django/images/image645.png)

Obviamente si vamos a utilizar Django y otros paquetes como Pillow y
django-ckeditor deberíamos instalarlos aquí mismo, pero es una mejor
práctica crear un fichero requirements.txt en nuestro repositorio para
luego instalarlo de forma mucho más cómoda. Iremos a nuestro directorio
del repositorio, crearemos el fichero y añadiremos lo siguiente,
haciendo referencia al nombre del paquete y a la versión que sabemos es
estable en nuestro proyecto:

![]({{cdn}}/django/images/image856.png)

![]({{cdn}}/django/images/image518.png)

Ahora vamos a publicar los cambios:

![]({{cdn}}/django/images/image621.png)\
![]({{cdn}}/django/images/image849.png)

Ahora vamos a clonar el repositorio desde la terminal Bash. Haremos un
simple git clone (podemos pegar con Control+V):

![]({{cdn}}/django/images/image539.png)

Con esto tenemos el repositorio ya en el servicio de PythonAnywhere,
vamos a instalar las dependencias en el entorno virtual:

![]({{cdn}}/django/images/image176.png)

Esperamos un rato que instale todo…

![]({{cdn}}/django/images/image89.png)

En este punto todos los paquetes habrán quedado instalados en nuestro
entorno virtual y deberíamos ser capaces de ejecutar el scripts
manage.py de forma normal.

Así que vamos a ejecutar el comando: python manage.py check --deploy

![]({{cdn}}/django/images/image546.png)

Es interesante ver cómo el propio Django analiza la configuración para
avisarnos de todo lo que deberíamos solucionar antes de hacer poner el
servidor en marcha en este entorno de producción.

No voy a entrar a comentar cada uno de ellos, la mayoría son poner a
True algunas opciones en el settings.py, otros son recomendaciones que
se entienden leyendo la descripción. Sin embargo hay dos que son
sumamente importantes:

![]({{cdn}}/django/images/image243.png)\
![]({{cdn}}/django/images/image488.png)

Así que tenemos que arreglarlos antes de continuar.

Simplemente editaremos el fichero settings.py con algún editor a través
de la terminal:

![]({{cdn}}/django/images/image356.png)\
![]({{cdn}}/django/images/image467.png)

Así desactivaremos el Debug y daremos permiso a los HOST locales,
incluyendo el propio dominio de la página.

La base de datos no tenemos que hacer nada con ella, ya que la hemos
publicado en el repositorio y se ha clonado tal cuál la teníamos. Ya os
dije que esto no es una buena práctica, pero casualmente las bases de
datos SQLite se gestionan en ficheros, por lo que esta es una copia de
la otra, por lo que no tenemos el problema de borrar datos
accidentalmente. En todo caso si utilizáis otro SGBD no uséis la misma.
Deberíais migrar manualmente y crear el superadministrador desde la
terminal bash.

Sea como sea ahora tenemos la configuración mínima recomendada para
realizar el despliegue, y para ello debemos crear una webapp que se
encargue de mantener el servicio de Django en marcha.

Abriremos otra pestaña en la sección Apps:
[https://www.pythonanywhere.com/user/webpersonal/webapps/](https://www.pythonanywhere.com/user/webpersonal/webapps/) y
crearemos una nueva app:

![]({{cdn}}/django/images/image655.png)

Aunque en la lista nos salga la opción Django, no seleccionaremos esa
opción, primero porque se crearía un nuevo proyecto y nosotros ya
tenemos uno existente, y segundo porque tampoco tiene soporte para
Django 2 automátic. Así que vamos a seleccionar la configuración Manual
para Python 3.6:

 ![]({{cdn}}/django/images/image200.png)+ ![]({{cdn}}/django/images/image210.png)

Ahora nos indicará que debemos configurar nuestro propio fichero WSGI:

![]({{cdn}}/django/images/image662.png)

¿Recordáis al principio del curso cuando os comenté que dentro del
proyecto Django, en el directorio donde está settings.py también hay un
script llamado wsgi.py? Pues es hora de que este fichero entre en
escena, aunque de una forma distinta, ya que pythonanywhere utiliza su
propia versión. Así que presionamos NEXT para crear la web app y acto
seguido, una vez se cree, llegaremos a la página de gestión de nuestra
web app:

![]({{cdn}}/django/images/image323.png)

De hecho ya podemos acceder a la página, aunque sólo nos aparecerá
información de prueba:

![]({{cdn}}/django/images/image527.png)

¿De dónde sale esta información de prueba? Pues ni nada menos que del
fichero wsgi que se está utilizando ahora mismo:

![]({{cdn}}/django/images/image58.png)

Luego volveremos a él, pero antes vamos a realizar la configuración
inferior. Debemos introducir el directorio con el código fuente del
proyecto y también el del entorno virtual:![]({{cdn}}/django/images/image58.png)

![]({{cdn}}/django/images/image58.png)

El directorio del código fuente es obviamente donde encuentra el
proyecto. Podemos consultarlo haciendo un pwd en la terminal,
seleccionarlo y copiarlo con Control+C:

![]({{cdn}}/django/images/image656.png) \
![]({{cdn}}/django/images/image157.png)

El del entorno virtual podemos consultarlo haciendo un which python, y
copiando la parte hasta el nombre del entorno:

![]({{cdn}}/django/images/image784.png)\
![]({{cdn}}/django/images/image254.png)

Ahora vamos de vuelta al fichero WSGI que utiliza nuestro proyecto, si
accedemos a él veremos que contiene una configuración de prueba en lugar
de poner en marcha nuestro servidor Django:

![]({{cdn}}/django/images/image126.png)

Así que evidentemente tenemos que configurar una serie de cosillas para
que todo funcione. Vamos a borrar todo el contenido, sí, todo. En su
lugar vamos a copiar la configuración recomendada por la propia empresa.
La encontramos en el enlace de configuración que os compartí al
principio de la lección y lo editaremos cambiando el directorio de
nuestro proyecto y el de la variable de entorno DJANGO\_SETTINGS\_MODULE
para que haga referencia al settings del proyecto:

[https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/](https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/) 

MUCHO OJO CON LOS ESPACIOS (COMO EN LA CAPTURA EN EL PATH):

![]({{cdn}}/django/images/image763.png)

Luego lo guardaremos y recargaremos el proyecto:

![]({{cdn}}/django/images/image293.png)![]({{cdn}}/django/images/image387.png)

En teoría una vez se recargue, si visitamos nuestra página deberíamos
funcionar perfectamente:

[https://webpersonal.pythonanywhere.com/](https://webpersonal.pythonanywhere.com/)

![]({{cdn}}/django/images/image480.png)

Podemos también visitar el panel de administrador:

[https://webpersonal.pythonanywhere.com/admin/](https://webpersonal.pythonanywhere.com/admin/) 
(hector -\> hola1234)

![]({{cdn}}/django/images/image276.png)

Todos nos funcionará, excepto por una cosa: los ficheros media. Y es que
estos ficheros no sé si lo recordaréis pero os dije muchas veces que se
suelen servir con servidores como Nginx o Apache y por defecto Django no
los servirá en producción. De hecho si lo pensáis detenidamente, ¿cómo
es que los ficheros media no los sirve pero los estáticos sí? Bueno eso
es gracias a que hemos utilizado la buena lógica de crear directorios
static dentro de las apps, así que él se encarga de servirlos. Pero
tampoco es buena idea, deberíamos hacer unos ajustes finales para que
nuestra webapp sirva los ficheros estáticos de forma correcta.

Para ello vamos a hacer lo siguiente, iremos al apartado FILES de la
webapp:

![]({{cdn}}/django/images/image107.png)

Aquí añadiremos dos urls y dos directorios:

![]({{cdn}}/django/images/image926.png)

Sé lo que estaréis pensando… El directorio media se entiende, pero
¿porque hemos puesto un directorio static si no existe en nuestra
aplicación? Pues muy sencillo, porque vamos a crearlo manualmente y
copiaremos todos los ficheros estáticos ahí! Pero tranquilos, que no
tenemos que hacerlo nosotros, Django lo hará por nosotros.

Simplemente debemos ir al fichero settings y  justo abajo en la
configuración de ficheros estáticos añadir la siguiente variable:

![]({{cdn}}/django/images/image925.png)

Guardamos el fichero, y ahora en nuestra terminal y con el entorno
virtual en marcha vamos a ejecutar la magia potagia:

![]({{cdn}}/django/images/image153.png)\
![]({{cdn}}/django/images/image253.png)

Habiendo hecho esto, reiniciamos la webapp:

![]({{cdn}}/django/images/image930.png)

Accedemos de nuevo a nuestra página y…

![]({{cdn}}/django/images/image281.png)

Valorar si añadir un mailbox nuevo y probar a enviar un correo o no hace
falta.

Ya lo tenemos todo funcionando. Nuestra web app está lista, sirviendo
ficheros estáticos y media con el servidor de ficheros estáticos de
Python Anywhere. ¿Qué os parece?

Sólo una última cosa, debemos volver al panel de la webapp una vez cada
tres meses si no queremos que la desactiven por inactividad:

![]({{cdn}}/django/images/image866.png)

Y bueno, todo lo que hemos visto es muy parecido en los demás servicios,
dejando de banda las opciones de configuración específicas de cada uno,
pero estoy seguro de que os habrá servido mucho, porque por lo menos
habréis experimentado lo que es el proceso de despliegue en vuestras
propios manos, que ya es algo.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>