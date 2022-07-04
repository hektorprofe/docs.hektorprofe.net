title: Pyinstaller | Curso de Python | Hektor Profe
description: Se conoce como distribución a la etapa final del código, cuando éste se distribuye o comparte con otras personas.

<style>
.md-footer-nav__link--next{
    display: none;
}

.admonition.note > .superfences-tabs > label:hover, .headerlink{
    color: #018dc5 !important;
}

.admonition.info{
    font-size: 100%;
}

.admonition.info label{
    font-size: 91%;
}

.admonition.note > .admonition-title {
    display: none;
}

</style>

# Pyinstaller

Ya hemos visto como distribuir nuestros paquetes... ¿Pero y si creamos una aplicación y queremos generar un ejecutable para utilizarla? Bueno, en este caso puede ser bastante complicado dependiendo de las dependencias que utilice el programa. 

Por suerte hay un módulo que nos ayudará mucho a generar ejecutables porque automatiza el proceso, ese es **pyinstaller**.

Lo que hace es generar un .EXE en Windows, un .DMG en MAC o el ejecutable que utilice el sistema operativo. Dentro del ejecutable se incluye el propio intérprete de Python, y por esa razón podremos utilizarlo en cualquier ordenador sin necesidad de instalar Python previamente.

## Instalación

La instalación es muy fácil:
```
pip install pyinstaller
```
No hay más.

## Primer ejecutable

Comencemos con algo simple, tenemos un script **hola.py**:
```python
print("Hola mundo!")
```
Y queremos crear un ejecutable a partir de él, pues haríamos lo siguiente:
```
pyinstaller hola.py
```
Una vez acabe el proceso se nos habrán creado varias carpetas. La que nos interesa es **dist**, y dentro encontraremos una carpeta con el nombre programa y en esta un montón de ficheros y el ejecutable, en mi caso como estoy en Windows es **hola.exe**.

Como es un programa para terminal, para ejecutarlo tengo que abrir la terminal en ese directorio y ejecutar el programa manualmente:

```
C:\Users\Hector\Desktop\hola\dist\hola>hola.exe
Hola mundo!
```

## Ejecutable con interfaz

Ahora vamos a hacer otro a partir de un simple programa con Tkinter, la librería de componentes integrada en Python que ya conocemos. Nos debería funcionar sin problemas:

```python
from tkinter import *

root = Tk()
Label(text='Hola mundo').pack(pady=10)
root.mainloop()
```
Suponiendo que lo hemos puesto en el mismo script:

```
pyinstaller hola.py
```
En esta ocasión si ejecutamos el programa con doble clic nos funcionará bien, el problema es que se muestra la terminal de fondo.

Para que desaparezca tenemos que indicar que es una aplicación en ventana, y eso lo hacemos de la siguiente forma al crear el ejecutable:

```
pyinstaller --windowed hola.py
```

## Ejecutable en un fichero

Ya véis que por defecto Pyinstaller crea un directorio con un montón de ficheros. Podemos utilizar un comando para generar un solo fichero ejecutable que lo contenga todo, pero este ocupara bastante más:

```
pyinstaller --windowed --onefile hola.py
```

## Cambiar el icono

También podemos cambiar el icono por defecto del ejecutable. Para ello necesitamos una imagen en formato .ico.

```
pyinstaller --windowed --onefile --icon=./hola.ico hola.py
```

Si por algo no os cambia el icono, probad cambiando el nombre del ejecutable. A veces el caché de Windows puede ignorar estas cosas.

## Limitaciones

El gran problema con Pyinstaller como os decía al principio son las dependencias. 

Si nuestro programa utiliza únicamente módulos de la librería estándard no tendremos ningún problema, pero si queremos utilizar módulos externos es posible que no funcione... A no ser que sea alguno de los soportados como PyQT, django, pandas, matpotlib... pero requieren una configuraciones extra.

Si queréis saber más os dejo [este enlace con los paquetes soportados](https://github.com/pyinstaller/pyinstaller/wiki/Supported-Packages).

___
<small class="edited"><i>Última edición: 9 de Noviembre de 2018</i></small>