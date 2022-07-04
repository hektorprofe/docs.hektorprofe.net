title: Cambio de escena | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Cambio de escena

![]({{cdn}}/pygame/024.gif)

Continuación de la lección anterior:

`scenes.py`

```python
class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pg.font.SysFont('Verdana', 48)

    def events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.game.change_scene(MainScene(self.game))

    def update(self, dt):
        self.text = self.font.render("PULSA ENTER", True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH/2, HEIGHT/2)

    def draw(self, display):
        display.fill((0, 0, 0))
        display.blit(self.text, self.text_rect)

class MainScene(Scene):
    def events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.game.change_scene(MenuScene(self.game))
```

`main.py`
```python
from scenes import MenuScene

class Game:
    def __init__(self):
        # ...
        self.scene = MenuScene(self)
```

**Adjuntos**

* [grass.png]({{cdn}}/pygame/grass.png)
* [boy.zip]({{cdn}}/pygame/boy.zip)

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>