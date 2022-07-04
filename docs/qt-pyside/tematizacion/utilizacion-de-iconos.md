title: Utilización de iconos | Curso Qt/PySide | Hektor Profe

# Utilización de iconos

<img src="{{cdn}}/pyside/32.png">

Anteriormente ya hemos utilizado algunos iconos cargándolos como recursos externos, pero Qt incluye un set de iconos predeterminados. Podemos hacer uso de ellos de la siguiente forma:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle)  # edited
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # recuperamos el icono de la libería estandard de la ventana
        icono = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        # lo podemos asignar a un botón
        boton = QPushButton(icono, "Botón guardar")

        self.setCentralWidget(boton)
```

He creado un pequeño programa para visualizar los iconos de la librería estandar dinámicamente, os lo adjunto en los recursos:

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)
import sys

iconos = ['SP_ArrowBack', 'SP_ArrowDown', 'SP_ArrowForward', 'SP_ArrowLeft', 'SP_ArrowRight', 'SP_ArrowUp', 'SP_BrowserReload', 'SP_BrowserStop', 'SP_CommandLink', 'SP_ComputerIcon', 'SP_CustomBase', 'SP_DesktopIcon', 'SP_DialogApplyButton', 'SP_DialogCancelButton', 'SP_DialogCloseButton', 'SP_DialogDiscardButton', 'SP_DialogHelpButton', 'SP_DialogNoButton', 'SP_DialogOkButton', 'SP_DialogOpenButton', 'SP_DialogResetButton', 'SP_DialogSaveButton', 'SP_DialogYesButton', 'SP_DirClosedIcon', 'SP_DirHomeIcon', 'SP_DirIcon', 'SP_DirLinkIcon', 'SP_DirOpenIcon', 'SP_DockWidgetCloseButton', 'SP_DriveCDIcon', 'SP_DriveDVDIcon', 'SP_DriveFDIcon', 'SP_DriveHDIcon', 'SP_DriveNetIcon', 'SP_FileDialogBack', 'SP_FileDialogContentsView', 'SP_FileDialogDetailedView', 'SP_FileDialogEnd', 'SP_FileDialogInfoView', 'SP_FileDialogListView', 'SP_FileDialogNewFolder', 'SP_FileDialogStart', 'SP_FileDialogToParent', 'SP_FileIcon', 'SP_FileLinkIcon', 'SP_MediaPause', 'SP_MediaPlay', 'SP_MediaSeekBackward', 'SP_MediaSeekForward', 'SP_MediaSkipBackward', 'SP_MediaSkipForward', 'SP_MediaStop', 'SP_MediaVolume', 'SP_MediaVolumeMuted', 'SP_MessageBoxCritical', 'SP_MessageBoxInformation', 'SP_MessageBoxQuestion', 'SP_MessageBoxWarning', 'SP_TitleBarCloseButton', 'SP_TitleBarContextHelpButton', 'SP_TitleBarMaxButton', 'SP_TitleBarMenuButton', 'SP_TitleBarMinButton', 'SP_TitleBarNormalButton', 'SP_TitleBarShadeButton', 'SP_TitleBarUnshadeButton', 'SP_ToolBarHorizontalExtensionButton', 'SP_ToolBarVerticalExtensionButton', 'SP_TrashIcon', 'SP_VistaShield']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creo un layaout en cuadrícula
        layout = QGridLayout()

        # recorro los iconos con un contador de posicion
        for contador, nombre in enumerate(iconos):
            # recupero el icono a partir de su nombre
            icono = self.style().standardIcon(getattr(QStyle, nombre))
            # creo un botón con el icono y su nombre del icono
            boton = QPushButton(icono, nombre)
            # añado el boton en una cuadrícula de 5 columnas
            # divido el contador entre 5 para conseguir la fila
            # con el módulo de la divisón entre 5 conseguiré la columna
            layout.addWidget(boton, contador // 5, contador % 5)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
```

Si necesitamos más iconos podemos imporarlos de recursos externos como ya vimos, o utilizar una colección como `qtawesome`. Lo malo es que a fecha de creación del curso esta colección todavía no está soportada por `PySide6`, podemos usarla cambiando las importaciones a `PySide2` si lo tenemos instalado:

```bash
pip install pyside2 qtawesome
```

Para recuperar los iconos es muy fácil:

```python
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton)  # edited PySide2
import sys
import qtawesome as qta


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # recuperamos un icono de qta y lo añadimos a un botón
        icono = qta.icon('fa5b.github')
        boton = QPushButton(icono, "Github")

        self.setCentralWidget(boton)
```

Podéis encontrar información sobre como personalizar los iconos y las colecciones disponibles en el repositorio de [qtawesome](https://github.com/spyder-ide/qtawesome#supported-fonts).



___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>