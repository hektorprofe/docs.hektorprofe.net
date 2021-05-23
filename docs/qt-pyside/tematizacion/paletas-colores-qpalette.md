title: Paletas de colores (QPalette) | Curso Qt/PySide | Hektor Profe

# Paletas de colores (QPalette)

La selección de colores que utiliza Qt para dibujar los componentes se maneja en paletas.

Vamos a experimentar con la paleta de colores de la aplicación de la lección anterior:

```python
from PySide6.QtGui import QPalette, QColor  # nuevo

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # creamos nuestra paleta de colores
    paleta = QPalette()
    paleta.setColor(QPalette.Window, QColor(51, 51, 51))
    paleta.setColor(QPalette.WindowText, QColor(235, 235, 235))

    # activamos la paleta en la aplicación
    app.setPalette(paleta)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

Como véis las paletas tienen accesores para establecer los colores de los diferentes componentes. He encontrado una paleta llamada [Dark Fusion](https://gist.github.com/lschmierer/443b8e21ad93e2a2d7eb) bastante chula para cambiar la apariencia a modo oscuro, os la dejo en los recursos, así como un enlace a la [documentación](https://doc.qt.io/qt-6/qpalette.html#ColorRole-enum) con los atributos configurables de la paleta:

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # dark fusion https://gist.github.com/lschmierer/443b8e21ad93e2a2d7eb
    app.setStyle("Fusion")
    dark_fusion = QPalette()
    dark_fusion.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.WindowText, Qt.white)
    dark_fusion.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    dark_fusion.setColor(QPalette.ToolTipText, Qt.white)
    dark_fusion.setColor(QPalette.Text, Qt.white)
    dark_fusion.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.ButtonText, Qt.white)
    dark_fusion.setColor(QPalette.BrightText, Qt.red)
    dark_fusion.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_fusion.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    dark_fusion.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_fusion.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    dark_fusion.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    # activamos la paleta en la aplicación
    app.setPalette(dark_fusion)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>