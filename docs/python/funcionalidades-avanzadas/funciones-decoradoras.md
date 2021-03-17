title: Funciones decoradoras | Curso de Python | Hektor Profe
description: Operadores encadenados, comprensión de listas, funciones decoradoras, generadoras, iteradoras, lambda y expresiones regulares.

# Funciones decoradoras

No cabe duda de que Python es un lenguaje flexible, y cuando trabajamos con funciones no es una excepción.

En Python, dentro de una función podemos definir otras funciones. Con la peculiaridad de que el ámbito de estas funciones se encuentre únicamente dentro de la función padre. Vamos a trabajar los ámbitos un poco más en profundidad:

!!! info "" 
    
    ```python
    def hola():
        
        def bienvenido():
            return "Hola!"
        
        return bienvenido
    ```

Si intentamos llamar a la función bienvenido...

!!! info "" 
    
    ```python
    bienvenido()
    ```

    ```
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-3-f083d151b813> in <module>()
    ----> 1 bienvenido()

    NameError: name 'bienvenido' is not defined
    ```

Como vemos nos da un error de que no existe. En cambio si intentamos ejecutar la función **hola()**:

!!! info "" 
    
    ```python
    hola()
    ```

    ```
    <function __main__.hola.<locals>.bienvenido>
    ```

Se devuelve la función bienvenido, y podemos apreciar dentro de su definición que existe un espacio llamado **locals**, el cual hace referencia al ámbito local que abarca la función.

## Ámbito local y global

Si utilizamos una función reservada **locals()** obtendremos un diccionario con todas las definiciones dentro del espacio local del bloque en el que estamos:

!!! info "" 
    
    ```python
    def hola():
        
        def bienvenido():
            return "Hola!"
        
        print( locals() )  # Mostramos el ámbito local

    hola()
    ```

    ```
    {'bienvenido': <function hola.<locals>.bienvenido at 0x000001F867E88C80>}
    ```

Como vemos se nos muestra un diccionario, aquí encontraremos la función **bienvenido()**.

Podríamos añadir algo más:

!!! info "" 
    
    ```python
    lista = [1,2,3]

    def hola():
        
        numero = 50
        
        def bienvenido():
            return "Hola!"
        
        print( locals() )  # Mostramos el ámbito local

    hola()
    ```

    ```
    {'bienvenido': <function hola.<locals>.bienvenido at 0x000001F867E88950>, 'numero': 50}
    ```

Como podemos observar, ahora además de la función tenemos una clave con el número y el valor 50. Sin embargo no encontramos la lista, pues esta se encuentra fuera del ámbito local. De hecho se encuentra en el ámbito global, el cual podemos mostrar con la función reservada **globals()**:

!!! info "" 
    
    ```python
    # Antes de ejecutar el bloque reinicia el Notebook para vaciar la memoria
    lista = [1,2,3]

    def hola():
        
        numero = 50
        
        def bienvenido():
            return "Hola!"
        
        print( globals() )  # Mostramos el ámbito global

    hola()
    ```

    ```
    {'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', '# Antes de ejecutar este bloque reinicia el Notebook para vaciar la memoria.\nlista = [1,2,3]\n\ndef hola():\n    \n    numero = 50\n    \n    def bienvenido():\n        return "Hola!"\n    \n    print( globals() )  # Mostramos el ámbito global\n\nhola()'], '_oh': {}, '_dh': ['C:\\Users\\hcost\\CursoPython\\Fase 4 - Temas avanzados\\Tema 15 - Funcionalidades avanzadas\\Apuntes'], 'In': ['', '# Antes de ejecutar este bloque reinicia el Notebook para vaciar la memoria.\nlista = [1,2,3]\n\ndef hola():\n    \n    numero = 50\n    \n    def bienvenido():\n        return "Hola!"\n    \n    print( globals() )  # Mostramos el ámbito global\n\nhola()'], 'Out': {}, 'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001D9380544A8>>, 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x000001D9380B4BA8>, 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x000001D9380B4BA8>, '_': '', '__': '', '___': '', '_i': '', '_ii': '', '_iii': '', '_i1': '# Antes de ejecutar este bloque reinicia el Notebook para vaciar la memoria.\nlista = [1,2,3]\n\ndef hola():\n    \n    numero = 50\n    \n    def bienvenido():\n        return "Hola!"\n    \n    print( globals() )  # Mostramos el ámbito global\n\nhola()', 'lista': [1, 2, 3], 'hola': <function hola at 0x000001D9381A3A60>}
    ```

Tampoco es necesario que nos paremos a analizar el contenido, pero como podemos observar, desde el ámbito global tenemos acceso a muchas más definiciones porque engloba a su vez todas las de sus bloques padres. 

Si mostramos únicamente las claves del diccionario **globals()**, quizá sería más entendible:

!!! info "" 
    
    ```python
    globals().keys()
    ```

    ```
    dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtin__', '__builtins__', '_ih', '_oh', '_dh', 'In', 'Out', 'get_ipython', 'exit', 'quit', '_', '__', '___', '_i', '_ii', '_iii', '_i1', 'lista', 'hola', '_i2'])
    ```

Ahora si buscamos bien encontraremos la clave **lista**, la cual hace referencia a la variable declarada fuera de la función. Incluso podríamos acceder a ella como si fuera un diccionario normal:

!!! info "" 
    
    ```python
    # Desde la función globals
    globals()['lista']  
    ```

    ```
    [1, 2, 3]
    ```

!!! info "" 
    
    ```python
    # Forma tradicional
    lista  
    ```

    ```
    [1, 2, 3]
    ```

## Funciones como variables

Volviendo a nuestra función **hola()**, ahora sabemos que si la ejecutamos, en realidad estamos accediendo a su función local  **bienvenido()**, pero eso no significa que la ejecutamos, sólo estamos haciendo referencia a ella.

Esa es la razón de que se devuelva su definición y no el resultado de su ejecución:

!!! info "" 
    
    ```python
    def hola():
        
        def bienvenido():
            return "Hola!"
        
        return bienvenido

    hola()
    ```

    ```
    <function __main__.hola.<locals>.bienvenido>
    ```

Por muy raro que parezca, podríamos ejecutarla llamando una segunda vez al paréntesis. La primera para **hola()** y la segunda para **bienvenido()**:

!!! info "" 
    
    ```python
    hola()()
    ```

    ```
    'Hola!'
    ```

Como es realmente extraño, normalmente lo que hacemos es asignar la función a una variable y ejecutarla como si fuera una nueva función:

!!! info "" 
    
    ```python
    bienvenido = hola()
    bienvenido()
    ```

    ```
    'Hola!'
    ```

A diferencia de las colecciones y los objetos, donde las copias se utilizaban como accesos directos, las copias de las funciones son independientes y aunque borrásemos la original, la nueva copia seguiría existiendo:

!!! info "" 
    
    ```python
    del(hola)
    bienvenido()
    ```

    ```
    'Hola!'
    ```

## Funciones como argumentos

Si ya era extraño ejecutar funciones anidadas, todavía es más extraño el concepto de enviar una función como argumento de otra función, sin embargo gracias a la flexibilidad de Python es posible hacerlo:

!!! info "" 
    
    ```python
    def hola():
        return "Hola!"

    def test(funcion):
        print( funcion() )
        
    test(hola)
    ```

    ```
    Hola Mundo
    ```

Quizá en este momento no se ocurren muchas utilidades para esta funcionalidad, pero creedme que es realmente útil cuando queremos extender funciones ya existentes sin modificarlas. De ahí que este proceso se conozca como un decorador, y de ahí pasamos directamente a las funciones decoradoras.

## Funciones decoradoras

Una función decoradora es una función que envuelve la ejecución de otra función y permite extender su comportamiento. Están pensadas para reutilazarlas gracias a una sintaxis de ejecución mucho más simple.

Imaginaros estas dos funciones sencillas:

!!! info "" 
    
    ```python
    def hola():
        print("Hola!")

    def adios():
        print("Adiós!")
    ```

Y queremos queremos crear un decorador para monitorizar cuando se ejecutan las dos funciones, avisando antes y después. 

Para crear una función decoradora tenemos que recibir la función a ejecutar, y envolver su ejecución con el código a extender:

!!! info "" 
    
    ```python
    def monitorizar(funcion):

        def decorar():
            print("\t* Se está apunto de ejecutar la función:", 
                funcion.__name__)
            funcion()
            print("\t* Se ha finalizado de ejecutar la función:", 
                funcion.__name__)

        return decorar

    def adios():
        print("Adiós!")
    ```

Ahora para realizar la monitorización deberíamos llamar al monitor ejecutando la función enviada y devuelta:

!!! info "" 
    
    ```python
    monitorizar(hola)()
    ```

    ```
        * Se está apunto de ejecutar la función: hola
    Hola!
        * Se ha finalizado de ejecutar la función: hola
    ```

Sin embargo esto no es muy cómodo, y ahí es cuando aparece la sintaxis que nos permite configurar una función decoradora en una función normal:

!!! info "" 
    
    ```python
    @monitorizar
    def hola():
        print("Hola!")

    @monitorizar
    def adios():
        print("Adiós!")
    ```

Una vez configurada la función decoradora, al utilizar las funciones se ejecutarán automáticamente dentro de la función decoradora:

!!! info "" 
    
    ```python
    hola()
    print()
    adios()
    ```

    ```
        * Se está apunto de ejecutar la función: hola
    Hola!
        * Se ha finalizado de ejecutar la función: hola

        * Se está apunto de ejecutar la función: adios
    Adiós!
        * Se ha finalizado de ejecutar la función: adios
    ```

## Paso de argumentos

!!! info "" 
    
    ```python
    def monitorizar_args(funcion):

        def decorar(*args,**kwargs):
            print("\t* Se está apunto de ejecutar la función:", 
                funcion.__name__)
            funcion(*args,**kwargs)
            print("\t* Se ha finalizado de ejecutar la función:", 
                funcion.__name__)

        return decorar

    @monitorizar_args
    def hola(nombre):
        print("Hola {}!".format(nombre))

    @monitorizar_args
    def adios(nombre):
        print("Adiós {}!".format(nombre))
        
    hola("Héctor")
    print()
    adios("Héctor")
    ```

    ```
        * Se está apunto de ejecutar la función: hola
    Hola Héctor!
        * Se ha finalizado de ejecutar la función: hola

        * Se está apunto de ejecutar la función: adios
    Adiós Héctor!
        * Se ha finalizado de ejecutar la función: adios
    ```

Ahora ya sabes qué son las funciones decoradoras y cómo utilizar el símbolo @ para automatizar su ejecución. Estas funciones se utilizan mucho cuando trabajamos con Frameworks Web como Django, así que seguro te harán servicio si tienes pensado aprender a utilizarlo.

___
<small class="edited"><i>Última edición: 6 de Octubre de 2018</i></small>