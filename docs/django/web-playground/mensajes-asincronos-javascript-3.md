title: Mensajes asíncronos con JS (3): Detalles  | Curso de Django | Hektor Profe

# Mensajes asíncronos con JS (3): Detalles 

El primer detalle que podéis observar es que al acceder al Hilo nos
aparece un Scroll vertical arriba del todo. Lo ideal sería que el Scroll
siempre estuviera abajo, justo en el último mensaje. Vamos a forzarlo
con Javascript en un plis plas.

La capa que tiene el Scroll es la del thread, vamos a darle una ID para
poder recuperarla y forzar ese scroll a la parte de abajo dando una
altura igual al propio scroll:

![]({{cdn}}/django/images/image795.png)\
![]({{cdn}}/django/images/image201.png)

![]({{cdn}}/django/images/image142.png)

Bien, y ahora vamos a lo importante. Hay dos cosas que debemos
implementar.

La primera es que al enviar un mensaje en lugar de mostrarnos el True
por pantalla se añada a la conversación sin necesidad de actualizar la
página.

Esto es un poco tedioso, requiere crear dinámicamente una capa con el
mensaje, añadirle las clases y el contenido. Luego insertarla al final
de la lista de mensajes y hacer el scroll hasta abajo:

![]({{cdn}}/django/images/image77.png)

Visto en perspectiva en el desarrollo web hay un montón de trabajo, pero
es muy reconfortante ver el resultado final funcionando:

![]({{cdn}}/django/images/image861.png)

Por cierto, ¿véis que al enviar el mensaje nos sigue apareciendo en el
textarea? Eso es lo segundo que nos falta, borrarlo:

![]({{cdn}}/django/images/image685.png)

Y con esto ya lo tenemos. Por cierto, podríamos probar a acceder con el
otro usuario a ver como se ve la conversación desde el otro lado ¿no?

![]({{cdn}}/django/images/image399.png)

Se ve perfecto y funciona todavía mejor.

Estamos muy cerca de terminar el proyecto, sólo nos falta añadir un
botón para iniciar conversaciones desde el perfil de otros usuarios. Lo
hacemos en la siguiente lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>