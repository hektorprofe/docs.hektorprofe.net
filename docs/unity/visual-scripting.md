title: Visual Scripting | Curso Unity sin programar | Hektor Profe

# Visual Scripting en Unity

En esta unidad vamos a aprender a desarrollar lógica de programación mediante el paquete `Visual Scripting` que viene integrado en Unity desde la versión 2021. 

Introduciremos poco a poco los diferentes elementos que componen esta tecnología a través de sencillos experimentos y pruebas.

## Flujo del videojuego

En este punto sabemos que los `GameObjects` se forman a base de `componentes`. Los componentes son en realidad códigos de programación que se añaden a los objetos de forma visual con el objetivo de implementar diferentes funcionalidades, como el `rigidbody` que controla las físicas o los `colliders` para las colisiones.

Sin embargo para desarrollar un juego no basta con los componentes predeterminados, sino que es necesario crear tu propia lógica y eso se consigue creando unos componentes personalizados conocidos como `Scripts`, en español `Guiones`, que derivan de un código en lenguaje C# llamado `MonoBehaviour`.

En otras palabras, en Unity, para añadir lógica personalizada a un videojuego es necesario saber el lenguaje C#. Pero no os preocupéis, porque en este curso no utilizaremos C# sino `Visual Scripting`, una interfaz que permite hacer algo parecido mediante diagramas y relaciones. 

Así que vamos a empezar creando una nueva escena `Basic (Built-in)` en nuestro proyecto `Sandbox 3D` que llamaremos `Experimentos`. En ella añadiremos un plano bastante grande (10,1,10) y un cubo, ambos reiniciando préviamente su componente `Transform`:

![]({{cdn}}/unity/Screenshot_66.png)

Ahora vamos a iniciar con un primer experimento, cuyo propósito es entender qué es el flujo de un videojuego y cómo modificarlo para añadir dinamismo e interactividad.

Empezaremos añadiendo un componente al cubo llamado `Script Machine` que significa literalmente `Máquina de guiones`: 

![]({{cdn}}/unity/Screenshot_67.png)

Como su nombre indica, el propósito de esta "máquina" es ejecutar `scripts` o guiones. Estos guiones, pueden definirse en la propia máquina, en cuyo caso se llaman `Embed scripts` o de forma externa en un recurso de tipo `Graph`, que en el contexto significa "guión gráfico". Si creamos un guión externo podemos reutilizarlo en diferentes máquinas, y si lo creamos embebido, se enlazará única y exclusivamente a la máquina actual:

![]({{cdn}}/unity/Screenshot_68.png)

Vamos a crear un guión reutilizable, por lo que haremos clic en la propiedad `Graph > New`. Lo haremos en un nuevo directorio llamado `Graphs` con el nombre `Experimento`. 

Un objeto puede tener múltiples `Script Machines` pero cada una puede ejecutar solo un guión. Establecer un nombre y una descripción a la máquina nos puede servir en el futuro:

![]({{cdn}}/unity/Screenshot_70.png)


Una vez tenemos el guión creado, vamos a editarlo haciendo clic en `Edit Graph`. La primera vez que hagamos esto se instalará en el proyecto el paquete de `Visual Scripting`, y luego se desplegará una ventana llamada `Visual Scripting Graph`. Mi recomendación es añadir esta ventana a la parte inferior porque la vamos a estar utilizando mucho:

![]({{cdn}}/unity/Screenshot_71.png)

Esta ventana, cuyo propósito es diseñar los diagramas de flujo del videojuego se puede maximizar y minimizar de diferentes formas:

* Haciendo clic en `Full Screen`.
* Haciendo doble clic en su interior.
* Con la combinación `Shift+Espacio`.

Podemos movernos por el gráfico presionando la rueda del ratón y hacer zoom con el mismo botón manteniendo `Control`.

Sea como sea en este punto tenemos un `visual script` (guión visual) enlazado al cubo de la escena, en el cuál encontramos dos cajas, una llamada `Start` y otra `Update`, ambas con el texto `Event` debajo y una flecha verde con un `slot`, en español `ranura`.

![]({{cdn}}/unity/Screenshot_72.png)

Si ponemos en marcha el juego (Control+P) mientras tenemos esta ventana visible notaremos algo interesante, y es que la caja llamada `Update` se torna de otro color, lo cuál significa que ese evento se está ejecutando:

![]({{cdn}}/unity/Screenshot_73.png)

Y es que los videojuegos se basan en repetir un ciclo muchas veces por segundo para generar la ilusión de movimiento, es lo que se conoce como `Game Loop` o bucle de juego.

En la [documentación de Unity](https://docs.unity3d.com/Manual/ExecutionOrder.html) podemos encontrar un repaso de todos los eventos que suceden en un objeto desde que empieza su ciclo de vida hasta que termina. Vale la pena repasar esta clasificación aunque sea de forma general:

* **Inicialización**: Se ejecutan una sola vez al crearse el objeto en la escena.
* **Físicas**: Pueden ocurrir más de una vez por fotograma y recalculan las físicas.
* **Evento de entrada**: Capturan la interacción externa del usuario: teclado, mando, gestos, etc.
* **Lógica de juego**: Ejecutados una vez por fotograma, aquí se define la interactividad.
* **Renderizado de escena**: Encargados de renderizar el videojuego cada fotograma.
* **Gizmos**: Para dibujar elementos flotantes de la interfaz en el diseño de la escena.
* **GUI**: Para dibujar elementos flotantes de la interfaz de usuario en el videojuego.
* **Fin de fotograma**: Como su nombre indica gestionan el momento final del fotograma.
* **Pausa**: Son los eventos que permiten controlar la pausa del videojuego.
* **Desmantelamiento**: Encargados de la destrucción del objeto y su limpieza de la memoria.

Según lo que acabamos de aprender, el evento `Start` (empezar) es de inicialización y se ejecuta una única vez al llamar el script, mientras que `Update` (actualizar) es de lógica de juego y se ejecuta una vez por fotograma.

La idea es que si configuramos una acción y la enlazamos a un evento, ésta se ejecutará cuando ocurre el evento, así que con eso en mente vamos a hacer clic derecho en el gráfico, escribimos `rotate` en el buscador y creamos un nodo de tipo `Transform:Rotate (X Angle, Y Angle, Z Angle)`:

![]({{cdn}}/unity/Screenshot_74.png)

Los nodos del gráfico se denominan unidades y la magia, como podéis suponer, al conectar las unidades entre ellas, configurando el flujo del programa para que se ejecuten unas u otras.

Si seleccionamos la unidad que hemos creado, veremos la información sobre su utilización en el inspector del gráfico:

![]({{cdn}}/unity/Screenshot_75.png)

Nos explica que este método aplica una rotación a los diferentes ejes X, Y, Z de un componente `Transform`. 

Además tiene unos inputs:

* `Invoke`: Invocación, de tipo `Flow` (flujo), ejecutará el método de rotación.
* `Target`: Objetivo, de tipo `Transform` (transformación), establece el componente sobre el que se ejecutará el método de rotación. Por defecto el valor es `Self`, haciendo referencia al componente `Transform` del propio cubo.
* `X, Y, Z`: Ángulos de tipo `Float` (flotante), correspondiente a un número decimal con los grados que rotará el `GameObject` en cada eje.

Y un output:

* `Exit`: Salida, de tipo `Flow`, se llamará una vez el método de rotación ha sido invocado.

Si seleccionamos el evento `Update` veremos que tiene una salida llamada `Trigger` (disparador) de tipo `Flow`, que concuerda con la entrada `Invoke` de la unidad de rotación, así que vamos a conectar ambas trazando una línea:

![]({{cdn}}/unity/Screenshot_76.png)

Si ejecutamos el juego (Control+P), veremos algo muy interesante:

![]({{cdn}}/unity/Record_10.gif)

Esta animación nos muestra el flujo del videojuego, como el evento `Update` se está ejecutando en cada fotograma y su salida está fluyendo hasta la unidad de rotación. 

No está sucediendo nada porque los ángulos están establecidos a 0, pero si los cambiamos...

![]({{cdn}}/unity/Record_11.gif)

Como véis el cubo se pone a girar.

Lo que estamos haciendo es modificar una propiedad en tiempo de juego, generando así una ilusión de movimiento. De hecho podemos ver cómo la propiedad `Rotation` del componente `Transform` se está modificando automáticamente:

![]({{cdn}}/unity/Record_12.gif)

Si en lugar de conectar el evento `Update`, conectamos la unidad de rotación al `Start`, ésta debería ejecutarse una única vez. Podemos borrar una relación desde uno de los extremos haciendo clic derecho:

![]({{cdn}}/unity/Screenshot_77.png)

Al probar el juego, si la rotación que hemos establecido es muy pequeña no vamos a notar ninguna diferencia, pero si ponemos por ejemplo 45 entonces veremos como el cubo empieza rotado:

![]({{cdn}}/unity/Screenshot_78.png)

Como hemos visto en este pequeño experimento, en los videojuegos existe un "flujo" que podemos utilizar para conectar las unidades del gráfico.

Este flujo no es más que el bucle de juego, un montón de instrucciones de código ejecutándose unas tras otras, aunque nosotros las veamos representadas gráficamente.

A partir de la siguiente lección empieza el verdadero curso, descansad un poco y le damos caña.

## Buscador de unidades

Retomándolo donde lo dejamos en la lección anterior, quiero profundizar un poco en las unidades.

Y es que cuando vamos a añadir un nodo en el gráfico, aparecen muchas categorías, cada una con infinidad de unidades disponibles:

![]({{cdn}}/unity/Screenshot_79.png)

Empecemos centrándonos en las primeras de la lista, pues hacen referencia a los componentes del `GameObject` donde se ha asignado la `Script Machine`. En nuestro caso el cubo tiene un `Transform`, los `Mesh Filter y Render`, un `Box Collider` y el propio `Script Machine`. Si queremos interactuar con cualquiera de ellos tenemos muchas unidades disponibles. Pero encima de todo también tenemos una categoría llamada `Game Object`, cuyas unidades nos permiten acceder y gestionar los `GameObjects` de la escena.

![]({{cdn}}/unity/Screenshot_80.png)

Volviendo al principio encontramos otras categorías generales, colecciones, controles, eventos, lógica, matemáticas, etc.

Existen más de 20.000 unidades y eso es porque deben cubrir cualquier acción programable. Es imposible saberlas todas de memoria y la idea es buscarlas y utilizarlas a medida que surja la necesidad. La gracia del `Visual Scripting`, es que tenemos a nuestra disposición un potente buscador de unidades y eso facilita la tarea a la hora de investigar.

Por ejemplo, vamos a suponer que después de rotar un grado el eje Y en cada `Update`, queremos desplazar el cubo hacia arriba.

Si movemos el cubo hacia arriba en la escena podemos observar que se modifica el eje Y del vector de posición en el componente `Transform`. Si abrimos el buscador de unidades y buscamos `transform translate`, encontraremos todas las unidades relacionadas con la traslación, la transformación que permite cambiar la posición:

![]({{cdn}}/unity/Screenshot_82.png)

Fijaros que aparece la misma unidad repetidas veces, esto se conoce como sobrecarga de un método, y sucede cuando tenemos diferentes formas de realizar una acción. En nuestro caso vamos a centrarnos en `Transform: Translate (X,Y,Z)` que simplemente toma un vector 3D con el valor a incrementar en cada eje:

![]({{cdn}}/unity/Screenshot_83.png)

Notaréis que por defecto esta unidad se muestra transparente, eso es porque no le llega ningún flujo de código y se considera inactiva.

Podemos unir el flujo de salida en la rotación con la entrada de flujo de la traslación y activarla:

![]({{cdn}}/unity/Screenshot_84.png)

Esto se traduciría como: en cada `Update` ejecutar una rotación y luego una traslación. Vamos a indicar un número muy pequeño al eje Y, por ejemplo `0.1` y veamos el resultado:

![]({{cdn}}/unity/Record_13.gif)

Como véis el cubo empieza a flotar hasta que desaparece. En cada fotograma estamos sumando 0.01 unidades del mundo a su posición Y (recordemos que una unidad del mundo equivale a los cuadrados del escenario), eso son 0.60 unidades de altura cada segundo suponiendo que el videojuego funciona a 60 FPS.

En definitiva el flujo es la corriente vital del script gráfico y fluye a través de las unidades activándolas para ejecutar sus acciones. 

## Tipos de datos

En esta lección vamos a introducir el uso de datos, otro de esos conceptos súmamente importantes, tanto en el desarrollo de videojuegos como en cualquier programa.

Vivimos en la era de la información, y esa información se representa digitalmente en forma de datos de diferentes tipos. Los tipos básicos que encontramos en Unity son:

* Los números enteros, llamados `integers`, no tienen parte decimal y pueden ser negativos.
* Los números decimales, llamados `floats`, tienen parte decimal y pueden ser negativos.
* Los valores lógicos, llamados `booleans`, representan la verdad/falsedad de una sentencia.
* Las cadenas de texto, llamadas `strings`, son para los caracteres y símbolos de escritura.

Luego tenemos tipos de datos estructurados como los `vectores`, que son conjuntos de varios decimales, o los `GameObjects`, que representan estructuras complejas formadas por multitud de información de todo tipo.

Por tanto, dependiendo de la información, deberemos utilizar unos tipos de datos u otros. Si queremos gestionar un número utilizaremos `integers` o `floats`, mientras que si necesitamos manipular un texto, utilizaremos `strings` y para almacenar el resultado de una sentencia lógica cuyo resultado sea verdadero o falso, haremos uso de los `booleans`.

Vamos a realizar algunos experimentos visuales para entender mejor cómo trabajar con los datos.

Cuando nuestro cubo se pone a dar vueltas y a flotar, lo hace porque hay un flujo desde el evento `Update` hasta las unidades de transformación.

¿Qué ocurriría si condicionamos el flujo dependiendo de un valor lógico verdadeo o falso? Vamos a hacerlo:

![]({{cdn}}/unity/Screenshot_85.png)

Lo que hemos conseguido aquí es un controlador que nos permite activar o desactivar el flujo de las transformaciones mediante una condición lógica llamada `if`, esn español `si`:

![]({{cdn}}/unity/Record_14.gif)

Vamos a mostrar en la consola un mensaje que nos diga si el cubo se mueve o no. Como un mensaje es una cadena de texto haremos uso del tipo `string` y lo pasaremos a una unidad que ejecute el método `Debug.Log`:

![]({{cdn}}/unity/Screenshot_86.png)

Dependiendo del valor lógico ahora se muestra un mensaje u otro por la consola:

![]({{cdn}}/unity/Screenshot_87.png)

Como véis con los datos podemos añadir dinamismo y mostrar información, pero hay un problema... Los datos que estamos manejando en nuestro ejemplo son valores literales, y si bien podemos modificarlos desde el `Script Graph` mientras desarrollamos el juego, en el juego final no vamos a contar con esta herramienta.

Si queremos manipular los datos de un videojuego necesitamos almacenarlos y ahí es donde entran en juego las variables, de las cuales hablaremos en la próxima lección.

## Uso de variables

Las variables son la quintaesencia de la programación, son algo tan básico e imprescindible que las llevamos utilizando durante todo el curso sin darnos cuenta.

¿Recordáis las propiedades de los componentes? Pues son variables, almacenes de datos de un tipo determinado identificados con un nombre y cuyo valor, como su nombre indica, puede variar:

![]({{cdn}}/unity/Screenshot_88.png)

Solo en los componentes actuales del cubo encontramos docenas y docenas de variables. Desde el propio nombre del objeto cubo, que es una `string`, la casilla de activar o desactivar el objeto, que es la visualización de un dato lógico `boolean`, los vectores de posición, rotación y escalado formados por varios números que hacen referncia a los ejes X, Y, Z y un largo etcétera. 

En definitiva todos los valores que se pueden modificar son variables.

Las variables existen dentro de lo que se conoce como `scopes`, en español ámbitos. Podemos observar esos ámbitos en el inspector del editor de gráficos:

![]({{cdn}}/unity/Screenshot_89.png)

Estos ámbitos pueden ser a nivel de gráfico, objeto, escena, aplicación y de guardado. El ámbito de gráfico es muy restrictivo, pues abarca únicamente el propio gráfico, mientras que las variables de guardado son accesibles desde cualquier lugar y además son persistentes. No vamos a entrar mucho en detalle porque estas cosas se aprenden mejor con la práctica.

Por lo pronto vamos a crear una variable de gráfico para substituir el literal booleano que controla si se mueve o no el cubo. La vamos a llamar `activarMovimiento` y será de tipo `Boolean`:

![]({{cdn}}/unity/Screenshot_90.png)

Los nombres de las variables deben ser autoexplicativos, sino acabaremos con un videojuego repleto de variables que no sabemos qué hacen. 

Algo interesante es que en `Visual Scripting` no hay restricciones respecto al nombre de las variables, pero igualmente os aconsejo utilizar alguna notación común y ceñiros a ella en el proyecto:

![]({{cdn}}/unity/Screenshot_91.png)

En cualquier caso ya tenemos una variable booleana que puede substituir al valor literal, vamos a arrastrarla al gráfico para utilizarla en lugar de éste:

![]({{cdn}}/unity/Screenshot_93.png)

A efectos prácticos es lo mismo, pero debemos considerar que el valor ahora existe en la memoria bajo el nombre `activarMovimiento` y eso nos permitirá interactuar con él desde otras unidades dentro del gráfico.

Vamos a crear un evento para capturar el momento en que el usuario presiona la tecla `espacio` del teclado. Para ello buscaremos una unidad `on keyboard input`. 

Este evento es especial y no requiere un flujo previo, se iniciará al interactuar con la tecla que nosotros le digamos, ya sea al presionarla (Down), dejar de presionarla (Up) o mantenerla (Hold):

![]({{cdn}}/unity/Screenshot_94.png)

Si conectamos a este evento, una unidad que sea capaz de cambiar el valor de la variable `activarMovimiento` deberíamos ser capaces de controlar cuando empieza a moverse le cubo.

La unidad que nos interesa se llama `set graph variable`. Notad que la unidad de la variable arrastrada se llama `Get Variable`, pues `get` permite recuperar el valor, mientras que `set` permite establecerlo. 

**Podemos arrastrar la variable al gráfico manteniendo la tecla ALT** para crear la unidad `SET` en lugar de `GET`, así que básicamente configuraremos el flujo y estableceremos la variable con un valor literal booleano:

![]({{cdn}}/unity/Screenshot_95.png)

Si probamos el juego, al presionar `ESPACIO` la variable cambiará su valor a verdadero y el cubo empezará a moverse.

Pero vamos un paso más allá, en lugar de usar un literal booleano podemos utilizar como fuente la propia variable `activarMovimiento` negando su valor. Negar un valor lógico da como resultado el contrario y es una operación muy simple, podemos hacerlo mediante una unida `negate`:

![]({{cdn}}/unity/Screenshot_96.png)

Lo que acabmos de hacer nos permite alternar los valores `verdadero` y `falso` de la variable booleana cada vez que presionamos la tecla espacio, pudiendo controlar a voluntad el movimiento del cubo.

Me gusta este experimento porque ilustra, aunque de forma sencilla, el funcionamiento de los videojuegos jugando con las variables y los eventos.

## Variables de objeto

En esta lección vamos a aborar el problema de trabajar con variables a nivel de gráfico y es que en un desarrollo óptimo un gráfico debería encargarse de una tarea y no mezclar acciones. Como decía Julio César, divida y vencerás.

En nuestro caso hemos realizado diferentes acciones en el mismo gráfico así que vamos a dividir su contenido en tres:

* `Controlador`: para activar o desactivar el movimiento.
* `Rotacion`: para añadir la rotación al objeto.
* `Traslacion`: para añadir la traslación al objeto.

Podemos clonar `Assets/Graphs/Experimento` un par de veces y cambiar sus nombres:

![]({{cdn}}/unity/Screenshot_97.png)

Ahora configuraremos tres máquinas de guiones, una para cada gráfico. Podemos simplemente copiar el componente y pegarlo como nuevo dos veces y configurarlos así:

![]({{cdn}}/unity/Screenshot_98.png)

Ahora vamos a establecer el código de cada gráfico para hacerlos independientes entre ellos.

**Controlador**:

![]({{cdn}}/unity/Screenshot_99.png)

**Rotación**:

![]({{cdn}}/unity/Screenshot_101.png)

**Traslación**:

![]({{cdn}}/unity/Screenshot_100.png)


Si probamos el videojuego notaremos que ya no funciona, pese a que el `Controlador` está funcionando y alterna correctamente la variable `Booleana`:

![]({{cdn}}/unity/Record_15.gif)

¿Qué está sucediendo? ¿Por qué no funciona? ¿Recordáis que al principio de la lección os he dicho que íbamos a abordar un problema? Pues aquí tenemos el problema.

La variable que tenemos en los gráficos, llamada `activarMovimiento`, en realidad no es una variable, sino tres variables diferentes con el mismo nombre. Cada una existiendo dentro del gráfico y de forma independiente de las demás.

Por suerte para nosotros, si lo que necesitamos es que las gráficos manipulen una variable común, podemos crearla a nivel del objeto. 

Así que vamos a borrar las tres variables `activarMovimiento` y luego la vamos a añadir de nuevo pero esta vez a nivel de `Objeto` desde el componente `Variables`:

![]({{cdn}}/unity/Screenshot_102.png)

Substituimos la variable a nivel de objeto en los tres gráficos, <u>teniendo en cuenta que ahora en el controlador debemos establecer el valor también a nivel de objeto</u>:

**Controlador**:

![]({{cdn}}/unity/Screenshot_106.png)

**Rotación**:

![]({{cdn}}/unity/Screenshot_104.png)

**Traslación**:

![]({{cdn}}/unity/Screenshot_105.png)

Y si ahora probamos el juego, al utilizar una variable común del objeto, ya funcionará perfectamente:

![]({{cdn}}/unity/Record_16.gif)

De la misma forma que una variable de gráfico no es común entre objetos, una de objetos no es común en la escena, ni una de escena en la aplicación.

Así que como véis el ámbito de las variables es un concepto muy importante y no podéis descuidarlo porque sino, dependiendo de lo que intentéis hacer, no podréis acceder a su información.

## Reutilización de scripts

El objetivo de esta lección es reutilizar nuestros scripts gráficos en diferentes cubos pero logrando un comportamiento ligeramente distinto entre ellos mediante el uso de variables para controlar la velocidad de rotación y traslación.

Así que vamos a crear un par de variables `Vector3` en el objeto llamadas `vectorRotacion` y `vectorTraslacion`, a las que asignaremos unos valores por defecto como los que estamos usando actualmente:

![]({{cdn}}/unity/Screenshot_107.png)

Y utilizaremos estas variables como origen de los datos para transformar el cubo. 

Por eso en lugar de la versión que establece de forma independiente los ejes, cambiaremos a `transform rotate eulers`, que toma como entrada un vector 3D, asignando su entrada al vector como la salida de nuestra variable `velocidadRotacion`:

![]({{cdn}}/unity/Screenshot_109.png)

Y haremos exactamente lo mismo para la traslación, cambiando la unidad de transformación a una versión que tome un vector3 como entrada:

![]({{cdn}}/unity/Screenshot_111.png)

Ahora viene la parte divertida, vamos a clonar el cubo con diferentes colores y tamaños. En mi ejemplo he hecho uno naranja 3*3*3, uno azul 2*2*2 y uno rojo 1*1*1:

![]({{cdn}}/unity/Screenshot_112.png)

Si presionamos espacio los tres cubos empezarán a flotar, pero lo interesante es que podemos controla de forma independencia la velocidad de rotación y traslación de cada uno ajustando las variables que hemos creado:

![]({{cdn}}/unity/Record_17.gif)

Como véis reutilizar scripts es la clave a la hora de impementar funcionalidades comunes en los objetos.

Pero, ¿y si quisiéramos añadir una pequeña variación a uno de los tres cubos? Por ejemplo, que en lugar de mover el cubo rojo al presionar espacio, tengamos que presionar la tecla R?

Para conseguir esta variación debemos crear una copia `embebida` del script `Controlador` en el cubo rojo y modificarla.

Esto se consigue presionando el botón `Convert`:

![]({{cdn}}/unity/Screenshot_113.png)

Al hacerlo el gráfico de los recursos `Assets/Graphs/Controlador` se copiará como un recurso embebido dentro del propio objeto y podremos editarlo a nuestro gusto, siendo éste independiente de los demás cubos:

![]({{cdn}}/unity/Screenshot_114.png)

Simplemente editaremos el gráfico y cambiaremos la tecla `Space` por la letra `R`:

![]({{cdn}}/unity/Screenshot_115.png)

Sin más complicación ahora podremos controlar cuando se mueven los cubos naranja y azul con el espacio, y el rojo con la R:

![]({{cdn}}/unity/Record_18.gif)

Con esto ya sabemos lo básico sobre reutilizar scripts gráficos y cómo sobreescribir comportamientos específicos.

## Grupos y superunidades

En esta última lección vamos a introducir brevemente el uso de los grupos y las superunidades, dos formas de organizar y reutilizar contenido en los scripts gráficos.

Los grupos son una forma de gestionar conjuntos de unidades, se basa en envolver unas cuantas unidades con el ratón mientras presionamos con la tecla `Control`:

![]({{cdn}}/unity/Screenshot_116.png)

Una vez tenemos un grupo podemos manipular en conjunto las unidades que lo forman, también podemos asignarle un nombre, una descripción y un color:

![]({{cdn}}/unity/Screenshot_117.png)

Crear grupos es una forma visual de organizar los scripts y comprobar de un vistazo su funcionamiento.

Por otro lado, con el objetivo de simplificar y reutilizar los gráficos, las superunidades nos permiten agrupar varias unidades en una única maestra identificada con un nombre, vienen a substituir las funciones de código.

Hagamos un ejemplo para ilustrar el funcionamiento.

En el script `Controlador` podemos substituir todo el proceso de alternar la variable en una única `superunidad` llamada `alternarMovimiento`. Para crearla hacemos clic derecho y buscamos `superunit` en el navegador:

![]({{cdn}}/unity/Screenshot_118.png)

Podemos acceder a la superunidad haciendo doble clic en ella y dentro veremos que tiene un `input` y un `output`, ahí definiremos los datos que entran y salen de la superunidad.

La entrada de nuestra superunidad corresponde al flujo que se genera al presionar una tecla, así que vamos a crear un disparador de entrada con el nombre `Flujo`:

![]({{cdn}}/unity/Screenshot_119.png)

Tenemos que llevarnos las unidades de fuera a la superunidad y configurar el flujo de entrada:

![]({{cdn}}/unity/Screenshot_120.png)

Y desde conectar el flujo del evento a la superunidad:

![]({{cdn}}/unity/Screenshot_121.png)

Como en esta superunidad no tenemos un `output` de salida, ya la tenemos lista y si probamos el juego hará lo mismo pero habremos simplicado ligeramente el gráfico.

![]({{cdn}}/unity/Record_19.gif)

A lo largo del curso trabajaremos activamente con los grupos y las superunidades.

Sea como sea con esto acabamos el primer bloque donde hemos repasado los conceptos básicos del desarrollo y a partir de ahora toca crear videojuegos.

___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>