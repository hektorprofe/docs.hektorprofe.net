title: Octava App (Registration) Iniciando la sesión | Curso de Django | Hektor Profe

# Octava App [Registration] Iniciando la sesión

Hasta ahora para iniciar y cerrar la sesión lo hemos hecho siempre a
través del panel de administrador, pero esto sólo nos vale para webs
sencillas. Si queremos crear algo más elaborado nos veremos obligados a
integrar este proceso dentro del diseño de la página.

Por suerte gracias a las CBV no tenemos que desarrollar el sistema desde
cero.

Para reutilizar parte del sistema de autenticación de Django,
empezaremos creando nueva app llamada registration (se le suele dar este
nombre). Esta app manejará tanto la autenticación como el registro y
vamos a estar bastantes lecciones con ella.

Así que como siempre, vamos a empezar creando esta nueva app:

![]({{cdn}}/django/images/image443.png)

En esta app no vamos a programar casi nada, sólo se va a encargar de
almacenar algunos templates.

A continuación vamos a dirigirnos al fichero urls.py del proyecto base y
vamos a configurar un nuevo apartado /accounts/, debe ser ese nombre
pues es el que las CBV de Django implementan por defecto:

![]({{cdn}}/django/images/image533.png)

Sólo con esto se nos han dado de alta varias URLS para manejar la
autenticación. Podemos ver exactamente cuales accediendo al servidor
/accounts/:\
![]({{cdn}}/django/images/image774.png)

![]({{cdn}}/django/images/image14.png)

Básicamente tenemos el login, el logout y varias vistas para manejar la
gestión de contraseñas. Por ahora centrémonos en las dos primeras. Son
todas las AUTH VIEWS que podemos ver en nuestra web favorita:

[https://ccbv.co.uk/](https://ccbv.co.uk/)\
 ![]({{cdn}}/django/images/image671.png)

Podríamos haber creado todas una a una manualmente, pero al haber hecho
el include directo nos lo hemos ahorrado.

Sea como sea si intentamos acceder a /accounts/login/ cargaremos una
LoginView genérica:

![]({{cdn}}/django/images/image652.png)

Y obviamente nos dará error de template:

![]({{cdn}}/django/images/image753.png)

Tenemos que crear el template login.html en el directorio
templates/registration de la app que hemos creado antes:

![]({{cdn}}/django/images/image182.png)

Dentro sólo debemos preparar y mostrar un formulario de la forma
clásica, pero como quiero ahorraros trabajo he preparado un diseño de
antemano. Simplemente he copiado el código HTML generado por defecto, he
comprobado errores globales en la lista form.non\_field\_errors y he
añadido los atributos class y placeholder a los inputs.

[https://gist.github.com/hcosta/7c3a46d5e5d061d936031ad5a6654acd](https://gist.github.com/hcosta/7c3a46d5e5d061d936031ad5a6654acd) 

Una vez creado el template tenemos que activar la app registration para
que se cargue y reiniciar el servidor:

![]({{cdn}}/django/images/image13.png)

Y si actualizamos la página deberías ser capaces de verla correctamente:

![]({{cdn}}/django/images/image124.png)

Si intentamos acceder, veréis que nos da un fallo:

![]({{cdn}}/django/images/image797.png)

Esto ocurre porque Django está redireccionandonos automáticamente a una
supuesta página de perfil en /accounts/profile. Más adelante crearemos
un perfil de usuario, así que por ahora nos interesa cambiar de alguna
forma esta redirección. ¿Cómo lo hacemos? Pues yendo a settings.py y
añadiendo:

![]({{cdn}}/django/images/image714.png)

Ahora si nos identificamos correctamente podréis notar como nos
redirecciona a la vista portada que tiene ese nombre:

![]({{cdn}}/django/images/image602.png)

Si en lugar de home quisiéramos redirigir al usuario a la lista de
páginas podríamos hacer con:

![]({{cdn}}/django/images/image913.png)

Ya que esta opción actúa como la función reverse.

Vamos a tomarnos una pausa y luego hacemos el logout en la próxima
lección.



___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>