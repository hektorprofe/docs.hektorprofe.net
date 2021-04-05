title: Creando un repositorio en Github | Curso de Django | Hektor Profe

# Creando un repositorio en Github

En esta lección vamos a crear un repositorio para almacenar uno de
nuestros proyectos y utilizarlo en el despliegue. No me voy a centrar en
enseñaros Git a fondo, sólo los cuatro comandos básicos para crear el
repo y enviar los datos. 

Así que vamos a suponer que todos tenemos una cuenta en
[github.com](https://github.com) y
tenemos Git instalado en nuestra computadora, al fin y al cabo era un
requisito para utilizar Visual Studio Code. Si no lo tenéis podéis
descargarlo en
[git-scm.com](https://git-scm.com).

A continuación voy a crear mi repositorio en Github para almacenar mi
proyecto webempresa, ya que este es el que os enseñaré a desplegar:

![]({{cdn}}/django/images/image477.png)

![]({{cdn}}/django/images/image839.png)

![]({{cdn}}/django/images/image214.png)

Ahora vamos a clonar el repositorio en nuestro equipo. Abrimos una
terminal en el directorio donde queramos clonarlo, en mi caso
CursoDjango:

![]({{cdn}}/django/images/image689.png)

Copiamos la URL para clonearlo:

![]({{cdn}}/django/images/image554.png)

Y utilizamos el comando git clone \<url\>:

![]({{cdn}}/django/images/image330.png)

Se creará una carpeta con nuestro repositorio, trasladaremos el proyecto
a ella, pues a partir de ahora trabajaremos ahí:

![]({{cdn}}/django/images/image850.png)

Accederemos a la carpeta a través de la terminal y ejecutaremos el
comando: git add . (para añadir nuestro proyecto al repositorio).

![]({{cdn}}/django/images/image607.png)

A continuación crearemos un commit para configurar una actualización con
todos los cambios que hemos hecho:

![]({{cdn}}/django/images/image350.png)

Al hacerlo por primera vez nos pedirá antes configurar un perfil con un
email y nombre. Utilizaremos el comando git config dos veces. Si vamos a
utilizar siempre este email y nombre en todos los proyectos podemos usar
la cláusula global tal como nos indica:

![]({{cdn}}/django/images/image258.png)

Volveremos a hacer el commit:

![]({{cdn}}/django/images/image380.png)

Veremos un resumen con los cambios, ya sólo falta enviar los datos al
repositorio, que haremos con un git push origin master:

![]({{cdn}}/django/images/image433.png)

Después de poner nuestro usuario y contraseña, veremo que se han
publicado los cambios en la web del repositorio y podemos navegar en él:

![]({{cdn}}/django/images/image864.png)

El paso de introducir el usuario y la contraseña nos lo podemos ahorrar
generando una clave SSH, os dejaré un enlace os explican cómo se hace:
[https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

Sea como sea ya tenemos el proyecto en un repositorio, así que en la
próxima lección veremos como adaptarlo para  desplegarlo en un servicio
online gratuito.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>