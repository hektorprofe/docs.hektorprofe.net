title: Creación de la superficie | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Creación de la superficie

![]({{cdn}}/pygame/001.png)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hola PyGame")

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
```

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>