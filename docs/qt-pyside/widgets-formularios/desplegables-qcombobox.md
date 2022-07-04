title: Desplegables QComboBox | Curso Qt/PySide | Hektor Profe

# Desplegables QComboBox

<img src="{{cdn}}/pyside/08.png">

Los desplegables son listas de opciones de las cuales se pueden selecciona una única opción.

Para añadir opciones se utiliza su método `addItems`:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox  # edited
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un desplegable
        desplegable = QComboBox()
        self.setCentralWidget(desplegable)

        desplegable.addItems(["Opción 1", "Opción 2", "Opción 3"])
```

Dependiendo de si queremos consultar el índice o el valor al cambiar podemos usar una señal `currentTextChanged` o `currentIndexChanged`:

```python
desplegable.currentIndexChanged.connect(self.indice_cambiado)
desplegable.currentTextChanged.connect(self.texto_cambiado)

def indice_cambiado(self, indice):
    print("Nuevo índice ->", indice)

def texto_cambiado(self, texto):
    print("Nuevo texto ->", texto)
```

Si quisiéramos un valor vacío por defecto, ya que éste se establece como el primer elemento añadido, sería tan sencillo como poner una cadena vacía:

```python
desplegable.addItems(["", "Opción 1", "Opción 2", "Opción 3"])
```

Y para comprobar la opción seleccionada:

```python
# consultamos el valor actual
print("Índice actual ->", desplegable.currentIndex())
print("Texto actual ->", desplegable.currentText())
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>