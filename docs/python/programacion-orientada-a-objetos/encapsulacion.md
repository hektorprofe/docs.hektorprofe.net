title: Encapsulación | Curso de Python | Hektor Profe
description: En esta unidad aprenderemos sobre un paradigma de programación distinto que cambió la forma de entender la programación.

# Encapsulación

Finalmente para acabar la introducción vale la pena comentar esta "técnica". No es santo de mi devoción porque no le veo mucho sentido, pero si venís de otros lenguajes quizá os interesa conocerla.

La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior. En Python no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas __ como indicando que son "especiales".

En el caso de los atributos quedarían así:

!!! info ""

    ```python
    class Ejemplo:
        __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    e = Ejemplo()
    print(e.__atributo_privado)
    ```

    ``` 
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-3-eed1a613919b> in <module>()
    ----> 1 print(e.__atributo_privado)

    AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'
    ```

Y en los métodos...

!!! info ""

    ```python
    class Ejemplo:
        def __metodo_privado(self):
            print("Soy un método inalcanzable desde fuera.")

    e = Ejemplo()
    e.__metodo_privado()
    ```

    ``` 
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-5-81c514698440> in <module>()
    ----> 1 e.__metodo_privado()

    AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'
    ```

¿Qué sentido tiene esto en Python? Ninguno, porque se pierde toda la gracia de lo que en esencia es el lenguaje: flexibilidad y polimorfismo sin control (hablaremos de esto más adelante).

Sea como sea para acceder a esos datos se deberían crear métodos públicos que hagan de interfaz. En otros lenguajes les llamaríamos *getters* y *setters* y es lo que da lugar a las *propiedades*, que no son más que atributos protegidos con interfaces de acceso:

!!! info ""

    ```python
    class Ejemplo:
        __atributo_privado = "Soy un atributo inalcanzable desde fuera."
        
        def __metodo_privado(self):
            print("Soy un método inalcanzable desde fuera.")
            
        def atributo_publico(self):
            return self.__atributo_privado
            
        def metodo_publico(self):
            return self.__metodo_privado()

    e = Ejemplo()
    print(e.atributo_publico())
    e.metodo_publico()
    ```

    ``` 
    Soy un atributo inalcanzable desde fuera.
    Soy un método inalcanzable desde fuera.
    ```

___
<small class="edited"><i>Última edición: 27 de Septiembre de 2018</i></small>