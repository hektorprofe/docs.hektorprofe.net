title: Paginación de resultados en ListView | Curso de Django | Hektor Profe

# Paginación de resultados en ListView

A no ser que sobreescribamos el método get\_queryset de una ListView
para filtrarla (de forma similar a como sobreescribimos el get\_object
en una DetailView), ésta por defecto devolverá todas las instancias.

Cuando trabajamos con poca información no pasa nada, pero imaginad si
tuviéramos cientos o miles de instancias… Para estos casos existe la
paginación, un sistema que permite dividir los registros en distintas
páginas para navegar sin saturarnos de datos.

Sinceramente configurar la paginación en una vista tradicional es,
hablando en plata, un coñazo, pero con las ListView es mega fácil. Sólo
debemos definir un atributo llamado “paginate\_by” donde estableceremos
el número de registros por página:

![]({{cdn}}/django/images/image448.png)

Si volvemos a la lista de perfiles ahora veremos que nos aparecen solo
dos:

![]({{cdn}}/django/images/image413.png)

Esto es debido a que estamos mostrando la primera página del paginador.
Para cargar la segunda página debemos añadir un parámetro GET llamado
page con el número 2 en la url:

![]({{cdn}}/django/images/image206.png)

![]({{cdn}}/django/images/image502.png)

Bueno, pues así es como gestiona automáticamente nuestra ListView la
paginación. Sólo debemos maquetar un menú de paginación en la parte
inferior ayudándonos de los Template Tags del paginador. Esto sí que es
un poco pesado, por eso os lo voy a dar hecho, podéis copiar el que
tengo en mi Gist. Lo he creado tomando como base la paginación de
Bootstrap:

[https://gist.github.com/hcosta/1c29ac407b6d23afab505ab8cb1ccb36](https://gist.github.com/hcosta/1c29ac407b6d23afab505ab8cb1ccb36) 

![]({{cdn}}/django/images/image314.png)

![]({{cdn}}/django/images/image196.png)

Empezando por arriba, el Tag is\_paginated nos sirve para saber si
debemos mostrar la paginación. Si por ejemplo paginásemos a 10
resultados no nos aparecería porque sólo tenemos 4 perfiles.

Ya en el menú, todo lo referente al paginador se gestiona en un objeto
llamado page\_obj que podemos consultar en todo momento. Este incluye
atributos has\_previous y has\_next para comprobar si la página actual
tiene una página anterior y siguiente. Si es que sí nos permite
recuperarlas con previous\_page\_number y next\_page\_number. Respecto
al bucle de páginas, lo podemos conseguir iterando con un for el
atributo page\_range. Ya como añadido podemos consultar number para
comprobar la página actual y determinar si añadir o no una clase activa
al número. Sólo hay que jugar un poco con todos estos elementos para
maquetar un paginador la mar de interesante.

Por cierto, no sé si os habréis fijado pero tenemos un warning al usar
el paginador:

![]({{cdn}}/django/images/image556.png)

Esto es debido a que no tenemos una ordenación por defecto para nuestros
perfiles. Solucionarlo es tan fácil como volver a registration/models y
añadir un campo Meta order:

![]({{cdn}}/django/images/image836.png)

Si queréis más información os dejo enlaces a la documentación oficial,
tanto de Django como de Bootstrap: \
[https://docs.djangoproject.com/en/dev/topics/pagination/](https://docs.djangoproject.com/en/dev/topics/pagination/) \
[https://getbootstrap.com/docs/4.0/components/pagination/](https://getbootstrap.com/docs/4.0/components/pagination/) 

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>