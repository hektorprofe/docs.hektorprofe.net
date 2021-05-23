title: Añadiendo funcionalidades al diseño | Curso Qt/PySide | Hektor Profe

# Añadiendo funcionalidades al diseño

Para interactuar con los componentes de la interfaz debemos acceder a ellos a partir de sus nombres de objeto, que aparecen en el inspector de objetos de Qt Designer. Podemos cambiar los nombres haciendo doble clic en ellos o utilizar los que crean por defecto.

Una vez tenemos los nombres es tan sencillo como manejar nuestras propias instancias:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox  # edited
from interfaces.mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # configuramos una señal para el botón
        self.pushButton.clicked.connect(self.mostrar_mensaje)

    def mostrar_mensaje(self):
        QMessageBox.information(
            self, "Diálogo", f"El contenido del campo de de texto es:\n\n{self.lineEdit.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

En cuanto a la acción para salir del programa, podemos recuperarla y establecer su señal tal como aprendimos al manejar los menús:

```python
# configuramos la señal de la acción para salir del programa
self.actionSalir.triggered.connect(self.close)
```

Con esto podremos cerrar la aplicación también haciendo servir el acceso directo `Control+Q` que configuramos en el diseñador.

Como véis los diseños compilados se utilizan como un programa normal, solo que la parte de generar la estructura se realiza en el fichero de diseño, un fichero que por cierto, nunca debemos editar, ya que tal como avisa en los comentarios superiores, si recompilamos la interfaz todos los cambios se perderán:

```python
# WARNING! All changes made in this file will be lost when recompiling UI file!
```

Además es buena idea tener la lógica del programa separada del diseño, esto se conoce más o menos como patrón Modelo-Vista, teniendo en el modelo la lógica del programa y en la vista el diseño del programa.

Solo me falta mostraros cómo gestionar múltiples diseños, por ejemplo una ventana principal y una subventana ambas creadas con Qt Designer.

Lo vemos en la próxima lección.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>