title: Lectura por teclado | Curso de Python | Hektor Profe
description: En la programación todo se resume a datos que representan información. Números, textos, fechas, imágenes, sonidos, vídeos... todo son datos.

# Lectura por teclado

Una forma de trabajar con datos dinámicos es a través del teclado con la instrucción *input()* que lee y devuelve una cadena:

!!! info "" 
    
    ```python
    valor = input()
    valor
    ```

    ```
    > algo
    'algo'
    ```

Aunque introduzcamos un número, en realidad es una cadena de texto:

!!! info "" 
    
    ```python
    valor = input("Introduce un valor: ")  # Podemos mostrar un mensaje
    valor
    ```

    ```
    Introduce un valor: 100
    '100'
    ```

Una cadena y un número no se pueden operar, dará error:

!!! info "" 
    
    ```python
    valor = input("Introduce un número entero: ")
    valor + 50  
    ```

    ```
    Introduce un número entero: 100
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-6-5071d551e583> in <module>()
    ----> 1 valor + 100
    TypeError: Can't convert 'int' object to str implicitly
    ```

Tenemos que utilizar la función *int()* para transformar una variable cadena a entero:

!!! info "" 
    
    ```python
    valor = int(input("Introduce un número entero: "))
    valor * 2
    ```

    ```
    Introduce un número entero: 500
    1000
    ```

También tenemos la función *float()* que hace lo propio pero transformando la cadena a flotante: 

!!! info "" 
    
    ```python
    valor = float(input("Introduce un número entero o flotante: "))
    valor * 2
    ```

    ```
    Introduce un número entero o flotante: : 3.14
    6.28
    ```

___
<small class="edited"><i>Última edición: 20 de Septiembre de 2018</i></small>