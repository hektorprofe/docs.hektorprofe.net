title: Retorno de valores | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.

<style>

.admonition.note > .superfences-tabs > label:hover, .headerlink{
    color: #018dc5 !important;
}

.admonition.info{
    font-size: 100%;
}

.admonition.info label{
    font-size: 91%;
}

.admonition.note > .admonition-title {
    display: none;
}

</style>

# Retorno de valores

Para comunicarse con el exterior, las funciones pueden devolver valores al proceso principal gracias a la instrucción **return**. 

En el momento de devolver un valor, la ejecución de la función finalizará:

!!! info "" 

    ```python
    def test():
        return "Una cadena retornada"

    test()
    ```

    ```
    'Una cadena retornada'
    ```

Los valores devueltos se tratan como valores literales directos del tipo de dato retornado:

!!! info "" 

    ```python
    print(test())
    ```

    ```
    Una cadena retornada
    ```

Por ejemplo no podemos sumar una cadena con un número:

!!! info "" 

    ```python
    c = test() + 10
    ```

    ```
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-6-0ac9d7015445> in <module>()
    ----> 1 c = test() + 10

    TypeError: Can't convert 'int' object to str implicitly
    ```

También podemos devolver cualquier tipo de colección y manejarla directamente:

!!! info "" 

    ```python
    def test():
        return [1,2,3,4,5]

    print(test())
    print(test()[-1])
    print(test()[1:4])
    ```

    ```
    [1, 2, 3, 4, 5]
    5
    [2, 3, 4]
    ```

Evidentemente es posible asignar el valor retornado a una variable:

!!! info "" 

    ```python
    lista = test()
    print(lista[-1])
    ```

    ```
    5
    ```

## Retorno múltiple

Una característica interesante, es la posibilidad de devolver múltiples valores separados por comas:

!!! info "" 

    ```python
    def test():
        return "Una cadena", 20, [1,2,3]

    test()
    ```

    ```
    ('Una cadena', 20, [1, 2, 3])
    ```

Estos valores se tratan en conjunto como una tupla inmutable y se pueden reasignar a distintas variables:

!!! info "" 

    ```python
    cadena, numero, lista = test()

    print(cadena)
    print(numero)
    print(lista)
    ```

    ```
    Una cadena
    20
    [1, 2, 3]
    ```

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>