title: Activando las traducciones | Curso Qt/PySide | Hektor Profe

# Activando las traducciones

Traducir los diálogos predeterminados a mano hace que se pierda su simplicidad, por eso es recomendable activar las traducciones. Esto implica que hay que distribuir los ficheros de traducción junto a los ejecutables, pero eso es algo que veremos más adelante.

Para activar la localización al idioma del sistema operativo debemos traducir la aplicación de la siguiente forma:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
from PySide6.QtCore import QTranslator, QLibraryInfo  # nuevo
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QMessageBox.warning(
            self, "Diálogo de aviso", "¿Estás seguro de aplicar los cambios?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # envolvemos la aplicación con el traductor
    translator = QTranslator(app)
    # recuperamos el directorio de traducciones
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    # cargamos la traducción en el traductor
    translator.load("qt_es", translations)
    # la aplicamos
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Podemos consultar los idiomas disponibles en la carpeta de traducciones:

```python
print(translations)
```

```bash
cd ruta/
explorer .
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>