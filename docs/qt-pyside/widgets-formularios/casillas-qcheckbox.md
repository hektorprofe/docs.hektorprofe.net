title: Casillas QCheckBox | Curso Qt/PySide | Hektor Profe

# Casillas QCheckBox

<img src="{{cdn}}/pyside/06.png">

Seguimos el tour viendo las casillas de verificación o checkboxes:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox  # edited
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos una casilla y la establecemos de widget central
        casilla = QCheckBox("Casilla de verificación")
        self.setCentralWidget(casilla)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Sirven como alternadores para saber si una opción está marcada o no. Podemos conectar una señal `stateChanged` para saber cuando cambia y consultar su valor:

```python
# señal para detectar cambios en la casilla
casilla.stateChanged.connect(self.estado_cambiado)

def estado_cambiado(self, estado):
    print(estado)
```

Fijaos que curiosamente los estados numéricos de la casilla son 0 y 2. Cuando es cero la está desmarcada y cuando es dos está marcada. Podemos utilizar banderas para analizar de forma más amigable la casilla:

```python
def estado_cambiado(self, estado):
    if estado == Qt.Checked:
        print("Casilla marcada")
    if estado == Qt.Unchecked:
        print("Casilla desmarcada")
```

Y por curiosidad, ¿si desmarcado es 0 y marcado 2, a qué hace referencia el estado 1? Este estado se llama tri-estado e indica que una casilla no está estrictamente ni marcada ni desmarcada, sino en estado neutro:

```python
# establecemos el triestado por defecto, también funcionan los otros
casilla.setCheckState(Qt.PartiallyChecked)

def estado_cambiado(self, estado):
    if estado == Qt.Checked:
        print("Casilla marcada")
    if estado == Qt.Unchecked:
        print("Casilla desmarcada")
    if estado == Qt.PartiallyChecked:
        print("Casilla neutra")
```

También podemos desactivar la casilla utilizando su método `setEnabled`, que es común en la mayoría de widgets:

```python
# la podemos desactivar
casilla.setEnabled(False)
```

Y para consultar el estado actual de la casilla simplemente utilizaríamos `isChecked` o `isTristate` para especificar un estado neutro:

```python
# consultamos el valor actual
print("¿Activada?", casilla.isChecked())
print("¿Neutra?", casilla.isTristate())
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>