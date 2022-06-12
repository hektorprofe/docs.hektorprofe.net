title: Estilos de aplicación | Curso Qt/PySide | Hektor Profe

# Estilos de aplicación

<img src="{{cdn}}/pyside/30.png">

Los estilos modifican la estética de los componentes. Por defecto Qt aplica estilos específicos para cada plataforma para integrar la aplicación visualmente, esa es la razón por la que el mismo programa se verá diferente en Windows, Linux y Mac.

Los estilos se pueden personaliar para no hacerlos dependientes de la plataforma y de hecho el propio Qt tiene un tema llamado **Fusion** que provee una estética multiplataforma y moderna.

He preparado un formulario con todo tipo de widgets para que podamos apreciar los cambios visuales al cambiar los estilos:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLineEdit, QSpinBox)
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow("Nombre", QLineEdit("Hector"))
        formulario.addRow("Email", QLineEdit(text="hola@ejemplo.com"))
        formulario.addRow("Edad", QSpinBox(value=32))

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Para activar el tema `Fusion` basta con llamar al método `setStyle` de la aplicación:

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Como podréis observar son cambios muy sutiles que por lo menos en Windows cuesta apreciar a simple vista, pero así nos aseguramos de visualizar la misma estética en todas las plataformas.

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>