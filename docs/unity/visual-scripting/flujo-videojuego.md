title: Visual scripting y flujo del videojuego | Curso Unity desde cero | Hektor Profe

# Flujo del videojuego

En esta unidad vamos a aprender a desarrollar lógica de programación mediante el paquete `Visual Scripting` que viene integrado en Unity desde la versión 2021. Introduciremos poco a poco los diferentes elementos que componen esta tecnología a través de sencillos experimentos y pruebas.

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


___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>