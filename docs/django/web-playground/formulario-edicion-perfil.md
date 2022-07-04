title: Haciendo editable el perfil | Curso de Django | Hektor Profe

# Haciendo editable el perfil

La razón por la que no hemos creado directamente una UpdateView la vais
a ver en breve, por ahora vamos a migrar la app registration:

![]({{cdn}}/django/images/image116.png)\
![]({{cdn}}/django/images/image757.png)

A continuación vamos a transformar la TemplateView en una UpdateView,
importando el modelo Profile:

![]({{cdn}}/django/images/image326.png)\
![]({{cdn}}/django/images/image743.png)

![]({{cdn}}/django/images/image565.png)

Ahora la gran pregunta...¿como conseguimos la primary key del perfil
para editarlo y enviarla a la CBV UpdateView? Pues os voy a contestar
con otra pregunta, ¿ sería buena idea pasar una pk del perfil en el
path? Obviamente la respuesta es NO, si hiciéramos eso cualquiera podría
editar todos los perfiles sólo sabiendo el id. Además, ¿si todavía no
hemos creado una instancia de perfil como vamos a mostrar un formulario
para editarlo?

Por suerte aunque no sepamos el id del perfil, podemos saber el id del
Usuario autenticado sin necesidad de pasarlo en el path, pues éste se
almacena en la propia request.

Ahora la última pieza que nos falta es recuperar el perfil a partir del
id del usuario que hay en request. ¿Cómo haremos esta magia oscura? Pues
sobreescribiendo el método get\_object de nuestra UpdateView, encargada
de recuperar el objeto que se tiene que modificar:

![]({{cdn}}/django/images/image899.png)

Get\_object debe devolver el objeto que editaremos, así que simplemente
podemos recuperarlo a partir de self.request.user:

![]({{cdn}}/django/images/image41.png)

Sin embargo con esto no es suficiente. Y es que estamos intentando
recuperar un Profile que todavía no existe. Por suerte podemos cambiar
la consulta para hacer uso del método get\_or\_create en lugar de get.
Lo bueno que tiene es que creará la instancia si no existe... y devuelve
dos valores: la instancia y un booleano indicando si la acaba de crear:

![]({{cdn}}/django/images/image430.png)

Tened en cuenta que aunque sólo utilicemos el primer valor, debemos
declarar los dos porque se están devolviendo ambos y hay que guardarlos
en algún lado.

Con esto vamos a probar si funciona..

![]({{cdn}}/django/images/image7.png)

Parece que sí, incluso podemos modificar la información…

![]({{cdn}}/django/images/image927.png)

Lo único que no funciona bien es la imagen. ¿Sabéis por qué? Pues no es
que tengamos un error ni mucho menos, es sólo que no hemos configurado
el formulario para aceptar ficheros desde el propio HTML. Hacerlo es muy
fácil, vamos a nuestro template y...

![]({{cdn}}/django/images/image865.png)

Recarguemos el formulario e intentemos enviar de nuevo la imagen:

![]({{cdn}}/django/images/image511.png)

¡Ahí la tenemos!

Por cierto, ¿sabéis que tan fácil sería acceder al perfil de cualquier
usuario? Pues sólo  tendríamos que hacer referencia a su profile como si
fuera otro campo de User:

![]({{cdn}}/django/images/image98.png)\
![]({{cdn}}/django/images/image222.png)

Esto es gracias a que las relaciones OneToOneField se enlazan
automáticamente al modelo con su mismo nombre, ni siquiera tenemos que
definir un related\_name, ¿no es genial?

En la siguiente lección le daremos un mejor aspecto a este formulario.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>