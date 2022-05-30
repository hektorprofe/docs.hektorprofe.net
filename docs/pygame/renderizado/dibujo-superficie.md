title: Dibujando en la superficie | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Dibujando en la superficie

![]({{cdn}}/pygame/002.png)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
BACKGROUND = (13, 17, 23)

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
display.fill(BACKGROUND)

pg.draw.line(display, (255, 0, 0), (50, 50), (150, 150), 3)
pg.draw.rect(display, (0, 255, 255), (550, 50, 100, 100))
pg.draw.circle(display, (255, 255, 255), (400, 250), 100, 10)
pg.draw.ellipse(display, (0, 255, 0), (75, 225, 150, 100))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
```

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>