title: Instalación y configuración de PySide | Curso Qt/PySide | Hektor Profe

# Instalación y configuración de PySide

Desde la terminal re/instalamos Pyside6:

```bash
pip install pyside6
```

Esto dará la ruta al directorio, la copiamos y abrimos:

```bash
c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages

explorer .
```

Buscamos la carpeta `PySide6`y dentro encontramos:

- `designer.exe`: Diseñador de interfaces gráficas.
- `uic.exe`: Compilador de interfaces de usuario.
- `rcc.exe`: Compilador de recursos.

Mi recomendación es añadir esta ruta al path del usuario para poder acceder cómodamente a al diseñador y las herramientas de compilación:

1. Clic derecho en Inicio > Sistema
2. Bajamos hasta encontrar "Configuración avanzada del sistema"
3. Variables de enterno > Editar variables de usuario > Path > Nuevo
4. Pegamos la carpeta de PySide6:

```
c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages\pyside6
```

Guardamos y reiniciamos las terminales y los editores.

Ahora podemos ejecutar desde cualquier lugar los ejecutables:

- `designer.exe`: Diseñador de interfaces gráficas.
- `uic.exe`: Compilador de interfaces de usuario.
- `rcc.exe`: Compilador de recursos.

Para configurar el compilador `uic` en Qt Designer

Abrimos el diseñador:

```bash
designer
```

- Fomulario > `View Python Code`

Nos indicará que se espera `uic` en el directorio `bin` del paquete `PySide6`:

```bash
cd c:\users\hcost\appdata\local\programs\python\python39\lib\site-packages\pyside6

explorer .
```

Creamos una carpeta `bin` y copiamos el fichero `uic.exe` dentro.

Listo, ya podemos previsualizar diseños en código Python y exporarlos en ficheros.

___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>