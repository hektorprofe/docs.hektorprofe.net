title: Múltiples botones | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Múltiples botones

![]({{cdn}}/pygame/028.gif)

Continuación de la lección anterior:

`gui.py`

```python
import pygame as pg


class Button:
    def __init__(self, x=0, y=0, text="", width=200, height=50, elev=6):
        self.font = pg.font.Font('res/fonts/04B03.ttf', 24)
        self.text = self.font.render(text, True, "#ffffff")
        self.text_rect = self.text.get_rect()

        self.bottom_rect = pg.Rect((x+elev, y+elev), (width, height))
        self.top_rect = pg.Rect((x, y), (width, height))
        self.text_rect.center = self.top_rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False

    def update(self):
        # Siempre supondremos que el botón no está clicado
        self.clicked = False
        # Luego comprobaremos si estamos encima
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.hover = True
            # Si presionamos mientras estamoas sobre el botón
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                # Si dejamos de presionar mientras estamos sobre el botón
                if self.pressed is True:
                    self.pressed = False
                    self.clicked = True
                    # print("Botón clicado")
        else:
            self.pressed = False
            self.hover = False

    def draw(self, display):
        top_rect_color = "#317bcf" if self.hover else "#3194cf"
        if not self.pressed:
            # Si no pulsamos dibujamos todo en su posición original
            pg.draw.rect(display, "#1a232e", self.bottom_rect)
            pg.draw.rect(display, top_rect_color, self.top_rect)
            self.text_rect.center = self.top_rect.center
        else:
            # Si pulsamos cambiamos la posición de dibujado abajo
            pg.draw.rect(display, top_rect_color, self.bottom_rect)
            self.text_rect.center = self.bottom_rect.center
        display.blit(self.text, self.text_rect)
```

`scenes.py`

```python
import sys
import pygame as pg

from gui import Button
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


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.button_play = Button(400, 100, "JUGAR")
        self.button_credits = Button(400, 175, "CREDITOS")
        self.button_exit = Button(400, 250, "SALIR")

    def events(self, events):
        if self.button_play.clicked:
            self.game.change_scene(MainScene(self.game))
        if self.button_credits.clicked:
            print("ESCENA DE CRÉDITOS")
        if self.button_exit.clicked:
            sys.exit()

    def update(self, dt):
        self.button_play.update()
        self.button_credits.update()
        self.button_exit.update()

    def draw(self, display):
        display.fill((0, 0, 0))
        self.button_play.draw(display)
        self.button_credits.draw(display)
        self.button_exit.draw(display)


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
```

**Adjuntos**

* [04B03.ttf]({{cdn}}/pygame/04B03.ttf)
* [grass.png]({{cdn}}/pygame/grass.png)
* [boy.zip]({{cdn}}/pygame/boy.zip)


___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>