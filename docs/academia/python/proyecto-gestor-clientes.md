title: Proyecto gestor de clientes | Python | Academia | Hektor Profe
description: Vamos a crear un proyecto utilizando los conceptos básicos: variables, colecciones, condiciones, bucles, funciones y módulos.

# Proyecto gestor de clientes en Python

<div class="contenedor_youtube">
  <iframe width="838" height="470" src="https://www.youtube.com/embed/LcGAfpQSkMU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Vamos a crear un programa poniendo a prueba lo básico de Python que mostrará un menú con estas opciones:

* Listar todos los clientes del gestor.
 * Consultar un cliente a partir de su **dni**.
* Agregar clientes con los campos **nombre**, **apellido**, **dni**.
* Modificar el nombre y apellido de un cliente a partir de su **dni**.
* Borrar un cliente a partir de su **dni**.
* Salir del programa.

No deberá guardar los datos en el disco duro, siempre partirá de unos clientes de prueba iniciales y no podrá haber dos clientes con el mismo **dni**.

**Repositorio**: <a href="https://github.com/hektorprofe/curso-gestor-clientes-python" target="_blank">https://github.com/hektorprofe/curso-gestor-clientes-python</a>

## Organizando el proyecto

Empezaremos creando una carpeta **Gestor de clientes** con un fichero **requirements.txt** y otro **README.md** ambos vacíos, además de una carpeta llamada **gestor/** para contener los scripts de nuestro proyecto.

Esta organización es una buena práctica para ahorrar problemas en el futuro ya que permite añadir todo lo que necesitemos en la raíz externa sin molestar al código fuente, como por ejemplo documentación, pruebas, configuraciones, etc. Es la clave para mentener un proyecto organizado y extensible.

Así que vamos a separar el inicial en dos ficheros, uno con el núcleo del programa y otro para las funciones auxiliares:

Uno para el fichero principal:

`gestor/core.py`
```python
""" Fichero principal del programa"""

def main():
    # TODO: Aquí se mostrará el menú
    pass
  
if __name__== "__main__":
    main()
```

Y otro para las funciones auxiliares:

`gestor/helpers.py`
```python
""" Funciones de ayuda """
```

## Creando el menú

Vamos a por nuestro menú, pero en lugar de añadirlo en el núcleo vamos a hacerlo en su propio módulo. Recordad, cuanto más separado y organizado esté el código más reutilizable y extensible será el programa:

`gestor/menu.py`
```python
""" Menú del programa """
import os

def loop():
    while True:
        os.system('cls')  # 'clear' para Linux y OS X

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        os.system('cls')  # 'clear' para Linux y OS X

        if option == '1':
            print("Listando los clientes...\n")
            # TODO
        if option == '2':
            print("Mostrando un cliente...\n")
            # TODO
        if option == '3':
            print("Modificando un cliente...\n")
            # TODO
        if option == '4':
            print("Modificando un cliente...\n")
            # TODO
        if option == '5':
            print("Borrando un cliente...\n")
            # TODO
        if option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")
```

Para probarlo podemos añadirlo a la función principal impórtándolo cómodamente:

`gestor/core.py` 
```python
""" Fichero principal del programa"""

import menu

def main():
    menu.loop()

if __name__ == "__main__":
    main()
```

## Primera función auxiliar

Es un buen momento para crear una función auxiliar, así veréis su utilidad.

Vamos a crear una función mejorada para limpiar la terminal porque la que tenemos no detecta automáticamente el sistema operativo y uno de los puntos fuertes de Python es que es multiplataforma así que aprovechémonos de eso.

`gestor/helpers.py`
```python
""" Funciones de ayuda """

import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
```

Ahora podemos cargar el módulo cómodamente y ejecutar la función en el menú en lugar de llamar directamente al módulo **os**:

`gestor/menu.py`
```python
import helpers

# os.system('cls')
helpers.clear()
```

## Gestionando clientes

Es momento de empezar a gestionar clientes y una forma interesante de manejarlos es en una lista representándolos con diccionarios con tres claves: **nombre**, **apellido** y **dni**.

Podríamos crear la lista de base en el propio menú pero no es el lugar adecuado, a fin de cuentas el menú debería simplemente llamar las acciones del gestor pero no contener variables relacionadas directamente con los clientes.

Así que vamos a crear un nuevo módulo para nuestro gestor. En él definiremos una lista y añadiremos algunos clientes de prueba, lo que en POO se conoce como [objetos simulados](https://es.wikipedia.org/wiki/Objeto_simulado), para nosotros serán unos simples diccionarios:

`gestor/manager.py`
```python
""" Administrador de clientes """

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'dni': '15J'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'dni': '48H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'dni': '28Z'})
```

Con esto ya tenemos los datos de prueba.

## Listando los clientes

Vamos a implementar ahora una forma de listar todos los clientes creando una función que recorra la lista y los muestre uno por uno. Para ello podemos ayudarnos de una función que muestre un único usuario de la forma que nosotros queramos, así podremos cambiarla en cualquier momento para adaptarla:

```python
def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")


def show_all():
    for client in clients:
        show(client)
```

Para utilizar este módulo simplemente lo importaremos, eso creará la lista de clientes con los datos de prueba y nos permitirá llamar la función **show_all**:

`gestor/menu.py`
```python
""" Menú del programa """

import helpers
import manager

# ...

if option == '1':
    print("Listando los clientes...\n")
    manager.show_all()
```

¿Véis qué cómodo es todo utilizando módulos?

## Consultando un cliente

Para consultar un cliente necesitaremos recorrer la lista en busca de un DNI y devolverlo si concuerda, podemos hacerlo con una función **find** que muestre el cliente y lo devuelva en caso de encontrarlo:

`gestor/manager.py`
```python
def find():

    dni = input("Introduce el DNI del cliente\n> ")

    for client in clients:
        if client['dni'] == dni:
            show(client)
            return client

    print("No se ha encontrado ningún cliente con ese DNI")
```

Y la añadimos a nuestro menú:

`gestor/menu.py`
```python
if option == '2':
    print("Mostrando un cliente...\n")
    manager.find()
```

## Añadiendo clientes 

Para añadir usuarios necesitaremos validar los tres campos del cliente:

* **nombre**: Mínimo de 2 caracteres y máximo de 30. 
* **apellidos**: Mínimo de 2 caracteres y máximo de 30. 
* **dni**: Debe tener 3 caracteres (es una prueba), dos números y una mayúscula al final. 

Creo que sería una buena idea ayudarnos de una función auxiliar que se encargue  de leer los valores por teclado y comprobar que tengan la longitud mínima y máxima que nosotros les indiquemos:

`gestor/helpers.py`
```python
def input_text(min_length, max_length):
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text
```

Además también tenemos que validar el **dni**, un campo especial que debe tener un patrón de dos números y una mayúsculas y no se puede repetir. Para crear el patrón podemos usar una sencilla expresión regular y testear algunos ejemplos de prueba en la documentación haciendo unos **doctests**:

`gestor/manager.py`
```python
def is_valid(dni):
    """
    >>> is_valid('48H')  # No válido, en uso
    False
    >>> is_valid('X82')  # No válido, incorrecto
    False
    >>> is_valid('21A')  # Válido
    True
    """

    # Comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['dni'] == dni:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Podemos ejecutar las pruebas ejecutando el script con el argumento **-v**:

```bash
python manage.py -v
```

Ya lo tenemos todo listo, en la siguiente sección crearemos la función para añadir el nuevo cliente.

Bien vamos a hacer uso de estos validadores que hemos creado para añadir usuarios:

`gestor/manager.py`
```python
def add():

    client = dict()

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce DNI (2 números y 1 carácter en mayúscula)")
        dni = helpers.input_text(3, 3)
        if is_valid(dni):
            client['dni'] = dni
            break
        print("DNI incorrecto o en uso")

    clients.append(client)
    return client
```

Si devolvemos el cliente creado podemos guardar el resultado de **add()** en una variable para acceder a sus campos si queremos, aunque por ahora no lo necesitamos:

`gestor/menu.py`
```python
if option == '3':
    print("Añadiendo un cliente...\n")
    manager.add()
    print("Cliente añadido correctamente\n")
```

## Modificando clientes

Para modificar un cliente lo que haremos es recorrer la lista enumerando los valores con índices, así podremos acceder a los diccionarios de los clientes. Una vez tengamos recuperado el cliente a partir de su **dni** leeremos de nuevo sus campos haciendo lo mismo que en el **add**:

`gestor/manager.py`
```python
def edit():
    dni = input("Introduce el DNI del cliente\n> ")
    for i, client in enumerate(clients):
        if client['dni'] == dni:
            print(f"Introduce nuevo nombre ({client['nombre']})")
            clients[i]['nombre'] = helpers.input_text(2, 30)
            print(f"Introduce nuevo apellido ({client['apellido']})")
            clients[i]['apellido'] = helpers.input_text(2, 30)
            return True
    return False
```

El **dni** no vamos a permitir modificarlo porque sería un rollo a nivel de validaciones, es mejor borrar el cliente y crearlo de nuevo tal como haremos en la siguiente lección.

Por ahora vamos a añadir esta función a nuestro menú y a probar si funciona:

`gestor/menu.py`
```python
if option == '4':
    print("Modificando un cliente...\n")
    if manager.edit():
        print("Cliente modificado correctamente\n")
```

## Borrando clientes

Por último la opción de borrar un cliente de la lista a partir de su **dni** es bastante simple, pues podemos hacerlo con el método **pop()** pasándole el índice donde se encuentra el diccionario que queremos borrar, algo que podemos saber fácilmente haciendo una enumeración de la lista:

`gestor/manager.py`
```python
def delete():
    dni = input("Introduce el DNI del cliente\n> ")
    for i, client in enumerate(clients):
        if client['dni'] == dni:
            client = clients.pop(i)
            show(client)
            return True
    return False
```

Y la añadimos al menú:

`gestor/menu.py`
```python
if option == '5':
    print("Borrando un cliente...\n")
    if manager.delete():
        print("Cliente borrado correctamente\n")
```

## Refactorización

Creo que podemos refactorizar un poco esos enumeradores. Si devolviéramos también el índice en nuestra función **find** podríamos reutilizarla, así que vamos a hacer un enumerador ahí y devolvámoslo:

`gestor/manager.py`
```python
def find():
    dni = input("Introduce el DNI del cliente\n> ")
    for i, client in enumerate(clients):
        if client['dni'] == dni:
            show(client)
            return i, client
    print("No se ha encontrado ningún cliente con ese DNI")
```

Ahora podemos reutilizar los bucles en las funciones **edit** y **delete**:

`gestor/manager.py`
```python
def edit():
    i, client = find()
    if client:
        print(f"Introduce nuevo nombre ({client['nombre']})")
        clients[i]['nombre'] = helpers.input_text(2, 30)
        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2, 30)
        return True

    return False

def delete():
    i, client = find()
    if client:
        client = clients.pop(i)
        return True
    return False
```

Y con esto acabamos.

___
<small class="edited"><i>Última edición: 16 de Marzo de 2021</i></small>