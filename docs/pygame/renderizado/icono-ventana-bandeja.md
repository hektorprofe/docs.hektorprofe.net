title: Iconos de ventana y bandeja | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Iconos de ventana y bandeja

![]({{cdn}}/pygame/006.png)

```python
import os
import ctypes
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400

pg.init()

# Esta parte de los iconos se configura antes del display.set_mode
# Configurar el icono 32x32 en el borde de ventana
pg.display.set_icon(pg.image.load('python.png'))
# Para Windows el icono del taskbar requiere un appid único en el programa
if os.name == 'nt':
    appid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

display = pg.display.set_mode((WIDTH, HEIGHT))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
```

**Adjuntos**

* [python.png]({{cdn}}/pygame/python.png)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>