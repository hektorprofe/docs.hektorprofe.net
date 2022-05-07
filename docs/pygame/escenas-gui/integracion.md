title: Ejemplo de integración | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Ejemplo de integración

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


"""gui.py"""
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
import sys
import pygame as pg
import pygame_gui as pgg
from entities import Player
from settings import *


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
        self.manager = pgg.UIManager(
            (WIDTH, HEIGHT), theme_path='res/themes/custom.json')

        self.play_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 100), (200, 50)),
            text='JUGAR', manager=self.manager)

        self.credits_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 175), (200, 50)),
            text='CREDITOS', manager=self.manager)

        self.exit_button = pgg.elements.UIButton(
            relative_rect=pg.Rect((400, 250), (200, 50)),
            text='SALIR', manager=self.manager)

    def events(self, events):
        for event in events:
            self.manager.process_events(event)
            if event.type == pgg.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.game.change_scene(MainScene(self.game))
                if event.ui_element == self.credits_button:
                    print("ESCENA DE CRÉDITOS")
                if event.ui_element == self.exit_button:
                    sys.exit()

    def update(self, dt):
        self.manager.update(dt)

    def draw(self, display):
        display.fill((0, 0, 0))
        self.manager.draw_ui(display)


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