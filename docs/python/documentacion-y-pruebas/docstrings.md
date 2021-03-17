title: Docstrings | Curso de Python | Hektor Profe
description: En esta sección repasamos los módulos Docstring, Pydoc, Doctest y Unittest de Python.

En Python todos los objetos cuentan con una variable especial llamada __doc__ gracias a la que podemos describir para qué sirven los y cómo se usan los objetos. Estas variables reciben el nombre de *docstrings*, cadenas de documentación.

## Funciones

Python implementa un sistema muy sencillo para establecer el valor de las docstrings, únicamente tenemos que crear un comentario en la primera línea después de la declaración.

!!! info "" 
    
    ```python
    def hola(arg):
        """Este es el docstring de la función"""
        print("Hola", arg, "!")
        
    hola("Héctor")
    ```

    ```
    Hola Héctor !
    ```

Para consultar la documentación es tan sencillo como utilizar la función reservada **help** y pasarle el objeto:

!!! info "" 
    
    ```python
    help(hola)
    ```

    ```bash
    Help on function hola in module __main__:

    hola(arg)
        Este es el docstring de la función
    ```

## Clases y métodos

De la misma forma podemos establecer la documentación de la clase después de la definición, y de los métodos, como si fueran funciones:

!!! info "" 
    
    ```python
    class Clase:
        """ Este es el docstring de la clase"""
        def __init__(self):
            """Este es el docstring del inicializador de clase"""
        def metodo(self):
            """Este es el docstring del metodo de clase"""

    o = Clase()
    help(o)
    ```

    ```bash
    Help on Clase in module __main__ object:

    class Clase(builtins.object)
     |  Este es el docstring de la clase
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Este es el docstring del inicializador de clase
     |  
     |  metodo(self)
     |      Este es el docstring del metodo de clase
    ```

## Scripts y módulos

Cuando tenemos un script o módulo, la primera línea del mismo hará referencia al docstring del módulo, en él deberíamos explicar el funcionamiento del mismo: 

!!! info "" 
    
    ```python
    """Este es el docstring del módulo"""
    def despedir():
        """Este es el docstring de la función despedir"""
        print("Adiós! Me despido desde la función despedir() del módulo prueba")
    def saludar():
        """Este es el docstring de la función saludar"""
        print("Hola! Te saludo desde la función saludar() del módulo prueba")
    ```

!!! info "" 
    
    ```python
    import mi_modulo
    
    help(mi_modulo)
    ```

    ```bash
    Help on module mi_modulo:

    NAME
        mi_modulo - Este es el docstring del módulo
    FUNCTIONS
        despedir()
            Este es el docstring de la función despedir
        saludar()
            Este es el docstring de la función saludar
    ```

!!! info "" 
    
    ```python
    help(mi_modulo.despedir)
    ```

    ```
    Help on function despedir in module mi_modulo:

    despedir()
        Este es el docstring de la función despedir
    ```

Como dato curioso, también podemos listar las variables y funciones del módulo con **dir()**:

!!! info "" 
    
    ```python
    dir(mi_modulo)
    ```

    ```
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'despedir',
     'saludar']
    ```

Como vemos muchas de ellas son especiales, seguro que muchas os suenan, os invito a comprobar sus valores:

!!! info "" 
    
    ```python
    print(mi_modulo.__name__)     # Nombre del módulo
    print(mi_modulo.__doc__)      # Docstring del módulo
    print(mi_modulo.__package__)  # Nombre del paquete del módulo
    ```

    ```
    'mi_modulo'
    Este es el docstring del módulo

    ```

## Paquetes

En el caso de los paquetes el docstring debemos establecerlo en la primera línea del inicializador:

`__init__.py`

!!! info "" 
    
    ```python
    """Este es el docstring de mi_paquete"""
    ```
    
    ```python
    import mi_paquete

    help(mi_paquete)
    ```

    ```bash
    Help on package mi_paquete:

    NAME
        mi_paquete - Este es el docstring de mi_paquete
    PACKAGE CONTENTS
        adios (package)
        hola (package)
    ```

## Ejemplos

Podéis aprender a crear buena documentación tomando como referencia contenido de las librerías internas de Python:

!!! info "" 
    
    ```python
    help(print)
    ```

    ```bash
    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    ```

!!! info "" 
    
    ```python
    help(len)
    ```

    ```bash
    Help on built-in function len in module builtins:

    len(obj, /)
        Return the number of items in a container.
    ```

!!! info "" 
    
    ```python
    help(str)
    ```

    ```bash
    Help on class str in module builtins:

    class str(object)
     |  str(object='') -> str
     |  str(bytes_or_buffer[, encoding[, errors]]) -> str
    ```

!!! info "" 
    
    ```python
    import datetime

    help(datetime)
    ```

    ```bash
    Help on module datetime:

    NAME
        datetime - Fast implementation of the datetime type.
    CLASSES
        builtins.object
            date
                datetime
    ```

Recordad, una buena documentación siempre dará respuesta a las dos preguntas: 

* ¿Para qué sirve?
* ¿Cómo se utiliza?

___
<small class="edited"><i>Última edición: 6 de Octubre de 2018</i></small>