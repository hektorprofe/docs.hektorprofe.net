title: Números | Curso de Python | Hektor Profe
description: En la programación todo se resume a datos que representan información. Números, textos, fechas, imágenes, sonidos, vídeos... todo son datos.

# Números

Para empezar lo más sencillo es utilizar el intérprete de Python como una calculadora:

!!! info ""
    
    ```python
    3 + 2
    ```

    ```
    5
    ``` 

!!! info "" 
    
    ```python
    3 - 2
    ```

    ```
    1
    ```     

!!! info "" 
    
    ```python
    3 * 2
    ```

    ```
    6
    ```  

Podemos utilizar comentarios # para explicar lo que hace nuestro código:

!!! info "" 
    
    ```python
    # División
    3 / 2
    ```

    ```
    1.5
    ```  

!!! info "" 
    
    ```python
    # Módulo
    3 % 2
    ```

    ```
    1
    ```  

!!! info "" 
    
    ```python
    # Potencia
    3 ** 2
    ```

    ```
    9
    ```  

Podemos distinguir 2 tipos de números:

* **Enteros**: Que no tienen una parte decimal y van desde menos infinito a más infinito.
* **Flotantes** o decimales: Números que tienen una parte decimal escrita con un punto.

!!! info "" 
    
    ```python
    # Número entero
    1
    ```

    ```
    1
    ```  

!!! info "" 
    
    ```python
    # Número flotante
    323239829389.238273283
    ```

    ```
    323239829389.2383
    ```  

También podemos realizar operaciones más complejas. Python interpretará automáticamente las prioridades de los operadores:

!!! info "" 
    
    ```python
    3 - 2 + 4 * 10
    ```

    ```
    41
    ```  

## Variables

Este es el concepto más importante en la programación, así que asegúrate de entenderlo bien practicando mucho.

!!! tip "Concepto fundamental"
    Una variable es un identificador que representa un espacio en la memoria. A este espacio se le puede asignar un valor para utilizarlo posteriormente como si se tratase de un valor literal, incluso se puede operar con otras variables y reasignarle otro valor en cualquier momento.

Asignación de un valor a la  variable 'n':

!!! info "" 
    
    ```python
    n = 3
    n
    ```

    ```
    3
    ```  

Suma de una variable entera con un literal número entero:

!!! info "" 
    
    ```python
    n + 3
    ```

    ```
    6
    ```  

Producto de una variable entera con un literal número entero:

!!! info "" 
    
    ```python
    n * 2
    ```

    ```
    6
    ``` 

Producto de una variable entera con un literal número entero:

!!! info "" 
    
    ```python
    n * n
    ```

    ```
    9
    ``` 

Suma de dos variables enteras:

!!! info "" 
    
    ```python
    # Creamos otra variable
    m = 10

    n + m
    ```

    ```
    13
    ``` 

Producto de dos variables y suma de un literal numérico:

!!! info "" 
    
    ```python
    n * m + 10
    ```

    ```
    40
    ``` 

Reasignación de los valores y cálculo de nuevo resultado:

!!! info "" 
    
    ```python
    n = 10
    m = 15

    n + m
    ```

    ```
    25
    ``` 
    
Asignación del valor de una variable a otra:

!!! info "" 
    
    ```python
    n = m
    n
    ```

    ```
    15
    ```

Incluso se puede asignar una operación mezclada:

!!! info "" 
    
    ```python
    n = m + 10
    n
    ```

    ```
    25
    ```

O el propio valor sumado con un literal:

!!! info "" 
    
    ```python
    n = n + 25
    n
    ```

    ```
    50
    ```

## Reutilización

Al crear una estructura de cálculos con variables podemos fácilmente adaptar sus valores para hacer distintas comprobaciones:

!!! info "" 
    
    ```python
    nota_1 = 2
    nota_2 = 5
    nota_media = (nota_1 + nota_2) / 2

    nota_media
    ```

    ```
    3.5
    ```

___
<small class="edited"><i>Última edición: 20 de Septiembre de 2018</i></small>