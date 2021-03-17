title: Cadenas de texto | Curso de Python | Hektor Profe
description: En la programación todo se resume a datos que representan información. Números, textos, fechas, imágenes, sonidos, vídeos... todo son datos.

# Cadenas de texto

Inmediatamente después de los números hay que echar un vistazo a las cadenas de texto, a fin de cuentas es la forma como las personas nos comunicamos de forma escrita. Las letras o caracteres son en definitiva símbolos de escritura y otro tipo de dato esencial. 

Siempre se definen entre comillas simples o dobles:

!!! info ""
    ```python
    'Hola Mundo'
    ```
    ```
    'Hola Mundo'
    ```

!!! info ""
    ```python 
    "Hola Mundo"
    ```
    ```
    'Hola Mundo'
    ```

Es posible poner comillas dobles en una cadena de comillas simples:

!!! info ""
    ```python 
    'Este texto incluye unas " "'
    ```
    ```
    'Este texto incluye unas " "'
    ```

Comillas simples en una cadena de comillas dobles:

!!! info "" 
    
    ```python
    "Esta 'palabra' se encuentra escrita entre comillas simples"
    ```

    ```
    "Esta 'palabra' se encuentra escrita entre comillas simples"
    ```

O también utilizar el carácter de escape \ para poner comillas del mismo tipo:

!!! info "" 
    
    ```python
    "Esta \"palabra\" se encuentra escrita entre comillas dobles"
    ```

    ```
    'Esta "palabra" se encuentra escrita entre comillas dobles'
    ```

!!! info "" 
    
    ```python
    'Esta \'palabra\' se encuentra escrita entre comillas simples'
    ```

    ```
    "Esta 'palabra' se encuentra escrita entre comillas simples"
    ```

## La función print()

Es una instrucción que nos permite mostrar correctamente el valor de una cadena (u otros valores/variables) por pantalla:

!!! info "" 
    
    ```python
    "Una cadena"
    'otra cadena'
    'otra cadena más'
    ```

    ```
    'otra cadena más'
    ```

!!! info "" 
    
    ```python
    print("Una cadena")
    print('otra cadena')
    print('otra cadena más')
    ```

    ```
    Una cadena
    otra cadena
    otra cadena más
    ```

Acepta caracteres especiales como las tabulaciones \t o los saltos de línea \n:

!!! info "" 
    
    ```python
    print("Un texto\tuna tabulación")
    ```

    ```
    Un texto    una tabulación
    ```

!!! info "" 
    
    ```python
    print("Un texto\nuna nueva línea")
    ```

    ```
    Un texto
    una nueva línea
    ```

Para evitar los caracteres especiales, debemos indicar que una cadena es cruda (raw):

!!! info "" 
    
    ```python
    print("C:\nombre\directorio")
    ```

    ```
    C:
    ombre\directorio
    ```

!!! info "" 
    
    ```python
    print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)
    ```

    ```
    C:\nombre\directorio
    ```

Podemos utilizar """ *(triple comillas)* para cadenas multilínea:

!!! info "" 
    
    ```python
    print("""Una línea
    otra línea
    otra línea\tuna tabulación""")
    ```

    ```
    Una línea
    otra línea
    otra línea  una tabulación
    ```

También es posible asignar cadenas a variables. La forma correcta de mostrarlas es con la instrucción *print()*:

!!! info "" 
    
    ```python
    c = "Esto es una cadena\ncon dos líneas"
    c
    ```

    ```
    'Esto es una cadena\ncon dos líneas'
    ```

!!! info "" 
    
    ```python
    c = "Esto es una cadena\ncon dos líneas"
    print(c)
    ```

    ```
    Esto es una cadena
    con dos líneas
    ```

## Operaciones

Una de las operaciones de las cadenas es la concatenación (o suma de cadenas):

!!! info "" 
    
    ```python
    c = "Esto es una cadena\ncon dos líneas"
    c + c
    ```

    ```
    'Esto es una cadena\ncon dos líneasEsto es una cadena\ncon dos líneas'
    ```

!!! info "" 
    
    ```python
    c = "Esto es una cadena\ncon dos líneas"
    print(c+c)
    ```

    ```
    Esto es una cadena
    con dos líneasEsto es una cadena
    con dos líneas
    ```

!!! info "" 
    
    ```python
    s = "Una cadena" " compuesta de dos cadenas"
    print(s)
    ```

    ```
    Una cadena compuesta de dos cadenas
    ```

!!! info "" 
    
    ```python
    c1 = "Una cadena"
    c2 = "otra cadena"
    print("Una cadena " + c2)
    ```

    ```
    Una cadena otra cadena
    ```

También es posible utilizar la multiplicación de cadenas:

!!! info "" 
    
    ```python
    diez_espacios = " " * 10
    print(diez_espacios + "un texto a diez espacios")
    ```

    ```
              un texto a diez espacios
    ```

## Índices en las cadenas

Los índices nos permiten posicionarnos en un carácter específico de una cadena.

Representan un número [índice], que empezando por el 0 indica el carácter de la primera posición, y así sucesivamente:

!!! info "" 
    
    ```python
    palabra = "Python"
    palabra[0] # carácter en la posición 0
    ```

    ```
    'P'
    ```

!!! info "" 
    
    ```python
    palabra[3]
    ```

    ```
    'h'
    ```

El índice negativo -1, hace referencia al carácter de la última posición, el -2 al penúltimo y así sucesivamente:

!!! info "" 
    
    ```python
    palabra[-1]
    ```

    ```
    'n'
    ```

!!! info "" 
    
    ```python
    print(palabra[-0]) 
    print(palabra[-2])
    print(palabra[-6])
    ```

    ```
    P
    o
    P
    ```

## Slicing en las cadenas

El slicing es una capacidad de las cadenas que devuelve un subconjunto o subcadena utilizando dos índices [inicio:fin]:

* El primer índice indica donde empieza la subcadena (se incluye el carácter).
* El segundo índice indica donde acaba la subcadena (se excluye el carácter).

!!! info "" 
    
    ```python
    palabra = "Python"
    palabra[0:2]
    ```

    ```
    'Py'
    ```

!!! info "" 
    
    ```python
    palabra[2:]
    ```

    ```
    'thon'
    ```

!!! info "" 
    
    ```python
    palabra[-2:]
    ```

    ```
    'on'
    ```

Si en el slicing no se indica un índice se toma por defecto el principio y el final:

!!! info "" 
    
    ```python
    palabra[:2]
    ```

    ```
    'Py'
    ```

!!! info "" 
    
    ```python
    palabra[2:]
    ```

    ```
    'thon'
    ```

!!! info "" 
    
    ```python
    palabra[:]
    ```

    ```
    'Python'
    ```

!!! info "" 
    
    ```python
    palabra[:2] + palabra[2:]
    ```

    ```
    'Python'
    ```

Si un índice se encuentra fuera del rango de la cadena, dará error:

!!! info "" 
    
    ```python
    palabra[99]
    ```

    ```
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-47-b31ddef6ab27> in <module>()
    ----> 1 palabra[99]
    IndexError: string index out of range
    ```

Pero con slicing esto no pasa y simplemente se ignora el espacio hueco:

!!! info "" 
    
    ```python
    palabra[:99]
    ```

    ```
    'Python'
    ```

!!! info "" 
    
    ```python
    palabra[99:]
    ```

    ```
    ''
    ```

## Inmutabilidad

Una propiedad de las cadenas es que no se puede modificar su contenido. Si intentamos reasignar un carácter, no nos dejará:

!!! info "" 
    
    ```python
    palabra[0] = "N"
    ```

    ```
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-51-c87a9e773639> in <module>()
    ----> 1 palabra[0] = "N"
    TypeError: 'str' object does not support item assignment
    ```

Sin embargo, utilizando slicing y concatenación podemos generar nuevas cadenas fácilmente:

!!! info "" 
    
    ```python
    palabra = "N" + palabra[1:]
    palabra
    ```

    ```
    'Nython'
    ```

## Funciones

Un ejemplo de función útil que soportan las cadenas es *len()*, que nos permite saber su longitud (el número de caracteres que contienen):

!!! info "" 
    
    ```python
    palabra = "Python"
    len(palabra)
    ```

    ```
    6
    ```

Hay más funciones, pero las iremos descubriendo a lo largo del curso.

___
<small class="edited"><i>Última edición: 20 de Septiembre de 2018</i></small>