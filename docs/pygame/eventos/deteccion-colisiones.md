title: Detección de colisiones | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Detección de colisiones

![]({{cdn}}/pygame/011.gif)

```python
import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 5, 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
dino_image = pg.image.load("dino.png").convert_alpha()
dino_rect = dino_image.get_rect()
star_image = pg.image.load("star.png").convert_alpha()
star_rect = star_image.get_rect()
star_rect.center = (WIDTH//2, HEIGHT//2)
clock = pg.time.Clock()


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and dino_rect.left > 0:
        dino_rect.x -= SPEED
    if keys[pg.K_RIGHT] and dino_rect.right < WIDTH:
        dino_rect.x += SPEED
    if keys[pg.K_UP] and dino_rect.top > 0:
        dino_rect.y -= SPEED
    if keys[pg.K_DOWN] and dino_rect.bottom < HEIGHT:
        dino_rect.y += SPEED

    if dino_rect.colliderect(star_rect):
        star_rect.x = random.randint(50, WIDTH - 50)
        star_rect.y = random.randint(50, HEIGHT - 50)
        print("COLISION")

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)
    display.blit(star_image, star_rect)

    pg.display.update()
```

**Adjuntos**

* [dino.png]({{cdn}}/pygame/dino.png)
* [grass.png]({{cdn}}/pygame/grass.png)
* [star.png]({{cdn}}/pygame/star.png)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>