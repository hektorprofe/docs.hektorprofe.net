title: Adaptar las plantillas con herencia | Curso de Django | Hektor Profe
description: En este ejercicio deberás adaptar las plantillas about, portfolio y contact para que extiendan de base.

# Adaptar las plantillas con herencia

Para este ejercicio deberás adaptar las plantillas *about, portfolio y contact* para que extiendan de *base*. También te reto a crear un nuevo bloque llamado *title* a través del cual debes lograr que cambie el título en cada página dentro de la etiqueta **&#60;title&#62;**. Las páginas deberán tener el título siguiendo este patrón:

* Portada | Mi Web Personal
* Acerca de | Mi Web Personal
* Portafolio | Mi Web Personal
* Contacto | Mi Web Personal

## Solución

`core/templates/core/base.html`

```html
{% raw %}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %} | Mi Web Personal</title>
</head>
<body>
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>

    {% block content %}{% endblock %}
    
</body>
</html>{% endraw %}
```

`core/templates/core/portada.html`

```html 
{% raw %}{% extends 'core/base.html' %}

{% block title %}Portada{% endblock %}

{% block content %}
    <h2>Mi Web Personal</h2>
    <p>Bienvenidos.</p>
{% endblock %}{% endraw %}
``` 

`core/templates/core/about.html`

```html 
{% raw %}{% extends 'core/base.html' %}

{% block title %}Acerca de{% endblock %}

{% block content %}
    <h2>Acerca de</h2>
    <p>Me llamo Héctor y me encanta Django!</p>
{% endblock %}{% endraw %}
```

`core/templates/core/portfolio.html`

```html
{% raw %}{% extends 'core/base.html' %}

{% block title %}Portafolio{% endblock %}

{% block content %}
    <h2>Portafolio</h2>
    <p>Algunos de mis trabajos.</p>
{% endblock %}{% endraw %}
```

`core/templates/core/contact.html`

```html
{% raw %}{% extends 'core/base.html' %}

{% block title %}Contacto{% endblock %}

{% block content %}
    <h2>Contacto</h2>
    <p>Aquí os dejo mi email y mis redes sociales:</p>

    <ul>
        <li><a href="mailto:hola@hektorprofe.net">Email</a></li>
        <li><a href="https://github.com/hcosta">Github</a></li>
        <li><a href="https://youtube.com">Youtube</a></li>
    </ul>
{% endblock %}{% endraw %}
```

___
<small class="edited"><i>Última edición: 25 de Octubre de 2018</i></small>