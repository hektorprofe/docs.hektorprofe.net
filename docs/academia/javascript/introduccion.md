title: Introducción | JavaScript | Academia | Hektor Profe
description: Aprende lo fundamental de este poderoso lenguaje utilizado tanto para desarrollo frontend como para backend.

# Introducción a JavaScript

<div class="contenedor_youtube">
  <iframe id="odysee-iframe" width="560" height="315" src="https://odysee.com/$/embed/-Curso--JavaScript-para-principiantes/95740f48927a8cb7d76849b8867cf1db0c0fceb0?r=3icueB68NV3UEFHyqs2QRfzRUeABmHDU" allowfullscreen></iframe>
</div>

Si te interesa aprender este lenguaje pero no sabes muy bien por dónde empezar, en este pequeño curso comparto contigo los primeros pasos que debes seguir para configurar tu entorno de desarrollo, crear tus primeros scripts y los tipos de datos básicos del lenguaje.

Independientemente del uso que quieras darle al lenguaje estos son los fundamentos que deben quedarte claros desde el principio, ya que estarás utilizándolos durante todo el tiempo.

Además haremos un breve repaso del uso que se le da profesionalmente para que no te quede ninguna duda antes de lanzarte a la piscina.

## Qué es JavaScript

JavaScript es uno de los lenguajes más famosos y utilizados del mundo, de hecho en perspectiva es el que tiene un crecimiento más constante y muchas grandes empresas como Netflix y Paypal lo utilizan para desarrollar sus aplicaciones.

Es sinónimo de empleo, tanto en el presente como en el futuro, ya que con él es posible especializarse en diferentes ramas:

* Desarrollador Front-end
* Desarrollador Back-end
* Desarrollador Full-Stack (ambas)

### ¿Qué se puede crear con él? 

Por mucho tiempo JavaScript fue utilizando únicamente en los navegadores para crear webs interactivas. Algunos desarrolladores se refirieron a él como un lenguaje pobre pero esos días quedaron atrás gracias al gran apoyo de su comunidad y a las inversiones de grandes compañías como Google y Facebook.

Actualmente JavaScript se puede utilizar para desarrollar:

* Aplicaciones web
* Aplicaciones móviles
* Aplicaciones con comunicación en tiempo real (chats, streaming...)
* Scripts y herramientas para la línea de comandos
* Videojuegos, tanto en 2D como 3D

### ¿Cómo se ejecuta?

Originalmente JavaScript se ideó para funcionar únicamente en navegadores, de manera que estos requerían incluir un motor para ejecutar su código. Por  ejemplo, el motor JavaScript de Firefox es el denominado SpiderMonkey y el de Chrome se llama v8.

Os cuento todo esto porque en 2009 un ingeniero llamado Ryan Dahl (~Döl) tomó el código open source del motor JavaScript de Chrome y lo embebió dentro de un programa de C++ al que llamó Node. En otras palabras, Node es un programa que incluye el motor v8 y nos permite ejecutar código JavaScript fuera del navegador. Esto hizo que JavaScript diera un salto, pasando de ser un lenguaje de frontend a un lenguaje todoterreno capaz de dar respuesta a todo tipo de necesidades.

### ¿Qué es ECMAScript?

Pues ECMAScript es sólo una especificación, mientras que JavaScript es un lenguaje de programación que confirma esa especificación. Es la organización ECMA (European Computers Manufacturers Association) la que se ocupa de desarrollar los estándares que luego se implementarán en los motores que ejecutarán JavaScript.

La primera especificación de ECMAScript (v1) se publicó en 1997, y aunque ha habido pequeñas revisiones, no fue hasta 2015 cuando se publicó la especificación ECMAScript 6, también conocida como ECMAScript 2015. Desde entonces cada año se lanza una nueva revisión añadiendo mejoras al lenguaje.

Pero basta de tanta cháchara y vamos a practicar para que podáis experimentar un poco lo que ofrece este lenguaje.

## Primer contacto

Como ya sabemos para ejecutar Javascript sólo necesitamos un navegador. Chrome por ejemplo integra un entorno de ejecución en tiempo real donde podemos hacer algunas pruebas.

Para abrirlo tenemos que acceder a la **Consola** de las **Herramientas para desarrolladores**, o haciendo clic derecho **Inspeccionar** en medio de una página.

Probad lo siguiente:

```javascript
console.log('Hola mundo');
```

Con esa instrucción podemos mostrar un mensaje en la consola, es el típico print de todos los lenguajes.

También podemos sumar dos números, como si fuera una calculadora:

```javascript
2 + 2
```

O interactuar con el navegador introduciendo este comando:

```javascript
alert('Hola mundo')
```

Como bien comentamos en la lección anterior, Javascript se creó para añadir interactividad en las páginas web, ¿pero esto qué significa? 

Si conocéis HTML sabréis que este lenguaje describe una estructura utilizando marcas. Estas marcas crean jerarquías que el navegador transforma en una estructura dinámica y viva con la que podemos interactuar, esa estructura se denomina DOM, Document Object Model o árbol de componentes. 

Vamos a experimentar un poco con algunas instrucciones que nos permiten interactuar con el DOM del documento actual:

```javascript
document.title = "Nuevo título"
```

No siempre es tan fácil modificar los componentes del documento…

```javascript
document.body = "Algo" // Esto no funcionará
```

Eso es debido a que la estructura del body es más compleja que el título:

```javascript
document.body.innerHTML = "Que tal"
```

Obviamente podemos poner contenido en lenguaje HTML:

```javascript
document.body.innerHTML = "<h1>Cabecera de primer nivel</h1>"
document.body.innerHTML += "<p>Esto es un parágrafo...</p>"
```

Vamos a dejarlo por ahora porque tampoco quiero abrumaros, además estoy seguro de que con esto ya empezáis a haceros una idea de lo que JavaScript nos permite hacer.

## Configurando el entorno

Si queremos escribir código Javascript, necesitamos un editor de código. Algunos editores muy extendidos hoy en día pueden ser:

* Visual Studio Code
* Sublime Text
* Atom

Hay muchos más pero mi favorito es VSCode, que se puede descargar desde [su web oficial](https://code.visualstudio.com). Es simple de utilizar, ligero y multiplataforma, es el que utilizaré en el curso así que podéis descargarlo e instalarlo siguiendo los pasos.

Lo segundo que necesitamos para tener un buen entorno de trabajo es Node, que se puede descargar desde [su web oficial](https://nodejs.org). Estrictamente no es necesario, pero es muy útil tenerlo para instalar librerías de terceros usando su gestor de paquetes npm.

Pausad el vídeo y tomaros vuestro tiempo para instalar Node, la versión LTS os servirá perfectamente; cuando lo tengáis seguiremos configurando un poco VSCode.

Para configurar VSCode vamos a hacerlo con un nuevo proyecto. Simplemente es necesario crear un directorio (por ejemplo **curso-js**) y lo abriremos con VSCode. 

Añadiremos un nuevo fichero llamado *index.html*, se supone que ya deberéis saber un poco de HTML así que no os extrañará esta parte. Ahora podemos escribir un **!** y presionar el tabulador, eso generará una plantilla HTML predefinida, también se puede escribir **html:5**:

`index.html`
```html
!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
</body>
</html>
```

Guardamos… y ahora vamos a instalar una extensión llamada **Live Server** que nos servirá para ver y actualizar en tiempo real los cambios en nuestras páginas HTML.

Una vez instalada y habiendo recargado VSCode si es necesario, podemos hacer clic derecho en el **index.html** y abrirlo en el Live Server.

Ahora si escribimos algo de código en el body, debería mostrarse automáticamente en el navegador al guardar el fichero:

```html
<body>
  <h1>Hola mundo</h1>
</body>
```

## Ejecución en el navegador

Ya lo tenemos todo preparado para escribir nuestro código JavaScript, ¿cómo y dónde lo hacemos?

* HTML integra una etiqueta llamada **script**, ella es la encargada de contener el código JavaScript. 
* En cuanto al dónde, hay dos lugares posibles: dentro de la cabecera **head** o dentro del **body**. 
* Lo más recomendable es añadirlo al final del body, justo después de todo el contenido. Hay dos razones para ello: 
    * La primera es que el navegador ejecuta el código de arriba hacia abajo, por lo que si ponemos el script en la cabecera, en el caso en que tengamos mucho código, el navegador no seguirá renderizando la web hasta que no haya procesado todo ese código y eso podría afectar negativamente a la experiencia de los usuarios. 
    * La segunda es la propia naturaleza de Javascript, y es que como explicamos antes está pensado para interactuar con el DOM. El problema es que para hacer referencia a esos elementos, estos tienen que haberse creado antes. En otras palabras, si por ejemplo ejecutamos un código para interactuar con un campo de texto, si ese campo no se ha renderizado no podremos interactuar con él. Solo podemos interactuar con los elementos HTML definidos antes del bloque **script**, y por eso poniéndolo al final estaremos seguro de que existen todos y podemos interactuar con cualquier elemento de la página.

`index.html`
```html
<body>
  <h1>Hola mundo</h1>
  <script>
  </script>
</body>
``` 

Es importante comentar que hay un caso excepcional donde sí se está bien definir un bloque script en la cabecera antes del body, relacionado con la carga de recursos y librerías de terceros, pero de eso ya hablaremos más adelante.

Por ahora vamos a intentar ejecutar algo simple:

```html
<script>
  // Esto es un comentario
  console.log('Hola mundo');
</script>
``` 

Si volvemos al navegador ya nos debería aparecer el mensaje en la consola del inspector.

## Separando el código

Organizar el código es fundamental para crear aplicaciones escalables y bien ordenadas, de ahí que no sea necesario escribir todo nuestro código en el propio HTML, podemos escribirlo en sus propios ficheros y cargarlos como si fueran librerías de código.

Vamos a crear un fichero **index.js** en nuestro proyecto y dentro escribiremos el código javascript sin las etiquetas:

`index.js` 
```javascript
// Esto es un comentario
console.log('Hola mundo');
``` 

Ahora podemos cambiar lo que teníamos antes y cargar este fichero con su contenido de la siguiente forma:

`index.html`
```html
  <script src="index.js"></script>
</body>
``` 

Funcionará exactamente igual que antes, pero habremos separado el código, dejando el HTML con la maquetación y el scripts JS para la lógica de JavaScript.

## Ejecución en Node.js

Al haber separado el código, hemos conseguido un script que se puede ejecutar también a través de Node.js. Para probarlo tendremos que abrir una terminal, navegador al directorio y ejecutar el siguiente comando:

```bash
node index.js
```

Así le pasaremos a node el scripts y éste ejecutará el contenido usando el motor v8 de Google.

Si hacemos uso de VSCode esto se simplifica gracias a la terminal integrada, ya que podremos ejecutar el código cómodamente ahí.

## Variables

Empezamos nuestro recorrido por los conceptos fundamentales hablando del más importante, no sólo de Javascript sino de cualquier lenguaje: las variables.

Programar sirve esencialmente para manipular datos o información, y para manipularlos muchas veces necesitaremos almacenarlos.

Utilizamos las variables para almacenar esos datos temporalmente en la memoria de los ordenadores. Así pues, una variable no es más que un nombre que damos a un espacio de la memoria donde guardaremos algunos datos. La clave está en que mientras tengamos el nombre de la variable siempre podremos acceder a la información que contiene.

Tradicionalmente en JavaScript se utiliza la palabra reservada **var** para declarar una variable, pero desde ES6 también se puede usar **let**. Su diferencia radica en los ámbitos que abarcan: **var** afecta al ámbito de la función y **let** al bloque, no quiero entrar en detalles para no liaros, si tenéis curiosidad así que os dejaré [un enlace](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Sentencias/let) donde se explican en detalle.

Sea como sea vamos a crear una variable en el **index.js** usando **let** para irnos acostumbrando:

`index.js`
```javascript
let nombre;

console.log(nombre);
``` 

Al ejecutarse este código veremos que el resultado es **undefined**, no definido. Esto nos indica que no tiene un valor asignado, así que vamos a darle uno. Podemos hacerlo inicializando la variable durante la declaración:

```javascript
let nombre = 'Héctor';  // tipo texto => cadena de caracteres => string

console.log(nombre);
``` 

Las cadenas son un tipo de datos pueden declararse de varias formas, normalmente limitando el texto entre comillas simples o dobles.

Así que hemos declarado una variable llamada nombre que contiene información de tipo texto.

Es importante comentar que no se puede ni se debe establecer cualquier nombre para una variable, hay que seguir algunas reglas y buenas prácticas:

1. No se puede usar de nombre una palabra reservada. Éstas forman parte de la sintaxis del lenguaje, por ejemplo let, var, if, for… No os preocupéis porque el propio editor os indicará un fallo si da la casualidad que habéis puesto un nombre reservado.
2. No pueden comenzar con un número.
3. No pueden contener espacios ni guiones, aunque sí guiones bajos, pero por convención es recomendable usar la notación camel case:


```javascript
let primerApellido;
let segundoApellido;
```

4. Deberían tener nombres descriptivos que den información contextual. Por ejemplo, nombres como a, b, x… no nos dan ninguna información y eso puede llevarnos a confusiones.
5. Son case sensitive, es decir, las mayúsculas y minúsculas afectan directamente a la singularidad de las variables. Por ejemplo, no es lo mismo primerApellido que PrimerApellido, son dos variables diferentes. 
6. Por último, si bien se pueden declarar múltiples variables en una línea separándolas por comas:

```javascript
let primerApellido = 'Costa', segundoApellido = 'Guzmán';
``` 

Es más recomendable hacerlo en dos para mejorar la legilibilidad:

```javascript
let primerApellido = 'Costa';
let segundoApellido = 'Guzmán';
```

## Constantes

Ya hemos visto lo que es una variable, pero lo que le da sentido al nombre es su capacidad de cambiar de valor en cualquier momento, es decir, de tener un valor variable.

Tomemos una variable numérica llamada número con un valor de 50:

`index.js`
```javascript
let numero = 50; // tipo número

console.log(numero);
``` 

Ahora supongamos que en un determinado momento necesitamos cambiar el 50 por otro número,, sería tan fácil como asignarlo con el igual, pero esta vez no necesitamos declarar la variable, sólo modificar el valor:

```javascript
let numero = 50;
numero = 100;

console.log(numero);
``` 

Ahora bien, quizá en algún momento nos gustaría proteger el valor inicial de una variable para que no se pueda editar. Para lograr esa funcionalidad haríamos uso de las constantes:

```javascript
const numero = 50;
numero = 100;

console.log(numero);
``` 

Al ejecutarse este código veremos un error en la consola **TypeError: Assignment to constant variable**. Tal como su nombre indica, un valor constante no puede cambiar, de ahí que de el error.

## Tipos primitivos

Ahora que sabemos como declarar e inicializar variables, es un buen momento para repasar los tipos de valores que podemos asignar a una variable en JavaScript. 

Ya  hemos visto las cadenas y los números, pero hay otros y además se organizan en dos tipos:

* Los tipos por valor o primitivos.
* Los tipos por referencia.

Vamos a hablar de los primeros, los otros los tocaré en las siguientes lecciones.

En la categoría de los tipos primitivos encontramos esencialmente 5:

* String (cadena)
* Number (número)
* Boolean (booleano)
* undefined (no definido)
* null (nulos)

El sentido de los tipos cadenas y número es implícito, pues sirven para almacenar información de ese tipo:

`index.js`
```javascript
let nombre = 'Héctor'; // literal cadena
let edad = 30; // literal número
``` 

El tipo booleano o lógico podemos entenderlo como el sentido afirmativo o negativo de una sentencia. Únicamente puede tener dos valores true o false (verdadero o falso), que por cierto son palabras reservadas:

```javascript
let llevoGafas = true; // literal booleano
``` 

El tipo indefinido ya lo vimos anteriormente, es el valor que tiene por defecto una variable no inicializada, que también se puede asignar:

```javascript
let apellido;
let apellido = undefined;
``` 

Por último el tipo nulo se utiliza para establecer un valor vacío en una variable, es decir, limpiar el valor pero dejando rastro de que la variable sí tuvo un valor anteriormente:

```javascript
let apellido = 'Costa';
let apellido = null;

console.log(apellido);
``` 

Y es que tenemos que entender que no es lo mismo el concepto de vacío que de indefinido. En el primero se entiende que ha habido o que habrá un valor, mientras que el otro indica que todavía no se ha asignado nada.

En cualquier caso es una cosa que os iréis topando con la práctica, así que no os preocupéis demasiado por ello.

## Tipado dinámico

JavaScript, al igual que Python, es un lenguaje de tipado dinámico.

Hay dos formas de tipado:

* Estático
* Dinámico

En los lenguajes estáticos, cuando declaramos una variable es necesario especificar el tipo que tiene y ese tipo es inalterable:

```javascript
String nombre = 'Héctor'; // java
```

En cambio en lenguajes como JavaScript, no es necesario establecer un tipo y además puede cambiar en cualquier momento, eso es porque viene determinado en tiempo de ejecución por el valor asignado a la variable:

```javascript
let nombre = 'Héctor'; // javascript
```

Podemos ver esto en acción desde la consola del navegador haciendo uso del operador **typeof**. Éste nos permite saber el tipo de una variable:

```javascript
typeof nombre

> "string"
```

Como vemos inicialmente la variable nombre es de tipo string, pero si le asignamos un número cambiará:

```javascript
nombre = 10
typeof nombre

> "number"
```

Algo interesante es que Javascript a diferencia de otros lenguajes no distingue explícitamente entre números enteros y flotantes como pasa en otros lenguajes. Si establecemos el valor…

```javascript
nombre = 10.5
typeof nombre

> "number"
```

Seguiremos teniendo un tipo number. 

Por cierto, notad que los decimales se escriben con un punto y no una coma, eso como siempre digo es "de facto" en casi todos los lenguajes, pues en inglés se escriben de esa forma.

Experimentad vosotros mismos un poco más con los otros tipos.

## Objetos

Es hora de hablar de los tipos por referencia que dejamos pendientes. Dentro de esta categoría encontramos:

* Objetos
* Arreglos
* Funciones

Así que vamos a empezar con los primeros.

## ¿Qué es un objeto?

En JavaScript y otros lenguajes, un objeto es eso, un objeto. De acuerdo, no es la mejor definición, pero se entiende mejor si pensamos en ello como la representación virtual de un objeto real. 

Mirad, los objetos en la vida real comparten propiedades que permiten definirlos. Por ejemplo pensemos en una persona. Hay muchas personas, pero todas comparten algunas propiedades comunes: tienen un nombre, un apellido, una edad...

Vamos a trasladar este concepto a código.

Partamos de la base que tenemos tres variables para representar esas propiedades de una persona:

`index.js`
```javascript
let nombre = 'Héctor';
let apellido = 'Costa';
let edad = 30;
```

Necesitamos una forma de trabajar con las tres variables en conjunto, es decir, un objeto. Lo haremos con la siguiente sintaxis:

```javascript
let persona = {

};
```

Las llaves indican que vamos a definir un objeto, cuyo contenido se declara en pares clave-valor.

Cada clave es como el nombre de la variable pero para la propiedad del objeto y seguido de dos puntos vendría el valor:

```javascript
let persona = {
  nombre: 'Héctor',
  apellido: 'Costa',
  edad: 30;
};

console.log(persona);
```

Como podremos observar en la consola, el objeto persona está formado por las tres propiedades.

Hay dos formas de trabajar con las propiedades de un objeto. Por ejemplo, si queremos modificar el contenido de una propiedad podemos usar:

```javascript
// Notación con punto

persona.nombre = 'Daniel';
console.log(persona.nombre);
```

O también:

```javascript
// Notación con corchetes

persona['nombre'] = 'Javier';
console.log(persona['nombre']);
```

La notación con corchetes tiene la ventaja de que puede ser dinámica, es decir, podemos definir en una variable una cadena con el nombre de la propiedad que queremos manipular:

```javascript
let propiedad = 'nombre';

persona[propiedad] = 'Fernando';
console.log(persona[propiedad]);
```

Quizá os parece algo confuso y no lo veis mucha utilidad, pero estoy seguro que dentro de un tiempo  recordaréis este truco y os hará un buen servicio.

## Arreglos

Cuando trabajamos con datos, a menudo necesitamos lidiar con más de uno a la vez. Eso lo conseguimos  en conjuntos llamados arreglos, arrays en inglés.

Dentro de un arreglo podemos definir varios elementos, ya sean literales u objetos. Por ejemplo, un arreglo de nombres:

`index.js`
```javascript
let nombres = ['Héctor', 'Daniel', 'Javier'];

console.log(nombres);
```

Si observamos la consola veremos que cada elemento dentro del array tiene un índice numérico. Este índice representa la posición del elemento en el arreglo, y el primer elemento siempre concuerda con el índice cero. De hecho utilizando estos índices podemos mostrar un solo elemento del arreglo:

```javascript
console.log(nombres[0]);
```

Como ya comentamos, JavaScript es un lenguaje dinámico que permite a las variables cambiar de tipo al vuelo. Lo mismo ocurre con los arreglos y su longitud, el número de elementos que contienen es dinámico, permitiéndonos añadir elementos de forma muy sencilla:

```javascript
nombres[3] = 'Juanito';

console.log(nombres);
```

Además no estamos limitados a añadir elementos del mismo tipo, podemos mezclar cualquier tipo de dato, incluso objetos dentro de un arreglo:

```javascript
nombres[1] = 999;

console.log(nombres);
```

¿Pero qué tipo de dato es un arreglo?

```javascript
typeof nombres

> "object"
```

¿Os esperábais un tipo array? Pues no, es un tipo de objeto que ya viene creado en JavaScript, y lo bueno es que contiene un montón de propiedades por defecto, las cuales podemos ver en el editor VSCode poniendo un puntito tras el arreglo.

Una de ellas es tremendamente útil y nos permite saber la longitud del arreglo, es decir, el número de elementos que contiene:

```javascript
console.log(nombres.length);
```

En una futura sección trataremos más en profundidad el tema de los arreglos y cómo trabajar con todas esas propiedades que contienen.

## Funciones

Dentro de los tipos por referencia ya hemos aprendido sobre los objetos y los arreglos, ahora es el turno de las funciones.

Las funciones son uno de los tipos de bloque de código fundamentales en la programación. Son esencialmente una serie de instrucciones reutilizables que realizan una determinada tarea o cálculo sobre unos valores. 

Se entiende mucho mejor en la práctica, así que vamos a crear una para su funcionamiento:

`index.js`
```javascript
function saludar() {
  console.log('Hola mundo');
}
```

No es necesario finalizar el bloque de la función con punto coma.

Una vez la tenemos definida la podemos ejecutar haciendo referencia a su nombre:

```javascript
saludar();
```

Los paréntesis es lo que indica que queremos ejecutar la función, sino los ponemos simplemente haríamos referencia a ella. 

Podemos ejecutarla tantas veces como queramos:

```javascript
saludar();
saludar();
saludar();
```

Tal como tenemos nuestra función no es muy útil, sólo imprime un mensaje, vamos a transformarla en algo más interesante.

Las funciones pueden recibir datos, datos que pueden manipularse dentro de la función para realizar diferentes tareas. Es precisamente el hecho de que una función puede recibir datos lo que las hace tan versátiles y uno de los conceptos claves de la programación.

Por ejemplo podríamos recibir un nombre y saludarlo. Para hacerlo es muy sencillo, sólo tenemos que definir un parámetro de la siguiente forma:

```javascript
function saludar(nombre) {
  console.log('Hola mundo');
}
```

El parámetro nombre se comportará como una variable que únicamente existirá dentro de la función, así que podemos hacer uso de ella:

```javascript
function saludar(nombre) {
  console.log('Hola ' + nombre);
}
```

Ahora para enviar el nombre, deberemos pasar el valor durante la llamada de la función como si fuera una variable o literal:

```javascript
saludar('Héctor');
```

En este punto es importante hacer una aclaración. Los valores que enviamos a una función se llaman argumentos, pero durante la definición nos referimos a ellos como parámetros.

Sea como sea con este cambio hemos transformado la función en algo dinámico que tiene comportamientos distintos dependiendo del nombre que le pasemos:

```javascript
saludar('Daniel');
saludar('Javier');
```

¿Y si quisiéramos enviar un segundo argumento con el apellido? Pues deberíamos añadir un segundo parámetro en la definición:

```javascript
function saludar(nombre, apellido) {
  console.log('Hola ' + nombre + ' ' + apellido);  // es mejorable
} 
```

Y al ejecutarlo enviar ese segundo argumento:

```javascript
saludar('Héctor', 'Costa');
```

Por cierto, ¿qué valor creéis que tiene el parámetro apellido si no lo enviamos?

```javascript
saludar('Héctor');
```

Pues tiene el valor **undefined**, como si fuera una variable no inicializada en el ámbito de la función.

## Funciones con retorno

Como os expliqué, las funciones pueden recibir argumentos y manejar sus valores como parámetros:

`index.js`
```javascript
function doblar(numero) {
  console.log(numero*2);
}

doblar(5);
```

El problema es que sólo existen dentro de su propio bloque, por lo que no podemos acceder a esa información desde el exterior:

```javascript
console.log(numero);

> Uncaught ReferenceError: numero is not defined
```

Si en lugar de mostrar el doble del número quisiéramos devolver ese valor al exterior para seguir trabajando con él, entonces necesitaremos usar el retorno de valores:

```javascript
function doblar(numero) {
  return numero*2;
}

doblar(5);
```

En este momento veremos que no se muestra nada, tendríamos que ponerlo en un **console.log()**:

```javascript
console.log(doblar(5));
```

Sin embargo la utilidad más común es almacenar el valor en una variable para poder seguir trabajando con ella:

```javascript
let numero = doblar(5);

console.log(numero);
```

De esta forma habremos devuelto un cálculo interno de la función al exterior.

Por cierto, imaginaros que queremos el doble del doble del doble de un número. ¿Cómo podríamos hacerlo? Pues fácil, llamando de forma anidada la función 3 veces:

```javascript
let numero = doblar(doblar(doblar(5)));  // 5 -> 10 -> 20 -> 40

console.log(numero);
```

No importa si no acabáis de entenderlo, era un ejemplo para liaros un poco. 

Lo que debéis recordar es que las funciones son un conjunto de instrucciones reutilizables identificadas con un nombre, que tienen como objetivo realizar una tarea o un cálculo y que pueden comunicarse con el exterior recibiendo y retornando datos.

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>