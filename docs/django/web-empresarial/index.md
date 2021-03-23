title: Proyecto Web Empresarial | Curso de Django | Hektor Profe
description: Empezamos el segundo proyecto del curso a lo largo del cual crearemos una web empresarial. 

# Proyecto Web Empresarial

Empezamos el segundo proyecto del curso a lo largo del cual crearemos una web empresarial. Se trata de una página de presentación para un negocio, donde se muestra información de la empresa, su catálogo de servicios y otras funcionalidades.

<div class='embed-container'><iframe src='https://player.vimeo.com/video/297286788' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

Vamos a echar un vistazo al frontend que os he preparado, el cual podéis descargar en los recursos de esta lección y descomprimir en el directorio CursoDjango.

!!! important "Demo de la Web Empresarial y recursos"
    Puedes ver el proyecto final en el siguiente enlace: <u><a href="http://webempresa.pythonanywhere.com/" target="_blank">http://webempresa.pythonanywhere.com/</a></u>. Recuerda que sólo los <u><a href="https://www.udemy.com/curso-django-2-practico-desarrollo-web-python-3/?couponCode=DJANGO2" target="_blank">alumnos matriculados</a></u> pueden descargar los diseños frontend preparados para realizar el curso paso a paso.

Como podéis observar tenemos un frontend para una cafetería: **La Caffettiera, L'AUTENTICO CAFFÈ D'ITALIA**. Si navegais por las distintas páginas notaréis que se trata de un frontend bastante bien acabado, da la sensación de que no hay mucho que hacer, pero creedme que este proyecto nos servirá para aprender un montón.

En todo desarrollo web lo primero es diferenciar las páginas estáticas de las dinámicas, es decir, por un lado las que su contenido no cambiará y por otro las que el cliente podrá manejar desde el panel de administrador. 

En el caso de la Caffettiera, las páginas estáticas serían la "portada", "historia" y "visítanos". Son páginas que apenas cambiarán con el tiempo y nos permiten trabajar más la parte frontend para hacerlas más atractivas. Todas ellas las manejaremos en la clásica app **Core**, como en la web personal.

Respecto a las secciones dinámicas nos quedan Servicios y Blog. 

Fijaros como la estructura de los Servicios es siempre la misma: subtítulo, título, imagen de fondo y un texto de contenido. Y por otro lado, las entradas del Blog también tienen una estructura común: fecha, título, imagen, texto de contenido, autor y categorías. Seguro que ya os habéis percatado de que ambas se pueden trasladar a modelos. Las manejaremos en sus respectivas apps **Services** y **Blog**.

Pero eso no es todo, hay otros elementos que nos conviene tener automatizados y que encontramos en el pie de página, me refiero a los enlaces a las redes sociales y las páginas genéricas con políticas de empresa, avisos legales, etc. Las redes sociales las vamos a gestionar en una app **Social** donde daremos al cliente la posibilidad de establecer el enlace a varias de ellas: twitter, facebook, instagram, etc. Respecto a las páginas secundarias, tendremos una app **Pages** para gestionarlas.

Finalmente  tenemos la sección de contacto. Que podríamos considerarla una página estática, pero como tiene que capturar el formulario y enviarnos los mensajes en forma de email, la vamos a gestionar en su propia app.

En resumen, el backend de "La Caffettiera" estará formado por ni más ni menos que seis apps completamente reutilizables: 

* **Core**: para gestionar las páginas estáticas (portada, historia y visítanos).
* **Services**: para gestionar los servicios de la sección servicios.
* **Blog**: para gestionar las entradas y sus categorías.
* **Social**: para manejar los enlaces a las redes sociales del pie de página. 
* **Pages**: para gestionar las páginas secundarias del pie de página. 
* **Contact**: para manejar capturar el formulario de contacto y enviar un email con el mensaje. 

___
<small class="edited"><i>Última edición: 29 de Octubre de 2018</i></small>