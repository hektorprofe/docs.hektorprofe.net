title: Interfaces gráficas con Tkinter | Curso de Python | Hektor Profe
description: Las interfaces gráficas son medios visuales con los que nuestros usuarios pueden interactuar y realizar tareas gráficamente.

# Interfaces gráficas con Tkinter

Las interfaces gráficas son medios visuales, mucho más cómodos que una terminal de texto, a través de las cuales nuestros usuarios pueden interactuar y realizar tareas gráficamente.

<div class='embed-container'><iframe src='https://player.vimeo.com/video/292161566' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

## Recursos

En esta unidad haremos servir algunos ficheros, básicamente imágenes. Las tendréis disponibles aquí por si queréis utilizarlas, simplemente **haced clic derecho y guardar como**:

|  Fichero    | Enlace |
|  --------   | -----: |
|  hola.ico   | <a href="/cdn/images/tkinter/hola.ico" target="_blank">Guardar como</a> |
|  hola.xbm   | <a href="/cdn/images/tkinter/hola.xbm" target="_blank">Guardar como</a>   |
|  imagen.gif | <a href="/cdn/images/tkinter/imagen.gif" target="_blank">Guardar como</a>   |

## Widgets

El módulo Tkinter cuenta con una serie de componentes gráficos llamados Widgets, gracias a los cuales podemos diseñar nuestras interfaces. 

Los widgets deben seguir una jerarquía a la hora de añadirse a la interfaz. Por ejemplo, un Marco (frame) forma parte del objeto raíz Tk. Y a su vez, un botón (button) puede formar parte de un contenedor como la raíz o un marco. 

Los que veremos en esta introducción a Tkinter son:

* **Tk**: Contenedor base o raíz de todos los widgets que forman la interfaz. No tiene tamaño propio sino que se adapta a los widgets que contiene.
* **Frame**: Marco contenedor de otros widgets. Puede tener tamaño propio y posicionarse en distintos lugares de otro contenedor (ya sea la raíz u otro marco).
* **Label**: Etiqueta dónde podemos mostrar algún texto estático.
* **Entry**: Campo de texto sencillo para escribir texto corto. Nombres, apellidos, números..
* **Text**: Campo de texto multilínea para escribir texto largo. Descripciones, comentarios...
* **Button**: Botón con un texto sobre el cual el usuario puede hacer clic.
* **Radiobutton**: Botón radial que se usa en conjunto donde es posible marcar una opción.
* **Checkbutton**: Botón cuadrado que se puede marcar con un tic.
* **Menu**: Estructura de botones centrados en la composición de menús superiores.
* **Dialogs**: Ventanas emergentes que permiten desde mostrar información al usuario (típico mensaje de alerta o de confirmación) hasta ofrecer una forma gráfica de interactuar con el sistema operativo (seleccionar un fichero de un directorio para abrirlo).
    
Hay otros widgets, pero estos son los más importantes.

___
<small class="edited"><i>Última edición: 4 de Octubre de 2018</i></small>