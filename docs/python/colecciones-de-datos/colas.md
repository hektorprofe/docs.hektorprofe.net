title: Colas | Curso de Python | Hektor Profe
description: Python integra un montón de colecciones para manejar datos. Ya conocemos las listas pero hay otros tipos que sirven para cubrir otras necesidades.

# Colas

Son colecciones de elementos ordenados que únicamente permiten dos acciones:

* Añadir un elemento a la cola.
* Sacar un elemento de la cola.

La peculiaridad es que el primer elemento en entrar es el primero en salir. En inglés se conocen como estructuras *FIFO (First In First Out)*.

Debemos importar la colección *deque* manualmente para crear una cola:

!!! info "" 

    ```python
    from collections import deque
    cola = deque()
    print(cola)
    ```

    ```
    deque([])
    ```

Podemos añadir elementos al crear la cola pasándolos en una lista:

!!! info "" 

    ```python
    cola = deque(['Hector','Juan','Miguel'])
    print(cola)
    ```

    ```
    deque(['Hector', 'Juan', 'Miguel'])
    ```

Luego podemos seguir añadiéndolos utilizando el método *append()*:

!!! info "" 

    ```python
    cola.append('Maria')
    cola.append('Arnaldo')
    print(cola)
    ```

    ```
    deque(['Hector', 'Juan', 'Miguel', 'Maria', 'Arnaldo'])
    ```

La parte interesante es a la hora de sacar los elementos, pues en esta ocasión utilizaremos el método *popleft()*. Hace lo mismo que *pop()* pero los extrae por la parte izquierda, que sería el principio de la cola:

!!! info "" 

    ```python
    print(cola.popleft())
    print(cola)
    ```

    ```
    'Hector'
    deque(['Juan', 'Miguel', 'Maria', 'Arnaldo'])
    ```

Además al igual que antes debemos asegurarnos de almacenar los elementos al sacarlos o los perderemos:

!!! info "" 

    ```python
    persona = cola.popleft()
    print(persona)
    print(cola)
    ```

    ```
    'Juan'
    deque(['Miguel', 'Maria', 'Arnaldo'])
    ```
___
<small class="edited"><i>Última edición: 23 de Septiembre de 2018</i></small>