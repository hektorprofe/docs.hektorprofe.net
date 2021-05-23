title: Diálogos de mensaje QMessageBox | Curso Qt/PySide | Hektor Profe

# Diálogos de mensaje QMessageBox

Si lo que deseamos en enviar un mensaje al usuario tenemos a nuestra disposición una clase llamada `QMessageBox` que simplifica la personalización de un `QDialog`. Básicamente podemos hacer todo lo de la anterior lección sin crear nuestra propia clase heredada y además podemos usar iconos predeterminados:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        # creamos un diálogo de mensaje con un título y un texto
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Título del diálogo")
        dialogo.setText("Esto es un diálogo de prueba")
        # añadimos unos botones y los traducimos
        dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText("Aceptar")
        dialogo.button(QMessageBox.Cancel).setText("Cancelar")
        # configuramos un icono
        dialogo.setIcon(QMessageBox.Question)

        # ejecutamos el diálogo y capturamos la respuesta
        respuesta = dialogo.exec_()
        # ahora debemos comprobar qué tipo de botón se ha clicado
        if respuesta == QMessageBox.Ok:
            print("Diálogo aceptado")
        else:
            print("Diálogo denegado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Os dejo documentación sobre los [botones](https://doc.qt.io/qt-6/qmessagebox.html#StandardButton-enum) e [iconos](https://doc.qt.io/qt-6/qmessagebox.html#Icon-enum) disponibles en los diálogos de mensaje.

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>