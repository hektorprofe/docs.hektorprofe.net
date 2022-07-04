title: Diálogos personalizados QDialog | Curso Qt/PySide | Hektor Profe

# Diálogos personalizados QDialog

<img src="{{cdn}}/pyside/20.png">

Todos los diálogos parten de la clase `QDialog` y están pensados para mostrar o pedir información al usuario en una nueva ventana temporal. Al estar pensados para aparecer de forma emergente, los diálogos requieren una acción desencadenante para aparecer.

Vamos a partir de un diálogo vacío para ver su funcionamiento:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)  # forma alternativa de redimensionar un widget

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QDialog(self)
        dialogo.setWindowTitle("Hola")
        dialogo.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

El diálogo `QDialog` está pensado para extenderlo, vamos a personalizar algunas opciones creando nuestro propio diálogo heredando de esta clase:

```python
class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola")

def boton_clicado(self):
    dialogo = Dialogo()
    dialogo.exec_()
```

Lo más esencial que nos permite un diálogo es interactuar con él a través de botones. Estos botones se configuran en su propia caja de botones llamada `QDialogButtonBox` que normalmente pondremos dentro de un layout donbe organizar el espacio:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLabel, QVBoxLayout,
    QDialog, QDialogButtonBox)
import sys


class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Hola")

        # creamos un layout y lo establecemos en el widget
        layout = QVBoxLayout()
        self.setLayout(layout)

        # podemos añadir una etiqueta
        layout.addWidget(QLabel("Diálogo de prueba"))

        # creamos unos botones predeterminados
        botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # y los añadimos al layout
        layout.addWidget(botones)
```

Los acciones básicas contra un `QDialog` son aceptarlo o denegarlo, ambas se deben configurar como señales en la caja de botones usando los métodos `accept` y `reject`:

```python
# configuramos unas señales predeterminadas
botones.accepted.connect(self.accept)
botones.rejected.connect(self.reject)
```

El sistema entenderá que el botón "Ok" indica aceptar el mensaje y "Cancel" lo contrario, retornando la respuesta al exterior para poder actuar en consecuencia:

```python
def boton_clicado(self):
    dialogo = Dialogo()
    respuesta = dialogo.exec_()
    if respuesta:
        print("Diálogo aceptado")
    else:
        print("Diálogo denegado")
```

Si deseamos que un diálogo emerja sobre la ventana donde se ha creado hay que pasarle la instancia del padre al crearlo:

```python
class Dialogo(QDialog):
    def __init__(self, parent=None):  # editado
        super().__init__(parent)      # editado

def boton_clicado(self):
    dialogo = Dialogo(self)  # editado
    respuesta = dialogo.exec_()
    if respuesta:
        print("Diálogo aceptado")
    else:
        print("Diálogo denegado")
```

Por cierto, los botones del diálogo se encuentran localizados, es decir que permiten traducciones. El problema es que hay que dar de alta un traductor y para dos botones no compensa hacerlo. Es más fácil cambiar el texto a mano:

```python
# traducción en tiempo real de los botones
botones.button(QDialogButtonBox.Ok).setText("Aceptar")
botones.button(QDialogButtonBox.Cancel).setText("Cancelar")
```

En los recursos os dejo la [documentación](https://doc.qt.io/qt-6/qdialogbuttonbox.html#StandardButton-enum) con la lista de botones que tenemos a nuestra disposición.

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>