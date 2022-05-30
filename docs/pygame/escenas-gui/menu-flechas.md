title: Menú con flechas | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Menú con flechas

![]({{cdn}}/pygame/025.gif)

Continuación de la lección anterior:

`scenes.py`

```cpp
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

        self.option = 0

    def events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if self.option % 3 == 0:
                        self.game.change_scene(MainScene(self.game))
                    elif self.option % 3 == 1:
                        print("ESCENA DE CRÉDITOS")
                    elif self.option % 3 == 2:
                        sys.exit()
                if event.key == pg.K_DOWN:
                    self.option += 1
                if event.key == pg.K_UP:
                    self.option -= 1

    def update(self, dt):
        pass

    def draw(self, display):
        display.fill((0, 0, 0))
        display.blit(self.text_play, self.text_play_rect)
        display.blit(self.text_credits, self.text_credits_rect)
        display.blit(self.text_exit, self.text_exit_rect)

        # display.blit(self.text_option, (360, 100))
        display.blit(self.text_option, (360, 100 + self.option % 3 * 75))


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