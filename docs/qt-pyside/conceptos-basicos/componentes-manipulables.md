title: Componentes manipulables | Curso Qt/PySide | Hektor Profe

# Componentes manipulables

Para acabar esta introducción vamos a ver cómo manipular un widget.

Si deseamos acceder a un widget desde un método es tan sencillo como almacenar un acceso a ese widget en la propia instancia, es decir, usar un atributo de clase:

```python
# me gusta crear los accesos alfinal
self.button = button
```

Una vez contamos con el accesor, o mejor llamado puntero, podemos hacer referencia a cualquier instancia de un widget para modificarla a voluntad:

```python
def boton_alternador(self, valor):
    if valor:
        self.button.setText("Estoy activado")
    else:
        self.button.setText("Estoy desactivado")
```

Hagamos un último ejemplo usando otro componente:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit  # editado
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        self.setMinimumSize(QSize(480, 320))

        # widget input de texto
        texto = QLineEdit()
        # capturamos la señal de texto cambiado
        texto.textChanged.connect(self.texto_modificado)

        # establecemos el widget central
        self.setCentralWidget(texto)

        # creamos el puntero
        self.texto = texto

    def texto_modificado(self):
        # recuperasmo el texto del input
        texto_recuperado = self.texto.text()
        # modificamos el título de la ventana al vuelo
        self.setWindowTitle(texto_recuperado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>