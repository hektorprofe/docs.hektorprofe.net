title: QSS: Qt Style Sheets | Curso Qt/PySide | Hektor Profe

# QSS: Qt Style Sheets

Lo último que veremos sobre tematización son las hojas de estilo de Qt, o abreviadas QSS.

Si sabéis algo de programación web seguro que os suena el lenguaje `CSS`, pues `QSS` es una forma de añadir estilo a los widgets utilizando prácticamente la misma sintaxis.

En esta práctica vamos a personalizar unos cuantos widgets básicos dentro de un layout estilo formulario:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel, QRadioButton,
    QCheckBox, QLineEdit, QSpinBox, QPushButton, QPlainTextEdit)
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
        formulario.addRow("QSpinBox", QSpinBox())

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)
```

La forma más sencilla de establecer los estilos es a través del método `setSyleSheets` del widget principal, pues con él podemos dar estilo a todo lo que contiene:

```python
# estilos QSS
self.setStyleSheet("""
    QMainWindow {
        background-color: #212121; }
    QLabel {
        color: #e9e9e9; }
    QPushButton {
        background-color: orange;
        font-family: "Arial";
        font-size: 14px;
        font-weight: bold; }
""")
```

Ahora bien, estos estilos son globales y afectan a todas las instancias. Si queremos estilizar una sola instancia podemos otorgarle un identificador:

```python
etiqueta = QLabel("QLabel")
etiqueta.setObjectName("etiqueta")
formulario.addRow(etiqueta)
```

Y referirnos a ella en QSS usando la almohadilla igual que en CSS:

```python
"""
#etiqueta {
  background-color: cyan;
  padding: 10px;
  color: black; }
"""
```

La verdad es que este tema abarca mucho y no quiero extenderme, os dejaré la [documentación](https://doc.qt.io/qt-6/stylesheet-reference.html#list-of-properties) con todas las propiedades disponibles y cada uno que profundice en la medida de lo necesario.

Lo que sí quiero compartir con vosotros es un pequeño widget para probar estilos en vivo, se basa en crear una subventana con un pequeño editor. Esto os ayudará a tematizar vuestros programas sin tener que guardar y ejecutar el código mil veces:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QLineEdit, QSpinBox, QPushButton, QPlainTextEdit, QVBoxLayout)
import sys


class EditorQSS(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.resize(480, 320)
        self.setWindowTitle("Editor QSS en vivo")

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet(
            "background-color: #212121; color: #e9e9e9; font-family: Consolas; font-size: 16px; ")
        self.editor.setFont("Consolas")
        self.editor.textChanged.connect(self.actualizar_estilos)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)

        self.show()

    def actualizar_estilos(self):
        qss = self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(qss)
        except:
            pass
```

Simplemente tenemos que crear una instancia en nuestro programa pasándole como parámetro el widget de la ventana y ya podemos empezar a probar estilos:

```python
# editor QSS en vivo
self.editorQSS = EditorQSS(self)
```


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>