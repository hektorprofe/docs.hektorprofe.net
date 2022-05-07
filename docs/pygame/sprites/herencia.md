title: Repaso de la herencia | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Repaso de la herencia

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


class Coche(Vehiculo):

    def __init__(self, color, vel, cc):
        # self.color, self.vel, self.cc = color, vel, cc

        # super(Coche, self).__init__(color)
        super().__init__(color)
        self.vel, self.cc = vel, cc

    def __str__(self):
        return f"Coche {self.color}, {self.vel} km/h, {self.cc} cc"


coche = Coche("azul", 150, 1200)
coche.info()


class Camioneta(Coche):

    def __init__(self, color, vel, cc, carga):
        super().__init__(color, vel, cc)
        self.carga = carga

    def __str__(self):
        return f"Camioneta {self.color}, {self.vel} km/h, " \
            f"{self.cc} cc, {self.carga} kg de carga"


camioneta = Camioneta("blanca", 100, 1500, 1200)
camioneta.info()
```



___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>