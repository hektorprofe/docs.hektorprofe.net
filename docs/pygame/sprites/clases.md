title: Repaso de las clases | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Repaso de las clases

```python
class Vehiculo(object):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Vehículo {self.color}"

    def info(self):
        print(self)


vehiculo = Vehiculo("rojo")
vehiculo.info()
```



___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>