title: Ejercicios « Métodos de las colecciones | Curso de Python | Hektor Profe
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

# Ejercicios « Métodos de las colecciones

## Ejercicio 1

Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

```
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
```

En este otro:

```
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
```

**Lo único prohibido es modificar directamente el texto.**

## Ejercicio 2

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

* Borrar los elementos duplicados.
* Ordenar la lista de mayor a menor.
* Eliminar todos los números impares.
* Realizar una suma de todos los números que quedan.
* Añadir como primer elemento de la lista la suma realizada.
* Devolver la lista modificada.
* Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:

!!! info ""
    
    ```python
    nueva_lista = modificar(lista)
    print( nueva_lista[0] == sum(nueva_lista[1:]) )
    ```

    ```
    True
    ```  

!!! Tip "Recordatorio" 
    La función *sum(lista)* devuelve una suma de los elementos de una lista.
    
## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.udemy.com/course/python-3-al-completo-desde-cero/?referralCode=11428CACE5771408E4D5)</u>.
___
<small class="edited"><i>Última edición: 1 de Octubre de 2018</i></small>