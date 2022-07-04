title: Barras de menú, estado y acciones QAction | Curso Qt/PySide | Hektor Profe

# Barras de menú, estado y acciones QAction

<img src="{{cdn}}/pyside/25.gif">

Un menú es un componente estandar que se puede configurar en las ventanas principales `QMainWindow`.

Se ubican en la parte superior de la ventana o pantalla y permiten a los usuarios acceder a las funcionalidades de las aplicaciones. Hay menús estandarizados como los de `Fichero, Edición y Ayuda`, cada uno con sus propias jerarquías y árboles de funciones. También ofrecen accesos directos y otras opciones de accesiblidad:

```python
from PySide6.QtWidgets import (QApplication, QMainWindow)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        # Recuperamos la barra de menú
        menu = self.menuBar()
        # Añadimos un menú de archivo
        menu_archivo = menu.addMenu("&Menú")
        # Añadimos una acción de prueba
        menu_archivo.addAction("&Prueba")
        # Añadimos un submenú
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        # Añadimos una acción de prueba
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        # Añadimos un separador
        menu_archivo.addSeparator()
        # Añadimos una última acción
        menu_archivo.addAction("S&alir")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Las opciones del menú se llaman acciones porque en realidad son objetos de la clase `QAction` que estamos creando implícitamente.

Vamos a completar la acción de salir con un icono, un accesor y para que se llame el método `close` de la ventana principal:

```python
from PySide6.QtGui import QIcon
from pathlib import Path

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


# Añadimos una acción completa
menu_archivo.addAction(
    QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")
```

Ahora bien, con el objetivo de reutilizar código es aconsejable crear nuestras propias acciones y luego añadirlas a los menús en lugar de hacerlo implícitamente:

```python
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox) # edited
from PySide6.QtGui import QAction, QIcon  # editado
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Menú")
        menu_archivo.addAction("&Prueba")
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        menu_archivo.addSeparator()
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")

        # Añadimos un menú de ayuda
        menu_ayuda = menu.addMenu("Ay&uda")
        # Creamos una acción específica para mostrar información
        accion_info = QAction("&Información", self)
        # Podemos configurar un icono en la acción
        accion_info.setIcon(QIcon(absPath("icon.png")))
        # También podemos especificar un accesor
        accion_info.setShortcut("Ctrl+I")
        # Le configuramos una señal para ejecutar un método
        accion_info.triggered.connect(self.mostrar_info)
        # Añadimos la acción al menú
        menu_ayuda.addAction(accion_info)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")
```

Las acciones también permiten configurar lo que se conoce como `statusTip` para mostrar la utilidad de la acción.

```python
# Añadimos un texto de ayuda
accion_info.setStatusTip("Muestra información irrelevante")
```

Esto no hará nada porque el texto se muestra en la barra de estado de la ventana principal, una barra que no tenemos activa. Así que vamos a darla de alta:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar)  # edited

# Añadimos una barra de estado
self.setStatusBar(QStatusBar(self))
```

Ahora al pasar el ratón por encima de la acción aparecerá en la parte inferior el texto explicativo.

En la siguiente lección seguiremos mejorando esta ventana principal, pero antes vamos a refactorizar un poco el código para aligerar el constructor:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        # construimos nuestro menú
        self.construir_menu()

    def construir_menu(self):
        # Recuperamos la barra de menú
        menu = self.menuBar()

        # Añadimos un menú de archivo
        menu_archivo = menu.addMenu("&Menú")
        # Añadimos una acción de prueba
        menu_archivo.addAction("&Prueba")
        # Añadimos un submenú
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        # Añadimos una acción de prueba
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
        # Añadimos un separador
        menu_archivo.addSeparator()
        # Añadimos una acción completa
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")

        # Añadimos un menú de ayuda
        menu_ayuda = menu.addMenu("Ay&uda")
        # Creamos una acción específica para mostrar información
        accion_info = QAction("&Información", self)
        # Podemos configurar un icono en la acción
        accion_info.setIcon(QIcon(absPath("info.png")))
        # También podemos especificar un accesor
        accion_info.setShortcut("Ctrl+I")
        # Le configuramos una señal para ejecutar un método
        accion_info.triggered.connect(self.mostrar_info)
        # Añadimos un texto de ayuda
        accion_info.setStatusTip("Muestra información irrelevante")
        # Añadimos la acción al menú
        menu_ayuda.addAction(accion_info)

        # Añadimos una barra de estado
        self.setStatusBar(QStatusBar(self))

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>