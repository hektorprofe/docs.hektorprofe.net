title: Ejercicios « Programación de funciones | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.


# Ejercicios « Programación de funciones

## Ejercicio 1

Realiza una función llamada **area_rectangulo(base, altura)** que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:

!!! info "Recordatorio"
    El área de un rectángulo se obtiene al multiplicar la base por la altura.

## Ejercicio 2

Realiza una función llamada **area_circulo(radio)** que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

!!! info "Recordatorio"
    El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

    !!! info "" 
    
    ```python
    import math

    print(math.pi)
    ```

    ```python 
    3.141592653589793
    ```

## Ejercicio 3

Realiza una función llamada **relacion(a, b)** que a partir de dos números cumpla lo siguiente:

* Si el primer número es mayor que el segundo, debe devolver 1.
* Si el primer número es menor que el segundo, debe devolver -1.
* Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

## Ejercicio 4

Realiza una función llamada **intermedio(a, b)** que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

!!! info "Recordatorio"
    El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

## Ejercicio 5

Realiza una función llamada **recortar(numero, minimo, maximo)** que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

* Devolver el límite inferior si el número es menor que éste
* Devolver el límite superior si el número es mayor que éste.
* Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10.

## Ejercicio 6

Realiza una función **separar(lista)** que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares. 

Por ejemplo:

!!! info "" 
    
    ```python
    pares, impares = separar([6,5,2,1,7])
    print(pares)
    print(impares)
    ```

    ```
    [2, 6]
    [1, 5, 7]
    ``` 

!!! tip "Sugerencia"
    Para ordenar una lista automáticamente puedes utilizar el método *.sort()*.

## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.hektorprofe.net/cupon/python)</u>.

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>