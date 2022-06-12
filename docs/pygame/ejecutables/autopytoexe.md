title: Ejecutable con Auto-py-to-exe | Curso PyGame | Hektor Profe
description: Apuntes del curso de desarrollo de videojuegos con PyGame en Python.

# Ejecutable con Auto-Py-to-Exe

Volviendo a la organización que os enseñé hace alguna unidades:

```
Game/
    requirements.txt    # dependencias
    game/
        main.py         # principal
```

Vamos a crear un entorno virtual con Pipenv en la raíz del proyecto.

Para ello necesitamos instalar Pipenv si no lo tenemos:

```
pip install pipenv
```

Ahora configuramos el `requirements.txt` con los paquetes mínimos necarios:

```json
pygame==2.1.2
pygame_gui==0.6.4
```

Y creamos en `Game\` el entorno virtual a partir del requirements:

```bash
cd Game
pipenv install -r requirements.txt
```

Esto creará en la raíz un `Pipfile` y un `Pipfile.lock`.

A continuación instalamos en ese entorno virtual `auto-py-to-exe` para generar el ejecutable:

```bash
cd Game
pipenv install auto-py-to-exe
```

Y ejecutamos el programa en este entorno con los paquetes mínimos:

```bash
cd Game
pipenv run auto-py-to-exe
```

En la pantalla web del programa seleccionaremos:

- **Script Location** será el `main.py` del videojuego.
- **One Directory** (OneFile podría no funcionar o requerir directorios).
- **Console Window Based**.
- **Additional Files** añadiremos el directorio `res` de recursos externos.
- **Icon** si tenemos una imagen ico para el ejecutable.

Antes de continuar observemos un instante que en la parte inferior nos aparece el comando:

```bash
pyinstaller --noconfirm --onedir --windowed --add-data
"C:/Users/hcost/Projects/curso_pygame/08_Distro/Game/game/res;res/"
"C:/Users/hcost/Projects/curso_pygame/08_Distro/Game/game/main.py"
```

Esto se muestra porque en realidad se utiliza este programa llamado pyinstaller para generar los ejecutables, y ese es el comando para generarlos.

Le damos a convert `.py` to `.exe`, en otras plataformas creará el ejecutable pertinente sin la extensión exe.

El ejecutable se generará en el directorio Output dentro de una carpeta llamada main y podremos ejecutar con el ejecutable `main.exe` de su interior, que si todo es correcto debería lanzar el videojuego.

El tamaño puede ser algo grande para lo que aparentemente es el juego, eso es porque el ejecutable incluye el intérprete de Python y las dependencias como **PyGame GUI**.

Concretamente dentro de `pygame_gui/data` encontraremos un montón de fuentes que, dado que no estamos utilizando, podemos borrar.

Al hacerlo el tamaño del directorio pasará de 47MB a 21MB, que comprimidos en un ZIP o 7ZIP baja a 11MB u 8MB respectivamente.

___
<small class="edited"><i>Última edición: 13 de Febrero de 2022</i></small>