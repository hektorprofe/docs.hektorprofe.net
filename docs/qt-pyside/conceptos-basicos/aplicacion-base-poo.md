title: Primera aplicación usando POO | Curso Qt/PySide | Hektor Profe

# Primera aplicación usando POO

<img src="{{cdn}}/pyside/02.png">

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):

    """
    Creamos nuestra propia clase MainWindow heredando de QMainWindow
    """

    # Creamos la ventana en el constructor a partir de una QMainWindow
    def __init__(self):

        # Con super ejecutamos su propio constructor
        # Así se crea la ventana en su propia instancia self
        super().__init__()

        # Damos un título al programa
        self.setWindowTitle("Hola mundo")

        # Guardamos el botón en una variable
        button = QPushButton("Hola")

        # Establecemos el botón como widget central de la ventana principal
        self.setCentralWidget(button)


# Si ejecutamos el propio script como programa principal
if __name__ == "__main__":
    # Creamos la aplicación
    app = QApplication(sys.argv)
    # Creamos nuestra ventana principal
    window = MainWindow()
    # Mostramos la ventana
    window.show()
    # Iniciamos el bucle del programa
    sys.exit(app.exec_())
```

La clave es extender el funcionamiento del constructor de `QMainWindow`, pues al ejecutar `super().__init__()` heredamos su comportamiento. Desde ese momento la propia instancia `self` de nuestra clase `MainWindow` adquiere los métodos heredados como `setWindowTitle` y `setCentralWidget`.



___
<small class="edited"><i>Última edición: 23 de Mayo de 2021</i></small>