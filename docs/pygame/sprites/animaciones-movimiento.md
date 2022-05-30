title: Animaciones en movimiento | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Animaciones en movimiento

![]({{cdn}}/pygame/023.gif)

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

        self.boy_down = [pg.image.load(
            f"boy/down_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_up = [pg.image.load(
            f"boy/up_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_left = [pg.image.load(
            f"boy/left_{i}.png").convert_alpha() for i in range(1, 5)]
        self.boy_right = [pg.image.load(
            f"boy/right_{i}.png").convert_alpha() for i in range(1, 5)]

        self.animation = self.boy_down
        self.animation_sprite = 0
        self.animation_speed = 6

        self.image = self.animation[self.animation_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Position, movement and flip config
        self.position = pg.Vector2(x, y)
        self.horizontal_speed = 175
        self.vertical_speed = 100

    def update(self, dt):
        # Input
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

        # Animate sprite
        if self.position == prev_position:
            self.animation_sprite = 0
        else:
            self.animation_sprite += self.animation_speed * dt
            if self.animation_sprite >= len(self.animation):
                self.animation_sprite = 0

        # Set image and flip if needed
        self.image = self.animation[int(self.animation_sprite)]

        # Update position
        self.rect = int(self.position.x), int(self.position.y)


common_group = pg.sprite.Group()
common_group.add(Player(325, 150))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    dt = clock.tick(FPS) / 1000
    common_group.update(dt)
    display.blit(background, (0, 0))
    common_group.draw(display)
    pg.display.update()
```

**Adjuntos**

* [grass.png]({{cdn}}/pygame/grass.png)
* [boy.zip]({{cdn}}/pygame/boy.zip)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>