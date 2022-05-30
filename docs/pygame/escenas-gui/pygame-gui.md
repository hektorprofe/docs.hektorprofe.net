title: PyGame GUI | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# PyGame GUI

![]({{cdn}}/pygame/029.gif)

Instalación del módulo:

```bash
pip install pygame_gui
```

Ejemplo:

`main.py`

```python
import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Say Hello',
    manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
```

Es buena idea después de realizar la práctica echar un vistazo a algunos ejemplos del [repositorio](https://github.com/MyreMylar/pygame_gui_examples).

Por orden:

- `quick_start.py`
- `button_theming_test.py`
- `documentation_test.py`
- `layout_anchor_test.py`
- `text_test.py`

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>