title: Actualización por fotograma | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Actualización por fotograma

![]({{cdn}}/pygame/018.gif)

```python
import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
FPS = 5

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
clock = pg.time.Clock()


class Mushroom(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, speed=0, auto=False):
        super().__init__()
        self.image = pg.image.load("mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

        if auto:
            self.rect.x = random.randint(0, WIDTH - self.image.get_size()[0])
            self.rect.y = random.randint(0, HEIGHT - self.image.get_size()[1])
            self.speed = random.randint(1, 5)

    def update(self):
        # Movimiento dependiente de los fotogramas por segundo
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.rect.x = 0


mushroom_group = pg.sprite.Group()
mushroom = Mushroom(50, 50, 3)  # 3 píxeles por fotograma
mushroom_group.add(mushroom)
mushroom_group.add(Mushroom(100, 100, 2))

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
    mushroom_group.update()
    mushroom_group.draw(display)
    pg.display.update()
```

**Adjuntos**

* [grass.png]({{cdn}}/pygame/grass.png)
* [mushroom.png]({{cdn}}/pygame/mushroom.png)

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>