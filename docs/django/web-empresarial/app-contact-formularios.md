title: Séptima App (Contact) Formularios | Curso de Django | Hektor Profe 

# Séptima App [Contact] Formularios

Durante las próximas cuatro lecciones nos introduciremos en el mundo de los formularios de Django, obviamente el objetivo será dotar de vida al formulario de contacto de nuestra web:

* En esta primera lección crearemos la respectiva app y trasladaremos la vista y el template contact que tenemos en Core. Aprenderemos a diseñar el formulario, a utilizarlo en la vista y a mostrarlo en su respectivo template. 
* En la segunda lección veremos cómo procesar y validar sus campos al enviarlo
* En la tercera lección os mostraré como fusionar el formulario para respetar el diseño del frontend.
* Para acabar esta serie añadiremos la funcionalidad de enviar emails, configuraremos un email real y lo probaremos.

## App Contact

Empecemos creando la app contacto:

```bash
python manage.py startapp contact
```

Trasladamos la vista `contacto` a la nueva app:

`webempresa/contact/views.py`

```python
from django.shortcuts import render

def contact(request):
    return render(request, "core/contact.html")
```

Creamos las url de la app:

`webempresa/contact/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
]
```

Las añadimos a las url del proyecto:

`webempresa/webempresa/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('admin/', admin.site.urls),

    # Paths de pages
    path('contact/', include('contact.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Activamos la app:

`webempresa/webempresa/settings.py`

```python
INSTALLED_APPS = [
    'contact',
]
```

Movemos el antiguo template de `core\templates\core\contact.html` a la app `contact\templates\contact\contact.html`

## Formulario de contacto

El caso es que cuando necesitemos un formulario, Django nos ofrece la posibilidad de crear un diseño de forma muy parecida a cómo se crean los modelos, de manera que él mismo se encargará de generar el HTML resultante. Además nos provee de una serie de métodos para procesarlo y validar sus campos. 

Normalmente se crean en un fichero forms.py dentro de la respectiva app, heredando de una clase llamada Form que hay en el módulo forms. Nosotros vamos a crear el nuestro en la app Core, que es la que gestiona la vista Contact:

`webempresa/contact/forms.py`
```python
from django import forms

class ContactForm(forms.Form):
    pass
```

Como os he dicho es parecido a crear un modelo, ya que debemos indicar los campos y su tipo. El nuestro tiene tres: un nombre que será una cadena de texto, un email que tiene su propio tipo y el contenido, es lo mínimo necesario para que alguien pueda enviarnos un mensaje y le podamos responder.

`webempresa/contact/forms.py`
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre", required=True)
    email = forms.EmailField(
        label="Email", required=True)
    content = forms.CharField(
        label="Contenido", required=True, widget=forms.Textarea()
```

Como podéis notar sus campos vienen definidos en el módulo forms en lugar de models y para el nombre se utiliza el atributo `label` en lugar de `verbose_name`. Por defecto estos campos se renderizan como tags `<input>`, pero se pueden cambiar estableciendo un tipo de widget, como en el caso del contenido donde queremos mostrar un tag `<textarea>`.

Hay campos para todo: cadenas, numéros, emails, fechas, opciones desplegables, ficheros, etc. Os adjunto [un enlace](https://docs.djangoproject.com/en/dev/ref/forms/fields/#built-in-field-classes) por si queréis aprender más.

Sea como sea ya tenemos diseñado el formulario, así que vamos a utilizarlo, pero antes comentaremos el que tenemos en el template `contact.html`, porque ese es sólo de prueba. Más adelante lo adaptaremos, pero por ahora nos centraremos en lo importante.

![]({{cdn}}/django/images/image296.png)

Importamos el formulario, creamos una instancia en la vista y la
enviamos al template:

![]({{cdn}}/django/images/image792.png)\
![]({{cdn}}/django/images/image711.png)

Ahora en nuestro template contact.html vamos el dibujar el formulario:

![]({{cdn}}/django/images/image755.png)

![]({{cdn}}/django/images/image521.png)

¿Habéis visto que fácil es que nos lo dibuje automáticamente?

Por defecto hemos dibujado en formulario como una tabla, de ahí que lo
hayamos puesto entre el tag \<table\>, pero también se puede dibujar
como parágrafos o una lista:

![]({{cdn}}/django/images/image205.png)                                        

![]({{cdn}}/django/images/image914.png)        

![]({{cdn}}/django/images/image673.png)         

![]({{cdn}}/django/images/image204.png)

Personalmente prefiero la forma de tabla, así que lo dejaré como estaba:

![]({{cdn}}/django/images/image838.png)

Sin embargo Django no dibuja todo el formulario, sólo los campos. No hay
ningún botón para procesarlo, y si inspeccionamos el código veremos
también falta el tag \<form\>, necesario para crear formularios HTML:

![]({{cdn}}/django/images/image883.png)

Seguimos en la segunda parte.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>