title: Entrada por teclado | Curso de Python | Hektor Profe
description: En esta sección aprenderemos sobre las distintas formas de leer y visualizar información.

# Entrada por teclado

Ya conocemos la función *input()* que lee una cadena por teclado. Su único inconveniente es que debemos transformar el valor a numérico si deseamos hacer operaciones con él:

!!! info "" 
    
    ```python
    decimal = float( input("Introduce un número decimal con punto: ") )
    ```

    ```
    Introduce un número decimal con punto: 3.14
    ```

Una forma interesante de leer varios valores es almacenar los datos en una lista e irlos añadiendo ahí para poderlos manipular en grupo:

!!! info "" 
    
    ```python
    valores = []
    print("Introduce 3 valores")
    for x in range(3):
        valores.append( input("Introduce un valor: ") )
    print(valores)
    ```

    ```
    Introduce 3 valores
    Introduce un valor: 10
    Introduce un valor: sdkjsdk
    Introduce un valor: skdjs
    ['10', 'sdkjsdk', 'skdjs']
    ```

Por ahora no hay mucho más que comentar sobre las entradas en tiempo de ejecución. También es posible leer datos de ficheros pero eso es algo que veremos más adelante.

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>