title: Usando diseños y recursos de Qt Designer | Curso Qt/PySide | Hektor Profe

# Usando diseños y recursos de Qt Designer

Para importar nuestros diseños en Python debemos transformarlos a código Python, eso se consigue compilando los diseños.

Para este fin se requiere de un programa intermediario de la Suite Qt llamado `uic`: User Interface Compiler.

Si añadimos el directorio de `PySide6` al path deberíamos poder acceder a él desde la terminal:

```bash
uic -h
```

El comando para compilar un diseño es:

```bash
cd 1-9-2/interfaces
uic.exe -g python mainwindow.ui -o mainwindow.py
```

Así habremos generado un fichero `python` dentro de la carpeta interfaces.

Este proceso se puede realizar directamente desde `Qt Designer` si se tiene configurado `uic.exe` tal como explico al principio del curso.

Sea como sea, si analizamos el fichero generado encontraremos las importaciones y el código para generar la ventana:

```python
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import recursos_rc
```

Quiero que os fijéis en la línea `import recursos_rc`.

Esta importación es la que va a cargar los recursos compilados del diseño, que deberán estar en el módulo `recursos_rc` de la propia carpeta, así que necesitamos crearlos.

Compilar los recursos es un proceso calcado a compilar los diseños, pero esta vez se utiliza otra herramienta de Qt llamada `rcc`: Resource Compiler.

El comando para compilar los recursos es:

```bash
cd 1-9-2
rcc.exe -g python resources.py -o resources.qrc  # mismo directorio
```

Esto tomará el fichero `resources.qrc` que habíamos creado en `Qt Designer` y lo compilará. Fijaros como el nombre debe concordar con el módulo que espera encontrar la ventana principal.

Ahora los iconos del programa se encuentran compilados en el fichero `recursos_rc.py`. Nuestro programa los tomará de ahí en lugar de utilizar las imágenes del directorio `recursos/`.

Llegados a este punto es hora de crear un programa con PySide e importar el diseño. La lógica de creación de la ventana principal es la siguiente:

```python
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz

    def __init__(self):

        # Llamamos al constructor explícito de QMainWindow
        super().__init__()

        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Vamos a ejecutar el programa a ver si todo funciona bien:

- `Widgets` -> Ok
- `Estilos` -> Ok
- `Recursos` -> Ok
- `Tips` -> Ok

Ya lo véis, fácil, rápido y para toda la familia.

En la próxima lección vamos a añadir funcionalidades al diseño.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>