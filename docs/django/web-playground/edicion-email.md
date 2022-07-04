title: Opción de editar el email | Curso de Django | Hektor Profe

# Opción de editar el email 

Editar el email podría ser una odisea utilizando vistas basadas en
clases. Eso es porque una UpdateView está limitada a un modelo, que en
nuestro caso es Profile. Si quisiéramos editar dos modelos, Profile y
User , no podríamos. En su lugar deberíamos implementar una vista
tradicional y manejar manualmente un formulario compartido de forma
parecida a como hicimos el de contacto.

Para estos casos mi recomendación es dejarnos llevar por el framework,
así que vamos a seguir la lógica de las UpdateView y vamos a separar la
edición del email en un formulario a parte. Sí, puede que el usuario
tengo que hacer un clic extra, pero para nosotros será mucho más fácil,
y además podemos dar a entender que el email no es algo que se pueda ir
cambiando tan a la ligera.

Así que se me ha ocurrido que podemos mostrar un campo con el email pero
sólo de lectura y debajo un enlace que diga: Si deseas editar tu email
haz clic aquí. Vamos a hacerlo.

![]({{cdn}}/django/images/image191.png)

Este campo es sólo de adorno, fijaros que no tiene un atributo name, por
lo que no se enviará:

![]({{cdn}}/django/images/image111.png)

Ahora vamos a diseñar un formulario para editar el email:

![]({{cdn}}/django/images/image9.png)

Pero con esto no basta, necesitamos validar el email, y en esta ocasión
debemos comprobar dos cosas: primero si se ha editado el email y si es
así, comprobar que éste no se repita.

¿Cómo lo hacemos? Pues por suerte para nosotros hay una lista llamada
changed\_data a la que podemos acceder desde el método clean, desde ahí
es muy fácil comprobar si ha cambiado el email:

![]({{cdn}}/django/images/image924.png)

Ahora sólo tenemos que preparar la vista:

![]({{cdn}}/django/images/image306.png)\
![]({{cdn}}/django/images/image81.png)

Vamos a crear una url:

![]({{cdn}}/django/images/image728.png)

Si accedemos a la URL pese a no haber creado el template, nos dará un
curioso error:

![]({{cdn}}/django/images/image463.png)

Al contrario de lo podíamos esperar, no se va a buscar el template en la
app registration, sino en auth. Eso es porque  Django maneja el modelo
User en esa app, pero no es nada que no podamos cambiar manualmente con
el template\_name:

![]({{cdn}}/django/images/image420.png)

Así que vamos a crearlo, podemos tomar de referencia el de
registro (signup.html) y cambiarlo ligeramente::

![]({{cdn}}/django/images/image811.png)

Vamos a ver si funciona:

![]({{cdn}}/django/images/image427.png)

Sí, ahí lo tenemos. ¿Pero porqué no se añade correctamente el widget que
hemos establecido?

Bueno, en este caso volvemos a estar ante un modelo extendido, y es que
User ya tiene sus propios campos y validaciones. Para sobreescribir sus
widgets debemos hacerlo en tiempo de ejecución, así que vamos a
llevarnos el widget a la vista:

 ![]({{cdn}}/django/images/image541.png)\
![]({{cdn}}/django/images/image819.png)

Una vez hecho esto, ya debería aparecernos bien:

![]({{cdn}}/django/images/image553.png)

Y si intentamos poner un email ya existente nos mostrará el fallo:

![]({{cdn}}/django/images/image666.png)

Finalmente sólo falta modificar el enlace y ya lo tendremos:

![]({{cdn}}/django/images/image889.png)

En la siguiente lección haremos algo parecido permitiendo al usuario
editar su contraseña. Para lograrlo nos serviremos de las vistas
automatizadas de la app auth, de forma muy similar a como hicimos el
formulario para reestablecerla.


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>