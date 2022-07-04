title: Listas | Curso de Python | Hektor Profe
description: En la programación todo se resume a datos que representan información. Números, textos, fechas, imágenes, sonidos, vídeos... todo son datos.

# Listas

Las listas se tratan  de un tipo compuesto de dato que puede almacenar distintos valores (llamados ítems o elementos) ordenados entre [ ] y separados con comas:

!!! info "" 
    
    ```python
    numeros = [1,2,3,4]
    numeros
    ```

    ```
    [1, 2, 3, 4]
    ```

## Índices y slicing

Funcionan de una forma muy similar a las cadenas de caracteres:

!!! info "" 
    
    ```python
    datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]

    print(datos[0])
    print(datos[-1])
    print(datos[2:])
    ```

    ```
    4
    Otra cadena
    [-15, 3.14, 'Otra cadena']
    ```

## Suma de listas

Da como resultado una nueva lista que incluye todos los ítems:

!!! info "" 
    
    ```python
    numeros + [5,6,7,8]
    ```

    ```
    [1, 2, 3, 4, 5, 6, 7, 8]
    ```

## Mutabilidad

A diferencia de las cadenas, en las listas sí podemos modificar sus ítems utilizando índices:

!!! info "" 
    
    ```python
    pares = [0,2,4,5,8,10]
    pares[3] = 6
    pares
    ```

    ```
    [0, 2, 4, 6, 8, 10]
    ```

Integran funcionalidades internas como el método *.append()* para añadir un ítem al final de la lista:

!!! info "" 
    
    ```python
    pares.append(12)
    pares.append(7*2)
    pares
    ```

    ```
    [0, 2, 4, 6, 8, 10, 12, 14]
    ```

Y una peculiaridad es que también aceptan asignación con slicing para modificar varios ítems en conjunto:

!!! info "" 
    
    ```python
    letras = ['a','b','c','d','e','f']
    letras[:3]
    ```

    ```
    ['a', 'b', 'c']
    ```

!!! info "" 
    
    ```python
    letras[:3] = ['A','B','C']
    letras
    ```

    ```
    ['A', 'B', 'C', 'd', 'e', 'f']
    ```

Asignar una lista vacía equivale a borrar los ítems de la lista o sublista:

!!! info "" 
    
    ```python
    letras[:3] = []
    letras
    ```

    ```
    ['d', 'e', 'f']
    ```

!!! info "" 
    
    ```python
    letras = []
    letras
    ```

    ```
    []
    ```

La función *len()* funciona con las listas del mismo modo que en las cadenas:

!!! info "" 
    
    ```python
    print(len(letras))
    print(len(pares))
    ```

    ```
    0
    8
    ```

## Listas anidadas

Podemos manipular fácilmente este tipo de estructuras utilizando múltiples índices, como si nos refieréramos a las filas y columnas de una tabla:

!!! info "" 
    
    ```python
    a = [1,2,3]
    b = [4,5,6]
    c = [7,8,9]
    r = [a,b,c]

    r
    ```

    ```
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ```

!!! info "" 
    
    ```python
    print(r[0])       # Primera sublista
    print(r[-1])      # Última sublista

    print(r[0][0])    # Primera sublista, y de ella, primer ítem
    print(r[1][1])    # Segunda sublista, y de ella, segundo ítem
    print(r[2][2])    # Tercera sublista, y de ella, tercer ítem
    print(r[-1][-1])  # Última sublista, y de ella, último ítem
    ```

    ```
    [1, 2, 3]
    [7, 8, 9]

    1
    5
    9
    9
    ```

___
<small class="edited"><i>Última edición: 20 de Septiembre de 2018</i></small>