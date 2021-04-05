title: Décima App (Messenger) Análisis y diseño | Curso de Django | Hektor Profe

# Décima App [Messenger] Análisis y diseño

He pensado mucho en una app que nos permita no sólo poner a prueba lo
que sabemos, sino también que aproveche la estructura que hemos
desarrollado y además podamos aprender cosas nuevas.

Al final se me ha ocurrido algo interesante: una app de mensajería
privada similar a la de Udemy. De hecho no sé si lo he comentado ya,
pero Udemy está en gran parte programado con Django, así que la he
utilizado de referencia.

Así que vamos a ponernos en situación analizando la funcionalidad
mientras aplicamos el principio de las Cinco W (Quién - Who, Qué - What,
Cuándo - When, Dónde - Where y Porqué - Why). Me gusta hacerlo porque
arroja mucha luz independientemente del campo dónde se aplique, además
sirve para filtrar.

-   ¿Quién hará uso de la funcionalidad? Un usuario registrados e
    identificado.
-   ¿Qué hará la funcionalidad? Establecer un chat privado entre ambos
    para que se comuniquen.
-   ¿Cuándo? Cuando un usuario decida iniciar una conversación con otro,
    o un usuario visite la sección “Mensajes” para revisar los chats que
    tiene abiertos y continuar sus conversaciones.
-   ¿Dónde? En su debida sección de Mensajes o a través del botón
    “Enviar mensaje” en los perfiles públicos.
-   ¿Por qué? Porque ofrecer una vía de comunicación privada es una
    opción que toda aplicación social debería incluir, además será
    reutilizable y nos servirá para aprender mucho.

Cabe señalar que nuestro sistema de mensajes no será en tiempo real, es
decir, no será un chat. Para eso hace falta crear websockets y se
requiere un nivel más avanzado. Lo nuestro será un sistema mucho más
simple, de enviar el mensaje

Ya que vamos a enviar mensajes, podríamos considerar que un Mensaje
“message” es un modelo. Así que como primera idea podríamos pensar en un
mensaje como un modelo con los siguientes campos:

-   Un emisor: el usuario que envía el mensaje
-   Un receptor: el usuario que recibe el mensaje
-   Un cuerpo: con el texto del mensaje
-   Una fecha: con el momento de creación

Con esto ya tenemos los mensajes, pero necesitamos una forma de
manejarlos en conjunto, y ahí es donde aparece el concepto de hilo de
conversación, en inglés “thread”.

Podemos entender un hilo como un lugar donde ocurre la conversación, una
especie de punto de encuentro entre varios usuarios donde se almacenan
mensajes, por lo que ya no necesitamos un receptor en el mensaje, el
receptor será el propio hilo que los contendrá. En consecuencia nos
quedarían dos modelos:

-   Message (mensaje): con tres campos: una relación FK al usuario que
    lo crea, el cuerpo y la fecha.
-   Thread (hilo): con dos relaciones M2M: una con los usuarios que
    forman parte del hilo y otra con los mensajes que se van añadiendo
    al mismo.

Lo bueno de este sistema es que un hilo no tiene porqué limitarse a dos
usuarios, aunque en nuestro caso así será porque es una restricción
impuesta por la propia funcionalidad.

Así que vamos a dejar preparada la app y sus modelos.

Vamos a llamarla Messenger porque Django ya incluye una app Messages y
no podemos repetir nombres. Como Messenger significa mensajero me
pareció un buen nombre alternativo, tambiénasí que vamos a utilizar ese:

![]({{cdn}}/django/images/image444.png)

![]({{cdn}}/django/images/image26.png)

Sin más preámbulos vamos a por nuestros modelos:

![]({{cdn}}/django/images/image85.png)\
![]({{cdn}}/django/images/image23.png)

Como véis esta parte no es muy compleja, ahora a ver cómo nos las
apañamos para manejarlo.

![]({{cdn}}/django/images/image283.png)\
![]({{cdn}}/django/images/image456.png)

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>