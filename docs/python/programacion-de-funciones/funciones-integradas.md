title: Funciones integradas | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.

# Funciones integradas

La librería estándar de Python incluye muchas funciones. Las hay para hacer conversiones entre tipos, matemáticas, utilidades... 

Aquí un resumen de las más utilizadas incluyendo algunas que ya conocemos:

## int()

Transforma una cadena a un entero (si no es posible da error):

!!! info "" 

    ```python
    n = int("10")
    print(n)
    ```

    ```
    10
    ```
    
## float()

Transforma una cadena a un flotante (si no es posible da error):

!!! info "" 

    ```python
    f = float("10.5")
    print(f)
    ```

    ```
    10.5
    ``` 

## str()

Transforma cualquier valor a una cadena:

!!! info "" 

    ```python
    c = "Un texto y dos números " + str(10) + " y " + str(3.14)
    print(c)
    ```

    ```
    Un texto y dos números 10 y 3.14
    ``` 

## bin()

Conversión de entero a binario:

!!! info "" 

    ```python
    bin(10)
    ```

    ```
    '0b1010'
    ``` 

## hex()

Conversión de entero a hexadecimal:

!!! info "" 

    ```python
    hex(10)
    ```

    ```
    '0xa'
    ``` 

## int(numero, base)

Reconversión a entero (base 10):

!!! info "" 

    ```python
    print(int('0b1010', 2))
    print(int('0xa', 16))
    ```

    ```
    10
    10
    ``` 

## abs()

Valor absoluto de un número (distancia):

!!! info "" 

    ```python
    abs(-10)
    ```

    ```
    10
    ``` 
    
## round()

Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza:

!!! info "" 

    ```python
    print(round(5.5))
    print(round(5.4))
    ```

    ```
    6
    5
    ``` 

## eval()

Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente:

!!! info "" 

    ```python
    eval('2 + 5')
    ```

    ```
    7
    ``` 
    
!!! info "" 

    ```python
    n = 10
    eval('n * 10 - 5')
    ```

    ```
    95
    ``` 

## len()

Longitud de una colección o cadena:

!!! info "" 

    ```python
    print(len("Una cadena"))
    print(len([]))
    ```

    ```
    10
    0
    ``` 

## help()

Invoca el menú de ayuda del intérprete de Python:

!!! info "" 

    ```python
    help()
    ```

    ```
    Welcome to Python 3.6's help utility!
    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.
    ....
    ```

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>