title: Diálogos predeterminados QMessageBox | Curso Qt/PySide | Hektor Profe

# Diálogos predeterminados QMessageBox

Por suerte no necesitamos crear diálogos todo el tiempo, Qt incluye diálogos predeterminados para realiar diferentes tareas:

## Mensaje de cuestión QMessageBox.question

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        # creamos un diálogo de tipo cuestión
        dialogo = QMessageBox.question(
            self, "Diálogo de cuestión", "Esta es una pregunta de prueba")

        # ahora podemos comprobar qué tipo de botón se devuelve
        print(dialogo)
        if dialogo == QMessageBox.Yes:
            print("Ha respondido sí")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Traducir los diálogos predeterminados no es algo trivial, en la siguiente lección os enseñaré como activar el traductor, por ahora veamos otros ejemplos.

## Mensaje acerca de QMessageBox.about

Para mostrar información del programa o el autor:

```python
def boton_clicado(self):
    dialogo = QMessageBox.about(
        self, "Acerca de", "<p>Información del programa</p><p>Segundo parágrado</p>")
```

Este diálogo toma por defecto el icono de la ventana, vamos a añadir uno de ejemplo para verlo, usaremos la función para generar rutas absolutas que os enseñé:

```python
self.setWindowIcon(QIcon(absPath("icon.png")))
```

## Mensaje crítico QMessageBox.critical

Este diálogo reproduce un sonido de error mientras muestra la ventana:

```python
def boton_clicado(self):
    dialogo = QMessageBox.critical(
        self, "Diálogo de error", "Ha ocurrido algo malo")
    print(dialogo)
```

## Mensaje informativo

Para mostrar información genérica:

```python
def boton_clicado(self):
    dialogo = QMessageBox.information(
        self, "Diálogo informativo", "Esto es un texto informativo")
```

## Mensaje de aviso QMessageBox.warning

Para mostrar un aviso:

```python
def boton_clicado(self):
    dialogo = QMessageBox.warning(
        self, "Diálogo de aviso", "Cuidado con este diálogo")
```

Si deseamos modificar los botones de un mensaje predeterminado podemos hacerlo:

```python
def boton_clicado(self):
    dialogo = QMessageBox.warning(
        self, "Diálogo de aviso", "¿Estás seguro de aplicar los cambios?",
        buttons=QMessageBox.Apply | QMessageBox.Cancel,
        defaultButton=QMessageBox.Cancel)

    if dialogo == QMessageBox.Apply:
        print("Aplicamos los cambios")
```

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>