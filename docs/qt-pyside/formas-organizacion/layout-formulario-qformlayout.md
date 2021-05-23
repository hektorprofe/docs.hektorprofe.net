title: Layout en formulario QFormLayout | Curso Qt/PySide | Hektor Profe

# Layout en formulario QFormLayout

Si lo que necesitamos es una estructura para manejar un formulario podemos usar un `QFormLayout` que nos permite añadir etiquetas y widgets en fila de una forma más cómoda que las cuadrículas:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFormLayout, QWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en formulario
        formulario = QFormLayout()

        # añadimos widgets con etiquetas en filas
        formulario.addRow("Campo 1", Caja("orange"))
        formulario.addRow("Campo 2", Caja("purple"))
        formulario.addRow("Campo 3", Caja("magenta"))
        formulario.addRow("Campo 4", Caja("gray"))
        formulario.addRow("Campo 5", Caja("red"))

        # cremos el widget dummy y le asignamos el layout
        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Dependiendo del sistema operativo el formulario se visualizará de forma diferente con el objetivo de respetar la integración, pero es posible cambiar la alineación de las etiquetas y los widgets manualmente:

```python
# configuraciones extra
formulario.setLabelAlignment(Qt.AlignRight)
formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
```


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>