title: Segunda App [Portfolio] Modelos | Curso de Django | Hektor Profe
description: En esta lección vamos a añadir dinamismo al portafolio haciendo que interactúe con una base de datos.

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{ color: #018dc5 !important; }
.admonition.note { box-shadow: none; margin: 0; padding: 0; border-left: 0; border-radius: 0; font-size: 105%; }
.admonition.note label{ font-size: 91%; }
.admonition.note > .admonition-title { display: none; }
</style>

# Segunda App [Portfolio] Modelos

Ahora ya tenemos el sitio fusionado, pero el requisito de nuestro cliente era tener un panel para gestionar el portafolio y ahora mismo sólo tenemos datos de prueba.

En esta lección vamos a añadir dinamismo al portafolio haciendo que interactúe con una base de datos, para ello crearemos una nueva app llamada **portfolio**. Durante su creación aprenderemos a definir modelos y a utilizar el panel de administrador. Os aseguro que os va a gustar.

Así que la pregunta es ¿qué gestiona el portafolio? ¿Proyectos no? ¿Y qué campos tiene un proyecto…? Un título, una descripción, un enlace y una imagen ¿verdad?.

Para que Django pueda manipular imágenes necesita un módulo externo llamado Pillow, vamos a empezar instalándolo en nuestro entorno virtual:

```
(django2) pip install Pillow
```

Una vez instalado Pillow vamos a definir la estructura de nuestros proyectos: aquí es donde entran en escena los modelos y el potente sistema de mapeado ORM modelo-objeto-relacional de Django. ¿Qué significa esto? 

Significa que si seguimos las pautas de Django podremos trabajar con objetos mapeados en la base de datos, de manera que al crear instancias de una clase específica, estas quedarán guardadas como registros de forma automática. 

En Django las clases que manejan estos objetos persistentes se conocen como Modelos. Lo vais a ver muy fácilmente con la práctica.

Vamos a crear nuestro modelo para almacenar *Proyectos*, pero como vamos a hacerlo en una nueva app tenemos que crearla antes:

```
(django2) python manage.py startapp portfolio
```

Para definir un nuevo modelo **Proyecto** nos vamos a dirigir al fichero **portfolio/models.py**, pero no podemos hacerlo de cualquier forma, debemos seguir unas pautas.

Crear un modelo es fácil, sólo tenemos que crear una clase heredando de una clase padre llamada **models.Model**. Es importante que el nombre de la clase siempre sea en singular, en nuestro caso sería **Project** (lo voy a poner en inglés para seguir un orden en todo el código):

`portfolio/models.py`

```python
from django.db import models

class Project(models.Model):
    pass
```

Esta clase representará una tabla dentro de la base de datos. Lo siguiente será crear sus columnas, que no serán otra cosa que los atributos de la clase. Por ahora crearemos el título, la imagen y la descripción, además de dos campos especiales que nos servirán para almacenar automáticamente la fecha y hora de creación del registro, así como la fecha y hora de la última edición. No os preocupéis por el campo de la dirección web, lo dejaremos para más adelante:


`portfolio/models.py`

```python
from django.db import models

class Project(models.Model):
    title = 
    description = 
    image = 
    created = 
    updated = 
```

Como podéis suponer con el nombre no basta. tenemos que indicarle a Django qué representarán cada uno de estos campos. Es decir, si son cadenas de texto, números, fechas, imágenes… Para hacerlo utilizaremos los modelos definidos dentro del módulo **models**.

`portfolio/models.py`

```python
from django.db import models

class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

Hay muchos tipos de datos, pero por ahora prefiero no entrar en detalles, luego os pondré un ejercicio donde tendréis que investigar sobre los tipos de datos. Por ahora tenemos una cadena con un título (charfield), una imagen (imagefield), un texto largo con la descripción (textfield) y dos fechas con hora (datetimefield).

Con esto ya tenemos nuestro modelo, pero todavía no podemos utilizarlo. Antes tenemos que añadir la app **portfolio** a las apps de nuestro proyecto y luego migrar el modelo a la base de datos.


`webpersonal/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'portfolio',  # <====
]
```

Para migrar la app necesitaremos dos comandos:

El primero es **makemigrations**, que sirve para indicarle a Django que hay cambios en algún modelo, de manera que creará un fichero de migraciones. Si en el futuro tenemos algún problema, siempre podremos restaurar una migración anterior.

Vamos a crear la migración a ver qué sucede:

```
(django2) python manage.py makemigrations portfolio
```

Nos devuelve un error: "El campo CharField debe tener definido un atributo max_length". ¿Recordáis cuando os he dicho que los modelos están enlazados a la base de datos? Pues esa es una de esas restricciones que tienen los campos de una tabla SQL. Los campos de tipo cadena de caracter necesitan que les definamos una longitud máxima. Vamos a hacerlo:


`portfolio/models.py`

!!! note 
```python
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

Ahora creamos de nuevo la migración y ya debería funcionar:

```
(django2) python manage.py makemigrations portfolio
```

Sólo nos falta aplicarla a la base de datos, que lo haremos con el comando **migrate**:

```
(django2) python manage.py migrate portfolio
```

**Recordad**, cada vez que hagamos un cambio en nuestro ficheros **models.py** ejecutaremos estos dos comandos para crear una migración y posteriormente aplicarla.

Ahora que tenemos nuestro modelo ¿podríamos crear algún registro no? ¿Cómo lo hacemos? Hay dos formas:

* Podemos crear una vista que procese un formulario y a partir de él crear los proyectos.
* O bien podemos utilizar el panel de administrador de Django y dejar que él se encargue de todo.

La primera forma tiene sentido en entornos abiertos donde tenemos que proporcionar formularios a los visitantes para que interactúen con la página. En cambio la segunda es ideal para entornos cerrados donde sólo algunos usuarios tienen acceso a la base de datos. Como nuestra web es personal y sólo nosotros o el cliente tendrá acceso a la base de datos, la segunda forma nos va de perlas, por ahora lo dejamos aquí.

___
<small class="edited"><i>Última edición: 25 de Octubre de 2018</i></small>