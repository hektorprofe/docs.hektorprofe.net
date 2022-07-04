title: Creación de subventanas | Curso Qt/PySide | Hektor Profe

# Creación de subventanas

<img src="{{cdn}}/pyside/28.png">

En esta lección vamos a ver cómo manejar ventanas secundarias. Para ello partiremos del siguiente programa:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.setWindowTitle("Ventana principal")
        # dummy widget para un layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # botón para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

    def mostrar_subventana(self):
        print("Subventana abierta")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Para nuestra subventana vamos a partir de una clase heredada de `QWidget` que instanciaremos en el método `mostrar_subventana`:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel)  # editado
import sys

class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
        # creamos una etiqueta
        etiqueta = QLabel("Soy una subventana")
        # creamos un layout y añadimos la etiqueta
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        # asignamos el layout al widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def mostrar_subventana(self):
        subventana = Subventana()
        subventana.show()
```

Si ejecutamos el código la subventana se creará pero desaparecerá en un instante. Esto ocurre porque la instancia existe en el ámbito de la función, cuando la función finaliza la subventana se borra de la memoria. Si queremos conservar la instancia debemos crear la instancia en la clase:

```python
def mostrar_subventana(self):
    self.subventana = Subventana()
    self.subventana.show()
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>