title: Módulo math | Curso de Python | Hektor Profe
description: Los módulos son ficheros que contienen definiciones que se pueden importar en otros scripts para reutilizar sus funcionalidades.

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

# Módulo math

Este módulo contiene un buen puñado de funciones para manejar números, hacer redondeos, sumatorios precisos, truncamientos... además de constantes. 

## Redondeos

!!! info "" 
    ```python
    import math

    print(math.floor(3.99))  # Redondeo a la baja (suelo)
    print(math.ceil(3.01))   # Redondeo al alta (techo)
    ```

    ```
    3
    4
    ```

## Sumatorio mejorado

!!! info "" 
    ```python
    numeros = [0.9999999, 1, 2, 3])
    math.fsum(numeros) 
    ```

    ```
    6.9999999
    ```

## Trucamiento

!!! info "" 
    ```python
    math.trunc(123.45)
    ```

    ```
    123
    ```

## Potencias y raices

!!! info "" 
    ```python
    math.pow(2, 3)  # Potencia con flotante 
    math.sqrt(9)    # Raíz cuadrada (square root)
    ```

    ```
    8.0
    3.0
    ```

## Constantes

!!! info "" 
    ```python
    print(math.pi)  # Constante pi
    print(math.e)   # Constante e
    ```

    ```
    3.141592653589793
    2.718281828459045
    ```

___
<small class="edited"><i>Última edición: 2 de Octubre de 2018</i></small>