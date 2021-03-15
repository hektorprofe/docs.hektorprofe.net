title: Template tag &#123;% url %&#125; | Curso de Django | Hektor Profe
description: Este tag nos permite hacer referencia directamente a una view desde nuestros templates.

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{ color: #018dc5 !important; }
.admonition.note { box-shadow: none; margin: 0; padding: 0; border-left: 0; border-radius: 0; font-size: 105%; }
.admonition.note label{ font-size: 91%; }
.admonition.note > .admonition-title { display: none; }
</style>

# Template tag &#123;% url %&#125;

Antes de continuar no puedo evitar introducir una buena práctica para que en el futuro nunca cometáis mis errores del pasado. Me refiero al template tag **&#123;% url %&#125;**. 

Este tag nos permite hacer referencia directamente a una view desde nuestros templates y es la forma correcta de escribir enlaces relativos dentro de nuestra web.

Vamos de vuelta a nuestro template **base.html** y vamos a sustituir los enlaces "hard code" escritos directamente, por url automatizadas. 

La forma es muy sencilla **&#123;% url 'nombre_en_el_path %'&#125;**:

`core/templates/core/base.html`
```html
{% raw %}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %}</title>
    
</head>
<body>
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="{% url 'home' %}">Portada</a></li>
        <li><a href="{% url 'about' %}">Acerca de</a></li>
        <li><a href="{% url 'portfolio' %}">Portafolio</a></li>
        <li><a href="{% url 'contact' %}">Contacto</a></li>
    </ul>

    {% block content %}{% endblock %}
    
</body>
</html>{% endraw %}
``` 

En la práctica es lo mismo, pero si vamos a nuestro **urls.py** y cambiamos una dirección, por ejemplo **about** por **about-me**:

`webpersonal/urls.py`
```python
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]
```

Sin cambiar absolutamente nada en el template, la url del menú se habrá actualizado y seguirá funcionando perfecto:

<div style="text-align:center;margin-top:25px"><img class="lazy" data-src="{{cdn}}/django/23.png"/></div>

Por tanto la enseñanza de la lección es:

> Nunca utilices hard-code para tus enlaces, en su lugar usa el template tag url.

___
<small class="edited"><i>Última edición: 25 de Octubre de 2018</i></small>