title: Luces, cámara y acción | Curso Unity desde cero | Hektor Profe

# Luces, cámara y acción

El objetivo de esta unidad es familiarizarte con Unity y aprender a moverte por la escena, a manipular objetos, moverlos, rotarlos, escalarlos... Qué son los recursos, los prefabs, los componentes y sus propiedades.

Así que vamos a dar nuestro primer pasito en el mundo del desarrollo de videojuegos, y qué mejor forma de hacerlo que experimentando de primera mano el potencial del motor Unity mientras aprendemos.

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

___
<small class="edited"><i>Última edición: 11 de Abril de 2021</i></small>