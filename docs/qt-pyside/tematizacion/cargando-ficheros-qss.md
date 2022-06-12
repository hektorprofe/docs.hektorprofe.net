title: Cargando ficheros QSS | Curso Qt/PySide | Hektor Profe

# Cargando ficheros QSS

<img src="{{cdn}}/pyside/34.png">

En esta última lección vamos a cargar ficheros QSS para no tener que escribir el código en el propio programa. He preparado un buen puñado de estilos que he encontrado por Internet, os los adjunto en los recursos, sentíos libres de utilizarlos respetando las directrices de cada creador, cuya fuente encontraréis en la cabecera de cada fichero.

Tengo un programa ya preparado para empezar a trabajar:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import Qt
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow("QCheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QDateEdit", QDateEdit())
        formulario.addRow("QDateTimeEdit", QDateTimeEdit())
        formulario.addRow("QSpinBox", QSpinBox())
        formulario.addRow("QDoubleSpinBox", QDoubleSpinBox())
        formulario.addRow("QComboBox", QComboBox())
        formulario.addRow("QFontComboBox", QFontComboBox())
        formulario.addRow("QProgressBar", QProgressBar())
        formulario.addRow("QLCDNumber", QLCDNumber())
        formulario.addRow("QSlider", QSlider(Qt.Horizontal))
        formulario.addRow("QDial", QDial())

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Para cargar los estilos me ayudaré de la función `absPath`, abriré los ficheros de estilo como si fueran texto, leeré su contenido y lo volcaré al método `setStyleSheet` de la ventana:

```python
def cargarQSS(self, file):
    # guardamos la ruta absoluta al fichero
    path = absPath(file)
    # intentamos abrirlo y volcar el contenido
    try:
        with open(path) as styles:
            self.setStyleSheet(styles.read())
    # si hay algún fallo lo capturamos con una excepción genérica
    except:
        print("Error abriendo estilos", path)
```

Solo resta llamar al método y probar algunos temas:

```python
# cargamos los estilos del fichero
self.cargarQSS("qss/Ubuntu.qss")
self.cargarQSS("qss/ElegantDark.qss")
self.cargarQSS("qss/ChatBee.qss")
self.cargarQSS("qss/EasyCode.qss")
```

Con esto tenéis toneladas de referencias para tematizar vuestros programas.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>