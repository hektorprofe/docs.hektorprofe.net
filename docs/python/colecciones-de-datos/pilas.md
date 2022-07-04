title: Pilas | Curso de Python | Hektor Profe
description: Python integra un montón de colecciones para manejar datos. Ya conocemos las listas pero hay otros tipos que sirven para cubrir otras necesidades.

# Pilas

Son colecciones de elementos ordenados que únicamente permiten dos acciones:

* Añadir un elemento a la pila.
* Sacar un elemento de la pila.

La peculiaridad es que el último elemento en entrar es el primero en salir. En inglés se conocen como estructuras *LIFO (Last In First Out)*.

Las podemos crear como listas normales y añadir elementos al final con el *append()*:

!!! info "" 

    ```python
    pila = [3,4,5]
    pila.append(6)
    pila.append(7)
    print(pila)
    ```

    ```
    [3, 4, 5, 6, 7]
    ```

Para sacar los elementos utilizaremos el método *pop()*. Al utilizareste método devolveremos el último elemento, pero también lo borraremos:

!!! info "" 

    ```python
    print(pila.pop())
    print(pila)
    ```

    ```
    7
    [3, 4, 5, 6]
    ```
Si queremos trabajar con él deberíamos asignarlo a una variable:

!!! info "" 

    ```python
    numero = pila.pop()
    print(numero)
    ```

    ```
    6
    ```

Si vamos sacando elementos llegará un momento en que la pila estará vacía y dará error porque no podrá sacar nada más:

!!! info "" 

    ```python
    pila.pop()
    pila.pop()
    pila.pop()
    pila.pop()
    ```

    ```
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-14-3900970cfbef> in <module>()
    ----> 1 pila.pop()
    IndexError: pop from empty list
    ```

___
<small class="edited"><i>Última edición: 23 de Septiembre de 2018</i></small>