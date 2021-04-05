title: TDD (2): Refactorización | Curso de Django | Hektor Profe

# TDD (2): Refactorización

Quizá os ha pasado por alto, o quizá no, pero tenemos un fallo de
seguridad importante en el momento de añadir un mensaje a un Hilo. Os lo
voy a demostrar con un Test.

Empezaremos añadiendo un tercer usuario:

![]({{cdn}}/django/images/image538.png)

Ahora crearemos un test que intente añadir un tercer mensaje al hilo
creado por user3 pese a que él no forme parte del hilo. Se supone que si
un usuario no forma parte del hilo no debe ser capaz de añadir un
mensaje, así que vamos a suponer que no, y por lo tanto éste contendrá
sólo los dos primeros mensajes:

![]({{cdn}}/django/images/image352.png)

Como podéis suponer, al ejecutar el test nos fallará:

![]({{cdn}}/django/images/image452.png)

Estaba claro como el agua que se añadiría, porque en ningún momento
hemos comprobado lo contrario. Tenemos que refactorizar para
solucionarlo.

¿Cómo vamos a modificar el comportamiento del campo Many2ManyField para
que compruebe que los mensajes los han creado usuarios que forman parte
del hilo? Pues con algo que ya conocemos: una señal, concretamente una
señal llamada m2m-changed, os dejaré documentación al respecto en los
recursos de la lección:
[https://docs.djangoproject.com/en/dev/ref/signals/\#m2m-changed](https://docs.djangoproject.com/en/dev/ref/signals/\#m2m-changed) 

Esta señal permite detectar cuando un campo Many2Many es modificado, así
que siguiendo el ejemplo de la documentación podríamos hacer lo
siguiente:

![]({{cdn}}/django/images/image286.png)

Y abajo del todo:

![]({{cdn}}/django/images/image918.png)

Como véis esta forma de crear la señal es directa y no requiere el uso
de un decorador @receiver.

En todo caso, no sabemos muy bien qué nos vamos a encontrar, así que
vamos a hacer un debug comprobando los argumentos instance, action y
pk\_set. Según la documentación, instance hace referencia al Thread
desde donde se llama la señal, action puede contener pre\_add o
post\_add, indicando el momento justo antes o después de guardar los
registros. Luego tenemos pk\_set, un conjunto donde se pasan las PK de
los mensaje que se añadirán o han sido añadidos, dependiendo del
momento:

![]({{cdn}}/django/images/image903.png)

Vamos a ejecutar sólo el test actual para mostrar estos valores al
llamarse la señal:

![]({{cdn}}/django/images/image348.png)\
![]({{cdn}}/django/images/image112.png)

Así se ve cómo efectivamente la señal capta dos momentos en el Thread 1,
pre\_add y post\_add con las PK de los mensajes.

A nosotros nos interesa el pre\_add, porque en él comprobaremos si algún
mensaje tiene un usuario que no forma parte del Hilo:

![]({{cdn}}/django/images/image219.png)\
![]({{cdn}}/django/images/image363.png)

Ahora sólo tenemos que sacar el mensaje de este usuario del conjunto
pk\_set. Sin embargo no podemos hacerlo dentro de la iteración, ya que
afectaría al conjunto y quedaría inconsistente:

![]({{cdn}}/django/images/image742.png)\
![]({{cdn}}/django/images/image429.png)

En su lugar podemos simplemente almacenar los mensajes fraudulentos en
otro conjunto:

![]({{cdn}}/django/images/image239.png)

Los vamos agregando ahí a medida que los encontramos:

![]({{cdn}}/django/images/image426.png)

Ya al final de todo, fuera de la iteración, hacemos podemos utilizar el
método difference\_update de los conjuntos para encontrar los elementos
no comunes (1, 2) entre el conjunto pk\_set y false\_pk\_set,
actualizándolos en pk\_set y filtrando así los mensajes:

![]({{cdn}}/django/images/image798.png)

Si ejecutamos el Test de nuevo, esta vez sí nos debería funcionar:

![]({{cdn}}/django/images/image455.png) ![]({{cdn}}/django/images/image762.png)

Esto sí que es TDD en toda regla, ya que a fuerza de refactorizar hemos
conseguido validar un test sin alterar su estructura.

Si esta lección os ha parecido interesante, entonces la siguiente os
gustará todavía más, pues añadiremos nuestro propio Model Manager para
el modelo Thread, ya veréis que útil.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>