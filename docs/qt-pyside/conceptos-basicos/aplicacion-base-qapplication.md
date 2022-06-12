title: Primera aplicación QApplication | Curso Qt/PySide | Hektor Profe

# Primera aplicación QApplication

<img src="{{cdn}}/pyside/01.png">

Estructura básica de un programa en PySide usando el componente base de Qt llamado `QWidget`, un widget vacío:

```python
from PySide6.QtWidgets import QApplication, QWidget
import sys

# Creamos una aplicación para gestionar la interfaz
app = QApplication(sys.argv)

# Creamos un widget para generar la ventana
window = QWidget()

# Mostramos la ventana, se encuentra oculta por defecto
window.show()

# Iniciamos el bucle del programa
sys.exit(app.exec_())
```

Ejecutamos el programa en la terminal o en Visual Studio Code con la extensión Code Runner `F1 > Run code`:

```bash
python main.py
```

- `QApplication`: Es el núcleo de un programa en Qt, se requiere para manejar el bucle de la aplicación, encargado de gestionar todas las interacciones con la interfaz gráfica de usuario.

Una aplicación requiere por lo menos un widget para mostrar algo en pantalla. Todos los widgets que heredan de `QWidget` se pueden visualizar como ventanas en sí mismos:

```python
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

# Esta vez la ventana la maneja un widget de tipo botón
window = QPushButton("Hola mundo")
window.show()

sys.exit(app.exec_())
```

Como podéis observar esto no es muy útil, ya que toda la ventana es el botón en sí mismo.

Por suerte Qt nos ofrece un widget capaz de gestionar ventanas con multitud de funcionalidades, se llama QMainWindow, el widget para gestionar ventanas principales.

```python
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

# Ahora la ventana la gestiona el widget de ventana principal
window = QMainWindow()

# Damos un título a la ventana principal
window.setWindowTitle("Hola mundo")

window.show()

sys.exit(app.exec_())
```

Aparentemente tenemos lo mismo que al usar un `QWidget`, pero esta ventana principal nos permite asignar un widget para ocupar su espacio central:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hola mundo")

# Guardamos el botón en una variable
button = QPushButton("Soy un botón")
# Establecemos el botón como widget central de la ventana principal
window.setCentralWidget(button)

window.show()
sys.exit(app.exec_())
```



___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>