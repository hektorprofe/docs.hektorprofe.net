title: Movimiento de teclado discreto | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Movimiento de teclado discreto

![]({{cdn}}/pygame/008.gif)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 50, 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
dino_image = pg.image.load("dino.png").convert_alpha()
dino_rect = dino_image.get_rect()

while 1:
    for event in pg.event.get():  # print(event)
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dino_rect.x -= SPEED
            if event.key == pg.K_RIGHT:
                dino_rect.x += SPEED
            if event.key == pg.K_UP:
                dino_rect.y -= SPEED
            if event.key == pg.K_DOWN:
                dino_rect.y += SPEED

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)

    pg.display.update()
```

**Adjuntos**

* [grass.png]({{cdn}}/pygame/grass.png)
* [dino.png]({{cdn}}/pygame/dino.png)

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>