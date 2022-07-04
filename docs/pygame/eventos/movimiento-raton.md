title: Movimiento de ratón | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Movimiento de ratón

![]({{cdn}}/pygame/007.gif)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
dino_image = pg.image.load("dino.png").convert_alpha()
dino_rect = dino_image.get_rect()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:  # print(event)
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN or \
                (event.type == pg.MOUSEMOTION and event.buttons[0] == 1):
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dino_rect.centerx = mouse_x
            dino_rect.centery = mouse_y

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)

    pg.display.update()
```

**Adjuntos**

* [dino.png]({{cdn}}/pygame/dino.png)
* [grass.png]({{cdn}}/pygame/grass.png)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>