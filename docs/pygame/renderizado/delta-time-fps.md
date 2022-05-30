title: Delta time y FPS | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Delta time y FPS

![]({{cdn}}/pygame/006.gif)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
BACKGROUND, WHITE = (13, 17, 23), (255, 255, 255)
FPS = 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont('Verdana', 16)

while 1:
    dt = clock.tick(FPS)  # clock.tick(0) sin límite
    fps = clock.get_fps()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.fill(BACKGROUND)

    dt_text = font.render(f"Delta time: {dt} ms", True, WHITE)
    fps_text = font.render(f"Frames per second: {fps}", True, WHITE)
    display.blit(dt_text, (50, 50))
    display.blit(fps_text, (50, 75))

    pg.display.update()
```

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>