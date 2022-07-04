title: TDD (3): Creando un Model Manager | Curso de Django | Hektor Profe

# TDD (3): Creando un Model Manager

Bien, pues ya sabemos cómo manejar nuestros modelos, incluso hemos
solventado el fallo de que un usuario no pueda enviar mensajes a un hilo
al cual no pertenece, pero sigo echando en falta algo, y eso es una
forma más sencilla de recuperar un Thread a partir de sus usuarios,
digamos que no me gusta lo de añadir filter dos veces. Así que ¿por qué
no creamos una consulta a medida dentro de Thread para recuperar una
instancia a partir de dos usuarios? Vamos a hacerlo.

Ya que hablamos de consultas a medida, lo que necesitamos es filtrar el
QuerySet, y eso es algo que requiere crear nuestro propio Model Manager
o Gestor de Modelos.

Al hacerlo podremos añadir un método como Thread.objects.find(user1,
user2) donde a partir de dos usuarios se busque el hilo de forma fácil y
cómoda.

Vamos a empezar creando un test:

![]({{cdn}}/django/images/image793.png)

Obviamente no va a pasar porque el método todavía no existe, pero esa es
la gracia, refactorizar y pasar el test:

![]({{cdn}}/django/images/image890.png)

Si queremos añadir nuestros propios filtros necesitamos crear un objects
Manager, y eso lo haremos en models.py, podríamos llamarlo
ThreadManager:

![]({{cdn}}/django/images/image729.png)

Ahora asignaremos nuestro Manager al campos objects del modelo Thread:

![]({{cdn}}/django/images/image659.png)

Con esto ya podemos centrarnos en crear el filtro. Es bien fácil, pues
dentro de un ThreadManager, la variable self hace referencia al propio
QuerySet, sólo tenemos que filtrarla así misma y devolver el resultado:

![]({{cdn}}/django/images/image568.png)

Si encontramos algún Thread lo devolvemos, y en caso contrario pues
devolvemos None.

Una vez creado el método, debería funcionarnos:

![]({{cdn}}/django/images/image875.png)

También podríamos comprobar si devuelve None con un hilo inexistente:

![]({{cdn}}/django/images/image794.png)\
![]({{cdn}}/django/images/image49.png)

¿Mucho más fácil que andar haciendo múltiples filtros no?

¿Qué os parece si añadimos una última funcionalidad, a modo de
get\_or\_create, podemos hacer un filtro find\_or\_create, que si no
encuentra un Hilo lo cree automáticamente, lo cual sería la guinda del
pastel y nos facilitaría muchísimo el trabajo. Vamos primero con el
test:

![]({{cdn}}/django/images/image351.png)

Que obviamente no pasará:

![]({{cdn}}/django/images/image265.png)

Vamos a crearlo:

![]({{cdn}}/django/images/image487.png)\
![]({{cdn}}/django/images/image822.png)

Con esto estamos listos para implementar las futuras vistas de nuestra
app con total seguridad. El TDD nos ha llevado de la mano en nuestros
experimentos y nos ha permito desarrollar las distintas funcionalidades
de las que haremos uso en las siguientes lecciones.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>