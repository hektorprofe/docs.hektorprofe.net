title: Blitting de Imágenes (copia) | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Blitting de Imágenes (copia) 

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
BACKGROUND = (13, 17, 23)

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
dino_image = pg.image.load("dino.png").convert_alpha()
# If you don't call convert, every time you blit a surface to your display
# surface, a pixel conversion will be needed -this is a per pixel operation,
# very slow- instead of a series of memory copies.
dino_rect = dino_image.get_rect()
dino_rect.topleft = (300, 150)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.fill(BACKGROUND)
    display.blit(dino_image, dino_rect)

    pg.display.update()
```
___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>