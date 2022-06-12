title: Tamaño de los widgets QSize | Curso Qt/PySide | Hektor Profe

# Tamaño de los widgets QSize
 
<img src="{{cdn}}/pyside/03.png">

En Qt existe un objeto llamado `QSize` que podemos asignar a los widgets para controlar su tamaño. Toma un ancho y un alto en píxeles y se puede establecer como tamaño mínimo, máximo o fijo para un widget:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize # Nuevo
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        button = QPushButton("Hola")
        self.setCentralWidget(button)

        # Tamaño mínimo del widget
        self.setMinimumSize(QSize(480, 320))
        # Tamaño máximo del widget
        self.setMaximumSize(QSize(480, 320))
        # Tamaño fijo del widget
        self.setFixedSize(QSize(480, 320))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Alternativamente, si no queremos complicarnos la vida podemos utilizar el método `resize` de la ventana:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        button = QPushButton("Hola")
        self.setCentralWidget(button)

        # Redimensión simple
        self.resize(480, 320)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

El inconveniente es que este método no da tanto juego como establecer las reglas independientes.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>