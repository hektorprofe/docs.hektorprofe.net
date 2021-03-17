title: Pydoc | Curso de Python | Hektor Profe
description: En esta sección repasamos los módulos Docstring, Pydoc, Doctest y Unittest de Python.

# Pydoc

En la lección anterior aprendimos que utilizando la función **help** podemos mostrar información formateada por la consola. Pues en realidad esta función hace uso del módulo **pydoc** para generar la documentación a partir de sus *docstrings*.

Desde la terminal no podemos utilizar la función *help*, pero sí existe la posibilidad de utilizar **pydoc** de forma similar.

Por ejemplo podemos consultar la documentación de scripts, módulos y clases utilizando la sintaxis:

!!! info "" 
    ```bash
    pydoc nombre.py
    ```

También podemos utilizar la misma sintaxis para los paquetes:

!!! info "" 
    ```bash
    pydoc nombre_paquete
    ```

## Documentación HTML

Una función interesante de Pydoc es que podemos generar la documentación de nuestro código utilizando la siguiente sintaxis:

!!! info "" 
    ```bash
    pydoc -w nombre.py
    ```

Si tenemos un paquete podemos generar toda la documentación de forma recursiva de la siguiente forma estando en el directorio del paquete:

!!! info "" 
    ```bash
    pydoc -w .\  # En MAC y Linux con la barra normal ./
    ```

O haciendo referencia al paquete:

!!! info "" 
    ```bash
    pydoc -w mi_paquete .\  # En MAC y Linux con la barra normal ./
    ```

Esto generará toda la documentación del paquete, subpaquete, clases, métodos y funciones. Está bien para publicarla en Internet, pero también podemos consultarla directamente en local lanzando un servidor temporal, desde el directorio del paquete:

!!! info "" 
    ```bash
    pydoc -p 8000
    ```

Aunque esto mostrará la documentación general de Python en ese momento, a parte de nuestro módulo.

___
<small class="edited"><i>Última edición: 6 de Octubre de 2018</i></small>