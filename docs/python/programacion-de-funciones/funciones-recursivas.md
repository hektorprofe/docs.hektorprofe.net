title: Funciones recursivas | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.

# Funciones recursivas

Se trata de funciones que se llaman a sí mismas durante su propia ejecución. Funcionan de forma similar a las iteraciones, pero debemos encargarnos de planificar el momento en que dejan de llamarse a sí mismas o tendremos una función rescursiva infinita.

Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

## Ejemplo sin retorno

Cuenta regresiva hasta cero a partir de un número:

!!! info "" 

    ```python
    def cuenta_atras(num):
        num -= 1
        if num > 0:
            print(num)
            cuenta_atras(num)
        else:
            print("Boooooooom!")
        print("Fin de la función", num)

    cuenta_atras(5)
    ```

    ```
    4
    3
    2
    1
    Boooooooom!
    Fin de la función 0
    Fin de la función 1
    Fin de la función 2
    Fin de la función 3
    Fin de la función 4
    ``` 

## Ejemplo con retorno

El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad de este tipo de funciones:

* 3! = 1 x 2 x 3 = 6
* 5! = 1 x 2 x 3 x 4 x 5 = 120

!!! info "" 

    ```python
    def factorial(num):
        print("Valor inicial ->",num)
        if num > 1:
            num = num * factorial(num -1)
        print("valor final ->",num)
        return num

    print(factorial(5))
    ```

    ```
    Valor inicial -> 5
    Valor inicial -> 4
    Valor inicial -> 3
    Valor inicial -> 2
    Valor inicial -> 1
    valor final -> 1
    valor final -> 2
    valor final -> 6
    valor final -> 24
    valor final -> 120

    120
    ``` 

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>