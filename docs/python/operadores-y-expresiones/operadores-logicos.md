title: Operadores lógicos | Curso de Python | Hektor Profe
description: Sabemos que la programación gira en torno a la información, en torno a los datos, ¿pero con qué propósito?

# Operadores lógicos

Encontramos 3 operadores especiales para realizar operaciones lógicas. Normalmente se utilizan para agrupar, excluir y negar expresiones. Puede ayudar echar un vistazo a [esta explicación](https://es.wikipedia.org/wiki/Tabla_de_verdad) sobre las tablas de la verdad:

* Not
* And
* Or

## Not (Negación lógica)

Niega un valor o expresión lógica:

!!! info "" 
    
    ```python
    not True
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    not False
    ```

    ```
    True
    ``` 

!!! info "" 
    
    ```python
    not True == False
    ```

    ```
    True
    ``` 

## And (Conjunción lógica)

Devuelve verdadero sólo si se cumplen todas las condiciones:

!!! info "" 
    
    ```python
    True and True
    ```

    ```
    True
    ``` 

!!! info "" 
    
    ```python
    True and False
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    False and True
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    False and False
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    Fa = 45
    a > 10 and a < 20
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    c = "Hola Mundo"
    len(c) >= 20 and c[0] == "H"
    ```

    ```
    False
    ``` 

## Or (Disyunción lógica)

Devuelve verdadero si se cumple como mínimo una condición:

!!! info "" 
    
    ```python
    True or True
    ```

    ```
    True
    ``` 

!!! info "" 
    
    ```python
    True or False
    ```

    ```
    True
    ``` 

!!! info "" 
    
    ```python
    False or True
    ```

    ```
    True
    ``` 

!!! info "" 
    
    ```python
    False or False
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    c = "OTRA COSA"
    c == "EXIT" or c == "FIN" or c == "SALIR"
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    c = "Lector"
    c[0] == "H" or c[0] == "h"
    ```

    ```
    False
    ```

___
<small class="edited"><i>Última edición: 21 de Septiembre de 2018</i></small>