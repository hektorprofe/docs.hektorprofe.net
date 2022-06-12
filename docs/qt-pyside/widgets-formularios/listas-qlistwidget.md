title: Listas QListWidget | Curso Qt/PySide | Hektor Profe

# Listas QListWidget

<img src="{{cdn}}/pyside/09.png">

Las listas son muy parecidas a los desplegables pero aquí las opciones no están ocultas ni hay ninguna activa por defecto. En lugar de índices manejan un tipo de valor llamado `QItem` y la señal de cambio aquí es `currentItemChanged`:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos una lista
        lista = QListWidget()
        self.setCentralWidget(lista)

        # Añadimos algunas opciones
        lista.addItems(["Opción 1", "Opción 2", "Opción 3"])

        # Y algunas señales
        lista.currentItemChanged.connect(self.item_cambiado)

    def item_cambiado(self, item):
        # Conseguimos el texto del ítem con su método text()
        print("Nuevo ítem ->", item.text())
```

Y para conseguir el ítem actual utilizaremos:

```python
print(lista.currentItem())
```

Como por defecto la lista no tiene nada seleccionado muestra `None`.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>