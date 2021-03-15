title: Templates about, portfolio y contact | Curso de Django | Hektor Profe
description: Ahora es tu turno de crear los templates de las otras dos páginas.

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{ color: #018dc5 !important; }
.admonition.note { box-shadow: none; margin: 0; padding: 0; border-left: 0; border-radius: 0; font-size: 105%; }
.admonition.note label{ font-size: 91%; }
.admonition.note > .admonition-title { display: none; }
</style>

# Templates about, portfolio y contact

Ahora es tu turno de crear los templates de las otras tres páginas. El resultado final será el mismo, pero ahora podrás dejar bien limpio el fichero **core/views.py** y borrar todo el código que ya no necesites.

## Solución
`core/templates/core/about.html`

```html 
<h1>Mi Web Personal</h1>

<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>

<h2>Acerca de</h2>

<p>Me llamo Héctor y me encanta Django!</p>
```
`core/templates/core/portfolio.html`

```html
<h1>Mi Web Personal</h1>

<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>

<h2>Portafolio</h2>

<p>Algunos de mis trabajos.</p>
```
`core/templates/core/contact.html`

```html
<h1>Mi Web Personal</h1>

<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>

<h2>Contacto</h2>

<p>Aquí os dejo mi email y mis redes sociales:</p>

<ul>
    <li><a href="mailto:hola@hektorprofe.net">Email</a></li>
    <li><a href="https://github.com/hcosta">Github</a></li>
    <li><a href="https://youtube.com">Youtube</a></li>
</ul>
```
`core/views.py`

```python
    from django.shortcuts import render, HttpResponse

    def home(request):
        return render(request, "core/home.html")

    def about(request):
        return render(request, "core/about.html")

    def portfolio(request):
        return render(request, "core/portfolio.html")

    def contact(request):
        return render(request, "core/contact.html")
    ```
`webpersonal/urls.py`

```python
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]
```

___
<small class="edited"><i>Última edición: 25 de Octubre de 2018</i></small>