title: Componentes y propiedades | Curso Unity desde cero | Hektor Profe

# Componentes y propiedades

Ahora que hemos aprendido sobre la escena y los objetos, vamos a profundizar en las partes que componen los objetos, me refiero a los componentes y sus propiedades.

Vamos a empezar escondiendo el banco de trabajo `Workbench`, lo buscamos en la jeraquía con ese nombre, lo selecionamos y lo desacivamos en el inspector:

![]({{cdn}}/unity/Screenshot_24.png)

Vamos a centrarnos en nuestros cascos, así que nos los vamos a llevar un poco más al medio:

![]({{cdn}}/unity/Screenshot_25.png)

Vamos a fijarnos en el inspector un poco más a fondo al seleccionar uno de los cascos.

Empezando por arriba tenemos una sección con el nombre del objeto, si está activo o no, la posibilidad de añadir tags (etiquetas) y layers (capas) y otras opciones. Los tags sirven para identificar conjuntos de objetos, mientras que las capas están relacionadas con el orden de renderiado:

![]({{cdn}}/unity/Screenshot_26.png)

A continuación encontramos una sección llamada `Transform`, este el primer componente de cualquier objeto, encargado de gestionar los vectores de transformación, a partir de los cuáles se basa el renderizado de gráficos. Existen tres transformaciones básicas:

![]({{cdn}}/unity/Screenshot_27.png)

- **Traslación**: Para mover un objeto en el espacio respecto a un punto de origen (0,0,0).
- **Rotación**: Para mover rotar un objeto en el espacio respecto a una rotación de origen (0,0,0).
- **Escalado**: Para escalar un objeto en el espacio respecto a un escalado de origen (0,0,0).

Las transformaciones son tan esenciales que se encuentran integradas en el propio editor y podemos ejecutarlas sobre los objetos seleccionados utilizando las herramientas de movimiento (W), rotación (E) y escalado (R). Siempre que realicemos un cambio en ellas, veremos los valores numéricos establecidos en los vectores del componente `Transform` mediante tres coordenadas X, Y, Z. Estos valores dentro de los componentes, que podemos modificar, se denominan propiedades.

Podemos usar las herramientas gráficas o modificar directamente las propiedades para transformar los objetos, o incluso hacer clic en los tres puntitos del componente y reiniciar el componente con los valores iniciales de las propiedades, que para los vectores 3D es la coordenada origen (0,0,0):

![]({{cdn}}/unity/Screenshot_28.png)

Un lugar que como vemos queda fuera y por debajo de la escena:

![]({{cdn}}/unity/Screenshot_29.png)

Con `Control+Z` podemos volver a como teníamos antes los valores, y ahora vamos a establecer la rotación del casco azul en (0,0,0):

![]({{cdn}}/unity/Screenshot_30.png)

Para poner el casco en vertical podemos establecer la coordenada X en 90 o con 270, dependiendo de por qué lado queramos dejar el casco levantado:

![]({{cdn}}/unity/Screenshot_31.png)

Si bien el componente `Transform` es el más importante y común de todos los objetos, Unity incluye miles de componentes para realizar todo tipo de tareas. Nuestro casco contiene además:

- **Mesh Filter**: Para establecer el modelo tridimensional del objeto.
- **Mesh Renderer**: Para dibujar el modelo en el espacio.
- **Shader**: Un programita que añade efectos gráficos al modelo.

En cambio el objeto `Main Camera` está formado por otros componentes diferentes, como uno llamado `Camera`, un `Audio Listener` y dos `Scripts`, además del tag `MainCamera` para poder identificarlo rápidamente:

![]({{cdn}}/unity/Screenshot_32.png)

Vamos a hacer un último experimento, seleccionando el casco azul, vamos a dejarlo flotando en el aire:

![]({{cdn}}/unity/Screenshot_33.png)

Si ponemos el juego en marcha (Control+P), el casco se mantiene en el aire porque no contiene ningún tipo de físicas.

Vamos a añadir un componente de cuerpo rígido al casco, para ello presionaremos el botón `Add Component` y buscaremos uno llamado `RigidBody`:

![]({{cdn}}/unity/Screenshot_34.png)

Solo añadiendo este objetos, si ponemos el juego en marcha, el casco empezará a caer. Eso es porque ahora le afecta la gravedad:

![]({{cdn}}/unity/Record_01.gif)

Sin embargo no chocará contra el suelo y eso es porque no tenemos colisiones configuradas.

Si observamos el objeto `Ground` veremos que contiene un componente de tipo `Box Collider`, haciendo clic en la propiedad `Edit Collider` se mostrará el contorno de la colisión del suelo:

![]({{cdn}}/unity/Screenshot_35.png)

Como el suelo ya tiene un colisionador, nos falta añadir otro en el casco azul, así que volvamos a él y añadamos un `collider` de tipo `Mesh Collider`, activando la opción `Convex` para que establezca los vértices en el lugar de la malla del modelo:

![]({{cdn}}/unity/Screenshot_36.png)

Si ahora probamos de nuevo el juego (Control+P):

![]({{cdn}}/unity/Record_02.gif)

Y voalà, ahí tenemos un casco con físicas que colisiona contra el suelo.

A lo largo de esta unidad hemos adquirido soltura para manejar el programa y unos fundamentos, sabemos movernos por el editor y manejar lo esencial. Entendemos como se compone una escena, los recursos, los objetos, los componentes y las propiedades.

Estamos preparados para dar el siguiente paso, crear un sandbox 3D.

___
<small class="edited"><i>Última edición: 11 de Abril de 2021</i></small>