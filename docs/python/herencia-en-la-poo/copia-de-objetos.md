title: Copia de objetos | Curso de Python | Hektor Profe
description: En esta unidad veremos en qué consiste eso de la herencia y cómo aprovecharla para ahorrarnos muchísimas líneas de código.

# Copia de objetos

De la misma forma que las colecciones, los objetos se pasan a las funciones por referencia. Si modificamos sus valores dentro, éstos se verán reflejados fuera.

Esto también afecta a la hora de hacer copias, creándose en su lugar un acceso al objeto en lugar de uno nuevo con sus valores:

!!! info "" 
    
    ```python
    class Test:
        pass

    test1 = Test()
    test2 = test1

    test1.algo = "Prueba"

    print(test2 == test1)  # ¿Son el mismo objeto?

    try:
        print(test2.algo)
    except Exception as e:
        print(e)
    ```

    ```
    True
    Prueba
    ```

Para realizar una copia a partir de sus valores podemos utilizar la función *copy* del módulo con el mismo nombre:

!!! info "" 
    ```python
    from copy import copy

    class Test:
        pass

    test1 = Test()
    test2 = copy(test1)

    test1.algo = "Prueba"

    print(test2 == test1)  # ¿Son el mismo objeto?

    try:
        print(test2.algo)
    except Exception as e:
        print(e)
    ```

    ```
    False
    'Test' object has no attribute 'algo'
    ```

La función *copy* se puede utilizar también para copiar colecciones:

!!! info "" 
    ```python
    from copy import copy

    lista1 = [1,2,3]
    lista2 = copy(lista1)
    lista1 = None

    print(lista1)
    print(lista2)
    ```

    ```
    None
    [1, 2, 3]
    ```

___
<small class="edited"><i>Última edición: 29 de Septiembre de 2018</i></small>