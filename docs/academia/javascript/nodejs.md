title: Introducción a Node.js | JavaScript | Academia | Hektor Profe
description: Aprende lo básico de Node, un entorno de ejecución JavaScript para el backend usado en la creación de servicios de networking.

# Introducción a Node.js

<!-- <div class="contenedor_youtube">
  <iframe width="838" height="470" src="https://www.youtube.com/embed/aMn4gcJfJA0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div> -->

Si ya cuentas con conocimientos básicos de JavaScript para el frontend, no pierdes nada por dar una oportunidad a Node.js y alcanzar el siguiente nivel.

A lo largo de este curso aprenderás para qué sirve, cómo implementar tus propios módulos de desarrollo y a utilizar algunos de los que vienen incluidos en su núcleo para desarrollar servicios de networking, como por ejemplo un servidor HTTP o una API de pruebas.

## ¿Qué es Node.js?

No pierdas la oportunidad de aprender esta tecnología que te puede ofrecer tanto a cambio de muy poco.

### ¿Para qué sirve?

Node se utiliza sobretodo para crear servicios backend conocidos como APIs, en español Interfaces de Programación de Aplicaciones. Estos son los servicios que potencian las aplicaciones conocidas como clientes. 

### Arquitectura cliente-servidor

Normalmente las aplicaciones cliente ofrecen bonitas interfaces que permiten a los usuarios interactuar con ellas cómodamente, por ejemplo una web funcionando en un navegador o una app móvil en tu smartphone son clientes.

Sin embargo lo que se ve es sólo la punta del iceberg, porque los clientes por sí mismo no tienen mucha utilidad, necesitan apoyarse de servicios centralizados conocidos como servidores, ellos son los encargados de almacenar información en la nube, registros en las bases de datos, enviar correos, notificaciones y mucho más, todo sin que el usuario se percate de lo que ocurre tras bambalinas.

### Ventajas que ofrece

Pues Node es ideal para crear este tipo de servicios porque es relativamente fácil de aprender comparado con otros frameworks como ASP.NET, Rails o Django que tienen una curva de aprendizaje mayor. 

Con Node en muy poco tiempo puedes tener prototipos funcionales que además ofrecen mucho rendimiento gracias a que se ejecutan sobre el motor v8 de Google. Esto sumado a que permite crear servicios escalables, son algunas de las razones por las que grandes compañías como Paypal, Netflix o Spotify lo utilizan. 

Además como Node utiliza JavaScript, si eres un programador web frontend y quieres transicionar o empezar con el backend, puedes hacerlo sin aprender un nuevo lenguaje.

Pero sobre todo lo demás, lo que destaca de Node es el enorme ecosistema que ha conseguido en muy pocos años. Si el de Python es ya inmenso con más de 175.000 paquetes, el de Node es absurdamente inmenso pues supera a día de hoy los 800.000 paquetes según las estimaciones de la web [modulecounts.com](http://www.modulecounts.com/).

Sin duda Node es una herramienta que vale la pena conocer, puede ofrecerte mucho a cambio de muy poco.

## Prompt de Node

Como ya vimos Node es un programa que se instala en el sistema y podemos ejecutarlo desde la terminal escribiendo:
 
```bash
node
```

Al ejecutarlo accederemos al Prompt de Node, una línea de comandos que nos permite ejecutar diferentes instrucciones en lenguaje JavaScript. 

Podemos realizar algunas operaciones al vuelo:

```javascript
2 + 2
5 * 5
```

Declarar variables y operarlas:

```javascript
a = 10
b = 5

a + b
```

Y no sólo podemos usar tipos primitivos, también podemos declarar un arreglo y manipularlo:

```javascript
palabras = ['casa', 'ordenador', 'coche']

palabras[0]
palabras[1]
```

Incluso una función:

```javascript
function saludar() { console.log("Hola mundo") }
saludar()
```

Algo que vale la pena comentar, es que si bien cuando ejecutamos JavaScript en el navegador contamos con una ventana para interactuar con ella y conseguir información de la ejecución, aquí no es el caso:

```javascript
window
```

Lo que tenemos en Node es un proceso, al que podemos hacer referencia con:

```javascript
process
```

Este proceso es un objeto con mucha informacion sobra la ejecución y lo podemos consultar desde nuestros programas:

```javascript
process.pid
process.env
```

De hecho también contiene un método para salir del intérprete:

```javascript
process.exit()
```

Pero aunque el Prompt esté bien para hacer algunas pruebas no sirve para crear programas, eso se hace en scripts y hablaremos de ellos en la siguiente lección.

## Código no bloqueante

Antes de comenzar os recomiendo instalar una extensión llamada Code Runner en Visual Studio Code, con ella podéis ejecutar los scripts de Node con una simple combinación de teclas Control+Alt+N. Si decidís utilizarla activad la opción **RunInTerminal** para utilizar la terminal del sistema en lugar de la que viene en Visual Studio Code, eso os ahorrará problemas.

Dicho esto, en el curso para principiantes ya vimos que es posible pasar como argumento un fichero o script con código JavaScript a Node para ejecutar las instrucciones que contiene, hágámoslo de nuevo:

`curso-node/hola.js`
```javascript
console.log('Hola mundo');
```

Para ejecutarlo podemos hacer desde la propia terminal de VSC o con Control+Alt+N si habéis instalado Code Runner:

```bash
node hola.js
```

Como cabría esperar se muestra nuestro saludo por pantalla.

Ahora bien, ¿y si quisiéramos que se muestre el saludo 2 segundos después de  ejecutar el programa?

JavaScript cuenta con una instrucción llamada **setTimeout** que permite establecer una especie de temporizador. Recibe dos argumentos, el primero es una función callback con el código a ejecutar y el otro son los milisegundos que debe esperar antes de ejecutar el código:

```javascript
setTimeout(function(){
	console.log('Hola mundo');
}, 2000);
```

Si lo ejecutamos veremos que efectivamente se espera 2 segundos y entonces muestra el mensaje.

En otros lenguajes esto sería equivalente a poner a "dormir" el script durante unos segundos, por ejemplo en Python se hace así:

```python
import time

time.sleep(2)  # dormir 2 segundos
print('Hola mundo')
```

Ahora bien, mirad lo que ocurre si escribimos otra instrucción después del **timeout**:

```javascript
setTimeout(function(){
	console.log('Hola');
}, 2000);

console.log('mundo')
```

Lo que ocurre es que el código fuera del **timeout** se llama inmediatamente, no se bloquea la ejecución.

En cambio la misma lógica en Python sí es bloqueante, es como si se parase completamente el programa durante esos 2 segundos:

```python
import time

time.sleep(2)  # dormir 2 segundos
print('Hola')

print('mundo')
```

El bloqueo de código ocurre en la mayoría de lenguajes pero a veces se puede solventar usando hilos de ejecución paralelos, algo que normalmente requiere de conocimientos avanzados.

Pero eso no es así en Node, ya que al estar desarrollado sobre un motor pensado para el navegador, donde es sumamente importante garantizar el funcionamiento estable y continuo sin bloquear el programa, esta capacidad de ejecutar múltiples tareas a la vez viene de fábrica, y eso que Node se ejecuta en un solo hilo, ¿curioso verdad?

Sea como sea es gracias a esta capacidad de gestionar múltiples tareas que Node es tan bueno manejando servicios con la arquitectura cliente-servidor y de hecho su propio nombre "Node" indica su principal objetivo, servir de "nodo" para unir diferentes procesos en uno.

En la próxima sección veremos como funcionan los módulos, la forma de organizar el código que utiliza Node.

## El objeto global

Cuando llamamos una instrucción como **console.log()**:

`app.js`
```javascript
console.log("Hola mundo")
```

Estamos haciendo referencia a un objeto llamado **console** y a su método **log()**. Lo interesante es que este objeto es accesible desde cualquier lugar, es lo que se conoce como un objeto global porque forma parte del ámbito global de un programa en Node.

Hay muchos objetos y funciones que forman parte del ámbito global, como por ejemplo las funciones para controlar temporizadores:

```javascript
setTimeout()
clearTimeout()

setInterval()
clearInterval()
```

Un par muy interesante son también **\_\_filename** y **\_\_dirname** que almacenan el nombre del fichero y su localización:

```javascript
console.log(__filename);
console.log(__dirname);
```

Pero la verdad es que estos dos objetos no son exactamente globales sino que se mapean en los ficheros al ejecutarse, como si fueran una configuración extra. 

Sea como sea cuando utilizamos JavaScript en el navegador, estos objetos forman parte de la ventana, el objeto **window**, pero en Node no tenemos ventana, sino que como vimos tenemos un proceso:

```javascript
console.log(process);
```

Este proceso almacena la información de la ejecución, pero en él no encontraremos las definiciones globales. Éstas se encuentran específicamente en otro objeto, el objeto **global**, cuyo contenido se añade al script al ejecutarse:

```javascript
global.console.log("Hola mundo")
global.setTimeout()
```

Usando esta lógica podríamos hacer un programa estructurando el código en diferentes ficheros y enviar datos entre ellos añadiéndolos al objeto global:

`datos.js`
```javascript
global.test = "Hola mundo";
```

Para cargar el fichero **datos.js** en nuestra **app.js**, utilizaríamos la función **require** que también forma parte del ámbito global:

`app.js`
```javascript
require('./datos');

console.log(global.test);
```

Esto implica varias cosas, pero la más importante es que los datos globales se pueden volver a modificar, no están protegidos o mejor dicho, encapsulados:

`app.js`
```javascript
require('./datos');

global.test = "Adiós mundo";
console.log(global.test);
```

La verdad es que usar variables globales es una mala práctica, no sólo en Node sino en todos los lenguajes. Hacen el código más difícil de entender, depurar, testear, mantener y reutilizar. Os dejaré [un hilo en Stack Overflow](https://softwareengineering.stackexchange.com/questions/148108/) donde podéis profundizar al respecto.

Así que todo esto nos lleva a la cuestión obvia, si no debemos utilizar **global** para comunicar las definiciones entre ficheros, ¿cómo lo hacemos? Pues con los módulos.

## Los módulos

La modularización es un concepto que se basa en crear pequeños bloques donde definimos nuestras variables y funciones.

Node se basa en este concepto para organizar su código, de manera que cada fichero se considera un módulo en sí mismo cuyo ámbito es el propio fichero. Es decir, las definiciones que contiene están aisladas de los demás ficheros.

Mirad:

`app.js`
```javascript
console.log(module);
```

Este objeto **module** tiene varias propiedades, como su identificador único, padres, hijos, el path, etc. Pero no os preocupéis por estos campos, la clave que debéis entender aquí es que el objeto **module** existe dentro del fichero y contiene la información para que éste pueda interactuar con otros módulos.

Así pues el contenido de cada módulo es privado por defecto y la única forma de acceder desde otro módulo es exportándolo para hacerlo público.

Veremos cómo hacerlo en las siguientes lecciones.

## Creando un módulo

Vamos a crear un módulo muy simple con una función que salude a un nombre que le enviamos:

`messages.js`
```javascript
function hello(name) {
	console.log("Hola " + name);
}
```

Por defecto la función **hello** es privada, tenemos que exportarla para que sea accesible desde otros módulos. Lo haremos así:

```javascript
module.exports.hello = hello;
```

Con esto tenemos el módulo listo.

## Utilizando un módulo

Para utilizar la función **hello** en nuestra aplicación tenemos que cargar el módulo con el **require** y almacenarlo en algún lugar, normalmente una constante con el mismo nombre y desde ella hacer uso de sus funciones:

`app.js`
```javascript
const messages = require('./messages');

messages.hello("Héctor")
```

Sin embargo normalmente un módulo contendrá más de una definición:

`messages.js`
```javascript
function hello(name) {
    console.log("Hola " + name);
}

function bye(name) {
    console.log("Adiós " + name);
}

var number = 12345;
```

Para poder utilizarlas también tendremos que añadirlas al export:

```javascript
module.exports.hello = hello;
module.exports.bye = bye;
module.exports.number = number;
```

Y las utilizaremos de la misma forma:

`app.js`
```javascript
const messages = require('./messages');

messages.hello("Héctor");
messages.bye("Héctor");
console.log(messages.number);
```

¿Entonces tenemos que exportar todas las definiciones por separado? Así es, pero podemos hacer un truco para ahorrarnos un poco de código.

## Exportación simplificada

Si queremos exportar todo el contenido de una vez podemos definir el contenido del módulo como un objeto:

`messages.js`
```javascript
module.exports = {
	number: number,
	hello: hello,
	bye: bye,
};
```

Es lo mismo pero por lo menos hemos reducido algo de código.

## Importación selectiva

Por último algo que debéis de haber notado es que al cargar un módulo estamos importando todas sus definiciones, esto no es muy interesante, sobretodo si tenemos módulos con muchas definiciones. Para solventarlo podemos requerir explícitamente las definciones que queremos.

La sintaxis para hacerlo sería la siguiente:

`app.js`
```javascript
const { hello, bye, number} = require('./lib');
```

La contraparte es que ya no tenemos un objeto con el módulo completo, sino cada definición lista para usarla:

```javascript
const { hello, bye, number} = require('./messages');

hello("Héctor")
bye("Héctor")
console.log(number)
```

Creo que con esto ya sabéis suficiente sobre cómo crear vuestros propios módulos. En la siguiente sección veremos algunos de los que vienen integrados en el núcleo de Node.

## Documentación

Como vengo comentando Node incluye un montón de módulos en su núcleo que podemos utilizar para desarrollar diferentes tipos de aplicaciones.

Si vamos al apartado de documentación de la [web oficial](https://nodejs.org/) para la versión LTS encontraremos una lista con todos los objetos y módulos que podemos utilizar en Node.

Como veréis hay muchísimos y este es un curso básico así que trataremos sólo algunos de los más interesantes.

## Módulo Path

Vamos a empezar este breve repaso con el módulo **path**, es básico porque provee varias utilidades para trabajar con ficheros y directorios.

Tal como indican en la documentación podemos cargarlo de esta forma con el require:

`app_path.js`
```javascript
const path = require('path');
```

Fijaros que al cargar un módulo interno no especificamos con un punto y una barra la localización específica sino directamente con su nombre.

Así que tenemos un objeto constante con el módulo **path** que incluye un puñado de métodos interesantes para trabajar con rutas.

Uno de esos métodos extremadamente útil es **parse()**. 

¿Recordáis que teníamos un objeto global llamado \_\_filename?

```javascript
console.log(__filename);
```

Este contiene la ruta exacta del fichero dentro del disco duro.

Pues lo que hace **parse()** es extraer toda la información de una ruta y la almacena en un objeto bien organizado, fijaros:

```javascript
var pathObj = path.parse(__filename);

console.log(pathObj);
```

Hemos transformado una simple cadena con una ruta al script actual en un objeto que contiene la raíz, el directorio contenedor, el nombre base del fichero, su extensión y su nombre simple, todo de forma automática. Consultar una de las propiedades sería tan fácil como referirnos a ella:

```javascript
console.log(pathObj.base);
```

Os animo a estudiar los ejemplos de la documentación, ya que es la mejor forma de aprender y descubrir las utilidades disponibles.

## Módulo OS

Otro módulo muy interesante es **OS** centrado en proporcionar información del sistema operativo:

`app_os.js`
```javascript
const os = require('os');
```

Algunos métodos que podemos consultar:

```javascript
console.log("Nombre de la máquina -> " + os.hostname());
console.log("Arquitectura -> " + os.arch());
console.log("Plataforma -> " + os.platform());
console.log("Memoria total (Bytes) -> " + os.totalmem());
```

Así conseguiremos la cantidad de bytes, si queremos saber los mega bytes deberíamos dividir dos veces entre 1024:

```javascript
let megaBytes = os.totalmem() / 1024 / 1024;
console.log("Memoria total (Mega Bytes) -> " + megaBytes);
```

Para redondear el decimal podemos usar el método **toFixed** de los números indicando cero decimales:

```javascript
let megabytes = Number(os.totalmem() / 1024 / 1024).toFixed(0);  // Number no requerido
console.log("Memoria total (Mega Bytes) -> " + megaBytes);
```

Por cierto, desde ECMA Script 6 se pueden usar los template strings para introducir variables en las cadenas, es mucho más fácil que ir escribiendo comillas dobles todo el rato:

```javascript
console.log(`Memoria total (Mega Bytes) -> ${megaBytes}`);
```

Vosotros mismos experimentad con los demás métodos del módulo para aprender más.

## Módulo File System

En esta lección os voy a enseñar cómo trabajar con ficheros en Node utilizando el módulo File System.

En este módulo tenemos un montón de métodos para manejar ficheros y directorios, vamos a ver los más esenciales para empezar a trabajar, luego cada uno puede profundizar más por su cuenta dependiendo de lo que desee hacer.
 
`app_fs.js`
```javascript
const fs = require('fs');
```

Lo primero que notaréis es que los métodos de este módulo se presentan en dos formas, la normal y otra con un Sync al final. Eso es porque están disponibles de forma no bloqueante por defecto (asíncrona) o bloqueante (síncrona). 

¿Recordáis la función **setTimeout**? Pues con los métodos asíncronos pasa lo mismo, se ejecutan sin bloquear el resto del programa.

Esto es importante porque normalmente estas tareas suelen ser bloqueantes debido a que, aunque sepas cuándo abres el fichero, no sabes cuanto se tardará  en leer o escribir su contenido, depende de varios factores, como la rapidez de la memoria o el propio tamaño del fichero. Al hacerlo de forma asíncrona no tenemos este problema y todo se sigue ejecutando independientemente de cuanto tarden en manipularse los ficheros, es un escenario ideal.

¿Y entonces porqué se incluyen las formas síncronas? Pues por conveniencia, porque quizá en algunos escenarios sí es conveniente detener la ejecución, pero creedme que no es lo normal.

Aún así vamos a realizar un ejemplo de código que lea el contenido de un directorio de ambas formas para que entendáis la diferencia con la práctica.

Para leer el contenido de un directorio, es decir los ficheros que hay dentro se utiliza el método **readdir**, éste devuelve un arreglo con los ficheros.

Hagámoslo primero de forma bloqueante:

```javascript
const files = fs.readdirSync('./');
console.log(files);

console.log("Fin del progama")
```

Como véis obtenemos el arreglo con los ficheros. Si quiséramos recorrerlos uno a uno podríamos usar el método **forEach** de las colecciones tal como expliqué en el curso del conversor de divisas:

```javascript
const files = fs.readdirSync('./');
files.forEach(file => {
    console.log(file);
});
```

Ahora vamos a la versión asíncrona, su peculiaridad es que su resultado se devuelve a una función callback de retorno que se llamará cuando se haya ejecutado el método, exactamente igual como funciona el **setTimeout** pero sin el temporizador, con la diferencia que la función requiere un parámetro para almacenar posibles errores si no se lee bien el directorio, y otro con los ficheros encontrados:

```javascript
// const files = fs.readdirSync('./');

fs.readdir('./', function (err, files) {
	files.forEach(file => {
	    console.log(file);
	});
});
```

Si lo ejecutamos devolverá el mismo resultado, pero lo interesante es que veremos el mensaje **Fin del programa** antes de que se lea el contenido del directorio. 

Una mejor implementación de este código haciendo uso del error sería uso de una condición **if** (sí en español) para comprobar si **err** tiene algún valor y en caso contrario, si todo está correcto, usar la contra condición **else** (sino en español) y mostrar los ficheros:

```javascript
fs.readdir('./', function (err, files) {
	if (err) {
		console.log("Ocurrió un error", err);
	} else {
		files.forEach(file => {
		    console.log(file);
		});
	}
});
```

Si provocamos manualmente un fallo, por ejemplo poniendo un directorio que no existe, veremos como nos muestra el fallo que ha ocurrido.

Sea como sea con este ejemplo seguro que os queda un poco más clara la diferencia entre código bloqueante y código no bloqueante que hemos venido comentando desde el principio del curso.

Os recomiendo echar un vistazo a los métodos **readFile** y **writeFile** para leer y escribir ficheros, mirad los ejemplos de la documentación y no tengáis miedo de experimentar.

## Módulo Http

Los módulos que hemos visto hasta ahora son utilidades, pero el último que vamos a ver es más especial porque está pensado para crear servicios web backend.

Este módulo es cosa fina y para entender bien como funciona os sugiero estudiar antes el protocolo Http en relación a la gestión de las peticiones, los mensajes, las cabeceras y sus respuestas. Os voy a dejar [un enlace a la wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto#Descripci%C3%B3n) donde se explica en detalle su funcionamiento.

Pero a lo que vamos, ¿qué es un servicio? Un servicio es un programa que está en marcha permentemente esperando para responder diferentes peticiones de clientes a través de la red informática, también se les llama servidores.

`app_http.js`
```javascript
const http = require('http');
```

El módulo **http** incluye un método para crear un servidor http que escucha las peticiones que le llegan desde un puerto de la red del sistema y responde con contenido HTML a esas peticiones, es decir, responde con páginas web que el cliente puede visualizar.

Para crear nuestro servidor lo haremos así:

```javascript
const server = http.createServer();
```

En este punto tenemos todo lo necesario en el objeto server, pero no lo tenemos escuchando todavía las peticiones, debemos indicarle que empiece a escuchar peticiones en algún puerto libre:

```javascript
const server = http.createServer();
server.listen(3000);

console.log("Servidor HTTP iniciado");
console.log("Escuchando el puerto 3000")
```

Ya tenemos nuestro servidor web escuchando el puerto 3000, pero sólo escucha, todavía no procesa ninguna petición. 

Vamos a hacer algo interesante, programar un evento. Los eventos son momentos que ocurren en los servicios y podemos detectarlos. Un momento importante es por ejemplo cuando se conecta un cliente al servidor. 

Para definir un evento se utiliza el método **on** y el nombre del evento que queremos programar, en nuestro caso será **connection**. 

Como en todas las tareas asíncronas, ésta llamará una función callback cuando se conecte un cliente, y en este caso le pasará un objeto de tipo **socket** que contiene información sobre la conexión activa entre el servidor y el cliente conectado:

```javascript
const server = http.createServer();

server.on('connection', function(socket) {
	console.log("Nueva conexión en el puerto 3000");
	console.log(socket);
});

server.listen(3000);
```

Si ponemos en marcha el servidor y hacemos una petición al puerto 3000, veremos que nos muestra por pantalla que ha ocurrido el evento. Una forma rápida de hacerlo es desde el navegador, o también podemos usar la herramienta **curl** que tienen todos los sitemas operativos, dividiendo cómodamente la terminal en dos:

```bash
curl 127.0.0.1:3000
``` 

Sin embargo la gracia de un servicio web no es manejar los sockets, eso es algo que se hace en una capa inferior. El objetivo de los servicios web es manejar las peticiones a diferentes URL del servidor y responderles contenido HTML.

Veremos cómo hacerlo en la siguiente lección.

## Peticiones y respuestas

Para poder manejar peticiones y respuestas, el método **createServer** permite definir una función callback que nos provee de dos objetos, uno llamado **request** (petición) y otro **response** (respuesta):

```javascript
const server = http.createServer(function(request, response){
	console.log(`Petición a la URL -> ${request.url}`);
});

server.listen(3000);
```

Fijaros qué ocurre si hacemos ahora diferentes peticiones con curl:

```bash
curl 127.0.0.1:3000
curl 127.0.0.1:3000/blog
``` 

El registro del servidor nos muestra esas peticiones:

```
Servidor HTTP iniciado
Escuchando el puerto 3000
Petición a la URL /
Petición a la URL /blog
```

¿Véis por donde van los tiros?

El problema es que estas conexiones siguen en marcha, por eso curl sigue funcionando hasta que finaliza automáticamente al cabo de un rato. Para cerrar la respuesta debemos llamar a su método **end**:

```javascript
const server = http.createServer(function(request, response){
	console.log(`Petición a la URL -> ${request.url}`);
	request.end();
});

server.listen(3000);
```

En este punto sólo nos falta hacer una cosa, identificar las diferentes URL que el cliente necesita y responderle un contenido diferente en cada caso.

Usando el condicional **if** podemos hacerlo de forma bastante rudimentaria:

```javascript
const server = http.createServer(function(request, response){
	console.log(`Petición a la URL -> ${request.url}`);
	if (request.url === "/") {
		response.write("Bienvenido a Hektor Profe");
	}
	if (request.url === "/blog") {
		response.write("Este es el blog de Hektor Profe");
	} 
	response.end();
});
```

Si volvemos a hacer las peticiones, esta vez nos devolverá los contenidos que nosotros estamos escribiendo en las respuestas:

```bash
curl 127.0.0.1:3000
curl 127.0.0.1:3000/blog
``` 

Si hacemos estas peticiones a través del navegador también funcionarán:

```bash
http://127.0.0.1:3000
http://127.0.0.1:3000/blog
``` 

Y si en lugar de enviar texto plano enviamos etiquetas HTML tendremos hecha toda la magia:

```javascript
const server = http.createServer(function (request, response) {
    console.log(`Petición a la URL -> ${request.url}`);
    if (request.url === "/") {
        response.write(`
            <h1>Hektor Profe</h1>
            <h3>Portada</h3>
            <p>Esto es un texto de mi portada...<p>
            <a href="/blog">Blog</a>
        `);
        response.end();
    }
    if (request.url === "/blog") {
        response.write(`
            <h1>Hektor Profe</h1>
            <h3>Blog</h3>
            <p>Esto es una noticia de mi blog...<p>
            <a href="/">Portada</a>
        `);
        response.end();
    }
});
```

¿Qué os parece? Evidentemente no es la mejor forma de programar un web backend, pero hemos conseguido un prototipo funcional de una web en muy poco tiempo.

## Simulando una API

No me quiero despedir sin antes hacer un interesante y revelador experimento. ¿Recordáis el proyecto del conversor de divisas? Pues os quiero mostrar como crear un prototipo muy muy sencillo simulando una API JSON de ese estilo usando lo que sabemos del módulo http.

Podríamos usar la siguiente base:

`app_api.js`
```javascript
const http = require('http');

const server = http.createServer(function (request, response) {
    if (request.url === "/api/divisas") {
    	// Supondremos que tenemos los datos de un fichero o base de datos
        response.end();
    }
});

server.listen(3000);
```

Vamos a tomar los valores tal cual los devuelve la API de *exchangeratesapi* [en este enlace](https://api.exchangeratesapi.io/latest?symbols=USD,GBP,JPY).

```javascript
let values = {
	"base":"EUR",
	"rates": {
		"USD":1.1199,
		"JPY":124.13,
		"GBP":0.8547
	}
}

response.end();
```

Ahora vamos a escribir el resultado en la respuesta, pero necesitamos transformar este objeto a formato JSON que es el que utilizan las API. 

Pues hacer esto es tan fácil como usar la librería JSON de JavaScript y su método stringify de la siguiente forma:

```javascript
let values = {
	"base":"EUR",
	"rates": {
		"USD":1.1199,
		"JPY":124.13,
		"GBP":0.8547
	}
}

response.write(JSON.stringify(values));
response.end();
```

Con esto podemos hacer la petición a la url **/api/divisas** y tendremos exactamente lo mismo que nos ofrece la API real:

```bash
http://127.0.0.1:3000/api/divisas
``` 

Claro, esto es sólo una simulación y los datos están escritos en crudo. La gracia del programa sería tener una base de datos actualizada y tomar la información para usarla en la API.

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>