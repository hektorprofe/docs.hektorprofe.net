title: Creando un perfil de usuario | Curso de Django | Hektor Profe

# Creando un perfil de usuario

Nuestro siguiente objetivo es ofrecerle al usuario tres campos extras
para personalizar su perfil: una imagen para usarla de avatar, un texto
como biografía y un enlace a una página web.

Podríamos crear un nuevo modelo User con estos tres campos extra, pero
esa sería la solución compleja. Vamos a por lo simple, crear un modelo
Profile que contenga esos 3 campos y una relación 1:1 con un Usuario, de
manera que cada instancia de User tenga enlazada una de Profile.

Lo vamos a crear en nuestra app Registration ¿Porqué ahí en lugar de en
una nueva app? Bueno, no sé si lo recordaréis pero por defecto django al
registrarse el usuario lo redireccionaba a /accounts/profile/ ¿no? Pues
esa es la razón. Más adelante sí crearemos una app Profiles para los
perfiles públicos, pero esta parte privada la manejaremos en
registration.

En este modelo no necesitamos darle nombre a los campos porque no vamos
a usarlos desde el panel de administrador:

![]({{cdn}}/django/images/image497.png)

Lo más remarcable es el uso de la relación OneToOneField. Esta es la
tercera relación que podemos crear en Django y le indica al modelo que
sólo puede haber perfil para cada usuario, no se pueden tener dos
perfiles para un mismo usuario, ni distintos usuarios para un mismo
perfil, esa es la clave del OneToOne. Haciendo un breve repaso, en
Django tenemos tres tipos de relaciones:

-   OneToOneField, relación (1:1) de 1 a 1. Única para ambos sentidos: 1
    usuario - 1 perfil
-   ForeignKeyField, relación (1:N) de 1 a varios. Única en un sólo
    sentido: 1 autor - N entradas 
-   ManyToManyField, relación (N:M) de varios a varios. No única en
    ningún sentido: N entradas - M categorías

Dicho esto, recordad que tenemos un campo de imagen, así que debemos
tener instalado Pillow en el entorno virtual y configurar el servidor
para servir ficheros MEDIA. En mi caso ya tengo Pillow, así que sólo
tengo que configurar el servidor:

![]({{cdn}}/django/images/image11.png)

![]({{cdn}}/django/images/image634.png)\
![]({{cdn}}/django/images/image282.png)

Perfecto.

Ahora necesitamos crear una página para editar el perfil. Por ahora
vamos a crearla como una simple TemplateView, luego os explico porqué.
También utilizaremos el decorador login\_required en el dispatch, ya que
no se puede editar un perfil sin estar identificado:

![]({{cdn}}/django/images/image900.png)

![]({{cdn}}/django/images/image877.png)

El template vamos a copiarlo de page\_form y lo adaptaremos un poco:

![]({{cdn}}/django/images/image385.png)

Y configuraremos el enlace en urls.py:

![]({{cdn}}/django/images/image453.png)

Finalmente pondremos el enlace en nuestro menú cuando el usuario inicia
la sesión:

![]({{cdn}}/django/images/image138.png)

Y comentamos la redirección de settings para el login:

![]({{cdn}}/django/images/image194.png)

Una vez hecho todo esto vamos a identificarnos con un usuario a ver si
nos lleva al perfil:

![]({{cdn}}/django/images/image766.png)

Bien, con esto bastará, vamos a tomarnos un descanso y continuamos en la
siguiente lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>