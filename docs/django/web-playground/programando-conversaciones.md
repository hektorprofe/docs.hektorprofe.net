title: Iniciando las conversaciones | Curso de Django | Hektor Profe

# Iniciando las conversaciones

Pues sí, hemos llegado a la penúltima lección de este mega proyecto,
donde añadiremos la funcionalidad de iniciar conversaciones. Vamos a por
ello.

Cuando presionemos el botón de enviar un mensaje desde un perfil, lo que
haremos es una petición a una vista que creará el hilo para seguidamente
redireccionarnos al hilo para empezar la conversación. Se hace rápido:

![]({{cdn}}/django/images/image640.png)\
![]({{cdn}}/django/images/image167.png)

![]({{cdn}}/django/images/image187.png)\
![]({{cdn}}/django/images/image366.png)

Finalmente sólo falta añadir el respectivo botón en el template
profile\_detail cuando el usuario sea distinto

![]({{cdn}}/django/images/image474.png)

Y si todo ha ido bien, ya lo tendremos:

![]({{cdn}}/django/images/image484.png)

Claro, hasta que no enviemos un mensaje y recarguemos no nos aparecerá
la conversación a la izquierda. Se podría detectar con javascript y si
es el primer mensaje actualizar la propia página:

![]({{cdn}}/django/images/image331.png)\
![]({{cdn}}/django/images/image928.png)

![]({{cdn}}/django/images/image759.png)

![]({{cdn}}/django/images/image422.png)

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>