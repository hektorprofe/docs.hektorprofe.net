title: Diálogos específicos | Curso Qt/PySide | Hektor Profe

# Diálogos específicos

<img src="{{cdn}}/pyside/24.png">

Vamos a acabar esta unidad viendo otros ejemplos de diálogos para usos específicos. Es importante tener en cuenta que es necesario activar las traducciones o los textos aparecerán en inglés.

## Diálogos de fichero QFileDialog

Se utilizan para generar la ruta a un fichero usando el explorador, es decir, no afectan al fichero en sí y solo sirven para saber donde se encuentra un fichero, ya sea para abrirlo o para guardarlo:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog)  # editado

def boton_clicado(self):
    fichero, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", ".")
    print(fichero)
```

También se puede usar en el modo para guardar un fichero:

```python
fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
```

Este modo es muy útil porque si el fichero ya existe te avisa de que se va a sobreescribir.

## Diálogos de entrada de datos QInputDialog

Pensados para pedir un dato concreto al usuario:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QInputDialog)  # editado

def boton_clicado(self):
    dialogo = QInputDialog.getText(self, "Título", "Texto")
    dialogo = QInputDialog.getInt(self, "Título", "Entero")
    dialogo = QInputDialog.getDouble(self, "Título", "Decimal")
    dialogo = QInputDialog.getItem(
        self, "Título",  "Colores", ["Rojo", "Azul", "Blanco", "Verde"])
```

Este diálogo devuelve una tupla, primero el valor y luego si se ha confirmado el diálogo. Esto sirve para saber si se cancela la captura de datos, por eso una forma de tratar la información es en dos variables:

```python
color, confirmado = QInputDialog.getItem(
    self, "Título",  "Colores", ["Rojo", "Azul", "Blanco", "Verde"])

if confirmado:
    print(color)
```

## Diálogos de fuente QFontDialog y color QColorDialog

Estos tienen el objetivo de seleccionar fuentes del sistema y colores.

Veamos como abrir una fuente para utilizarla en un botón:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFontDialog)  # new

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

        self.boton = boton

    def boton_clicado(self):
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            # fuente es un objeto QFont
            self.boton.setFont(fuente)
```

Y ahora un color para usarlo de fondo:

```python
def boton_clicado(self):
    color = QColorDialog.getColor()
    if color.isValid():
        # color es un objeto QColor, name() devuelve su código hexadecimal
        self.boton.setStyleSheet(f"background-color: {color.name()}")
```

Con esto hemos cubierto casi todo sobre los diálogos, si queréis profundizar os dejo la [documentación](https://doc.qt.io/qt-6/dialogs.html) oficial.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>