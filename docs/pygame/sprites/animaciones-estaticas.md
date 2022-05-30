title: Animaciones estáticas | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Animaciones estáticas

![]({{cdn}}/pygame/022.gif)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
FPS = 60

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        # Sprites and animation config
        self.boxer_idle = [pg.image.load(
            f"boxer/idle{i}.png").convert_alpha() for i in range(1, 11)]
        self.boxer_left_punch = [pg.image.load(
            f"boxer/punchl{i}.png").convert_alpha() for i in range(1, 7)]
        self.boxer_right_punch = [pg.image.load(
            f"boxer/punchr{i}.png").convert_alpha() for i in range(1, 7)]

        self.animation = self.boxer_idle
        self.animation_sprite = 0
        self.animation_speed = 16  # Frames per second

        self.image = self.animation[self.animation_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, dt):
        self.animation_sprite += self.animation_speed * dt
        if self.animation_sprite >= len(self.animation):
            self.animation_sprite = 0
            # Volvemos a la animación idle cuando las otras acaban
            if self.animation != self.boxer_idle:
                self.animation = self.boxer_idle

        self.image = self.animation[int(self.animation_sprite)]

    def attack_left_punch(self):
        self.animation = self.boxer_left_punch
        self.animation_sprite = 0

    def attack_right_punch(self):
        self.animation = self.boxer_right_punch
        self.animation_sprite = 0


common_group = pg.sprite.Group()

player = Player(190, 50)
common_group.add(player)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                player.attack_right_punch()
            if event.key == pg.K_z:
                player.attack_left_punch()
    dt = clock.tick(FPS) / 1000
    common_group.update(dt)
    display.blit(background, (0, 0))
    common_group.draw(display)
    pg.display.update()
```

**Adjuntos**

* [grass.png]({{cdn}}/pygame/grass.png)
* [boxer.zip]({{cdn}}/pygame/boxer.zip)

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>