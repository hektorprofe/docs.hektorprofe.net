title: Layout en cuadrícula QGridLayout | Curso Qt/PySide | Hektor Profe

# Layout en cuadrícula QGridLayout

El layout en cuadrícula se basa en crear un único layout compuesto de filas y columnas. Primero se crea la cuadrícula y luego se rellena cada hueco o celda haciendo referencia a ella con índices que empiezan valiendo cero:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGridLayout, QWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en cuadrícula
        cuadricula = QGridLayout()

        # añadimos widgets en las celdas usando los índices
        cuadricula.addWidget(Caja("orange"), 0, 0)
        cuadricula.addWidget(Caja("purple"), 1, 1)
        cuadricula.addWidget(Caja("magenta"), 2, 2)
        cuadricula.addWidget(Caja("gray"), 2, 0)
        cuadricula.addWidget(Caja("red"), 0, 2)

        # cremos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

El tamaño de la cuadrícula vendrá determinado automáticamente por los mayores índices con un widget, lo que generará huecos vacíos si no los rellenemos explícitamente.

Vamos a hacer un experimento para generar dinámicamente una cuadrícula con cajas de colores aleatorios a partir de dos bucles for:

```python
import random

# bucles for para generar una cuadrícula
for fila in range(5):
    for columna in range(5):
        # añadimos una caja de color aleatorio
        color = str(hex(random.randint(0, 16777215)))  # int(0xFFFFFF)
        cuadricula.addWidget(Caja(f"#{color[2:]}"), fila, columna)
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>