title: Primer diseño en Qt Designer | Curso Qt/PySide | Hektor Profe

# Primer diseño en Qt Designer

Muy bien, pues vamos a diseñar nuestra primera interfaz. Si tenemos el directorio de PySide6 en el PATH del sistema podemos abrir el programa escribiendo:

```bash
designer
```

## Primer formulario

Lo primero es seleccionar qué tipo de formulario crear, vamos a crear una ventana principal `Main Window`.

- En el centro tenemos la vista de diseño con la ventana principal.
- A la izquierda tenemos la caja de Widgets.
- Arriba el control de elementos y disposiciones.
- A la derecha encontramos de arriba a abajo:
  - El inspector de objetos en una vista jerárquica.
  - El editor de propiedades del componente seleccionado.
  - Y el navegador de recursos del programa.

## Personalizar la ventana

Vamos a empezar a personalizar la ventana usando algunas propiedades:

- `geometry`: 480 ancho y 320 alto
- `windowTitle`: Primer diseño

Ahora vamos a crear un conjunto de recursos para utilizarlos en el programa.

- Hacemos clic en el `lápiz` del navegador de recursos.
- En la columna izquierda clic derecho > `Nuevo`.
- En el directorio de la aplicación guardamos el fichero con el nombre `recursos`.
- Con `resources.qrc` seleccionado, clic derecho en la columna derecha > Nuevo prefijo.
- Le damos por ejemplo el nombre `iconos`, clic derecho `Añadir archivos`.
- Buscamos un icono png para ponerlo en nuestra ventan, lo añadimos y aceptamos.

<img src="{{cdn}}/pyside/09-docs/01.png">

- `windowIcon`: Desplegamos, "Elija recurso" y seleccionamos el icono.

* Guardamos el diseño `Control+S` con nombre `mainwindow.ui` en un directorio llamado, por ejemplo `interfaces`.

- Presionamos `Control+R` para ver una previsualización de la ventana principal.

## Componentes y disposiciones

Vamos a añadir algunos elementos:

- `Label`: Introduce un texto
- `LineEdit`
- `PushButton`: Enviar

Veréis que no quedan muy bien dispuestos, eso es porque nuestra ventana no tiene un layout establecido.

<img src="{{cdn}}/pyside/09-docs/02.png">

Con la ventana seleccionada hacemos clic en el layout vertical de la barra superior, automáticamente los elementos se posicionarán siguiendo esta disposición:

<img src="{{cdn}}/pyside/09-docs/03.png">

Automáticamente se creará un dummy widget con un layout para el `centralWidget` y los componentes se posicionarán automáticamente. Además ahora encontraremos un nuevo apartado `Layout`en las propiedades del objeto `centralWidget` donde podemos cambiar su configuración.

Sin embargo veréis que nuestros elementos se posicionan raro porque la etiqueta se expande por defecto.

Para solucionar esto vamos a añadir abajo del todo un widget `Vertical Spacer`:

<img src="{{cdn}}/pyside/09-docs/04.png">

Como podéis suponer los `Spacers` rellenan automáticamente el espacio sobrante de un layout.

Podemos probar otras disposiciones hasta encontrar una que nos guste y utilizar el botón `Ajuste de tamaño` para redimensionar el tamaño de la ventana acordemente a su contenido:

<img src="{{cdn}}/pyside/09-docs/05.png">

Otra cosa importante es que las ventanas principales vienen con su `menuBar` y `statusBar` ya creadas.

Podemos agregar campos al menú superior simplemente escribiendo ahí. Luego podemos gestionar las acciones mediante el inspector de objetos y de propiedades. Cualquier cosa que debáis configurar de un widget la encontraréis ahí, por ejemplo podemos añadir un acceso directo al botón de &Salir del menú:

<img src="{{cdn}}/pyside/09-docs/06.png">

Y añadir una imagen al botón de salir, siempre que préviamente la añadamos a nuestros recursos:

<img src="{{cdn}}/pyside/09-docs/07.png">

Si añadimos `statusTips` a nuestros componentes, se mostrarán automáticamente en el previsualizador:

<img src="{{cdn}}/pyside/09-docs/08.png">

También podemos cambiar los estilos del programa haciendo clic derecho en el objeto `MainWindow` del inspector y con la opción `Cambiar Hoja de Estilos`.

Se abrirá un formulario donde podemos pegar todo el contenido de nuestro fichero QSS tradicional:

<img src="{{cdn}}/pyside/09-docs/09.png">

Y creo que ya hemos visto todos los conceptos clave.

En el segundo bloque del curso diseñaremos algunos programas, pero el mejor maestro es la práctica. Os aconsejo perderos un rato probando layouts, widgets y cambiando sus propiedades para aprender por vuestra cuenta.

En la próxima lección vamos a transformar este diseño en un fichero Python para empezar a trabajar con él.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>