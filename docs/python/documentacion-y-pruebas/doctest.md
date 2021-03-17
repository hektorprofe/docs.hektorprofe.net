title: Doctest | Curso de Python | Hektor Profe
description: En esta sección repasamos los módulos Docstring, Pydoc, Doctest y Unittest de Python.

# Doctest

Si por un lado las **docstrings** nos permitían describir documentación, los **doctest** nos permiten combinar pruebas en la propia documentación.

Este concepto de integrar las pruebas en la documentación nos ayuda a mantener las pruebas actualizadas, y además nos sirve como ejemplo de utilización del código, ayudándonos a explicar su propósito.

Para utilizar **doctests** hay que inidicar una línea dentro de la documentación de la siguiente forma:

!!! info "" 
    ```python
    >>>
    ```

De esta Python entenderá que debe ejecutar el contenido dentro del comentario como si fuera código normal, y lo hará hasta que encuentre una línea en blanco (o llegue al final de la documentación).

La mejor forma de ver a **doctest** en acción.

## Definiendo pruebas

Por regla general cada prueba va ligada a una funcionalidad, pueden ser funciones, clases o sus métodos. Por ejemplo, dada una función **suma**...

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos"""
        return a+b
    ```

Para realizar una prueba dentro de la función, vamos a ejecutar un código de prueba de la propia suma:

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        >>> suma(5,10)
        """
        return a+b
    ```

Bien, ya tenemos la prueba, pero ahora nos falta indicarle a doctest cuál es el resultado que debería devolver la prueba, y eso lo indicaremos en la siguiente línea:

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        >>> suma(5,10)
        15
        """
        return a+b
    ```

¡Muy bien! Ahora tenemos que ejecutar la pruebas y ver si funciona o no, pero antes tenemos que adaptar el código.

## Pruebas en un módulo

Para ejecutar pruebas tendremos que utilizar la terminal, así vamos a guardar la función en un script **test.py** como si fuera un módulo con funciones.

Ahora justo al final indicaremos que se ejecten las pruebas doctest de las funciones del módulo escribiendo el siguiente código abajo del todo:

!!! info "" 
    ```python
    import doctest
    doctest.testmod()  # Notar que mod significa módulo
    ```

Esto sería suficiente, pero con el objetivo de evitar que este código se ejecute al importarlo desde otro lugar, se suele indicar de la siguiente forma:

!!! info "" 
    ```python
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
    ```

Así únicamente se lanzarán las pruebas al ejecutar directamente el módulo, y ya podremos ejecutar el módulo desde la terminal:

!!! info "" 
    ```bash
    python test.py
    ```

Como resultado veremos que no se muestra nada. Eso no significa que no se ejecute nuestra prueba, sino que esta ha funcionado correctamente y no hay fallos.

Si queremos podemos mostrar todo el registro de ejecución pasando un argumento -v a python justo al final:

!!! info "" 
    ```bash
    python test.py -v
    ```

Y entonces veremos el siguiente resultado:

!!! info "" 
    ```bash
    Trying:
        suma(5,10)
    Expecting:
        15
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
    1 tests in __main__.suma
    1 tests in 2 items.
    1 passed and 0 failed.
    Test passed.
    ```

En el que se prueba el código suma(5,10), se espera 15 y el resultado es ok; un resumen y finalmente Test passed.

## Creando varias pruebas

Evidentemente podemos definir múltiples pruebas. Probemos también alguna que sabemos que es incorrecta:

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        >>> suma(5,10)
        15
        
        >>> suma(0,0)
        1
        
        >>> suma(-5,7)
        2
        """
        return a+b
    ```

Ahora, si ejecutamos el script de forma normal...

!!! info "" 
    ```bash
    python test.py
    ```

A diferencia que antes sí que nos muestra algo, indicándonos que uno de los tests a fallado:

!!! info "" 
    ```bash
    **********************************************************************
    File "test.py", line 7, in __main__.suma
    Failed example:
        suma(0,0)
    Expected:
        1
    Got:
        0
    **********************************************************************
    1 items had failures:
    1 of   3 in __main__.suma
    ***Test Failed*** 1 failures.
    ```

La cuestión ahora sería revisar el test si es incorrecto, o adaptar la función para que devuelve el resultado esperado en el test. Evidentemente en este caso hemos hecho un test incorrecto a propósito así que simplemente lo borraríamos.

## Pruebas que nos guían

Una de las ventajas de usar tests es que podemos utilizarlos para detectar posibles fallas. En el siguiente ejemplo vamos a guiarnos de los tests para implementar correctamente una función.

!!! info "" 
    ```python
    def palindromo(palabra):
        """
        Comprueba si una palabra es un palíndrimo. Los palíndromos son 
        palabras o frases que se leen igual de ambos lados.
        Si es un palíndromo devuelve True y si no False

        >>> palindromo("radar")
        True
        
        >>> palindromo("somos")
        True
        
        >>> palindromo("holah")
        False
        """
        if palabra == palabra[::-1]: 
            return True
        else:
            return False
    ```

Bien, ¿pero que ocurre si hacemos el siguiente test?

!!! info "" 
    ```python
    >>> palindromo("Ana")
    True
    ```

Pues que nos falla:

!!! info "" 
    ```bash
    **********************************************************************
    File "test.py", line 11, in __main__.palindromo
    Failed example:
        palindromo("Ana")
    Expected:
        True
    Got:
        False
    **********************************************************************
    1 items had failures:
    1 of   3 in __main__.palindromo
    ***Test Failed*** 1 failures.
    ```

Claro, es que Ana empieza por mayúscula, pero hay que recordar que un palíndrimo lo es si se pronuncia igual, por tanto las mayúsculas no debes afectar. En este caso por tanto tendríamos que readaptar nuestro código para prevenir el error:

!!! info "" 
    ```python
    def palindromo(palabra):
        """
        Comprueba si una palabra es un palíndrimo. Los palíndromos son 
        palabras o frases que se leen igual de ambos lados.
        Si es un palíndromo devuelve True y si no False
        
        >>> palindromo("radar")
        True
        
        >>> palindromo("somos")
        True
        
        >>> palindromo("holah")
        False
        
        >>> palindromo("Ana")
        True
        """
        if palabra.lower() == palabra[::-1].lower(): 
            return True
        else:
            return False
    ```

Y en el test de la frase... ¿"Atar a la rata"? Esto también es un palíndromo:

!!! info "" 
    ```
    >>> palindromo("Atar a la rata")
    True
    ```

!!! info "" 
    ```
    **********************************************************************
    Failed example:
        palindromo("Atar a la rata")
    Expected:
        True
    Got:
        False
    **********************************************************************
    1 items had failures:
    1 of   4 in __main__.palindromo
    ***Test Failed*** 1 failures.
    ```

¡Nos falla de nuevo! El problema en este caso son los espacios, ya que estos no se leen pero si existen en la cadena, la frase no concuerda.

!!! info "" 
    ```python
    def palindromo(palabra):
        """
        Comprueba si una palabra es un palíndrimo. Los palíndromos son 
        palabras o frases que se leen igual de ambos lados.
        Si es un palíndromo devuelve True y si no False
        
        >>> palindromo("radar")
        True
        
        >>> palindromo("somos")
        True
        
        >>> palindromo("holah")
        False

        >>> palindromo("Atar a la rata")
        True
        """
        if palabra.lower().replace(" ", "") == 
                                    palabra[::-1].lower().replace(" ", ""): 
            return True
        else:
            return False
    ```

Todavía habría algunos casos como los acentos que nos darían fallos, pero ya véis por donde va la lógica. Se trata de guiarnos a partir de los tests para crear la función correctamente.

De hecho en el mundo de la programación hay una práctica conocida como TDD, **Test Driven Development** o **Desarrollo guiado por pruebas** que trata de escribir las pruebas primero y luego refactorizar para ir puliendo la funcionalidad.

Es una práctica algo avanzada y no la veremos en este curso, pero vale la pena comentarla.

## Tests avanzados
Hasta ahora hemos hecho unos tests muy simples, pero los **doctests** son muy flexibles. Algunas de sus funcionalidades interesantes son la posibilidad de ejecutar bloques de código o la captura de excepciones.

Para crear un test que incluya un bloque de código, debemos utilizar las sentencias anidadas para simular tabulaciones:

!!! info "" 
    ```python
    ...
    ```

!!! info "" 
    ```python
    def doblar(lista):
        """Dobla el valor de los elementos de una lista
        >>> l = [1, 2, 3, 4, 5] 
        >>> doblar(l)
        [2, 4, 6, 8, 10]
        """
        return [n*2 for n in lista]
    ```
En este caso hemos creado la lista del test manualmente, pero podríamos generarla con un bucle utilizando sentencias anidadas:

!!! info "" 
    ```python
    def doblar(lista):
        """Dobla el valor de los elementos de una lista
        >>> l = [1, 2, 3, 4, 5] 
        >>> doblar(l)
        [2, 4, 6, 8, 10]

        >>> l = [] 
        >>> for i in range(10):
        ...     l.append(i)
        >>> doblar(l)
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        """
        return [n*2 for n in lista]
    ```

Si ejecutamos el script monitorizando todo:

!!! info "" 
    ```bash
    python test.py -v
    ```

Podemos observar la ejecución del test avanzado:

!!! info "" 
    ```
    Trying:
        l = [1, 2, 3, 4, 5]
    Expecting nothing
    ok
    Trying:
        doblar(l)
    Expecting:
        [2, 4, 6, 8, 10]
    ok
    Trying:
        l = []
    Expecting nothing
    ok
    Trying:
        for i in range(10):
            l.append(i)
    Expecting nothing
    ok
    Trying:
        doblar(l)
    Expecting:
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
    5 tests in __main__.doblar
    5 tests in 2 items.
    5 passed and 0 failed.
    Test passed.
    ```

Por último vamos a volver a nuestra función suma para tratar excepciones dentro de los tests.

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        Pueden ser números:
        
        >>> suma(5,10)
        15
        
        >>> suma(-5,7)
        2
        
        Cadenas de texto:
        
        >>> suma('aa','bb')
        'aabb'
        
        O listas:
        
        >>> a = [1, 2, 3]
        >>> b = [4, 5, 6]
        >>> suma(a,b)
        [1, 2, 3, 4, 5, 6]
        """
        return a+b
    ```

Ahora sabemos que no podemos sumar tipos distintos, ¿cómo podemos tenerlo en cuenta en un test?

Pues por ahora podemos suponer un resultado y comprobar el resultado cuando falle:

!!! info "" 
    ```
    >>> suma(10,"hola")
    "10hola"
    ```

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        Pueden ser números:
        
        >>> suma(5,10)
        15
        
        >>> suma(-5,7)
        2
        
        Cadenas de texto:
        
        >>> suma('aa','bb')
        'aabb'
        
        O listas:
        
        >>> a = [1, 2, 3]
        >>> b = [4, 5, 6]
        >>> suma(a,b)
        [1, 2, 3, 4, 5, 6]
        
        Sin embargo no podemos sumar elementos de tipos diferentes:
        
        >>> suma(10,"hola")
        "10hola"
        """
        return a+b
    ```

Si ejecutamos el script monitorizando todo:

!!! info "" 
    ```bash
    python test.py -v
    ```

Podemos observar el fallo:

!!! info "" 
    ```
    Trying:
        suma(5,10)
    Expecting:
        15
    ok
    Trying:
        suma(-5,7)
    Expecting:
        2
    ok
    Trying:
        suma('aa','bb')
    Expecting:
        'aabb'
    ok
    Trying:
        a = [1, 2, 3]
    Expecting nothing
    ok
    Trying:
        b = [4, 5, 6]
    Expecting nothing
    ok
    Trying:
        suma(a,b)
    Expecting:
        [1, 2, 3, 4, 5, 6]
    ok
    Trying:
        suma(10,"hola")
    Expecting:
        "10hola"
    **********************************************************************
    File "test.py", line 26, in __main__.suma
    Failed example:
        suma(10,"hola")
    Exception raised:
        Traceback (most recent call last):
        File "C:\Program Files\Anaconda3\lib\doctest.py", line 1321, in __run
            compileflags, 1), test.globs)
        File "<doctest __main__.suma[6]>", line 1, in <module>
            suma(10,"hola")
        File "test.py", line 29, in suma
            return a+b
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    1 items had no tests:
        __main__
    **********************************************************************
    1 items had failures:
    1 of   7 in __main__.suma
    7 tests in 2 items.
    6 passed and 1 failed.
    ***Test Failed*** 1 failures.
    ```

Concretamente debemos fijarnos en la primera línea y última de la excepción:

!!! info "" 
    ```
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ```

Y precisamente esto es lo que tenemos que indicar en el test:

!!! info "" 
    ```python
    def suma(a, b):
        """Esta función recibe dos parámetros y devuelve la suma de ambos
        
        Pueden ser números:
        
        >>> suma(5,10)
        15
        
        >>> suma(-5,7)
        2
        
        Cadenas de texto:
        
        >>> suma('aa','bb')
        'aabb'
        
        O listas:
        
        >>> a = [1, 2, 3]
        >>> b = [4, 5, 6]
        >>> suma(a,b)
        [1, 2, 3, 4, 5, 6]
        
        Sin embargo no podemos sumar elementos de tipos diferentes:
        
        >>> suma(10,"hola")
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
        """
        return a+b
    ```

___
<small class="edited"><i>Última edición: 6 de Octubre de 2018</i></small>