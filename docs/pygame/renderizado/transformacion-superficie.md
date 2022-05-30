title: Transformación de superficies | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Transformación de superficies

![]({{cdn}}/pygame/005.png)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
BACKGROUND = (13, 17, 23)

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
dino_image = pg.image.load("dino.png").convert_alpha()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.fill(BACKGROUND)
    display.blit(dino_image, (0, 100))  # imagen por defecto

    dino_flipped = pg.transform.flip(dino_image, True, True)
    display.blit(dino_flipped, (100, 100))  # imagen volteada H y V

    dino_scaled = pg.transform.scale(dino_image, (100, 50))
    display.blit(dino_scaled, (200, 100))  # imagen esclada a 100 x 25 px

    dino_scaled = pg.transform.scale(dino_image, (50, 100))
    display.blit(dino_scaled, (300, 100))  # imagen esclada a 25 x 100 px

    dino_rotated = pg.transform.rotate(dino_image, 45)
    display.blit(dino_rotated, (350, 100))  # imagen esclada a 25 x 100 px

    dino_rotozoomed = pg.transform.rotozoom(dino_image, 90, 2)
    display.blit(dino_rotozoomed, (500, 100))  # imagen esclada a 25 x 100 px

    pg.display.update()
```

**Adjuntos**

* [dino.png]({{cdn}}/pygame/dino.png)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>