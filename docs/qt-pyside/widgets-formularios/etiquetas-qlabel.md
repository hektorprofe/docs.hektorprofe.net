title: Etiquetas QLabel | Curso Qt/PySide | Hektor Profe

# Etiquetas QLabel

<img src="{{cdn}}/pyside/05.png">

Empezamos este tour con las etiquetas, uno de los widgets más sencillos de Qt. Se trata de una pieza de texto que se puede posicionar en nuestra aplicación. Podemos asignar el texto al crearlas o mediante su método `setText()`:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))

        # widget etiqueta
        etiqueta = QLabel("Soy una etiqueta")
        # establecemos el widget central
        self.setCentralWidget(etiqueta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Las etiquetas permiten configurar una fuente a través de la cuál controlar el tamaño y otros atributos.

Podemos recuperar la fuente por defecto y aumentar su tamaño:

```python
# recuperamos la fuente por defecto
fuente = etiqueta.font()
# establecemos un tamaño
fuente.setPointSize(24)
# la asignamos a la etiqueta
etiqueta.setFont(fuente)
```

O podemos utilizar una fuente del sistema, aunque para ello debemos crear una instancia de la clase `QFont`:

```python
from PySide6.QtGui import QFont  # nuevo

# cargamos una fuente del sistema
fuente = QFont("Comic Sans MS", 24)
# la asignamos a la etiqueta
etiqueta.setFont(fuente)
```

Las etiquetas también nos permiten alinearlas respecto a su contenedor, para ello necesitamos importar las definiciones estándard de Qt:

```python
from PySide6.QtCore import QSize, Qt  # editado

# establecemos unas flags de alineamiento
etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
```

Estas definiciones se conocen como banderas o "flags". Son enumeradores con nombre para usarlos más cómodamente. Al unirlos con la tubería se evalúan en conjunto:

```python
print(int(Qt.AlignHCenter), int(Qt.AlignVCenter), int(Qt.AlignHCenter | Qt.AlignVCenter))
print(bin(Qt.AlignHCenter), bin(Qt.AlignVCenter), bin(Qt.AlignHCenter | Qt.AlignVCenter))
```

Otra cosa muy útil que permiten las etiquetas es cargar imágenes en su interior, para ello utilizamos un objeto de tipo `QPixemap` o mapa de píxeles creado a partir de una imagen y lo asignamos a la etiqueta. Tengo una imagen preparada en el directorio del script:

```python
from PySide6.QtGui import QFont, QPixmap  # editado

# creamos la imagen
imagen = QPixmap("naturaleza.jpg")
# la asginamos a la etiqueta
etiqueta.setPixmap(imagen)
```

En el momento en que cargamos recursos externos debemos empezar a tener en cuenta el concepto de la ruta al recurso.

Cuando establecemos `naturaleza.jpg`, el programa espera que ese recurso se encuentre en el mismo directorio desde donde se ejecuta el script. Por eso debemos tener en cuenta es posible ejecutar un script sin estar en su mismo directorio y si lo hacemos esos recursos no se encontrarán. Debemos navegar hasta el programa y ejecutarlo desde su carpeta:

```bash
cd 1-2/1-2-1
python programa.py
```

Alternativamente podemos utilizar el módulo `Path` de Python para generar una ruta absoluta al recurso concreto a partir del script actual y solventar el problema para siempre. Os recomiendo crear una función como la siguiente para facilitar la reutilización:

```python
def absPath(file):
    # Devuelve la ruta absoluta a un fichero desde el propio script
    return str(Path(__file__).parent.absolute() / file)

print(absPath("naturaleza.jpg"))
imagen = QPixmap(absPath("naturaleza.jpg"))
```

Sea como sea nuestra imagen ya se muestra, pero si quisiéramos que se reescale junto al tamaño de la ventana deberíamos establecer el atributo `scaledContents` en `True`:

```python
# hacemos que se escale con la ventana
etiqueta.setScaledContents(True)
```



___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>