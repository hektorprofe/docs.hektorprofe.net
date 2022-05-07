title: Menú clicable | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Menú clicable

```python
"""entities.py"""
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

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
from scenes import MenuScene


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.scene = MenuScene(self)

    def run(self):
        while 1:
            dt = self.clock.tick(FPS) / 1000
            ev = pg.event.get()
            for event in ev:
                if event.type == pg.QUIT:
                    sys.exit()
            self.scene.events(ev)
            self.scene.update(dt)
            self.scene.draw(self.display)
            pg.display.update()

    def change_scene(self, scene):
        self.scene = scene


if __name__ == '__main__':
    game = Game()
    game.run()

"""scenes.py"""
from entities import Player
import pygame as pg
import sys


class Scene:
    def __init__(self, game):
        self.game = game

    def events(self, events):
        raise NotImplementedError("events must be defined")

    def update(self, dt):
        raise NotImplementedError("update must be defined")

    def draw(self, display):
        raise NotImplementedError("draw must be defined")


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pg.font.Font('res/fonts/04B03.ttf', 48)

        self.text_play = self.font.render("JUGAR", True, (255, 255, 255))
        self.text_play_rect = self.text_play.get_rect()
        self.text_play_rect.topleft = (400, 100)

        self.text_credits = self.font.render("CREDITOS", True, (255, 255, 255))
        self.text_credits_rect = self.text_credits.get_rect()
        self.text_credits_rect.topleft = (400, 175)

        self.text_exit = self.font.render("SALIR", True, (255, 255, 255))
        self.text_exit_rect = self.text_exit.get_rect()
        self.text_exit_rect.topleft = (400, 250)

        self.text_option = self.font.render(">", True, (255, 255, 255))
        self.text_option_rect = self.text_option.get_rect()

        self.option = -1

    def events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.option == 0:
                    # El cambio de cursor común mejor en Game.change_scene
                    # pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                    self.game.change_scene(MainScene(self.game))
                elif self.option == 1:
                    print("ESCENA DE CRÉDITOS")
                elif self.option == 2:
                    sys.exit()

    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()

        if self.text_play_rect.collidepoint(mouse_pos):
            self.text_option_rect.topleft = (360, 100)
            self.option = 0
        elif self.text_credits_rect.collidepoint(mouse_pos):
            self.text_option_rect.topleft = (360, 175)
            self.option = 1
        elif self.text_exit_rect.collidepoint(mouse_pos):
            self.text_option_rect.topleft = (360, 250)
            self.option = 2
        else:
            self.option = -1

    def draw(self, display):
        display.fill((0, 0, 0))
        display.blit(self.text_play, self.text_play_rect)
        display.blit(self.text_credits, self.text_credits_rect)
        display.blit(self.text_exit, self.text_exit_rect)

        if self.option >= 0:
            display.blit(self.text_option, self.text_option_rect)


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("res/images/grass.png").convert_alpha()
        self.common_group = pg.sprite.Group()
        self.common_group.add(Player(325, 150))

    def events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game.change_scene(MenuScene(self.game))

    def update(self, dt):
        self.common_group.update(dt)

    def draw(self, display):
        display.blit(self.background, (0, 0))
        self.common_group.draw(display)

"""settings.py"""
CAPTION = "My videogame"
WIDTH = 720
HEIGHT = 400
FPS = 60
```


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>