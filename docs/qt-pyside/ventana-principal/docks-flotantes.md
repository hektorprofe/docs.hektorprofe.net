title: Docks flotantes QDockWidget | Curso Qt/PySide | Hektor Profe

# Docks flotantes QDockWidget

<img src="{{cdn}}/pyside/27.gif">

El último componente que nos falta ver de las ventanas principales son los docks floatantes.

Los docks son contenedores flotantes que se pueden posicionar a los lados de la ventana, desacoplarlos e incluso cerrarlos.

Al igual que la ventana principal tiene su método para establecer un widget principal, los docks tiene un método `setWidget` para configurar el widget que contendrán. Nuestra clase `Caja` es muy simple y nos permitirá hacernos una idea del funcionamiento, así que vamos a recuperarla para utilizarla de widget de los docks:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar,
    QToolBar, QLabel, QDockWidget)  # edited

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        # ...
        # añadimos los docks
        self.construir_docks()
        # creamos una caja como widget central de la ventana principal
        self.setCentralWidget(Caja("gray"))

    def construir_docks(self):
        # creamos un dock
        dock1 = QDockWidget()
        # le damos un título (optativo)
        dock1.setWindowTitle("DOCK 1")
        # establecemos el widget que contendrá
        dock1.setWidget(Caja("green"))
        # ancho mínimo (optativo)
        dock1.setMinimumWidth(100)
        # lo añadimos en una posición de la ventana principal
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Como véis los `docks` son super flexibles. Eso sí, al cerrarlo lo perdemos y deberíamos proveer de alguna forma de crearlo de nuevo, o también podemos limitar sus características :

```python
dock1.setFeatures(
    QDockWidget.NoDockWidgetFeatures | QDockWidget.DockWidgetFloatable |
    QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)
```

También podemos controlar su tamaños:

```python
# tamaños (optativos)
dock1.setMinimumWidth(125)
dock1.setMinimumHeight(100)
dock1.setMinimumSize(125, 100)
```

Y añadir más docks en otras posiciones para juguetear con ellos:

```python
# creamos más docks para jugar con ellos
dock2 = QDockWidget()
dock2.setWindowTitle("DOCK 2")
dock2.setWidget(Caja("yellow"))
dock2.setMinimumSize(125, 100)
self.addDockWidget(Qt.RightDockWidgetArea, dock2)

dock3 = QDockWidget()
dock3.setWindowTitle("DOCK 3")
dock3.setWidget(Caja("blue"))
dock3.setMinimumSize(125, 100)
self.addDockWidget(Qt.BottomDockWidgetArea, dock3)
```

Fijaros como podemos acoplar widgets unos sobre otrossi hay suficiente espacio o apilarlos usando pestañas, dan muchísimo juego.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>