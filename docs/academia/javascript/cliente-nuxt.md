title: Cliente en Nuxt.js para API | JavaScript | Academia | Hektor Profe
description: Desarrolla un cliente web sobre la API creada con Django para gestionar tus películas favoritas usando JavaScript y Nuxt.js.

# Cliente en Nuxt.js para API

Este curso es una continuación del <a href="/academia/django/api-rest-framework/">Proyecto API con DRF</a>, en el que utilizando un framework JavaScript llamado Nuxt.js (basado en Vue.js), os enseñaré a crear un cliente web SPA.

El cliente nos ofrecerá tanto formularios de registro como de identificación y contará con dos páginas, una para visualizar el top de películas y realizar búsquedas, y otra para gestionar sus películas favoritas, ya que éstas se podrán marcar o desmarcar fácilmente y gestionarse en la propia sección.

Por si fuera poco añadiremos también unas alertas <span style="font-weight:500">toast</span> asíncronas que quedan geniales.

## Creando nuestro proyecto

Este curso es una continuación del [Proyecto API de pelis con DRF](/curso/proyecto-api-peliculas-django-rest-framework), en el que utilizando un framework JavaScript llamado Nuxt.js (basado en Vue.js), os enseñaré a crear un cliente web SPA.

El cliente nos ofrecerá tanto formularios de registro como de identificación y contará con dos páginas, una para visualizar el top de películas y realizar búsquedas, y otra para gestionar sus películas favoritas, ya que éstas se podrán marcar o desmarcar fácilmente y gestionarse en la propia sección.

Por si fuera poco añadiremos también unas alertas <span style="font-weight:500">toast</span> asíncronas que quedan geniales.

Dicho lo cual, teniendo Node.js instalado, desde la terminal ejecutamos:

```bash
npx create-nuxt-app cli_peliculas
```

Tendremos que elegir las siguientes opciones:

* Project name: **Enter**
* Project description: **Enter**
* Author name: **Enter**
* Package manager: **npm**
* UI Framework: **Buefy**
* Custom server framework: **none**
* Nuxt.js modules: **Axios**
* Linting tools: **Enter**
* Test framework: **Enter**
* Rendering mode: **SPA**

Esto nos creará una SPA básica usando Nuxt.js y la UI de Buefy automáticamente, vamos a echarle un vistazo:

```bash
cd .\cli_pelis\
npm run dev
```

Si accedemos a la url [http://localhost:3000](http://localhost:3000) podréis ver que la SPA ya cuenta con dos páginas y un diseño adaptativo basado en Bulma pero utilizando Buefy como librería de componentes para Vue.

Podríamos borrar lo que hay y construir nuestro cliente desde cero, pero he pensado que es mejor adaptar lo que tenemos, así nos centramos en lo importante.

## Adaptando el diseño y las páginas

Ya en VSC y con nuestro proyecto en marcha vamos a modificar un poco su estructura.

Seguramente la primera pregunta que tendréis sea... ¿cómo maneja Nuxt.js las páginas?, pues muy fácil, lo hace a través de componentes en el directorio pages.

Ahí encontraremos dos: **index.vue** e **inspire.vue**. La página **index.vue**, como podéis suponer hace referencia a la raíz del sitio, mientras que inspire es una página cualquier. De hecho, dejando de banda index, el nombre que damos al componente de la página concuerda con el que debemos poner en la URL para acceder a ella. 

Con eso en mente vamos a modificar el nombre **inspire.vue** a **favoritas.vue**.

Al hacerlo dejará de funcionar, eso es porque en el menú el enlace sigue apuntando a la anterior, vamos a editarlo… ¿pero dónde se encuentra?

Si las páginas son componentes, éstas deben cargarse dentro de algún sitio, ¿no? Pues ese sitio es el layout principal. Lo encontraremos en **layouts/default.vue**, que es que se utiliza por defecto.

Como podréis observar en este fichero no encontramos las típicas cabeceras de html, head y body. Nuxt.js funciona con componentes y código JavaScript, de manera que para configurar esa parte hay que hacerlo editando el fichero de configuración **nuxt.config.js**.

Sea como sea vamos a editar el enlace del menú. Por defecto se nos ha creado dinámicamente, vamos a ponerlo manual y ya que estamos cambiaremos los iconos y lo haremos un poco más ancho:

`layouts/default.vue`
```html
<aside class="column is-3 section"> <!-- 3 en lugar de 2 y 9 por 10 -->
  <p class="menu-label is-hidden-touch">General</p>
  <ul class="menu-list">
    <li>
      <nuxt-link to="/" exact-active-class="is-active">
        <b-icon icon="video"/>
        Películas
      </nuxt-link>
    </li>
    <li>
      <nuxt-link to="/favoritas" exact-active-class="is-active">
        <b-icon icon="star"/>
        Favoritas
      </nuxt-link>
    </li>
  </ul>
</aside>
```

Aprovecharemos para cambiar también el título del proyecto:

```html
<a class="navbar-item" href="/">Super Películas</a>
```

Lo siguiente que podemos hacer es preparar el menú superior para mostrar los botones de registro y login. 

Siguiendo la estructura de un navbar en bulma, tal como indican en la [documentación](https://bulma.io/documentation/components/navbar/), vamos a añadir un par de botones a la parte derecha:

```html
<!-- Contenido del menú, al nivel del navbar-brand-->
<div class="navbar-menu">
  <div class="navbar-end">
    <div class="navbar-item">
      <div class="buttons">
        <a class="button">
          <strong>Registro</strong>
        </a>
        <a class="button is-light">
          Acceder
        </a>
      </div>
    </div>
  </div>
</div>
```

Implementar el funcionamiento del menú desplegable sería muy tedioso, pero gracias a Vue podemos implementar su funcionamiento en un santiamén. 

Para forzar que se muestre el menú superior al presionar el botón en dispositivos móviles necesitamos forzar su visualización con CSS, ya que éste se esconde automáticamente.

Podríamos crear una variable en el componente llamada *isActive*, por defecto le daremos false indicando que el menú estará plegado:

```javascript
export default {
 data() {
   return {
     isActive: false,
   }
 }
}
```

Cuando hagamos clic en la hamburguesa haremos un toggle, cambiando el valor con un evento clic:

```html
<div class="navbar-burger" @click="isActive = !isActive">
```

A la clase CSS que siempre visualizará el contenido podríamos llamarla *active*:

```css
.active{
  display: block !important;
}
```

Ya sólo nos falta añadirla condicionada al nav-menu usando el bind class:

```html
<div class="navbar-menu" :class="{ active: isActive }">
```

Finalmente podríamos editar el contenido de las páginas, pero no lo vamos a borrar todo, dejaremos por lo menos una tarjeta para usarla como base de las películas:

`pages/index.vue`
```html
<template>
 <section class="section">
   <h2 class="title">Películas</h2>
   <div class="columns is-mobile">
     <card
       title="Free"
       icon="github-circle"
     >
       Open source on 
       <a href="https://github.com/buefy/buefy"> GitHub</a>
     </card>
   </div>
 </section>
</template>
```

`pages/favoritas.vue`
```html
<template>
 <section class="section">
   <h2 class="title">Favoritas</h2>
 </section>
</template>
```

## Adaptando el componente Card

Vamos a preparar el componente central en torno al que gira la SPA, la tarjeta para las películas.

El componente que ahora crea esa cajita en la portada se llama Card, el mismo que tiene esta estructura en Bulma. Tal como está no nos sirve, necesitamos adaptarla un poco. 

Lo primero que podemos hacer es cambiarle el nombre, en lugar de **Card.vue** podríamos llamarla **Peli.vue**.

Obviamente al cambiarle el nombre dejará de funcionar, tendremos que adaptarlo al importarlo:

`pages/index.vue`
```javascript
import Peli from '~/components/Peli'

export default {
  components: {
    Peli
  }
}
```

Y al usarlo:

```html
<Peli
  title="Free"
  icon="github-circle"
>
  Open source on 
  <a href="https://github.com/buefy/buefy"> GitHub</a>
</Peli>
```

¿Creamos algunas pelis de prueba? Mockup data que se dice.

Vamos a añadir una lista con objetos simulando lo que recibiremos de la API, cada uno formado por los campos: id, título, favoritos, imagen, estreno y resumen. 

Podéis copiarlos tal cual os los dejo aquí abajo:

```json
 data: function () {
   return {
     'pelis': [
       {
         'id': 1,
         'titulo': 'El Padrino',
         'favoritos': '3',
         'imagen': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg',
         'estreno': '1972',
         'resumen': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
       },
       {
         'id': 2,
         'titulo': 'El Padrino: Parte 2',
         'favoritos': '1',
         'imagen': 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg',
         'estreno': '1974',
         'resumen': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.',
       },
       {
         'id': 3,
         'titulo': 'El Padrino: Parte 3',
         'favoritos': '0',
         'imagen': 'https://m.media-amazon.com/images/M/MV5BNTc1YjhiNzktMjEyNS00YmNhLWExYjItZDhkNWJjZjYxOWZiXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
         'estreno': '1990',
         'resumen': 'In the midst of trying to legitimize his business dealings in New York City and Italy in 1979, aging Mafia Don Michael Corleone seeks to avow for his sins, while taking his nephew Vincent Mancini under his wing.',
       }
     ]
   }
 },
```

Ahora necesitamos iterar este array y enviar los datos de cada peli al componente. Es muy fácil:

```html
{% raw %}<Peli
 v-for="peli in pelis"
 :key="peli.id"
 :peli="peli"
/>{% endraw %}
```

Usando el v-for repetimos el componente para cada película que guardamos en peli. El v-for requiere indicar una :key única para identificar cada componente, le podemos asignar la id de la película. Por último podemos enviar una propiedad con todo el objeto peli al componente.

Con esto veremos que se crean 3 cajas, pero sin contenido. Lo que debemos hacer es adaptar el componente para extraer los datos de la propiedad peli y hacer uso de ellos:

```javascript
export default {
 props: {
   peli: {
     type: Object
   }
 },
}
```

La estructura de la película es algo más tediosa de programar porque requiere código de Bulma, os voy a facilitar un template básico para no liarnos demasiado:

`components/Peli.vue`
```html
{% raw %}<template>
 <div class="column is-full-mobile is-half-tablet 
             is-one-third-desktop is-one-quarter-widescreen">
   <div class="card">
     <header class="card-header">
       <p class="card-header-title">{{ peli.titulo }}</p>
     </header>
     <div class="card-image">
       <figure class="image">
         <img :src="peli.imagen">
       </figure>
     </div>
     <footer class="card-footer">
       <a class="button is-light card-footer-item">
         <span>{{ peli.favoritos }}</span>
         <b-icon icon="star"></b-icon>
       </a>
     </footer>
   </div>
 </div>
</template>{% endraw %}
```

Este diseño se adapta a las diferentes pantallas usando la grid de columnas de Bulma, parecido a como funciona Boostrap.

Sea como sea ya deberían aparecer las películas, lo malo es que nos surgirá un pequeño problema al estrechar la pantalla, y es que desaparecen las pelis horizontalmente. 

El fallo lo podemos solucionar fácilmente indicando que el contenedor de columns en el **index.vue** acepta multilíneas:

`pages/index.vue`
```html
<div class="columns is-multiline">
```

## Añadiendo una ventana modal

Con lo que tenemos hasta ahora vamos más que sobrados, pero me pareció interesante ilustraros lo que nos facilita buefy tareas como crear una ventana modal.

La idea es que al hacer clic en la película nos aparezca el resumen en este componente emergente. Esto podría parecer un gran trabajo, pero como cada peli es una instancia del mismo componente es muy fácil de implementar. 

Primero necesitamos una variable para controlar si mostrar o no una ventana modal:

`components/Peli.vue`
```javascript
data() {
  return {
    isModalActive: false
  };
},
```

Ahora siguiendo el ejemplo de la [documentación](https://buefy.org/documentation/modal/) de Buefy os facilito el código de la modal, que podemos poner justo debajo del footer de la peli o donde queráis, ya que a fin de cuentas emergerá por encima de todo lo demás:

```html
{% raw %}<!-- Modal para el resumen y año de estreno -->
<b-modal :active.sync="isModalActive">
 <div class="card">
   <div class="card-content">
     <h2 class="title">
       {{ peli.titulo }}
       <small>({{ peli.estreno }})</small>
     </h2>
     <p>{{peli.resumen}}</p>
   </div>
 </div>
</b-modal>{% endraw %}
```

Fijaros en el atributo **active:sync**, ahí es donde pasamos la variable que controla si mostrar o no la modal; así que como podéis suponer sólo necesitamos añadir el evento clic a algún lado y cambiar su valor de false a true. Ese sitio puede ser la propia imagen de la película:

```html
 <div class="card-image" @click="isModalActive=true">
```

Si queréis un efecto más chulo podéis añadir un poco de CSS cambiando el cursor a manita tanto en la imagen como en el fondo oscuro de la modal, eso daría una pista al usuario de que puede hacer clic ahí:

```css
.card-image,
.modal-background {
  cursor: pointer !important;
}
```

Tomaos un descanso porque en la siguiente sección empezamos a darle caña a la API.

## Axios y primera petición

Axios es un cliente http basado en promesas que nos permitirá interactuar fácilmente con la api, para hacerlo deberemos configurar la ruta raíz en el fichero **nuxt.config.js**:

`nuxt.config.js`
```javascript
axios: {
  baseURL: "http://127.0.0.1:8844/api/v1"
},
```

Para cargar las películas en la portada de nuestra página vamos a utilizar el método asyncData de Nuxt.js. En él importamos el módulo axios y realizaremos la petición:

`pages/index.vue`
```javascript
asyncData ({ $axios }) {
  return $axios.get('/peliculas/')
  .then((res) => {
    console.log(res)
  })
}
```

Ahora si tenemos funcionando la API que enseñé a crear en mi otro curso y cargamos la página veremos que nos da un error cuando axios hace la petición, en la consola podremos leer:

```
Access to XMLHttpRequest at 'http://127.0.0.1:8844/api/v1/peliculas/'
from origin 'http://localhost:3000' has been blocked by CORS policy: 
No 'Access-Control-Allow-Origin' header is present on the requested 
resource.
```

¿Qué significa el error y cómo lo solucionamos? Lo veremos en la próxima lección.

## Peticiones CORS a la API de Django

El error nos está indicando que el servidor Django no está configurado para aceptar el intercambio de recursos de origen cruzado o CORS (Cross-origin resource sharing en inglés). En otras palabras, pese a que el cliente y la API se ejecutan en la misma ip local 127.0.0.1, al estar en puertos diferentes no se permite el acceso.

Para solucionarlo deberemos hacer un inciso y modificar nuestro servidor para permitir las peticiones desde la URL 127.0.0.1:3000 que es donde se ejecuta el cliente en desarrollo.

Lo único que tendremos que hacer es instalar y configurar una app de Django llamada [Django Cors Headers](https://github.com/ottoyiu/django-cors-headers/):

```bash
pipenv install django-cors-headers==2.4.0
``` 

Ahora tenemos que activarla y configurarla en el **settings.py** añadiendo en la lista blanca la ip o dominios donde queremos permitir CORS:

```python
INSTALLED_APPS = (  ...
  'corsheaders',
)

MIDDLEWARE = [  ...
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_WHITELIST = (
  'localhost:3000',
  '127.0.0.1:3000'
)
```

Un vez configurados los cors headers si actualizamos la página del cliente ya debería cargar los datos, lo podemos comprobar en el apartado Network del inspector de Chrome.

## Cargando las películas

Ahora que tenemos la información sólo tenemos que sustituir los datos de prueba por los que recibimos. Lo haremos borrando el array 'pelis' de data y devolviendo el nuevo 'data' asíncrono en el método asyncData de Nuxt.js:

`pages/index.vue`
```javascript
asyncData ({ $axios }) {
  return $axios.get('/peliculas/')
  .then((res) => {
    return {
      'pelis': res.data
    }
  })
}
```

Con esto tenemos la magia hecha y al cargar la página ya nos aparecerán las películas en la portada cargadas a través de la API.

Si quisiéramos que aparezcan las películas ordenadas de más a menos favoritos, podríamos cambiar la query de axios añadiendo el filtro programado en DRF:

```javascript
return $axios.get('/peliculas/?ordering=-favoritos')
```

## Buscador de películas por título

Lo último que nos falta en la portada sería añadir un pequeño buscador por título. La API que creamos cuenta un sistema de búsqueda así que podríamos hacer uso de él.

Vamos a empezar creando una variable reactiva para controlar un input de texto:

`pages/index.vue`
```javascript
data() {
  return {
    searchText: ''
  };
},
```

El formulario que manejará esta parte tendrá in input con un v-model que enlazará esta variable, y además un par de botones para buscar y reiniciar el filtro, podéis copiarlo tal cual:

```html
<!-- Empieza la parte de la búsqueda -->
<div class="columns">
  <div class="column">
    <form action="" v-on:submit.prevent="search">
      <b-input
        type="text"
        id="searchInput"
        v-model="searchText"
        placeholder="Filtro por título"
        required>
      </b-input>
    </form>
  </div>
  <div class="column">
    <a class="button is-primary" @click="search">Buscar</a> &nbsp;
    <a class="button is-info" @click="clear">Limpiar</a>
  </div>
</div>
<br>
<!-- Fin de la búsqueda -->
```

Ahora crearemos los dos métodos que se encargarán de hacer la petición, así como desactivar el input, algo importante sobretodo en dispositivos móviles para esconder el teclado virtual:

```javascript
search () {
  this.pelis = []
  this.$el.querySelector('#searchInput').blur()  // esconder teclado
  return this.$axios.get('/peliculas/', {
    params: {
      'search': this.searchText,
      'ordering': '-favoritos'
    }
  })
  .then((res) => {
    this.pelis = res.data
  })
},
clear () {
  this.searchText = '';
  this.search()
}
```

Con esto tendremos el sistema de búsqueda implementado.

## Manejando la autenticación

Empezamos esta sección donde implementaremos el sistema de usuarios en el cliente, primeros haremos la parte de la autenticación y cuando la tengamos añadiremos el registro.

Vamos a crear un pequeño formulario de login que aparezca en una ventana modal cuando hacemos clic en el enlace del menú superior.

Este es el código de la modal, podéis copiarlo directamente:

`layouts/default.vue`
```html
<!-- Modal para el login -->
<b-modal :active.sync="isLoginActive">
  <form action="">
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Identificación</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Email">
          <b-input
            type="email"
            v-model="loginEmail"
            placeholder="Tu email"
            required>
          </b-input>
        </b-field>
        <b-field label="Contraseña">
          <b-input
            type="password" 
            v-model="loginPassword"
            password-reveal
            placeholder="Tu contraseña"
            required>
          </b-input>
        </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-primary">Acceder</button>
    </footer>
    </div>
  </form>
</b-modal>
```

Hace uso de tres variables reactivas, dos cadenas con un email y un password (al que podemos dar datos de prueba para ahorrarnos tiempo), y también otra variable para controlar si se muestra o no:

```javascript
isLoginActive: false,

loginEmail: 'test@test.com',
loginPassword: 'TEST1234A',
```

Como podéis suponer esta variable la modificaremos al hacer clic en el botón de Acceder:

```html
<a class="button is-light" @click="isLoginActive=true">
  Acceder
</a>
```

Lo siguiente es capturar el momento que se envía el formulario y en lugar de hacer una petición automática ejecutar un método para gestionar la petición, por ejemplo 'login':

```javascript
methods: {
  login() {
    return this.$axios.post('/auth/login/', {
      email: this.loginEmail,
      password: this.loginPassword
    })
    .then((res) => {
      if (res.data.key){
      console.log(res.data.key)
      }
    })
    .catch((err) => {
      console.log(err);
    })
  }
 }
```

Para prevenir el envío automático y llamar al método lo haremos así:

```html
<form action="" v-on:submit.prevent="login">
```

Si probamos deberíamos recibir correctamente la key, o sea el token. 

El siguiente paso será almacenarlo para poder utilizarlo en cualquier lugar de nuestra aplicación, de manera que podamos saber en todo momento si estamos o no autenticados.

## Creando nuestro store

Un store es como un almacén de datos transversal accesible desde cualquier parte de nuestra aplicación. Nuxt implementa el store [Vuex](https://nuxtjs.org/guide/vuex-store/) en su núcleo, por lo que es relativamente fácil empezar a trabajar, sólo tenemos que crear el fichero **index.js** dentro del directorio *store/*.

Sin embargo hay dos cosas a tener en cuenta sobre Vuex:

* Los estados (o datos del store, por decirlo de alguna forma) son reactivos, de manera que si se modifica, el cambio se reflejará instantáneamente en toda la aplicación.

* El segundo es que no se puede mutar un estado directamente, es necesario hacer lo que denomina un “commit”. Esto asegura que los cambios dejan un rastro, lo que nos permite entender mejor nuestras aplicaciones.

Hay dos estados que vamos a manejar en nuestra aplicación, el primero es el token y el segundo un "nombre" de usuario. En realidad no será el nombre, simplemente extraemos la primera parte del email.

Para añadir nuestros los dos estados lo haremos así:

`store/index.js`
```javascript
export const state = () => ({
  token: null,
  user: null
})
```

Justo debajo necesitamos crear un par de mutaciones para establecer sus valores:

```javascript
export const mutations = {
  saveUser(state, user){
    state.user = user;
  },
  saveToken(state, token){
    state.token = token;
  }
}
```

Una vez lo tengamos podemos empezar a trabajar con nuestro Store. 

Justo en el momento del login almacenaremos los valores si recibimos correctamente el token de la API, también esconderemos la ventana modal del formulario de login:

`layouts/default.vue`
```javascript
login() {
  return this.$axios.post('/auth/login/', {
    email: this.loginEmail,
    password: this.loginPassword
  })
  .then((res) => {
    if (res.data.key){
      this.$store.commit('saveToken', res.data.key)
      this.$store.commit('saveUser', this.loginEmail.split("@")[0])
      // Reiniciamos los campos
      this.loginEmail = ''
      this.loginPassword = ''
      // Escondemos la modal
      this.isLoginActive = false;
    }
  })
  .catch((error) => {
    alert(Object.values(error.response.data))
  })
},
```

Con esto deberíamos ser capaces de identificarnos al hacer login, el problema es que no podemos saber si realmente estamos identificados o no. Bueno, sí que podemos, debugeando el valor de nuestros estados en medio del código o usando la extensión [Vue Devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=es) de Chrome, bastante recomendable para estos casos.

Una forma interesante de acceder a los estados es usar un valor computado, esto evita algunos errores sobretodo usando apps universales con SSR.

```javascript
computed: {
  user: function () {
    return this.$store.state.user;
  }
},
```

Con esto podemos consultar el nombre del usuario autenticado en todo momento y alternar algunas opciones en el menú superior:

```html
<a class="button" v-if="!user">
  <strong>Registro</strong>
</a>
<a class="button is-primary" v-else>
  Bienvenido {{user}} 😄
</a>
<a class="button is-light" @click="isLoginActive=true" v-if="!user">
  Acceder
</a>
<a class="button is-light" @click="logout" v-else>
  Salir
</a>
```

Ya sólo nos faltaría crear el método para hacer el Logout, cuyo propósito sería simplemente establecer los estados a null:

```javascript
logout() {
  this.$store.commit('saveToken', null)
  this.$store.commit('saveUser', null)
}
```

## Manejando el registro

Como podéis suponer el proceso de registro no será muy diferente al de autenticación. Necesitaremos pasar un email y dos contraseñas repetidas. Si es correcto directamente se devolverá el token y haremos el login.

Evidentemente en un desarrollo más profesional deberíamos enviar el email de verificación a los usuarios, pero como este proyecto es para aprender el funcionamiento general los registraremos directamente.

Empezaremos creando una segunda modal para el registro, podemos ponerla debajo de la de login:

`layouts/default.vue`
```html
<!-- Modal para el registro -->
<b-modal :active.sync="isRegisterActive">
  <form action="" v-on:submit.prevent="register">
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Registro</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Email">
          <b-input
            type="email"
            v-model="registerEmail"
            placeholder="Tu email"
            required>
          </b-input>
        </b-field>
        <b-field label="Contraseña">
          <b-input
            type="password" 
            v-model="registerPassword1"
            password-reveal
            placeholder="Tu contraseña"
            required>
          </b-input>
        </b-field>
        <b-field label="Repite la contraseña">
          <b-input
            type="password" 
            v-model="registerPassword2"
            password-reveal
            placeholder="Tu contraseña"
            required>
          </b-input>
        </b-field>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-primary">Registrarse</button>
      </footer>
    </div>
  </form>
</b-modal>
```

Ésta hará uso de las siguientes variables:

```javascript
isRegisterActive: false,

registerEmail: '',
registerPassword1: '',
registerPassword2:'',
```

Y se abrirá al hacer clic en el botón de registro del menú superior:

```html
<a class="button" v-if="!user" @click="isRegisterActive=true">
    <strong>Registro</strong>
</a>
```

Al completar el formulario llamaremos al método register():

```javascript
register() {
 return this.$axios.post('/auth/registration/', {
   email: this.registerEmail,
   password1: this.registerPassword1,
   password2: this.registerPassword2
 })
 .then((res) => {
   if (res.data.key){
     this.$store.commit('saveToken', res.data.key)
     this.$store.commit('saveUser', this.registerEmail.split("@")[0])
     // Reiniciamos los campos
     this.registerEmail = ''
     this.registerPassword1 = ''
     this.registerPassword2 = ''
     // Escondemos la modal
     this.isRegisterActive = false;
   }
 })
 .catch((error) => {
   alert(Object.values(error.response.data))
 })
},
```

Con esto ya debería funcionar el formulario y cuando el usuario se registre accederá automáticamente al establecerse su token y usuario en el store.

En caso de que algo no funcione, como estamos mostrando los fallos que nos devuelve la API podremos verlo en un alert, cuyo idioma nos aparecerán automáticamente en el que tenga configurado Django, ¡es genial!

## Página de películas favoritas

Antes de nada, la sección de películas favoritas debería aparecer únicamente si el usuario está autenticado, así que en lugar de generar el menú dinámicamente vamos a hacerlo a mano comprobando esa posibilidad:

`pages/favoritas.vue`
```html
<ul class="menu-list">
  <li>
    <nuxt-link to="/pelis" exact-active-class="is-active">
      <b-icon icon="video"/>
      Películas
    </nuxt-link>
  </li>
  <li v-if="user">
    <nuxt-link to="/favoritas" exact-active-class="is-active">
      <b-icon icon="star"/>
      Favoritas
    </nuxt-link>
  </li>
</ul>
```

Otra opción importante es que no se pueda visitar esta página si  no estamos autenticados. 

Para manejar la situación usaremos el fetch, un método que se ejecuta antes de montar la página y que está indicado para gestionar el store. En él podemos comprobar si hay un usuario y si no redireccionar a otra página:

```javascript
fetch ({ store, redirect }) {
  if (!store.state.user) {
    return redirect('/')
  }
},
```

Si intentamos visitar */favoritas* sin iniciar sesión seremos redirigidos automáticamente a la portada.

Por supuesto también tenemos que tener en cuenta que al cerrar la sesión se redireccione a la portada, así que modificaremos el logout() para hacerlo, esta vez usando el módulo *$router* de Nuxt.js:

`layouts/default.vue`
```javascript
logout() {
  ...
  // Redireccionamos a la portada al salir
  this.$router.replace({ path: '/' })
}
```

El siguiente paso será recuperar las pelis favoritas del usuario al cargar la página, para ello necesitaremos consultar la API pasando el token de autenticación:

`pages/favoritas.vue`
```javascript
asyncData ({ store, $axios }) {
  if (store.state.token) {
    return $axios.get('/favoritas/', {
      headers: {
        'Authorization': `Token ${store.state.token}`
      }
    })
    .then((res) => {
      return {
        'favoritas': res.data
      }
    })
  }
},
```

Si inspeccionamos las peticiones veremos si se está llamando correctamente a la API.

Sólo tenemos que copiar literalmente la visualización de películas de la portada a esta página y debería funcionar:

```html
<template>
 <section class="section">
   <h2 class="title">Favoritas</h2>
   <div class="columns is-multiline">
     <Peli
       v-for="favorita in favoritas"
       :key="favorita.pelicula.id"
       :peli="favorita.pelicula"
     />
   </div>
 </section>
</template>
```

Lo mejor de todo es que podemos editar el componente Card para modificar la estructura de todas las películas de la web, tanto de la portada como las de nuestro perfil.

Por cierto, un detalle muy útil sería redireccionar al usuario a sus pelis favoritas cuando se identifique, es fácil usando el módulo *$router* de Nuxt.js: 

`layouts/default.vue`
```javascript
.then((res) => {
  if (res.data.key){
    ...
    // Redireccionamos a las pelis favoritas
    this.$router.replace({ path: '/favoritas' })
  }
})
```

## Manejando las favoritas en el store

Vamos a hacer que el usuario pueda marcar y desmarcar películas como favoritas, sin embargo antes necesitamos controlar en todo momento las películas que ya son favoritas, por ejemplo teniendo la lista en el store.

No necesitamos guardar toda la información, nos bastaría con un array que contenga sólo los id:

`store/index.js`
```javascript
export const state = () => ({
  ...
  favIds: []
})
```

Para manejarlo podemos crear una mutación llamada *toggleFavorite* que añada o borre un id a la lista:

```javascript
toggleFavorite(state, id){
  var index = state.favIds.indexOf(id)
  if (index !== -1) state.favIds.splice(index, 1)
  else state.favIds.push(id)
}
```

El momento perfecto para añadirlas en el store es al acceder al visitar la página de pelis favoritas, pero sólo si el arregla está vacío será necesario agregarlas:

`pages/favoritas.js`
```javascript
.then((res) => {
  // Añadimos los ids de las pelis favoritas al store
  if (store.state.favIds.length == 0) {
    res.data.forEach((fav) => {
      store.commit('toggleFavorite', fav.pelicula.id)
    });
  }
  return {
    'favoritas': res.data
  }
})
```

Comprobando el store con la extensión de Vue podemos ver cómo se ejecuta un commit cada vez que se añade una peli a favoritos.

Con esto ya podemos controlar los cambios en la memoria de la aplicación, no nos costaría mucho añadir una clase activa al botón si la peli actual forma parte de la lista en el store:

`components/Peli.vue`
```html
{% raw %}<a 
  class="button is-light card-footer-item"
  :class="{ 'is-primary': 
            this.$store.state.favIds.indexOf(peli.id) !== -1 }"
>{% endraw %}
```

Como estamos trabajando con componentes esto nos funcionará tanto en la portada como en la sección películas.

## Añadiendo el botón de acción

Vamos a hacer que funcione ese botón para manejar las películas favoritas.

Lo primero será crear un método para manejar la petición autenticada y establecer o borrar el favorito:

`components/Peli.vue`
```javascript
{% raw %}methods: {
  toggleFavorite() {
    // Si estamos identificados... que lo deberíamos
    if (this.$store.state.token) {
      return this.$axios
        .post(
          "/favorita/",
          { id: this.peli.id },
          {
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          }
        )
        .then(res => {
          if (res.data.id) {
            this.$store.commit("toggleFavorite", res.data.id);
          }
        })
        .catch(error => {
          alert(Object.values(error.response.data));
        });
    } else {
      alert("Necesitas identificarte para marcar pelis favoritas");
    }
  }
}{% endraw %}
```

```html
{% raw %}<a
  class="button is-light card-footer-item"
  :class="{ 'is-primary': 
            this.$store.state.favIds.indexOf(peli.id) !== -1} "
  @click="toggleFavorite"
>{% endraw %}
```

Sólo nos faltaría sumar o restar al número de favoritos dependiendo del resultado:

```javascript
{% raw %}.then(res => {
  if (res.data.id) {
    this.$store.commit("toggleFavorite", res.data.id);
    if (res.data.favorita) {
      this.peli.favoritos += 1;
    } else {
      this.peli.favoritos -= 1;
    }
  }
}){% endraw %}
```

Como podéis observar trabajar con componentes nos ahorra mucho trabajo.

## Implementando un plugin de alertas

La aplicación ya está funcionando perfectamente, pero hay un detalle que podemos perfeccionar, me refiero a esos alerts() que hemos puesto.

Los alerts son como ventanas emergentes que bloquean la ejecución del código. 

Vamos a usar una librería llamada [Toastr](https://github.com/CodeSeven/toastr) para sustituirlos y crear un efecto non-blocking mucho más interesante y elegante.

Pero  no vamos a utilizarla desde CDN, aprovecharemos que Vue tiene una versión llamada [vue-toaster](https://www.npmjs.com/package/vue-toasted) que podemos instalar de la siguiente forma:

```bash
npm install vue-toasted --save
```

Ahora vamos a crear un plugin para poder utilizarlo en nuestra app:

`plugins/toast.js`
```javascript
import Vue from 'vue'
import Toasted from 'vue-toasted';

var options = {
  position: 'top-center',
  duration: 4000,  // milisegundos de vida
}

Vue.use(Toasted, options)
```

Para activar el plugin, y dado que sólo funcionará en el lado del cliente lo haremos así en:

`nuxt.config.js`
```javascript
plugins: [
  { src: '~/plugins/toast', ssr: false},
],
```

Ahora sólo tenemos que hacer uso de la librería sustituyendo los alerts de los errores, por ejemplo del registro y el login:

`layouts/default.vue`
```javascript
// alert(Object.values(error.response.data))
this.$toasted.error(Object.values(error.response.data))
```

El resultado es simplemente genial.

Hay varias opciones, para mostrar mensajes satisfactorios, errores y más, echad una ojeada a la [documentación de vue-toasted](https://github.com/shakee93/vue-toasted#usage) para aprender más.

___
<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>