title: Adaptar los demás templates | Curso de Django | Hektor Profe
description: En este ejercicio deberás lograr que las secciones de nuestra web con Django se vean exactamente iguales. 

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{ color: #018dc5 !important; }
.admonition.note { box-shadow: none; margin: 0; padding: 0; border-left: 0; border-radius: 0; font-size: 105%; }
.admonition.note label{ font-size: 91%; }
.admonition.note > .admonition-title { display: none; }
</style>

# Adaptar los demás templates

En este ejercicio deberás tomar como referencia las maquetas *about.html, portfolio.html y contact.html* y lograr que las secciones de nuestra web con Django se vean exactamente iguales. 

!!! info "Recordatorio"

    No olvides el tag **&#60;hr&#62;** dentro del footer. Esta línea debe mostrarse en todas las páginas menos la portada, a ver si se te ocurre alguna forma de hacerlo. Pistas: variable **&#123;&#123;request.path&#125;&#125;** y template tags: **&#123;% if %&#125;** **&#123;% endif %&#125;**.

## Solución

`core/templates/core/base.html`

```html
{% raw %}<!-- Contenido -->
<div class="container">
  {% block content %}{% endblock %}
</div>{% endraw %}
``` 

El **&#60;hr&#62;** se puede poner en un block, pero esta solución es más elegante.

`core/templates/core/base.html`

```html
{% raw %}<!-- Contenido -->

<div class="container">
  {% block content %}{% endblock %}
</div>

{% if request.path != "/" %}<hr>{% endif %}

<!-- Pié de página -->{% endraw %}
``` 

`core/templates/core/about.html` 
```html
{% raw %}{% extends 'core/base.html' %}
{% load static %}

{% block title %}Acerca de{% endblock %}

{% block background %}{% static 'core/img/about-bg.jpg' %}{% endblock %}

{% block headers %}
    <h1>Acerca de</h1>
    <span class="subheading">Biografía</span>
{% endblock %}

{% block content %}
<div class="row"> 
    <div class="col-lg-3 col-md-4 offset-lg-1">
        <img class="img-fluid avatar" 
            src="{% static 'core/img/avatar.jpg' %}" alt="">
    </div>
    <div class="col-lg-7 col-md-8">
        <h2 class="section-heading">Juan Pérez</h2>   
        <p>Nacido en... lorem ipsum dolor sit amet, consectetur
        adipisicing elit. Saepe nostrum ullam eveniet pariatur
        voluptates odit, fuga atque ea nobis sit soluta odio.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Saepe nostrum ullam eveniet pariatur voluptates odit...</p>
    </div>
</div>
{% endblock %}{% endraw %}
``` 

`core/templates/core/portfolio.html` 
```html
{% raw %}{% extends 'core/base.html' %}

{% load static %}

{% block title %}Portafolio{% endblock %}

{% block background %}{% static 'core/img/portfolio-bg.jpg' %}{% endblock %}

{% block headers %}
    <h1>Portafolio</h1>
    <span class="subheading">Currículo</span>
{% endblock %}

{% block content %}
    <!-- Proyecto -->
    <div class="row project">  	
        <div class="col-lg-3 col-md-4 offset-lg-1">
            <img class="img-fluid" 
                src="{% static 'core/img/about-bg.jpg' %}" alt="">
        </div>
        <div class="col-lg-7 col-md-8">
            <h2 class="section-heading title">Segundo proyecto</h2>   
            <p>As we got further and further away, it [the Earth]
            diminished in size. Finally it shrank to the size of a marble,
            the most beautiful you can imagine. That beautiful, warm....</p>
            <p><a href="http://google.com">Más información</a></p>
        </div>
    </div>
    <!-- Proyecto -->
    <div class="row project">  	
        <div class="col-lg-3 col-md-4 offset-lg-1">
            <img class="img-fluid" 
                src="{% static 'core/img/home-bg.jpg' %}" alt="">
        </div>
        <div class="col-lg-7 col-md-8">
            <h2 class="section-heading title">Primer proyecto</h2>   
            <p>As we got further and further away, it [the Earth]
            diminished in size. Finally it shrank to the size of a marble,
            the most beautiful you can imagine. That beautiful, warm....</p>
            <p><a href="http://google.com">Más información</a></p>
        </div>
    </div>
{% endblock %}{% endraw %}
``` 

`core/templates/core/contact.html`
```html
{% raw %}{% extends 'core/base.html' %}

{% load static %}

{% block title %}Contacto{% endblock %}

{% block background %}{% static 'core/img/contact-bg.jpg' %}{% endblock %}

{% block headers %}
    <h1>Contacto</h1>
    <span class="subheading">Asesoría</span>
{% endblock %}

{% block content %}
<div class="row"> 
    <div class="col-lg-8 col-md-10 mx-auto">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Saepe nostrum ullam eveniet pariatur voluptates odit, fuga
        atque ea nobis sit soluta odio, adipisci quas excepturi maxime
        quae totam ducimus consectetur?</p>
        <br>
        <p><b>Teléfono:</b> +09 876 543 210</p>
        <p><b>Honorarios:</b> 60€/h (precio base)</p>
    </div>
</div>
{% endblock %}{% endraw %}
``` 

___
<small class="edited"><i>Última edición: 25 de Octubre de 2018</i></small>