title: Adaptando un ejemplo | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Adaptando un ejemplo

```python
"""player.py"""
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        # Updated resource paths
        self.boy_down = [pg.image.load(
            f"res/images/boy/down_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_up = [pg.image.load(
            f"res/images/boy/up_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_left = [pg.image.load(
            f"res/images/boy/left_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_right = [pg.image.load(
            f"res/images/boy/right_{i}.png").convert_alpha() for i in range(1, 5)]

        self.animation = self.boy_down
        self.animation_sprite = 0
        self.animation_speed = 6

        self.image = self.animation[self.animation_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.position = pg.Vector2(x, y)
        self.horizontal_speed = 175
        self.vertical_speed = 100

    def update(self, dt):
        keys = pg.key.get_pressed()

        prev_position = self.position.copy()

        if keys[pg.K_LEFT]:
            self.animation = self.boy_left
            self.position.x -= self.horizontal_speed * dt
        elif keys[pg.K_RIGHT]:
            self.animation = self.boy_right
            self.position.x += self.horizontal_speed * dt
        if keys[pg.K_UP]:
            self.animation = self.boy_up
            self.position.y -= self.vertical_speed * dt
        elif keys[pg.K_DOWN]:
            self.animation = self.boy_down
            self.position.y += self.vertical_speed * dt

        if self.position == prev_position:
            self.animation_sprite = 0
        else:
            self.animation_sprite += self.animation_speed * dt
            if self.animation_sprite >= len(self.animation):
                self.animation_sprite = 0

        self.image = self.animation[int(self.animation_sprite)]

        self.rect = int(self.position.x), int(self.position.y)

"""main.py"""
import sys
import pygame as pg

from settings import *
from entities import Player


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.display = pg.display.set_mode((WIDTH, HEIGTH))
        self.clock = pg.time.Clock()
        self.background = pg.image.load(
            "res/images/background/grass.png").convert_alpha()
        self.common_group = pg.sprite.Group()
        self.common_group.add(Player(325, 150))

    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            dt = self.clock.tick(FPS) / 1000
            self.common_group.update(dt)
            self.display.blit(self.background, (0, 0))
            self.common_group.draw(self.display)
            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
```



___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>