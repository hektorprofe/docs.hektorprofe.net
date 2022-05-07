title: Gestor de escenas | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Gestor de escenas

PyGame no ofrece una forma de manejar diferentes escenas, así que os voy a enseñar a desarrollar vuestro propio gestor de escenas.

```python
"""scenes.py"""
import pygame as pg
from settings import *
from entities import Player


class Scene:
    def __init__(self, game):
        self.game = game

    def events(self, events):
        raise NotImplementedError("events must be defined")

    def update(self, dt):
        raise NotImplementedError("update must be defined")

    def draw(self, display):
        raise NotImplementedError("draw must be defined")


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = pg.image.load("res/images/grass.png").convert_alpha()
        self.common_group = pg.sprite.Group()
        self.common_group.add(Player(325, 150))

    def events(self, events):
        pass

    def update(self, dt):
        self.common_group.update(dt)

    def draw(self, display):
        display.blit(self.background, (0, 0))
        self.common_group.draw(display)


"""main.py"""
from settings import *
from entities import Player
from scenes import MainScene

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.scene = MainScene(self)            # Scene

    def run(self):
        while 1:
            dt = self.clock.tick(FPS) / 1000
            ev = pg.event.get()                 # new
            for event in ev:                    # edited
                if event.type == pg.QUIT:
                    sys.exit()
            # Scene events
            self.scene.events(ev)
            self.scene.update(dt)
            self.scene.draw(self.display)
            pg.display.update()

    def change_scene(self, scene):
        self.scene = scene


if __name__ == '__main__':
    game = Game()
    game.run()
```



___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>