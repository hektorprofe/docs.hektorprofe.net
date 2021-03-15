title: Operadores relacionales | Curso de Python | Hektor Profe
description: Sabemos que la programación gira en torno a la información, en torno a los datos, ¿pero con qué propósito?

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

# Operadores relacionales

Sirven para comparar dos valores, dependiendo del resultado de la comparación se devolverá:

* Verdadero (True), si es cierta
* Falso (False), si no es cierta

## Igual que

!!! info "" 
    
    ```python
    3 == 2
    ```

    ```
    False
    ```  

## Distinto de

!!! info "" 
    
    ```python
    3 != 2 
    ```

    ```
    True
    ```  

## Mayor que

!!! info "" 
    
    ```python
    3 > 2
    ```

    ```
    True
    ```  

## Menor que

!!! info "" 
    
    ```python
    3 < 2
    ```

    ```
    False
    ```  

## Mayor o igual que

!!! info "" 
    
    ```python
    3 >= 4
    ```

    ```
    False
    ```   

## Menor o igual que

!!! info "" 
    
    ```python
    3 <= 4
    ```

    ```
    True
    ```  

También podemos comparar variables:

!!! info "" 
    
    ```python
    a = 10
    b = 5

    a > b
    ```

    ```
    True
    ```  

!!! info "" 
    
    ```python
    b != a
    ```

    ```
    True
    ```  

!!! info "" 
    
    ```python
    a == b*2
    ```

    ```
    True
    ```  

Y otros tipos, como cadenas, listas, el resultado de algunas funciones o los propios tipos lógicos:

!!! info "" 
    
    ```python
    "Hola" == "Hola"
    ```

    ```
    True
    ```  

!!! info "" 
    
    ```python
    "Hola" != "Hola"
    ```

    ```
    False
    ``` 

!!! info "" 
    
    ```python
    c = "Hola"
    c[0] == "H"
    ```

    ```
    True
    ```  

!!! info "" 
    
    ```python
    c = "Hola"
    c[-1] == "a"
    ```

    ```
    True
    ```  

!!! info "" 
    
    ```python
    l1 = [0,1,2]
    l2 = [2,3,4]

    l1 == l2 
    ```

    ```
    False
    ```  

!!! info "" 
    
    ```python
    len(l1) == len(l2)
    ```

    ```
    True
    ```

!!! info "" 
    
    ```python
    l1[-1] == l2[0]
    ```

    ```
    True
    ```

!!! info "" 
    
    ```python
    True == True
    ```

    ```
    True
    ```

!!! info "" 
    
    ```python
    False == True
    ```

    ```
    False
    ```

!!! info "" 
    
    ```python
    False != True
    ```

    ```
    True
    ```

!!! info "" 
    
    ```python
    True > False
    ```

    ```
    True
    ```

!!! info "" 
    
    ```python
    False > True
    ```

    ```
    False
    ```

La representación aritmética de *True* y *False* equivale a 1 y 0 respectivamente:

!!! info "" 
    
    ```python
    True * 3
    ```

    ```
    3
    ``` 

!!! info "" 
    
    ```python
    False / 5
    ```

    ```
    0.0
    ``` 

!!! info "" 
    
    ```python
    True * False
    ```

    ```
    0
    ``` 

___
<small class="edited"><i>Última edición: 21 de Septiembre de 2018</i></small>