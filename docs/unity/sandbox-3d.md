title: Sandbox 3D | Curso Unity | Hektor Profe

# Sandbox 3D en Unity

En esta unidad vamos a crear un sandbox (o caja de arena), un entorno para experimentar con muchos objetos, físicas, materiales y colisiones. 

Si sois nuevos en Unity os va a resultar muy revelador y si ya tenéis experiencia os vendrá bien para repasar todo.

## Preparando el proyecto

Utilizando como base el proyecto del escenario, que por algo le pusimos `Sandbox 3D`, vamos a crear una nueva escena con una cámara y una luz en `File > New Scene > Basic (Built In)`:

![]({{cdn}}/unity/Screenshot_38.png)

Lo primero será guardar la escena (Control+S) con el nombre `Sandbox`, dentro del directorio `Scenes` del proyecto.

Si hacemos clic en la `Main Camera` y desplegamos su componente `Camera` observaremos que por defecto se encuentra en la posición (0,1,-10). Ese -10 en el eje Z nos indica que está un poco por delante del punto de origen (0,0,0). En Unity cuanto más grande es el eje Z más profundo y cuanto más pequeño más cerca de nosotros, como si el objeto se saliera de la pantalla:

![]({{cdn}}/unity/Screenshot_39.png)

Vamos a añadir un cubo 3D a la escena `GameObject > 3D Object > Cube`. Al hacerlo un cubo enorme se creará:

![]({{cdn}}/unity/Screenshot_40.png)

En realidad no es tan grande, es solo que se ha añadido muy cerca de la cámara. Si reiniciamos su componente `Transform` volverá a la posición (0,0,0) y lo veremos con más perspectiva:

![]({{cdn}}/unity/Screenshot_41.png)

A todo esto, ¿véis los cuadros que forman el suelo virtual de la escena? Eso son las unidades en las que se divide el mundo. Nuestro cubo tiene un tamaño escalado de (1,1,1) y eso significa que ocupa unida unidad del mundo de ancho, de alto y de profundo. Si lo movemos a la coordenada (0, 0.5, 0) lo posicionaremos perfectamente sobre una de esas unidades del mundo:

![]({{cdn}}/unity/Screenshot_42.png)

¿Por qué 0.5? Pues eso está relacionado con el origen del cubo, que está justo en su centro, que es el lugar desde donde salen las flechas de movimiento. Por lo tanto si lo movemos media unidad en cada dimensión lo alinearemos con las unidades del mundo.

Ok, tenemos un cubo flotando en un suelo virtual, vamos a añadir uno de verdad `GameObject > 3D Object > Plane`. Le reiniciamos la posición a (0,0,0) y lo tendremos justo debajo del cubo:

![]({{cdn}}/unity/Screenshot_43.png)

Por cierto, espero que estéis de acuerdo conmigo en que el fondo por defecto de Unity es feísimo, para cambiarlo por un color sólido más elegante seleccionaremos la cámara y estableceremos la propiedad `Environment` en `Solid Color` y pondremos el color que más os guste, yo pondré un gris oscuro:

![]({{cdn}}/unity/Screenshot_44.png)

Sin embargo este cambio solo afectará a la vista de juego, si queremos que el fondo también sea de un color sólido en el espacio, deberemos configurar las luces del proyecto en `Window > Rendering > Lighting > Environment`, donde pondremos `Skybox Material` en `None`.

Acto seguido iremos a `Edit > Peferences` y en el color `Background` pondremos el color que nos guste más para el fondo, usando el cuentagotas podemos establecer el que pusimos en la cámara.

![]({{cdn}}/unity/Screenshot_45.png)

Nuestra escena se ve muy gris, vamos a dar color a los objetos mediante materiales. Así que vamos a crear uno para el suelo y otro para el cubo.

Abrimos el directorio `Assets/Materials` y ahí clic derecho `Create > Material`, le damos el nombre `Suelo` y lo arrastramos al suelo de la escena:

![]({{cdn}}/unity/Screenshot_46.png)

Por defecto el material tiene el color blanco pero aparece amarillo en el juego debido a la luz. Si seleccionamos el objeto `Directional Light` veremos que ésta tiene un color amarillento ligero. Para lograr una fidelidad completa del color del material deberemos establecer la luz de colorn blanco:

![]({{cdn}}/unity/Screenshot_47.png)

En cuanto al cubo podemos crear un material de otro color y asignarlo, yo le llamaré `Cubo` y tendrá un color anaranjado:

![]({{cdn}}/unity/Screenshot_48.png)

Bien, con estos elementos tenemos algo básico para empezar a trabajar.

## Físicas y materiales

Muy bien, vamos a empear esta lección con un reto:

!!! warning "Ejercicio"
    Crea una esfera de color rojo, reinicia su componente `Transform` y haz que flote encima del borde del cubo.

Más o menos así:

![]({{cdn}}/unity/Screenshot_49.png)

Venga, otro reto:

!!! warning "Ejercicio"
    Añade un componente `RigidBody` a la esfera para activar sus físicas y luego prueba el juego para ver qué ocurre.

Tal que así:

![]({{cdn}}/unity/Record_03.gif)

El caso es que la esfera choca contra el borde del cubo y empieza a rodar hasta caer y desaparecer.

Tengo una idea, para evitar que la bola caiga por los bordes vamos a bordear el suelo para hacer un tope, pero antes haremos el suelo el doble de grande, escalando su tamaño a (2,2,2), así tendremos más espacio para jugar.

![]({{cdn}}/unity/Screenshot_50.png)

Para crear los topes usaremos como base un cubo, que alargándolos y rotaremos hasta conseguir el tamaño deseado.

!!! warning "Ejercicio"
    Crea un cubo, estíralo y posiciónalo a los lados del suelo para evitar que la esfera caiga al vacío. Luego clónalo y bordea el suelo en sus cuatro lados.

Al final debería quedarnos algo así, con 4 cubos haciendo de topes:

![]({{cdn}}/unity/Screenshot_51.png)

Las propiedades de `Transformación` de cada cubo pueden establecerse manualmente para conseguir una alineación y tamaño perfectos:

* (0.0, 0.5, 0.0) (0,0,0) (20,1,1)
* (9.5, 0.5, 0.0) (0,90,0) (20,1,1)
* (0.0, 0.5, 9.5) (0,0,0) (20,1,1)
* (-9.5, 0.5, 0.0) (0,90,0) (20,1,1)

Con esto conseguiremos que el cubo no caiga:

![]({{cdn}}/unity/Record_04.gif)

Vamos a hacer algo interesante, demos al cubo la posición de origen y hagámoslo mucho más alto y el doble de grande, como si fuera una columna en medio del escenario:

![]({{cdn}}/unity/Screenshot_52.png)

Si dejamos caer la esfera desde el borde, ¿os habéis fijado que no rebota contra el suelo? Eso es porque si bien, tiene un material para manejar el aspecto, no tiene un material físico establecido.

![]({{cdn}}/unity/Record_05.gif)

Para crear un material físico haremos clic derecho en `Assets/Materials > Create > Physic Material` y le daremos el nombre `Goma`.

Arrastraremos el material a la esfera y se añadirá al componente `Sphere Collider` en su propiedad `Material` automáticamente:

![]({{cdn}}/unity/Screenshot_53.png)

Si bien este material está configurado para tener una fricción, tenemos que añadir un coheficiente de rebote. Este número debe establecerse entre 0 y 1, siendo 0 un rebote nulo y 1 el máximo, pongamos 1 para ver como queda:
 
![]({{cdn}}/unity/Screenshot_54.png)

Si probamos de nuevo, ahora la esfera rebotará contra el suelo como si fuera de goma:

![]({{cdn}}/unity/Record_06.gif)

El problema es que ahora la "pelota" no frena hasta toparse de nuevo con el pilar. Para solucionarlo debemos indicarle a la "pelota" que debe tener en cuenta una resistencia al movimiento, esta se puede configurar en la propiedad `Angular Drag` del `RigidBody`. Un arrastre angular de 0.05 es muy pequeño, pero si lo subimos por ejemplo a 2.5, el resultado será algo diferente: 

![]({{cdn}}/unity/Screenshot_55.png)

Y este será el nuevo resutado:

![]({{cdn}}/unity/Record_07.gif)

Con esto hemos visto cómo afectan los `materiales físicos` a los objetos y también cómo la propiedad `Angular Drag` resta aceleración a los cuerpos en movimiento.

Poco a poco nos vamos intoduciendo en el sistema de físicas, en la siguiente lección vamos a profundizar un poco más.

## Creando un circuito

En esta clase váis a dar rienda suelta a nuestra imaganción, el objetivo es utilizar diferentes objetos tridimensionales, planos, cubos, esferas y lo que se os ocurra para crear un circuito que la pelota siga hasta llegar a una meta. Practicad y divertiros un rato con las colisiones, las físicas y los materiales.

Os aconsejo crear un objeto vacío llamado `Circuito`, reiniciar su componente `Transform` e introducir dentro todos los elementos del escenario excepto la cámara, las luces y la esfera:

![]({{cdn}}/unity/Screenshot_56.png)

Esto os permitirá manejar todos los elementos del circuito de forma más cómoda:

![]({{cdn}}/unity/Screenshot_57.png)

Así que nada, sed creativos y adelante:

!!! warning "Ejercicio"
    Crea un circuito 3D para la pelota, que mediante una inercia inicial sea capaz de llegar a una meta. Utiliza los atajos de las herramientas de transformación (W,E,R,T) para cambiar el tamaño de los objetos de forma cómoda en conjunto con la tecla `Control` y no dudes en crear conjuntos de objetos y duplicarlos con `Control+D` para ahorrarte trabajo. Experimenta con las propiedades de los materiales, los rebotes y el `Angular Drag` para conseguir completar el circuito. No tiene que quedar pulido, sino divertido.

Aquí tenéis una muestra de mi circuito para que os hagáis una idea, podéis hacer algo mucho más sencillo o complicarlo tanto como queráis, la cuestión es practicar lo aprendido hasta ahora:

![]({{cdn}}/unity/Record_08.gif)

## Paquete Cinemachine

En esta lección vamos a introducir un paquete muy potente de Unity que utilizaremos bastante de ahora en adelante, se trata de `Cinemachine`, una colección de scripts automatizados para controlar cámaras.

Vamos a ir a `Window > Package Manager`, desplegaremos el menú y seleccionaremos `Unity Registry`, buscaremos el paquete `Cinemachine` y lo instalaremos:

![]({{cdn}}/unity/Screenshot_60.png)

Una vez instalado, vamos a crear una cámara muy sencilla desde `GameObject > Cinemachine > Virtual Camera`. La configuraremos con la propiedad `Follow` siguiendo a nuestra esfera, y el `body` será de tipo `Framing Transposer`, un encuadre de trasposición:

![]({{cdn}}/unity/Screenshot_61.png)

Solo habiendo hecho esto tendremos un sistema de seguimiento para la esfera que nos mostrará en todo momento y de forma suavizada una vista en tercera persona.

Si desactivamos la propiedad de la cámara virtual `Game Window Guides` este es el resultado:

![]({{cdn}}/unity/Record_09.gif)

Como véis en poco tiempo se puede empezar a conseguir resultados muy interesantes, pero la verdad es que solo estamos rascando la superfície.

## Creando un ejecutable

En esta lección vamos a ver cómo se genera un ejecuable para compartir nuestro videojuego. Creo que es importante que sepáis hacerlo más pronto que tarde, así que voy a aprovechar la oportunidad para explicarlo muy brevemente.

Con nuestro proyecto abierto, iremos a `File > Build Settings`, aquí añadiremos la escena inicial del proyecto, en nuestro caso será `Sandbox`, las demás podemos borrarlas:

![]({{cdn}}/unity/Screenshot_62.png)

Seleccionaremos la plataforma, en nuestro caso PC, Mac o Linux y presionaremos `Build and Run`, construir y ejecutar. Nos pedirá un directorio, recomiendo crear el binario en un directorio `Bin` dentro del propio proyecto y cuando finalice el proceso podremos disfrutar de nuestro sandbox a pantalla completa y con alta definición:

![]({{cdn}}/unity/Screenshot_63.png)

Podemos navegar al directorio del `Bin` del proyecto fácilmente abriéndo el directorio `Assets` en el explorador y navegando al directorio `Bin`:

![]({{cdn}}/unity/Screenshot_64.png)

Para distribuir el videojuego podemos fácilmente comprimir todos estos ficheros en un algún contenedor como `Zip` o `7-zip` y compartirlo con nuestros amigos:

![]({{cdn}}/unity/Screenshot_65.png)

Como véis el procedimiento es sencillo y en pocos pasos tenemos el ejecutable listo. 

Evidentemente existen más plataformas de exportación y seguro que veremos algunas cuando sepamos más, por ahora lo dejamos aquí.

En la próxima unidad empezaremos con el **Visual Scripting**, lo que nos permitirá transformar nuestro escenario en un entorno interactivo.

<!-- 
A todo esto, ¿que pasaría si mientras el juego está en marcha rotamos el suelo? Vamos a probar:

![]({{cdn}}/unity/Record_08.gif)

Como véis la pelota se mueve en conjunto con el suelo, pero si rotamos demasiado rápido eventualmente la pelota lo atraviesa y cae, como si no pudiera seguir el ritmo de la colisión:

![]({{cdn}}/unity/Record_09.gif)

En la siguiente lección vamos a arreglar este comportamiento.


Cuando movemos demasiado rápido el suelo, su velocidad es tan alta que atraviesa la pelota. Esto sucede porque Unity no realiza cálculos físicos ni detección de colisiones contínuamente.

En breve veremos como solucionarlo, pero antes vamos a unir todos los componentes del escenario menos la pelota en uno llamado `Tablero`.

Lo creamos vacío y lo reiniciamos el `Transform`:

![]({{cdn}}/unity/Screenshot_57.png)

Luego arrastramos los demás objetos dentro:

![]({{cdn}}/unity/Screenshot_56.png)

Y así conseguiremos manejar todos los elementos del tablero en conjunto excepto la pelota:

![]({{cdn}}/unity/Record_10.gif)

Así que... ¿Cómo arreglamos las colisiones y conseguimos que la pelota no atraviese el suelo? Para conseguir unas físicas perfectas entre dos objetos necesitamos que ambos tengan un componente `RigidBody`, pero resulta que el suelo no tiene uno, solo tiene un `Mesh Collider`.

Así que vamos a añadir al suelo ese componente `rigidbody`, y si probamos el juego, al suelo le afectará la gravedad y caerá al vacío, justo igual que la pelota:

![]({{cdn}}/unity/Record_11.gif)

Además veremos en la parte inferior un error:

![]({{cdn}}/unity/Screenshot_58.png)

Nos está avisando de que un `MeshCollider` no convexo con cuerpos rígidos no cinemáticos no está soportado desde Unity 5.

¿Sabéis qué es la `cinemática`? Para entenderla debemos recuperar antes las definiciones de `estática` y `dinámica`. Según la Wikipedia:

    La estática es la rama de la física que analiza los cuerpos en reposo y
    estudia el equilibrio de fuerzas en los sistemas físicos en equilibrio
    estático, es decir, donde las posiciones relativas no varían con el tiempo.

Por otro lado:

    La dinámica es la rama de la física que describe la evolución en el tiempo
    de un sistema físico en relación con los motivos o causas que provocan los
    cambios de estado físico o estado de movimiento.

Finalmente:

    La cinemática es la rama de la mecánica que describe el movimiento de los
    objetos sólidos sin considerar las causas que lo originan y se limita, 
    principalmente, al estudio de la trayectoria en función del tiempo.

En Unity todo esto se traduce en tres tipos de cuerpos:

* `Estáticos`: Cuerpos sin `Rigidbody` que el motor de físicas considera sin movimiento. Se utilizan para colisionadores inamovibles como suelos y paredes.
* `Dinámicos`: Cuerpos con `Rigidbody` y la propiedad `isKinematic` en falso, se mueven de acuerdo a las leyes físicas y el motor se encarga de simularlos.
* `Cinemáticos`: Cuerpos con `Rigidbody` y la propiedad `isKinematic` en verdadero, tiene propiedades físicas y puede moverse, pero es el programador quién se encarga de gestionarlos.

En definitiva, teníamos un suelo estático que no se movía y al añadirle un `Rigidbody` éste se ha vuelto dinámico y Unity lo está controlando por nosotros. Pero si queremos controlar nosotros el suelo conservando las propiedades físicas, entonces debemos indicarle que es cinemático:

![]({{cdn}}/unity/Screenshot_59.png)

En el momento en que tenemos dos cuerpos físicos colisionando, podemos decirle a Unity cómo calcular las físicas entre ellos.
 -->




<!-- 
TODO: Crear un bola, hacer que interactue con el entorno, rotar el plano, que los objetos se muevan usando rigidbodies, fricciones, rebotes, etc.

https://learn.unity.com/tutorial/setting-up-the-game?uv=2020.2&projectId=5f158f1bedbc2a0020e51f0d#
https://www.youtube.com/watch?v=9ZEu_I-ido4&list=PLPV2KyIb3jR53Jce9hP7G5xC4O9AgnOuL&index=3 
-->
___
<small class="edited"><i>Última edición: 12 de Abril de 2021</i></small>