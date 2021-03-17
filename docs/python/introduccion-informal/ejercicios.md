title: Ejercicios « Introducción informal | Curso de Python | Hektor Profe
description: En la programación todo se resume a datos que representan información. Números, textos, fechas, imágenes, sonidos, vídeos... todo son datos.

# Ejercicios « Introducción informal

## Ejercicio 1

Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:

!!! info "" 
    
    ```python
    "Hola Mundo"     
    [1, 10, 100]      
    -25              
    1.167             
    ["Hola", "Mundo"] 
    ' '    
    ```

## Ejercicio 2

Determina mentalmente (sin programar) el resultado que aparecerá por pantalla en las siguientes operaciones con variables:

!!! info "" 
    
    ```python
    a = 10
    b = -5
    c = "Hola "
    d = [1, 2, 3] 

    print(a * 5)
    print(a - b)
    print(c + "Mundo")
    print(c * 2)
    print(d[-1])
    print(d[1:])
    print(d + d)   
    ```

## Ejercicio 3

El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

!!! info "" 
    
    ```python
    numero_1 = 9
    numero_2 = 3
    numero_3 = 6

    media = numero_1 + numero_2 + numero_3 / 3
    print("La nota media es", media)
    ```

## Ejercicio 4

A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

* La primera nota vale un 15% del total
* La segunda nota vale un 35% del total
* La tercera nota vale un 50% del total

Desarrolla un programa para calcular perfectamente la nota final:

!!! info "" 
    
    ```python
    nota_1 = 10
    nota_2 = 7
    nota_3 = 4

    # Completa el ejercicio aquí
    ```

## Ejercicio 5

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

!!! tip "Ayuda"
    La función llamada *sum(lista)* devuelve una suma de todos los elementos de la lista ¡Pruébalo!

!!! info "" 
    
    ```python
    matriz = [ 
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13]
    ]

    # Completa el ejercicio aquí
    ```

## Ejercicio 6

Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

> ***Nombre*** ***Apellido*** ha sacado un ***Nota*** de nota.

!!! tip "Ayuda"
    Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: **cadena[::-1]**

!!! info "" 
    
    ```python
    cadena = "zeréP nauJ,01"

    # Completa el ejercicio aquí
    ```
    
## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.udemy.com/course/python-3-al-completo-desde-cero/?referralCode=11428CACE5771408E4D5)</u>.

___
<small class="edited"><i>Última edición: 20 de Septiembre de 2018</i></small>