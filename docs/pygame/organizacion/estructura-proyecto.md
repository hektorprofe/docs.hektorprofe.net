title: Estructura de un proyecto | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Estructura de un proyecto

De acuerdo al handbook [The Hitchiker's Guide to Python](https://docs.python-guide.org/writing/structure/) una forma recomendable de organizar de nuestros proyectos podría ser la siguiente:

```
Game/
    requirements.txt    # dependencias
    LICENSE             # optativo
    README.md           # optativo
    .gitignore          # optativo
    game/
        main.py         # principal
        settings.py     # configuración
        entities.py     # entidades
        res/            # recursos
            images/
            audios/
            fonts/
            maps/
```

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>