title: Creando un Mixin de identificación | Curso de Django | Hektor Profe

# Creando un Mixin de identificación

Nuestra app de páginas está muy bien y todo funciona sin problemas, pero
tenemos un fallo capital, extremadamente importante. ¿Sabéis cual es?
Probad lo siguiente.

Si vamos al panel de admin y cerramos la sesión, al volver al apartado
de páginas está claro que no nos aparece el menú de administrar páginas.
¿Todo bien no? Pero y si accedemos manualmente a la url /pages/create/ ?

![]({{cdn}}/django/images/image594.png)

Pues que cosas… parece que carga el formulario ¿Nos dejará crear una
página?

Sí, y no sólo podemos crear, también podemos editar y borrar.

Este es nuestro fallo, cualquiera puede manejar la base de datos a
través de nuestras vistas CRUD porque son PÚBLICAS.

¿Cómo vamos a solucionarlo? Pues añadiendo un acceso privado para que
sólo los usuarios identificados y miembros del STAFF puedan gestionarla.

¿Recordáis el método GET que tienen las CBV? ¿Que se encargaba de la
respuesta a una petición GET?. Pues resulta que hay un método que en
lugar de controlar la respuesta permite controlar la petición. Ese
método es dispatch.

Si redefinimos dispatch podremos comprobar la request, y dentro de la
request si hay un usuario identificado:

![]({{cdn}}/django/images/image654.png)\
![]({{cdn}}/django/images/image67.png) ![]({{cdn}}/django/images/image67.png)

Pero esto es sólo un debug, lo que deberíamos hacer es redireccionar al
visitante al LOGIN para que se identifique:

![]({{cdn}}/django/images/image558.png)

Y ahora viene la gran pregunta. ¿Debemos sobreescribir el dispatch en
toooooodas las vistas donde queramos que el usuario se identifique? Y la
respuesta es: por supuesto que no! Para eso existen los Mixins.

Un Mixin es una implementación de una o varias funcionalidades para una
clase, podemos crearlo una vez y heredar su comportamiento donde
queramos dándole prioridad a su implementación antes que la de otra
clase.

Fijaros, vamos a trasladar nuestro dispatch a un nuevo mixin, podemos
crearlo en el propio views.py:

![]({{cdn}}/django/images/image530.png)

Esta es nuestra funcionalidad especial, ahora sólo debemos hacer que
nuestras CBV hereden de él dándole prioridad durante la herencia, es
decir, poniendo más a la izquierda:

![]({{cdn}}/django/images/image513.png)

Esto básicamente sobreescribirá el méotod dispath del CreateView con el
dispath de nuestro Mixin, y así tendremos nuestra funcionalidad
implementada. Vamos a probarlo…

![]({{cdn}}/django/images/image584.png)

Con esto hemos aprendido como se crea y utiliza un Mixin, si queréis más
información os dejaré documentación al respecto, tened en cuenta que
podéis sobreescribir cualquier atributo o método, por lo que son muy
útiles:\
[https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/](https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/) 

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>