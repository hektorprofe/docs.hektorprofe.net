title: Layouts básicos QVBoxLayout y QHBoxLayout | Curso Qt/PySide | Hektor Profe

# Layouts básicos QVBoxLayout y QHBoxLayout

Existen dos tipos de disposición básica para organizar elementos vertical u horizontalmente.

Empecemos por el primer tipo:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # empezamos creando un layout vertical
        layout = QVBoxLayout()

        # le añadimos una caja verde
        layout.addWidget(Caja("green"))

        # probamos a establecerlo como widget central
        self.setCentralWidget(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Al ejecutarlo veremos que nos devuelve un error:

```
TypeError: 'PySide6.QtWidgets.QMainWindow.setCentralWidget' called with wrong argument types:
PySide6.QtWidgets.QMainWindow.setCentralWidget(QVBoxLayout)
```

Nos está indicando que no se permite utilizar un layout como widget central. Eso es porque los layouts no son widgets, no heredan de la clase `QWidget`.

La forma de manejar esto es crear un `dummy widget` para asignarle el layout y usarlo como widget central:

```python
from PySide6.QtWidgets import ..., QWidget  # edited

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(Contenedor("green"))

        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)
```

Como podemos observar el layout contiene la caja verde, que a su vez se encuentra dentro del dummy widget asignado como widget principal. La diferencia más notable es que un layout tiene espacios y márgenes, por eso la caja no ocupa todo el espacio.

Vamos a añadir más cajas para ver cómo organiza el espacio automáticamente:

```python
# le añadimos unas cuantas cajas
layout.addWidget(Caja("green"))
layout.addWidget(Caja("blue"))
layout.addWidget(Caja("red"))
```

¿Véis como el layout vertical reparte equitativamente el espacio entre los widgets que contiene?

Vamos a cambiar a un layaout horizontal para ver cómo se reparten los objetos:

- `QVBoxLayout` -> `QHBoxLayout`
- `layout = QVBoxLayout()` -> `layout = QHBoxLayout()`

Es exactamente lo mismo, pero en esta ocasión todo se organiza horizontalmente.

Para modificar los márgenes del layout se utiliza el método `setContentsMargins` pasándole por orden los píxeles a la izquierda, arriba, derecha y abajo:

```python
# modificamos los márgenes
layout.setContentsMargins(0,0,0,0)
```

Y para quitar el espaciado entre los widgets utilizaremos `setSpacing` con 0 píxeles:

```python
# modificamos el espaciado
layout.setSpacing(0)
```

Sobra decir que estamos usando nuestra caja para visualizar el espacio de cada widget, pero en la vida real estaríamos añadiendo etiquetas, campos de texto y otros widgets para diseñar formularios o lo que necesitemos.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>