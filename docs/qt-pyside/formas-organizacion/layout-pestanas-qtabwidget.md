title: Layout con pestañas QTabWidget | Curso Qt/PySide | Hektor Profe

# Layout con pestañas QTabWidget

<img src="{{cdn}}/pyside/19.gif">

El último tipo de disposición que veremos es con pestañas utilizando un `QTabWidget`, se trata de una variante del apilado con un control más visual. Esta variante sí hereda de la clase `QWidget` y por tanto no requiere un dummy widget:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QTabWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout de pestañas
        tabs = QTabWidget()

        # Añadimos varios widgets como pestañas con nombres
        tabs.addTab(Caja("orange"), "Uno")
        tabs.addTab(Caja("magenta"), "Dos")
        tabs.addTab(Caja("purple"), "Tres")
        tabs.addTab(Caja("red"), "Cuatro")

        # asignamos las pestañas como widget central
        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Algunas opciones interesantes de este widget es que podemos modificar la posición de las pestañas:

```python
tabs.setTabPosition(QTabWidget.West)  # West, East, North, South
```

O hacer que las pestañas se puedan arrastrar para cambiar el orden:

```python
tabs.setMovable(True)
```

Y con esto acabamos el repaso de los layouts esenciales de Qt.

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>