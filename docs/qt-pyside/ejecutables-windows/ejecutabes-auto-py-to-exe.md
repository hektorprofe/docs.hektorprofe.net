title: Ejecutables con auto-py-to-exe | Curso Qt/PySide | Hektor Profe

# Ejecutables con auto-py-to-exe

Empezamos instalando `pyside6` y `auto-py-to-exe` en un entorno virtual dentro del directorio del programa (en VSC clic derecho `Open in terminal`).

Este paso es optativo, pero si no lo hacemos el ejecutable incluirá todas las dependencias instaladas en Python. Al crear un entorno virtual con los módulos mínimos el tamaño final del ejecutable se verá reducido drásticamente:

```bash
pip install pipenv
pipenv install pyside6 auto-py-to-exe            # sin intérprete
python -m pipenv install pyside6 auto-py-to-exe  # con intérprete
```

Iniciamos la interfaz de compilación:

```bash
pipenv run auto-py-to-exe
pipenv run auto-py-to-exe            # sin intérprete
python -m pipenv run auto-py-to-exe  # con intérprete
```

En los ajustes:

- `Script Location`: Fichero principal del programa
- `Onefile`: One Directory
- `Console Window`: Window Based (hide console)
- `Additional Files/Folders`: Aquí debemos incluir todos los recursos externos no compilados y dependencias de Qt, que debemos buscar en el entorno virtual. Este paso es imprescindible dado que estamos utilizando `PySide6` y `auto-py-to-exe` no incluye automáticamente las dependencias de Qt. Para `PySide2` sí que las incluye así que con suerte en futuras actualizaciones podríamos saltarnos este paso.

Pipenv crea los entornos virtuales en el directorio del usuario, vamos a buscar las siguiente dependencias de Qt ahí, si tenemos dificultados para encontrar el directorio podemos ayudanros de Pipenv:

```bash
pipenv --venv
cd path/del/entorno
explorer .
```

Navegaremos a las dependencias de PySide6:

- `Lib/site-packages/PySide6`

Y copiamos lo siguiente al directorio output del ejecutable:

<img src="{{cdn}}/pyside/10-docs/01.png">

- Una vez configurado todo pulamos `CONVERT .PY TO .EXE` y en un rato deberíamos tener nuestro programa compilado en la carpeta `output`.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>