title: Campos numéricos QSpinBox y QDoubleSpinBox | Curso Qt/PySide | Hektor Profe

# Campos numéricos QSpinBox y QDoubleSpinBox

<img src="{{cdn}}/pyside/12.png">

A diferencia de los campos de texto, los numéricos fuerzan al usuario a escribir números y proveen métodos para su control. Encontramos para almacenar enteros y decimales, empecemos por los enteros:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un campo numérico entero
        numero = QSpinBox()
        self.setCentralWidget(numero)

        # Probamos algunas opciones
        numero.setMinimum(0)
        numero.setMaximum(10)
        numero.setRange(0, 10)
        numero.setSingleStep(1)

        # Probamos algunas señales
        numero.valueChanged.connect(self.valor_cambiado)

    def valor_cambiado(self, numero):
        # al presionar enter recuperamos el texto a partir del widget central
        print("Valor cambiado ->", numero)
```

Los campos numéricos permiten establecer prefijos y sufijos, útiles para manejar monedas y medidas:

```python
numero.setPrefix("$")
numero.setSuffix("%")
```

En cuanto a los decimales son exactamente lo mismo pero utilizando el widget `QDoubleSpinBox`:

- `QSpinBox` -> `QDoubleSpinBox`
- `numero = QSpinBox()` -> `numero = QDoubleSpinBox()`
- `numero.setSingleStep(1)` -> `numero.setSingleStep(0.5)`

En ambos widgets podemos establecer un valor por defecto con el método `setValue` y recuperarlo con `value`:

```python
# Establecer y recuperar el valor
numero.setValue(3.14)
print(numero.value())
```

<img src="{{cdn}}/pyside/11.png">

Con esto acabamos el repaso de los widgets básicos para formularios.

Existen muchos otros widgets para realizar todo tipo de tareas. Descubriremos algunos de ellos más adelante, pero si queréis una referencia completa lo mejor es buscar en la [documentación de qt](https://doc.qt.io/qt-6/qwidget.html) las clases heredadas de `QWidget`.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>