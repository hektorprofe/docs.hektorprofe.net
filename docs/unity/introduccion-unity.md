title: Introducción al motor | Curso Unity sin programar | Hektor Profe

# Introducción al uso del motor

El objetivo de esta unidad es familiarizarte con Unity y aprender a moverte por la escena, a manipular objetos, moverlos, rotarlos, escalarlos... Qué son los recursos, los prefabs, los componentes y sus propiedades.

## Luces, cámara y acción

Muy bien pues vamos a dar nuestro primer pasito en el mundo del desarrollo de videojuegos, y qué mejor forma de hacerlo que experimentando de primera mano el potencial del motor Unity mientras aprendemos.

Vamos a crear un nuevo proyecto `Universal Render Pipeline` con la versión `Unity 2021` o mayor, pues es a partir de ésta que encontramos Visual Scripting incluido y más adelante haremos uso de él, y le vamos a llamar `Sandbox 3D`.

![]({{cdn}}/unity/Screenshot_1.png)

_Nota: En caso de que este proyecto se elimina en futuras versiones, dejaré una copia en los recursos de la lección. Se puede abrir desde `Unity Hub` usando el botón ADD._

Unity está dividido en subventanas llamadas docks. Estas ventanitas se pueden arrastrar y posicionar donde nosotros queramos, podemos añadir de nuevas y quitarlas. Sin embargo existen disposiciones por defecto que nos facilitan el trabajo. Si os habéis hecho un lío, la disposición por defecto se puede recargar desde `Window > Layouts > Default`. Podemos guardar nuestras disposiciones con un nombre y reutilizarlas en otros proyectos.

Usando la disposición por defecto, de izquierda a derecha y de arriba hacia abajo, encontramos las ventanas más importantes:

- La jeraquía de objetos de la escena
- La vista de escena y de juego
- El inspector de objetos
- El explorador de recursos y la consola

Estas ventanas son las más esenciales y prácticamente siempre las tendremos abiertas, hablaremos de ellas a medida que las utilicemos.

![]({{cdn}}/unity/Screenshot_2.png)

Por lo pronto vemos una paqueña escena a lo lejos. Si presionamos el botón `Play`, aparecerá un pequeño escenario.

Al presionar este botón entraremos en el modo de reproducción del juego y éste nos mostrará lo que ve la cámara de la escena.

Notad que cuando el videojueto se pone en marcha puede tardar una cantidad considerable de tiempo, podemos reducir prácticamente la totalidad del tiempo de precarga haciendo una sencilla configuración en el proyecto desde `Edit > Project Settings > Edit` y hacia abajo activamos la opción `Enter Play Mode Options` y `Reload Scene` (para más detalles de qué hacen estas opciones un [enlace](https://docs.unity3d.com/2021.1/Documentation/Manual/ConfigurableEnterPlayMode.html)):

![]({{cdn}}/unity/Screenshot_151.png)

Ahora, lo primero que debéis recordad es que, cualquier cambio realizado en la escena durante el modo de reproducción, se revertirá al salir de él. Os aconsejo tintar la ventana durante este modo para nunca confundiros y luego perder el trabajo. A mi me gusta poner un color que se vea bien, como un azul chillón.

Para hacerlo vamos a salir del modo de reproducción, iremos a `Edit > Preferences > General > Playmode tint` y seleccionaremos nuestro color. Así al poner en marcha el juego, la interfaz se mostrará tintada, y creedme que este truco os ahorrará mucho tiempo:

![]({{cdn}}/unity/Screenshot_3.png)

Saliendo del modo de reproducción, vapodemos acercarnos un poco a la escena con la rueda del ratón:

![]({{cdn}}/unity/Screenshot_4.png)

¿Véis el escenario de atrezzo que tenemos? Es como el escenario de una película, podemos movernos por ahí libremente utilizando la combinación `Clic derecho + AWSD`, incluso podemos modificar la velocidad de movimiento con `Control + Ruedecita del ratón`. Como véis en cierta forma los videojuegos en Unity se crean como una película. Tenemos el escenario, el atrezzo y la cámara enfocando el lugar que mostraremos al jugador.

Si abrimos la jerarquía de objetos y hacemos doble clic en el objeto `Main Camera` nos posicionaremos sobre él. Utilizando las `flechas azul, roja y verde` podemos cambiar su posición. 

Cuando movemos un objeto por la escena estamos haciendo uso de la herramienta de movimiento, representada por una cruz con flechas en el menú superior. Podemos activar esta herramienta presionando la `tecla W` del teclado. Así mismo podemos volver a la herramienta de vista presionando la manita o la `tecla Q`. Si activamos la herramienta de rotación, con la `tecla E` podemos cambiar la dirección de la cámara. Tened en cuenta que tenemos tres rotaciones, una por cada dimensión: horizontal, vertical y profundidad:

![]({{cdn}}/unity/Screenshot_5.png)

Por cierto, si arrastramos la ventana `Game` a un lado, podemos editar la escena mientras vemos en grande el resultado del juego en funcionamiento. Me gusta posicionar la jeraquía abajo y dejar espacio arriba para las ventanas `Game` y `Scene`, esto me permite trabajar con más perspectiva:

![]({{cdn}}/unity/Screenshot_6.png)

De forma similar al objeto cámara, también tenemos las luces de la escena, que nos permite iluminar el escenario. Son fundamentales, sin ellas no veríamos ningún color en el videojuego.

En esta escena tenemos dos fuentes de luz configuradas, la primera es una luz global en la parte superior. Se corresponde al objeto `Directional Light`, y si lo desactivamos básicamente veremos la escena mucho más oscura:

![]({{cdn}}/unity/Screenshot_7.png)

Luego tenemos un objeto foco, que podemos seleccionar desde la jerarquía `Example Assets > Props > Construction Light Low > Spot Light`. A diferencia de una luz direccional que da luz de forma global a la escena, una spot light está dirigida a un punto concreto. Si la desactivamos apreciaremos mejor donde está enfocando:

![]({{cdn}}/unity/Screenshot_8.png)

Por ahora vamos a dejarlo aquí, pero antes activemos de nuevo las luces del escenario:

![]({{cdn}}/unity/Screenshot_9.png)

## Objetos, recursos y prefabs

Antes hemos interactuado con algunos objetos como la cámara y las luces, pero esos no son los únicos objetos de la escena, la realidad es que todo lo que existe en la escena SON objetos.

Fijémonos en la jeraquía, ¿véis el cubo a la izquierda de cada elemento? Eso nos indica que es un objeto de juego, en inglés `GameObject`:

![]({{cdn}}/unity/Screenshot_10.png)

¿Y véis que hay objetos que tienen varios niveles? Eso significa que son objetos compuestos de otros objetos, como un padre con muchos hijos enlazados a él:

![]({{cdn}}/unity/Screenshot_37.png)

Muy bien, pues para que estos objetos existan, debemos añadirlos de alguna forma y de algún sitio, ¿no? Pues ese sitio son los recursos del proyecto:

![]({{cdn}}/unity/Screenshot_11.png)

Los recursos, o assets en inglés, contienen todo tipo de información. Desde los modelos 3D de los objetos, los materiales, las texturas, los sonidos, los ficheros de configuración, las bases de datos y un larguísimo etcétera, que incluye incluso, la información de las propias escenas.

Y es que en un proyecto poemos tener múltiples escenas. La escena actual se llama `SampleScene` y podemos guardarla con `Control+S`. El recurso de esta escena se encuentra en la carpeta `Assets/Scenes`. Otros recursos se encuentran en otras carpetas bien organizadas, como `ExampleAssets`, `Materials`, `Presets`, `Scripts`, etc.

Vamos a acercarnos un poco a la mesa de trabajo de la escena, y utilizando la herramienta de movimiento (W), vamos a seleccionar ese casco amarillo. Si os aparecen unas bolas enormes es debido a los iconos de ayuda de la interfaz de Unity conocidos como Gizmos. Podemos hacerlos más pequeños:

![]({{cdn}}/unity/Screenshot_12.png)

Y desactivar esas líneas amarillos que tienen que ver con las luces desactivando los Gizmos de `LightProbeGroup`:

![]({{cdn}}/unity/Screenshot_13.png)

Así veremos simplemente el casco seleccionado con un borde naranja:

![]({{cdn}}/unity/Screenshot_14.png)

Este casco es, como os comenté al princpio, un `GameObject`, concretamente uno llamado `Safety Hat`, y también podemos moverlo mediante las flechas y el cuadrado (W) y rotarlo (E):

![]({{cdn}}/unity/Screenshot_15.png)

Vamos a crear otro casco a partir de su recurso. Para hacerlo buscaremos en la ventana de recursos, en `Models` el modelo `safetyhat` y lo arrastraremos al suelo de la escena:

![]({{cdn}}/unity/Screenshot_16.png)

Como véis por defecto este casco es gris, eso es porque no tiene una textura. En el directorio `Textures\Props\HardHat` encontramos tres texturas para nuestro casco, vamos a arrastrar la azul al casco:

![]({{cdn}}/unity/Screenshot_17.png)

Como véis, en el momento en que arrastramos un recurso a la escena se crea un objeto para representarlo.

Si quisiéramos crear otro casco azul, podríamos repetir el proceso o duplicarlo, seleccionando el objeto `safetyhat` en la jeraquía y presionando `Control+D`:

![]({{cdn}}/unity/Screenshot_18.png)

Pero quiero que tengáis presente una cosa, estos dos cascos son objetos independientes entre ellos. Si arrastramos la textura rosa a uno de ellos, los cambios no afectan al otro:

![]({{cdn}}/unity/Screenshot_19.png)

Sin embargo ese no es el caso de los `Prefabs`. ¿Véis en la jerarquía que hay algunos objetos cuyo cubo es de color azul? Eso significa que son `Prefabs`, plantillas para generar objetos iguales.

Si navegamos al directorio `Assets/Prefabs` veremos algunos. Por ejemplo los botes de pintura. Vamos a arrastrar algunos a la escena:

![]({{cdn}}/unity/Screenshot_20.png)

La diferencia entre tener objetos independientes y prefabs, es que éstos últimos están enlazados a una plantilla común, o dicho de otra forma, a un objeto original.

Si hacemos doble clic en el prefab de los botes de colores, se abrirá de forma independiente:

![]({{cdn}}/unity/Screenshot_21.png)

Si modificamos algún elemento de este Prefab, por ejemplo modificando el tamaño de los botes y la brocha (R), rotándolos un poco y moviéndolos de sitio...

![]({{cdn}}/unity/Screenshot_22.png)

Si ahora volvemos a la escena haciendo clic en `Screnes > Paint Supplies` de la parte superior, veremos que se han modificado todos los botes de pintura al modificar nosotros el original.

![]({{cdn}}/unity/Screenshot_23.png)

Después de este experimento queda clara la idea de que los `objetos` se crean a partir de `recursos` y pueden ser independientes o estar vinculados a un `prefab`.

Poco a poco ahondaremos en estos temas e incluso crearemos nuestros propios prefabs.

## Componentes y propiedades

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