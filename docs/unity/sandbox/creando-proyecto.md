title: Proyecto Sandbox 3D | Curso Unity desde cero | Hektor Profe

# Sandbox 3D en Unity

En esta unidad vamos a crear un sandbox (o caja de arena), un entorno para experimentar con muchos objetos, físicas, materiales y colisiones. Si sois nuevos en Unity os va a resultar muy revelador y si ya tenéis experiencia os vendrá bien para repasar todo.

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

___
<small class="edited"><i>Última edición: 12 de Abril de 2021</i></small>