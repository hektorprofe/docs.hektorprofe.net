title: Ejercicios « Controlando el flujo | Curso de Python | Hektor Profe
description: Si un programa sólo ejecutara instrucciones planas estaríamos muy limitado, por eso existen las condiciones y los bucles.

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

# Ejercicios « Controlando el flujo

## Ejercicio 1

Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

* Mostrar una suma de los dos números
* Mostrar una resta de los dos números (el primero menos el segundo)
* Mostrar una multiplicación de los dos números

En caso de introducir una opción inválida, el programa informará de que no es correcta.

## Ejercicio 2

Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

## Ejercicio 3

Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

!!! hint "Sugerencia"
    Puedes utilizar la funciones *sum()* y *range()* para hacerlo más fácil.<br>
    El tercer parámetro en la función *range(inicio, fin, salto)* indica un salto de números, pruébalo.

## Ejercicio 4

Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

## Ejercicio 5

Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

!!! info "Concepto útil"
    La sintaxis _**[valor] in [lista]**_ permite comprobar si un valor se encuentra en una lista (devuelve *True* o *False*).


## Ejercicio 6

Utilizando la función *range()* y la conversión a listas genera las siguientes listas dinámicamente:

* Todos los números del 0 al 10 [0, 1, 2, ..., 10]
* Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
* Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
* Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
* Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

!!! info "Concepto útil"
    Se pueden generar saltos en el _**range()**_ estableciendo su tercer parámetro  _**range(inicio, fin, salto)**_, experimenta.


## Ejercicio 7

Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

!!! info "" 
    
    ```python
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

    # Completa el ejercicio aquí
    ```

## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.udemy.com/course/python-3-al-completo-desde-cero/?referralCode=11428CACE5771408E4D5)</u>.

___
<small class="edited"><i>Última edición: 22 de Septiembre de 2018</i></small>