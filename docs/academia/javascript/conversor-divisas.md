title: Conversor de divisas vía API | JavaScript | Academia | Hektor Profe
description: Aprende lo básico de Node, un entorno de ejecución JavaScript para el backend usado en la creación de servicios de networking.

# Conversor de divisas vía API

En este curso aprenderéis de forma práctica cómo crear una pequeña aplicación web para saber el valor de diferentes divisas.

Si no tenéis mucha experiencia en desarrollo web este proyecto es una forma excelente de practicar, ya que maquetaremos la interfaz de forma muy simple con HTML y CSS para luego añadir la capa de JavaScript que manejará las funcionalidades interactivas.

La guinda del pastel será realizar una petición a una API online para extraer la información de las divisas e introducirlas en la aplicación haciendo uso de la función fetch.

## Diseñando el conversor

* Creamos un directorio para el proyecto **Conversor**.
* Creamos un fichero **index.html**.
* Autocompletamos con ! + tab y abrimos en **Live Server**.
* Cambiamos el title del HTML a **Conversor de divisas**.
* Añadimos la estructura base al body:

`index.html`
```html
<div>
  <div>Euros</div>
  <input type="number" value="1" /> 
</div>
<div>
  <div>Dólares</div>
  <input type="number" value="1" />  
</div>
<div>
  <div>Libras</div>
  <input type="number" value="1" /> 
</div>
<div>
  <div>Yenes</div>
  <input type="number" value="1" />  
</div>
```

## Añadiendo estilos CSS

* Creamos los estilos mientras añadimos los identificadores:

`index.html`
```html
<div class="divisa">
  <div class="nombre">Euros</div>
  <input class="valor" type="number" value="1" />
</div>

<div class="divisa">
  <div class="nombre">Dólares</div>
  <input class="valor" type="number" value="1" />
</div>

<div class="divisa">
  <div class="nombre">Libras</div>
  <input class="valor" type="number" value="1" />
</div>

<div class="divisa">
  <div class="nombre">Yenes</div>
  <input class="valor" type="number" value="1" /> 
</div>
```

Y para la css dentro de un nuevo tag **style** antes de cerrar la cabecera **head**:

```css
body {
  font-family: sans-serif;
  max-width: 280px;
  margin: 25px auto;
}

.divisa {
  display: grid;                    /* cuadrícula */
  grid-template-columns: 50% 50%;   /* 2 columnas iguales */
  margin-bottom: 15px;
  background: rgb(37, 169, 209); 
  color: white;
}

.nombre, .valor{
  padding: 5px;
  font-size: 16px;
  align-self: center;  /* alinear elemento al centro en altura */
  text-align: center;  /* alinear texto al centro en ancho */
}
```

* Luego trasladamos los estilos a un fichero **styles.css** separado y lo importamos en la cabecera:

```html
<link rel="stylesheet" href="styles.css" type="text/css">
```

## Accediendo a los inputs

* Comprobaremos [este enlace a la API](https://api.exchangeratesapi.io/latest?symbols=USD,GBP,JPY) con el valor actual de diferentes divisas respecto al euro.

* Crearemos un campo dataset en cada input con el valor al cambio con el nombre que queramos:

`index.html`
```html
<input class="valor" type="number" data-cambio="1"/>
<input class="valor" type="number" data-cambio="1.125"/>
<input class="valor" type="number" data-cambio="125.86"/> 
<input class="valor" type="number" data-cambio="0.8647"/> 
```

* Crearemos un script para establecer los valores iniciales de los inputs usando el método **forEach** que tienen los arrays en JavaScript:

`scripts.js`
```javascript
let inputs = document.querySelectorAll(".valor");
inputs.forEach(function mostrarValor(input) {
  console.log(input.value);           // mostramos el valor
  console.log(input.dataset.cambio);  // mostramos el cambio
});
```

* La función puede ser anónima, sin tener nombre:

```javascript
inputs.forEach(function (input) {
```

* Incluso se puede simplificar a una función flecha:

```javascript
inputs.forEach((input) => {
```

* Como vemos nos sobra un paréntesis:

```javascript
inputs.forEach(input => {
```

* Finalmente trasladamos el código JavaScript a un fichero **scripts.js** separado y lo cargamos justo antes de cerrar el body:

```html
<script src="scripts.js" type="text/javascript"></script>
```

## Valores iniciales

* Establecemos el valor inicial de cada input en su valor de cambio:

`scripts.js`
```javascript
inputs.forEach(input => {
  input.value = input.dataset.cambio;
});
```

* En este punto veremos que en Chrome solo podemos subir y bajar enteros, añadiremos un paso decimal a los inputs:

`index.html`
```html
step="0.25"  <!-- en el yen se puede dejar igual porque no tiene décimas -->
```

* Lo siguiente que tenemos que hacer es que el programa detecto cuando cambiamos uno de los inputs y calcule el cambio para los demás inputs.

## Capturando un evento

* Para detectar cuando cambia el valor de un input tendremos que configurar su  evento **onChange**. La forma fácil es añadirlo al input:

`index.html`
```html
<input 
  class="valor" type="number" value="1" data-cambio="1" 
  step="0.25" onChange="valorCambiado(this)" />
```

`scripts.js`
```javascript
function valorModificado(input) {
  console.log(input.value)
}
```

* Lo añadiremos a todos los inputs.

## Factor de conversión

* Nuestro siguiente reto es recalcular los demás campos cuando uno cambia, ¿cómo podemos hacerlo?

* La clave está en calcular un factor de conversión usando una regla de tres y lo haremos diviendo el valor original de cambio por el valor actual establecido. Como resultado obtendremos el factor o tanto por uno (es decir un porcentaje de 0 a 1) para multiplicar en los demás campos.

`scripts.js`
```javascript
console.log(input.value / input.dataset.cambio);
```

* Para realizar los cálculos en los inputs tendremos que volver a recorrerlos y establecer sus valores:

```javascript
function valorCambiado(input) {
  let factor = input.value / input.dataset.cambio;
  inputs.forEach(input => {
    input.value = input.dataset.cambio * factor;
  })
}
```

* Con esto ya tenemos el conversor funcionando, auque os quiero comentar algo que debemos evitar y eso es repetir variables como nombres de parámetros. Aunque en nuestro caso no ha pasado nada, podría darse la situación en que os surjan problemas, así que os recomiendo que en lugar de usar el nombre input dentro de la función valorCambiado, pongáis otro, por ejemplo "campo", ya que esos representan todos los diferentes "campos" y no sólo el que ha cambiado:

```javascript
function valorCambiado(input) {
  let factor = input.value / input.dataset.cambio;
  inputs.forEach(campo => {
    campo.value = (campo.dataset.cambio * factor).toFixed(2);
  })
}
```

* Ya sólo nos falta hacer que los valores de cambio se tomen de la API automáticamente, pero antes dejadme mostraros como redondear con JavaScript nuestro resultado a dos decimales:

```javascript
campo.value = (campo.dataset.cambio * factor).toFixed(2);
```

* Por cierto, está divertido usar la tecla arriba y abajo en los campos para ver como se van actualizando nuestras conversiones.

## Peticiones con fetch()

Nuestra última tarea en este proyecto es recopilar los valores de cambio de las divisas en tiempo real a través del enlace a la API del servicio Exange Rates.

JavaScript integra una función llamada **fetch()** que permite realizar peticiones web como si fuéramos nosotros y capturar la respuesta para manipular los datos resultantes.

La estructura básica de una petición con fetch es siempre la misma, por lo que no es necesario memorizarla, basta con entender qué hace.

Vamos a hacer nuestra petición al cargar el script:

`scripts.js`
```javascript
let url = 'https://api.exchangeratesapi.io/latest?symbols=USD,GBP,JPY';

fetch(url)
.then(function (response) { 
  return response.json()
}) 
.then(function (data) { 
  console.log(data);
})
.catch(function (error) { 
  console.error(error); 
})
```

La lógica siempre es:

* Realizar la petición.
* Esperar a tener la respuesta y transformarla a datos manipulables.
* Esperar a tener los datos manipulables listos para hacerlos servir.
* Capturar los posibles fallos en la petición.

Lo bueno que tiene **fetch()** es que funciona con promesas, un tipo de código que se ejecuta asíncronamente sin bloquear el renderizado de nuestras páginas.

Pero bueno, sea como sea con esto deberíamos ver una estructura de objetos en la consola con los datos devueltos o un error si falla la petición.

## Simplificando fetch()

Antes de continuar vamos a hacer un inciso para transformar la petición **fetch** a funciones flecha para simplicar el código, ya que generalmente se deja todo más simple.

Primero borremos las funciones:

`scripts.js`
```javascript
fetch(url)
.then(response => { 
  return response.json()
})
.then(data => { 
  console.log(data);
})
.catch(error => { 
  console.error(error); 
})
```

Ahora, algo muy interesante que se puede hacer con las funciones flecha es devolver un resultado directo sin necesidad de abrir un bloque, fijaros:

```javascript
fetch(url)
.then(response => 
  response.json()
)
```

Como lo que se devuelve es una sola instrucción implícita, podemos incluso no devolver nada y mostrar algo directamente por pantalla:

```javascript
.then(data => 
  console.log(data)
)
.catch(error => 
  console.error(error)
)
```

Este código tan simple que hemos conseguido suele escribirse en tres líneas substituyendo la variable response por una r:

```javascript
let url = 'https://api.exchangeratesapi.io/latest?symbols=USD,GBP,JPY';
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.error(error))
```

Esta es la forma más simplificada posible de **fetch()**, pero tened en cuenta que en el momento que necesitemos más de una instrucción en las funciones flecha tendremos que crear un bloque con llaves obligatoriamente.

## Accediendo a los datos

Muy bien tenemos los valores de la API listos para manipularlos en datos JSON. JSON es el acrónimo de **JavaScript Object Notation**, así que en realidad lo que tenemos son objetos con sus propiedades que podemos consultar de la forma como os enseñé en mi curso de JavaScript para principiantes.

`scripts.js`
```javascript
.then(data => {
  console.log(data.rates);
})
```

En un nivel más de profundidad tenemos los datos que necesitamos:

```javascript
.then(data => {
  console.log(data.rates.GBP);
  console.log(data.rates.USD);
  console.log(data.rates.JPY);
})
```

Ahora tenemos que tirar de nuestro ingenio e idear una forma de establecer los valores en los campos... ¿Cómo podríamos hacerlo?

¿Cada divisa tiene un código en mayúsculas verdad? USD, GBP, JPY

Este código podría servirnos para usarlo de referencia a la hora de establecer los valores de cambio, pero necesitamos añadirlo a cada input. Podemos hacerlo por ejemlo asignando un atributo **id**:

`index.html`
```html
data-clave="USD"
data-clave="GBP"
data-clave="JPY"
```

En el caso del euro no lo necesitamos porque siempre se toma como base 1 euro al hacer las conversiones. 

Ahora simplemente tenemos que hacer referencia a los inputs a partir de esa id y asignarles su nuevo valor de cambio:

`scripts.js`
```javascript
.then(data => {
  document.querySelector('#USD')
    .dataset.cambio = data.rates.USD;
  document.querySelector('#GBP')
    .dataset.cambio = data.rates.GBP;  
  document.querySelector('#JPY')
    .dataset.cambio = data.rates.JPY;
})
```

Después de hacer este ajuste veremos que todo parece funcionar perfectamente, pero hay un problema. ¿Recordáis que os comenté que **fetch** funciona con promesas asíncronas? Eso signica que sabemos cuando realizamos la petición y confiamos en la promesa de que se procese la información al recibirse la respuesta, pero de mientras el proceso queda en un limbo temporal. 

Ese tiempo es suficiente para que nuestra web muestre los valores de cambio que tenemos establecidos manualmente en los inputs en lugar de los que se cargan de la API.

Lo solucionaremos en la próxima y última lección.

## El detalle final

Para evitar el problema inherente de usar las promesas tendremos que establecer los valores de cambio en los inputs justo después de recibirlos dentro del **fetch()**:

`scripts.js`
```javascript
// Nos llevamos esto arriba del todo para reutiliarlo
let inputs = document.querySelectorAll(".valor");

let url = 'https://api.exchangeratesapi.io/latest?symbols=USD,GBP,JPY';
fetch(url)
  .then(r => r.json())
  .then(data => {
    document.querySelector('#USD')
      .dataset.cambio = data.rates.USD;
    document.querySelector('#GBP')
      .dataset.cambio = data.rates.GBP;  
    document.querySelector('#JPY')
      .dataset.cambio = data.rates.JPY;

    // Recorremos y establecemos los valores aquí en lugar de abajo
    inputs.forEach(input => {
      input.value = input.dataset.cambio;
    });
  })
  .catch(error => console.error(error))
```

Con esto podemos borrar el dataset data-cambio de todos los inputs exceputando el del euro, ya que es el único que debe tener un valor manual de 1 porque no se recibe de la API.

`index.html`
```html
data-cambio="1"  <!-- dejar sólo el del euro y borrar los otros -->
```

Y así llegamos al final de este pequeño proyecto, para que veais que sin saber programar demasiado se pueden hacer cosas muy chulas.

Nos vemos en el próximo.

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>