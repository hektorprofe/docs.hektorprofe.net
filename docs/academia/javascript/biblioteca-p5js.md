title: Introducción a la biblioteca p5.js | Hektor Profe
description: Descubre el mundo de la programación desde cero a medida que la aplicas en todo tipo de experimentos visuales, prácticos y divertidos.

# Introducción a la biblioteca p5.js

Bienvenidos a esta introducción a la programación utilizando la biblioteca **p5**, cuyo propósito nos lo explican sus creadores en la página web [p5js.org](https://p5js.org/es/):

```
[...] Se trata de una biblioteca creada con el objetivo de hacer la programación
accesible a artistas, diseñadores, educadores y principiantes; reinterpretando 
la web actual y ofreciendo un conjunto completo de funcionalidades para dibujar 
e interactuar con los componentes HTML5 del navegador, como por ejemplo 
textos, entradas de usuario, vídeos, cámara y sonidos.
```

En definitiva con ella se pueden dibujar líneas, figuras, colores, textos... Y esa es la razón por la que nos puede ayudar mucho a entender la programación; todos sabemos que una imagen vale más que mil palabras. 

¿Os imagináis aprender conceptos como las variables, las condiciones o los bucles gráficamente? ¿Utilizando figuras geométricas? ¿Generando animaciones de esas mismas figuras para moverlas por la pantalla haciendo todo tipo de cosas? Pues de eso trata esta serie de cursos.

Para crear un proyecto con **p5.js** podemos hacerlo de dos formas:

* **A través del editor online** en la dirección [https://editor.p5js.org](https://editor.p5js.org/).
* **Utilizando un editor** en vuestro propio ordenador siguiendo los pasos de la sección [Empezar](https://p5js.org/es/get-started/) de la página oficial.

Os recomiendo la primera opción a no ser que tengáis experiencia en desarrollo web, sólo hay que crear una cuenta donde pone **Signup** y ya podréis guardar vuestros proyectos en la nube de forma gratuita. 

Si estamos identificados [en el editor online](https://editor.p5js.org/) podemos crear un nuevo proyecto, asignarle un nombre (por ejemplo *01 - Hola mundo*) y guardarlo. Para recuperarlo lo haremos desde el apartado **My Account** > **My Sketches**.

Un **sketch** es un bosquejo o dibujo, de ahí que el fichero principal de un proyecto en **p5** se llame **sketch.js**, indicando la extensión **.js** que el fichero contiene código en lenguaje JavaScript, pero no os preocupéis por eso.

Por ahora fijaos que por defecto este fichero **sketch.js** contiene un código:

`01 - Hola mundo/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
```


Todavía no sabemos para qué sirve pero pronto lo descubriremos, pinchad el botón superior para ejecutarlo, veréis que a la derecha se dibuja un cuadrado gris.

No os sintáis abrumados por estás instrucciones, al fin y al cabo este curso es para absolutos principiantes. Quiero que os enfoquéis en la traducción y significado de las palabras que aparecen:

* **function** -> función
* **setup** -> preparar
* **createCanvas** -> crear lienzo
* **draw** -> dibujar
* **background** -> fondo

Si unimos estos términos utilizando nuestra lógica podemos entender que tenemos dos funciones o comandos:

* **setup** para preparar el programa y crear un lienzo
* **draw** para dibujar o pintar un fondo en el lienzo

La biblioteca **p5** es muy intuitiva y sabiendo un poco de inglés podemos hacernos una idea de lo que hacen todas las instrucciones. En este caso como podemos deducir se ha preparado un espacio para dibujar, un lienzo, en el cuál hemos dibujado el fondo con un color.

¿Ahora qué creéis que son los números que aparecen entre paréntesis en las instrucciones **createCanvas** y **background**? Probad a cambiarlos y veréis:

* **createCanvas(ancho, alto)**: tamaño del lienzo
* **background(color)**: código del color

Evidentemente todo esto no me lo estoy inventando yo, son los creadores de esta biblioteca lo que han programado estas instrucciones para que podamos utilizarlas de forma intuitiva. 

Si queréis aprender más sobre las funcionalidades de **p5** podéis consultar la [referencia oficial](https://p5js.org/es/reference/) que se encuentra perfectamente traducida al español, además os dejaré [una chuleta](https://github.com/bmoren/p5js-cheat-sheet) muy útil con las instrucciones básicas de la biblioteca, aunque ésta sí se encuentra en inglés.

En fin, no le deis muchas vueltas porque a lo largo del curso veremos en profundidad estos conceptos y os iréis familiarizando con ellos poco a poco.

## Escribiendo código

Como el curso gira en torno a la biblioteca **p5** y ésta ha sido desarrollada en JavaScript, todo el código que vamos a escribir será en ese lenguaje de programación.

Sin embargo este no es el único lenguaje que existe, hay muchos otros, como C y Java, pasando por C++, Python o PHP por poner algunos ejemplos. Cada uno tiene sus pros y sus contras pero todos se fundamentan en unos conceptos básicos comunes, por eso **es muy importante recordar siempre que la programación no se trata de memorizar sino de entender**, porque independientemente del lenguaje que aprendas éste siempre te servirá como base para los demás.

Así que no perdáis el tiempo memorizando las instrucciones de este curso, siempre podéis repasar los ejemplos, la documentación o la chuleta que os déjé en la lección anterior. Vosotros centraros en entender lo mejor que podáis lo que hace cada instrucción.

Dicho lo cuál voy a enseñaros lo más básico para escribir código JavaScript, que por cierto, del lenguaje Java no tiene nada a parte del nombre.

### Comentarios de código

Ya expliqué detenidamente lo que es JavaScript en mi curso para principiantes, por eso me limitaré a comentar que es un lenguaje enfocado a los navagadores web y como todos tenemos un navegador no necesitamos instalar nada para utilizarlo.

Por ejemplo, vamos a empezar con los comentarios, una parte fundamental que nos sirve para explicar y detallar el código que escribimos. Hay dos formas de escribirlos, en una línea o en bloque:

`02 - Escribiendo código/sketch.js`
```javascript
// Este comentario ocupa una línea
Esto no es un comentario y dará error si lo ejecuto

/* Este comentario en bloque desactiva todo el código
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
*/
```


Durante el curso yo no voy a poner comentarios en el código, pero os animo a que vosotros sí lo hagáis con vuestras propias palabras en las partes que os cuesten más de entender.

### Mensajes en la consola

Escribir código es una tarea opaca por naturaleza y la única forma de ver si funciona es a base de prueba y error, por eso algunas veces necesitaremos mostrar valores y textos que nos confirmen que se ejecutan determinados códigos.

Una forma de hacerlo es a través de la consola que encontraremos en la parte inferior del editor, así como en las **Hrramientas para desarrolladores** que suelen tener los navegadores.

Por ejemplo podemos imprimir un mensaje en la consola justo antes de crear el canvas y otro luego utilizando la instrucción **print** que tiene **p5**: 

```javascript
function setup() {
  print("Ahora se creará el canvas")
  createCanvas(400, 400);
}
```

Por cierto, algunos programadores ponen el punto y coma al final de una instrucción por influencia de otros lenguajes o porque les ayuda a identificar mejor las líneas, pero en JavaScript no es obligatorio su uso.

### Mensajes de alerta

Otra forma de mostrar mensajes es a través de las alertas del navegador, son ventanitas emergentes que aparecen en medio de la pantalla. Lo malo que tienen es que bloquean el código hasta que se confirman. Se utilizan con la instrucción **alert** de JavaScript:

```javascript
function setup() {
  alert("Ahora se creará el canvas")
  createCanvas(400, 400);
}
```

Iremos practicando estos conceptos a lo largo del curso así que pasemos a algo más interesante.

## Dibujando figuras

Por fin ha llegado el momento que todos estábamos esperando, la hora de meter las manos en la masa y empezar a dibujar en ese lienzo que nos proporciona **p5**.

Tenemos multitud de instrucciones para dibujar en nuestro lienzo, vamos a ver algunas de ellas en [la referencia](https://p5js.org/es/reference/) de **p5**. Empecemos por algo tan sencillo como una línea con la función **line()**.

En la documentación nos dan algunos ejempos sobre cómo utilizar esta instrucción, básicamente se tienen que indicar dos puntos dentro del eje de coordenadas del lienzo para dibujar una línea de un punto al otro... Pero un momento, ¿qué demonios es un eje de coordenadas? Tranquilos, que ahora os lo explico muy rápidamente.

### El eje de coordenadas

Un eje de coordenadas es un sistema donde podemos determinar la posición de puntos y objetos geométricos. En nuestro caso tenemos un canvas con una anchura y altura de 400 píxeles que nos sirve como base, considerando que su esquina superior izquierda es el punto origen con coordenada (0, 0) haciendo referencia a los píxeles 0 y 0 en los ejes X (ancho) e Y (alto) respectivamente. Por otra parte sabiendo que el canvas hace 400x400, el punto en su esquina inferior derecha se encontraría ni más ni menos que en la coordenada (400, 400). 

Sabiendo todo esto lo que nos está pidiendo la función **line()** son los valores de la coordenada X e Y del punto donde empezará la recta (x1, y1) y la coordenada donde finalizará (x2, y2):

`03 - Figuras/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  line(0, 0, 400, 400);
  // line(0, 400, 400, 0);
  // line(0, 200, 400, 200);
  // line(200, 0, 200, 400);
}
```


###  Dibujando un rectángulo

Sabiendo cómo se dibujan rectas podríamos dibujar cualquier polígono, pero **p5** nos proporciona funciones para ahorrarnos trabajo. Por ejemplo para dibujar un rectángulo podemos utilizar la función **rect()** que nos pide una coordenada inicial y luego una anchura y altura para el rectángulo:

```javascript
function draw() {
  background(220);
  rect(0, 0, 200, 200);
}
```

Este rectángulo o más bien cuadrado ocupa una cuarta parte del lienzo. ¿Qué pasaría si luego dibujamos otro cuadrado que ocupe todo el lienzo?

```javascript
function draw() {
  background(220);
  rect(0, 0, 200, 200);
  rect(0, 0, 400, 400);
}
```

Pues como véis se dibuja encima del pequeño haciéndolo desaparecer. Esto nos enseña que cuando dibujamos en el canvas, las formas van quedando abajo como por capas. Si queremos ver ambos cuadrados en el lienzo, entonces tendremos que dibujar primero el grande y luego el pequeño:

```javascript
function draw() {
  background(220);
  rect(0, 0, 400, 400);
  rect(0, 0, 200, 200);
}
```

Con esto es suficiente para empezar, si queréis aprender más por vuestra cuenta recordad que [en la referencia](https://p5js.org/es/reference/) tenéis todo lo necesario.

## Colores y rellenos

¿Qué sería del arte sin los colores? **p5** nos ofrece un montón de instrucciones para manejar colores, vamos a introducirnos en el tema con las más básicas, sin embargo para entender bien cómo se utilizan los colores tenemos que aprender antes qué es la escala de grises y el código RGB.

### Escala de grises

Empecemos un proyecto vacío y vamos a centrarnos en ese fondo que por defecto es de color gris:

`04 - Colores/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
```


El número 220 que nos aparece por defecto es un valor numérico que hace referencia a un color en una escala de grises. En esa escala el 0 es el color negro y el 255 representa el blanco. Los valores intermedios determinan la intensidad de color entre el negro y el blanco, así que como resultado tenemos 256 colores (8 bits) en la escala de grises contando el cero.

### Código RGB

Ahora bien, si en lugar de grises queremos manejar colores reales, tenemos a nuestra disposición el código RGB, donde RGB significan Rojo, Verde y Azul. Utilizando este código, con 256 posibilidades para cada color, el 0 representa la mínima intensidad del color y 255 la máxima. De esta forma se pueden mezclar entre ellos 256x256x256 (24 bits) de colores diferentes. ¿Os suena el concepto de True Color y los 16 millones de colores? Pues esa es la cantidad de colores posibles que se pueden manejar con el código RGB. Veámoslo con unos ejemplos.

Si queremos que el lienzo sea de un color en su máxima intensidad podemos establecer uno de los colores a 255 y los otros dos a 0:

```javascript
function draw() {
  background(255, 0, 0);
  // background(0, 255, 0);
  // background(0, 0, 255);
}
```

Lo curioso es que estableciendo la misma profundidad en los tres colores podemos simular la escala de grises:

```javascript
function draw() {
  background(0, 0, 0);
  // background(255, 255, 255);
}
```

Sobra decir que para conseguir el color que queramos tendremos que mezclar estos tres, ¿cómo conseguimos el código? Pues simplemente podemos mirar en internet, buscando [en el propio Google](https://www.google.com/search?q=colorpicker) la palabra **colorpicker** nos aparecerá una de esas tablas para encontrar el código de cualquier color.

### Rellenos y bordes

Pintar el lienzo está muy bien, ¿pero qué hay de las figuras? **p5** nos da la posibilidad de pintar no sólo el interior de nuestras figuras sino también sus bordes.

Para entender cómo funciona esta característica tenéis que sentiros como verdaderos artistas, porque decidme vosotros, ¿qué hace un artista antes de ponerse a pintar? Pues está claro, elegir el color y untar en él su pincel.

Nosotros tenemos que usar la misma lógica, justo antes de dibujar una figura vamos a establecer un color para pintarla, eso lo haremos con la instrucción **fill()** que significa rellenar, mirad:

```javascript
function draw() {
  background(220);
  fill(255, 0, 0);
  rect(100, 100, 200, 200);
}
```

De la misma forma funciona la función **stroke()**, permitiéndonos establecer el color del borde la figura que vamos a dibujar, siendo éste por defecto negro y con un tamaño de 1 píxel:

```javascript
function draw() {
  background(220);
  fill(255, 0, 0);
  stroke(0, 0, 255);
  rect(100, 100, 200, 200);
}
```

Si queremos establecer el tamaño del borde necesitaremos utilizar otra instrucción, **strokeWeight()**, a la que indicaremos el tamaño del borde en píxeles:

```javascript
function draw() {
  background(220);
  fill(255, 0, 0);
  strokeWeight(20);
  stroke(0, 0, 255);
  rect(100, 100, 200, 200);
}
```

Al establecer estas opciones para el relleno y los bordes todas las demás figuras que dibujemos también las utilizarán:

```javascript
function draw() {
  background(220);
  fill(255, 0, 0);
  strokeWeight(20);
  stroke(0, 0, 255);
  rect(100, 100, 200, 200);
  rect(200, 200, 100, 100);
}
```

Aquí necesitaremos sentirnos como verdaderos pintores, cambiando el color de relleno y de borde antes de dibujar cada figura:

```javascript
function draw() {
  background(220);

  fill(255, 0, 0);
  strokeWeight(20);
  stroke(0, 0, 255);
  rect(100, 100, 200, 200);

  fill(0, 255, 0);
  stroke(0);
  rect(200, 200, 100, 100);
}
```

Por último si en algún momento queremos desactivar el relleno o el borde podemos hacerlo con **noFill()** y **noStroke()** respectivamente, ambas funciones no requieren ningún valor y os las podéis imaginar como cuando el pintor limpia su pincel, por lo que si dibujamos algún contenido después de ejecutarlas no se verá nada en el lienzo:

```javascript
function draw() {
  background(220);

  fill(255, 0, 0);
  strokeWeight(20);
  stroke(0, 0, 255);
  rect(100, 100, 200, 200);

  noFill();
  noStroke();
  rect(200, 200, 100, 100);
}
```

## Variables internas

En esta lección vamos a introducir uno de los conceptos fundamentales de la programación: las variables. Pero antes de definir lo que es una variable, pensemos en lo que hemos estado haciendo y qué nos falta.

Hasta ahora hemos dibujado diferentes figuras en un lienzo utilizando las funciones de **p5**. Estas figuras son estáticas, aparecen en el lienzo tal como las definimos y no cambian a no ser que modifiquemos el código y lo volvamos a ejecutar. 

Sin embargo los programas no suelen funcionar de esa forma, normalmente en ellos realizamos un conjunto de acciones que empieza por abrir el programa y esperar a que carguen los componentes gráficos para interactuar con ellos. Luego ya nos ponemos a presionar botones y hacer clic en diferentes lugares para que el programa haga lo que necesitamos.

Todas estas acciones componen lo que se conoce como el flujo del programa y ese flujo no existiría si no fuera por algo vital: el tiempo. 

### El tiempo es dinámico

Así es, lo que no estamos teniendo en cuenta en nuestros ejemplos es que el tiempo fluye y esa es la clave para entender la necesidad de las variables y su capacidad para añadir dinamismo en los programas.

Volvamos a dibujar alguna forma en el lienzo para entender esta idea:

`05 - Variables sistema/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  fill(220, 0, 0);
  ellipse(200, 200, 100, 100);
}
```


Igual que hemos venido haciendo hasta ahora, al ejecutar el código tendremos nuestro lienzo con una figura, todo muy estático y lógico, pues hemos imaginado que somos pintores dibujando sobre un lienzo. Primero preparamos el lienzo y luego dibujamos en él las formas que queremos, incluso podemos ajustar préviamente colores para los rellenos y bordes de las figuras.

Sin embargo recordad que nos falta algo que no hemos tenido en cuenta: el tiempo.

¿Y si os dijera que este lienzo no se dibuja únicamente una vez? 

Vamos a hacer uso por un momento de aquella instrucción que muestra mensajes en la pantalla y vamos a utilizarla en la función **draw** (dibujar) donde tenemos las instrucciones que crean la figura:

```javascript
function setup() {
  print("Voy a crear el canvas")
  createCanvas(400, 400);
}

function draw() {
  print("Voy a dibujar en el canvas")
  background(220);
  fill(220, 0, 0);
  ellipse(200, 200, 100, 100);
}
```

Si ejecutamos este código, veremos como aparece una sola vez el texto "Voy a crear el canvas" pero innumerables veces "Voy a dibujar en el canvas".

Efectivamente, la función **draw()** y todo su contenido no es algo estático como la preparación del lienzo, sino que es dinámico y se ejecuta a lo largo del tiempo, concretamente unas 30 veces por segundo. Esta cantidad se conoce como fotogramas por segundo.

¿Pero si **draw()** es dinámica por qué percibimos su resultado como algo estático? Pues porque ese resultado nunca cambia, estamos dibujando las figuras en posiciones y colores constantes que no varían.

En otras palabras, si conseguimos alterar el contenido de **draw** para que su resultado cambie, entonces conseguiremos captar su dinamismo. ¿Cómo? Pues por ejemplo modificando las posiciones y colores de las figuras a lo largo del tiempo. ¿Y eso cómo se consigue? Pues ni más ni menos que utilizando valores variables, ahí tenemos nuestra respuesta.

### Variables mouseX y mouseY

La biblioteca **p5** cuenta con algunas variables internas que podemos utilizar para conseguir información, dos de las más interesantes son **mouseX** y **mouseY**. Estas variables contienen las coordenadas X e Y donde se encuentra el puntero del ratón sobre el lienzo respecto al punto de origen (0, 0). 

Si en lugar de mostrar por pantalla el texto "Voy a dibujar el canvas" mostramos esas variables veremos sus valores:

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  print(mouseX, mouseY)
  background(220);
  fill(220, 0, 0);
  ellipse(200, 200, 100, 100);
}
```

El hecho de que estos dos valores vayan cambiando su valor es la prueba de que son valores variables.

Si en lugar de dibujar nuestra redonda en el punto estático (200, 200) lo hiciéramos en las coordenadas del ratón, ¿qué creéis que ocurriría? Vamos a intentarlo:

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  fill(220, 0, 0);
  ellipse(mouseX, mouseY, 100, 100);
}
```

¡Pues ahí lo tenemos! Una redonda dinámica dibujándose bajo nuestro ratón, cuya posición es variable porque sus cooredenadas son **valores variables**.

### Dibujando el lienzo

Antes de acabar esta reveladora lección, quiero experimentar un poco más con vosotros.

Hasta ahora lo primero que hemos hecho al dibujar sobre el lienzo es empezar llenando el fondo de color gris usando la función **background**, pero ¿qué ocurriría si no lo rellenamos? Vamos a pintar una redonda muy pequeña sobre el lienzo pero pintando el fondo sola una vez durante su preparación:

```javascript
function setup() {
  createCanvas(400, 400);
  background(220);
}

function draw() {
  fill(0);
  ellipse(mouseX, mouseY, 15, 15);
}
```

Al hacer esto lo que hemos conseguido es que en cada fotograma se dibuja una pequeña redonda, pero como no pintamos de nuevo el fondo para vaciar su contenido, se conservan los dibujos de los anteriores fotogramas generando el efecto de que dibujamos con el ratón.

El problema es que muy rápidamente llenamos todo el lienzo y es imposible seguir dibujando, así que no voy a desaprovechar la oportunidad de explicaros lo que es un evento y cómo podemos utilizarlo para vaciar nuestro lienzo.

### Definiendo un evento

Ya sabemos que los programas informáticos se ejecutan indefinidamente en el tiempo y eso es lo que les añade dinamismo. Una de las formas de manejar el dinamismo es a través de variables que cambian su valor, pero hay otras formas y una de ellas son los eventos.

Imaginémonos un evento como una interacción que sudece mientras el programa está en marcha, por ejemplo cuando se presiona un botón.

Presionar un botón es un evento interactivo que realiza el usuario y es otra forma de añadir dinamismo. Como programadores podemos capturar esos eventos y ejecutar instrucciones para realizar diferentes tareas.

El ejemplo más sencillo para ilustrar esto es capturar el evento clic del ratón y dibujar el fondo del lienzo para simular que vaciamos su contenido, eso se haría así:

```javascript
function setup() {
  createCanvas(400, 400);
  background(220);
}

function draw() {
  fill(0);
  ellipse(mouseX, mouseY, 15, 15);
}

function mousePressed() {
  background(220);
}
```

Como siempre todas estas funcionalidades y variables internas las encontráréis perfectamente documentadas en la [referencia](https://p5js.org/es/reference/) de **p5**.

## Variables propias

En la lección anterior introducimos las variables, el concepto más importante de la programación, ya que gracias a ellas podemos almacenar valores que cambian a lo largo del tiempo y conseguir así crear programas dinámicos. 

Vimos cómo utilizar dos variables internas de **p5** que nos dicen las coordenadas del cursor: **mouseX** y **mouseY**, pero el verdadero potencial de las variables no se limita a usar las que ya están creadas sino a que podemos crear nuestras propias variables.

### Ciclo de vida de las variables

Una variable es un espacio en la memoria del dispositivo donde podemos almacenar información en forma de datos, como por ejemplo números y textos. Para facilitar el acceso a ese espacio le damos un nombre y ese es ni más ni menos que el nombre de la variable, cuyo proceso de creación se denomina **declaración**.

La forma más sencilla de declarar una variable en JavaScript es haciendo uso de la instrucción **var**. Veamos un ejemplo creando dos variables para substituir la posición donde dibujamos una figura en el lienzo. Podemos declararlas al principio de un **sketch**:

`06 - Variables propias/sketch.js`
```javascript
var circuloX;  // circulo_x
var circuloY;  // circulo_y

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(mouseX, mouseY, 50, 50)
}
```


Recordad que no podemos darle cualquier nombre a una variable, hay una serie de palabras reservadas que no podemos utilizar, si utilizáis alguna os dará un error de tipo **SyntaxError: Unexpected token** al ejecutar el código. Además no pueden contener espacios en los nombres, por eso suelen separarse las palabras con mayúsculas al principio de cada una menos la primera, esto se conoce como notación **camelCase**. Otra práctica común es separar las palabras con barras bajas haciendo uso de la notación **snake_case**.

Sea como sea ya tenemos nuestras variables declaradas pero todavía no tienen ningún valor, tenemos que asignarles algún dato para poder utilizarlas y este proceso se denomina **inicialización**.

Podríamos darle las posiciones del centro del lienzo:

```javascript
var circuloX = 200;
var circuloY = 200;
```

Ya tenemos las variables declaradas e inicializadas, sólo no falta **hacer uso** de ellas. ¿Os imagináis cómo? Pues está claro, substituyéndolas por los variables internas **mouseX** y **mouseY**: 

```javascript
function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circuloX, circuloY, 50, 50)
}
```

Ahora viene la parte divertida y es que por defecto nuestras variables tienen un valor que no cambia, pero nosotros podemos modificarlo de muchas formas. Por ejemplo, podemos sumar una cantidad a **circuloX** cada vez que detectemos un evento de clic haciendo referencia:

```javascript
function mousePressed() {
  circuloX = circuloX + 5;
}
```

¿Interesante verdad? ¿Y si este incremento lo hacemos dentro de la función **draw** que se ejecuta varias veces qué creéis que pasará?

```javascript
function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circuloX, circuloY, 50, 50)
  circuloX = circuloX + 5;
}
```

¡Pues hemos creado una animación que mueve la figura! Dependiendo de cómo ajustemos estos valores podemos crear diferentes efectos, por ejemplo una diagonal hacia abajo a la derecha partiendo desde la esquina superior izquierda:

```javascript
var circuloX = 0;
var circuloY = 0;

function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circuloX, circuloY, 50, 50)
  circuloX = circuloX + 1;
  circuloY= circuloY + 1;
}
```

Como véis las variables son la clave para añadir dinamismo a un programa y en nuestro caso sirven para generar el efecto de movimiento de la figura, sin duda un ejemplo muy ilustrativo de su importancia.

## Objetos

Ahora que sabemos cómo crear y utilizar variables vamos a introducir el concepto de objetos.

Volvamos al ejemplo donde dibujamos un círculo en el lienzo utilizando algunas variables para controlar su tamaño y posición:

`07 - Objetos/sketch.js`
```javascript
var circuloX = 100;
var circuloY = 100;
var circuloD = 50;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circuloX, circuloY, circuloD, circuloD)
}
```


Esta forma es correcta pero si os lo paráis a pensar da la sensación de que estas variables están desconectadas entre ellas. Sí, tenemos la palabra **circulo** delante de cada una pero no se entienden como que las tres formen parte de algo único como sería el círculo.

Los objetos son unas estructuras que nos permiten hacer eso, definir entidades que cuentan con sus propias variables internas, conocidas como propiedades.

En otras palabras, podríamos declarar una nueva variable llamada **circulo** que contenga las propiedades **x**, **y** y **d** de diámetro:

```javascript
// var circuloX = 100;
// var circuloY = 100;
// var circuloD = 50;

var circulo = {
  x, y, d
}
```

Como véis esta es la sintaxis para crear un objeto con esas tres propiedades, sin embargo nos falta inicializar su valopres y eso lo haremos con la notación en clave y valor, separando las propiedades de su valores con dos puntos:

```javascript

var circulo = {
  x: 100,
  y: 100,
  d: 50
}
```

¿Os imagináis como podemos hacer referencia a esas propiedades para utilizarlas en la función **draw**?

```javascript
function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circulo.x, circulo.y, circulo.d, circulo.d)
}
```

¿Verdad que en forma de propiedades las tres variables transmiten la sensación de trabajar en conjunto? 

Así pues para animar nuestro círculo podríamos hacerlo incrementando sus propiedades **x** e **y**:

```javascript
function draw() {
  background(220);
  fill(200, 0, 0)
  ellipse(circulo.x, circulo.y, circulo.d, circulo.d)
  circulo.x += 1  // circulo.x = circulo.x + 1
  circulo.y += 1  // circulo.y = circulo.y + 1
}
```

Sin duda los límites de lo que podemos crear están en nuestra imaginación y por eso os animo a hacer vuestros propios experimentos. Recordad que tenéis la referencia en español donde encontraréis más instrucciones y ejemplos.

## Valores mapeados

Con lo que sabemos ya podríamos pasar a la siguiente sección sin problemas, pero antes quiero compartir con vosotros un par de funciones interesantes que nos proporciona **p5**, seguro que se os ocurrirán unas cuantas formas de aplicarlas en vuestros experimentos.

Vamos a empezar por la función **map()** cuyo objetivo es ni más ni menos que mapear valores.

¿Qué significa mapear? Pues en nuestro caso se trata de automatizar reglas de tres, ahora lo veréis.

Vamos a partir del siguiente **sketch**:

`08 - Mapeo/sketch.js`
```javascript
var c = 255;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  fill(c, 0, 0)
  ellipse(200, 200, 50, 50)
}
```


Típico, un círculo rojo en el centro del lienzo.

Ya sabemos que un color tiene 256 intensidades siendo el 0 la mínima y el 255 la máxima.

Si dividimos 256/2 para conseguir la intensidad media nos daría 128 ¿verdad? Por tanto una intensidad del 50% es 128. En esta escala en tantos por ciento tenemos que 100% es el 255, 50% el 128 y 0% el 0. Siguiendo este patrón lo que hace la función de mapeado **map** es conseguir los resultados haciendo una regla de tres en función de dos conjuntos de valores mínimos y máximos.

Por ejemplo, si quisiéramos un 37% de intensidad podríamos hacer lo siguiente:

```javascript
var c = 255;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  c = map(37, 0, 100, 0, 255)
  fill(c, 0, 0)
  ellipse(200, 200, 50, 50)
}
```

¿Se entiende el concepto? Ahora la parte divertida es que podemos hacer esa cantidad proporcional a lo que queramos, por ejemplo la altura del lienzo y la posición del cursor en su eje Y:

```javascript
var c = 255;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  c = map(mouseY, 0, 400, 0, 255)
  fill(c, 0, 0)
  ellipse(200, 200, 50, 50)
}
```

¡Interesante! Vamos a añadir un par más de círculos con colores verde y azul a ver como queda:
```javascript
var c = 255;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  c = map(mouseY, 0, 400, 0, 255)
  fill(c, 0, 0)
  ellipse(100, 200, 50, 50)
  fill(0, c, 0)
  ellipse(200, 200, 50, 50)
  fill(0, 0, c)
  ellipse(300, 200, 50, 50)
}
```

## Valores aleatorios

Por último en esta lección vamos a introducir la función **random** o aleatoria en español, que permite como podéis suponer, generar valores aleatorios. 

Esta función toma un valor mínimo y otro máximo para generar un valor aleatorio entre ambos:

`09 - Aleatoria/sketch.js`
```javascript
var numero;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  numero = random(0, 100)
  print(numero)
}
```
 

Fijaros como nos aparece en la consola un número diferente todo el rato, como la tasa de fotogramas está establecida a 30 por segundo pues se muestran 30 números aleatorios. 

Ahora bien, existe una función de **p5** llamada **framerate()** con la que podemos establecer el número de veces por segundo que se dibuja el lienzo:

```javascript
var numero;

function setup() {
  createCanvas(400, 400)
  frameRate(1)
}

function draw() {
  background(220)
  numero = random(0, 100)
  print(numero)
}
```

Como véis esto afecta directamente a la cantidad de veces que generamos un número aleatorio, que ahora es una por segundo.

Pero vamos a hacer un ejemplo más interesante. ¿Recordáis que si no dibujamos el fondo en cada fotograma se conservan los dibujos que vamos haciendo?

## Expresiones lógicas

Durante la sección anterior aprendimos a dibujar figuras, utilizar variables y algunas funciones internas de **p5**, pero todo eso no es más que la punta del iceberg. Todavía nos falta aprender mucho más y a partir de ahora se os abrirá un nuevo mundo de posibilidades, eso es porque váis a aprender a controlar el flujo, o lo que es lo mismo, programar el código para que haga lo que vosotros queráis.

El control de flujo lo componen básicamente dos partes:

* Las **condiciones**, con las que podemos decidir si un código se ejecuta o no.
* Los **bucles**, que sirven para repetir un código mientras se cumple cierta condición.

Dejaremos los bucles para más adelante porque dependen en cierta forma de las condiciones, así que nos centraremos primeros en las condiciones, aunque para entenderlas antes debemos aprender qué son las expresiones lógicas.

Para condicionar el flujo de nuestro programa, éste deberá evaluar una expresión para decidir si se ejecuta un bloque de código o no, algo que conseguirá comparando dos valores, ya sean literales o variables, mediante un operador relacional:

* **Igual que**: ==
* **Distinto de**: !=
* **Mayor que**: >
* **Mayor o igual que**: >=
* **Menor que**: <
* **Menor o igual que**: <=

El resultado de esta comparación puede resultar únicamente en únicamente dos posibilidades lógicas, de ahí que se denominen expresiones lógicas:

* Si se cumple diremos que su resultado es **verdadero**, en inglés **true**.
* Si no se cumple diremos que su resultado es **falso**, en inglés **false**.

Ambos valores **true** y **false** forman lo que se conoce como tipos de datos lógicos o booleanos, unos datos diferentes de los números y los textos.

Pero basta de hablar y vamos a practicar algunas condiciones y sus resultados:

`10 - Expresiones logicas/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
  
  // Condiciones básicas
  var a = 10;
  var b = 15;
  var c = 20;
  
  var r = a == b;
  print(r)
  
  print(a == b)
  print(a != b)
  print(a > b)
  print(a < b)
  print(b >= c)
  print(b <= c)
  
  // Precedencia de operadores
  print(c < a*3)
  print(a+c == b*2)
  print(a+b+c > 50)
  print(a*b-a*c < 0)
  
  // Con lógicos
  var n = true;
  var m = false;
  
  print(n == true)
  print(n != true)
  print(n == m)
  print(n > m)
  
  // Con textos
  var s = "hola";
  var t = "adios";
  
  print(s == "hola")
  print(s == t)
}

function draw() {
  background(220);
}
```


## Condición if-else

Ahora que sabemos cómo se evalúan las expresiones lógicas ya podemos crear nuestras propias condiciones, para ello se utiliza esta sintaxis:

```javascript
if (true) {
  // Bloque que se ejecutará
}
```

### Si (if)

En español **if** significa **si** y podemos leerlo como "si se cumple la condición ejecutar el bloque de código". Además donde tenemos **true** podemos poner cualquier expresión lógica cuyo resultado sea verdadero. Vamos a hacer un ejemplo:

`11 - Condicion si/sketch.js`
```javascript
var dibujar = true;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  if (dibujar == true) {
    fill(220, 0, 0)
    ellipse(200, 200, 50, 50)
  }
}
```


Como véis podemos controlar si dibujamos o no el círculo con la variable **dibujar** y algo muy interesante que podríamos hacer es activar o desactivar la condición definiendo un evento de clic:

```javascript
function mousePressed(){
  dibujar = !dibujar;
}
```

El operador lógico **!** sirve para negar una expresión lógica, devolviendo verdadero si ésta es falsa o falso si es verdadera.

### Si no (else)

Lo que hemos hecho también se puede programar con una contracondición **else**, que se añade siempre después de un **if** para comprobar el caso contrario. En conjunto se leería "si se cumple la condición ejecutar el bloque de código, si no se cumple ejecutar el otro bloque de código":

```javascript
function mousePressed(){
  if (dibujar) {
  	dibujar = false
  } else {
  	dibujar = true
  }
}
```

Un experimento genial que podemos hacer es programar un círculo que se mueva en diagonal por el lienzo, pero si se sale del margen entonces cambiará revertirá su dirección.

Partiremos de un ejemplo básico donde el círculo se mueve en diagonal hasta el infinito:

```javascript
var circulo = { x: 0, y: 0 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  // Pintamos el círculo
  fill(220, 0, 0)
  ellipse(circulo.x, circulo.y, 50, 50)
  // Movemos el círculo
  circulo.x += 2
  circulo.y += 2
}
```

Ahora lo que vamos a hacer es una condición justo al final del **draw** para comprobar si la posición que tenemos después de modificarla se ha salido del lienzo. Eso sería tan fácil de comprobar si la posición **x** del círculo es mayor que el ancho del lienzo o si la posición **y** es mayor que la altura del lienzo:

```javascript
// Comprobamos si nos salimos del lienzo
if (circulo.x > width) {
  print("El círculo se ha salido del lienzo")
}
```

Con esto ya tenemos nuestra condición lista y lo que tocaría es modificar el código para que el círculo cambie la dirección. ¿Cómo podemos hacerlo?

Una solución este problema muy utilizada utiliza en los videojuegos es definir una nueva variable para representar si la dirección es positiva o negativa. Supodnremos que si es **1** será positiva y si es **-1** será negativa:

```javascript
var circulo = { x: 0, y: 0, d: 1 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  // Pintamos el círculo
  fill(220, 0, 0)
  ellipse(circulo.x, circulo.y, 50, 50)
  // Movemos el círculo en base a la dirección
  circulo.x += 2 * circulo.d
  circulo.y += 2 * circulo.d
  // Comprobamos si nos salimos del lienzo
  if (circulo.x > width) {
    print("El círculo se ha salido del lienzo")
  }
}
```

Ahora si multiplicamos esa dirección por la cantidad que se mueve el círculo conseguiremos sumar o restar dependiendo del caso y sólo tendremos que cambiar la dirección si nos salimos del lienzo haciendo algo tan fácil como multiplicar por -1, ya que si tenemos -1 pasará a ser 1 y si tenemos 1 pasará a ser -1:

```javascript
var circulo = { x: 0, y: 0, d: 1 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  // Pintamos el círculo
  fill(220, 0, 0)
  ellipse(circulo.x, circulo.y, 50, 50)
  // Movemos el círculo en base a la dirección
  circulo.x += 2 * circulo.d
  circulo.y += 2 * circulo.d
  // Comprobamos si nos salimos del lienzo
  if (circulo.x > width) {
    circulo.d *= -1
  }
}
```

Con esto habremos logrado que el círculo rebote en la esquina de abajo.

## Condiciones múltiples

Hemos visto que podemos utilizar **if** y **else** para comprobar una condición y ejecutar un código u otro en caso de que se cumpla o no, sin embargo en algunas ocasiones vamos a necesitar lidiar con más de una condición, e ahí lo que se conoce como condiciones múltiples.

Volvamos al ejemplo de la lección anterior donde nuestro círculo se movía por la diagonal rebotando de un lado al otro:

`12 - Condicion extendida/sketch.js`
```javascript
var circulo = { x: 0, y: 0, d: 1 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  // Pintamos el círculo
  fill(220, 0, 0)
  ellipse(circulo.x, circulo.y, 50, 50)
  // Movemos el círculo
  circulo.x += 2 * circulo.d
  circulo.y += 2 * circulo.d
  // Comprobamos si nos salimos del lienzo
  if (circulo.x > width) { circulo.d *= -1 }
  if (circulo.x < 0) { circulo.d *= -1 }
}
```


Ahora vamos a trazar tres líneas horizontales cortando el lienzo, una a 100 píxeles de altura, otra a 200 y otra 300. Lo haremos justo después de pintar el fondo:

```javascript
function draw() {
  background(220)
  // Pintamos el círculo
  fill(220, 0, 0)
  // Dibujamos tres líneas horizontales
  line(0, 100, width, 100)
  line(0, 200, width, 200)
  line(0, 300, width, 300)
  // ...
}
```

Estas tres líneas las vamos a usar como una guía porque nuestro siguiente objetivo será pintar la figura de un color diferente dependiendo de en qué parte se encuentre:

* Si se encuentra en la primera parte, de 0 a 100 píxeles de altura, la figura será amarilla.
* Si se encuentra en la segunda parte, de 100 a 200 píxeles de altura, la figura será roja.
* Si se encuentra en la tercera parte, de 200 a 300 píxeles de altura, la figura será verde.
* Si se encuentra en la segunda parte, de 300 a 400 píxeles de altura, la figura será azul.

Como podéis suponer cuatro posibilidades implican cuatro condiciones. Podríamos intentar hacerlo con lo que sabemos hasta ahora sobreescribiendo unas propiedades del círculo **r**, **g**, **b** y ajustando los colores en cada caso:

```javascript
var circulo = { 
  x: 0, y: 0, d: 1, 
  r: 0, g: 0, b: 0 
}

// ...

function draw() {
  // ...
  
  // Dibujamos tres líneas horizontales
  line(0, 100, width, 100)
  line(0, 200, width, 200)
  line(0, 300, width, 300)
  // Pintamos el círculo
  if (circulo.y > 0) { 
    circulo.r = 220
    circulo.g = 220
    circulo.b = 0
  } 
  if (circulo.y > 100) { 
    circulo.r = 220
    circulo.g = 0
    circulo.b = 0
  } 
  if (circulo.y > 200) { 
    circulo.r = 0
    circulo.g = 220
    circulo.b = 0
  } 
  if (circulo.y > 300) { 
    circulo.r = 0
    circulo.g = 0
    circulo.b = 220
  } 
  fill(circulo.r, circulo.g, circulo.b) 
  // ...
}
```

Es una forma de hacerlo, pero no es óptima, eso es porque estas condiciones no están relacionadas entre ellas. Es decir, se están ejecutando siempre todas sobreescribiendose unas a otras. Pensadlo por un momento, si el círculo se encuentra en un lugar cuya posición **y** es mayor que 300, eso significa que también es mayor que 0, mayor que 100 y mayor que 200. Si añadimos un print en las condiciones lo veremos:

```javascript
if (circulo.y > 0) { 
  circulo.r = 220
  circulo.g = 220
  circulo.b = 0
  print("Primera parte")
} 
if (circulo.y > 100) { 
  circulo.r = 220
  circulo.g = 0
  circulo.b = 0
  print("Segunda parte")
} 
if (circulo.y > 200) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Tercera parte")
} 
if (circulo.y > 300) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Cuarta parte")
} 
```

Esto es un problema porque estamos ejecutando muchísimo código innecesariamente, pero no temáis porque lo podemos arreglar. Existe una instrucción condicional que sirve para vincular varias condiciones entre ellas y optimizar mucho el código, se trata del **else if**, en español **si no si**.

El bloque **else if** se puede utilizar múltiples veces entre un bloque **if** y un bloque **else**, aunque éste último no es obligatorio:

```javascript
if (circulo.y > 0) { 
  circulo.r = 220
  circulo.g = 220
  circulo.b = 0
  print("Primera parte")
} else if (circulo.y > 100) { 
  circulo.r = 220
  circulo.g = 0
  circulo.b = 0
  print("Segunda parte")
}  else if (circulo.y > 200) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Tercera parte")
} else if (circulo.y > 300) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Cuarta parte")
} 
```

Al cambiar el código veremos que no funciona correctamente y eso tiene una explicación. Se debe a que cuando se ejecuta una de las condiciones los demás **else if** se descartan. De ahí que para utilizar esta estructura haya que desarrollar las condiciones de menos excluyente a más excluyente, justo al contrario de como lo tenemos.

Pensadlo detenidamente, la condición **circulo.y > 0** excluye todas las demás, por tanto la primera que deberíamos comprobar es **circulo.y > 300** porque esa no excluye las demás, ¿verdad? Luego la de **circulo.y > 200**, la de **circulo.y > 100** y finalmente **circulo.y > 0**:

```javascript
if (circulo.y > 300) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Cuarta parte")
}  else if (circulo.y > 200) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Tercera parte")
} else if (circulo.y > 100) { 
  circulo.r = 220
  circulo.g = 0
  circulo.b = 0
  print("Segunda parte")
} else if (circulo.y > 0) { 
  circulo.r = 220
  circulo.g = 220
  circulo.b = 0
  print("Primera parte")
}
```

## Relaciones múltiples

A parte de crear condiciones múltiples con la estructura **if**, **else if** y **else** también tenemos la posibilidad de definir más de una relación en la misma expresión lógica.

Siguiendo con el ejemplo de antes, en él tenemos un lienzo dividido en cuatro partes y en cada una establecemos un color diferente. Pero supongamos por un momento que en lugar de cuatro colores queremos manejar dos, el verde para la primera y tercera parte y el azul para la segunda y la cuarta.

Podríamos cambiar el código para conseguir este funcionamiento sin mucha complicación:

```javascript
if (circulo.y > 300) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Cuarta parte")
}  else if (circulo.y > 200) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Tercera parte")
} else if (circulo.y > 100) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Segunda parte")
} else if (circulo.y > 0) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Primera parte")
}
```

Es una forma correcta de solucionarlo pero una vez más no es la óptima.

Veréis, hay una regla no escrita en programación que dice que si estás repitiendo código es que lo estás haciendo mal y así es, tenemos los mismos códigos repetidos. ¿Ya que tenemos sólo dos colores no sería más lógico implementar dos condiciones? Pues eso se puede lograr usando múltiples relaciones.

Para unir dos relaciones contamos con dos operadores lógicos conocidos como **and** y **or**. Dependiendo de lo que necesitamos hacer utilizaremos uno u otro:

* **and**: Conocido como **Y** lógica ejecutará un bloque cuando se cumplan las dos relaciones.
* **or**: Conocido como **O** lógica ejecutará un bloque si por lo menos se cumple una de las dos relaciones.

Sabiendo esto os planteo la siguiente cuestión. ¿Cómo podemos asegurarnos en una única condición de que la figura se encuentra en la primera parte del lienzo? No podemos simplemente decir que su posición **y** es mayor que 0 porque esa condición también sirve para las otras tres partes. 

Lo que limita la primera parte es el valor máximo de **y**, que en este caso es 100, por tanto la condición que garantiza que el círculo se encuentra en la primera parte es la unión de ambas a la vez, cuando **y > 0** y también **y <= 100**.

Aplicando esta lógica para cada parte tendremos las siguientes condiciones:

* Parte 1: **y > 0** a la vez que **y <= 100**.
* Parte 2: **y > 100** a la vez que **y <= 200**.
* Parte 3: **y > 200** a la vez que **y <= 300**.
* Parte 4: **y > 300** a la vez que **y <= 400**.

Utilizar estas relaciones múltiples sería una alternativa a los **else if**, ya que cada opción excluye a las otras. Sabiendo que el operador lógico para el **and** es **&&** podríamos hacer lo siguiente para unificar estas relaciones:

```javascript
if (circulo.y > 300 && circulo.y <= 400) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Cuarta parte")
}

if (circulo.y > 200 && circulo.y <= 300) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Tercera parte")
} 

if (circulo.y > 100 && circulo.y <= 200) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Segunda parte")
} 

if (circulo.y > 0 && circulo.y <= 100) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Primera parte")
}
```

Son condiciones tan exclusivas que no importa el orden como las definamos.

¿Pero en qué afecta esto a lo que os decía al principio? Pues es la clave de todo porque si sabemos que cada uno de estos conjuntos de relaciones implica una de las partes, si pudiéramos unir los conjuntos de la primera parte y la tercera y de la segunda con la cuarta, ¡ya podríamos ahorrarnos repetir código! Y ahí es cuando entra en acción el operador **or** que se escribe con **||**:

```javascript
if ( (circulo.y > 200 && circulo.y <= 300) || (circulo.y > 0 && circulo.y <= 100)) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
  print("Primera parte o tercera")
} 
  
if ((circulo.y > 300 && circulo.y <= 400) || (circulo.y > 100 && circulo.y <= 200)) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
  print("Segunda parte o cuarta")
}
```

Entiendo que tanto código pueda ser abrumador, tranquilos, vamos a simplificarlo para que se entienda mucho mejor, mirad:

```javascript
var primera = circulo.y > 200 && circulo.y <= 300;
var segunda = circulo.y > 100 && circulo.y <= 200
var tercera = circulo.y > 0 && circulo.y <= 100;
var cuarta  = circulo.y > 300 && circulo.y <= 400;

if (primera || tercera) { 
  circulo.r = 0
  circulo.g = 220
  circulo.b = 0
} 
  
if (segunda || cuarta) { 
  circulo.r = 0
  circulo.g = 0
  circulo.b = 220
}
```

¿Muchísimo mejor verdad?

Con esto ya sabéis qué es condicionar el código, cómo utilizar relaciones múltiples y estáis más que preparados para aprender a utilizar los bucles.

## Bucles while y for

Dentro del control de flujo encontramos unas estructuras muy interesantes llamadas iteraciones o bucles. 

Como podéis suponer los bucles son unas estructuras que sirven para repetir la ejecución de un bloque de código. 

Para entender este comportamiento vamos a desarrollarlo visualmente, partiendo de un ejercicio donde vamos a dividir en líneas verticales un lienzo cada 40 píxeles de ancho. Suponiendo que el lienzo tiene 400 píxeles de ancho al final tendríamos 10 porciones de 40 píxeles cada una. Podríamos hacerlo incrementando una variable para dibujar cada línea:

`13 - Mientras/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  
  var x = 0
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
  x += 40
  line(x, 0, x, 400)
  
}
```


En seguida se ve que en este ejemplo hay mucho código repetido, siendo un escenario para automatizar el código repetido en un bucle.

¿Para qué vamos a escribir 9 veces el mismo código si podemos decirle a nuestra máquina que repita ese código 9 veces? Os enseñaré a hacerlo de dos formas distintas.

### Bucle while (for)

La primera estructura de control iterativo es el **while**, conocido en español como **mientras** y sirve para ejecutar un código mientras se cumple una condición.

Para ejecutar correctamente un bucle **mientras** lo primero es identificar la condición que nos permite repetir el código y lo segundo aseurarnos de que esa condición se dejará de cumplir eventualmente. Este segundo punto es vital porque si se repita para siempre estaremos ante un bucle infinito y el proceso acabará colapsando.

En nuestro caso el ejemplo es muy sencillo pues sabemos exactamente cuando tenemos que dejar de dibujar líneas. Ese momento es cuando la **x** sea mayor que el ancho del lienzo:

Vamos a por ello:

`13 - Mientras/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  
  var x = 0
  while (x < width) {
    x += 40
    line(x, 0, x, 400)
  }
  
}
```


Nuestro bucle **while** se leería como "Mientras X sea menor que el ancho del lienzo incrementamos la X en 40 píxeles y trazamos una línea vertical". Cuando la X sea mayor de 400 la condición no se cumplirá y el bucle dejará de ejecutarse (todo sucede en un único fotograma).

### Bucle for (para)

La segunda forma de solucionar el problema es mediante el bucle **for**, conocido como **para** en español y funciona igual que el **while** pero cambiando su sintaxis. 

Este bucle nos permite crear una variable, condicionarla y manipularla en cada iteración, fijaros como quedaría el **while** transformado en **for**: 

```javascript
function draw() {
  background(220)
  
  for (var x = 0; x < width; x += 40) {
    line(x, 0, x, 400)
  }
  
}
```

### While vs for

Si bien es cierto que ambas estructuras hacen lo mismo, normalmente el bucle **while** se utiliza cuando no se conoce el número de veces que necesitamos repetir el bucle y el **for** cuando sí sabemos el número de veces que lo queremos repetir.

Esto es así porque la sintaxis que ofrece el **for** simplifica esta necesidad, de ahí que la variable que maneja suela denominarse contador. 

Hagamos un último ejemplo muy divertido para ilustrar esto, partiendo de un círculo de 20x20 en medio del lienzo pero sin rellenar su fondo, únicamente con el borde:

```javascript
function draw() {
  background(220)
  noFill()

  ellipse(200, 200, 20, 20)
}
```

A partir de esta base nuestro objetivo es dibujar múltiples círculos, cada uno a una distancia del centro que se vaya incrementando 20 píxeles. Es decir, si el primero tiene un diámetro de 20, el segundo lo tendrá de 40, el tercero de 60 y así... Esto lo repetiremos un número determinado de veces, por ejemplo 15.

Como sabemos de antemano cuántas veces queremos repetir el dibujo utilizaremos el **for** y su variable como contador para limitarlo, incrementándolo una vez en cada iteración. Fijaros:

```javascript
function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  noFill()
  
  for (var x = 0; x < 15; x += 1) {
    ellipse(200, 200, 20, 20)  
  }
  
}
```

Con esto ya dibujamos 15 veces un círculo pero nos falta incrementar el diámero 20 píxeles en cada iteración. Para hacerlo podemos utilizar otra variable:

```javascript
function draw() {
  background(220)
  noFill()
  
  var diametro = 20;
  
  for (var x = 0; x < 15; x += 1) {
    ellipse(200, 200, diametro, diametro)  
    diametro += 20
  }
  
}
```

¿Así queda más claro por qué la variable del **for** suele utilizarse como contador verdad? 

Con esto la lección se puede dar por concluida pero se me ha ocurrido algo genial y muy divertido.

## Hora de divertirse

Siguiendo con el ejemplo anterior, imaginad por un momento que en lugar de dibujar 15 círculos empezamos dibujando 0, al cabo de unos instantes dibujamos 1, luego 2 y así hasta llegar a 30. Al llegar a 30 en lugar de sumar 1 restaríamos 1 hasta llegar de nuevo a 0 e invertir el proceso. ¿Os podéis imaginar lo que intento decir? ¡Vamos a hacerlo!

Empezaremos estableciendo una variable para limitar el número de círculos y la utilizaremos en el **for**:

```javascript
var limite = 0;

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(220)
  noFill()
  
  var diametro = 20;
  
  for (var x = 0; x < limite; x += 1) {
    ellipse(200, 200, diametro, diametro)  
    diametro += 20
  }
  
}
```

Ahora vamos a incrementar en cada fotograma ese límite hasta un máximo de 30 y veamos qué ocurre:

```javascript
// ...

if (limite < 30) {
  limite += 1
}
```

¡Nada mal! Como el lienzo se dibuja 30 veces por segundo pues se dibujan los 30 círculos en ese tiempo.

Si modificamos el frameRate para que sea 15 fotogramas por segundo debería tardar unos 2 segundos en rellenar el lienzo (30/15 = 2):

```javascript
function setup() {
  createCanvas(400, 400)
  frameRate(15)
}
```

Ahora viene lo mejor, si utilizamos otra variable para manejar la cantidad que sumamos al límite podemos hacer que valga 1 o -1 dependiendo de si estamos sumando para llegar a 30 o restando para llegar a 0. Eso junto a unas condiciones debería permitirnos generar un efecto infinito que sume y reste círculos:

```javascript
var cantidad = 1;  // sumamos 

// ...

if (limite > 30) {
  cantidad = -1
} else if (limite < 0) {
  cantidad = 1
}

limite += cantidad
```

## Tablero de ajedrez

Llegamos al final de la sección donde hemos aprendido como el control de flujo nos permite condicionar y repetir bloques de código. 

En esta lección vamos a repasar todos los conceptos haciendo un interesante ejercicio mientras introducimos el uso de los bucles anidados, una situación que sucede cuando dentro de un bucle tenemos otro bucle.

Para demostrar visualmente lo que ocurre he decidido enseñaros cómo dibujar un tablero de ajedrez, será un poco largo pero estoy seguro de que os gustará.

¿Conocéis la estructura de un tablero de ajedrez? Se trata de una superficie cuadrada dividida en 8x8 cuadrados, 32 blancos y 32 negros. Empezando por el cuadrado de la esquina superior ubicamos la primera fila en la que el primer cuadrado es blanco, el segundo negro, el tercero blanco otra vez y así. Para la segunda fila se alternan los colores, de manera que nunca queden dos cuadrados del mismo color unidos por un lado.

<div class="image">
   <img src="https://raw.githubusercontent.com/hcosta/apuntes-cdn/master/docs/p5js/ajedrez.jpg"/>
   <div style="font-size:80%">Tablero de madera con casillas blancas en amarillo y negras en marrón.</div>
</div>

Ya sabemos dibujar cuadrados y rellenarlos de colores, así que podríamos dibujar los 64 cuadrados manualmente en el lienzo... pero seamos realistas, ¿quién haría eso sabiendo que podemos usar bucles?

Para afrontar este problema vamos a empezar por lo más básico, dividir el lienzo equitativamente en 64 cuadrados. Esto lo podemos hacer trazando líneas rectas, dividiendo el ancho y alto del lienzo entre 8 para saber el tamaño de los cuadrados y en un bucle trazar las líneas horizontales y verticales:

`14 - Bucles anidados/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Divisiones horizontales
  for (var i=1; i<=8; i++){
    var x = ancho_celda * i
    line(0, x, height, x)
  }

  // Divisiones verticales
  for (var j=1; j<=8; j++){
    var y = alto_celda * j
    line(y, 0, y, width)
  }
}
```


Muy bien, con esto hemos conseguido dibujar el tablero y sólo nos falta pintar las celdas acordemente.

Por desgracia lo que hemos hecho no nos sirve para nada y es que esto sólo dibuja el tablero y lo que nosotros necesitamos son cuadrados pintarlos de colores... así que tendremos que pensar otra forma de hacerlo utilizando cuadrados.

Lo que os propongo es dividir el problema en partes más sencillas que podamos afrontar gradualmente hasta dar con la solución completa. Ya sabéis lo que dicen de divide y vence.

### Dibujando una celda

Empecemos de nuevo por lo más esencial, dibujar el primer cuadrado de la esquina superior. Éste no nos debería costar demasiado pues ya sabemos lo que tenemos que hacer:

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Dibujamos un cuadrado
  rect(0, 0, ancho_celda, alto_celda)
}
```

Muy bien, ya hemos dado el primer paso.

### Dibujando una fila

Ahora que tenemos un cuadrado nuestro siguiente objetivo será dibujar toda la fila, por ahora sin preocuparnos de los colores. 

Para conseguirlo podemos dibujar los 8 cuadrados uno al lado del otro en un bucle **for**:

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Dibujamos una fila
  for (var i=0; i<8; i++) {
    // Dibujamos un cuadrado
    rect(i*ancho_celda, 0, ancho_celda, alto_celda)
  }
}
```

¡Vamos progresando! 

### Dibujando el tablero

Tenemos una fila, salta a la vista qué debemos hacer, ¿verdad? Dibujar 8 filas una debajo de otra.

Aquí es mis estimados alumnos donde entra en juego el segundo bucle, un bucle dentro de otro, pues si tenemos un bucle para dibujar una fila, debemos utilizarlo dentro de otro para que se repita nuevamente.

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Recorremos 8 filas
  for (var j=0; j<8; j++) {
    // Dibujamos una fila
    for (var i=0; i<8; i++) {
       // Dibujamos un cuadrado
       rect(i*ancho_celda, 0, ancho_celda, alto_celda)
    }
  }
}
```

Con esto tenemos la fila dibujándose 8 veces en el mismo sitio, tenemos que ajustar la altura para dibujar las celdas dependiendo de la fila:

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Recorremos 8 filas
  for (var j=0; j<8; j++) {
    // Dibujamos una fila
    for (var i=0; i<8; i++) {
       // Dibujamos un cuadrado
       rect(i*ancho_celda, j*alto_celda, ancho_celda, alto_celda)
    }
  }
} 
```

¡Por fin! Ahora sí tenemos lo necesario para poder pintar el tablero, pues estamos dibujando cuadrados que podemos rellenar de colores. 

La cuestión es determinar de qué color pintar los cuadrados... ¿Se os ocurre alguna forma?

### Pintando una fila

Como no sabemos exactamente por dónde empezar hagamos lo mismo que antes, pintemos el diseño de la primera fila con el primer cuadrado en blanco, el segundo en negro y así sucesivamente.

Una forma de pintar los cuadrados sería comprobando el contador del **for** anidado. Podemos hacer diferentes **if** y si la **i** vale 0 pintarlo blanco, si vale **1** pintarlo negro, si vale **2** blanco, etc.

Sin embargo como podéis suponer esta forma no es óptima y lo malo es que no sabemos como determinar automáticamente este caso. ¿Cómo podemos hacerlo entonces? Bueno, la clave está en un operador aritmético que todavía no conocemos y váis a aprender ahora mismo, el módulo.

¿Sabéis lo que es una división entera? Cuando por ejemplo dividimos 5 entre 2, el resultado es 2 y nos sobra 1. Ese 1 se llama resto o residuo de la división entera. Pues bien, el operador de módulo **%** es un operador como la suma o la división, pero lo que hace es devolvernos el residuo de una división.

¿Por qué es tan importante? Porque si calculamos el módulo de un número entre otro y el resultado es diferente de cero podemos determinar si ese número es múltiplo del primero o no. En otras palabras, podemos saber si una casilla es par o impar y eso amigos es todo lo que necesitamos para pintar las celdas:

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Recorremos 8 filas
  for (var j=0; j<8; j++) {
    // Dibujamos una fila
    for (var i=0; i<8; i++) {
      // Determinamos si el módulo del contador de la fila es par
      if (i%2 == 0) {
        // Si el residuo es 0 es par, pintamos blanco
        fill(255)
      } else {
        // Si el residuo es diferente de 0 es impar, pintamos negro 
        fill(0)
      }
      // Dibujamos un cuadrado
      rect(i*ancho_celda, j*alto_celda, ancho_celda, alto_celda)
    }
  }
}
```

Bien, hemos pintado la estructura de las líneas impares perfectamente.

### Pintando el tablero

Ahora nos falta identificar las líneas pares y ya lo tendremos. ¿Cómo podemos hacerlo? Pues de la misma forma que hemos determinado si las celdas eran pares podemos comprobar las filas, haciendo uso de condiciones anidadas:

```javascript
function draw() {
  background(220);
  
  var ancho_celda = width/8;
  var alto_celda = height/8;
  
  // Recorremos 8 filas
  for (var j=0; j<8; j++) {

    // Determinamos los colores de la fila
    var color_celda_par;
    var color_celda_impar;
    if (j%2 == 0) {
      // Si la fila es par 
      color_celda_par = 255;
      color_celda_impar = 0;
    } else {
      // Si la fila es impar 
      color_celda_par = 0;
      color_celda_impar = 255;
    }

    // Dibujamos una fila
    for (var i=0; i<8; i++) {
      // Determinamos si el módulo del contador de la fila es par
      if (i%2 == 0) {
        // Si el residuo es 0 es par
        fill(color_celda_par)
      } else {
        // Si el residuo es diferente de 0 es impar
        fill(color_celda_impar)
      }
      // Dibujamos un cuadrado
      rect(i*ancho_celda, j*alto_celda, ancho_celda, alto_celda)
    }

  }

}
```

Sin palabras, perfectamente geométrico, perfectamente equilibrado. Dibujado programáticamente usando variables, condiciones y bucles.

En esto amigos consiste el arte de dibujar gráficos, en ingeniárselas para dibujar lo que queramos sobre el lienzo y lo mejor es que no hay una sola forma de hacer las cosas. Por eso es una tarea tan creativa a la par que lógica.

Por cierto, si queréis almacenar colores RGB en una variable se puede hacer usando la función **color** de **p5**, que por cierto acepta tanto valores en formato RGB como en hexadecimal:

```javascript
if (j%2 == 0) {
  // Si la fila es par 
  color_celda_par = color('#DAB692');
  color_celda_impar = color(133, 44, 25);
} else {
  color_celda_par = color(133, 44, 25);
  color_celda_impar = color('#DAB692');
}
```

## Funciones

Empezamos una nueva sección en la que vamos a aprender sobre las funciones y hay que decir que ya hemos utilizado muchas funciones de la biblioteca **p5**, como **setup**, **draw** y todas las que sirven para dibujar formas y colores.

En la programación las funciones son uno de los conceptos más importantes porque permiten escribir código modular y reutilizable:

* **Modular** porque nos ofrece la posibilidad de organizar nuestro código de una forma coherente.
* **Reutilizable** porque podemos ejecutar una función tantas veces como queramos.

Si buscamos una definición concreta, las funciones son bloques de código reutilizable identificados con un nombre cuyo objetivo es solucionar un problema. Recordad, las buenas funciones deben dar solución a sólo un problema, si solucionan más de un problema significa que podríamos haberlo dividido en más funciones, lo que nos permitiría organizar mejor el código, hacerlo más extensible y fácil de utilizar.

Podmos aprender sobre la sintaxis de una función observando **setup**:

```javascript
function setup() {

}
```

Como se puede apreciar hacemos uso de la palabra reservada **function** para definir el nombre de una función, seguido de los paréntesis y las llaves que envuelven su bloque de código.

Vamos a recuperar el ejemplo del círculo que rebota diagonalmente y lo vamos a utilizar para practiar como crear y llamar nuestras propias funciones:

`15 - Funciones/sketch.js`
```javascript
var circulo = { x: 0, y: 0, d: 1 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
}
```


Para reorganizar el código utilizando funciones una forma de hacerlo es identificar los verbos, ya que éstos indican acciones:

* Pintar
* Mover
* Rebotar

Cada una de estas acciones podría trasladarse a una función para organizar mejor el código:

```javascript
function pintar() {
  // Pintamos el círculo
  fill(220, 0, 0)
  ellipse(circulo.x, circulo.y, 50, 50)
}

function mover() {
  // Movemos el círculo
  circulo.x += 2 * circulo.d
  circulo.y += 2 * circulo.d
}

function rebotar() {
  // Comprobamos si nos salimos del lienzo
  if (circulo.x > width) {
    circulo.d *= -1
  } else if (circulo.x < 0) {
    circulo.d *= -1
  }
}
```

Finalmente tendríamos que ejecutar nuestras funciones en lugar del código:

```javascript
var circulo = { x: 0, y: 0, d: 1 }

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  mover()
  rebotar()
  pintar()
}
```

Estamos haciendo lo mismo pero ahora tenemos el código organizado modularmente. Podríamos desactivar una característica como la de hacer que el círculo rebote comentando la línea que ejecuta esa funcionalidad:

```javascript
function draw() {
  background(220)
  mover()
  //rebotar()
  pintar()
}
```

### Parámetros y argumentos

¿Recordáis que para dibujar una figura necesitábamos enviar a la función la posición donde queremos dibujarla y su tamaño? Esos datos son conocidos como parámetros de la función y es lo que nos permite añadir dinamismo a su funcionamiento, logrando diferentes resultados dependiendo de los datos que les enviemos.

Vamos a aprender sobre los parámetros creando nuestra propia función para dibujar casitas. Cada casita estará formada por dos figuras:

* Un cuadrado gris para la pared principal
* Un triángulo rojo para el tejado

`16 - Parametros/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  casita()
}

function casita() {
  
  var x = 100;
  var y = 100;
  var lado = 50;
  
  // Pintamos la pared
  fill(100)
  rect(x, y, lado, lado)
  
  // Pintamos el techo
  fill(220, 0, 0)
  triangle(x, y, x+lado, y, x+lado/2, y-lado/2)
  
}
```


Muy bien, con esto podemos dibujar una casita. Lo malo es que todavía no podemos reutilizar la función porque sus variables tienen valores estáticos que no cambian.

La idea como podéis suponer es añadir las variables **x**, **y** y **lado** como parámtros para poder establecerlos en el momento de dibujar la casita, así que vamos a hacerlo:

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  casita()
}

function casita(x, y, lado) {
  
  // Pintamos la pared
  fill(100)
  rect(x, y, lado, lado)
  
  // Pintamos el techo
  fill(220, 0, 0)
  triangle(x, y, x+lado, y, x+lado/2, y-lado/2)
  
}
```

Lo interesante es que al crear los parámetros estos recibirán los valores por orden en el momento de enviarlos a la función y además no tenemos que usar la palabra **var** para definirlos:

```javascript
casita(100, 100, 50)
```

Con esto ya le diremos que **x** e **y** valen 100 y el **lado** tiene un tamaño de 50, pero lo mejor de todo es que cambiando los valores podemos dibujar diferentes casitas:

```javascript
function draw() {
  background(220)
  casita(50, 50, 50)
  casita(150, 150, 100)
  casita(300, 300, 25)
}
```

De hecho nada nos impide usarlo dentro de un bucle y hacer un poco de magia:

```javascript
function draw() {
  background(220)
  for (var i=0;i<20;i++){
    casita(i*10, i*10, i*10)
  }
}
```

Los valores que se envían a las funciones y se almacenan en los parámetros se denominan argumentos. Aunque en realidad son datos correlativos (unos se envían y los otros se reciben), es importante diferenciarlos porque los parámetros tienen nombre y los argumentos no.

### Retorno de valores

Para acabar el tema de las funciones vamos a ver otra de sus características, ya que éstas no sólo pueden recibir información, también pueden devolverla y esta funcionalidad se conoce como retorno de valores. 

Vamos a hacer un ejemplo para que veáis la utilidad porque se trata de un concepto muy simple.

¿Recordáis la operación módulo? La utilizamos para dibujar el tablero de ajedrez, concretamente para identificar si un número era par o impar. Pues vamos a crearnos una función que haga precisamente eso.

`17 - Retorno/sketch.js`
```javascript
function setup() {
  createCanvas(400, 400);
  for(var i=0;i<10;i++) {
    esPar(i)
  }
}

function draw() {
  background(220)
}

function esPar(numero) {
  if (numero % 2 == 0) {
    print(numero, "es par")
  } else {
    print(numero, "es impar")
  }
}
```


Muy bien, nuestra función recibe un número, hace un cálculo y nos muestra un mensaje por pantalla. Pero... ¿Y si en lugar de mostrar un mensaje quisiéramos utilizarla para colorear las filas pares de una tabla? Está claro que con mostrar un mensaje no es suficiente, necesitamos algo más y eso es que la función se comunique con el exterior para decirnos si el número es par o no.

Para lograrlo utilizaremos el retorno de valores y podemos hacerlo de una forma muy sencilla, devolviendo **true** si el número es par y **false** si es impar:

```javascript
function esPar(numero) {
  if (numero % 2 == 0) {
    return true
  } else {
    return false
  }
}
```

Esto se puede simplificar en dos líneas ya que como hemos dicho **return** no sólo devuelve un valor sino que también finaliza la función, haciendo imposible que se ejecute más de un **return** en la misma función:

```javascript
function esPar(numero) {
  if (numero % 2 == 0) return true
  return false
}
```

La instrucción return nos permite finalizar una función y devolver un valor al exterior. Ese valor podemos almacenarlo en una variable o utilizarlo directamente:

```javascript
function setup() {
  createCanvas(400, 400);
  for(var i=0;i<10;i++) {
    var resultado = esPar(i)
    if (resultado) print(i, "es par")
    else print(i, "es impar")
  }
}
```

Ahora que sabemos cómo almacenar los datos que devuelve una función ya podemos dibujar nuestra tabla con las filas pares coloreadas:

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220)
  var filas = 25;
  for(var i=0;i<filas;i++) {
    fila(0, i*(height/filas), width, height/filas, esPar(i))
  }
}

function esPar(numero ) {
  if (numero % 2 == 0) return true
  return false
}

function fila(x, y, anchura, altura, esPar){
  if (esPar) fill(150) 
  else noFill()
  rect(x, y, anchura, altura)
}
```

¿Qué os ha parecido este ejemplo? Ahora ya sabéis como lo hacen para colorear las filas de las tablas automáticamente.

## Clases 

Vamos a llegar a la idea de clase partiendo de un ejemplo donde dibujamos un objeto simple como un círculo:

```javascript
var circulo = { 
	x: 100, 
	y: 100, 
	d: 50
}

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  ellipse(circulo.x, circulo.y, circulo.d, circulo.d);
}
```

Ahora viene una revelación interesante y es que nosotros sabemos que los objetos almacenan propiedades, pero esas propiedades no tienen porqué ser simples datos, pueden ser funciones:

```javascript
var circulo = { 
	x: 100, 
	y: 100, 
	d: 50,
	saludar: function() { 
		print("¡Hola :3! soy un círculo")
	}
}
```

Para llamar una función de un objeto simplemente accederemos a su nombre y las ejecutaremos como una función normal:

```javascript
function setup() {
  createCanvas(400, 400);
  circulo.saludar();
}
```

Con esto en mente no sería descabellada la idea de incluir en el objeto su propia función **draw** para dibujarse a sí misma, ¿verdad?

```javascript
var circulo = { 
	x: 100, 
	y: 100, 
	d: 50,
	saludar: function() { 
		print("¡Hola :3! soy un círculo")
	},
	draw: function() {
		ellipse(circulo.x, circulo.y, circulo.d, circulo.d);
	}
}

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();  // dibujamos el círculo a sí mismo
}
```

¡Funciona! 

Muy bien muy bien, ¿pero por qué estamos trabajando con funciones si esta es la lección de las clases? Ahora mismo lo váis a descubrir.

Ahora supongamos que quisiéramos dibujar otro círculo a parte del que ya tenemos. ¿Qué haríamos? ¿Copiamos toda la estructura del circulo para crear otro circulo diferente? Nada nos impide hacerlo:

```javascript
var circulo = { 
	x: 100, 
	y: 100, 
	d: 50,
	saludar: function() { 
		print("¡Hola :3! soy un círculo")
	},
	draw: function() {
		ellipse(circulo.x, circulo.y, circulo.d, circulo.d);
	}
}

var circulo2 = { 
	x: 300, 
	y: 300, 
	d: 50,
	saludar: function() { 
		print("¡Hola :3! soy un círculo")
	},
	draw: function() {
		ellipse(circulo2.x, circulo2.y, circulo2.d, circulo2.d);
	}
}

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();
  circulo2.draw();
}
```

¿Y si quisiéramos dibujar 10 círculos tendríamos que crear 10 veces un objeto con las mismas propiedades? 

En seguida se nota que algo no cuadra, debería existir una forma de manejar esto sin repetir tanto código... y así es amigos, esa forma son las clases.

Las clases sirven como moldes para generar objetos con propiedades y funciones comunes en sus estructuras. 

Así que en lugar de crear tantos objetos vamos a crear una clase círculo para generar círculos:

```javascript
class Circulo {
  
}
```

Bien ya tenemos la clase definida.

Ahora necesitamos una forma de definir sus propiedades internas, eso se hace definiendo una función especial que tienen llamado **constructor** que recibe las propiedades que queremos asignar al objeto:

```javascript
class Circulo {
	constructor(x, y, d) {
		alert("Soy un círculo cuyas propiedades valen", x, y, d)
	}
}
```

Fijaros como no tenemos que usar la palabra **function** para crear la función **constructor**.

Muy bien, ahora tenemos que usar esta clase para generar un círculo, eso lo haremos instanciando un objeto a partir de ella con la instrucción **new**:

```javascript
var circulo = new Circulo(100, 100, 50);

function setup() {
  createCanvas(400, 400);
}
```

Como véis así hemos conseguido almacenar en la variable circulo unas propiedades. 

Por cierto, de la misma forma que las variables dentro de los objetos se denominan propiedades, las funciones reciben el nombre de métodos. Por tanto la función **constructor** en realidad se denomina método **constructor**.

Sabiendo eso vamos a añadir el método **draw** a la clase **Circulo** para dibujar la figura:

```javascript
class Circulo {
	constructor(x, y, d) {
		alert("Soy un círculo cuyas propiedades valen", x, y, d)
	}

	draw(){
		ellipse(x, y, d, d);
	}
}

var circulo = new Circulo(100, 100, 50);

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();
}
```

Esta es la única forma como por ahora podemos suponer que se hace, pero lamentablemente esto no va a funcionar. Nos dará un error indicando que no se encuentra la propiedad **x** para poder dibujar el círculo.

¿Por qué ocurre esto? Bueno, no sé si recordaréis que antes para dibujar el círculo a sí mismo lo que hacíamos era pasar a la función **ellipse** los propios valores del objeto **circulo**. En las clases no podemos hacerlo de esa forma, además la idea de que los valores son accesibles entre los métodos haciendo referencia al nombre no funciona de esa forma.

Sí, existe una forma de acceder a las propiedades entre los métodos, pero para entenderla necesitamos aprender el concepto instancia.

### Instancias

Cuando generamos un objeto a partir una clase lo que hacemos en realidad es crear una instancia de esa clase, eso significa reservar un espacio en la memoria del sistema para guardar ahí sus datos.

Podemos consultar la instancia mostrándola directamente en la consola:

```javascript
class Circulo {
	constructor(x, y, d) {
	}

	draw(){
		//ellipse(x, y, d, d);
	}
}

var circulo = new Circulo(100, 100, 50);

function setup() {
  createCanvas(400, 400);
  print(circulo)
}

function draw() {
  background(220);
  circulo.draw();
}
```

Siendo la instancia la representación de un objeto no sería extraño que pudiéramos crearle manualmente una propiedad después de generarla y acceder a ella:

```javascript
class Circulo {
	constructor(x, y, d) {
	}

	draw(){
		//ellipse(x, y, d, d);
	}
}

var circulo = new Circulo(100, 100, 50);
circulo.nombre = "Circulito"

function setup() {
  createCanvas(400, 400);
  print(circulo.nombre)
}

function draw() {
  background(220);
  circulo.draw();
}
```

Así pues sabemos que si creamos una propiedad en una instancia su valor se conserva y podemos seguir usándolo. 

Pues para acceder a esa información dentro de los métodos la idea es la misma, hacer referencia a la instancia. ¿Cómo? Con una propiedad especial de las clases llamada **this**.

### La propiedad this

Dentro de una clase la palabra **this** hace referencia a la propia instancia:

```javascript
class Circulo {
	constructor(x, y, d) {
		this.nombre = "Circulito"
	}

	draw(){
		//ellipse(x, y, d, d);
	}
}

var circulo = new Circulo(100, 100, 50);

function setup() {
  createCanvas(400, 400);
  print(circulo.nombre)
}

function draw() {
  background(220);
  circulo.draw();
}
```

¿Véis? Es la misma idea pero con **this** podemos hacer referencia a la instancia desde dentro, representando al objeto en sí mismo.

Así pues la clave para manejar las propiedades comunes entre los métodos consiste en asignar los valores que enviamos a los métodos a la propia instancia y hacer referencia a ella para acceder a sus valores:

```javascript
class Circulo {
	constructor(x, y, d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}

	draw(){
		ellipse(this.x, this.y, this.d, this.d);
	}
}

var circulo = new Circulo(100, 100, 50);

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();
}
```

En este punto podemos reutilizar nuestra clase Circulo de una forma cómoda para crear más circulos sin repetir código:

```javascript
class Circulo {
	constructor(x, y, d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}

	draw(){
		ellipse(this.x, this.y, this.d, this.d);
	}
}

var circulo = new Circulo(100, 100, 50);
var circulo2 = new Circulo(200, 200, 50);
var circulo3 = new Circulo(300, 300, 50);

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();
  circulo2.draw();
  circulo3.draw();
}
```

¿Mucho mejor verdad? Podemos crear tantas clases, métodos e instancias como queramos, sin duda es una forma magnífica de estructurar nuestro código.

### Clases en ficheros

En esta pequeña lección vamos a introducir el uso de ficheros JavaScript para organizar mejor nuestro código cuando utilizamos clases.

Partiendo del ejemplo anterior:

```javascript
class Circulo {
	constructor(x, y, d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}

	draw(){
		ellipse(this.x, this.y, this.d, this.d);
	}
}

var circulo = new Circulo(100, 100, 50);
var circulo2 = new Circulo(200, 200, 50);
var circulo3 = new Circulo(300, 300, 50);

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  circulo.draw();
  circulo2.draw();
  circulo3.draw();
}
```

La idea consiste en crear un fichero específico para cada clase y cargarlo en el **sketch** para tener un código pulido y bien organizado.

Para hacerlo desplegaremos el panel a la izquierda del editor, donde encontraremos los ficheros que componen un **sketch** en **p5.js**:

* **sketch.js**: El script donde se maneja el código para dibujar en el sketch.
* **index.html**: El fichero principal del proyecto con la estructura HTML.
* **style.css**: El fichero con los estilos visuales en formato CSS.

Bien, pues lo que vamos a hacer es crear un nuevo script JavaScript con el nombre de la clase, en nuestro casp **circulo.js** y dentro trasladaremos la definición de la clase:

`circulo.js`
```javascript
class Circulo {
	constructor(x, y, d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}

	draw(){
		ellipse(this.x, this.y, this.d, this.d);
	}
}
```


Lo único que tendremos que hacer es cargar el fichero en las cabeceras del **index.html**, justo antes de cargar el **sketch.js**.

Es muy importante cargarlo antes porque como se hace uso de la clase **Circulo** en el fichero **sketch.js**, ésta tiene que haberse importado antes:

`index.html`
```html
<body>
	<script src="circulo.js"></script>
	<script src="sketch.js"></script>
</body>
```


¡Listo! Con esto tenemos nuestro proyecto usando clases definidas en sus propios ficheros, una forma perfecta de organizar mejor nuestro código.

## Arreglos

Hasta ahora hemos utilizado datos como números, textos y objetos, pero siempre individualmente. Lo que vamos a ver en esta última sección del curso es una cómo crear unas estructuras para almacenar múltiples datos llamadas arreglos, o en inglés **arrays**..

Un arreglo consiste en un listado que contiene datos separados por comas, como números, textos u objetos.

En la práctica este concepto se ve muy bien con un sencillo ejemplo:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

function setup() {
  createCanvas(400, 400);
  print(colores);  // mostramos los valores
}

function draw() {
  background(220);
}
```

Como véis los arreglos se definen entre corchetes y contienen los datos separados por comas, en nuestro caso es un arreglo con cadenas de texto.

Muy bien tenemos una lista de colores, ¿qué utilidad tiene? Pues por ejemplo que podemos acceder a un elemento en concreto utilizando índices.

### Utilizando índices

Un índice hace referencia a una posición del arreglo, siendo 0 la primera posición:

* 0 => "negro"
* 1 => "azul"
* 2 => "verde"
* 3 => "amarillo"
* 4 => "rojo"

Podemos acceder al dato almacenando en una posición concreta haciendo referencia al índice entre corchetes:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

function setup() {
  createCanvas(400, 400);
  print(colores[0]);
  print(colores[1]);
  print(colores[4);
}

function draw() {
  background(220);
}
```

Vamos a dibujar con la función **text** de **p5** el primer color de nuestro arreglo:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  textSize(24);
  text(colores[0], 100, 100);
}
```

¿Cuál es la gracia de todo esto? Pues que ese índice no tiene porqué ser un valor literal, pueed ser una variable:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

var indice = 0;  // creamos un índice

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  textSize(24);
  text(colores[indice], 100, 100);
}
```

Si ahora definimos un evento de clic y aumentamos ese índice deberíamos ser capaces de ir dibujando los diferentes valores, pues estaremos haciendo referencia a posiciones diferentes dentro del arreglo:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

var indice = 0;  // creamos un índice

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  textSize(24);
  text(colores[indice], 100, 100);
}

function mousePressed(){
  indice++;
}
```

¿Qué os parece?

Evidentemente el último elemento del arreglo es el color "rojo", así que una vez nuestro índice supera esa posición ya no dibuja nada.

Sin embargo nosotros podríamos añadir una condición para reiniciar el indice a 0 en caso de que se supere el número de elementos del arreglo:

```javascript
var colores = ["negro", "azul", "verde", "amarillo", "rojo"]

var indice = 0;  // creamos un índice

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  textSize(24);
  text(colores[indice], 100, 100)
}

function mousePressed(){
  indice++;

  // Como empezamos a contar por 0 el último índice es 1 menos que el número de elementos
  if (indice > 5 - 1){
  	indice = 0;
  }
}
```

Ahora al llegar al final reiniciamos el índice así que vuelve a empezar desde el principio.

Por cierto, existe una forma de conseguir la longitud de un arreglo automáticamente para no tener que contar los elementos a mano:

```javascript
function mousePressed(){
  indice++;

  // Como empezamos a contar por 0 el último índice es 1 menos que el número de elementos
  if (indice > colores.length - 1){
  	indice = 0;
  }
}
```

#### Acceso con índices

Durante la lección anterior aprendimos a trabajar con arreglos utilizando índices y creamos una variablepara ir  accediendo a sus valores mientras la increntábamos.

Ese concepto de crear una variable e incrementarla es la forma como se suele recorrer un arreglo de forma automática. ¿Y sabéis qué? Los bucles **for** son perfectos para ello, sólo tenemos que asumir que el contador del for es el índice del arreglo.

Haciendo eso podemos recorrer todos los elementos de un bucle de una vez.

Vamos a trabajar este concepto con un genial ejemplo donde partiremos de un arreglo con los diámetros de varios círculos:

```javascript
var diametros = [4, 18, 2, 11, 9, 3, 16, 12, 1, 7];

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
```

Para dibujar el primer círculo accederíamos con el índice 0 al primer valor del arreglo:

```javascript
function draw() {
  background(220);
  ellipse(200, 200, diametros[0], diametros[0]);
}
```

Ahora vamos a aplicar la técnica del **for** para recorrer todos los diámetros de arreglo y dibujar un círculo para cada uno:

```javascript
function draw() {
  background(220);
  noFill();  // Desactivamos el relleno para que se vean todos
  for(var i=0;i<diametros.length;i++){
    ellipse(200, 200, diametros[i], diametros[i]);
  }
}
```

No se ve mucho el dibujo porque los diámetros son muy pequeños, pero se están dibujando todos los círculos de una vez.

Ahora viene la parte chula, vamos a crear una variables llamada **factor** que por defecto valdrá 1 y la multiplicaremos por los diámetros:

```javascript
var diametros = [4, 18, 2, 11, 9, 3, 16, 12, 1, 7];
var factor = 1;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  noFill();
  for(var i=0;i<diametros.length;i++){
    ellipse(200, 200, diametros[i]*factor, diametros[i]*factor);
  }
}
```

Y ahora viene la magia, vamos a incrementar ese factor al hacer clic en el lienzo:

```javascript
function mousePressed(){
  factor *= 2;
}
```

¿Habéis visto que efecto más chulo? Si en lugar de presionar nosotros el ratón incrementamos el factor automáticamente al final del **draw**...

```javascript
function draw() {
  background(220);
  noFill();
  for(var i=0;i<diametros.length;i++){
    ellipse(200, 200, diametros[i]*factor, diametros[i]*factor);
  }
  factor *= 2;
}
```

Buenooo todo ocurre muy rápido, pero si modificamos el incremento del factor por un número muy muy pequeño ya veréis:

```javascript
function draw() {
  background(220);
  noFill();
  for(var i=0;i<diametros.length;i++){
    ellipse(200, 200, diametros[i]*factor, diametros[i]*factor);
  }
  factor *= 1.01;
}
```

Si tenemos en cuenta que dentro del arreglo tenemos un diametro que vale 1 píxel, en el momento que el factor sea 400 es cuando ese círculo cerá tan grande como el lienzo. Si aprovechamos y en ese momento reiniciamos el factor a 1 tendremos un bucle infinito muy interesante:

```javascript
var diametros = [4, 18, 2, 11, 9, 3, 16, 12, 1, 7];
var factor = 1;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  noFill();
  for(var i=0;i<diametros.length;i++){
    ellipse(200, 200, diametros[i]*factor, diametros[i]*factor);
  }
  factor *= 1.01;
  if (factor > 400) factor = 1;
}
```

Hipnotizante...

#### Acceso sin índices

En esta pequeña sección vamos a ver otra forma de acceder a los elementos de un objeto sin necesidad de utilizar índice, sólo una variante del for llamada **for .. of**:

```javascript
var numeros = [100, 150, 300, 500]

function setup() {
  createCanvas(400, 400);
  for (var numero of numeros){
    print(numero); 
  }
}

function draw() {
  background(220);
}
```

La gracia de este método es que se recorren los elementos automáticamente mientras se almacenan en la variable que definimos, en nuestro caso **numero**.

Esta forma hace que trabajar con arreglos de objetos sea muy cómodo, por ejemplo podemos crear nuestra propia clase **Circulo** y crear varias instancias en un arreglo para dibujarlas todas en cada fotograma: 

```javascript
class Circulo {
  constructor(r,g,b,d){
    this.r = r;
    this.g = g;
    this.b = b;
    this.d = d;
  }
  
  fill () {
    fill(this.r, this.g, this.b);
  }
  
  draw () {
    this.fill();
    ellipse(random(0,400), random(0,400), this.d, this.d);
  }
}

var circulos = [
  new Circulo(235, 0, 0, 50),
  new Circulo(0, 235, 0, 50),
  new Circulo(0, 0, 235, 50)
]

function setup() {
  createCanvas(400, 400);
  frameRate(1);  // Importante que sea bajo
}

function draw() {
  background(220);
  for (var circulo of circulos){
    circulo.draw();
  }
}
```

En la última lección modificaremos un poco este ejemplo para explicar algunas cosas más.

### Manipulando arreglos

Por último las tres acciones básicas que se pueden realizar sobre un arreglo son:

* **Añadir** elementos.
* **Borrar** elementos.
* **Modificar** elementos.

Vamos a modificar el ejemplo de la lección anterior para ilustrar como funcionan estas acciones:

```javascript
class Circulo {
  constructor(r,g,b,d){
    this.r = r;
    this.g = g;
    this.b = b;
    this.d = d;
  }
  
  fill () {
    fill(this.r, this.g, this.b);
  }
  
  draw () {
    this.fill();
    ellipse(random(0,400), random(0,400), this.d, this.d);
  }
}

var circulos = [
  new Circulo(235, 0, 0, 50),
  new Circulo(0, 235, 0, 50),
  new Circulo(0, 0, 235, 50)
]

function setup() {
  createCanvas(400, 400);
  frameRate(1.5);  // Importante que sea pequeño
}

function draw() {
  background(220);
  for (var circulo of circulos){
    circulo.draw();
  }
}
```

#### Añadir elementos

Podemos añadir nuevos elementos al arreglo en cualquier momento haciendo uso de su método **push**.

Por ejemplo podemos generar un nuevo círculo y añadirlo al arreglo si presionamos presionar la tecla con la **flecha arriba** del teclado tal y como explican en la [documentación de la función keyPressed](https://p5js.org/es/reference/#/p5/keyPressed):

```javascript
function keyPressed() {
  if(keyCode == UP_ARROW) {
    print("Flecha arriba presionada")
  }
}
```

Esto tiene un inconveniente y es que las teclas sólo se detectan si préviamente hemos hecho clic en el lienzo. Sin embargo podemos forzar ese estado al empezar el **sketch** automáticamente:

```javascript
// Esto simula que hacemos clic en el canvas
this.focus();
```

Con esto ya podemos crear nuestro círculo y agregarlo al arreglo sin presionar antes el lienzo:

```javascript
function keyPressed() {
  if(keyCode == UP_ARROW) {  
    // Generamos un círculo
    var circulo = new Circulo(
      random(0,255), random(0,255), random(0,255), 50
    )
    // Lo añadimos al arreglo con push
    circulos.push(circulo);
  }
}
```

Por defecto se añadirá al final de arreglo y se irá dibujando automáticamente.

Por cierto sería útil dibujar un texto con el número de círculos:

```javascript
function draw() {
  background(220);
  for (var circulo of circulos){
    circulo.draw();
  }
  // Dibujamos el número de círculos
  fill(0)
  textSize(25)
  text(circulos.length, 15, 35)
}
```

#### Borrar elementos

El borrado de elementos de un arreglo consiste en sacar esos elementos de arreglo. Existen diferentes métodos para hacerlo y los más básicos son:

* **pop()**: Para extraer del arreglo su último elemento.
* **shift()**: Para extraer del arreglo su primer elemento.
* **splice(indice, cantidad)**: Para extraer del arreglo una cantidad de elementos a partir de una posicion determinada.

Podéis elegir el que queráis dependiendo de vuestras necesidades, en nuestro caso simplemente borarremos el primer círculo del arreglo con **shift** al presionar la **flecha abajo**:

```javascript
function keyPressed() {
  if(keyCode == UP_ARROW) {  
    // Generamos un círculo
    var circulo = new Circulo(
      random(0,255), random(0,255), random(0,255), 50
    )
    // Lo añadimos al arreglo con push
    circulos.push(circulo);
  } 

  else if (keyCode == DOWN_ARROW) {  
    // Borramos el primer círculo
    circulos.shift();
  }
}
```

#### Modificar elementos

Por último veamos como modificar algún valor de nuestros círculso dinámicamente, por ejemplo podríamos darles un tamaño aleatorio al hacer clic con el ratón.

Sólo tenemos que recorrer los objetos y modificar su diámetro:
  
```javascript
function mousePressed(){
  var diametro = random(1, 100);
  for (var circulo of circulos){
    circulo.d = diametro;
  }
}
```

Este es el código final del ejemplo:

```javascript
this.focus();

class Circulo {
  constructor(r,g,b,d){
    this.r = r;
    this.g = g;
    this.b = b;
    this.d = d;
  }
  
  fill () {
    fill(this.r, this.g, this.b);
  }
  
  draw () {
    this.fill();
    ellipse(random(0,400), random(0,400), this.d, this.d);
  }
}

var circulos = [
  new Circulo(235, 0, 0, 50),
  new Circulo(0, 235, 0, 50),
  new Circulo(0, 0, 235, 50)
]

function setup() {
  createCanvas(400, 400);
  frameRate(1);
}

function draw() {
  background(220);
  for (var circulo of circulos){
    circulo.draw();
  }
  // Dibujamos el número de círculos
  fill(0)
  textSize(25)
  text(circulos.length, 15, 35)
}


function keyPressed() {
  
  if(keyCode == UP_ARROW) {  
    // Generamos un círculo
    var circulo = new Circulo(
      random(0,255), random(0,255), random(0,255), 50
    )
    // Lo añadimos al arreglo con push
    circulos.push(circulo);
  } 
  
  else if (keyCode == DOWN_ARROW) {  
    // Borramos el primer círculo
    circulos.shift();
  } 
}
  
function mousePressed(){
  var diametro = random(1, 100);
  for (var circulo of circulos){
    circulo.d = diametro;
  }
}
```

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>