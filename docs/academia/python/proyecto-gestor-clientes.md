title: Proyecto gestor de clientes | Python | Academia | Hektor Profe
description: Vamos a crear un proyecto utilizando los conceptos básicos: variables, colecciones, condiciones, bucles, funciones y módulos.

# Proyecto gestor de clientes en Python

## Requisitos

Vamos a crear un programa poniendo a prueba lo que sabemos de Python:

- Listar los clientes del gestor.
- Consultar un cliente a partir del **dni**.
- Agregar un cliente con campos **nombre**, **apellido**, **dni**.
- Modificar el nombre y apellido de un cliente a partir del **dni**.
- Borrar un cliente a partir del **dni**.
- Salir del programa.

No deberá guardar los datos en el disco duro, siempre partirá de unos clientes de prueba iniciales y no podrá haber dos clientes con el mismo **dni**.

**Repositorio**: <a href="https://github.com/hektorprofe/curso-gestor-clientes-python" target="_blank">https://github.com/hektorprofe/curso-gestor-clientes-python</a>

## Organización

Empezaremos creando una carpeta **Gestor de clientes** con un fichero **requirements.txt** y otro **README.md** ambos vacíos, además de una carpeta llamada **gestor/** para contener los scripts de nuestro proyecto.

Esta organización es una buena práctica para ahorrar problemas en el futuro ya que permite añadir todo lo que necesitemos en la raíz externa sin molestar al código fuente, como por ejemplo documentación, pruebas, configuraciones, etc. Es la clave para mentener un proyecto organizado y extensible.

Así que vamos a separar el inicial en dos ficheros, uno con el núcleo del programa y otro para las funciones auxiliares:

Uno para el fichero principal:

`gestor/run.py`

```python
if __name__== "__main__":
    # TODO: Iniciar el menú
    pass
```

Y otro para las funciones auxiliares:

`gestor/helpers.py`

```python
# TODO: Funciones de ayuda
```

## Mock database

Empecemos con la base de datos del backend, que por ahora contendrá mock objects (objetos para pruebas), más adelante los refactorizaremos cambiándolos por persistencia en un fichero.

Primero la clase `Cliente`para manejar un cliente:

`gestor/database.py`

```python
class Cliente:

    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"
```

Y una clase `Clientes` para utilizar como fuente de datos y que implementará las funcionalidades de buscar, crear, actualizar y borrar clientes. Es una clase especial con funciones estáticas, eso significa que no se utilizará para crear instancias, sino que la usaremos directamente como origen único de la información:

```python
class Clientes:

    # Mock objects para hacer pruebas
    lista = [
        Cliente('15J', 'Marta', 'Perez'),
        Cliente('48H', 'Manolo', 'Lopez'),
        Cliente('28Z', 'Ana', 'Garcia')
    ]

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                return Clientes.lista[i]

    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(i)
                return cliente
```

Podemos probar los métodos abajo:

```python
if __name__ == "__main__":
    print("Buscar 15J\t", Clientes.buscar("15J"))
    print("Crear 99X\t", Clientes.crear("99X", "Hector", "Costa"))
    print("Modificar 99X\t", Clientes.actualizar("99X", "Victor", "Costa"))
    print("Borrar 48H\t", Clientes.borrar("48H"))
    print("Buscar 48H\t", Clientes.buscar("48H"))
```

Perfecto, la base de datos de prueba ya la tenemos funcionando.

## Estructurando el menú

Vamos a construir el menú, en lugar de añadirlo en el `run.py` vamos a hacerlo en su propio módulo. Recordad, cuanto más separado y organizado esté el código más reutilizable y extensible será el programa:

`gestor/menu.py`

```python
import os

def iniciar():
    while True:
        os.system('clear') # cls en Windows

        print("========================")
        print("  BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar el Manager   ")
        print("========================")

        opcion = input("> ")
        os.system('clear') # cls en Windows

        if opcion == '1':
            print("Listando los clientes...\n")
        if opcion == '2':
            print("Buscando un cliente...\n")
        if opcion == '3':
            print("Añadiendo un cliente...\n")
        if opcion == '4':
            print("Modificando un cliente...\n")
        if opcion == '5':
            print("Borrando un cliente...\n")
        if opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")
```

Para probarlo podemos añadirlo al fichero `run.py` impórtándolo cómodamente:

`gestor/run.py`

```python
import menu

if __name__ == "__main__":
    menu.iniciar()
```

## Funciones auxiliares

Es un buen momento para crear unas funciones de ayuda.

La primera será una versión mejorada para limpiar la terminal porque la que tenemos no detecta automáticamente el sistema operativo y uno de los puntos fuertes de Python es que es multiplataforma:

`gestor/helpers.py`

```python
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
```

Ahora podemos cargar el módulo cómodamente y ejecutar la función en el menú en lugar de llamar directamente al módulo **os**:

`gestor/menu.py`

```python
import helpers

helpers.limpiar_pantalla()
```

La segunda función de ayuda será para leer un texto cómodamente:

`gestor/helpers.py`

```python
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
```

La utilizaremos para leer los campos dni, nombre y apellido del cliente que vayamos a gestionar.

## Implementando el menú

Por fin ha llegado el momento de conectar la base de datos y el menú, tendremos que envolver las funcionalidades de nuestra `database` en las diferentes opciones del menú:

`gestor/menu.py`

```python
if opcion == '1':
    print("Listando los clientes...\n")
    for cliente in db.Clientes.lista:
        print(cliente)

if opcion == '2':
    print("Buscando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    cliente = db.Clientes.buscar(dni)
    print(cliente) if cliente else print("Cliente no encontrado.")

if opcion == '3':
    print("Añadiendo un cliente...\n")
    dni = helpers.leer_texto(
        3, 3, "DNI (2 ints y 1 char)").upper()
    nombre = helpers.leer_texto(
        2, 30, "Nombre (de 2 a 30 chars)").capitalize()
    apellido = helpers.leer_texto(
        2, 30, "Apellido (de 2 a 30 chars)").capitalize()
    db.Clientes.crear(dni, nombre, apellido)
    print("Cliente añadido correctamente.")

if opcion == '4':
    print("Modificando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    cliente = db.Clientes.buscar(dni)
    if cliente:
        nombre = helpers.leer_texto(
            2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
        apellido = helpers.leer_texto(
            2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
        db.Clientes.modificar(cliente.dni, nombre, apellido)
        print("Cliente modificado correctamente.")
    else:
        print("Cliente no encontrado.")

if opcion == '5':
    print("Borrando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    print("Cliente borrado correctamente.") if db.Clientes.borrar(
        dni) else print("Cliente no encontrado.")

if opcion == '6':
    print("Saliendo...\n")
    break

input("\nPresiona ENTER para continuar...")
```

## Validación del campo DNI

Hay dos cosas que tenemos comprobar para el campo DNI antes de añadir un nuevo cliente. La primera es que el DNI sea válido, es decir, cumpla un formato de dos números y una letra. La segunda es que no haya ningún otro cliente con ese DNI, así que pongámonos a ello:

`gestor/menu.py`

```python
def dni_valido(dni):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in db.Clientes.lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True
```

Esto lo utilizaremos en un bucle para leer el `dni` hasta que sea válido:

```python
if opcion == '3':
    print("Añadiendo un cliente...\n")

    # Comprobación de DNI válido
    while 1:
        dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
        if dni_valido(dni):
            break

    nombre = helpers.leer_texto(
        2, 30, "Nombre (de 2 a 30 chars)").capitalize()
    apellido = helpers.leer_texto(
        2, 30, "Apellido (de 2 a 30 chars)").capitalize()
    db.Clientes.crear(dni, nombre, apellido)
```

## Persistencia en fichero CSV

En esta lección vamos a implementar el módulo CSV, que ya vimos anteriormente en el curso, para almacenar los clientes del gestor.

Cuando el programa se ponga en marcha, la clase `database.Clientes` cargará los clientes de un fichero y los irá serializando a medida que se realicen cambios.

Para que todo funcione correctamente, trasladaremos los mock objects al fichero CSV desde el principio:

`gestor/clientes.csv`

```csv
15J;Marta;Perez
48H;Manolo;Lopez
28Z;Ana;Garcia
```

Cargaremos los clientes del fichero en la lista de `Clientes`:

```python
class Clientes:
    # Creamos la lista y cargamos los clientes en memoria
    lista = []
    with open("clientes.csv", newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
```

Esta parte ya funcionará, ahora debemos implementar el método para guardar los `Clientes` de vuelta en el fichero después de modificarlos.

Podemos crear el método:

```python
@staticmethod
def guardar():
    with open("clientes.csv", "w", newline="\n") as fichero:
        writer = csv.writer(fichero, delimiter=";")
        for c in Clientes.lista:
            writer.writerow((c.dni, c.nombre, c.apellido))
```

Lo llamamos después de `crear`, `modificar` o `borrar` un cliente:

```python
@staticmethod
def crear(dni, nombre, apellido):
    cliente = Cliente(dni, nombre, apellido)
    Clientes.lista.append(cliente)
    Clientes.guardar() # new
    return cliente

@staticmethod
def modificar(dni, nombre, apellido):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            Clientes.lista[i].nombre = nombre
            Clientes.lista[i].apellido = apellido
            Clientes.guardar() # new
            return Clientes.lista[i]

@staticmethod
def borrar(dni):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            cliente = Clientes.lista.pop(i)
            Clientes.guardar() # new
            return cliente
```

Listo, el programa ya debería sincronizar automáticamente los cambios realizados en la memoria también en el fichero CSV.

## Kit de pruebas unitarias

## Interfaz gráfica con Tkinter

---

<small class="edited"><i>Última edición: 11 de Julio de 2022</i></small>
