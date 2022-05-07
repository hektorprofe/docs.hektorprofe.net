title: Estructura principal | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Estructura principal

```python
"""requirements.txt"""
pygame==2.1.2

"""settings.py"""
CAPTION = "My videogame"
WIDTH = 720
HEIGHT = 400
FPS = 60

""" main.py """
import sys
import pygame as pg

from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.display = pg.display.set_mode((WIDTH, HEIGTH))
        self.clock = pg.time.Clock()

    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            dt = self.clock.tick(FPS) / 1000
            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
```


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>