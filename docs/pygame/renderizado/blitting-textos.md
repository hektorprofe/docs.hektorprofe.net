title: Blitting de Textos (copia) | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Blitting de Textos (copia)

![]({{cdn}}/pygame/004.png)

```python
import sys
import pygame as pg

WIDTH, HEIGHT = 720, 400
BACKGROUND, BLUE, DARKBLUE = (13, 17, 23), (0, 125, 255), (10, 25, 50)

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))

# fonts = pg.font.get_fonts()
# for font in fonts:
#     print(font)

system_font = pg.font.SysFont('Verdana', 64)
system_text = system_font.render("Hola Mundo", True, BLUE, DARKBLUE)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WIDTH//2, HEIGHT//2 - 50)

custom_font = pg.font.Font('04B03.ttf', 48)
custom_text = custom_font.render("Hola Mundo", True, BLUE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WIDTH//2, HEIGHT//2 + 50)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.fill(BACKGROUND)
    display.blit(system_text, system_text_rect)
    display.blit(custom_text, custom_text_rect)

    pg.display.update()
```

**Adjuntos**

* [04B03.ttf]({{cdn}}/pygame/04B03.ttf)

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>