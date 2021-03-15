title: Métodos de las listas | Curso de Python | Hektor Profe
description: Ahora que conocemos los objetos y tenemos una idea más clara de cómo funciona Python, es un buen momento para revisitar las colecciones y aprender algunos de sus métodos de clase.

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

# Métodos de las listas

## append()

Añade un ítem al final de la lista:

!!! info ""
    
    ```python
    lista = [1,2,3,4,5]
    lista.append(6)
    lista
    ```

    ```
    [1, 2, 3, 4, 5, 6]
    ```

## clear()

Vacía todos los ítems de una lista:

!!! info ""
    
    ```python
    lista.clear()
    lista
    ```

    ```
    []
    ```   

## extend()

Une una lista a otra:

!!! info ""
    
    ```python
    l1 = [1,2,3]
    l2 = [4,5,6]
    l1.extend(l2)
    l1
    ```

    ```
    [1, 2, 3, 4, 5, 6]
    ```

## count()

Cuenta el número de veces que aparece un ítem:

!!! info ""
    
    ```python
    ["Hola", "mundo", "mundo"].count("Hola")
    ```

    ```
    1
    ```

## index()

Devuelve el índice en el que aparece un ítem (error si no aparece):


!!! info ""
    
    ```python
    ["Hola", "mundo", "mundo"].index("mundo")
    ```

    ```
    1
    ```

## insert()

Agrega un ítem a la lista en un índice específico:

Primera posición (0):

!!! info ""
    
    ```python
    l = [1,2,3]
    l.insert(0,0)
    l
    ```

    ```
    [0, 1, 2, 3]
    ```

Penúltima posición (-1):

!!! info ""
    
    ```python
    l = [5,10,15,25]
    l.insert(-1,20) 
    l
    ```

    ```
    [5, 10, 15, 20, 25]
    ```

Última posición en una lista con len():

!!! info ""
    
    ```python
    l = [5,10,15,25]
    n = len(l)
    l.insert(n,30)
    l
    ```

    ```
    [5, 10, 15, 20, 25, 30]
    ```

Una posición fuera de rango añade el elemento al final de la lista (999):

!!! info ""
    
    ```python
    l.insert(999, 35)
    l
    ```

    ```
    [5, 10, 15, 20, 25, 30, 35]
    ```

## pop()

Extrae un ítem de la lista y lo borra:

!!! info ""
    
    ```python
    l = [10,20,30,40,50]
    print(l.pop())
    print(l)
    ```

    ```
    50
    [10, 20, 30, 40]
    ```

Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):

!!! info ""
    
    ```python
    print(l.pop(0))
    print(l)
    ```

    ```
    10
    [20, 30, 40]
    ```

## remove()

Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:

!!! info ""
    
    ```python
    l = [20,30,30,30,40]
    l.remove(30)
    print(l)
    ```

    ```
    [20, 30, 30, 40]
    ```

## reverse()

Le da la vuelta a la lista actual:

!!! info ""
    
    ```python
    l.reverse()
    print(l)
    ```

    ```
    [40, 30, 30, 20]
    ```

Las cadenas no tienen el método *.reverse()* pero podemos simularlo haciendo unas conversiones:

!!! info ""
    
    ```python
    lista = list("Hola mundo")
    lista.reverse()
    cadena = "".join(lista)
    cadena    
    ```

    ```
    'odnum aloH'
    ```


## sort()

Ordena automáticamente los ítems de una lista por su valor de menor a mayor:

!!! info ""
    
    ```python
    lista = [5,-10,35,0,-65,100]
    lista.sort()
    lista
    ```

    ```
    [-65, -10, 0, 5, 35, 100]
    ```

Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:

!!! info ""
    
    ```python
    lista.sort(reverse=True)
    lista
    ```

    ```
    [100, 35, 5, 0, -10, -65]
    ```

___
<small class="edited"><i>Última edición: 1 de Octubre de 2018</i></small>