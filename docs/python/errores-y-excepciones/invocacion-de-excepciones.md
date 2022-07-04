title: Invocación de excepciones | Curso de Python | Hektor Profe
description: En algunas ocasiones nuestros programas pueden fallar ocasionando su detención. Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos momentos y tratarlos debidamente para prevenirlos.

# Invocación de excepciones

En algunas ocasiones quizá nos interesa llamar un error manualmente, ya que un *print* común no es muy elegante:

!!! info "" 
    
    ```python
    def mi_funcion(algo=None):
        if algo is None:
            print("Error! No se permite un valor nulo (con un print)")
            
    mi_funcion()
    ```

    ```
    Error! No se permite un valor nulo (con un print)
    ``` 

## Instrucción raise

Gracias a *raise* podemos lanzar un error manual pasándole el identificador. Luego simplemente podemos añadir un *except* para tratar esta excepción que hemos lanzado:

!!! info "" 
    
    ```python
    def mi_funcion(algo=None):
        try:
            if algo is None:
                raise ValueError("Error! No se permite un valor nulo")
        except ValueError:
            print("Error! No se permite un valor nulo (desde la excepción)")

    mi_funcion()
    ```

    ```
    Error! No se permite un valor nulo (desde la excepción)
    ``` 

___
<small class="edited"><i>Última edición: 26 de Septiembre de 2018</i></small>