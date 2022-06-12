title: Widget personalizado QWidget | Curso Qt/PySide | Hektor Profe

# Widget personalizado QWidget

<img src="{{cdn}}/pyside/13.png">

Hasta ahora hemos trabajado ejemplos muy sencillos en una ventana principal con un solo widget, pero ahora vamos a dar un paso adelante y a implementar varios widgets en el mismo espacio. Si vamos a utilizar varios widgets necesitamos organizarlos y precisamente para eso existen los layouts, que se traducirían en español como disposiciones.

Hace un tiempo encontré una forma excelente de ilustrar el funcionamiento de los layouts. Consiste en crear una clase base con un fondo coloreado, así veremos exactamente el espacio que ocupan los layouts de una forma muy visual.

Así que vamos a preparar un widget personalizado para visualizar nuestros layouts, lo vamos a llamar `caja` y lo heredaremos de una simple label:

```python
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")
```

Me váis a permitir adelantarme un poco y utilizar una hoja de estilo para otorgar un color de fondo a nuestra caja mediante el método `setStyleSheet`. Este método lo estudiaremos a fondo en la unidad de tematización.

Vamos a crear una ventana principal básica usando esta caja como widget central:

```python
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys


class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        caja = Contenedor("green")
        self.setCentralWidget(caja)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Listo, en la siguiente lección vamos a experimentar creando contenedores y organizándolos en diferentes disposiciones.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>