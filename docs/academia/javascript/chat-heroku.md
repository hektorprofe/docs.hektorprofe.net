title: Chat online y despliegue en Heroku | JavaScript | Academia | Hektor Profe
description: Desarrolla paso a paso tu propio chat online; el servidor con Node.js, el cliente con jQuery y el despliegue en internet gratis con Heroku.

# Chat online y despliegue en Heroku

## Preparando el servidor

Vamos a empezar con este proyecto creando por ejemplo una carpeta **Chat-Node**, no le pongáis espacios ni caracteres especiales porque la vamos a iniciar como proyecto con Node, separad los espacios con guiones si lo necesitáis.

Dentro iniciamos un proyecto para trabajar con dependencias, todo por defecto excepto el main que podemos llamar **server.js**:

```javascript
npm init
```

Para este proyecto vamos a empezar a utilizar el módulo Express, así podremos servir los ficheros estáticos del frontend junto al backend fácilmente. Podemos instalarlo en un momento haciendo:

```javascript
npm install -s express
```

Ahora en nuestro **server.js** creamos iniciamos nuestro servidor HTTP con express:

`server.js`
```javascript
var express = require("express")
var app = express()

var server = app.listen(3000, () => {
  console.log("Servidor listo en http://127.0.0.1:3000")
})
```

En este punto os recomiendo instalar Nodemon, es un pequeño demonio que reiniciará automáticamente nuestro servicio de Node al detectar un cambio:

```javascript
npm install -g nodemon
```

Ahora para poner en marcha el servidor lo haremos con:

```javascript
nodemon server.js
```

Si guardáis el fichero **server.js** veréis que el servidor se reinicia automáticamente.

¿Muy práctico verdad?

## Preparando el cliente

Vamos a diseñar una página HTML para manejar el cliente web del chat, podemos usar bootstrap para ir rápido. Os voy a dejar el código en los apuntes ya con todo preparado, si tenéis alguna duda sobre el funcionamiento me lo decís en los comentarios de la lección.

Podemos crearlo en una carpeta llamada **public** haciendo referencia a los ficheros estáticos públicos:

`public/index.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
    body { 
      margin: 15px; font-family: sans-serif }
    h3 {
      padding: 0; margin: 0; margin-bottom: 1rem;}
    #chat { 
      background: rgb(245, 245, 245); height: 200px; width: calc(100% - 20px); 
      max-width:620px; border: 1px solid gray; margin-bottom: 10px; 
      padding: 10px; overflow-y: auto; overflow-y: scroll;}
    #controls { 
      display: grid; width: calc(100%); max-width:642px; 
      grid-template-columns: 25% 55% 20%; }
    #controls input { 
      padding: 8px 5px; }
    </style>
  </head>
  <body>
    <div id="chat"></div>
      <form autocomplete="off">
        <div id="controls">
          <input type="text" id="username" placeholder="Usuario" />
          <input type="text" id="content" placeholder="Mensaje" />
          <input type="submit" value="Enviar" />
        </div>
      </form>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
  </body>
</html>
```

Bien, con esto ya lo tenemos.

Ahora tenemos que servir los ficheros estáticos con Express, para hacerlo haremos lo siguiente en nuestro servidor:

```javascript
app.use(express.static(__dirname + '/public'))
```

Con esto ya podemos poner en marcha el servidor y si accedemos veremos como se carga la pantalla inicial de nuestro chat.

## Conexiones al servidor

Para que manejar conversaciones en tiempo real entre un servidor y sus clientes a través de la red necesitamos utilizar sockets. 

Manejar sockets suele ser una tarea bastante tediosa, pero por suerte para nosotros hay una tecnología llamada web sockets que nos facilitará mucho la vida. Para utilizarla en JavaScript podemos hacr uso de la biblioteca Socket.IO.

Tendremos que implementarla en ambos lados de nuestra aplicación, vamos a empezar por el servidor:

```javascript
npm install -s socket.io
```

Para utilizar el módulo en el servidor tendremos que iniciar un servicio http paralelo en nuestra app y cargarlo en la biblioteca **justo después de crear nuestra app**: 

`server.js`
```javascript
var http = require('http').Server(app)
var io = require('socket.io')(http)
```

Para capturar las conexiones al servidor definiremos un evento **connection** que recuperará el socket abierto entre el servidor y el cliente:

```javascript
io.on('connection', (socket) => {
  console.log('Usuario conectado', socket)
})
```

Y ahora muy importante, en lugar de poner en marcha el servidor Express directamente, usaremos el que hemos redefinido en **http** que es donde tenemos socket.io funcionando:

```javascript
var server = http.listen(3000, () => {
```

Con esto ya estamos escuchando los web sockets, pero no podemos probarlos hasta programar alguna prueba en el cliente web. 

Así que vamos a cargar la biblioteca socket.io en el frontend que se añade automáticamente como recurso del servidor:

`public/index.html`
```html
<!-- Cargamos la biblioteca de sockets que se añade automáticamente --> 
<script src="/socket.io/socket.io.js"></script> 
```

Con la biblioteca cargada el primer paso es conectar el cliente al server:

```javascript
var socket = io()
```

Si cargamos de nuevo la página HTML veremos como ya nos aparece en el servidor el mensaje de **Usuario conectado**.

## Bienvenida al cliente

Sabemos que se ha conectado un cliente, vamos a enviarle una señal de vuelta para darle la bienvenida al servidor:

`server.js`
```javascript
console.log('Usuario conectado')
socket.emit('bienvenida')
```

Ahora en el cliente vamos a detectar ese evento llamado **bienvenida** y al llamarse mostraremos la bienvenida en el chat:

`public/index.html`
```javascript
// Cuando jQuery se haya cargado
$(function() {  

  // Capturamos la señal de bienvenida y saludamos al usuario
  socket.on("bienvenida", function() {
    $("#chat")
      .empty()
      .append("<h3>Bienvenido al chat de Hektor Profe</h3>")
  })

})
```

¡Listo!

## Mensajes al servidor

El siguiente paso es que el cliente pueda enviar mensajes al servidor. 

Para hacerlo debemos emitir un mensaje del cliente hacia el servidor, pero no vamos a emitirlo a cualquier sitio sino a un evento llamado por ejemplo **nuevo_mensaje**:

`server.js`
```javascript
socket.on('nuevo_mensaje', (message) => {
	console.log(message)
})
```

De vuelta al cliente vamos a detectar cuando se envía el formulario, recuperaremos los datos y los emitiremos al servidor en una pequeña estructura que representará un mensaje:

`public/index.html`
```javascript
// Capturamos el clic en el botón de enviar
var form = $("form").on("submit", function(e){
  // Desactivamos el formulario para enviarlo con JS
  e.preventDefault() 
  // Creamos un objeto con el mensaje
  var message = {
    name: $("#username").val(), 
    content: $("#content").val()
  }
  // Lo emitimos
  socket.emit("nuevo_mensaje", message)
})
```

Si enviamos un mensaje veréis que aparece en el servidor el objeto que lo contiene.

## Difundiendo el mensaje

Nuestro servidor ya recibe los mensajes, ahora tenemos que difundirlos a los clientes conectados para mostrarlos en el chat, esto es lo que se conoce como hacer un "broadcast" del mensaje.

Para hacer una difusión global lo haremos a nivel del servidor y no del socket del cliente con un evento que podemos llamar **difundir_mensaje**:

`server.js`
```javascript
socket.on('nuevo_mensaje', (message) => {
  // Dinfundimos el mensaje a todos los clientes
  io.sockets.emit('difundir_mensaje', message)
})
```

Ahora tenemos que capturar este evento en el cliente, recuperar el objeto message recibido y mostrarlo:

`public/index.html`
```javascript
// Recuperamos el mensaje y lo añadimos al HTML
socket.on('difundir_mensaje', function(message) {
  $("#chat")
    .append(`
      <b>${message.name}</b>
      ${message.content}<br>`)
})
```

¡Listo! Por increíble que parezca con esto tenemos un protitpo completamente funcional, probad a abrir varias ventanas y hablar con diferentes nombres.

Sin embargo no quiero dejar el chat como está, creo que es una buena oportunidad para analizar algunos problemas que existen a niel de cliente y solucionarlos.

## Puliendo el cliente

En esta lección vamos analizar y solucionar algunos problemas importantes que tiene el cliente web de nuestro chat.

El primer problema que salta a la vista es que no tenemos un sistema de autenticación, así que cualquier puede cambiar su nombre para hacerse pasar por otra persona.

Arreglar esto de forma óptima conllevaría manejar una base de datos o fichero de registros, con usuario y contraseñas encriptadas. Es demasiado trabajo para un curso de nivel intermedio, así que vamos a simplemente a bloquear el campo de nombre para que no se pueda editar una vez envías el primer mensaje:

`public/index.html`
```javascript
socket.emit("nuevo_mensaje", message)        // Lo emitimos
$("#username").attr("disabled","disabled")  // Desactivamos el nombre
```

Algo más que podemos hacer inmediatamente después de enviar el mensaje es borrar el mensaje para que el usuario tenga que escribirlo uno nuevo y no pueda "spamear" el mismo todo el rato:

```javascript
$("#content").val("").focus()  // Borramos el mensaje y lo seleccionamos
```

Ahora, creo que sería importante validar el usuario y el mensaje para que por lo menos ambos tengan un caracter de longitud, así evitaremos que se envíen mensajes vacíos o nombres vacíos:

```javascript
// Lo emitimos al servidor si cumple las condiciones
if (message.name.length > 0 && message.content.length > 0) {
  socket.emit("nuevo_mensaje", message)  // Lo emitimos
  $("#username").attr("disabled","disabled") // Desactivamos el nombre
  $("#content").val("").focus()  // Borramos el mensaje y lo seleccionamos
}
```

Sin embargo esto no funcionará si alguien introduce un espacio porque lo tomaré como un carácter invisible. 

Para solucionar esta situación podemos hacer utilizar el método **trim()** en los valores recuperados, eso borrará los espacios al principio y al final del nombre y el mensaje:

```javascript
// Creamos un objeto con el mensaje
var message = {
  name: $("#username").val().trim(), 
  content: $("#content").val().trim()
}
```

Vamos bien, pero seguimos teniendo un problema importantísimo. Si un usuario envía un mensaje con tag HTML, este se inyectará en el chat, probad a inyectar una alerta dentro de un tag script:

```javascript
<script>alert("Hola")</script>
```

Esto es una brecha de seguridad considerable que deja la puerta abierta a inyectar código en otros usuarios y creedme que eso es muy malo. ¿Os imagináis que alguien os carga una librería remota de JavaScript? Han habido casos en que se han inyectado librerías para minear criptomonedas de esta forma en páginas web, haciendo que todos los clientes que visitaban la web inyectada minearan para beneficio del hacker que inyectó su librería en el código. 

Por suerte podemos evitar esto de una forma muy sencilla, sólo tenemos que asegurar el contenido del mensaje transformando las flechas de los tags en caracteres. Para ello vamos a crear una función que asegure una cadena:

```javascript
// Función para prevenir inyección de tags
function special(str){ 
  // gi => Reemplazo global case-insensitive
  str = str.replace(/</gi, '&lt;') // importante usar comillas simples
  str = str.replace(/>/gi, '&gt;') // en las expresiones regulares
  return str
}
```

Y la utilizamos para asegurar los campos antes de añadirlos en el chat:

```javascript
$("#chat")
  .append(`
    <b>${special(message.name)}</b>
    ${special(message.content)}<br>`)
```

Si ahora intentamos enviar un script o cualquier tag HTML:

```javascript
<script>alert("Hola")</script>
```

Se nos muestra la cadena en crudo, así que problema resuelto y podemos dar por concluido nuestro chat online.

En la siguiente sección del curso os enseñaré a desplegar el chat en la nube usando Heroku sin coste para que podáis probar el proyecto con vuestros amigos.

## Preparando el repositorio

Heroku es una plataforma que permite desplegar y escalar servicios creados en todo tipo de lenguajes. Node.js no es una excepción y en muy pocos pasos podemos tener nuestro chat en la nube sin coste, simplemente usando el plan gratuito.

El plan gratuito es para hacer pruebas, así que no se os ocurra colgar proyectos reales para vuestro clientes porque tienen una cuota limitada. 

En cualquier caso no voy a entrar en detalles, simplemente os enseñaré los pasos para desplegar el proyecto, realizaremos un cambio y lo volveremos a desplegar.

Lo primero y fundamental es tener una cuenta en Heroku, os podéis registrar en [www.heroku.com](https://www.heroku.com/) donde pone Signup.

Una vez creada instalamos el cliente de Heroku en Node, es muy fácil pero tardará un ratito, así que paciencia:

```bash
npm install -g heroku
```

Ahora, antes de desplegar un proyecto en Heroku es necesario hacer algunas preparaciones.

La primera es crear un fichero llamado **Procfile**, éste contendrá el tipo de proceso que deseamos iniciar y el comando que iniciará el servicio:

`Procfile
```
web: node server.js
```

El siguiente requisito es que el proyecto esté gestionado con el control de versiones Git, así que no tenemos remedio que instalar ese programa, os dejaré el [enlace en los apuntes](https://git-scm.com/downloads). Podéis hacer siguiente, siguiente, siguiente sin mucha complicación.

Una vez tengáis Git instalado y hayáis reiniciado Visual Studio Code podréis manejar Git desde el propio editor, sin embargo antes debemos configurar un email y un nombre de usuario en Git, eso lo podemos haciendo **clic derecho en la carpeta de nuestro proyecto** y **Git Bash Here**.

En la nueva terminal de Git vamos a configurar sólo una primera vez nuestra información de autoría:

```bash
git config --global user.email "hola@hektor.dev"
git config --global user.name "Héctor Costa"
```

Acto seguido iniciaremos el repositorio escribiendo lo siguiente estando en el directorio del proyecto:

```bash
git init
```

Cuando lo tengamos procederemos a identificarnos en Heroku para crear el proyecto remoto y poder desplegarlo:

```bash
heroku login
```

Os pedirá abrir el navegador para identificaros en la web, una vez hecho creamos el proyecto en heroku:

```bash
heroku create
```

A parte de crearlo se abrá añadido la configuración remota para el despliegue, lo sabréis porque aparecerá una URL y un repositorio de Git almacenado en Heroku.

Con esto ya estamos listos para volver a Visual Studio Code y continuar desde allí, sin embargo **es importante que reiniciéis el editor** para que se detecte Git y podáis usarlo cómodamente antes de continuar.

## Realizando el despliegue

Al abrir de nuevo el proyecto veréis que se activa la tercera opción para "Controlar código fuente" y se añaden tropocientosmil ficheros al repositorio, eso es porque las dependendencias de Node almacenadas en la carpeta **node_modules** también se han añadido. No queremos eso, vamos a crear un fichero **.gitignore** para decirle que la ignore:

`.gitignore`
```
node_modules/
```

Veréis como el directorio se pone gris, eso es que ya lo está ignorando.

Ahora desde el propio editor, en la parte superior vamos a añadir un mensaje explicando los cambios, esto que se conoce como un hacer un "Commit", cuando lo tengamos confirmamos en el botón de arriba.

Finalmente hacemos clic en los tres puntitos y seleccionamos la opción **Publicar en rama**.

Como solo tenemos el la rama maestro en Heroku configurada se publicarán ahí los cambios directamente, si tuviéramos más ramas nos pediría seleccionar una específica.

Podemos intentar acceder a la URL del proyecto y en su puerto 3000 a ver si funciona:

```
https://intense-ocean-94826.herokuapp.com:3000 
```

Al publicar estos cambios automáticamente se realizará el despliegue, pero lamentabelmente esto no funcionará a la primera.

Podemos consultar un registro del servidor en la terminal:

```
heroku logs -a intense-ocean-94826 -n 50
```

En este caso en particular indagando encontraremos esta línea:

```
Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
```

Básicamente nos dice que falló la asignación al puerto 3000, ¿sabéis poqué? Cuando hemos definido el **Procfile** hemos indicado que el servicio es del tipo **web**, eso le obliga a Heroku a ejecutarlo en el puerto 80. Sin embargo la solución no es tan fácil como cambiar el puerto al 80 y ya está. 

Heroku internamente asigna un puerto dinámico al servicio web y lo mapea automáticamente al 80 del servidor.

Ese puerto dinámico es el que tenemos que recuperar del proceso y asignarlo, podemos hacerlo así:

```javascript
// Asignar el puerto que Heroku maneja y si no existe el 3000 manualmente
var server = http.listen(process.env.PORT || 3000, () => {
  console.log("Servidor listo en http://127.0.0.1:" + server.address().port);
});
```

Ahora hacemos un commit, confirmamos y publicamos los cambios.

Si todo ha ido bien deberíamos ser capaces de acceder desde la URL normal, que mapea el puerto 80 automáticamente, a nuestro chat web:

```
https://intense-ocean-94826.herokuapp.com
```

Recordad que podéis consultar los registros con **heroku logs** en cualquier momento para saber si hay algún problema.

Con esto llegamos al final de este interesante proyecto, espero que el curso os haya parecido interesante y hayáis aprendido algo nuevo, os traeré más contenido sobre Node muy pronto, mientras tanto nos vemos por la academia.

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>