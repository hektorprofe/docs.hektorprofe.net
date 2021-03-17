title: Función map() | Curso de Python | Hektor Profe
description: Operadores encadenados, comprensión de listas, funciones decoradoras, generadoras, iteradoras, lambda y expresiones regulares.

# Función map()

Esta función trabaja de una forma muy similar a **filter()**, con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map:

!!! info "" 
    
    ```python
    def doblar(numero):
        return numero*2
        
    numeros = [2, 5, 10, 23, 50, 33]

    map(doblar, numeros)
    ```

    ```
    <map at 0x212eb6e0748>
    ```

Fácilmente podemos transformar este iterable en una lista:

!!! info "" 
    
    ```python
    list(map(doblar, numeros))
    ```

    ```
    [4, 10, 20, 46, 100, 66]
    ```

Y podemos simplificarlo con una función lambda para substituir la llamada de una función definida:

!!! info "" 
    
    ```python
    list( map(lambda x: x*2, numeros) )
    ```

    ```
    [4, 10, 20, 46, 100, 66]
    ```

La función **map()** se utiliza mucho junto a expresiones lambda ya que permite ahorrarnos el esfuerzo de crear bucles for.

Además se puede utilizar sobre más de un iterable con la condición que tengan la misma longitud. 

Por ejemplo si queremos multiplicar los números de dos listas:

!!! info "" 
    
    ```python
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    list( map(lambda x,y : x*y, a,b) )
    ```

    ```
    [7, 9, 11, 13, 15]
    ```

E incluso podemos extender la funcionalidad a tres listas o más:

!!! info "" 
    
    ```python
    c = [11, 12, 13, 14, 15]

    list( map(lambda x,y,z : x*y*z, a,b,c) )
    ```

    ```
    [66, 168, 312, 504, 750]
    ```

## Mapeando objetos

Evidentemente, siempre que la utilicemos correctamente podemos mapear una serie de objetos sin ningún problema:

!!! info "" 
    
    ```python
    def incrementar(p):
        p.edad += 1
        return p

    personas = map(incrementar, personas)

    for persona in personas:
        print(persona)
    ```

    ```
    Juan de 36 años
    Marta de 17 años
    Manuel de 79 años
    Eduardo de 13 años
    ```

Claro que en este caso tenemos que utilizar una función definida porque no necesitamos actuar sobre la instancia, a no ser que nos tomemos la molestia de rehacer todo el objeto:

!!! info "" 
    
    ```python
    personas = [
        Persona("Juan", 35),
        Persona("Marta", 16),
        Persona("Manuel", 78),
        Persona("Eduardo", 12)
    ]

    personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)

    for persona in personas:
        print(persona)
    ```

    ```
    Juan de 36 años
    Marta de 17 años
    Manuel de 79 años
    Eduardo de 13 años
    ```

___
<small class="edited"><i>Última edición: 6 de Octubre de 2018</i></small>