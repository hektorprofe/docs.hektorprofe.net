title: Botones radiales QRadioButton | Curso Qt/PySide | Hektor Profe

# Botones radiales QRadioButton

Muy parecidas a las casillas son los botones radiales, sin embargo estos solo pueden marcarse o desmarcarse, no tienen estado neutro:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un botón radial y lo establecemos de widget central
        radial = QRadioButton("Botón radial")
        self.setCentralWidget(radial)

        # señal para detectar cambios en el botón
        radial.toggled.connect(self.estado_cambiado)

        # Podemos activarla por defecto
        radial.setChecked(True)

        # consultamos el valor actual
        print("¿Activada?", radial.isChecked())

    def estado_cambiado(self, estado):
        if estado:
            print("Radial marcado")
        else:
            print("Radial desmarcado")

```


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>