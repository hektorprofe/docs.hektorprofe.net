title: Envío de valores | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.

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

# Envío de valores

Para comunicarse con el exterior las funciones no sólo pueden devolver valores, también pueden recibir información:

!!! info "" 

    ```python
    def suma(a, b):  # valores que se reciben
        return a + b
    ```

    ```
    Una cadena
    20
    [1, 2, 3]
    ```

Ahora podemos enviar dos valores a la función:

!!! info "" 

    ```python
    resultado = suma(2, 5)  # valores que se envían
    print(resultado)
    ```

    ```
    7
    ```

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>