title: Métodos de los diccionarios | Curso de Python | Hektor Profe
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

# Métodos de los diccionarios

!!! info ""

    ```python
    colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
    ```

## get()

Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:

!!! info ""
    
    ```python
    colores.get('negro','no se encuentra')
    ```

    ```
    'no se encuentra'
    ```

## keys()

Genera una lista en clave de los registros del diccionario:

!!! info ""
    
    ```python
    colores.keys()
    ```

    ```
    dict_keys(['amarillo', 'azul', 'verde'])
    ```
    
## values()

Genera una lista en valor de los registros del diccionario:

!!! info ""
    
    ```python
    colores.values()
    ```

    ```
    dict_values(['yellow', 'blue', 'green'])
    ```

## items()

Genera una lista en clave-valor de los registros del diccionario:

!!! info ""
    
    ```python
    colores.items()
    ```

    ```
    dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
    ```

!!! info ""
    
    ```python
    for clave, valor in colores.items():
        print(clave, valor)
    ```

    ```
    amarillo yellow
    azul blue
    verde green
    ```  

## pop()

Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:

!!! info ""
    
    ```python
    colores.pop("amarillo", "no se ha encontrado")
    ```

    ```
    'yellow'
    ```  

!!! info ""
    
    ```python
    colores.pop("negro","no se ha encontrado")
    ```

    ```
    'no se ha encontrado'
    ```  

## clear()

Borra todos los registros de un diccionario:

!!! info ""
    
    ```python
    colores.clear()
    colores
    ```

    ```
    {}
    ```  

___
<small class="edited"><i>Última edición: 1 de Octubre de 2018</i></small>