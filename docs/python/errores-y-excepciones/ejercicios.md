title: Ejercicios « Errores y excepciones | Curso de Python | Hektor Profe
description: En algunas ocasiones nuestros programas pueden fallar ocasionando su detención. Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos momentos y tratarlos debidamente para prevenirlos.

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

# Ejercicios « Errores y excepciones 

## Ejercicio 1

Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

!!! info "" 
    
    ```python
    resultado = 10/0
    ```

## Ejercicio 2

Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

!!! info "" 
    
    ```python
    lista = [1, 2, 3, 4, 5]
    lista[10]
    ```

## Ejercicio 3 

Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

!!! info "" 
    
    ```python
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
    ```

## Ejercicio 4 

Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

!!! info "" 
    
    ```python
    resultado = 15 + "20"
    ```

## Ejercicio 5

Realiza una función llamada **agregar_una_vez(lista, el)** que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo *ValueError* que debes capturar y mostrar este mensaje en su lugar:

!!! info "" 
    
    ```
    Error: Imposible añadir elementos duplicados => [elemento].
    ```

Cuando tengas la función intenta añadir los siguiente valores a la lista **10, -2, "Hola"** y luego muestra su contenido.

!!! info "Sugerencia"
    Puedes utilizar la sintaxis "elemento in lista"

!!! info "" 
    
    ```python
    elementos = [1, 5, -2]

    # Completa el ejercicio aquí
    ```

## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.udemy.com/course/python-3-al-completo-desde-cero/?referralCode=11428CACE5771408E4D5)</u>.
    
___
<small class="edited"><i>Última edición: 26 de Septiembre de 2018</i></small>