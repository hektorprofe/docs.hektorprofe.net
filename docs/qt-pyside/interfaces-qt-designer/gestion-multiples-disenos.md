title: Gestión de múltiples diseños | Curso Qt/PySide | Hektor Profe

# Gestión de múltiples diseños

Supongamos que en lugar de mostrar un cuadro de diálogo queremos crear una subventana un diseñada con Qt Designer.

Vamos a crear algo sencillo tomando como base la clase `QWidget`:

<img src="{{cdn}}/pyside/09-docs/10.png">

Compilamos el diseñode la subventana:

```bash
cd 1-9-4/interfaces
uic.exe -g python mainwindow.ui -o mainwindow.py
```

Vamos a partir del programa de antes sin la señal del botón:

```python
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaces.mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSalir.triggered.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Importamos la subventana, creamos un nuevo widget a nuestro gusto heredando de `QWidget` y su diseño para poder llamar a su método `setupUi`:

```python
from interfaces.subventana import Ui_Form  # el diseño de un widget es un form

class Subventana(QWidget, Ui_Form):
    def __init__(self):
        # llamamos al constructor
        super().__init__()
        # generamos la interfaz de la subventana
        self.setupUi(self)
        # señal para cerrar la subventana
        self.pushButton.clicked.connect(self.close)
```

Fijaros como la lógica es la misma, pero al heredar de `Qwidget` debemos llamar a su constructor explícitamente. Recordad que la diferencia entre una ventana principal y un widget es que los segundos no contienen componentes como los las barras de menus o de herramientas.

Ahora, para manejar esta subventana lo haremos exactamente igual que aprendimos en las unidades anteriores, creando una instancia de la misma y mostrándola al presionar el botón de la ventana principal:

```python
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionSalir.triggered.connect(self.close)

        # creamos la subventana pero no la mostramos
        self.subventana = Subventana()
        # señal para abrir la subventana enviándole el texto del campo
        self.pushButton.clicked.connect(self.mostrar_subventana)

    def mostrar_subventana(self):
        # establecemos el texto de la ventana principal en la subventana
        self.subventana.label.setText(self.lineEdit.text())
        # y mostramos la subventana
        self.subventana.show()
```

<img src="{{cdn}}/pyside/09-docs/11.png">

Y ya lo tenemos.

Solo comentar algo, si hubiéramos creado un diálogo en Qt Designer deberíamos haber heredado de la clase `QDialog` en lugar de `QWidget`, tenedlo presento.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>