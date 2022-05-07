title: Clase sprite y grupos | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Clase sprite y grupos

```python
import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
FPS = 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
clock = pg.time.Clock()


class Mushroom(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, auto=False):
        super().__init__()
        self.image = pg.image.load("mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        if auto:
            self.rect.x = random.randint(0, WIDTH - self.image.get_size()[0])
            self.rect.y = random.randint(0, HEIGHT - self.image.get_size()[1])


mushroom_group = pg.sprite.Group()
mushroom = Mushroom(50, 50)
mushroom_group.add(mushroom)
mushroom_group.add(Mushroom(100, 100))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                mushroom_group.add(Mushroom(auto=True))
            if event.key == pg.K_z:
                mushroom_group.empty()
    clock.tick(FPS)
    display.blit(background, (0, 0))
    mushroom_group.draw(display)
    pg.display.update()
```



___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>