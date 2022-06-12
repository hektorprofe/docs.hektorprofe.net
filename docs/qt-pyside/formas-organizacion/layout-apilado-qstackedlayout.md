title: Layout apilado QStackedLayout | Curso Qt/PySide | Hektor Profe

# Layout apilado QStackedLayout

<img src="{{cdn}}/pyside/18.gif">

Otra disposición que da mucho juego es apilar los widgets usando un `QStackedLayout`:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QStackedLayout, QWidget)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout apilado
        layout = QStackedLayout()

        # Añadimos varios widgets unos sobre otros
        layout.addWidget(Caja("orange"))
        layout.addWidget(Caja("magenta"))
        layout.addWidget(Caja("purple"))
        layout.addWidget(Caja("red"))

        # creamos el widget dummy y le asignamos el layout apilado
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

El problema de este layout es que necesita controladores.

Vamos a definir un evento que capture cuando presionamos las flechas del teclado para poder alternar entre los widgets. Los eventos ya existen en el widget, lo que haremos es sobreescribir su comportamiento:

```python
from PySide6.QtCore import Qt  # nuevo

def keyPressEvent(self, event):
    # detectamos la flecha presionada
    if event.key() == Qt.Key_Right:
        print("Flecha derecha presionada")
    elif event.key() == Qt.Key_Left:
        print("Flecha izquierda presionada")
    # continuamos con el evento por defecto
    event.accept()
```

Ahora utilizaremos el método `setCurrentIndex` del layout para controlar el widget que se muestra teniendo en cuenta que el índice empieza valiendo 0 y al tener 4 widgets su valor máximo será 3. Este numero máximo podemos conseguirlo contando los elementos del layout con su método `count`.

Al presionar la flecha derecha incrementaremos el índice y con la izquierda lo decrementaremos. Para generar un efecto infinito si el índice es menor que cero lo estableceremos al máximo, si es mayor que el máximo lo estableceremos a cero:

```python
# necesitamos crear un accesor para usar el layout desde el evento
self.layout = layout

def keyPressEvent(self, event):
    # recuperamos el índice
    indice = self.layout.currentIndex()
    # buscamos el indice máximo del layout contando cuantos widgets tiene
    indice_maximo = self.layout.count() - 1

    # dependiendo de la flecha presionada sumamos o restamos
    if event.key() == Qt.Key_Right:
        indice += 1
    elif event.key() == Qt.Key_Left:
        indice -= 1

    # rectificamos el índice para generar el efecto infinito
    if indice > indice_maximo:
        indice = 0
    if indice < 0:
        indice = indice_maximo

    # finalmente establecemos el nuevo índice
    self.layout.setCurrentIndex(indice)

    # continuamos con el evento por defecto
    event.accept()
```

En este experimento hemos introducido los `eventos`, pero podríamos haber utilizado unos botones para cambiar de índice sin problema.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>