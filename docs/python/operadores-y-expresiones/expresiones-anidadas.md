title: Expresiones anidadas | Curso de Python | Hektor Profe
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

# Expresiones anidadas

Se pueden solucionar empleando las reglas de precedencia:

1. Primero los paréntesis que indican prioridad.
2. Segundo, las expresiones aritméticas por sus propias reglas.
3. Tercero, las expresiones relacionales.
4. Cuarto, las expresiones lógicas.

!!! info "" 
    
    ```python
    a = 10
    b = 5

    a * b - 2**b >= 20 and not (a % b) != 0
    ```

    ```
    False
    ``` 

___
<small class="edited"><i>Última edición: 21 de Septiembre de 2018</i></small>