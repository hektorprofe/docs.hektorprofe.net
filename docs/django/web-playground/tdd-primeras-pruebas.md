title: TDD (1): Primeras pruebas | Curso de Django | Hektor Profe

# TDD (1): Primeras pruebas

Ahora que tenemos la app con los modelos es muy tentador lanzarnos a la
piscina, pero no sería buena idea. A diferencia de todo lo que hemos
hecho en esta ocasión nuestro objetivo es desarrollar una funcionalidad
poco común, así que necesitamos experimentar un poco antes.

La mejor forma de experimentar es hacer pruebas porque como sabéis se
ejecutan en una base de datos aislada. Así que en lugar de ir
directamente a por las vistas, vamos a desarrollar algunas
funcionalidades básicas relacionadas con nuestros modelos Thread y
Message mientras las probamos en pequeños Tests.

Para hacerlo vamos a adoptar una práctica que en ingeniería de software
se conoce como TDD, Test Driven Development (Desarrollo Guiado por
Pruebas). Es una forma de programar muy interesante que se basa en crear
primero la prueba y luego desarrollar la funcionalidad. Cuando el TDD se
hace bien las pruebas te llevan de la mano y desvelan nuevas formas de
hacer las cosas, ya lo veréis.

![]({{cdn}}/django/images/image16.png)

Cuando no tengamos muy claro por dónde empezar, siempre podemos simular
situaciones básicas, como la creación de y consulta de los modelos, así
que vamos a hacerlo:

![]({{cdn}}/django/images/image172.png)

Al crear los usuarios y el hilo como variables de instancia con self,
podemos hacer uso de ellos en cualquier método de la clase, por ejemplo
en un test\_add\_users\_to\_thread:

![]({{cdn}}/django/images/image284.png)

Añadir valores a un campo Many2Many es tan fácil como utilizar su método
add y pasarlos separados por comas. Pero ésto no podemos dejarlo así,
nos falta comprobar si se han añadido correctamente, así que podemos
hacer una simple aserción y comparar si el hilo tiene dos usuarios:

![]({{cdn}}/django/images/image772.png)

Ahora podemos ejecutar el tests de diferentes formas. Por ejemplo, si
queremos ejecutar todos los Tests dentro del fichero tests.py de la app
messenger haríamos:

![]({{cdn}}/django/images/image401.png)

Si en cambio queremos ejecutar sólo los de la clase ThreadTestCase
haríamos:

![]({{cdn}}/django/images/image369.png)

Y si sólo quisiéramos ejecutar el test que acabamos de crear haríamos:

![]({{cdn}}/django/images/image592.png)

Esto es útil cuando tenemos muchas Clases y tests diferentes, pero en
nuestro caso tendremos poquitos, así que utilizaremos siempre la primera
forma.

Sea como sea el Test valida correctamente:

![]({{cdn}}/django/images/image771.png)

Por lo que sabemos que en efecto, esta forma de añadir Usuarios a un
Hilo funciona.

¿Qué os parece ahora crear un test para recuperar un hilo ya existente a
partir de sus usuarios? La forma más fácil de filtrar por dos usuarios,
es simplemente anidar dos filtros de la siguiente forma:

![]({{cdn}}/django/images/image922.png)

Ahora podemos hacer una aserción que compruebe si el Hilo donde hemos
añadido los usuarios, el que es de instancia, es el mismo al que en
teoría hay en la primera posición del QuerySet que devuelve filter:

![]({{cdn}}/django/images/image358.png)\
![]({{cdn}}/django/images/image482.png)

Pues parece que sí, que de esta forma se puede recuperar el hilo. Por
cierto, no sé si os habéis percatado, pero para cada Test (método que
empieza por test\_) se crea de nuevo la base de datos y se ejecuta el
SetUp, esa es la razón por la que se nos muestra varias veces el
mensaje...

![]({{cdn}}/django/images/image186.png)

Deberíamos comentar esta línea del modelo Profile de “registration” para
que no moleste.

A todo esto, ¿y si intentamos recuperar un hilo que no existe qué
pasaría? ¿El QuerySet que devuelve filter debería estar vacío no? Vamos
a probarlo:

![]({{cdn}}/django/images/image437.png)![]({{cdn}}/django/images/image653.png)

¿Y qué hay de los mensajes? Vamos a trabajar un poco con ellos. Podemos
crearlos y añadirlos prácticamente igual que los usuarios:

![]({{cdn}}/django/images/image579.png)\
![]({{cdn}}/django/images/image59.png)

Si queremos hasta podemos mostrar la conversación:

![]({{cdn}}/django/images/image83.png)\
![]({{cdn}}/django/images/image295.png)

Con estos 4 tests hemos experimentado las acciones esenciales:

-   Crear hilos
-   Asignarles usuarios
-   Recuperar hilos a partir de sus usuarios
-   Crear mensajes, asignarlos a hilos y recuperarlos

¿Puede considerarse esto TDD? Pues todavía no, porque al utilizar un
framework como Django todo lo que hemos hecho hasta ahora nos viene
dado. Sin embargo en las siguientes dos lecciones vamos a mejorar estas
funcionalidades, y ahí si haremos TDD propiamente dicho, creando código
y refactorizando hasta conseguir validar algunos Tests.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>